"""THE MOVE SET: which stall facts are about the reader and which are
about the alphabet the reader was given.

THE QUESTION
------------
Every escape radius the corpus states, every "two-move lookahead"
cure and the whole cure-graph metric count steps in ONE move set,
fixed once and never re-opened. A stall is "no neighbour is better"
and a radius is "fewest edges to a better class", so both are
statements about an EDGE SET before they are statements about a
landscape. Change the alphabet and a stall can dissolve. Nothing in
the corpus has ever asked which of its stall facts survive that.

THE SECOND LEVEL, and it is the reason the rig was widened. The first
run answered "which moves does a reader have" and found that nine of
the ten stalls are readers who may only change patience one notch at
a time (F1). That leaves the harder question underneath: WHY may a
reader only move one notch? Patience is a coordinate a reader SETS,
not one the object hands them, and the unit step is a constraint the
corpus imposes silently. So the axis is widened all the way -- to a
CLIQUE on each patience coordinate, any value to any value in one
move -- and the question becomes whether ANY stall survives a reader
who sets patience freely.

Two definitions stand in the corpus and they are NOT the same set:
  neighbors_cure (explore_scale_clock.py:830) -- neighbors_single5's
    eight single-coordinate steps (two route-preference flips, four
    patience steps on the axis 0,1,2,3,INF, and TWO steps on the
    drawdown coordinate) plus the preference diagonal. NINE at most.
  typed_moves (explore_shift_telescope.py:336) -- the same two flips,
    the same four patience steps and the same diagonal, with NO
    drawdown move. SEVEN at most.
The corpus writes as though they were one set. They differ exactly
where the drawdown axis has more than one value, i.e. where a
resource cap is live: d_axis(W) returns [INF] whenever W = 0, so at
an unresourced or budget-only setting the two sets COINCIDE
policy-for-policy. That is the first thing this rig checks, because
it decides how much of the corpus the difference can touch.

A THIRD set exists and is not a rival: the move cure's PATIENCE
DIAGONALS (explore_bootstrap_cures.py) widen the set deliberately and
say so. It is a comparison case, not a competing definition.

Two moves are already suspect on the corpus's own evidence. The
DIAGONAL moves two coordinates for the price of one and never appears
among the nesting move types at any censused class. And a
RE-SELECTION inside a class costs nothing at all, where
explore_charged_radius.py F1 shows the accounting is not neutral:
charging re-selection moved one stall's radius from 2 to 3 while its
class radius stayed 2.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, the counted-trace quotient and the
ten stall specimens are the parents' (explore_scale_clock.py,
explore_stall_tie.py, explore_stall_assembly.py,
explore_shift_telescope.py, explore_charged_radius.py). A policy is
(st, ss, pt, pc, d): two route preference bits, tree and chain
patience on the axis 0,1,2,3,INF, and the drawdown coordinate. The
specimens are the ten the corpus states a finite radius for -- the
ruler disagreement, the six designed burst traps, the three
horizon-cut (squaring-map) stalls -- rebuilt by
explore_charged_radius.py's own builders so that nothing about the
landscapes is re-derived here.

WHOSE VOCABULARY THIS IS WRITTEN IN
-----------------------------------
The GRAPH's, and deliberately not the reader's. Nothing here runs a
reader, reads a cell or compares a trace: the behavioral signature of
every policy is imported unchanged, so the CLASSES and their RANKS are
fixed inputs and the only thing that varies is which pairs of classes
are joined. That is the whole design -- a variant changes edges and
nothing else -- and it is what makes the sweep cheap and its
comparisons exact.
TRANSPLANT, flagged: "the diagonal never nests at one move" is an
intuition from the NESTING census, whose object is a cell refinement
and whose move set is typed_moves. Nothing about nesting is assumed
here; the diagonal is removed and the graph is re-measured.

THE VARIANTS
------------
V0 cure    the corpus's set: neighbors_cure. The baseline.
V1 nodiag  the diagonal removed (neighbors_single5).
V2 nodraw  the drawdown steps removed -- typed_moves' set, reached
           from the other direction.
V3 bare    both removed: route flips and patience steps only.
V4 step2   the corpus's set PLUS patience steps of index-distance 2
           on AX_BASE, on both patience coordinates.
V5 step3   step2 PLUS index-distance 3, so every patience move of
           distance at most 3. Cumulative, so the lattice holds.
V6 clique  every patience value to every other in ONE move, on each
           coordinate separately -- the free-setting reader. Route
           bits and the drawdown are untouched, so this widens the
           patience axis and nothing else.
Re-selection is NOT a variant here and cannot be: a re-selection
stays inside a class, so as a class-graph edge it is a self-loop and
build_quotient discards it. It cannot move a stall or a class radius,
which is why explore_charged_radius.py had to leave the quotient to
measure it. The rig asserts that rather than sweeping it (C3).

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
THE LATTICE IS FORCED AND IT IS THE WHOLE READING. Order the variants
by inclusion of edge sets: bare < nodiag < cure < step2 and
bare < nodraw < cure. Because classes and ranks do not depend on the
move set, a landscape's class graph under a smaller set is a SUBGRAPH
of its graph under a larger one, on the same vertices with the same
ranks. Two consequences, both exact:
  (i) STALLS GROW DOWNWARD. Stallhood is "no neighbour ranks lower".
      Deleting edges can only preserve it, so stalls(bare) contains
      stalls(nodiag) and stalls(nodraw), each of which contains
      stalls(cure), which contains stalls(step2), which contains
      stalls(step3), which contains stalls(clique). The chain
      extends at the top exactly because step3 and clique are
      CUMULATIVE over the sets below them.
  (ii) RADII GROW DOWNWARD. A path in a subgraph is a path in the
      supergraph, so r_class is monotone non-increasing as edges are
      added, at every class, in the same order.
So a specimen can only STOP stalling under step2, step3 or clique,
and can only gain radius under nodiag, nodraw or bare. Any observed
violation is a BUG and not a finding, which is K4 below.
THE FLOOR LEMMA ALREADY DECIDES THE WIDE END, AND THE RUN IS ITS
CHECK. The floor lemma (explore_pinned_freshening.py,
explore_minimal_cell.py) says that from ANY member of ANY off-bottom
finite-loss class, the DOUBLY PINNED policy at that member's own
style pair -- both patiences 0, route bits unchanged -- lands in a
class that nests pointwise and strictly improves the deficit. Now
read the first run's own mechanism against it: all TEN specimens sit
with one patience at 0 and the other at 2 or 3. So at every one of
the ten, the doubly pinned floor differs from the specimen's member
in ONE patience coordinate only, and a move set that admits an
arbitrary jump on one patience coordinate reaches it in ONE MOVE.
Hence, MODULO ONE STEP named below:
  (iii) ALL TEN DISSOLVE UNDER clique, the survivor included.
  (iv) The FOUR specimens sitting at patience 3 -- two at (0,3),
       the survivor among them, and two at (3,0) -- have their floor
       at index-distance 3, since that is exactly the jump from
       patience 3 to patience 0, so STEP3 dissolves all four at the
       latest. Three of the four already dissolve at step2, where
       the distance-2 move to patience 1 happens to improve; the
       survivor is the one where it does not.
THE ONE STEP, and it is why the derivation is not a proof. The lemma
improves the DEFICIT and nests; the graph ranks by the COMPOSITE
order (clock loss primary, deficit lexicographic as tiebreak), and
nothing in the lemma's statement says the composite must fall with
the deficit. So the derivation reaches "the floor is one move away
and improves the deficit" and stops there. The run supplies the rest,
which is what makes it worth running even though everything else
about it is forced: if a floor move failed to lower the rank, the gap
between "nests and improves the deficit" and "ranks lower" would be
real and would be a finding about the lemma's reach, not about the
alphabet. E5 tests the floor move directly, off the variant
machinery entirely, so that the two readings cannot hide each other.
WHAT IS NOT FORCED is the landscape-wide count. The floor is one
clique move away only from a member with a patience ALREADY at 0; a
class all of whose members carry both patiences positive needs two
moves to reach its floor and may stall with a free-setting reader.
Whether any class in the ten landscapes is such a class is the
measurement, and it is what "does a free reader stall anywhere"
means.
WHERE nodraw CAN DIFFER AT ALL. d_axis(W) = [d in (0,1,2,4) : d < W]
+ [INF], so |daxis| = 1 exactly when W = 0. The specimens' settings
are the parents': the ruler disagreement at (B,W) = (2,0), the three
horizon-cut stalls unresourced, and the burst traps drawn from
SETTINGS = [(None,0), (1,0), (2,0), (2,2)]. Only (2,2) has a live
drawdown axis, so nodraw = cure at every specimen except any burst
trap sitting at (2,2), and how many that is the run prints.
WHAT A DISSOLVED STALL WOULD MEAN. Not that the corpus is wrong: a
stall is defined relative to a move set and the corpus's is stated.
It would mean the stall is a property of the ALPHABET rather than of
the landscape -- and the reader who has the wider alphabet is not a
hypothetical, since the move cure ships one publicly.
INDEX CONVENTIONS. Nothing here dereferences a trace by step index.
The patience axis AX_BASE is indexed for the step-2 variant; the
index is read from the axis object itself, never assumed, and INF sits
at the top end as the parents build it.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C0 [positive control, run first] The ten specimens rebuild, the
   counts are 1, 6 and 3, and r_class is 2 at all ten under V0 --
   the corpus's published figure. A miss is K1 and no verdict is read.
C1 [control] Every variant's class graph stands on the same vertex
   set. The ranks cannot differ at all -- each variant is handed the
   parent's own rank map, unmodified -- so the vertex set is the half
   a construction error could move, and it is the half checked.
C2 [control] The two copies of neighbors_cure -- explore_scale_clock.py
   and explore_banking_reader.py:758 -- agree policy-for-policy over
   every specimen's policy space. The aim owes this check.
C3 [control] Admitting re-selection as an edge changes no class
   neighbour set anywhere: the quotient already discards it.
P1 [the drawdown asymmetry] nodraw differs from cure at SOME burst
   trap, i.e. at least one of the six sits at (B,W) = (2,2).
   GUESS: yes, one or two of the six.
P2 [the diagonal] Removing the diagonal changes NO specimen's stall
   status -- forced -- and raises NO specimen's radius above 2.
   GUESS: it holds. The diagonal is a shortcut between two flips, and
   both flips are in every variant, so a diagonal edge is a
   two-edge path in nodiag; a radius-2 escape using a diagonal at its
   first step becomes a radius-3 escape and the guess is that none of
   the ten routes that way. Scored per specimen.
P3 [the diagonal, off the specimens] Removing the diagonal CREATES
   new stalls somewhere in the ten landscapes. GUESS: yes, at a
   handful of classes -- the diagonal is the only move that changes
   both route bits at once and some class must depend on it.
P4 [the wider alphabet] step2 DISSOLVES at least one of the ten.
   GUESS: yes, and among the burst traps rather than the horizon-cut
   ones, whose route the corpus has read directly.
P5 [the population] Under step2 the total stall count across the ten
   landscapes falls by more than half. GUESS: yes -- a stall is a
   local statement and doubling the patience reach is a large change
   to a five-coordinate neighbourhood.

P6 [the survivor, derived] The one step-2 survivor stops stalling
   under step3, and its r_class falls to 1. Forced by the floor lemma
   at a member sitting at patience (0,3); the run is the check.
P7 [the ten, derived] Under clique no specimen of the ten is a stall
   and every r_class is 1. Same derivation, no patience left out.
P8 [the free reader] Some class SOMEWHERE in the ten landscapes is
   still a stall under clique. GUESS: yes -- the floor is one clique
   move away only from a member already carrying a zero patience, and
   a landscape with hundreds of classes should hold one that does not.
   If instead the count is zero everywhere, every stall the corpus has
   is a statement about the patience STEP SIZE and nothing else.
P9 [the refusal artifact] No dissolution at step3 or at clique needs a
   move to REFUSAL (patience INF). GUESS: it holds, as it did at
   step2 -- the mechanism runs toward the floor, i.e. downward.

KILL CRITERIA (observables; the meaning is weighed after the run)
----------------------------------------------------------------
K1 Any control miss (C0, C1, C2, C3). The population is not the
   parents' and nothing below is a verdict.
K2 THE AIM'S KILL-SHAPE. Every one of the ten remains a stall under
   every variant AND its r_class is 2 under every variant. The move
   set is incidental to the corpus's stall facts and the metric is
   robust; the question closes.
K3 Some specimen stops stalling under step2, or gains radius under
   nodiag/nodraw/bare. That stall or that radius is a property of the
   move set; the rig prints the class, the variant, and the move that
   made the difference.
K5 THE WIDE END'S KILL-SHAPE. No class anywhere in the ten
   landscapes stalls under clique. Then the whole finite-loss stall
   corpus is a statement about incremental patience, the one survivor
   is a two-notch accident, and what the corpus owes is a hypothesis
   clause in front of every radius claim rather than a new object.
K6 A floor move that does NOT lower the rank at some member of some
   specimen (E5). The floor lemma's improvement and the graph's rank
   order come apart; the rig prints the member, the floor policy and
   both ranks, and P6/P7 are read against that rather than assumed.
K4 Any violation of the forced lattice -- a stall appearing when
   edges are ADDED, a radius rising when edges are added, or a class
   set differing across variants. The rig has a bug and prints the
   offending pair rather than a verdict.

ENGINE
------
E0 the controls: rebuild the ten specimens through
   explore_charged_radius.py's builders, reproduce the counts and the
   published radii, reconstruct each landscape's drawdown axis from
   its own policy space and check the reconstruction against the
   parent's own neighbour function (C0, C2).
E1 the variant sweep at the ten specimens: for each landscape and
   each variant, the move-set size, whether the specimen is still a
   stall, and its r_class (P1, P2, P4, K2, K3).
E2 the lattice check across every off-bottom class of every landscape
   (C1, K4), and the landscape-wide stall counts per variant (P3, P5).
E3 the anatomy of any specimen whose status or radius moves: the
   variant, the neighbour class the new edge reaches, and the move
   that reaches it; then the SHAPE of every dissolution under each
   widening variant -- the improving moves that variant adds, by
   their per-coordinate delta, and how many of them reach refusal
   (P9, K5's artifact guard, and F1's mechanism at step2).
E5 the floor move read directly, off the variant machinery (E4 is
   deliberately unused: the imported forge prints its own E4 banner at
   collect time, and two engines called E4 in one output is a reader's
   trap): at every
   member of every one of the ten specimens, the doubly pinned policy
   at that member's own style pair, its class, and its rank against
   the specimen's (K6, P6, P7); then the same read over EVERY off-bottom
   class of the ten landscapes, and the classes the doubly pinned
   policies themselves occupy per landscape, which is the floor
   theorem's own premise (F9); then the two spike1 burst traps at
   (B, W) = (2, 0) read against each other -- the survivor and the
   control that differs from it in no coordinate the corpus records
   except the STREAM -- by printing, from each one's singleton
   member, the class rank reached at every value of each patience
   coordinate. That table is the step-size structure itself: it says
   at which distances an improving class first appears on each side,
   which is what makes one of the pair a step-2 survivor and the
   other not.
Exact integer and Fraction arithmetic throughout; the quotient and
the ranks are the parents' and are not recomputed. Sequential;
estimated run well under a minute, the burst forge rebuild the
driver; memory trivial (no BLAS import); exit nonzero on any check
failure.

FINDINGS (entered after the runs; ALL CHECKS PASS, exit 0, 13.3 s,
28.1 MB peak working set under the memory watch -- the final run's,
the wall figure varying by a few tenths across runs and the peak by a
tenth. F1-F5 are the
narrow sweep's, F6-F8 the widened one's; the verdict below is the
widened reading and it retires the narrow one's)
----------------------------------------------------------------
F1 NINE OF THE TEN STALLS ARE PROPERTIES OF THE MOVE SET, AND THE
   AIM'S KILL-SHAPE MISSES BY THE WIDEST MARGIN AVAILABLE. Admit a
   patience step of index-distance 2 and nine of the ten specimens
   STOP STALLING outright -- the ruler disagreement, five of the six
   burst traps and all three horizon-cut stalls -- each of them
   dropping from r_class 2 to r_class 1, i.e. each acquiring a
   strictly better NEIGHBOUR rather than a shorter route. Across the
   ten landscapes the total stall count falls from 10 to 1. P4 and P5
   are both right and P5's "more than half" understates it by a lot.
   The mechanism is uniform: all TEN sit with one patience at 0 and
   the other at 2 or 3 -- (0,2) five times, (0,3) twice, (3,0) twice,
   (2,0) once -- and at each of the NINE the escape gained is the
   single step DOWN that coordinate, to patience 0 or 1: a delta of
   exactly -2 on one patience with the other patience, both route
   bits and the drawdown all unchanged, at every one of them. The
   tenth has the same shape and gains nothing, which is F2. NOTE THE
   VARIANT'S OWN EDGE: index-distance 2 on the axis 0,1,2,3,INF also
   admits patience 2 -> INF, which is a jump to REFUSAL and not a
   doubled patience at all. No dissolution uses one -- every improving
   step-2 move at all nine is downward -- so the finding does not rest
   on that artifact, and a wider variant must be read with the same
   check. Under the
   corpus's set that step costs two moves and the intermediate
   patience is not an improvement, which is the entire content of
   "escape radius 2". These stalls are an artifact of the patience
   axis being traversable one notch at a time.
F2 THE ONE SURVIVOR IS THE ONE SPECIMEN THE CORPUS ALREADY KNEW WAS
   DIFFERENT. The single stall that survives the wider alphabet is
   the burst trap on the spike1@6 stream under the doubling map at
   horizon 120, (B, W) = (2, 0), 57 classes -- which is exactly and
   only the specimen where explore_charged_radius.py F1 found the
   published radius not member-realisable, its charged and pure radii
   both 3 against a class radius of 2. Two independent perturbations
   of the metric -- charging the quotient's free re-selection, and
   widening the patience step -- single out the same one stall of ten
   from opposite directions. Nothing in either rig's design connects
   them: the first is about which MEMBER a route departs from, the
   second about which POLICIES are adjacent at all. It survives
   the TWO-notch step only: F6 dissolves it at three, so it is the
   corpus's last stall to fall and not a stall about the landscape.
F3 THE ASYMMETRY BETWEEN THE TWO DEFINITIONS IS REAL, IT IS NARROW,
   AND IT RUNS THE OTHER WAY. The two sets differ only where the
   drawdown axis is live, which is |daxis| = 3 at exactly two of the
   ten specimens -- the burst traps at (B, W) = (2, 2), on spike1@6
   and spike1@12 -- and |daxis| = 1 at the other eight, where
   neighbors_cure and typed_moves coincide policy-for-policy. P1 is
   right at the top of its band. At those two landscapes deleting the
   drawdown steps does NOT move the specimen: it stays a stall at
   radius 2. What it does is CREATE stalls elsewhere -- 1 to 3 at
   spike1@6/(2,2) and 1 to 5 at spike1@12/(2,2), taking the corpus
   population from 10 to 16. So the reader holding typed_moves' set
   is not blind to any published stall; they are stalled at six
   classes the published set escapes, all of them at a live resource
   cap and all invisible to a corpus whose specimens sit at W = 0.
   The two definitions are safe for every claim the corpus states and
   unsafe for the population it never censused.
F4 THE DIAGONAL IS NOT REDUNDANT AND IT IS STILL INERT, WHICH IS THE
   SHARPER STATEMENT. Removing it changes NOTHING anywhere: the same
   10 stalls, the same radii, no new stall at any class of any of the
   ten landscapes. P3 is refuted. But it is not doing nothing -- it
   supplies 360 class edges that no other move supplies at seven of
   the ten landscapes (24 to 108 apiece, out of 764 class-leaving
   diagonal moves over all ten), and ZERO at the other three, where
   every diagonal lands in a class some flip already reaches. So a
   move can add a sixth of a landscape's adjacency and be invisible
   to every question the corpus asks of the graph. WHAT SEPARATES THE
   THREE IS CONFOUNDED HERE and the rig cannot part it: they are the
   only squaring-map landscapes of the ten AND the only unresourced
   ones, so redundancy may be the map's doing or the budget's, and
   nothing in this population decides which. The inertness, by
   contrast, is a fact about the stalls and holds at all ten. The
   corpus had neither, and its suspicion of the diagonal was right
   about the object and wrong about the reason.
F5 RE-SELECTION CANNOT BE A VARIANT, AND THE SECOND COPY AGREES.
   Admitting re-selection as an edge changes no class neighbour set
   at any of the ten landscapes (C3) -- it is a self-loop the
   quotient discards, so no stall and no class radius can move under
   it, and explore_charged_radius.py's departure from the quotient
   was forced rather than stylistic. And the two copies of
   neighbors_cure -- explore_scale_clock.py:830 and
   explore_banking_reader.py:758 -- agree policy-for-policy over
   every specimen's policy space (C2), which discharges the check the
   aim owed.

F6 EVERY STALL IN THE CORPUS DIES AT PATIENCE STEP SIZE 3, AND THE
   CLIQUE IS NEVER NEEDED. Under step3 the stall count is ZERO at
   every one of the ten landscapes -- not merely at the ten
   specimens but over every off-bottom class of all ten landscapes,
   whose class counts run 17 to 157 and total 611, of which 601
   sit off the bottom. The population
   runs 10 (cure), 10 (nodiag), 16 (nodraw), 16 (bare), 1 (step2),
   0 (step3), 0 (clique). So the
   free-setting reader is not needed to make the point and the
   clique adds nothing over distance 3: P8 is REFUTED -- the guess
   was that some class of some landscape would still stall for a
   reader who sets patience freely, and none does. The one step-2
   survivor, the spike1@6 trap, falls at step3 with its r_class
   going 2 to 1, which is P6 exactly; and no specimen of the ten is
   a stall under clique with every r_class at 1, which is P7.
   AND THE ZERO REACHES FURTHER THAN THE TEN, for free. Stalls are
   monotone under adding edges (K4), so a landscape with none under
   the corpus's own set can have none under a wider one -- and the
   imported forge's own banner reports 6 landscapes with stalls out
   of the 448 the burst battery sweeps. So no landscape in that
   battery holds a stall at a three-notch patience step either.
   That is derived from the lattice rather than measured, and it
   costs nothing.
F7 THE FALL WAS DERIVABLE BEFORE THE RUN UP TO ONE STEP, AND THAT
   STEP IS WHAT THE RUN BUYS. All ten specimens sit
   with one patience at 0, so the doubly pinned floor differs from
   each member in ONE coordinate and any move set admitting an
   arbitrary jump on one patience reaches it in one move, and the
   floor lemma makes it strictly better IN DEFICIT. That is as far
   as the derivation goes, and F9 narrows it further: the lemma is
   proved UNRESOURCED and seven of the ten specimens are not, so at
   those seven the improvement is MEASURED here and not inherited.
   The graph also ranks by the composite order, not by the
   deficit. E5 checks that step directly, off the variant
   machinery, at all 13 members of the ten specimens: the floor
   improves at every one,
   the rank falling to 0 at nine members and to 1 or 2 at the four
   members of the two spike1@10 specimens. That is the step the
   derivation could not take -- the floor lemma improves the DEFICIT
   and nests, while the graph ranks by the composite order with the
   clock loss primary, and nothing in the lemma says the composite
   must fall. Here it does, at every member. The survivor's own case
   is the derivation in miniature: its member sits at patience
   (0,3), index-distance 3 from the floor, which is why step2
   reaches patience 1 and misses while step3 lands on the floor and
   its class ranks 0 against the specimen's 8.
   AND THE WIDENING IS NOT THE REFUSAL ARTIFACT. At step2, step3 and
   clique alike, every improving move each variant adds is a single
   DOWNWARD patience step with the other patience, both route bits
   and the drawdown unchanged, and NONE of them reaches refusal --
   0 of the improving moves at every dissolution at all three
   variants. The widened axis admits patience -> INF, and no
   dissolution anywhere uses one.
F8 THE LAST STALL AND ITS CONTROL DIFFER AT ONE CELL, AND IT IS AN
   ADJACENT-RANK INVERSION. The survivor (spike1@6) and its control
   (spike1@12) are the same in every coordinate the corpus records
   -- doubling map, horizon 120, (B, W) = (2, 0), 57 classes, the
   singleton class sigma = (1,1) at patiences (0,3) -- and differ
   only in the STREAM. Read the class rank reached at every value of
   each patience coordinate from that member and the two profiles
   are IDENTICAL along the tree axis (own, 26, 42, 45, 56 at
   patience 0,1,2,3,INF) and identical along the chain axis at four
   of its five values (0 reaches rank 0, 2 reaches 10, INF reaches
   11, 3 is its own class). They differ at chain patience 1 ALONE:
   the control reaches rank 8 against its own rank 9 -- strictly
   better, so it dissolves at step2 -- while the survivor reaches
   rank 9 against its own rank 8, strictly worse. The two landscapes
   are distinct objects and their classes are not the same classes,
   so what is shared is the RANK PROFILE: the same five values are
   reached on each axis, and what the stream flips is which of the
   adjacent pair 8 and 9 the specimen itself holds. So the corpus's
   one two-notch survivor is a single adjacent-rank inversion and
   nothing larger, which is why no coordinate the corpus records
   could have predicted it. The profile also shows
   WHY a unit-step reader stalls at all: rank along the chain axis
   runs 0, 8/9, 10, own, 11 -- non-monotone in patience, so a reader
   stepping down one notch at a time walks through classes worse
   than their own before reaching the floor, and stops.

F9 THE FLOOR THEOREM CARRIES AN UNSTATED RESOURCE FENCE, AND ITS
   CONCLUSION SURVIVES WHERE ITS PREMISE DOES NOT. The theorem earns
   the name "the bottom" from a premise: a policy greedy at both
   kinds commits the floor at every step whatever the route, so all
   four doubly pinned policies are ONE class and that class is the
   bottom. Read over the ten landscapes that premise holds at the
   three UNRESOURCED ones -- 4 policies, 1 class, rank 0 at each --
   and FAILS at all seven resourced ones, where the doubly pinned
   policies occupy 3, 4, 8 or 12 distinct classes spanning ranks 0
   through 11. The mechanism is not subtle once looked at: under a
   rank budget a greedy reader cannot always AFFORD the floor, so
   the route preferences and the drawdown schedule enter the run,
   which is exactly what the premise says they do not. The parent
   census that proved it is unresourced (explore_pinned_freshening.py
   runs where "the rank IS the loss order"), so nothing there is
   wrong; what is missing is the fence, and the scope line enumerates
   map, stream, horizon and patiences while saying no map fence and
   no patience hypothesis stands on it -- naming every dimension
   except the one that breaks it.
   WHAT SURVIVES IS THE CONCLUSION, and this rig widens its evidence
   rather than narrowing it. Over all 601 off-bottom classes and
   1,362 members of the ten landscapes, resourced and unresourced
   alike, the doubly pinned floor's class ranks strictly lower
   wherever it is a DISTINCT class: 1,328 of 1,328, in the COMPOSITE
   order the cure graph uses and not merely in the deficit. The 34
   exceptions are members that ARE the doubly pinned policy, so they
   are members already at their floor and nothing else -- which is
   also what corrects the parent's aside that "a member already
   doubly pinned sits at rank 0", true unresourced and false under a
   cap. And those 34 sit in exactly 30 classes, which are EXACTLY the
   30 classes no patience jump of any distance improves: a class
   holding its own doubly pinned policy has nowhere down the patience
   axis to go, which is the mechanism behind the verdict's guard.

THE VERDICT. THE STALL IS NOT AN OBJECT; IT IS THE PATIENCE STEP
SIZE. Widening the move set on ONE parameter -- how far a reader may
move a patience coordinate in one move -- takes the stall count over
the ten landscapes from 10 to 1 at step size 2 and to ZERO at step
size 3, over every off-bottom class and not merely the specimens.
Nothing survives to the clique, so a reader who sets patience freely
never stalls anywhere in this corpus. PATIENCE IS STILL NOT THE WHOLE
ALPHABET, which is the misreading this invites: 30 of the 601
off-bottom classes have no improving patience jump at ANY distance and
are cured only by a route flip or a drawdown move. What the widening
dissolves is the STALLS, never the dependence on the other
coordinates. The mechanism is one lemma
read at step size: every one of these classes has a member one
patience jump from its doubly pinned floor, the floor lemma makes
that floor strictly better, and the only question the graph asks is
whether the jump is in the alphabet. So every published escape
radius of 2 measures the distance to the floor in UNIT patience
steps, every stall the corpus states is a reader who may only change
patience one notch at a time, and what makes such a reader stop is
that rank is NON-MONOTONE in patience: the classes between them and
the floor are worse than their own. The corpus's last stall to fall
is one adjacent-rank inversion (F8) and not a landscape fact either.
The zero is not confined to the ten:
stalls are monotone under adding edges, and only 6 of the burst
battery's 448 landscapes hold one under the corpus's own set, so
none of the 448 holds one at three notches.
What the corpus owes is therefore not a new object but a HYPOTHESIS
in front of the census: its stalls and its radii are statements
about an alphabet, and that alphabet is stated everywhere as a
definition and argued nowhere.
AND THE TWO DEFINITIONS ARE NOT THE HAZARD THE AIM SUSPECTED: they
coincide at eight of the ten specimens and agree at the other two,
differing only in a population the corpus never censused, where the
narrower set stalls six extra classes at a live resource cap.

Run record. The first run (E0-E3) exited 0 in 13.0 s with every
control passing. Two post-run edits, neither touching a prediction
band. The first added the WORLD column to E1, E2 and E3: two
spike1@10 specimens printed under identical name-and-setting labels --
a de-duplication key missing the coordinate that identifies its object
-- and without the column F2's identification of the survivor could not
be made. The second added the diagonal's own
contribution to E2 -- the count of class-leaving diagonal moves and
of class edges no other move supplies -- because the sweep had shown
the diagonal changes no verdict and "changes no verdict" and "adds no
edge" are different claims that only a count separates; F4 is that
count. A third edit came from the audit: E1 now prints each stall
class's SIZE and its MEMBERS. F1's mechanism sentence had been read
off the anatomy lines, which cover only the nine specimens that
moved, so the tenth's policy had entered the record from a parent rig
rather than from this one -- and F2's control, the spike1@12 trap
identical to the survivor in every coordinate the corpus records, is
visible only once all ten are printed side by side. The same round
enumerated every improving step-2 move at the nine rather than
reading the anatomy's samples, which is what puts the -2 delta and
the absence of any INF jump into F1, and it enters the rig as E3's
closing check rather than as a docstring assertion.
THE WIDENING is the second run, and it is a design edit rather than
a post-run one: V5 and V6 entered with their own hand-attack, their
own predictions P6-P9 and their own kill criteria K5-K6 fixed before
any of them ran, because the first run's F1 had made the question
underneath it -- why one notch -- the live one. E3's shape read was
generalised from step2 to every widening variant at the same time,
and E5 was written to test the floor move OFF the variant machinery
so that the derivation and the sweep could not confirm each other by
sharing code. One bug was caught before any finding was read: E5's
comparison set selected its landscapes by indexing the SETTING as a
tuple when the parents pass it as a formatted string, so the table
printed nothing at all rather than printing something wrong. It now
locates the survivor from the run itself -- the specimen still
stalling under step2 -- and compares it against every specimen
sharing its world and setting, so no landscape in that table is
named by hand. The audit then strengthened two checks that were
weaker than the sentences resting on them. E3's shape check asserted
that a dissolution's added moves move one patience and leave the
rest alone, which the variants guarantee BY CONSTRUCTION and which
therefore could not fail; it now asserts what the finding actually
claims -- that every improving added move is DOWNWARD and none
reaches refusal -- which is falsifiable and holds. And E5's floor
check verified the RANK half of the derivation while its own name
claimed the other half, that the floor is one jump away; the
zero-patience premise that carries that half is now its own check.
The audit then re-derived the headline by a route that shares none of
the rig's aggregation: for each off-bottom class, scan its members'
neighbours directly -- the parent's cure moves plus patience jumps of
index-distance <= d -- and ask whether any lands in a strictly better
class, building no class graph and running no BFS. It reproduces
10, 10, 1, 0, 0 at d = 0,1,2,3,4 over 601 off-bottom classes, which is
the sweep's own table from a different computation, and it is where the
30-class figure in the verdict came from. Final run under the memory
watch, ALL CHECKS PASS, exit 0, 13.3 s, 28.1 MB peak.
"""

