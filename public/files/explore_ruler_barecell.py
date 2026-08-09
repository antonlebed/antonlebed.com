"""explore_ruler_barecell.py -- ESTIMATOR FACT OR TOWER FACT: the
set-valued read's two failures re-run on BARE CELLS with no ring
anywhere (the ring-free control for explore_ruler_setvalued.py; the rig, the
sampler interface, the estimator code and the oracles are IMPORTED from
explore_ruler_setvalued.py rather than rewritten, which is what makes
the comparison a control rather than a second experiment).

THE QUESTION. The set-valued read found two failures on designed cells
of the primorial family: split conformal's exact WORST-ATOM coverage
collapsing to 0.0000 while its marginal guarantee held, and the
thresholded-posterior FORM -- the object a published theorem certifies
as ambiguity-minimal -- standing strictly above a feasible non-threshold
rule by one label and by two. Both were reported as properties of the
protocols rather than of the family. That report is an inference from a
single family. This file asks whether either failure needs the ring at
all: the same protocols, the same estimator code, the same scoring, run
on hand-set categorical cells with no tower, no modulus and no fiber in
them. The placement/truth split the point ruler established says the
family should contribute PLACEMENT and truth and not the failure; if a
bare cell cannot be made to fail, that split is wrong here and the
failures were facts about this object.

WHOSE VOCABULARY. The suspicion is written in the conformal-prediction
literature's terms -- marginal against conditional coverage, ambiguity,
the thresholded posterior -- and not in the tower's, which is correct
for a probe whose object is somebody else's instrument. The one word
inherited from the surrounding corpus is ATOM, and it is used in the
literature's sense throughout: a point of positive marginal mass in
the observable.

TRANSPLANT, MARKED. The expectation that the failures survive the ring's
removal is imported from the POINT ruler, where the same split was
measured on estimators returning a number. A set-valued instrument fails
through its set constructor rather than through a bias, so the transplant
is across a change of instrument KIND and is exactly what this file is
built to test rather than to assume.

THE HAND ATTACK, and it moved the probe (worked on paper before any
engine code; it is recorded here because it changed what gets measured).

The form failure was attributed to ATOMICITY: the observable is a
residue, so the marginal law has M atoms, and the same atomicity that
voids the distribution-free conditional-coverage impossibility was read
as voiding the optimal form. The Lagrangian for the ambiguity problem
says otherwise. Minimizing E|H| - lam * P(Y in H(X)) is a POINTWISE
problem: include y at x iff 1 - lam*p(y|x) < 0, i.e. iff p(y|x) > 1/lam.
At p(y|x) = 1/lam exactly the objective is INDIFFERENT to including y --
so every rule that takes all labels strictly above the level and ANY
sub-collection of the labels sitting exactly ON it is a minimizer. The
strict-threshold set {y : p(y|x) >= t} is only one of those, and it is
the one that must take the whole tied block or none of it.

Three consequences, all of which change the measurement:

  (a) The driver is a TIE, not an atom. Nothing in the argument mentions
      the marginal law of X. A non-atomic distribution whose posterior
      ties would penalize the same form; an atomic one whose posterior
      does not would not. So the sentence to test is not "atomicity
      voids the form" but "the strict form pays at ties, and breaking
      the tie restores optimality" -- and if that is right, the ring's
      role was only to SUPPLY ties generically, a finite ring read
      through a modulus having finitely many posterior values.

  (b) The tie must sit AT THE OPERATIVE LEVEL. A tie somewhere else in
      the posterior costs nothing, because the rule never resolves it.
      This is a sharper, more falsifiable claim than "ties hurt", and it
      is the one the cells below are designed to place on both sides of.

  (c) THE MARGINAL OPTIMUM WAS NEVER COMPUTED. The set-valued read
      certified the strict form suboptimal by exhibiting a FEASIBLE
      rival -- the per-atom smallest set -- and that certificate is
      sound, but it bounds the optimum from above and is not the
      optimum. The tie-broken threshold can be strictly SMALLER than the
      per-atom rule, and where a hard atom is light enough the optimum
      abandons it entirely. So the quantity this file scores is the FORM
      PENALTY, E|O_marg| - OPT, against a marginal optimum computed and
      CERTIFIED rather than bounded.

WHICH CONSTRAINT EACH OBJECT IS OPTIMAL FOR, AND WHAT CERTIFIES IT (the
correction explore_ruler_setvalued.py earned: it named an object "the
marginal optimum" that was the best THRESHOLD set, and the print that
caught it was a negative price where feasibility forbids one).

  O_cond  -- per atom, the smallest set with mass >= 1-alpha AT THAT
             ATOM. Optimal for the CONDITIONAL constraint. Certificate:
             a per-atom greedy over a sorted list is exactly optimal for
             a per-atom constraint, trivially.
  O_marg  -- {y : p(y|r) >= t}, t the largest level whose marginal
             coverage still reaches 1-alpha. This is the FORM the
             published theorem names, and here it carries NO optimality
             certificate: it is the object under test, not a reference.
  OPT     -- the true minimum of E|H| over ALL rules meeting the
             MARGINAL constraint. Certificate, two kinds and the rig
             prints which one applies at each cell:
               EXACT, where every atom carries the same weight. Then the
               problem is "choose per-atom sizes minimizing their sum
               subject to the summed top-s masses reaching the target",
               each atom's increments are decreasing (the masses are
               sorted), so all increments have equal cost, and taking
               the largest gains first is exactly optimal.
               BRACKETED, where weights differ. The fractional
               relaxation is a lower bound L (its feasible set contains
               the integer one) and the same greedy run integrally is an
               upper bound U; the rig prints [L, U] and the optimum is
               certified when they meet.
  The FORM PENALTY is E|O_marg| - OPT, and it is reported against the
  certified side of the bracket so that a positive penalty is never an
  artifact of the bound.

INCUMBENT CONTACT. The three papers behind this question are quoted
full-text in explore_ruler_setvalued.py and are not re-quoted here; nothing
in this file re-reads them. What it adds is that the ambiguity theorem's
object is scored against a computed optimum rather than against a
feasible rival, and that the Lagrangian above is the textbook argument
for that theorem rather than a competing one -- the finding, if it lands,
is about the FORM the theorem's statement fixes and not about the
theorem being wrong.

THE CELLS. Seven hand-set categorical cells, no ring anywhere: a list of
per-atom posteriors as exact Fractions, carried through the SAME sampler
interface (BareCell, the positive control's own class) and the SAME
estimator code. alpha = 0.30 throughout, frozen from
explore_ruler_setvalued.py so the two runs are comparable. The design
places both sides of the tie rule and both sides of the coverage
collapse.

  cell        M  k  what it places                        tie at t* ?
  B-TIE-1     1  3  one atom, posterior (3/7, 2/7, 2/7).   YES
                    ONE atom, so there is no conditional
                    /marginal distinction at all -- if the
                    penalty survives here it needs neither
                    a ring nor a second atom
  B-TIE-3     3  3  the same posterior at every atom: the   YES
                    ring's flat cell with the ring removed
  B-DEAD-7    3  7  uniform 1/7 at every atom: the ring's   YES
                    divisibility-dead cell, removed
  B-NOTIE     4  4  sixteen DISTINCT posterior values,      NO
                    oracle sizes 1, 2, 3, 3. The
                    differential control: if the penalty is
                    a tie fact it must vanish here
  B-STRADDLE  8  3  seven peaked atoms and one flat one,    NO
                    all values distinct. The seven tops
                    average past 1-alpha on their own, so a
                    global threshold can clear the bar
                    without reaching the eighth atom's best
                    label at all
  B-MIXED     8  3  B-STRADDLE with the hard atom TIED at   NO
                    (0.40, 0.30, 0.30): a tie that is NOT
                    at the operative level. Separates "has
                    a tie" from "has a tie where the rule
                    resolves one"
  B-TILT-W    4  3  B-TIE-3 with UNEQUAL atom weights       YES
                    (2/5, 3/10, 1/5, 1/10): the ring-free
                    analogue of a tilted cell, and the one
                    cell where the optimum arrives as a
                    bracket rather than exactly

n in {2000, 8000, 32000}, TRIALS = 40, one fixed seed per (cell, n,
trial) -- all inherited from explore_ruler_setvalued.py unchanged.

PREDICTIONS, fixed before the engine.
  P1 THE TIE RULE. The form penalty is strictly positive at B-TIE-1,
     B-TIE-3, B-DEAD-7 and B-TILT-W, and exactly 0 at B-NOTIE,
     B-STRADDLE and B-MIXED. Stated as the falsifiable half: a tie at
     the operative level t* is NECESSARY for a positive penalty, so a
     cell printing multiplicity 1 at t* and a positive penalty kills the
     rule.
  P2 THE SIZES. The penalty is 1 label at B-TIE-1 and B-TIE-3 and 2 at
     B-DEAD-7 -- the same two numbers the ring cells printed, reproduced
     with no ring present, since the arithmetic that produced them
     (three masses 3/7, 2/7, 2/7 against a 0.70 bar; seven masses 1/7)
     is carried by the posterior alone.
  P3 THE COVERAGE COLLAPSE IS REPRODUCED. At B-STRADDLE and B-MIXED
     split conformal's exact worst-atom coverage is 0.0000 at every
     sample size while its exact marginal coverage stays at or above
     0.70, and 16-fold more data does not move it; Mondrian's worst atom
     on the same draws stays near the nominal level. No ring anywhere.
  P4 THE OPTIMUM ABANDONS A LIGHT HARD ATOM. At B-STRADDLE and B-MIXED
     OPT is strictly BELOW E|O_cond|, because the cheapest way to reach
     0.70 marginally is to cover the seven peaked atoms and give the
     eighth nothing. So the per-atom rule is not the marginal optimum
     and that file's certificate was a bound, as the hand attack says.
  P5 ESTIMATION STILL RESCUES THE PRACTICE. At the tied cells the
     deployed methods' mean set size is at or below E|O_marg|, because
     an estimated posterior has no exact ties -- the same asymmetry
     explore_ruler_setvalued.py found, reproduced off the family.

KILL-SHAPE, an observable and frozen in advance: if the bare
cells reproduce NEITHER a zero split worst-atom coverage at any cell NOR
a positive form penalty at any cell, then both failures were tower facts
after all -- which closes the channel's placement/truth split rather
than extending it, and is the larger finding of the two.

CONTROLS (run and asserted before any result is read).
  K0 THE IMPORTED POSITIVE CONTROL, run by calling
     explore_ruler_setvalued.py's own control_K0 unchanged: the
     three-atom bare problem whose conditional oracle sizes are 1, 2
     and 3, with Mondrian's median per-atom excess
     0 and max at most 1 and both methods marginally valid. If the
     import is wired wrong this is where it shows, before anything else
     is read.
  K1 THE TRUTH CONTROL: every cell's per-atom posterior sums to exactly
     1 in Fractions, and the atom weights sum to exactly 1.
  K2 THE SAMPLER CONTROL, again that file's own control_K2 unchanged:
     pooled empirical atom and label frequencies within 4 binomial
     standard errors of the exact values at the largest n.
  K3 THE OPTIMUM CONTROL: at every cell L <= U; the integer construction
     is FEASIBLE (its exact marginal coverage reaches 1-alpha); and
     OPT <= E|O_cond| and OPT <= E|O_marg|, since both are feasible for
     the marginal constraint. A violation of any of these is an
     arithmetic bug in the new code, not a finding.
  K4 THE RE-SCORE CONTROL: the four RING cells, scored through this
     file's imported oracles, must reproduce the imported file's printed
     E|O_cond| and E|O_marg| exactly -- 1.0000/1.0000, 2.0000/3.0000,
     5.0000/7.0000 and 1.2010/1.0000. This certifies that the two runs
     are the same machinery on the same truth, which is the whole basis
     of the ring/bare comparison.
  K5 THE THRESHOLD-LEVEL CONTROL: this file recomputes the operative
     level t* locally in order to report it, and the sets that level
     produces must equal the imported oracle_marg's sets at every atom
     of every cell. Reporting t* from a private copy that has drifted
     would make the tie rule unfalsifiable.

THE ONE PIECE OF NEW CODE, named in advance: the CERTIFIED MARGINAL
OPTIMUM (the increment greedy, its exactness certificate under equal
weights, and the fractional lower bound otherwise), the operative-level
report, and WeightedBareCell -- the unequal-atom-weight sibling of
explore_ruler_setvalued.py's BareCell. The sampler, the two conformal
methods, the exact coverage scorer, the two oracles and both reused
controls are imported.

RESOURCE ENVELOPE. Pure Python integers, Fractions and lists; no numpy,
no BLAS arenas. Peak footprint is one sample of at most 32000
(atom, label) pairs plus seven small posterior tables -- far under the
512MB default. 7 cells x 3 sample sizes x 40 trials, each trial linear
in n, with a per-sample label loop in Python: estimated under a minute,
and run under memwatch to print the peak.

RUN RECORD (post-run edit; printed output copied, slate above UNCHANGED
-- where a prediction was wrong or a design was misbuilt, the correction
is here and the frozen text is left standing).

Run: 11 cells scored exactly, 7 of them x 3 sample sizes x 40 trials,
wall 12.0s, peak working set 158.6 MB against the 512 MB default
(memwatch), the wall including the audit search added below. That
peak is 7x explore_ruler_setvalued.py's 21.3 MB and it is all one cell:
TILT-4-WIDE's tied block has 26 distinct weights, so the subset-sum
reaches its 200,000-sum cap and falls back to a bracket. The bracket
still settles that cell's question, so the cap was not raised.
The two tables below run wider than this file's 78-column prose, and
are left that way deliberately: they are output copied verbatim, so
rewrapping them would make the record something other than what the
run printed.

CONTROL K3 FIRED ON THE FIRST EXECUTION, before any result was read,
and the design above is left standing with the correction here. It
described the integer upper bound as "the same greedy run integrally",
and at B-TILT-W that printed 2.1 against a feasible rival at 2.0 -- the
ratio-greedy takes BOTH tied items of the heaviest atom before touching
a lighter one, which is right for the fractional problem and wrong for
the integer one where cost is the atom's weight. The knapsack argument
in certified_optimum is the repair: every pair strictly above the
operative level is in the optimum, and the tied block is closed by a
min-cost SUBSET SUM. This is the control catching an instrument bug and
not a finding.

AND THE REPAIRED ARGUMENT IS ITSELF INCOMPLETE, found at audit rather
than by a control, which is why the exhaustive check in main() was added
after the fact and is labelled AUDIT VERIFICATION rather than dressed as
a sixth frozen control. The argument says the optimum contains every
pair strictly above the operative level, because dropping one forces
buying its mass back at the worse ratio t*. That step assumes the
replacement is bought from the TIED BLOCK. It need not be: a pair BELOW
t* sitting at a very light atom can be cheaper in absolute cost than a
tied pair at a heavy one, ratio and cost being different things. So the
construction is guaranteed FEASIBLE and is a sound upper bound, but its
optimality does not follow from the argument as written.
The upper bound is all the positive-penalty claims need -- OPT <= upper
gives penalty >= E|O_marg| - upper > 0 whatever the truth is. What needs
EXACTNESS is the zeros (a multiplicity-1 cell pricing at exactly 0) and
the price figures, so those were checked against an exhaustive search
over per-atom size vectors, which is exhaustive over the rules that can
be optimal because cost at an atom depends only on the COUNT taken
there. All seven bare cells agree with the certificate exactly. So do
FLAT-3 (2.0000) and DEAD-7 (4.9333), whose 15 atoms are identical, which
collapses their search to one over how many atoms sit at each size.
TILT-3 and TILT-4-WIDE cannot be searched at M = 15 and 105 with
distinct atoms, and nothing is claimed of them beyond a positive
penalty. Nine of eleven exact, two bounded, and no number below rests on
the incomplete step -- the run prints that 9/11 and names the two it
cannot search.

  cell           M  k | E|Ocond| E|Omarg| OPT (certificate)        |     t* mult | PENALTY
  TILT-3        15  3 |   1.0000   1.0000 0.9288 exact (LP 0.9008) | 0.7160   10 | +0.0712  (ring)
  FLAT-3        15  3 |   2.0000   3.0000 2.0000 exact (LP 1.9500) |    2/7   30 | +1.0000  (ring)
  DEAD-7        15  7 |   5.0000   7.0000 4.9333 exact (LP 4.9000) |    1/7  105 | +2.0667  (ring)
  TILT-4-WIDE  105  4 |   1.2010   1.0000 [0.8967, 0.9028] bracket | 0.6530   26 | +0.0972  (ring)
  B-TIE-1        1  3 |   2.0000   3.0000 2.0000 exact (LP 1.9500) |    2/7    2 | +1.0000  (bare)
  B-TIE-3        3  3 |   2.0000   3.0000 2.0000 exact (LP 1.9500) |    2/7    6 | +1.0000  (bare)
  B-DEAD-7       3  7 |   5.0000   7.0000 5.0000 exact (LP 4.9000) |    1/7   21 | +2.0000  (bare)
  B-NOTIE        4  4 |   2.2500   2.0000 2.0000 exact (LP 1.8636) |  11/50    1 | +0.0000  (bare)
  B-STRADDLE     8  3 |   1.1250   0.8750 0.8750 exact (LP 0.8422) |    4/5    1 | +0.0000  (bare)
  B-MIXED        8  3 |   1.1250   0.8750 0.8750 exact (LP 0.8422) |    4/5    1 | +0.0000  (bare)
  B-TILT-W       4  3 |   2.0000   3.0000 2.0000 exact (LP 1.9500) |    2/7    8 | +1.0000  (bare)

  the deployed methods on the bare cells: per-atom size excess over each
  method's own oracle (split vs O_marg, mondrian vs O_cond), and EXACT
  coverage; med/max/mean over 40 trials x all atoms
  cell              n | SPLIT med max   mean | MOND med max  mean | marg s|m      | cond min s|m
  B-TIE-1        2000 |  -1.0   0   -0.8750 |  0.0   1  0.1250 | 0.7500|0.7500 | 0.7143|0.7143
  B-TIE-1        8000 |  -1.0   0   -0.9500 |  0.0   1  0.0500 | 0.7286|0.7286 | 0.7143|0.7143
  B-TIE-1       32000 |  -1.0   0   -0.9750 |  0.0   1  0.0250 | 0.7214|0.7214 | 0.7143|0.7143
  B-TIE-3        2000 |  -1.0   0   -0.9250 |  0.0   1  0.3250 | 0.7357|0.8071 | 0.4286|0.7143
  B-TIE-3        8000 |  -1.0   0   -0.9917 |  0.0   1  0.1167 | 0.7167|0.7476 | 0.4286|0.7143
  B-TIE-3       32000 |  -1.0   0   -1.0000 |  0.0   1  0.0083 | 0.7143|0.7167 | 0.4286|0.7143
  B-DEAD-7       2000 |  -2.0   0   -1.8333 |  0.0   2  0.4167 | 0.7381|0.7738 | 0.4286|0.7143
  B-DEAD-7       8000 |  -2.0   0   -1.9417 |  0.0   2  0.2833 | 0.7226|0.7548 | 0.4286|0.7143
  B-DEAD-7      32000 |  -2.0  -1   -2.0000 |  0.0   2  0.0500 | 0.7143|0.7214 | 0.5714|0.7143
  B-NOTIE        2000 |   0.0   2    0.0125 |  0.0   2  0.1625 | 0.7299|0.8007 | 0.5200|0.6300
  B-NOTIE        8000 |   0.0   1    0.0000 |  0.0   1  0.0563 | 0.7287|0.7894 | 0.5200|0.7100
  B-NOTIE       32000 |   0.0   1    0.0000 |  0.0   1  0.0125 | 0.7295|0.7841 | 0.5200|0.7100
  B-STRADDLE     2000 |   0.0   1    0.0031 |  0.0   1  0.0719 | 0.7275|0.8362 | 0.0000|0.6800
  B-STRADDLE     8000 |   0.0   0    0.0000 |  0.0   1  0.0219 | 0.7262|0.8224 | 0.0000|0.7200
  B-STRADDLE    32000 |   0.0   0    0.0000 |  0.0   1  0.0156 | 0.7262|0.8206 | 0.0000|0.7200
  B-MIXED        2000 |   0.0   1    0.0031 |  0.0   1  0.0781 | 0.7275|0.8372 | 0.0000|0.7000
  B-MIXED        8000 |   0.0   0    0.0000 |  0.0   1  0.0750 | 0.7262|0.8362 | 0.0000|0.7000
  B-MIXED       32000 |   0.0   0    0.0000 |  0.0   1  0.0656 | 0.7262|0.8334 | 0.0000|0.7000
  B-TILT-W       2000 |  -1.0   0   -0.9625 |  0.0   1  0.3312 | 0.7371|0.7950 | 0.4286|0.7143
  B-TILT-W       8000 |  -1.0   0   -0.9062 |  0.0   1  0.2125 | 0.7450|0.7586 | 0.4286|0.7143
  B-TILT-W      32000 |  -1.0   0   -0.9625 |  0.0   1  0.0563 | 0.7386|0.7221 | 0.4286|0.7143

KILL-SHAPE: MISSED, on the basis frozen, and in both halves at once. The
bare cells reproduce a zero split worst-atom coverage (B-STRADDLE and
B-MIXED, 0.0000 at every sample size) AND a positive form penalty
(B-TIE-1, B-TIE-3, B-DEAD-7, B-TILT-W). Neither failure was a tower
fact, and the placement/truth split extends from the point ruler to a
SET-valued instrument: the family contributes placement and exact truth,
not the failure.

WHAT THE RUN SAYS, at the honest tier.

0. READ THE PREDICTIONS AS A CODE CHECK, NOT AS A RESULT. All five were
   CONFIRMED, which is what should happen when the hand attack derived
   them on paper before the engine existed -- P1 and P2 are arithmetic
   over three masses against a 0.70 bar. The information in this run is
   in the two things the slate did NOT predict, which are items 2 and 3.

1. THE PENALTY IS A TIE FACT AND THE HAND ATTACK WAS RIGHT: the ring is
   not load-bearing. B-TIE-1 is ONE atom, three hand-set masses, no
   modulus and no fiber, and the strict-threshold form costs a full extra
   label there. With one atom the conditional and marginal constraints
   are the same constraint, so there is no atomicity question left to
   attribute the failure to. What the family supplied was the tie, and it
   supplied it generically because a finite ring read through a modulus
   has finitely many posterior values. Measured the way the ring cells
   were measured -- against the per-atom rule, which is what the
   imported file had -- the two gaps come back exactly: +1 label off
   the flat cell's {3/7, 2/7, 2/7} and +2 off the dead cell's seven
   1/7's. Against the
   CERTIFIED optimum the dead cells differ (+2.0000 bare against
   +2.0667 on the ring) and item 4 says why: that is integrality on 15
   atoms against 3, not the ring.

2. THE TIE RULE CAME BACK AS A BICONDITIONAL, which is stronger than the
   necessary condition P1 froze. Across all ELEVEN cells, ring and bare
   together, the form penalty is positive at exactly the cells whose
   operative level t* carries multiplicity 2 or more, and exactly zero at
   the three with multiplicity 1 -- and this holds through a range of
   multiplicities from 2 to 105 and both weightings. Observation, exact,
   11 cells. The mechanism is the pointwise indifference in the hand
   attack: at the operative level the objective does not care which tied
   labels are taken, so a rule that must take the whole block or none of
   it is the only kind that can pay, and it pays exactly when there is a
   block to take.

3. THE RING CELLS WERE UNDER-REPORTED, AND THE CORRECTION RUNS THE OTHER
   WAY FROM THE IMPORTED FILE'S. Scored against the certified optimum
   rather than against the feasible per-atom rival, the form penalty is
   positive at ALL FOUR ring cells -- including the two LIVE ones, TILT-3
   (+0.0712) and TILT-4-WIDE (at least +0.0972; that cell's 26-weight tied
   block exceeds the subset sum's cap, so its optimum returns as the
   bracket [0.8967, 0.9028] and its penalty is a lower bound, which is
   enough to be positive), where that file saw E|O_marg| = E|O_cond| and
   reported no penalty at all. The per-atom rule is an upper bound on the
   optimum and it is a loose one, so that certificate was sound and its
   reach was short. The finding it certified stands and grows: the form
   pays on every cell of this family, not only the degenerate ones.

4. AND THE NEGATIVE PRICE IS GONE. The imported file's "price of
   conditional coverage", E|O_cond| - E|O_marg|, printed NEGATIVE at two
   cells, which is the impossibility that exposed the misnamed object.
   Against the optimum it is non-negative at every one of the eleven, and
   what sets it is INTEGRALITY and not merely whether the atoms differ.
   Where they differ it is strictly positive -- +0.0712 and about +0.30 at
   the two live ring cells, +0.2500 at B-NOTIE, B-STRADDLE and B-MIXED.
   Where every atom carries the same mass multiset it is zero ONLY IF the
   granularity forbids shaving a label, and at 15 atoms it does not: DEAD-7
   prices at +0.0667 because the MARGINAL constraint is an average and 74
   labels clear the bar where the per-atom rule costs 75, so fourteen atoms
   get five and the fifteenth gets four and undercovers. B-DEAD-7 is the
   same cell at 3 atoms, where 15 labels are needed and 14 fall short, and
   it prices at exactly zero. So probe 1's frozen P4 -- positive at the
   tilted cells, zero at the flat and dead ones -- is TRUE against the
   right object except at that one cell, and the exception is a granularity
   effect its slate had no way to see while it was comparing against the
   wrong object at all.

5. THE MARGINAL OPTIMUM ABANDONS AN OUTNUMBERED HARD ATOM OUTRIGHT, and
   the design word "light" in the hand attack above is wrong for the
   cells that were actually built: every atom of B-STRADDLE and B-MIXED
   carries the SAME mass 1/8. Nothing is down-weighted and nothing is
   rare. The seven peaked atoms clear the bar by themselves at 0.72625,
   which is all it takes. At
   B-STRADDLE and B-MIXED, OPT = 0.8750 = 7/8 exactly -- seven singletons
   at the seven peaked atoms and the EMPTY SET at the eighth. It is the
   cheapest way to reach 0.70 marginally, it is what split conformal
   actually does there, and it is why that method's exact worst-atom
   coverage is 0.0000 while its marginal coverage is 0.7262. So the
   collapse is not a defect of the estimator: at these cells the marginal
   optimum ITSELF has zero coverage at an atom, and split conformal is
   converging to it correctly. The auditor's complaint is with the
   constraint, not with the algorithm meeting it -- which is the sharpest
   form this question has taken, correct and informative being
   different properties.

6. WHAT ESTIMATION BUYS, again and off the family. At every tied cell the
   deployed split predictor's mean size sits a full penalty BELOW its own
   exact threshold oracle (-1.0000 at B-TIE-3, -2.0000 at B-DEAD-7 by
   n = 32000): the estimated posterior has no exact ties, so the deployed
   method is not confined to the true posterior's level sets and beats the
   best rule of its own form. explore_ruler_setvalued.py found this on
   the ring; it is not a ring fact either.
"""

