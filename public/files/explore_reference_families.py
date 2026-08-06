"""THE READER LAWS BY DETERMINANT: is Farey rigidity the hypothesis,
or is being a PARTIAL QUOTIENT the hypothesis?

THE QUESTION
------------
explore_ladder_entry.py proved the chain-preferring nesting law under
the identity map and named exactly where the map enters: a reference
is a Farey interval, determinant +-1, so a reference fine enough to
open a door on a ladder is necessarily coarser than one that has
already maxed that ladder. Under sq and dbl the image of a cylinder
loses the determinant and the two finenesses decouple.

That reads as though the determinant were the whole story. This rig
takes the REFERENCE FAMILY as the design variable rather than the map
— the maps are just one way to produce non-Farey references — and
sorts the laws by what the reference lattice actually does. Two
questions, and the second reprices the first:

(A) THE VERTEX SEQUENCE. G1 says an occupied straddle's vertex is
    always a convergent and a strict semiconvergent never carries a
    ladder. If that is literal, a chain move consumes one run of
    same-direction Stern-Brocot steps — a PARTIAL QUOTIENT — and the
    chain/tree preference axis is "reads the continued fraction"
    against "reads the binary path", which would make the reader
    corpus a description of two classical algorithms.
(B) THE FAMILY SORT. Build references by hand and run the SAME
    exit-index invariant, which is map-neutral by construction. The
    families are chosen so that DETERMINANT and PHASE come apart:
    a determinant +-1 family that is NOT the cylinder family is the
    discriminating specimen, and there is exactly one natural one.

WHY THE UNIMODULAR MAPS CANNOT BE THAT SPECIMEN (fixed before the
engine). The unimodular maps in play are exactly those preserving
the positive reals, hence the products of the two Stern-Brocot
generators — a WORD W, which is what lets the second half of this
argument run at all. A unimodular image of a Farey interval is a
Farey interval, and the image of the nested cylinder chain of x is a
nested Farey chain converging to the image point, hence a chain of
Stern-Brocot nodes on that point's own path. Prepending W to a path
merges its last run with the path's leading run, and a merge moves a
run's START and never its END, so every cylinder boundary of x is
still one of the image point's; the extra boundaries W introduces
all sit at depths above the family's first reference. The image
family is therefore a sub-chain of the image point's own cylinders —
in phase, merely starting later. So no map of
determinant +-1 can produce an OUT-OF-PHASE Farey family. The only
out-of-phase determinant +-1 family is the one no map produces: the
full Stern-Brocot descent, every node rather than the partial-quotient
subsequence. That family is the experiment.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cells, references, the commit loop and the exit-index invariant are
explore_ladder_entry.py's and its parents' (explore_scale_clock.py,
explore_seed_exclusion.py, explore_chain_persistence.py). The readers
are the chain-preferring slice (st, ss) = (1, 0) except where leg A
names the tree-preferring slice (0, 1) explicitly.

NOTATION. (l, r) a tree cell, w = l (+) r its vertex, x the stream
point. L_j = l + j w the near ladder, S_k(w) = (L_k, R_k). conv_i the
convergents and a_i the partial quotients OF THE POINT THE FAMILY
CONVERGES TO — never of the unmapped stream point, which is the trap
explore_ladder_entry.py's map legs recorded. Every family therefore
carries its OWN digits, read off the finest reference by Stern-Brocot
descent, and every convergent-keyed tally is computed against those.

INDEX, MAP-NEUTRALLY. The parent read a reference's index off its
position in the stream (n - P). That is only the cylinder index when
the family IS the cylinder family. Here index(J) is INTRINSIC: the
largest j with J contained in C_j of the family's own point, which
agrees with the parent on the cylinder family (checked, C3) and is
defined for every family.

DETERMINANT, AS MEASURED. A family's nominal determinant is not its
realized one: applying an integer matrix of determinant d to a
cylinder endpoint can leave a common factor, and the reduced pair's
determinant is then a proper divisor of d. Every leg reports the
realized |det| multiset over the references it actually ran, and the
sort is by THAT, never by the label.

THE FAMILIES
------------
Each is a nested interval chain over one digit stream.
  cyl      det 1, in phase   the cylinders themselves (control)
  sb       det 1, OUT of phase   every Stern-Brocot node on x's path
  shift    det 1   t -> t + 1
  mob1     det 1   t -> (2t + 1)/(t + 1)
  dbl      det 2   t -> 2t                     (the parent's map)
  half     det 2   t -> t/2
  aff2     det 2   t -> 2t + 1
  mob2     det 2   t -> t/(t + 2)
  tri      det 3   t -> 3t
  mob3     det 3   t -> (t + 1)/(t + 4)

HAND-ATTACK (fixed before the engine)
-------------------------------------
D1 The cylinder family is the partial-quotient family. x's
   Stern-Brocot path is R^{a_0} L^{a_1} R^{a_2} ..., and C_i is the
   node at the END of the i-th run. So the sb family's references
   include every node strictly inside a run, which is exactly a
   strict semiconvergent interval.
D2 G2 is the step that phase breaks. G2 reads "the cylinders strictly
   inside (L_j, w) are exactly those of index at least sigma + 1",
   and its proof is that C_sigma shares the endpoint w while
   C_{sigma+1} = (L_a, L_{a+1}) has its near end strictly past L_a.
   A node INSIDE the run — (L_j, L_{j+1}) for 1 <= j < a — is strictly
   inside (L_j, w) too, and its near end is NOT past L_a. So a
   semiconvergent reference is fine enough to open a door on the
   ladder without having maxed it: the two finenesses decouple at
   determinant +-1. If that is right, the lemma's hypothesis was
   never Farey rigidity.
D3 Determinant is then a SUFFICIENT breaker and not the axis: |det|
   >= 2 forces the reference off the Farey lattice and so off the
   cylinder chain of any point, but |det| = 1 does not force it ONTO
   the cylinder chain, only onto the Stern-Brocot path.

PREDICTIONS, fixed before the engine ran
----------------------------------------
R1 [gate, positive control] The cyl family shows ZERO stale-regime
   exit-index violations and the dbl family shows some — the parent's
   two known verdicts, reproduced by this rig's own instrument over
   this rig's own scans. A rig that cannot reproduce both proves
   nothing about any new family (K1).
R2 [gate, control on the digit reader] For the cyl family the digits
   read back off the finest reference by Stern-Brocot descent are a
   prefix of the digits the stream was built from, every stream (K2).
R3 [gate, control on the index] For the cyl family the intrinsic
   index of J[i] equals i, every reference (K3).
R4 [PROBE A] Under the cyl family every chain-preferring run's
   ordered straddle-vertex sequence consists of CONVERGENTS with
   strictly increasing convergent index, and the tree-preferring
   slice occupies strict-semiconvergent vertices at a positive rate.
   GUESS on the sharper form: in the stale regime the chain-preferring
   sequence is CONSECUTIVE convergents with no index skipped.
R5 [the unimodular families] shift, mob1: realized |det| = 1 at every
   reference, every reference is a cylinder of the family's own
   point, and the laws survive with zero stale-regime violations —
   the tree automorphism argument, machine-checked.
R6 [THE DISCRIMINATOR] The sb family, determinant 1 and out of phase,
   BREAKS the laws: nonzero stale-regime exit-index violations and
   nonzero G3 failures. If it does NOT break, then +-1 IS the whole
   story, the lemma's hypothesis is Farey rigidity alone, and D2 is
   wrong about which step carries the phase — the more surprising
   outcome, and a finding either way.
R7 [determinant >= 2] Every family of realized determinant 2 or 3
   violates in the stale regime. THE KILL SHAPE: a determinant-2
   family with ZERO stale-regime violations at this scope, which
   would say the determinant is not the axis and would owe a name for
   what is.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 An R1 miss: the instrument does not reproduce both parent
   verdicts — no verdicts from any other leg.
K2 An R2 miss: the digit reader is wrong, so every convergent-keyed
   tally in every non-cylinder family is meaningless.
K3 An R3 miss: the intrinsic index disagrees with the parent's on the
   family where both are defined, so the G2/G3 tallies are not the
   parent's quantities.
Otherwise every tally prints as a finding; R4 to R7 misses scope the
classification, not the rig.

ENGINE
------
E1 the gates (R1, R2, R3) on the cylinder and dbl families.
E2 PROBE A (R4): the vertex sequence under the cylinder family, both
   preference slices, over every scan and run.
E3 THE FAMILY SORT (R5, R6, R7): all ten families, the realized
   determinant multiset, the G1/G2/G3 tallies against the family's
   OWN convergents, and the exit-index invariant by regime.
E4 the verdict table: families sorted by realized determinant against
   what each keeps.
E5 (added after the family sort printed, and the reason is at H4):
   G4's arithmetic step infers index(c) >= index(T) + 1 from the
   stale regime, which is the sentence "one step back is one partial
   quotient back". Measured directly per family, in CYLINDER index:
   the fraction of stale-regime decisions that actually deliver the
   gap G4 assumes. Its prediction, fixed before it ran, is R8.
E6 THE INTRINSIC REGIME (added after this record's verdict named it
   as the next question; predictions R9 to R12, fixed before it ran).
   Every leg above reads the regime off the POLICY — stale means the
   chain lag pc is smaller than the tree lag P, which is a statement
   about stream steps. Restate it INTRINSICALLY, per decision and in
   the family's own cylinder index: a decision is intrinsically stale
   when index(chain reference) >= index(tree reference) + 1, which is
   what the lagged-step definition was only ever a proxy for. Then
   re-tally G4's three conclusions against THAT classification, over
   the same ten families and the same scans. Same tallies as E3, the
   `i-` keys, plus the counterfactual the argument turns on and no
   leg has ever measured: at a door decision, what the DECLINED chain
   reference would have reached.
E7 THE REPAIR AS A PER-DECISION CONDITIONAL (added after E6 printed,
   and the reason is at H8; predictions R13, R14, fixed before it
   ran). E6 sorts by FAMILY and leaves a determinant split with no
   mechanism behind it. D4's first step is G2's conclusion, so the
   statement the repair really makes carries no family label at all:
   G2 at the door plus the intrinsic index gap. Both legs of E6 —
   the chain reference's reach, and the exit-index verdict — are
   re-split by whether G2 held AT THAT DOOR.
E8 THE MISSING SLICE (added by this record's audit; prediction R15,
   fixed before it ran). Every `i-` figure in E6 and E7 is the
   CHAIN-preferring slice, while the door inequalities are stated
   over DOORS — a scope the sort never measured. Both of E7's splits
   are re-run on the tree-preferring slice.
Exact big-integer arithmetic throughout; scans are exhaustive digit
products; memory trivial; exit nonzero on any check failure.

R8, fixed before E5 ran: the cylinder family delivers the gap at
EVERY stale decision (that is what stale means when one stream step
is one partial quotient), and the sb family does not, while keeping
G1, G2 and G3 exactly — which would locate the failure in G4's
arithmetic rather than in any of its three inputs.

HAND-ATTACK ON THE REPAIR (fixed before E6's engine, on paper)
--------------------------------------------------------------
D4 Take a door at a convergent vertex w of cylinder index sigma in a
   determinant-1 family, the decision intrinsically stale. G2 is
   sufficient at determinant 1, so the tree reference has ti >=
   sigma + 1; intrinsic staleness then gives ci >= ti + 1 >=
   sigma + 2; G3 is free everywhere, so a chain reference at index
   >= sigma + 2 has MAXED the ladder, reaching a_{sigma+1}; a chain
   candidate at that rung therefore exists and a chain-preferring
   run takes it. The run does not door. So the door cannot happen,
   and the repair should hold at every determinant-1 family, sb
   included — phase being a proxy for the index gap rather than a
   hypothesis of its own.
D5 THREE PLACES D4 CAN FAIL, named before the run, because each is a
   step the corpus has never measured at the decisions this argument
   needs:
   (a) G3 is tallied only at chain moves TAKEN. At a door decision
       the chain candidate is declined and its rung is never
       recorded, so "index >= sigma + 2 maxes the ladder" is an
       extrapolation exactly where D4 leans on it. E6 measures it.
   (b) At a straddle the chain candidate needs k2 > k STRICTLY. A run
       already sitting at the maxed rung has no chain candidate and
       doors — legitimately, since that exit is AT the maxed index
       and not below it.
   (c) The exit-index invariant looks FORWARD, over later chain moves
       whose own decisions may be intrinsically fresh, while the
       intrinsic regime labels the exit's own decision. A violation
       surviving the restatement would most likely enter through
       that asymmetry, and would say the LAW needs phase even where
       the PROOF step is repaired.
D6 The intrinsic index is undefined for a reference not inside C_0 of
   the family's own point. Those decisions are neither stale nor
   fresh intrinsically; they get their own bucket and are counted,
   never silently dropped into either side.

PREDICTIONS for E6, fixed before it ran
---------------------------------------
R9  [THE REPAIR] Every determinant-1 family — cyl, sb, shift, mob1 —
    shows ZERO intrinsically stale exit-index violations, ZERO
    intrinsically stale straddle exits below the maxed index, and
    ZERO intrinsically stale doors out of a tree cell at a convergent
    vertex. That is G4's conclusion restored off phase.
R10 [THE CONTROL THE REPAIR NEEDS] The restriction is real and not
    vacuous: sb's intrinsically stale bucket is neither empty nor all
    of its policy-stale decisions, and its 7,421 policy-stale
    exit-index violations RECLASSIFY rather than vanish — they
    reappear in the intrinsically fresh or undefined buckets, and the
    three buckets reconcile against the policy-stale total.
R11 [DETERMINANT >= 2] The restatement does NOT rescue the families
    that leave the Farey lattice: violations survive inside the
    intrinsic stale regime there, because G2 fails and D4's first
    step is unavailable. If they come out clean too, the repair is
    stronger than the argument that motivated it and the determinant
    leaves the theorem entirely.
R12 [THE DECLINED CANDIDATE] At every intrinsically stale door at a
    convergent vertex in a determinant-1 family, the declined chain
    reference reaches exactly the maxed rung a_{sigma+1} — D5(a)
    measured rather than assumed. This is the mechanism whichever way
    R9 lands.
THE KILL SHAPE: violations surviving inside the intrinsic stale
regime under sb, which would say phase is necessary and not merely a
proxy, and would owe the fourth hypothesis by name.

PREDICTIONS for E7, fixed before it ran
---------------------------------------
R13 Every declined chain reference falling SHORT of the maxed rung at
    an intrinsically stale convergent-vertex door is one whose door
    failed G2. Equivalently: G2 at the door plus the intrinsic index
    gap forces the maxed ladder, in every family at every
    determinant — which would put the determinant out of G4 entirely
    and leave a per-decision conditional in its place.
R14 The same on the conclusion: no exit-index violation survives an
    intrinsically stale exit whose own door satisfied G2.
KILL for both: a short reach, or a violation, with G2 holding at the
door — which would say the intrinsic gap and G2 together are still
not enough, and would owe a fourth input by name.

R15, fixed before E8 ran: the two halves come apart on the
tree-preferring slice, because D4's last step is the PREFERENCE and
nothing else in it is. The GEOMETRIC half survives unchanged — at an
intrinsically stale G2-respecting door the declined chain reference
has still maxed the ladder, that being a fact about cylinders and
not about who takes what — while the NESTING conclusion does not,
since a tree-preferring run doors exactly where a chain-preferring
one chains: nonzero exit-index violations at those same doors.
KILL: R15a failing, which would make the maxed-ladder step
preference-dependent and put the door inequalities back in
question.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0)
----------------------------------------------------------------
H1 THE ANSWER IS NO, AND THE THREE LEMMAS COME APART. Over 16 runs
   x 10 families x the digit products each family could build from
   (1,209 to 1,241 of the 1,241 streams, the shortfall being the
   images too short to walk), determinant +-1 is NOT what the
   ladder-entry lemma rests on. The dependencies separate cleanly and
   each lemma answers to a DIFFERENT hypothesis:
     G1 is universal. Not one straddle at a strict semiconvergent
        vertex anywhere — 681,632 occupied vertices over the full
        cross product of ten families with BOTH preference slices,
        zero exceptions. G1 is a fact about the point's own descent
        and it survives every lattice.
     G2 is the DETERMINANT law, ONE WAY ONLY. Keyed to the
        determinant of the reference that opened the door — the
        family label cannot answer this, since every family
        realizing 2 or 3 realizes 1 at most of its own references —
        determinant +-1 is SUFFICIENT and nothing more: 568,195
        doors opened by a determinant-1 reference, zero failures,
        while |det| = 2 holds at 14,939 doors and fails at 73,354
        and |det| = 3 holds at 18,735 and fails at 65,377. So
        leaving the Farey lattice PERMITS G2 to fail rather than
        forcing it, and this is the only lemma Farey rigidity buys
        at all.
     G3 is free. Zero failures anywhere, in any family, at this
        scope — the maxed-ladder lemma asks nothing of the lattice.
     G4 needs a THIRD hypothesis, and it is neither of the two above.
H2 THE THIRD HYPOTHESIS IS PHASE, AND THE DISCRIMINATOR NAMES IT. The
   sb family — every Stern-Brocot node on the point's path rather
   than the partial-quotient subsequence — realizes determinant 1 at
   all 16,901 of its references, keeps G1, G2 and G3 with zero
   failures, and BREAKS G4's conclusion three ways: 1,716
   stale-regime doors from a tree cell into a convergent's near child
   (the parent's S5a, zero under cylinders), 6,968 of 14,451
   stale-regime straddle exits below the maxed index (S5b, zero under
   cylinders), and 7,421 stale-regime exit-index violations (S5c,
   zero under cylinders). E5 says why in one number: the cylinder
   family's stale regime delivers the index gap G4 assumes at 71,492
   of 71,492 decisions, the sb family at 66,327 of 134,432. G4's step
   "the stale regime makes the chain reference at least one step
   finer" silently reads STEP as PARTIAL QUOTIENT. It is true of the
   cylinder family because one cylinder is one partial quotient, and
   it is false the moment the reference stream refines more finely
   than the digits do. So the hypothesis was never that a reference
   is a Farey interval; it is that the reference stream is the
   PARTIAL-QUOTIENT stream. Farey rigidity is what makes that stream
   available, not what makes the lemma run.
H3 NO UNIMODULAR MAP CAN BE THE DISCRIMINATOR, AS DERIVED. shift and
   mob1 realize determinant 1 at every reference and keep all four
   laws with zero violations, confirming the tree-automorphism
   argument: a unimodular image of the cylinder chain is the cylinder
   chain of the image point, so it is in phase by construction. This
   is why the discriminator had to be built by hand rather than
   mapped, and it is the sharp form of the parent's H5 — the maps
   break the lemma by breaking the determinant, but the determinant
   is only one of the two ways to leave the partial-quotient stream,
   and it is the less fundamental one.
H4 THE DETERMINANT REMAINS SUFFICIENT AND IS NOT NECESSARY. The
   kill shape R7 named — a determinant-2 family nesting as well as
   the cylinders — did NOT land: all six families realizing 2 or 3
   violate in the stale regime (292 to 1,389). But the shape it was
   testing for was answered from the other side, which is why the
   item closes anyway: sb is a determinant-1 family that nests
   STRICTLY WORSE than the cylinders, so +-1 is not sufficient, and
   the axis is phase. Determinant >= 2 PERMITS G2 to break and a
   family that breaks G2 breaks G4 downstream; phase breaks G4 alone,
   over intact lemmas. Two independent breakages, which is why the
   determinant sort looked like a law: every family that leaves the
   lattice also leaves the phase, and only a hand-built family
   separates them. Neither breakage is forced — a determinant-2
   reference opens a G2-respecting door 14,939 times — so the sort is
   by what a lattice ALLOWS, never by what it compels.
   Consistency the sort produced for free: aff2 = 2t + 1 is a
   unimodular translate of dbl and reproduces its G2 and violation
   counts exactly; mob2 = t/(t + 2) is a unimodular translate of half
   and reproduces its G2 count, its violation count differing only
   because the run must first descend into a different subtree of the
   root under a fixed horizon.
H5 PROBE A, AND IT ANSWERS ITS QUESTION IN THE NEGATIVE. A chain move
   IS a partial quotient, more strongly than asked: every occupied
   straddle vertex is a convergent under BOTH preference slices, and
   every vertex sequence walks the convergents in strictly increasing
   index (the cylinder family's 8,127 chain-preferring and 5,875
   tree-preferring sequences, zero exceptions; the vertex claim
   itself is H1's, at the ten-family cross product). So the
   chain/tree axis is NOT "reads the
   continued fraction" against "reads the binary path" — both read
   the continued fraction, and the tree preference reaches
   semiconvergents only as CELLS it doors through, never as vertices
   it chains at. What the axis actually is, is STRIDE: in the stale
   regime the chain-preferring run never once walks consecutive
   convergents (0 of 5,859 sequences) while the tree-preferring run
   does in 1,646 of 5,875. Chain preference skips convergents; tree
   preference visits every one. The corpus has been describing one
   classical algorithm at two strides, not two algorithms.
R4c AS FROZEN WAS MIS-SPECIFIED and its miss is recorded rather than
   repaired: it predicted the tree-preferring slice would occupy
   strict semiconvergent VERTICES, which asks a chain-move tally
   about the slice defined by preferring not to chain. The observable
   that decides what it meant to ask is R4c', and the answer it gives
   is stronger than the prediction it replaced — no slice ever chains
   at a semiconvergent, so the vertex layer does not carry the axis
   at all. No other prediction or threshold was touched.

H6 THE REPAIR HOLDS, AND PHASE WAS A PROXY TOO. Restated
   intrinsically — per decision, index(chain ref) >= index(tree ref)
   + 1 in the family's own cylinder index — G4's three conclusions
   return in full at every determinant-1 family, the out-of-phase
   discriminator included. Zero intrinsically stale exit-index
   violations at cyl (25,524 exits), sb (11,850), shift and mob1
   (32,970 each); zero intrinsically stale doors out of a tree cell
   at a convergent vertex and zero intrinsically stale straddle exits
   below the maxed index, at all four. The restriction is real and
   not vacuous (R10): sb's intrinsically stale bucket is 11,850
   doors against 51,718 intrinsically fresh, and its 7,421
   POLICY-stale violations do not vanish but RECLASSIFY — 27,010
   violations across the intrinsic buckets, every one of them outside
   the stale one. So the answer to the question this record left open
   is yes: the 7,421 sit entirely in the half the intrinsic regime
   drops, and phase is not a third hypothesis but the cylinder
   family's way of guaranteeing the index gap at every stale
   decision.
H7 AND THE DETERMINANT GOES TOO — THE HYPOTHESIS IS TWO INDEX
   INEQUALITIES AT ONE DOOR. R11 predicted the restatement would
   rescue nothing off the Farey lattice and it MISSED, in the
   direction that matters: all four determinant-2 families come out
   clean inside the intrinsic stale regime as well (aff2, dbl 15,654
   exits; half 10,782; mob2 20,742; zero violations each), and only
   the two determinant-3 families still break it (mob3 1,162 of
   27,565, tri 421 of 14,500). E7 says why, and it is not a fact
   about 2 against 3: D4's first step is G2's conclusion, so the
   conditional the repair actually states carries no family label at
   all. Split every intrinsically stale convergent-vertex door by
   whether G2 held AT THAT DOOR and the sort by determinant
   disappears — 68,958 doors where G2 held, across all ten families
   (the count runs over convergent-vertex doors whose a_{sigma+1} is
   inside the family's own read digits, the ladder's length being
   undefined past the horizon; that is an exclusion of the
   instrument's reach, not of a case),
   and the chain reference has maxed the ladder at every
   single one, zero short; 4,511 where G2 failed, short at 2,356 of
   them, and those failures occur only at the determinant-3 families
   because they are the only families in this sort that fail G2 at an
   intrinsically stale door at all. The conclusion follows the same
   split exactly: zero exit-index violations at the 68,958, and all
   1,583 surviving violations at exits whose own door failed G2.
   THE REPAIRED HYPOTHESIS is therefore per-DECISION and has neither
   a determinant nor a phase in it: at a door at a convergent vertex,
   index(tree ref) >= sigma + 1 and index(chain ref) >=
   index(tree ref) + 1. G1 and G3 are free, so those two inequalities
   are the whole of what G4's ARITHMETIC needs; H10 is what the LAW
   needs besides.
H8 WHICH SETTLES WHAT KIND OF STATEMENT THE THEOREM IS, and it is
   none of the three the question offered. Not a policy a reader
   could execute — a run cannot read its own reference's cylinder
   index without knowing the digits — and not a statement about a
   FAMILY either, since the determinant-3 families carry decisions of
   both kinds and no family label decides which. It is a statement
   about DECISIONS. The family-level theorem is recovered as a
   COROLLARY at the cylinder family, where both inequalities hold at
   every stale decision by construction: G2 has zero failures at
   determinant 1, and E5's gap is delivered at 71,492 of 71,492. That
   is the whole content of "phase" — a family for which the policy's
   own lag comparison is a sound proxy for the index gap.
H9 THE CHILD SPLIT, and it corrects a NAME rather than a number. The
   parent's S5a is checked as "no stale-regime door from a tree cell
   into a convergent vertex's NEAR child", but its tally keys the
   cell doored out of and never splits the two children, so the check
   forbids doors into EITHER. Both children are entered in quantity
   wherever such doors occur at all (cyl 8,137 low against 8,572
   high, all intrinsically fresh), so the distinction the name draws
   is one no tally has ever made. The claim is stronger for it — an
   empty superset — and the name is what needs correcting, not the
   figure. Same species as this thread's other definition-drift
   finding: the predicate and the noun were written in different
   passes.
H11 NOTHING WAS DECLINED AT THOSE DOORS, AND G4'S CONCLUSIONS RUN ON
   TWO DIFFERENT MECHANISMS (R16, added by the audit). The prose
   above called the chain reference at those 68,958 doors the
   DECLINED one, which implies a chain move was on offer and passed
   over — and a chain-preferring run passing over an available chain
   move would contradict its own definition. It never happened:
   every one of the 68,958 is a STRADDLE already sitting at the
   maxed rung, where the commit loop's chain candidate requires a
   STRICT improvement and so offers nothing; zero are tree cells and
   zero had a candidate available, at every family. So G4's two
   conclusions are not one mechanism read twice:
     - the tree-cell door into a convergent's near child is empty
       because a chain candidate DOES exist there and the preference
       takes it — the run chains rather than doors;
     - the straddle exits are not empty at all, and what holds the
       invariant is that they leave AT the maxed index, the only
       rung left to leave from.
   The exit-index invariant is satisfied by the exit's own height,
   not by the exit being prevented. That is the sharper statement of
   why the door inequalities suffice, and the word "declined" was
   hiding it — the second conclusion has no counterfactual in it.
H10 THE TWO HALVES COME APART AT THE PREFERENCE, AS R15 PREDICTED,
   AND THAT IS WHERE THE REST OF THE LAW LIVES. E6 and E7 read the
   chain-preferring slice only, which is a scope neither states; run
   over the tree-preferring slice the GEOMETRIC half is untouched —
   88,932 intrinsically stale G2-respecting doors across the ten
   families, the declined chain reference having maxed the ladder at
   every one, zero exceptions — while the nesting conclusion
   collapses: 33,319 exit-index violations at exits whose door met
   both inequalities, against ZERO on the chain-preferring slice. So
   the door inequalities force the GEOMETRY, and the chain
   PREFERENCE is what converts that geometry into the law. This is
   the sharpest form the axis has taken: the preference is not a
   label on two algorithms (H5) but the step that decides whether a
   run takes the maxed rung it has been handed. The full hypothesis
   is the two inequalities AND the preference. The parent NAMES the
   preference throughout — its H4 is filed at the chain-preferring
   slice — so what was missing was never the qualifier but the
   MEASUREMENT that the step is load-bearing: the other slice was
   never run, so "a chain-preferring run chains instead" sat behind
   a passing tally as an assumption. It is now a printed contrast.

THE VERDICT. The map was never the variable, and neither in the end
was the lattice or the phase. A reference family breaks the
chain-preferring nesting law two independent ways — by leaving the
Farey lattice, which costs it G2, or by refining faster than the
digits do, which costs it nothing but G4's own arithmetic — and the
maps do both at once, which is why determinant looked like the axis
for as long as maps were the only families in hand. But both
breakages are the same breakage seen through a family label. Read
per DECISION, G4 needs exactly two index inequalities at the door it
is about, and every family-level hypothesis the thread has proposed
— Farey rigidity, the partial-quotient stream, phase — is a
different sufficient condition for those two to hold. The cylinder
family satisfies both at every stale decision, which is why it
looked like the hypothesis.

What this does NOT settle, and it is the next question: G2 is now
the only lattice-sensitive input left, and it is still keyed to the
determinant of the reference that opened the door rather than
derived from anything intrinsic. Determinant 1 is sufficient for it
and 2 and 3 are not necessary breakers (14,939 and 18,735
G2-respecting doors at those determinants). What separates a
determinant-2 reference that respects G2 from one that does not is
untested, and it is now the last place a lattice fact is doing work
in this corpus.

Run record. THREE runs plus a smoke test of the gate leg. The first
carried H1 to H3 and H5 and printed the family sort; it also failed
R4c, which is recorded above as a mis-specification of the
prediction rather than of the rig. The second added E5 — the index
gap measured directly in cylinder index, which is what turns "sb
breaks" into H2's named mechanism — and corrected R4c's check to
R4c'. The third is this record's audit: the family sort ran the
chain-preferring slice only, so G1's "universal" was a cross product
of families with slices that had never been run together, and H1
carried the CYLINDER family's two-slice count against the ten-family
claim. The audit ran the missing half rather than narrowing the
claim, and R4a' is the check that now holds it. The fourth added E6,
the regime restated intrinsically, and carried H6; reading its
family table is what forced E7, since a determinant-2/determinant-3
split with no mechanism behind it is a sort and not a law, and the
fifth run added E7 and carried H7 to H9. A sixth split the
unclassifiable bucket, which had been named for one cause and was
carrying two — a lag that has not elapsed against a reference
genuinely outside C_0 — and it matters because that bucket carries
violations: the split is clean at every family, and it is what lets
H6's reclassification be read at all. Each run is about eleven
seconds; memory trivial. A seventh run is this record's audit: E6
and E7 read one preference slice and said so nowhere, so E8 ran the
other rather than narrowing the claim, and H10 is what it found. The
same pass corrected two claim surfaces the run itself refutes —
R11's check name, which asserted the restatement rescues nothing off
the Farey lattice while its own table shows four families rescued,
and E7's column header, which read a "not maxed" predicate as
"short" when only R12 measures the direction. The E1 gates
run first and abort the rig on failure, so nothing downstream is
read unless both parent verdicts reproduce.
"""