import os
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import explore_scale_clock as SC
import explore_banking_reader as BR
import explore_charged_radius as CR

FAILURES = []


def check(name, ok, detail=""):
    print("  [%s] %s%s" % ("ok" if ok else "FAIL", name,
                           ("  " + detail) if detail else ""))
    if not ok:
        FAILURES.append(name)
    return ok


# ----------------------------------------------------------------- #
# the variants: each is a neighbour function of (policy, axis, daxis)
# ----------------------------------------------------------------- #

def nb_cure(p, axis, daxis):
    return SC.neighbors_cure(p, axis, daxis)


def nb_nodiag(p, axis, daxis):
    return SC.neighbors_single5(p, axis, daxis)


def _no_draw(p, axis, daxis):
    """neighbors_single5 with the two drawdown steps deleted."""
    st, ss, pt, pc, d = p
    out = [(1 - st, ss, pt, pc, d), (st, 1 - ss, pt, pc, d)]
    it, ic = axis.index(pt), axis.index(pc)
    if it > 0:
        out.append((st, ss, axis[it - 1], pc, d))
    if it < len(axis) - 1:
        out.append((st, ss, axis[it + 1], pc, d))
    if ic > 0:
        out.append((st, ss, pt, axis[ic - 1], d))
    if ic < len(axis) - 1:
        out.append((st, ss, pt, axis[ic + 1], d))
    return out