import itertools
import os
import sys
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_setvalued import (  # noqa: E402
    ALPHA, SAMPLE_SIZES, TRIALS, BASE_SEED,
    BareCell, CELLS,
    aggregate, control_K0, control_K2, median,
)

F = Fraction


# --------------------------------------------- the unequal-weight cell

class WeightedBareCell(BareCell):
    """A bare cell whose atoms do not carry equal marginal mass."""

    def __init__(self, name, atom_posteriors, weights):
        BareCell.__init__(self, name, atom_posteriors)
        self.w = [F(x) for x in weights]

    def atom_prob(self, r):
        return self.w[r]

    def atom_prob_f(self, r):
        return float(self.w[r])

    def label_prob(self):
        return [sum(self.w[r] * self.post[r][y] for r in range(self.M))
                for y in range(self.k)]

    def sample(self, n, rng):
        rs = rng.choices(range(self.M), weights=[float(x) for x in self.w],
                         k=n)
        out = []
        for r in rs:
            u, acc, y = rng.random(), 0.0, self.k - 1
            for yy in range(self.k):
                acc += float(self.post[r][yy])
                if u <= acc:
                    y = yy
                    break
            out.append((r, y))
        return out


# ------------------------------------------- the certified optimum

SUM_CAP = 200000


def _min_subset_sum(weights, need):
    """min{sum(S) : S a sub-multiset of `weights`, sum(S) >= need}.

    Exact when the achievable-sum set stays under SUM_CAP; otherwise
    returns the descending-greedy fill, which is only an upper bound.
    """
    groups = {}
    for w in weights:
        groups[w] = groups.get(w, 0) + 1
    sums = {F(0)}
    for w, n in sorted(groups.items(), reverse=True):
        nxt = set()
        for s in sums:
            for i in range(n + 1):
                nxt.add(s + i * w)
        if len(nxt) > SUM_CAP:
            fill, acc = F(0), F(0)
            for w2 in sorted(weights, reverse=True):
                if acc >= need:
                    break
                acc += w2
                fill += w2
            return fill, False
        sums = nxt
    ok = [s for s in sums if s >= need]
    assert ok, "the tied block cannot reach the deficit"
    return min(ok), True


