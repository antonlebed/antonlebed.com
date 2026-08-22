"""THE PINNED COMPOSITE: what the intermediate class supplies.

THE QUESTION
------------
At a pinned chain the stepwise nesting argument is dead: freshening
the tree from a stall's own member leaves the class nesting nowhere
and improving nothing, at all three squaring-map stalls
(explore_pinned_telescope.py F4). Yet exactly one of the several
strictly improving classes at cure distance two DOES nest pointwise
against each stall, and the route to it is two tree freshenings with
the second taken from a DIFFERENT member of the intermediate class --
one carrying a different style pair, which the quotient supplies free.
So the derivation the reader corpus's open edge owes is not a stepwise
lemma but a two-move COMPOSITE, and its object is the intermediate
CLASS rather than either endpoint.

This rig is the composite's cheapest first probe. It does not attempt
the proof. It asks what the intermediate class IS: how many policies
it holds, what they share beyond the signature that defines them, and
which of them the second move can be taken from. The order matters --
asking what the members share before asking what the composite proves
is what keeps the derivation from being written about the wrong object.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves, quotient, the stall object
and the landscape evaluator are the parents' (explore_scale_clock.py,
explore_stall_tie.py, explore_stall_unresourced.py,
explore_stall_assembly.py, explore_shift_telescope.py,
explore_pinned_telescope.py). UNRESOURCED throughout: drawdown inert,
100 policies, counted window starting at step 8, quotient by counted
trace, cure neighbours, lexicographic deficit. The patience axis is
0, 1, 2, 3, INF, where 0 reads the current image and INF refuses the
reference entirely.

WHOSE VOCABULARY THIS IS WRITTEN IN
-----------------------------------
Not the telescopes'. "Delay", "freshening", "nesting" are statements
about a single run's cells against another single run's cells, and
both telescopes are written in them. The object here is a CLASS, and a
class is not a run: the quotient's signature is the tuple of counted
committed intervals and nothing else (explore_stall_tie.py run_pol --
sig = hash(counted), the counted window starting at step 8). So the
vocabulary this suspicion needs is the quotient's own: what a class
FIXES (its counted cells) against what it LEAVES FREE (the style pair,
the patience pair, and every step before the window). TRANSPLANT,
flagged: nothing about nesting is imported here at all, which is the
point -- F4 measured the first step failing to nest, so an argument
that starts from a nesting property of the first move is starting from
a refuted premise.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
Write a member as pi = (st, ss, pt, pc) with the drawdown inert. The
stall class s is a singleton {p0}, p0 = (st0, ss0, pt0, 0) with
pt0 in {3, 3, 2} at the three specimens. Move one is pt-down:
q = (st0, ss0, pt0 - 1, 0), lying in some class z distinct from s.
Move two is taken from a member r of z and lands in the escape class
t, which nests pointwise against s.

WHAT THE CLASS FIXES. Every member of z produces the SAME committed
interval at every counted step, by the definition of the signature.
That is the whole of what membership asserts, and it is an assertion
about steps 8 onward only.

WHAT THE CLASS LEAVES FREE, and it is three things, not one. (i) The
style pair: two members may differ in either preference bit or both.
(ii) The patience pair: the signature says nothing about where on the
patience square a member sits, so a class can collect several. (iii)
Every step before the window. Two members agreeing on all counted
cells may have reached them along different pre-window routes, and no
statement of the quotient's can see that.

WHY THE RE-SELECTION CANNOT BE INERT. The cure moves are typed
(explore_shift_telescope.py typed_moves): two route flips, the
preference diagonal, and four patience steps. A patience step cannot
touch a route preference. So if the escape class t is reached from
some r in z by a patience step, and t's own members carry a style pair
p0 does not, then no sequence of patience steps from p0 can reach t at
all and the re-selection is FORCED rather than convenient. That is an
argument about the move definition and it claims possibility, never a
count: how many classes the re-selection actually adds, and whether t
is among them, is what E2 prints.

WHAT A COMPOSITE WOULD HAVE TO ARGUE. If the members of z that reach t
are exactly those carrying one style pair, then the composite's
hypothesis is a statement about which style pairs a class HOLDS -- an
occupancy statement, provable or refutable by the quotient alone --
and the second move is then an ordinary freshening from a member whose
own nesting behaviour can be argued in the telescopes' vocabulary. If
instead the reaching members are spread across style pairs, the
occupancy route is closed and the composite must argue about the
pre-window states, which is the harder object and the one the quotient
was built to forget.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C0 [positive control, run first] The three squaring-map specimens
   reproduce as stalls, each a singleton class, at patiences (3,0),
   (3,0), (2,0); each keeps five, four and three strictly improving
   classes at cure distance two; and exactly one of those nests
   pointwise against the stall at each. A miss means the population is
   not the parents' and no verdict below is read (K1).
A1 [the size] For each first move out of the stall, the size of the
   class it lands in. GUESS, marked as a guess: the class carrying the
   escape holds more than one style pair and at least four members.
   That it holds more than one member is not a guess -- F4's route
   requires it -- and a singleton there is K2.
A2 [what the members share] Within the escape-carrying class: the
   style pairs present, the patience pairs present, and whether all
   members agree at EVERY step or only at the counted ones. GUESS:
   several patience pairs are present, and the members do NOT all
   agree pre-window -- the first disagreement sits strictly before
   step 8.
A3 [what the re-selection buys] From the first move's landing member q
   alone, the set of classes one typed move reaches; from all members
   of that class, the same set. Print both sizes and whether the
   escape class t sits in the first. GUESS: t is absent from the
   single-member set at all three specimens -- the re-selection is
   forced, not optional (K3 if present).
A4 [the composite's object] The members of the escape-carrying class
   from which some typed move reaches t, with the move types. GUESS:
   a proper nonempty subset, every one of them reaching t by pt-down,
   and membership determined by the style pair alone -- which is the
   occupancy route the hand-attack names as the cheap one.

FOLLOW-UP SLATE (frozen after E0-E3's first print and before the
amended run; no prediction above was touched)
----------------------------------------------------------------
K3 fired at all three specimens. The escape class holds the policy
reached by lowering the tree patience TWICE from the stall's own
member -- the same style pair throughout -- so the re-selection the
aim and the parent's F4 both assert is not needed anywhere, and A4's
"style-determined" answer is the degenerate one: every member of the
intermediate class reaches the escape, the stall's own descendant
included. That collapses the object. What is to be derived is not a
composite through a class but a TWO-STEP FRESHENING of a single
member, whose first step happens not to nest -- an object that lives
in the telescopes' vocabulary after all, one member and its cells.
Two questions follow, and neither was asked above.
B1 [the corrected statement, hard] At each specimen, with p0 the
   stall's member, q = pt-down(p0) and q2 = pt-down(q): q's class is
   distinct from the stall's, does NOT nest pointwise against it and
   does not strictly improve; q2's class DOES nest pointwise, DOES
   strictly improve, and IS the unique nesting escape E0 found.
   GUESS: all three specimens, every clause. A miss is K4.
B2 [does the two-step freshening reach past the specimens] Over the
   parents' census scope (horizons 9, 10, 12, 16; maps identity and
   doubling), take every present-pinned class and every member with
   the freshening move available twice, and record whether the
   twice-freshened policy's class nests pointwise against the class
   and strictly improves. Report it against the distance-one reach
   the parent measured, and separately for the classes that reach
   NOTHING at distance one -- the residue's residue, which the parent
   counts at 420, all of them doubling with the chain pinned.
   Controls: the parent's per-side class totals reproduce (identity
   2,546 tree-side; doubling 597 chain-side and 2,955 tree-side) and
   the distance-one misses reproduce 420 on the doubling tree side and
   zero elsewhere. GUESS, marked as a guess: the twice-freshened
   landing nests and improves for a majority of the present-pinned
   classes that have two freshenings to spend, and it reaches a strict
   majority of the 420.

KILL CRITERIA (observables; the meaning is weighed after the run)
----------------------------------------------------------------
K4 Any specimen where a clause of B1 fails. The corrected statement
   is wrong too, the escape is not the twice-freshening, and the rig
   prints the cells rather than a verdict.
K1 Any control count misses (stall reproduction, the singleton, the
   patience pair, the distance-two improving counts 5/4/3, the unique
   nesting escape). The population is not the parents' and nothing
   below is a verdict.
K2 The escape-carrying class is a singleton at any specimen. F4's
   "different member" is false as stated there and the composite has
   no re-selection in it.
K3 The escape class t is reachable by one typed move from the first
   move's own landing member q at any specimen. The re-selection is
   not forced there, the walk is a plain two-step patience walk, and
   the composite's stated object is wrong at that specimen.

ENGINE
------
E0 the control (C0), which also fixes the escape class t per specimen.
E1 the first moves out of the stall and the classes they land in (A1,
   A2).
E2 what the re-selection buys, per landing class (A3).
E3 the reaching members and what distinguishes them (A4).
E4 the two-step freshening at the three stalls (B1).
E5 the two-step freshening over the parents' census scope (B2).
Exact big-integer arithmetic for every verdict; floating point only in
printed logs. Sequential; estimated run a few minutes, the E5 census
the driver; memory trivial (no BLAS import); exit nonzero on any check
failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, 5.5 s,
15.3 MB peak under the memory watch)
----------------------------------------------------------------
F1 THE RE-SELECTION IS NOT NEEDED ANYWHERE, AND THE PARENT'S ROUTE
   SENTENCE ASSERTS A NECESSITY THAT IS FALSE. K3 fires at all three specimens. At the two
   census specimens the stall is (1,0,3,0) and the unique nesting
   escape class is {(0,0,1,0), (1,0,1,0)}; at the designed specimen
   the stall is (0,1,2,0) and the escape class holds twenty members,
   (0,1,0,0) among them. So lowering the tree patience twice from the
   stall's OWN member -- (1,0,3,0) -> (1,0,2,0) -> (1,0,1,0), and
   (0,1,2,0) -> (0,1,1,0) -> (0,1,0,0) -- lands in the escape, with
   the style pair never changing. A4's style-determination question
   gets the degenerate answer: 2 of 2, 2 of 2 and 18 of 18 members of
   the intermediate class reach the escape, the stall's own descendant
   included, so no subset is singled out and no occupancy statement is
   available to be made. What the re-selection buys is real -- from the
   landing member alone one typed move reaches 4, 4 and 4 classes
   against 5, 5 and 7 from the whole class -- but the escape is not
   what it buys: the escape sits inside the SMALLER set at all three,
   so it is reachable with no re-selection spent. Reachable WITH one
   too, and that is the distinction the parent's sentence lost: the
   route it describes exists, and the necessity it claims for it does
   not. The parent's F4 sentence -- the second freshening taken from
   a different member, the quotient supplying the re-selection free --
   was INFERRED from the intermediate class holding a second style
   pair and never measured; its route printer collected move-type
   pairs over every member and never reported which member paid.
F2 THE INTERMEDIATE CLASS, MEASURED. Sizes 2, 2 and 18. At the two
   census specimens it carries a single patience pair (2,0) at two
   style pairs, so A1's guess of four or more members and A2's guess
   of several patience pairs both fail there; at the designed
   specimen it carries all four style pairs and five patience pairs
   (1,0), (1,1), (1,2), (1,3), (1,INF), where both hold. A2's
   pre-window half holds everywhere it can: against the stall's own
   descendant, the other members first differ at step 3, step 3 and
   step 4 -- strictly before the counted window opens at step 8 --
   except one member at the designed specimen that agrees at every
   step. So the quotient's blindness is real and it is pre-window, but
   it is not what the escape rides on.
F3 THE CORRECTED STATEMENT HOLDS AT ALL THREE (B1, hard). One
   freshening leaves the stall's class and neither nests nor improves;
   two freshenings nest pointwise, strictly improve, and land in the
   unique nesting escape. K4 does not fire. The non-monotonicity F4
   found is therefore a property of ONE member's walk, not of a route
   through a class.
F4 THE RESIDUE'S RESIDUE CLOSES, AND IT CLOSES AT DISTANCE TWO.
   Over the parents' census scope: identity tree-side 2,546 classes,
   all reaching at distance one; doubling chain-side 597, all at
   distance one; doubling tree-side 2,955 = 2,535 at distance one plus
   420 reaching nothing there -- and the twice-freshened landing
   reaches ALL 420. So every present-pinned class in the census scope
   reaches a pointwise-nested strictly improving class within two
   freshenings taken from a SINGLE member, with no re-selection
   anywhere. B2's guess is wrong in both directions and the second
   error is a question mismatch rather than a miss: the 420 leg is not
   a strict majority but all of it, while the twice-freshened reach
   over all classes is a minority (734 of 2,546 identity tree-side,
   1,279 of 2,955 doubling tree-side, and 0 of 597 doubling chain-side)
   because a class that already exits at distance one has its second
   freshening walk PAST the exit. The distance-two leg is a statement
   about the classes that need it.
   THE DISTANCE LABELS ARE THIS RIG'S OWN, and the audit is what made
   them so. Every recorded exit sits at exactly one freshening (5,678
   class-sides, no other value) and no walk freezes, so "distance one"
   is measured here rather than inherited from the parent. And the
   two-step leg REQUIRES an intermediate class distinct from BOTH
   endpoints, and neither half is free. 5,327 present-pinned member
   walks across the census have their first freshening stay inside the
   start class, so their second freshening is a distance-ONE move
   counted twice; and a second freshening can also land back in the
   intermediate class, which is again distance one. Imposing both
   leaves the 420 untouched -- for them the intermediate cannot qualify,
   having no nesting improving exit by hypothesis -- and costs the
   all-classes figures the doubling chain side entirely.
F5 WHAT THE DERIVATION NOW OWES, AND IT IS SMALLER THAN THE AIM SAID.
   The object is one member and its cells, and the once-failing case
   is the HYPOTHESIS rather than a second conclusion -- E5 refutes the
   universal reading outright, the twice-freshened landing nesting and
   improving for a minority of classes overall. The statement to prove:
   at a present-pinned class where NO member's single freshening lands
   nested and strictly improving, some member's SECOND freshening does,
   the two steps taken from that one member. The
   quotient, the intermediate class and the free re-selection all drop
   out of the statement, and what is left is written in the
   telescopes' own vocabulary -- one run's cells against another's,
   which is the vocabulary both parents' lemmas are proved in.

THE VERDICT. The aim was written about the wrong object, and the
correction shrinks the owe rather than growing it. There is no
composite through a class here: at all three squaring-map stalls the
radius-two escape is two tree freshenings of the stall's own member,
same style pair throughout, and the free re-selection the corpus
credited it to is never spent. What survives from the parent, and is
the whole of what makes this hard, is the non-monotonicity: the first
freshening nests nowhere and improves nothing, so no stepwise argument
reaches the escape and the two-step landing has to be argued directly.
And the reach is no longer three specimens: every present-pinned class
in the parents' census scope is covered at distance one or two by
freshening alone (F4), the 420 that distance one could not reach
included, which turns the stalls from an exception into the specimen
case of a rule stated over the whole residue.

Run record. ONE engine, three runs. The first ran E0-E3; K3 fired at
all three specimens and the follow-up slate above was frozen before
the amended run, with no prediction, control or finding touched. The
second added E4 and E5 under that slate. The third re-scoped one check
in E2 that had wired a GUESS as a hard assertion -- the parent
telescope's own recorded trap, repeated here -- so the K3 firing is
reported as the verdict it is rather than as a rig failure; the
observable and every count are unchanged. A FOURTH run was added by the
audit, which asked whether this rig measures the distances it labels or
inherits them: it did inherit them, and the two checks added at that
question found 5,327 members whose first freshening stays in class, so
E5's two-step leg now REQUIRES a distinct intermediate class. The 420
and every reproduction control are unchanged by it; the all-classes
twice-freshened figures in F4 are the tightened ones. No prediction, no
control and no finding above F4 was touched. Final run ALL CHECKS PASS,
exit 0, 5.5 s.
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
EXPECT_ESC = {"census-2313..": 5, "census-3212..": 4, "designed-16": 3}

def fmt4(p):
    return "(%d,%d,%s,%s)" % (
        p[0], p[1],
        "INF" if p[2] is None else str(p[2]),
        "INF" if p[3] is None else str(p[3]))

def all_cells(J, policy, horizon):
    """Committed intervals at EVERY step, counted and pre-window."""
    tr = SC.run_reader(J, policy[:4], horizon)[3]
    return [tr[n][2] for n in range(horizon)]

def first_diff(J, a, b, horizon):
    """First step at which two members' committed cells differ, or
    None if the two runs agree at every step."""
    ca, cb = all_cells(J, a, horizon), all_cells(J, b, horizon)
    for n in range(horizon):
        if ca[n] != cb[n]:
            return n
    return None

# ----------------------------------------------------------------- #
# E0: the control, and the escape class per specimen
# ----------------------------------------------------------------- #

def e0_control():
    print("\nE0  THE CONTROL (the parents' stalls and their escapes)")
    seen = {}
    for tag, digs, horizon in TS.SQ_SPECIMENS:
        ev = SA.evaluate(list(digs), "sq", horizon)
        if not ev["stalls"]:
            check("%s reproduces as a stall" % tag, False)
            continue
        sig_of = {p: s for s, ps in ev["mem"].items() for p in ps}
        qloss = ev["qloss"]
        for s in ev["stalls"]:
            mem = ev["mem"][s]
            Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
            pats = sorted({(p[2], p[3]) for p in mem})
            esc = set()
            for p in mem:
                for _t1, q in TS.typed_moves(p):
                    z = sig_of[q]
                    if z == s:
                        continue
                    for r in ev["mem"][z]:
                        for _t2, q2 in TS.typed_moves(r):
                            w = sig_of[q2]
                            if w in (s, z) or qloss[w][1][2]:
                                continue
                            if Fraction(qloss[w][1][0],
                                        qloss[w][1][1]) < Lx:
                                esc.add(w)
            check("%s singleton stall at patience %s"
                  % (tag, (EXPECT_PATIENCE[tag],)),
                  len(mem) == 1 and pats == [EXPECT_PATIENCE[tag]])
            check("%s keeps %d distance-2 improving classes"
                  % (tag, EXPECT_ESC[tag]), len(esc) == EXPECT_ESC[tag])
            p0 = sorted(mem, key=SC.pol_key)[0]
            cx = TS.counted_cells(ev["J"], p0, horizon)
            nesting = []
            for w in esc:
                rep = sorted(ev["mem"][w], key=SC.pol_key)[0]
                if TS.nests_pointwise(TS.counted_cells(ev["J"], rep,
                                                       horizon), cx):
                    nesting.append(w)
            check("%s: exactly one distance-2 improving class nests"
                  % tag, len(nesting) == 1)
            if len(nesting) != 1:
                continue
            t = nesting[0]
            print("    %s: stall %s, escape class members %s"
                  % (tag, fmt4(p0),
                     " ".join(fmt4(r) for r in
                              sorted(ev["mem"][t], key=SC.pol_key))))
            seen[tag] = (ev, horizon, s, p0, esc, t, sig_of)
    return seen

# ----------------------------------------------------------------- #
# E1: the first moves and the classes they land in
# ----------------------------------------------------------------- #

def e1_landing(seen):
    print("\nE1  THE FIRST MOVES AND WHERE THEY LAND")
    land = {}
    for tag in sorted(seen):
        ev, horizon, s, p0, _esc, _t, sig_of = seen[tag]
        print("  %s: from %s" % (tag, fmt4(p0)))
        byz = {}
        for ty, q in TS.typed_moves(p0):
            z = sig_of[q]
            if z == s:
                print("    %-9s -> in class (no move)" % ty)
                continue
            byz.setdefault(z, []).append((ty, q))
        for z, moves in sorted(byz.items(),
                               key=lambda kv: ev["qranks"][kv[0]]):
            mem = sorted(ev["mem"][z], key=SC.pol_key)
            styles = sorted({(r[0], r[1]) for r in mem})
            pats = sorted({(r[2], r[3]) for r in mem},
                          key=lambda a: (99 if a[0] is None else a[0],
                                         99 if a[1] is None else a[1]))
            q = moves[0][1]
            diffs = [(r, first_diff(ev["J"], q, r, horizon))
                     for r in mem if r != q]
            pre = [d for _r, d in diffs
                   if d is not None and d < SC.N0]
            same = [r for r, d in diffs if d is None]
            print("    %-24s -> class of %d member(s), styles %s, "
                  "patiences %s"
                  % ("/".join(ty for ty, _q in moves), len(mem),
                     styles, pats))
            print("        vs %s: %d member(s) agree at every step, "
                  "%d first differ pre-window, first-diff steps %s"
                  % (fmt4(q), len(same), len(pre),
                     sorted(set(d for _r, d in diffs
                                if d is not None))))
            land.setdefault(tag, []).append((z, moves, mem))
    return land

# ----------------------------------------------------------------- #
# E2: what the re-selection buys
# ----------------------------------------------------------------- #

def e2_reselection(seen, land):
    print("\nE2  WHAT THE RE-SELECTION BUYS")
    for tag in sorted(seen):
        ev, horizon, s, p0, _esc, t, sig_of = seen[tag]
        for z, moves, mem in land.get(tag, []):
            q = moves[0][1]
            from_q = {sig_of[q2] for _ty, q2 in TS.typed_moves(q)}
            from_z = set()
            for r in mem:
                for _ty, q2 in TS.typed_moves(r):
                    from_z.add(sig_of[q2])
            from_q.discard(z)
            from_z.discard(z)
            hit_q, hit_z = t in from_q, t in from_z
            print("    %s via %s: %d class(es) from %s alone, %d from "
                  "the whole class; escape reachable from %s alone: %s"
                  % (tag, "/".join(ty for ty, _x in moves),
                     len(from_q), fmt4(q), len(from_z), fmt4(q),
                     "YES" if hit_q else "no"))
            if hit_z and hit_q:
                K3_FIRED.append((tag, q))

# ----------------------------------------------------------------- #
# E3: the reaching members and what distinguishes them
# ----------------------------------------------------------------- #

def e3_reaching(seen, land):
    print("\nE3  WHICH MEMBERS REACH THE ESCAPE")
    for tag in sorted(seen):
        ev, horizon, s, p0, _esc, t, sig_of = seen[tag]
        for z, moves, mem in land.get(tag, []):
            reach = []
            for r in mem:
                tys = sorted({ty for ty, q2 in TS.typed_moves(r)
                              if sig_of[q2] == t})
                if tys:
                    reach.append((r, tys))
            if not reach:
                continue
            print("    %s via %s: %d of %d member(s) reach the escape"
                  % (tag, "/".join(ty for ty, _x in moves),
                     len(reach), len(mem)))
            for r, tys in sorted(reach, key=lambda a: SC.pol_key(a[0])):
                print("        %s by %s" % (fmt4(r), " ".join(tys)))
            rst = {(r[0], r[1]) for r, _ in reach}
            ost = {(r[0], r[1]) for r in mem} - rst
            print("        reaching styles %s, non-reaching styles %s, "
                  "style-determined: %s"
                  % (sorted(rst), sorted(ost),
                     "YES" if not (rst & ost) else "no"))

# ----------------------------------------------------------------- #
# E4: the two-step freshening at the three stalls
# ----------------------------------------------------------------- #

def improves(ev, w, Lx):
    q = ev["qloss"][w][1]
    return not q[2] and Fraction(q[0], q[1]) < Lx

def e4_two_step(seen):
    print("\nE4  THE TWO-STEP FRESHENING AT THE STALLS")
    for tag in sorted(seen):
        ev, horizon, s, p0, _esc, t, sig_of = seen[tag]
        cx = TS.counted_cells(ev["J"], p0, horizon)
        Lx = Fraction(ev["qloss"][s][1][0], ev["qloss"][s][1][1])
        q = PT.freshen(p0)
        q2 = PT.freshen(q)
        for lbl, r in (("step 1", q), ("step 2", q2)):
            w = sig_of[r]
            cw = TS.counted_cells(ev["J"], r, horizon)
            print("    %s %s: %s -> class of %d member(s), "
                  "nests %s, improves %s%s"
                  % (tag, lbl, fmt4(r), len(ev["mem"][w]),
                     "YES" if TS.nests_pointwise(cw, cx) else "no",
                     "YES" if improves(ev, w, Lx) else "no",
                     ", IS the nesting escape" if w == t else ""))
        w1, w2 = sig_of[q], sig_of[q2]
        c1 = TS.counted_cells(ev["J"], q, horizon)
        c2 = TS.counted_cells(ev["J"], q2, horizon)
        check("%s: one freshening leaves the class without nesting "
              "or improving" % tag,
              w1 != s and not TS.nests_pointwise(c1, cx)
              and not improves(ev, w1, Lx))
        check("%s: two freshenings nest, improve, and land in the "
              "unique nesting escape" % tag,
              TS.nests_pointwise(c2, cx) and improves(ev, w2, Lx)
              and w2 == t)

# ----------------------------------------------------------------- #
# E5: the two-step freshening over the census scope
# ----------------------------------------------------------------- #

EXPECT_SIDE = {("id", "tree"): 2546, ("id", "chain"): 0,
               ("dbl", "tree"): 2955, ("dbl", "chain"): 597}
EXPECT_D1_MISS = {("id", "tree"): 0, ("id", "chain"): 0,
                  ("dbl", "tree"): 420, ("dbl", "chain"): 0}

def two_step_hit(ev, horizon, s, cx, Lx, cellcache, sig_of, side):
    """From any member of s on this side, does freshening TWICE land
    in a class that nests pointwise against s and strictly improves?
    The INTERMEDIATE must be a distinct class: a first freshening that
    stays in s makes the landing one move from a member of s, which is
    cure-graph distance ONE and is the parent's leg, not this one."""
    for p in ev["mem"][s]:
        if not PT.is_present_pinned(p) or PT.side_of(p) != side:
            continue
        cur = PT.freshen(p)
        z = sig_of[cur]
        if z == s or not PT.is_present_pinned(cur):
            continue
        cur = PT.freshen(cur)
        w = sig_of[cur]
        # Landing back in the INTERMEDIATE class is distance one, not
        # two: the improving class would then be one move from a member
        # of s and the parent's leg already owns it.
        if w == s or w == z:
            continue
        if w not in cellcache:
            rep = sorted(ev["mem"][w], key=SC.pol_key)[0]
            cellcache[w] = TS.counted_cells(ev["J"], rep, horizon)
        if TS.nests_pointwise(cellcache[w], cx) and improves(ev, w, Lx):
            return True
    return False