def nb_nodraw(p, axis, daxis):
    st, ss, pt, pc, d = p
    return _no_draw(p, axis, daxis) + [(1 - st, 1 - ss, pt, pc, d)]


def nb_bare(p, axis, daxis):
    return _no_draw(p, axis, daxis)


def nb_step2(p, axis, daxis):
    """The corpus's set plus patience steps of index-distance 2."""
    st, ss, pt, pc, d = p
    out = list(SC.neighbors_cure(p, axis, daxis))
    it, ic = axis.index(pt), axis.index(pc)
    if it > 1:
        out.append((st, ss, axis[it - 2], pc, d))
    if it < len(axis) - 2:
        out.append((st, ss, axis[it + 2], pc, d))
    if ic > 1:
        out.append((st, ss, pt, axis[ic - 2], d))
    if ic < len(axis) - 2:
        out.append((st, ss, pt, axis[ic + 2], d))
    return out


def _patience_jumps(p, axis, maxd):
    """Single-coordinate patience moves of index-distance <= maxd,
    on both patience coordinates."""
    st, ss, pt, pc, d = p
    it, ic = axis.index(pt), axis.index(pc)
    out = []
    for j, v in enumerate(axis):
        if 0 < abs(j - it) <= maxd:
            out.append((st, ss, v, pc, d))
        if 0 < abs(j - ic) <= maxd:
            out.append((st, ss, pt, v, d))
    return out