def certified_optimum(cell, alpha, level):
    """Minimize E|H| subject to marginal coverage >= 1-alpha.

    The problem is separable over (atom, label) PAIRS -- pair (r, y)
    costs P(r) and covers P(r)*p(y|r) -- so it is a knapsack whose
    ratio is p(y|r) alone. Every pair strictly above the operative level
    t* is in the optimum (dropping one and replacing its mass at the
    worse ratio t* costs strictly more), and the tied block at t* is
    never exhausted (t* is by construction the largest level whose full
    inclusion reaches the target). So the optimum is the strict-above
    set plus the CHEAPEST sub-collection of the tied block that closes
    the deficit -- a min-cost subset sum, not a greedy fill, which is
    what control K3 caught on the first run.

    Returns (lower, upper, exact, coverage). `lower` is the fractional
    relaxation, kept as an independent check on the arithmetic.
    """
    target = 1 - alpha
    above_cost, above_cov, tie = F(0), F(0), []
    for r in range(cell.M):
        w = cell.atom_prob(r)
        post = cell.posterior(r)
        for y in range(cell.k):
            if post[y] > level:
                above_cost += w
                above_cov += w * post[y]
            elif post[y] == level:
                tie.append(w)

    deficit = target - above_cov
    if deficit <= 0:
        return above_cost, above_cost, True, above_cov

    lower = above_cost + deficit / level
    fill, exact = _min_subset_sum(tie, deficit / level)
    upper = above_cost + fill
    return lower, upper, exact, above_cov + level * fill