def e5_census():
    print("\nE5  THE TWO-STEP FRESHENING OVER THE CENSUS SCOPE")
    tab = {(mp, sd): {"classes": 0, "d1": 0, "d2": 0,
                      "d1miss": 0, "d1miss-d2": 0}
           for mp in PT.CENSUS_MAPS for sd in ("tree", "chain")}
    # The distance LABELS below are this rig's own, not the parent's:
    # "distance one" means the first class-changing freshening is one
    # freshening away, and "distance two" means the intermediate
    # landing is a distinct class rather than the start class. Both
    # are recorded here and checked, never inherited.
    exit_d = {}
    frozen_walks = 0
    stayed_in_class = 0
    for horizon in PT.CENSUS_HORIZONS:
        for mp in PT.CENSUS_MAPS:
            for _wname, digs in MR.census_pool(horizon):
                ev = SA.evaluate(digs, mp, horizon)
                sig_of = {p: s for s, ps in ev["mem"].items()
                          for p in ps}
                cellcache = {}
                for s in ev["marg"]:
                    _nt, sh, _fz, _imp, _v, _ptw = TS.class_stats(
                        ev, horizon, s, cellcache, sig_of)
                    if sh:
                        continue
                    walks = PT.walk_class(ev, horizon, s, cellcache,
                                          sig_of)
                    cx = cellcache[s]
                    Lx = Fraction(ev["qloss"][s][1][0],
                                  ev["qloss"][s][1][1])
                    for sd in ("tree", "chain"):
                        rec = walks[sd]
                        if rec is None:
                            continue
                        cell = tab[(mp, sd)]
                        cell["classes"] += 1
                        if rec["best"] is not None:
                            exit_d[rec["best"]] = \
                                exit_d.get(rec["best"], 0) + 1
                        frozen_walks += rec["frozen"]
                        stayed_in_class += sum(
                            1 for p in ev["mem"][s]
                            if PT.is_present_pinned(p)
                            and PT.side_of(p) == sd
                            and sig_of[PT.freshen(p)] == s)
                        d1 = rec["best"] is not None
                        d2 = two_step_hit(ev, horizon, s, cx, Lx,
                                          cellcache, sig_of, sd)
                        cell["d1"] += d1
                        cell["d2"] += d2
                        if not d1:
                            cell["d1miss"] += 1
                            cell["d1miss-d2"] += d2
            print("  h=%-2d %-3s done" % (horizon, mp))
    print("  exit distances recorded %s, frozen walks %d, members "
          "whose first freshening stays in class %d"
          % (sorted(exit_d.items()), frozen_walks, stayed_in_class))
    check("every recorded exit sits at ONE freshening, so the "
          "distance labels below are measured (%s)" % sorted(exit_d),
          set(exit_d) == {1})
    check("no walk freezes, so every class has an exit to record "
          "(%d)" % frozen_walks, frozen_walks == 0)
    for key in sorted(tab):
        c = tab[key]
        print("  %-3s %-5s: %d classes | distance-1 reach %d, "
              "twice-freshened reach %d | distance-1 misses %d, "
              "of which twice-freshened reaches %d"
              % (key[0], key[1], c["classes"], c["d1"], c["d2"],
                 c["d1miss"], c["d1miss-d2"]))
        check("%s %s class total reproduces %d (%d)"
              % (key[0], key[1], EXPECT_SIDE[key], c["classes"]),
              c["classes"] == EXPECT_SIDE[key])
        check("%s %s distance-1 misses reproduce %d (%d)"
              % (key[0], key[1], EXPECT_D1_MISS[key], c["d1miss"]),
              c["d1miss"] == EXPECT_D1_MISS[key])

def main():
    print("THE PINNED COMPOSITE: what the intermediate class supplies")
    seen = e0_control()
    if FAILURES:
        print("\nCONTROL FAILED -- no verdict read below.")
        print("FAILURES: %s" % ", ".join(FAILURES))
        return 1
    land = e1_landing(seen)
    e2_reselection(seen, land)
    e3_reaching(seen, land)
    if K3_FIRED:
        print("\n  K3 FIRES at %d of 3 specimens: the escape is one "
              "typed move from the first move's own landing member "
              "(%s). The re-selection is not forced anywhere."
              % (len(K3_FIRED),
                 ", ".join("%s %s" % (t, fmt4(q))
                           for t, q in K3_FIRED)))
    e4_two_step(seen)
    e5_census()
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % ", ".join(FAILURES)))
    return 1 if FAILURES else 0

if __name__ == "__main__":
    sys.exit(main())