def nb_step3(p, axis, daxis):
    """step2 plus index-distance 3: every patience move of distance
    at most 3, so the set is cumulative over step2."""
    return (list(SC.neighbors_cure(p, axis, daxis))
            + _patience_jumps(p, axis, 3))


def nb_clique(p, axis, daxis):
    """The free-setting reader: any patience value to any other in
    one move, on each coordinate separately."""
    return (list(SC.neighbors_cure(p, axis, daxis))
            + _patience_jumps(p, axis, len(axis)))


VARIANTS = (("cure", nb_cure), ("nodiag", nb_nodiag),
            ("nodraw", nb_nodraw), ("bare", nb_bare),
            ("step2", nb_step2), ("step3", nb_step3),
            ("clique", nb_clique))

# the variants that only ADD patience moves to the corpus's set,
# widest last: the shape read walks these.
WIDENING = ("step2", "step3", "clique")

# edge-set inclusions the hand-attack forces: (smaller, larger)
LATTICE = (("bare", "nodiag"), ("bare", "nodraw"),
           ("nodiag", "cure"), ("nodraw", "cure"),
           ("cure", "step2"), ("step2", "step3"),
           ("step3", "clique"))


# ----------------------------------------------------------------- #
# landscape assembly
# ----------------------------------------------------------------- #