def exhaustive_optimum(cell, alpha, budget=3000000):
    """The optimum by exhaustive search over per-atom SIZE vectors.

    Added at audit, not a frozen control -- see the run record. A rule's
    cost at an atom depends only on how MANY labels it takes there, so
    for a fixed size the top-mass labels are best and the search over
    size vectors is exhaustive over the rules that can be optimal.
    Returns None where the search is too large to run.
    """
    M, k = cell.M, cell.k
    if (k + 1) ** M > budget:
        return None
    tops, w = [], [cell.atom_prob(r) for r in range(M)]
    for r in range(M):
        masses = sorted(cell.posterior(r), reverse=True)
        tops.append([sum(masses[:s]) for s in range(k + 1)])
    target = 1 - alpha
    best = None
    for sizes in itertools.product(range(k + 1), repeat=M):
        cov = sum(w[r] * tops[r][sizes[r]] for r in range(M))
        if cov >= target:
            cost = sum(w[r] * sizes[r] for r in range(M))
            if best is None or cost < best:
                best = cost
    return best


def exhaustive_optimum_homogeneous(cell, alpha):
    """The optimum where every atom is IDENTICAL and equally weighted.

    Added at audit alongside exhaustive_optimum, and for the same
    reason. When the atoms carry the same mass multiset and the same
    weight, a rule's cost and coverage depend only on HOW MANY atoms sit
    at each size, so the search collapses from (k+1)^M size vectors to
    the compositions of M into k+1 parts -- which is what lets the two
    15-atom ring cells be checked at all. Returns None where the atoms
    are not homogeneous.
    """
    M, k = cell.M, cell.k
    w0 = cell.atom_prob(0)
    ref = sorted(cell.posterior(0), reverse=True)
    for r in range(M):
        if cell.atom_prob(r) != w0:
            return None
        if sorted(cell.posterior(r), reverse=True) != ref:
            return None
    g = [sum(ref[:s]) for s in range(k + 1)]
    target = (1 - alpha) * M
    best = [None]

    def walk(size, left, cost, cov):
        if size == k:
            cost2, cov2 = cost + k * left, cov + g[k] * left
            if cov2 >= target and (best[0] is None or cost2 < best[0]):
                best[0] = cost2
            return
        # An upper bound on the coverage still reachable: give every
        # remaining atom the full label set. Prunes the search hard.
        if cov + g[k] * left < target:
            return
        for n in range(left + 1):
            walk(size + 1, left - n, cost + size * n, cov + g[size] * n)

    walk(0, M, 0, F(0))
    # best[0] counts labels; expected size weights each by w0 = 1/M.
    return None if best[0] is None else best[0] * w0