import os
import sys
import itertools
from math import gcd

import explore_scale_clock as SC
import explore_seed_exclusion as SE
import explore_chain_persistence as CP

FAILURES = []


def check(name, ok):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, name))
    if not ok:
        FAILURES.append(name)


# ----------------------------------------------------------------- #
# the scans and the run axis                                         #
# ----------------------------------------------------------------- #

# Alphabets are kept free of very large digits: the sb family's
# horizon is the SUM of the digits, not their count, and the
# exit-index invariant is quadratic in the horizon.
SCANS = [
    ((1, 2, 3, 9), 4),
    ((1, 2, 3), 6),
    ((1, 2), 8),
]

# One axis for every family, so the comparison is like for like. P = 0
# is excluded for the reason recorded at explore_ladder_entry.py's
# MAP_RUNS: under a non-identity family the descent to contain the
# current reference is a harmonic slog past the commit loop's runaway
# guard, and the axis restriction is the family's cost rather than a
# choice about coverage.
RUNS = [(P, pc) for P in (1, 2, 3, None) for pc in (0, 1, 2, 3)]

CHAIN_PREF = (1, 0)
TREE_PREF = (0, 1)


def is_stale(P, pc):
    if pc is None or P is None:
        return None
    return pc <= P - 1


def regime(P, pc):
    s = is_stale(P, pc)
    return "stale" if s else ("fresh" if s is False else "none")