def daxis_of(mem):
    """Reconstruct a landscape's drawdown axis from its own policy
    space: finite values ascending, then the spend-all sentinel."""
    vals = {p[4] for ps in mem.values() for p in ps}
    fin = sorted(v for v in vals if v is not SC.INF_D)
    return fin + ([SC.INF_D] if SC.INF_D in vals else [])


def collect():
    """The ten specimens as
    (family, name, world, setting, space, sig_of, mem, qranks,
     daxis, stalls, parent_nbr_fn)."""
    fams = (("RULER", CR.ruler_landscape()),
            ("BURST", CR.burst_landscapes()),
            ("SQ", CR.sq_landscapes()))
    out = []
    for family, rows in fams:
        for (name, world, setting, mem, nbrs, nbr_fn,
             qranks, stalls) in rows:
            sig_of = {p: s for s, ps in mem.items() for p in ps}
            space = list(sig_of)
            out.append((family, name, world, setting, space, sig_of,
                        mem, qranks, daxis_of(mem), list(stalls),
                        nbr_fn))
    return out


def edges(space, sig_of, nbr_fn):
    """Class neighbour sets under one neighbour function."""
    nbrs = {s: set() for s in set(sig_of.values())}
    for p in space:
        sp = sig_of[p]
        for q in nbr_fn(p):
            t = sig_of.get(q)
            if t is not None and t != sp:
                nbrs[sp].add(t)
    return nbrs