def operative_level(cell, alpha):
    """The level the strict-threshold rule lands on, and its multiplicity.

    A local recomputation, kept honest by control K5: the sets it
    implies must equal the imported oracle_marg's.
    """
    post = {r: cell.posterior(r) for r in range(cell.M)}
    pr = {r: cell.atom_prob(r) for r in range(cell.M)}
    levels = sorted({v for r in post for v in post[r]}, reverse=True)
    for t in levels:
        cov = sum(pr[r] * sum(v for v in post[r] if v >= t)
                  for r in range(cell.M))
        if cov >= 1 - alpha:
            mult = sum(1 for r in post for v in post[r] if v == t)
            sets = {r: {y for y in range(cell.k) if post[r][y] >= t}
                    for r in range(cell.M)}
            return t, mult, cov, sets
    raise AssertionError(("no feasible threshold", cell.name))


def expected_size(cell, sets):
    return sum(float(cell.atom_prob(r)) * len(sets[r])
               for r in range(cell.M))




# ------------------------------------------------------- the bare cells

def _f(vals, den):
    return [F(v, den) for v in vals]


BARE = [
    BareCell("B-TIE-1", [_f([3, 2, 2], 7)]),
    BareCell("B-TIE-3", [_f([3, 2, 2], 7)] * 3),
    BareCell("B-DEAD-7", [_f([1] * 7, 7)] * 3),
    BareCell("B-NOTIE", [_f([71, 13, 9, 7], 100),
                         _f([52, 23, 14, 11], 100),
                         _f([34, 29, 22, 15], 100),
                         _f([33, 28, 21, 18], 100)]),
    BareCell("B-STRADDLE", [_f([86, 9, 5], 100),
                            _f([85, 11, 4], 100),
                            _f([84, 13, 3], 100),
                            _f([83, 15, 2], 100),
                            _f([82, 17, 1], 100),
                            _f([81, 12, 7], 100),
                            _f([80, 14, 6], 100),
                            _f([40, 32, 28], 100)]),
    BareCell("B-MIXED", [_f([86, 9, 5], 100),
                         _f([85, 11, 4], 100),
                         _f([84, 13, 3], 100),
                         _f([83, 15, 2], 100),
                         _f([82, 17, 1], 100),
                         _f([81, 12, 7], 100),
                         _f([80, 14, 6], 100),
                         _f([40, 30, 30], 100)]),
    WeightedBareCell("B-TILT-W", [_f([3, 2, 2], 7)] * 4,
                     [F(2, 5), F(3, 10), F(1, 5), F(1, 10)]),
]