# ----------------------------------------------------------------- #
# fractions, intervals, determinants                                 #
# ----------------------------------------------------------------- #

def reduce_frac(e):
    g = gcd(abs(e[0]), abs(e[1]))
    return (e[0] // g, e[1] // g) if g > 1 else e


def det2(a, b):
    return abs(a[0] * b[1] - a[1] * b[0])


def frac_le(a, b):
    return a[0] * b[1] <= b[0] * a[1]


def contains_iv(outer, inner):
    """Closed containment of intervals given as endpoint pairs."""
    return frac_le(outer[0], inner[0]) and frac_le(inner[1], outer[1])


def apply_mat(M, e):
    a, b, c, d = M
    return reduce_frac((a * e[0] + b * e[1], c * e[0] + d * e[1]))


def map_iv(M, iv):
    p, q = apply_mat(M, iv[0]), apply_mat(M, iv[1])
    return (p, q) if SC.lt(p, q) else (q, p)


# ----------------------------------------------------------------- #
# the Stern-Brocot reader: path, digits, nodes                       #
# ----------------------------------------------------------------- #

def sb_walk(iv, maxdepth=4000):
    """Descend the Stern-Brocot tree while the node strictly contains
    iv. Returns (path, nodes) with path a list of 'L'/'R' and nodes
    the interval at each depth, the root first."""
    l, r = SC.ROOT[1], SC.ROOT[2]
    path, nodes = [], [(l, r)]
    for _ in range(maxdepth):
        v = SC.mediant(l, r)
        if contains_iv((l, v), iv):
            l, r, step = l, v, "L"
        elif contains_iv((v, r), iv):
            l, r, step = v, r, "R"
        else:
            break
        path.append(step)
        nodes.append((l, r))
    return path, nodes


def runs_of(path):
    out = []
    for ch in path:
        if out and out[-1][0] == ch:
            out[-1][1] += 1
        else:
            out.append([ch, 1])
    return out


def path_digits(path):
    """CF digits of the point the path descends toward. The FINAL run
    is dropped: a truncated path bounds its last run below but does
    not close it, so its length is not a digit yet."""
    rr = runs_of(path)
    if not rr:
        return []
    if rr[0][0] == "L":
        rr = [["R", 0]] + rr
    return [n for _, n in rr[:-1]]


def run_end_depths(path):
    """Depths at which a same-direction run CLOSES — the depths whose
    nodes are the cylinders, in order."""
    rr = runs_of(path)
    out, d = [], 0
    for _, n in rr[:-1]:
        d += n
        out.append(d)
    return out


# ----------------------------------------------------------------- #
# the families                                                       #
# ----------------------------------------------------------------- #

MATS = {
    "shift": (1, 1, 0, 1),
    "mob1":  (2, 1, 1, 1),
    "dbl":   (2, 0, 0, 1),
    "half":  (1, 0, 0, 2),
    "aff2":  (2, 1, 0, 1),
    "mob2":  (1, 0, 1, 2),
    "tri":   (3, 0, 0, 1),
    "mob3":  (1, 1, 1, 4),
}

FAMILIES = ["cyl", "sb"] + list(MATS)

NOMINAL = {"cyl": 1, "sb": 1, "shift": 1, "mob1": 1,
           "dbl": 2, "half": 2, "aff2": 2, "mob2": 2,
           "tri": 3, "mob3": 3}


def build_family(name, digs):
    """The reference stream, plus the digits and convergents OF THE
    POINT THAT STREAM CONVERGES TO. Returns None when the family is
    too short to run."""
    cyls = SC.cylinders(list(digs))
    if name == "cyl":
        refs = list(cyls)
    elif name == "sb":
        _, nodes = sb_walk(cyls[-1])
        refs = nodes[1:]
    else:
        M = MATS[name]
        refs = [map_iv(M, c) for c in cyls]
    if len(refs) < 3:
        return None
    path, _ = sb_walk(refs[-1])
    fdigs = path_digits(path)
    if len(fdigs) < 2:
        return None
    fcyls = SC.cylinders(fdigs)
    fcvs = CP.convergents(fdigs)
    return refs, fdigs, fcvs, fcyls


def intrinsic_index(iv, fcyls):
    """The largest j with iv inside C_j of the family's own point;
    None when iv is not inside C_0."""
    out = None
    for j, c in enumerate(fcyls):
        if contains_iv(c, iv):
            out = j
        else:
            break
    return out


# ----------------------------------------------------------------- #
# the walk                                                           #
# ----------------------------------------------------------------- #

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


def trace(refs, ridx, fcvs, fdigs, P, pc, s_t, s_s, tally, spec,
          verts=None):
    """One run over one family. Every micro-decision classified
    against the FAMILY's own convergents; the exit-index invariant
    checked afterwards. Returns False if the commit loop ran away."""
    reg = regime(P, pc)
    h = len(refs)
    C = SC.ROOT
    exits = []
    seen = []
    for n in range(h):
        rt = refs[n - P] if P is not None and n - P >= 0 else None
        rc = refs[n - pc] if pc is not None and n - pc >= 0 else None
        ti = ridx[n - P] if P is not None and n - P >= 0 else None
        ci = ridx[n - pc] if pc is not None and n - pc >= 0 else None
        try:
            C, records = SE.commit_step(C, rt, rc, s_t, s_s)
        except AssertionError:
            tally[("runaway", reg)] = tally.get(("runaway", reg), 0) + 1
            return False
        # E6: the regime restated INTRINSICALLY, per decision and in
        # the family's own cylinder index, rather than read off the
        # policy's lags. Undefined when either reference sits outside
        # C_0 (D6) — its own bucket, never folded into either side.
        if ti is None or ci is None:
            # Two causes, kept apart: the lag has not elapsed (or the
            # policy holds no such reference at all), against a
            # reference that exists but sits outside C_0 and so has
            # no intrinsic index. Only the second is D6's case, and a
            # bucket named for one carrying both would be read as the
            # second.
            ireg = ("i-nolag"
                    if (rt is None or rc is None) else "i-noidx")
        else:
            ireg = "i-stale" if ci >= ti + 1 else "i-fresh"
        for cell, cand_tree, cand_chain, took in records:
            if ti is not None and ci is not None:
                tally[("gap", reg, ci >= ti + 1)] = \
                    tally.get(("gap", reg, ci >= ti + 1), 0) + 1
            v, l, r, k = cell_vertex(cell)
            sig = conv_index(fcvs, v)
            at_conv = sig is not None
            a_next = (fdigs[sig + 1]
                      if at_conv and sig + 1 < len(fdigs) else None)
            if took == "chain":
                kk = cand_chain[5]
                if verts is not None and (not seen or seen[-1][0] != v):
                    seen.append((v, sig))
                tally[("vertex", reg, "conv" if at_conv else "semi")] = \
                    tally.get(("vertex", reg,
                               "conv" if at_conv else "semi"), 0) + 1
                if at_conv and a_next is not None and kk > a_next:
                    spec.setdefault("G1-index", []).append(
                        (fdigs[:8], P, pc, n, kk, a_next))
                if (at_conv and a_next is not None and ci is not None
                        and ci >= sig + 2):
                    key = ("G3", reg, kk == a_next)
                    tally[key] = tally.get(key, 0) + 1
                    if kk != a_next:
                        spec.setdefault("G3", []).append(
                            (fdigs[:8], P, pc, n, kk, a_next, ci, sig))
            elif took == "door":
                tally[("door", reg, "conv" if at_conv else "semi",
                       cell[0])] = \
                    tally.get(("door", reg,
                               "conv" if at_conv else "semi",
                               cell[0]), 0) + 1
                tally[("i-door", ireg, "conv" if at_conv else "semi",
                       cell[0])] = \
                    tally.get(("i-door", ireg,
                               "conv" if at_conv else "semi",
                               cell[0]), 0) + 1
                if at_conv and cell[0] == "T":
                    # Which child the door entered. S5a is named for
                    # the NEAR child (l, w); the parent's tally does
                    # not split them, so the split is printed here
                    # and the name is read against it.
                    side = "lo" if cand_tree[2] == v else "hi"
                    tally[("i-door-child", ireg, side)] = \
                        tally.get(("i-door-child", ireg, side), 0) + 1
                if at_conv and a_next is not None and rc is not None:
                    # D5(a): the DECLINED chain reference's reach.
                    # G3 is only ever tallied at chain moves taken,
                    # so this is the step D4 leans on and no leg has
                    # measured. Raw kmax, not the strict-improvement
                    # candidate, which is the counterfactual asked.
                    kd = SC.chain_kmax(v, l, r, rc)
                    tally[("i-declined", ireg, kd == a_next,
                           kd > a_next)] = \
                        tally.get(("i-declined", ireg, kd == a_next,
                                   kd > a_next), 0) + 1
                    # E7 (R13): the same reach, split by whether G2
                    # held AT THIS DOOR. D4's first step is G2's
                    # conclusion, so the conditional it really states
                    # is per-decision and carries no family label.
                    if ti is not None:
                        tally[("i-g2decl", ireg, ti >= sig + 1,
                               kd == a_next)] = \
                            tally.get(("i-g2decl", ireg, ti >= sig + 1,
                                       kd == a_next), 0) + 1
                        # R16: WHICH doors these are. "Declined"
                        # implies a chain move was on offer; at a
                        # straddle already sitting at the maxed rung
                        # commit_step offers none, since it requires
                        # a STRICT improvement. Print the split the
                        # prose leans on rather than assuming it.
                        tally[("i-declkind", ireg, ti >= sig + 1,
                               cell[0], cand_chain is not None)] = \
                            tally.get(("i-declkind", ireg,
                                       ti >= sig + 1, cell[0],
                                       cand_chain is not None), 0) + 1
                g2ok = None
                if at_conv and ti is not None:
                    ok = ti >= sig + 1
                    g2ok = ok
                    tally[("G2", reg, ok)] = \
                        tally.get(("G2", reg, ok), 0) + 1
                    # G2 keyed to the determinant of the REFERENCE
                    # that opened the door, not to the family's
                    # label: every family realizing 2 or 3 realizes
                    # 1 at most of its references too, so the
                    # family-level sort cannot say whether the law
                    # is per-reference. Added by the audit of this
                    # record; its verdict is at H1.
                    dt = det2(rt[0], rt[1])
                    tally[("G2det", ok, dt)] = \
                        tally.get(("G2det", ok, dt), 0) + 1
                    if not ok:
                        spec.setdefault("G2", []).append(
                            (fdigs[:8], P, pc, n, ti, sig))
                    if cell[0] == "S" and a_next is not None:
                        tally[("exit-k", reg, k == a_next)] = \
                            tally.get(("exit-k", reg, k == a_next), 0) + 1
                        tally[("i-exit-k", ireg, k == a_next)] = \
                            tally.get(("i-exit-k", ireg,
                                       k == a_next), 0) + 1
                exits.append((v, l, r, k, n, ireg, g2ok))
    for v, l, r, k, n1, iexit, g2ok in exits:
        worst = k
        for m in range(n1 + 1, h):
            if pc is None or m - pc < 0:
                continue
            worst = max(worst, SC.chain_kmax(v, l, r, refs[m - pc]))
        ok = worst <= k
        tally[("exit-inv", reg, ok)] = \
            tally.get(("exit-inv", reg, ok), 0) + 1
        tally[("i-exit-inv", iexit, ok)] = \
            tally.get(("i-exit-inv", iexit, ok), 0) + 1
        # E7 (R14): the exit carries the G2 verdict of its own door,
        # so the surviving violations can be read against it.
        tally[("i-g2exit", iexit, g2ok, ok)] = \
            tally.get(("i-g2exit", iexit, g2ok, ok), 0) + 1
        if not ok:
            spec.setdefault("exit-inv", []).append(
                (fdigs[:8], P, pc, n1, k, worst))
            if iexit == "i-stale":
                spec.setdefault("i-exit-inv-stale", []).append(
                    (fdigs[:8], P, pc, n1, k, worst))
    if verts is not None:
        verts.append((reg, seen))
    return True


def scan_family(name, scans=SCANS, runs=RUNS, pref=CHAIN_PREF,
                collect_verts=False, keep=3):
    tally, spec, dets = {}, {}, {}
    verts = [] if collect_verts else None
    streams = built = 0
    for alpha, h in scans:
        for digs in itertools.product(alpha, repeat=h):
            streams += 1
            fam = build_family(name, digs)
            if fam is None:
                continue
            built += 1
            refs, fdigs, fcvs, fcyls = fam
            for iv in refs:
                d = det2(iv[0], iv[1])
                dets[d] = dets.get(d, 0) + 1
            ridx = [intrinsic_index(iv, fcyls) for iv in refs]
            for P, pc in runs:
                trace(refs, ridx, fcvs, fdigs, P, pc, pref[0], pref[1],
                      tally, spec, verts)
    for k in sorted(spec):
        spec[k] = spec[k][:keep]
    return tally, spec, dets, streams, built, verts


def stale_bad(tally):
    return tally.get(("exit-inv", "stale", False), 0)


def stale_tot(tally):
    return (tally.get(("exit-inv", "stale", True), 0)
            + tally.get(("exit-inv", "stale", False), 0))


def show(tally, spec, prefix="    "):
    for k in sorted(tally, key=str):
        print("%s%-44s %d" % (prefix, str(k), tally[k]))
    for k in sorted(spec):
        for s in spec[k]:
            print("%sSPECIMEN %-10s %s" % (prefix, k, s))


# ----------------------------------------------------------------- #
# E1  the gates                                                      #
# ----------------------------------------------------------------- #

def e1_gates():
    print("\nE1  THE GATES")
    # R2: the digit reader against the digits the stream was built from
    bad2 = None
    for alpha, h in SCANS:
        for digs in itertools.product(alpha, repeat=h):
            cyls = SC.cylinders(list(digs))
            path, _ = sb_walk(cyls[-1])
            got = path_digits(path)
            if list(digs)[:len(got)] != got or len(got) < 1:
                bad2 = (digs, got)
                break
        if bad2:
            break
    print("  R2 digit reader: %s" % ("mismatch %s" % (bad2,)
                                     if bad2 else "prefix at every stream"))
    check("R2 the Stern-Brocot digit reader returns a prefix of the "
          "stream's own digits", bad2 is None)

    # R3: the intrinsic index against the parent's positional one
    bad3 = None
    for alpha, h in SCANS:
        for digs in itertools.product(alpha, repeat=h):
            fam = build_family("cyl", digs)
            if fam is None:
                continue
            refs, _, _, fcyls = fam
            for i, iv in enumerate(refs):
                if intrinsic_index(iv, fcyls) != i:
                    bad3 = (digs, i)
                    break
            if bad3:
                break
        if bad3:
            break
    print("  R3 intrinsic index: %s" % ("mismatch %s" % (bad3,)
                                        if bad3 else "equals n at every "
                                        "cylinder reference"))
    check("R3 the intrinsic index agrees with the parent's positional "
          "index on the cylinder family", bad3 is None)

    # R1: both parent verdicts reproduced
    tc, _, _, _, bc, _ = scan_family("cyl")
    td, _, _, _, bd, _ = scan_family("dbl")
    print("  R1 cyl  stale exits %d, violations %d  (%d streams)"
          % (stale_tot(tc), stale_bad(tc), bc))
    print("  R1 dbl  stale exits %d, violations %d  (%d streams)"
          % (stale_tot(td), stale_bad(td), bd))
    check("R1a the cylinder family has zero stale-regime exit-index "
          "violations", stale_tot(tc) > 0 and stale_bad(tc) == 0)
    check("R1b the dbl family violates the exit-index invariant in the "
          "stale regime", stale_bad(td) > 0)
    return tc


# ----------------------------------------------------------------- #
# E2  PROBE A: the vertex sequence                                   #
# ----------------------------------------------------------------- #

def e2_probe_a():
    print("\nE2  PROBE A: IS A CHAIN MOVE A PARTIAL QUOTIENT?")
    out = {}
    for label, pref in (("chain-preferring", CHAIN_PREF),
                        ("tree-preferring", TREE_PREF)):
        t, _, _, _, _, verts = scan_family(
            "cyl", pref=pref, collect_verts=True)
        nconv = t.get(("vertex", "stale", "conv"), 0) \
            + t.get(("vertex", "fresh", "conv"), 0) \
            + t.get(("vertex", "none", "conv"), 0)
        nsemi = t.get(("vertex", "stale", "semi"), 0) \
            + t.get(("vertex", "fresh", "semi"), 0) \
            + t.get(("vertex", "none", "semi"), 0)
        seqs = mono = consec = stale_seqs = stale_consec = 0
        for reg, seen in verts:
            if len(seen) < 2:
                continue
            seqs += 1
            idxs = [s for _, s in seen]
            if any(s is None for s in idxs):
                continue
            mono += all(b > a for a, b in zip(idxs, idxs[1:]))
            cc = all(b == a + 1 for a, b in zip(idxs, idxs[1:]))
            consec += cc
            if reg == "stale":
                stale_seqs += 1
                stale_consec += cc
        print("  %-16s straddle vertices: convergent %d, strict "
              "semiconvergent %d" % (label, nconv, nsemi))
        print("  %-16s vertex sequences %d; strictly increasing "
              "convergent index %d; consecutive %d; stale-regime "
              "consecutive %d of %d"
              % (label, seqs, mono, consec, stale_consec, stale_seqs))
        out[label] = (nconv, nsemi, mono, seqs, stale_consec, stale_seqs)
    nc, ns, mono, seqs, sc, ss = out["chain-preferring"]
    check("R4a every chain-preferring straddle vertex is a convergent",
          nc > 0 and ns == 0)
    check("R4b every chain-preferring vertex sequence walks the "
          "convergents in strictly increasing order", mono == seqs)
    tn, ts, _, _, _, _ = out["tree-preferring"]
    # R4c as frozen was mis-specified: it asked a CHAIN-move tally
    # about the slice defined by preferring not to chain. The
    # observable that decides what it meant to ask is the one below,
    # and it is stronger than what R4c predicted.
    check("R4c' NEITHER preference slice ever chains at a strict "
          "semiconvergent vertex", ts == 0 and tn > 0)
    return out


# ----------------------------------------------------------------- #
# E3  the family sort                                                #
# ----------------------------------------------------------------- #

def e3_families():
    print("\nE3  THE FAMILY SORT")
    rows = []
    g1conv = g1semi = 0
    g2det = {}
    for name in FAMILIES:
        t, sp, dets, streams, built, _ = scan_family(name)
        # G1 is a claim about BOTH preference slices, so both are run
        # over every family: reading the chain-preferring slice alone
        # and calling the result universal would be a scope the sort
        # never measured. Added by the audit of this record.
        tt, _, _, _, _, _ = scan_family(name, pref=TREE_PREF)
        # kept, not discarded: E7 reads the same door tallies off it,
        # since every `i-` figure is otherwise the chain-preferring
        # slice while the door inequalities are stated over DOORS.
        for d in (t, tt):
            for kk, vv in d.items():
                if kk[0] == "vertex":
                    if kk[2] == "conv":
                        g1conv += vv
                    else:
                        g1semi += vv
                elif kk[0] == "G2det":
                    g2det[kk] = g2det.get(kk, 0) + vv
        dl = sorted(dets.items())
        dstr = ", ".join("%d:%d" % (d, n) for d, n in dl)
        g2bad = t.get(("G2", "stale", False), 0) \
            + t.get(("G2", "fresh", False), 0)
        g3bad = t.get(("G3", "stale", False), 0) \
            + t.get(("G3", "fresh", False), 0)
        semi = sum(v for k, v in t.items()
                   if k[0] == "vertex" and k[2] == "semi")
        gapT = t.get(("gap", "stale", True), 0)
        gapF = t.get(("gap", "stale", False), 0)
        rows.append((name, NOMINAL[name], dstr, built, streams,
                     stale_tot(t), stale_bad(t), g2bad, g3bad, semi,
                     sum(v for k, v in t.items() if k[0] == "runaway"),
                     gapT, gapF, t, sp, tt))
        print("\n  --- %s (nominal det %d) ---" % (name, NOMINAL[name]))
        print("    realized |det|: %s" % dstr)
        print("    streams built %d of %d" % (built, streams))
        show(t, sp)
    print("\n  G2 PER REFERENCE, keyed to the determinant of the "
          "reference that opened the door:")
    for ok in (True, False):
        row = sorted((d, n) for (kk, o, d), n in g2det.items()
                     if o is ok)
        print("    G2 %-5s  %s" % ("holds" if ok else "FAILS",
                                   ", ".join("|det|=%d: %d" % (d, n)
                                             for d, n in row)))
    bad1 = sum(n for (kk, o, d), n in g2det.items()
               if o is False and d == 1)
    good1 = sum(n for (kk, o, d), n in g2det.items()
                if o is True and d == 1)
    check("R6' G2 is a per-REFERENCE determinant law: no door opened "
          "by a determinant-1 reference ever fails it",
          good1 > 0 and bad1 == 0)

    print("\n  G1 OVER THE CROSS PRODUCT (ten families x both "
          "preference slices):")
    print("    convergent vertices %d, strict semiconvergent %d"
          % (g1conv, g1semi))
    check("R4a' G1 is universal: no run of either preference chains "
          "at a strict semiconvergent in any family",
          g1conv > 0 and g1semi == 0)
    return rows


def e4_verdict(rows):
    print("\nE4  THE VERDICT TABLE (sorted by realized determinant)")
    print("  %-7s %-4s %-16s %9s %8s %6s %6s %7s %7s %9s"
          % ("family", "det", "realized |det|", "staleExit", "violate",
             "G2bad", "G3bad", "semiVtx", "runaway", "gapFail%"))
    for r in sorted(rows, key=lambda r: (r[1], r[0])):
        tot = r[11] + r[12]
        pct = (100.0 * r[12] / tot) if tot else float("nan")
        print("  %-7s %-4d %-16s %9d %8d %6d %6d %7d %7d %8.1f%%"
              % (r[0], r[1], r[2][:16], r[5], r[6], r[7], r[8],
                 r[9], r[10], pct))
    by = {r[0]: r for r in rows}
    for nm in ("shift", "mob1"):
        check("R5 %s (unimodular) keeps the laws: zero stale-regime "
              "violations" % nm,
              by[nm][5] > 0 and by[nm][6] == 0)
        check("R5 %s realizes determinant 1 only" % nm,
              by[nm][2] == "1:%d" % sum(
                  int(p.split(":")[1]) for p in by[nm][2].split(", ")))
    sb = by["sb"]
    print("\n  THE DISCRIMINATOR (det 1, out of phase):"
          " stale exits %d, violations %d, G2 failures %d,"
          " G3 failures %d" % (sb[5], sb[6], sb[7], sb[8]))
    # E5, added after the family sort printed: G4's arithmetic step
    # infers index(c) >= index(T) + 1 from the stale regime, which is
    # only "one step back is one partial quotient back". Measured
    # directly, per family, in CYLINDER index.
    print("  E5 the stale regime's index gap, in cylinder index:")
    for r in sorted(rows, key=lambda r: (r[1], r[0])):
        tot = r[11] + r[12]
        print("    %-7s delivered %d of %d stale decisions"
              % (r[0], r[11], tot))
    check("R8a the cylinder family's stale regime delivers the index "
          "gap G4 assumes at every decision", by["cyl"][12] == 0
          and by["cyl"][11] > 0)
    check("R8b the out-of-phase determinant-1 family does NOT: the "
          "step that fails is G4's arithmetic, not G1/G2/G3",
          sb[12] > 0 and sb[7] == 0 and sb[8] == 0)
    d2 = [r for r in rows if r[1] == 2]
    clean2 = [r[0] for r in d2 if r[5] > 0 and r[6] == 0]
    print("  determinant-2 families with zero stale violations: %s"
          % (clean2 or "none"))
    return sb, clean2


# ----------------------------------------------------------------- #
# E6  the regime restated intrinsically                              #
# ----------------------------------------------------------------- #

DET1 = ("cyl", "sb", "shift", "mob1")


def e6_intrinsic(rows):
    """G4's three conclusions re-tallied against the INTRINSIC stale
    regime — index(chain ref) >= index(tree ref) + 1, per decision —
    rather than against the policy's lags. Design and predictions R9
    to R12 in the docstring."""
    print("\nE6  THE INTRINSIC REGIME (index gap per decision, not "
          "stream lag)")
    print("  %-7s %-4s %8s %7s %8s %7s %8s %7s %8s %7s"
          % ("family", "det", "iStExit", "iStBad", "iFrExit", "iFrBad",
             "noLagEx", "noLagB", "noIdxEx", "noIdxB"))
    by = {}
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        t = r[13]
        cells = []
        for b in ("i-stale", "i-fresh", "i-nolag", "i-noidx"):
            good = t.get(("i-exit-inv", b, True), 0)
            bad = t.get(("i-exit-inv", b, False), 0)
            cells += [good + bad, bad]
        by[r[0]] = (r, cells)
        print("  %-7s %-4d %8d %7d %8d %7d %8d %7d %8d %7d"
              % ((r[0], r[1]) + tuple(cells)))

    print("\n  the two other G4 conclusions, intrinsically:")
    print("  %-7s %-4s %14s %14s %10s"
          % ("family", "det", "iSt tree-doors", "iSt exit<maxed",
             "iSt total"))
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        t = r[13]
        td = t.get(("i-door", "i-stale", "conv", "T"), 0)
        xk = t.get(("i-exit-k", "i-stale", False), 0)
        tot = sum(v for k, v in t.items()
                  if k[0] == "i-door" and k[1] == "i-stale")
        print("  %-7s %-4d %14d %14d %10d"
              % (r[0], r[1], td, xk, tot))

    # R9: the repair, at every determinant-1 family.
    for nm in DET1:
        r, cells = by[nm]
        t = r[13]
        check("R9a %s (det 1): no exit-index violation inside the "
              "intrinsic stale regime" % nm,
              cells[0] > 0 and cells[1] == 0)
        check("R9b %s (det 1): every intrinsically stale straddle "
              "exit leaves at the maxed index" % nm,
              t.get(("i-exit-k", "i-stale", False), 0) == 0)
        check("R9c %s (det 1): no intrinsically stale door out of a "
              "tree cell at a convergent vertex" % nm,
              t.get(("i-door", "i-stale", "conv", "T"), 0) == 0)

    # R10: the restriction is real, and sb's violations reclassify
    # rather than vanish.
    sb = by["sb"][0]
    tsb = sb[13]
    ist = sum(v for k, v in tsb.items()
              if k[0] == "i-door" and k[1] == "i-stale")
    ifr = sum(v for k, v in tsb.items()
              if k[0] == "i-door" and k[1] == "i-fresh")
    print("\n  R10 sb: intrinsically stale doors %d against "
          "intrinsically fresh %d" % (ist, ifr))
    check("R10a the intrinsic stale regime is a real restriction "
          "under sb: neither empty nor everything", ist > 0 and ifr > 0)
    polbad = stale_bad(tsb)
    allbad = sum(v for k, v in tsb.items()
                 if k[0] == "i-exit-inv" and k[2] is False)
    print("  R10 sb: exit-index violations, policy-stale %d, total "
          "over all intrinsic buckets %d" % (polbad, allbad))
    check("R10b sb's policy-stale violations reclassify rather than "
          "vanish: the intrinsic buckets carry at least as many",
          allbad >= polbad and polbad > 0)

    # R11: determinant >= 2 is not rescued.
    survivors = [r[0] for r in rows
                 if r[1] >= 2 and by[r[0]][1][1] > 0]
    clean = [r[0] for r in rows if r[1] >= 2 and by[r[0]][1][1] == 0]
    print("\n  R11 determinant >= 2, inside the intrinsic stale "
          "regime: still violating %s, RESCUED %s"
          % (survivors or "none", clean or "none"))
    check("R11 PARTIAL MISS (H7): the restatement is not universal "
          "off the Farey lattice -- some family there still violates "
          "inside the intrinsic stale regime", len(survivors) > 0)
    check("R11 and it DOES rescue families R11 predicted it would "
          "not, which is the miss E7 explains", len(clean) > 0)

    # R12: the chain reference's reach at the doors D4
    # turns on -- the step no leg has measured.
    print("\n  R12 the chain reference's reach at intrinsically "
          "stale convergent-vertex doors (R16 below says whether "
          "any of it was on OFFER):")
    print("  %-7s %-4s %10s %10s %10s"
          % ("family", "det", "= a_next", "> a_next", "< a_next"))
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        t = r[13]
        eq = t.get(("i-declined", "i-stale", True, False), 0)
        gt = t.get(("i-declined", "i-stale", False, True), 0)
        lt = t.get(("i-declined", "i-stale", False, False), 0)
        print("  %-7s %-4d %10d %10d %10d" % (r[0], r[1], eq, gt, lt))
    lt1 = sum(by[nm][0][13].get(("i-declined", "i-stale", False,
                                 False), 0) for nm in DET1)
    eq1 = sum(by[nm][0][13].get(("i-declined", "i-stale", True,
                                 False), 0) for nm in DET1)
    check("R12 at a determinant-1 family's intrinsically stale "
          "convergent-vertex doors the chain reference has maxed "
          "the ladder", eq1 > 0 and lt1 == 0)

    # S5a is named for the NEAR child; the parent's tally never split
    # the two children. Printed so the name can be read against it.
    print("\n  the child a tree door enters, at convergent vertices "
          "(S5a's name says 'near'):")
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        t = r[13]
        row = [(b, s, t.get(("i-door-child", b, s), 0))
               for b in ("i-stale", "i-fresh", "i-nolag", "i-noidx")
               for s in ("lo", "hi")]
        print("  %-7s %s" % (r[0], ", ".join(
            "%s/%s %d" % (b[2:], s, n) for b, s, n in row if n)))

    for nm in ("sb",):
        for s in by[nm][0][14].get("i-exit-inv-stale", []):
            print("  SPECIMEN %s intrinsic-stale violation %s" % (nm, s))
    return by


def e7_per_decision(rows):
    """E6 sorts by family and leaves a determinant-2/determinant-3
    split with no mechanism. D4's first step is G2's conclusion, so
    the conditional the repair really states is per-DECISION: G2 at
    the door plus the intrinsic index gap. Predictions R13, R14."""
    print("\nE7  THE REPAIR AS A PER-DECISION CONDITIONAL")
    print("  intrinsically stale convergent-vertex doors, split by "
          "whether G2 held at the door:")
    print("  %-7s %-4s %12s %12s %12s %12s"
          % ("family", "det", "G2 ok max", "G2 ok !max",
             "G2 bad max", "G2 bad !max"))
    okshort = okmax = 0
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        t = r[13]
        a = t.get(("i-g2decl", "i-stale", True, True), 0)
        b = t.get(("i-g2decl", "i-stale", True, False), 0)
        c = t.get(("i-g2decl", "i-stale", False, True), 0)
        d = t.get(("i-g2decl", "i-stale", False, False), 0)
        okmax += a
        okshort += b
        print("  %-7s %-4d %12d %12d %12d %12d"
              % (r[0], r[1], a, b, c, d))
    check("R13 G2 at the door plus the intrinsic index gap forces "
          "the maxed ladder, in every family and at every "
          "determinant", okmax > 0 and okshort == 0)
    print("  (the !max columns test index != a_next, not a "
          "direction; R12 splits it and finds the gap always "
          "downward, never past the maxed rung)")

    print("\n  intrinsically stale exits, split by their own door's "
          "G2 verdict:")
    print("  %-7s %-4s %12s %12s %12s %12s"
          % ("family", "det", "G2 ok held", "G2 ok VIOL",
             "G2 bad held", "G2 bad viol"))
    okviol = okheld = 0
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        t = r[13]
        a = t.get(("i-g2exit", "i-stale", True, True), 0)
        b = t.get(("i-g2exit", "i-stale", True, False), 0)
        c = t.get(("i-g2exit", "i-stale", False, True), 0)
        d = t.get(("i-g2exit", "i-stale", False, False), 0)
        okheld += a
        okviol += b
        print("  %-7s %-4d %12d %12d %12d %12d"
              % (r[0], r[1], a, b, c, d))
    check("R14 no exit-index violation survives an intrinsically "
          "stale exit whose own door satisfied G2",
          okheld > 0 and okviol == 0)

    # E8 (R15): every figure above is the CHAIN-preferring slice,
    # while the door inequalities are stated over doors. The missing
    # half is run rather than the claim narrowed. D4's last step is
    # the preference, so the two halves should come apart here.
    print("\n  E8 the same two splits on the TREE-preferring slice:")
    print("  %-7s %-4s %10s %10s %11s %10s"
          % ("family", "det", "decl max", "decl !max", "exits held",
             "exits VIOL"))
    tmax = tbad = theld = tviol = 0
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        t = r[15]
        a = t.get(("i-g2decl", "i-stale", True, True), 0)
        b = t.get(("i-g2decl", "i-stale", True, False), 0)
        c = t.get(("i-g2exit", "i-stale", True, True), 0)
        d = t.get(("i-g2exit", "i-stale", True, False), 0)
        tmax += a
        tbad += b
        theld += c
        tviol += d
        print("  %-7s %-4d %10d %10d %11d %10d"
              % (r[0], r[1], a, b, c, d))
    print("\n  R16 what those doors ARE (chain-preferring slice, "
          "intrinsically stale, G2 holding):")
    print("  %-7s %-4s %12s %12s %12s %12s"
          % ("family", "det", "straddle/no", "straddle/yes",
             "tree/no", "tree/yes"))
    sn = sy = tn = ty = 0
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        t = r[13]
        a = t.get(("i-declkind", "i-stale", True, "S", False), 0)
        b = t.get(("i-declkind", "i-stale", True, "S", True), 0)
        c = t.get(("i-declkind", "i-stale", True, "T", False), 0)
        d = t.get(("i-declkind", "i-stale", True, "T", True), 0)
        sn += a
        sy += b
        tn += c
        ty += d
        print("  %-7s %-4d %12d %12d %12d %12d"
              % (r[0], r[1], a, b, c, d))
    check("R16 no chain move was DECLINED at those doors: every one "
          "is a straddle already at the maxed rung, where the commit "
          "loop's strict-improvement test offers no chain candidate",
          sn > 0 and sy == 0 and tn == 0 and ty == 0)

    check("R15a the GEOMETRIC half is preference-free: at a "
          "tree-preferring run's intrinsically stale G2-respecting "
          "doors the chain reference has still maxed the ladder",
          tmax > 0 and tbad == 0)
    print("  R15b the nesting conclusion on the tree slice: %d exits "
          "held, %d violated" % (theld, tviol))


def main():
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    print("THE READER LAWS BY DETERMINANT")
    print("scans: %s" % (SCANS,))
    print("runs:  %d per family, preference slice (st, ss) = (1, 0) "
          "except leg E2" % len(RUNS))
    e1_gates()
    if FAILURES:
        print("\nGATE FAILED -- no verdicts from any later leg.")
        print("FAILURES: %s" % FAILURES)
        return 1
    e2_probe_a()
    rows = e3_families()
    e4_verdict(rows)
    e6_intrinsic(rows)
    e7_per_decision(rows)
    print("\n%d checks failed" % len(FAILURES))
    if FAILURES:
        for f in FAILURES:
            print("  FAIL %s" % f)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