def radius(s0, nbrs, qranks):
    return CR.r_class(s0, nbrs, lambda t: qranks[t] < qranks[s0])


def stalls_of(nbrs, qranks):
    return {s for s in nbrs
            if qranks[s] > 0 and all(qranks[t] >= qranks[s]
                                     for t in nbrs[s])}


def fmt(v):
    return "-" if v is None else str(v)


# ----------------------------------------------------------------- #
# E0: controls
# ----------------------------------------------------------------- #

def e0_controls(lands):
    print("\nE0  CONTROLS: the ten specimens, the axes, the two copies")
    counts = {}
    for (family, _n, _w, _s, _sp, _si, _m, _q, _d, stalls,
         _f) in lands:
        counts[family] = counts.get(family, 0) + len(stalls)
    check("ruler disagreement: 1 stall class",
          counts.get("RULER") == 1, "got %s" % counts.get("RULER"))
    check("burst traps: 6 stall specimens",
          counts.get("BURST") == 6, "got %s" % counts.get("BURST"))
    check("horizon-cut stalls: 3 stall classes",
          counts.get("SQ") == 3, "got %s" % counts.get("SQ"))

    bad_r, bad_ax, bad_copy = [], [], []
    for (_fam, name, _w, _s, space, sig_of, _m, qranks, daxis,
         stalls, pnbr) in lands:
        nb = edges(space, sig_of, lambda p: nb_cure(p, SC.AX_BASE,
                                                    daxis))
        for s0 in stalls:
            if radius(s0, nb, qranks) != 2:
                bad_r.append((name, radius(s0, nb, qranks)))
        for p in space:
            if sorted(map(str, pnbr(p))) != \
                    sorted(map(str, nb_cure(p, SC.AX_BASE, daxis))):
                bad_ax.append((name, p))
                break
            if sorted(map(str, BR.neighbors_cure(p, SC.AX_BASE,
                                                 daxis))) != \
                    sorted(map(str, SC.neighbors_cure(p, SC.AX_BASE,
                                                      daxis))):
                bad_copy.append((name, p))
                break
    check("C0: published escape radius is 2 at all ten",
          not bad_r, "misses %s" % (bad_r,))
    check("C0: reconstructed drawdown axis reproduces each parent's "
          "own neighbour function", not bad_ax, "misses %s" % (bad_ax,))
    check("C2: the two neighbors_cure copies (scale_clock, "
          "banking_reader) agree policy-for-policy",
          not bad_copy, "misses %s" % (bad_copy,))

    # C3: re-selection is a self-loop on classes.
    bad_rs = []
    for (_fam, name, _w, _s, space, sig_of, mem, qranks, daxis,
         _st, _f) in lands:
        base = edges(space, sig_of, lambda p: nb_cure(p, SC.AX_BASE,
                                                      daxis))
        withrs = edges(space, sig_of,
                       lambda p: list(nb_cure(p, SC.AX_BASE, daxis)) +
                       [q for q in mem[sig_of[p]] if q != p])
        if base != withrs:
            bad_rs.append(name)
    check("C3: admitting re-selection as an edge changes no class "
          "neighbour set", not bad_rs, "misses %s" % (bad_rs,))

    print("  the drawdown axis per landscape:")
    for (_fam, name, _w, setting, _sp, _si, _m, _q, daxis, _st,
         _f) in lands:
        print("    %-28s %-14s |daxis| = %d  %s"
              % (name, setting, len(daxis),
                 "LIVE" if len(daxis) > 1 else "singleton"))


# ----------------------------------------------------------------- #
# E1: the variant sweep at the ten specimens
# ----------------------------------------------------------------- #

def e1_sweep(lands):
    print("\nE1  THE VARIANT SWEEP at the ten specimens")
    head = "    %-24s %-11s %-11s %-5s %-5s" % ("specimen", "world",
                                                  "setting", "rank",
                                                  "|s0|")
    for vname, _f in VARIANTS:
        head += " %-10s" % vname
    print(head + "   (stall? / r_class)")
    rows = []
    for (_fam, name, world, setting, space, sig_of, mem, qranks,
         daxis, stalls, _f) in lands:
        for s0 in stalls:
            cells, rec = [], {}
            for vname, vfn in VARIANTS:
                nb = edges(space, sig_of,
                           lambda p, f=vfn: f(p, SC.AX_BASE, daxis))
                st = s0 in stalls_of(nb, qranks)
                r = radius(s0, nb, qranks)
                rec[vname] = (st, r, nb)
                cells.append("%-10s" % ("%s/%s" % ("Y" if st else "n",
                                                   fmt(r))))
            print("    %-24s %-11s %-11s %-5d %-5d %s"
                  % (name, world, setting, qranks[s0], len(mem[s0]),
                     " ".join(cells)))
            print("      members: %s"
                  % " | ".join(SC.fmt_pol5(q) for q in
                               sorted(mem[s0], key=SC.pol_key)))
            rows.append((name, world, setting, s0, space, sig_of,
                         qranks, daxis, rec))
    return rows


# ----------------------------------------------------------------- #
# E2: the lattice, and the landscape-wide stall counts
# ----------------------------------------------------------------- #