RING_EXPECTED = {
    "TILT-3": (1.0000, 1.0000),
    "FLAT-3": (2.0000, 3.0000),
    "DEAD-7": (5.0000, 7.0000),
    "TILT-4-WIDE": (1.2010, 1.0000),
}


# ---------------------------------------------------------- controls

def control_K1(cell):
    for r in range(cell.M):
        assert sum(cell.posterior(r)) == 1, (cell.name, "posterior", r)
    assert sum(cell.atom_prob(r) for r in range(cell.M)) == 1, \
        (cell.name, "weights")
    return True


def control_K3(cell, alpha, lower, upper, cov, ec, em):
    assert lower <= upper, (cell.name, "bracket", lower, upper)
    assert cov >= 1 - alpha, (cell.name, "infeasible optimum", cov)
    opt = float(upper)
    assert opt <= ec + 1e-9, (cell.name, "opt above O_cond", opt, ec)
    assert opt <= em + 1e-9, (cell.name, "opt above O_marg", opt, em)
    return True


def control_K5(cell, alpha, local_sets):
    ref = cell.oracle_marg(alpha)
    assert local_sets == ref, (cell.name, "threshold drift")
    return True


def control_K4(cell, ec, em):
    want = RING_EXPECTED[cell.name]
    assert abs(ec - want[0]) < 5e-5, (cell.name, "O_cond", ec, want[0])
    assert abs(em - want[1]) < 5e-5, (cell.name, "O_marg", em, want[1])
    return True