def e2_lattice(lands):
    print("\nE2  THE LATTICE and the landscape-wide stall counts")
    print("    %-24s %-11s %6s" % ("landscape", "world", "cls"),
          end="")
    for vname, _f in VARIANTS:
        print(" %7s" % vname, end="")
    print("   (stall classes)")
    viol_rank, viol_stall, viol_rad = [], [], []
    totals = {v: 0 for v, _f in VARIANTS}
    for (_fam, name, world, _s, space, sig_of, _m, qranks, daxis,
         _st, _f) in lands:
        per = {}
        for vname, vfn in VARIANTS:
            nb = edges(space, sig_of,
                       lambda p, f=vfn: f(p, SC.AX_BASE, daxis))
            per[vname] = (nb, stalls_of(nb, qranks))
        # C1: the vertex set and ranks are shared by construction;
        # check the graphs are on the same vertices.
        vsets = {frozenset(per[v][0]) for v, _f in VARIANTS}
        if len(vsets) != 1:
            viol_rank.append(name)
        for small, large in LATTICE:
            if not per[large][1] <= per[small][1]:
                viol_stall.append((name, small, large))
            for s in per[large][0]:
                if qranks[s] == 0:
                    continue
                rl = radius(s, per[large][0], qranks)
                rs = radius(s, per[small][0], qranks)
                if rl is None and rs is None:
                    continue
                if rl is None or (rs is not None and rl > rs):
                    viol_rad.append((name, small, large, s, rs, rl))
        line = "    %-24s %-11s %6d" % (name, world,
                                          len(per["cure"][0]))
        for vname, _f in VARIANTS:
            line += " %7d" % len(per[vname][1])
            totals[vname] += len(per[vname][1])
        print(line)
    print("    %-24s %-11s %6s" % ("TOTAL", "", ""), end="")
    for vname, _f in VARIANTS:
        print(" %7d" % totals[vname], end="")
    print()
    check("C1: every variant's class graph is on the same vertex set",
          not viol_rank, "misses %s" % (viol_rank,))
    print("    the diagonal's own contribution, per landscape "
          "(class edges it adds that no other move supplies):")
    tot_add = tot_diag = 0
    for (_fam, name, world, _s, space, sig_of, _m, _q, daxis,
         _st, _f) in lands:
        base = edges(space, sig_of,
                     lambda p: nb_nodiag(p, SC.AX_BASE, daxis))
        wide = edges(space, sig_of,
                     lambda p: nb_cure(p, SC.AX_BASE, daxis))
        add = sum(len(wide[s] - base[s]) for s in wide)
        diag = 0
        for p in space:
            q = (1 - p[0], 1 - p[1], p[2], p[3], p[4])
            if sig_of.get(q) not in (None, sig_of[p]):
                diag += 1
        tot_add += add
        tot_diag += diag
        print("      %-24s %-11s %4d diagonal moves leaving their "
              "class, %d new class edges" % (name, world, diag, add))
    print("      TOTAL %d class-leaving diagonal moves, %d new class "
          "edges" % (tot_diag, tot_add))
    check("K4: stalls are monotone -- adding edges never creates one",
          not viol_stall, "misses %s" % (viol_stall[:4],))
    check("K4: radii are monotone -- adding edges never raises one",
          not viol_rad, "misses %s" % (viol_rad[:4],))
    return totals


# ----------------------------------------------------------------- #
# E3: anatomy of every specimen that moved
# ----------------------------------------------------------------- #

def e3_anatomy(rows):
    print("\nE3  ANATOMY of every specimen whose status or radius "
          "moved")
    moved = 0
    for (name, world, setting, s0, space, sig_of, qranks, daxis,
         rec) in rows:
        base_st, base_r, _nb = rec["cure"]
        for vname, _vfn in VARIANTS:
            if vname == "cure":
                continue
            st, r, nb = rec[vname]
            if st == base_st and r == base_r:
                continue
            moved += 1
            print("  %s (%s %s) under %s: stall %s -> %s, r_class "
                  "%s -> %s" % (name, world, setting, vname,
                                "Y" if base_st else "n",
                                "Y" if st else "n",
                                fmt(base_r), fmt(r)))
            base_nb = rec["cure"][2]
            gained = nb[s0] - base_nb[s0]
            lost = base_nb[s0] - nb[s0]
            for t in sorted(gained, key=lambda t: qranks[t])[:6]:
                wit = None
                for p in [q for q in space if sig_of[q] == s0]:
                    for q in [x for x in _vfn(p, SC.AX_BASE, daxis)
                              if sig_of.get(x) == t]:
                        wit = (p, q)
                        break
                    if wit:
                        break
                print("      GAINED neighbour rank %d (own rank %d)"
                      "  witness %s -> %s"
                      % (qranks[t], qranks[s0],
                         SC.fmt_pol5(wit[0]) if wit else "?",
                         SC.fmt_pol5(wit[1]) if wit else "?"))
            for t in sorted(lost, key=lambda t: qranks[t])[:6]:
                print("      LOST neighbour rank %d (own rank %d)"
                      % (qranks[t], qranks[s0]))
    if not moved:
        print("  none: every specimen holds its status and its radius "
              "under every variant")
    for wide in WIDENING:
        vfn = dict(VARIANTS)[wide]
        print("")
        print("  the shape of every %s dissolution -- the improving "
              "moves %s adds:" % (wide, wide))
        bad, inf_only, any_diss = [], [], False
        for (name, world, setting, s0, space, sig_of, qranks, daxis,
             rec) in rows:
            if rec[wide][0] or not rec["cure"][0]:
                continue
            any_diss = True
            mvs = []
            for p in [q for q in space if sig_of[q] == s0]:
                base = set(nb_cure(p, SC.AX_BASE, daxis))
                for q in vfn(p, SC.AX_BASE, daxis):
                    t = sig_of.get(q)
                    if q in base or t is None or t == s0:
                        continue
                    if qranks[t] >= qranks[s0]:
                        continue
                    dt = (SC.AX_BASE.index(q[2])
                          - SC.AX_BASE.index(p[2]))
                    dc = (SC.AX_BASE.index(q[3])
                          - SC.AX_BASE.index(p[3]))
                    to_inf = q[2] is None or q[3] is None
                    same = (p[0], p[1], p[4]) == (q[0], q[1], q[4])
                    mvs.append((dt, dc, to_inf, same, qranks[t]))
                    if not same or to_inf or min(dt, dc) >= 0:
                        bad.append((wide, name, p, q))
                    if wide == "step2" and (dt, dc) not in (
                            (-2, 0), (0, -2)):
                        bad.append((wide, name, p, q))
            down = [m for m in mvs
                    if m[3] and not m[2] and min(m[0], m[1]) < 0]
            if not down:
                inf_only.append((wide, name))
            shp = sorted({(m[0], m[1], m[2]) for m in mvs})
            print("    %-24s %-11s %-11s %d improving (%d to refusal),"
                  " deltas %s"
                  % (name, world, setting, len(mvs),
                     sum(1 for m in mvs if m[2]),
                     " ".join("(%+d,%+d)%s"
                              % (a, b, " TO-INF" if c else "")
                              for a, b, c in shp)))
        if not any_diss:
            print("    none: %s dissolves no specimen the corpus's "
                  "own set stalls" % wide)
        check("%s: EVERY improving move it adds at a dissolution is "
              "a single patience step DOWNWARD, the other patience, "
              "both route bits and the drawdown unchanged, and none "
              "reaches refusal%s" % (wide, " -- by exactly -2 (F1)"
                                     if wide == "step2" else ""),
              not bad, "misses %s" % (bad[:3],))
        check("%s: and at least one such move exists at every "
              "dissolution, so none of them rests on a jump to "
              "REFUSAL (P9)" % wide,
              not inf_only, "misses %s" % (inf_only[:3],))
    return moved


# ----------------------------------------------------------------- #
# E5: the floor move read directly, and the spike1 pair
# ----------------------------------------------------------------- #