# --------------------------------------------------------------- main

def score(cell, alpha):
    """The exact column: three objects, the level, and the penalty."""
    oc = {r: cell.oracle_cond(r, alpha)[0] for r in range(cell.M)}
    t, mult, tcov, sets = operative_level(cell, alpha)
    control_K5(cell, alpha, sets)
    om = sets
    ec = expected_size(cell, oc)
    em = expected_size(cell, om)
    lower, upper, exact, cov = certified_optimum(cell, alpha, t)
    control_K3(cell, alpha, lower, upper, cov, ec, em)
    return {
        "oc": oc, "om": om, "ec": ec, "em": em,
        "t": t, "mult": mult, "tcov": tcov,
        "lo": float(lower), "up": float(upper), "exact": exact,
    }


def main():
    print("=" * 74)
    print("CONTROLS")
    print("=" * 74)
    k0 = control_K0()
    print("K0 imported positive control PASS  oracle sizes %s  "
          "mondrian median/max excess %s/%s" % k0)
    for cell in BARE:
        control_K1(cell)
    print("K1 truth control PASS   posteriors and atom weights sum to 1")
    for cell in BARE:
        control_K2(cell, max(SAMPLE_SIZES), BASE_SEED + 777)
    print("K2 imported sampler control PASS   frequencies within 4 SE")

    ring = {}
    for cell in CELLS:
        s = score(cell, ALPHA)
        control_K4(cell, s["ec"], s["em"])
        ring[cell.name] = s
    print("K4 re-score control PASS   the four ring cells reproduce "
          "the imported file's exact oracle sizes")
    print("K3 optimum control PASS    bracket ordered, construction "
          "feasible, optimum below both feasible rivals")
    print("K5 threshold control PASS  the local level reproduces the "
          "imported oracle's sets")

    checked, names = 0, []
    for cell in BARE + CELLS:
        s = ring[cell.name] if cell.name in ring else score(cell, ALPHA)
        brute = exhaustive_optimum(cell, ALPHA)
        if brute is None:
            brute = exhaustive_optimum_homogeneous(cell, ALPHA)
        if brute is None:
            names.append(cell.name)
            continue
        assert abs(float(brute) - s["up"]) < 1e-12, \
            (cell.name, "certificate not optimal", float(brute), s["up"])
        checked += 1
    print("AUDIT VERIFICATION PASS    the certified optimum equals an "
          "exhaustive search at %d/%d cells; not searchable: %s"
          % (checked, len(BARE) + len(CELLS), ", ".join(names)))

    print()
    print("=" * 74)
    print("THE EXACT COLUMN: three objects, and the form penalty")
    print("(O_cond = conditional optimum; O_marg = the strict threshold "
          "FORM;")
    print(" OPT = the certified marginal optimum; penalty = E|O_marg| - OPT)")
    print("=" * 74)
    print("%-12s %3s %2s | %8s %8s %-24s | %6s %4s | %s" %
          ("cell", "M", "k", "E|Ocond|", "E|Omarg|", "OPT (certificate)",
           "t*", "mult", "PENALTY"))
    rows = [("ring", c, ring[c.name]) for c in CELLS]
    rows += [("bare", c, score(c, ALPHA)) for c in BARE]
    for kind, cell, s in rows:
        if s["exact"]:
            cert = "%.4f exact" % s["up"]
            if abs(s["lo"] - s["up"]) > 1e-9:
                cert += " (LP %.4f)" % s["lo"]
        else:
            cert = "[%.4f, %.4f] bracket" % (s["lo"], s["up"])
        pen = s["em"] - s["up"]
        # A tilted cell's operative level is an exact ratio of powers of
        # theta -- hundreds of digits, and unreadable. The load-bearing
        # column is the multiplicity beside it.
        lvl = (str(s["t"]) if s["t"].denominator <= 1000
               else "%.4f" % float(s["t"]))
        print("%-12s %3d %2d | %8.4f %8.4f %-24s | %6s %4d | %+.4f  (%s)" %
              (cell.name, cell.M, cell.k, s["ec"], s["em"], cert,
               lvl, s["mult"], pen, kind))

    print()
    print("=" * 74)
    print("THE DEPLOYED METHODS ON BARE CELLS: size against each method's")
    print("own oracle, and EXACT coverage (%d trials, alpha=%s)"
          % (TRIALS, ALPHA))
    print("=" * 74)
    print("%-12s %6s | %-24s | %-24s" %
          ("cell", "n", "SPLIT med/max/mean size",
           "MOND med/max/mean size"))
    for cell in BARE:
        s = score(cell, ALPHA)
        oc, om = s["oc"], s["om"]
        for n in SAMPLE_SIZES:
            acc = aggregate(cell, n, oc, om, ALPHA,
                            BASE_SEED + 1000 * SAMPLE_SIZES.index(n))
            se, me = acc["split_excess"], acc["mond_excess"]
            sc, mc = acc["split_cond"], acc["mond_cond"]
            sm = sum(acc["split_marg"]) / len(acc["split_marg"])
            mm = sum(acc["mond_marg"]) / len(acc["mond_marg"])
            print("%-12s %6d | %5.1f %4d %8.4f       | %5.1f %4d %8.4f"
                  "       | marg %.4f|%.4f  cond min %.4f|%.4f"
                  % (cell.name, n,
                     median(se), max(se), sum(se) / len(se),
                     median(me), max(me), sum(me) / len(me),
                     sm, mm, min(sc), min(mc)))
            if acc["fallback"]:
                print("             (empty-atom fallback fired %d times)"
                      % acc["fallback"])

    print()
    print("KILL-SHAPE READ: no zero split worst-atom coverage at any bare")
    print("cell AND no positive form penalty at any bare cell would make")
    print("both failures tower facts and close the placement/truth split.")


if __name__ == "__main__":
    main()