def e4_floor(lands):
    print("\nE5  THE FLOOR MOVE, read off the variant machinery")
    print("    at every member of every specimen: the doubly pinned")
    print("    policy at that member's own style pair, and its rank")
    bad, notzero = [], []
    for (_fam, name, world, setting, _sp, sig_of, mem, qranks,
         _dx, stalls, _f) in lands:
        for s0 in stalls:
            for p in sorted(mem[s0], key=SC.pol_key):
                if p[2] != 0 and p[3] != 0:
                    notzero.append((name, p))
                fl = (p[0], p[1], 0, 0, p[4])
                t = sig_of.get(fl)
                ok = (t is not None and t != s0
                      and qranks[t] < qranks[s0])
                if not ok:
                    bad.append((name, p, fl))
                print("    %-24s %-11s member %s" % (name, setting,
                                                     SC.fmt_pol5(p)))
                print("      floor %s  rank %s -> %s  %s"
                      % (SC.fmt_pol5(fl), qranks[s0],
                         "absent" if t is None else qranks[t],
                         "improves" if ok else "DOES NOT IMPROVE"))
    check("K6: the doubly pinned floor ranks strictly lower at every "
          "member of every specimen", not bad,
          "misses %s" % (bad[:3],))
    check("K6: and every member already carries a patience at 0, so "
          "the floor is ONE arbitrary patience jump away and no "
          "specimen can stall under clique -- the half of the "
          "derivation the rank check does not reach",
          not notzero, "misses %s" % (notzero[:3],))
    e5_corpus(lands)

    # the survivor and its controls, read against each other.
    # The survivor is located from the run -- the specimen still
    # stalling under step2 -- and the comparison set is every
    # specimen sharing its world and its setting, so nothing here
    # is named by hand.
    surv = None
    for (_fam, name, world, setting, space, sig_of, mem, qranks,
         daxis, stalls, _f) in lands:
        nb2 = edges(space, sig_of,
                    lambda q: nb_step2(q, SC.AX_BASE, daxis))
        st2 = stalls_of(nb2, qranks)
        for s0 in stalls:
            if s0 in st2:
                surv = (name, world, setting)
    print("")
    print("    THE STEP-2 SURVIVOR AND ITS CONTROLS -- every "
          "specimen sharing its world and setting:")
    if surv is None:
        print("      none: no specimen stalls under step2")
        return
    print("      survivor: %s (%s %s)" % surv)
    print("      from each member, the class rank reached at every "
          "value of each patience coordinate")
    print("      ('=' the member's own class, '-' no such policy, "
          "'*' strictly better)")
    for (_fam, name, world, setting, _sp, sig_of, mem, qranks,
         _dx, stalls, _f) in lands:
        if (world, setting) != (surv[1], surv[2]):
            continue
        for s0 in stalls:
            for pol in sorted(mem[s0], key=SC.pol_key):
                print("      %-24s %s  [rank %d]%s"
                      % (name, SC.fmt_pol5(pol), qranks[s0],
                         "   <- SURVIVOR" if name == surv[0] else ""))
                for coord, lab in ((2, "tree "), (3, "chain")):
                    cells = []
                    for v in SC.AX_BASE:
                        q = list(pol)
                        q[coord] = v
                        t = sig_of.get(tuple(q))
                        vv = "INF" if v is None else str(v)
                        if t is None:
                            cells.append("%s:-" % vv)
                        elif t == s0:
                            cells.append("%s:=" % vv)
                        else:
                            cells.append("%s:%d%s"
                                         % (vv, qranks[t],
                                            "*" if qranks[t]
                                            < qranks[s0] else ""))
                    print("        %s patience -> %s"
                          % (lab, "  ".join(cells)))


# ----------------------------------------------------------------- #
# E5b: the floor move over EVERY off-bottom class, and the doubly
# pinned policies' own classes per landscape
# ----------------------------------------------------------------- #

def e5_corpus(lands):
    print("\n  THE FLOOR MOVE OVER EVERY OFF-BOTTOM CLASS of the ten")
    print("  landscapes, not only the stall specimens:")
    absent = same = notbetter = 0
    nmem = ncls = 0
    nopat = set()
    samecls = set()
    for (_f, name, world, setting, _sp, sig_of, mem, qranks, _dx, _s,
         _fn) in lands:
        key = (name, world, setting)
        for s0, members in mem.items():
            if qranks[s0] == 0:
                continue
            ncls += 1
            jump = False
            for pol in members:
                nmem += 1
                fl = (pol[0], pol[1], 0, 0, pol[4])
                t = sig_of.get(fl)
                if t is None:
                    absent += 1
                elif t == s0:
                    same += 1
                    samecls.add((key, s0))
                elif qranks[t] >= qranks[s0]:
                    notbetter += 1
                for v in SC.AX_BASE:
                    for q in ((pol[0], pol[1], v, pol[3], pol[4]),
                              (pol[0], pol[1], pol[2], v, pol[4])):
                        if q == pol:
                            continue
                        u = sig_of.get(q)
                        if u is not None and u != s0 \
                                and qranks[u] < qranks[s0]:
                            jump = True
            if not jump:
                nopat.add((key, s0))
    print("    %d off-bottom classes, %d members" % (ncls, nmem))
    print("    floor policy absent from the space : %d" % absent)
    print("    floor lands in the member's OWN class: %d" % same)
    print("    floor lands lower-ranked but NOT better: %d" % notbetter)
    check("the doubly pinned floor ranks strictly lower at EVERY "
          "member whose floor is a distinct class -- %d of %d, the "
          "composite order and not the deficit" % (nmem - same,
                                                   nmem - same),
          not absent and not notbetter,
          "absent %d, not-better %d" % (absent, notbetter))
    check("and every member whose floor is its OWN class IS the "
          "doubly pinned policy, so the exceptions are members "
          "already at their floor and nothing else",
          same == sum(1 for (_f, _n, _w, _st, _sp, sig_of, mem, qranks,
                             _dx, _s, _fn) in lands
                      for s0, ms in mem.items() if qranks[s0]
                      for pol in ms
                      if pol[2] == 0 and pol[3] == 0
                      and sig_of.get((pol[0], pol[1], 0, 0,
                                      pol[4])) == s0),
          "same-class %d" % same)
    check("the classes holding their own doubly pinned floor are "
          "EXACTLY the classes no patience jump of any distance "
          "improves (%d of them)" % len(samecls),
          nopat == samecls,
          "nopat %d, samecls %d, overlap %d"
          % (len(nopat), len(samecls), len(nopat & samecls)))

    print("\n  THE DOUBLY PINNED POLICIES' OWN CLASSES, per")
    print("  landscape -- the floor theorem's premise is that they")
    print("  are ONE class and that it is the bottom:")
    bad_unres = []
    for (_f, name, world, setting, space, sig_of, _m, qranks, daxis,
         _s, _fn) in lands:
        pins = [pol for pol in space if pol[2] == 0 and pol[3] == 0]
        cls = {}
        for pol in pins:
            cls.setdefault(sig_of[pol], []).append(pol)
        ranks = sorted({qranks[t] for t in cls})
        one = len(cls) == 1 and ranks == [0]
        res = len(daxis) > 1 or setting != "unresourced"
        print("    %-24s %-11s %-11s %2d policies -> %2d class(es), "
              "ranks %s%s" % (name, world, setting, len(pins),
                              len(cls), ranks,
                              "" if one else "   <-- NOT one class"))
        if not res and not one:
            bad_unres.append(name)
    check("the premise holds at every UNRESOURCED landscape -- which "
          "is the scope the parent census proved it in",
          not bad_unres, "misses %s" % (bad_unres,))


def main():
    lands = collect()
    e0_controls(lands)
    if FAILURES:
        print("\nCONTROLS FAILED -- no verdict read")
        return 1
    rows = e1_sweep(lands)
    e2_lattice(lands)
    e3_anatomy(rows)
    e4_floor(lands)
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % FAILURES))
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
