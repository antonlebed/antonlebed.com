"""
explore_forced_one.py -- THE FORCED-ONE INSTRUMENT: the one direction
the growth certificate cannot force, attacked in the window families
the normal form distinguishes -- THREE of them, where the question was
posed as two. (Sibling of explore_growth_certificate.py,
whose certifier, population and supplies this file reuses; the machine
and its VM are explore_born_at_zero.py's.)

THE SETTING. The growing-window machine: windows are copies of Z/m_j
appended by GROW with every register born 0; ADD/SUB/MUL/write-constant
broadcast to every window at once; the one cross-window read is a global
1-bit zero-test (register a zero in ALL windows). A certificate of
infinite growth is a SEGMENT of the run between two equal program
counters holding a GROW, and it repeats forever exactly when every TEST
inside it reads the same bit at every repetition. The three locks of
explore_growth_certificate.py force some of those bits, and its census
measured where they stop: 97-99% of the uncovered grow-heavy programs
fail in ONE direction -- the fresh window reads 0 and the scheme cannot
force the bit to ONE, because forcing a ONE needs EVERY window while
forcing a ZERO needs one persisting witness. THIS FILE BUILDS THE
INSTRUMENT FOR THAT DIRECTION.

THE QUESTION. Can the forced-ONE direction be decided, and how much of
the residue does deciding it convert?

THE HAND ATTACK (on paper, before this file's engine).

  THE CENSUS OF WINDOWS AT A TEST. Fix the segment, rotated to start at
  a GROW (the rotation is the certifier's and the earlier rig already
  pays it), let W be its executed op word of length L, and let the test
  sit at offset s reading register a. Number the repetitions j = 0, 1,
  ... with 0 the one the run was observed at. Every window present at
  the test in repetition j is in exactly one of three families, and the
  normal form gives each its content:

    OLD -- in the pool at the start of repetition 0, with modulus m and
      column v. It has seen W exactly j times since then and then the
      prefix, so it reads PRE_s(F^j(v))[a] mod m, where F is the whole
      segment's map on (Z/m)^r and PRE_s is W[0:s]'s.
    YOUNG-SAME -- born at a GROW at offset d < s during repetition j
      itself. Born all-zero, its suffix is exactly W[d+1:s], so it
      reads E(W[d+1:s])[a] mod its own modulus.
    YOUNG-EARLIER -- born at a GROW at offset d during a repetition
      i < j. Its suffix is W[d+1:L] then W repeated k = j-i-1 times
      then W[0:s], so it reads PRE_s(SEG^k(E(W[d+1:L])))[a] mod its own
      modulus, where SEG is the free INTEGER evaluation of W.

  There is no fourth family: a window born at offset d >= s in
  repetition j does not exist yet at that test, and one born in an
  earlier repetition at any offset is YOUNG-EARLIER with the k that
  counts the whole repetitions between. So forcing the bit to ONE is
  exactly forcing all three families to 0, and the three are three
  different questions.

  ARM A -- OLD WINDOWS ARE A LOCK, NOT A QUESTION. F is a map on the
  finite set (Z/m)^r, so the orbit v, F(v), F^2(v), ... is eventually
  periodic and closes within m^r steps. Enumerate the tail and the
  cycle and read PRE_s at each: "reads 0 at this offset in every
  repetition" is DECIDED per window, and the pool at the segment start
  is finite. Two windows of equal modulus and equal column have equal
  orbits, so the work is per DISTINCT (m, column) pair and not per
  window -- which the normal form already said, equal age and modulus
  being identical forever.

  ARM B -- YOUNG-SAME IS A FINITE INTEGER CHECK. The suffix W[d+1:s]
  is fixed, so E(W[d+1:s])[a] is one integer per grow offset d < s,
  and if it is 0 over Z it is 0 modulo anything -- which is what a
  certificate needs, the modulus at that birth being different in every
  repetition. Sufficient and not necessary: E could be non-zero and
  still divisible by every modulus that window will ever have, which
  this instrument declines rather than decides. AND ITS ANTECEDENT IS
  SHADOWED, which is a claim about REACH and therefore owes a
  measurement (D10): on an unbounded supply a non-zero read at the LAST
  grow before the test belongs to LOCK-ZERO-F, consulted first, so arm
  B is the decider only for a window born at an EARLIER grow -- the
  window the older rig never looked at -- or where the modulus is too
  small.

  ARM C -- YOUNG-EARLIER IS THE REAL ONE, AND IT IS A QUESTION ABOUT Z.
  The content is a free INTEGER evaluation of a word that lengthens by
  a whole segment each repetition: finite in d, infinite in k. The
  cheap first move is whether the integer action y_0 = E(W[d+1:L]),
  y_{k+1} = SEG(y_k) reaches a FIXED POINT or a CYCLE -- if it does,
  the k-quantifier collapses to the finitely many states of the tail
  and the cycle and the arm decides. If it does neither, this route
  does not reach the second half at all.
  KILL FROZEN AS AN OBSERVABLE, not as a judgement: D5 prints the
  three-way tally, and NON-DECIDABLE-ROUTE fires when "neither" is the
  plurality of the triples the census produces.

  ARM STATIC -- THE CASE BOTH DIRECTIONS SHARE, AND IT IS FREE. If a
  is written NOWHERE in W, then F fixes a's coordinate, every old
  window reads the same value at every repetition, and every young
  window was born 0 in a and is never written. So the bit is constant
  across repetitions and equals the bit the run READ -- forced, in
  whichever direction that was, with no arm consulted. THE SCAN IS
  OVER THE WHOLE BODY AND NOT THE PREFIX: the earlier rig's residue
  label "unwritten-in-segment" scans back only from the test, so a
  write at an offset PAST the test wears that label while breaking
  this lock outright. The label and the lock are different predicates
  and the difference is measured (D4).

  AND THE ORBIT PAYS A ZERO LOCK TOO. Arm A's orbit is a set of read
  values per old window; the bit is forced ONE when every such set is
  {0}, and forced ZERO when some one of them omits 0 -- one persisting
  witness, the asymmetry read off the same finite object. It is
  tallied apart from the ONE instrument so the ONE instrument's own
  reach stays readable.

  WHAT THE INSTRUMENT THEREFORE STILL CANNOT BE. Complete. Arm B
  declines a divisibility it cannot see, arm C declines an action that
  neither stabilizes nor cycles, and arm A declines an orbit past its
  budget. Soundness is the whole claim; reach is measured.

THE DESIGN (findings enter by a separate post-run edit; kills are
frozen as OBSERVABLES, never as inferences).

D1  SOUNDNESS, the positive control that gates everything. Every
    program this instrument certifies is simulated far past the
    certifying segment; it must still be running and must reach 600
    grows.
    KILL (prints as UNSOUND): a certified program that halts or stalls
    short of 600 grows. The derivation above is then false and nothing
    else in the run may be read.

D2  THE FORCING CROSS-CHECK, the second positive control and the one
    the earlier rig could not make. A forcing is a claim about EVERY
    repetition, so checking it against the ONE bit the segment was
    found at is the weakest reading available. Instead replay from the
    segment's start and walk the body CYCLICALLY: the program counter
    must match at every step and every TEST must read the bit the
    segment recorded at THAT OFFSET. Offsets and not instructions --
    one TEST can execute twice inside a segment at two offsets with two
    last writes, and its two bits are then legitimately different, so
    keying by instruction manufactures its own mismatches.
    KILL (prints as FORCE-MISMATCH): any disagreement, at any
    repetition. This is where an unsound arm surfaces, and it is
    strictly stronger than the segment-local check.

D3  THE BATTERY. The corpus's four programs (explore_born_at_zero.py
    S2 plus the data-gated grower): a halting program, a frozen-pulse
    non-halter with finitely many grows, a forever-growing loop, and a
    grower whose loop tests a register the ops write. Expected: NO
    CERTIFICATE for the first two, CERTIFIED for the third.
    KILL (prints as MISFIRE): a certificate for the halting program or
    the frozen pulse.
    PREDICTION FROZEN, and it is a prediction the earlier rig's verdict
    contradicts: the DATA-GATED grower now CERTIFIES. Its old windows
    hold a non-zero increment the fresh windows do not, so its test bit
    is forced ZERO by an old window's orbit -- which is why the zero
    lock rides along rather than being scope creep.

D4  COVERAGE, against the frozen earlier census (600 programs, seed 11,
    step cap 4000, length 12, sqrt supply, r=3: 109 grow-heavy, 52
    certified of which 49 branch-free, lock-carried 3, 57 uncovered of
    which 56 forced-ONE). Report the same cells with the instrument
    attached, split by lock, and separately the count of the previously
    UNCOVERED that the ONE instrument alone converts.
    KILL (prints as ONE-VACUOUS): the ONE instrument (STATIC in its ONE
    direction, plus A+B+C) converts ZERO uncovered grow-heavy programs
    -- the instrument is empty in practice whatever its derivation.
    ALSO REPORTED, because the two are different predicates and the
    difference is the point: how many of the residue's 46
    "unwritten-in-segment" programs have a write to the tested register
    PAST the test, and so are not LOCK-STATIC at all.
    PREDICTION FROZEN: LOCK-STATIC carries the bulk of what is
    converted and arms A/B/C together add few, because a random loop
    whose tested register is written inside the segment writes it with
    a data op whose free evaluation moves. Sharper, so that it can be
    wrong: LOCK-STATIC converts at least half of the 46.

D5  THE HALF-(b) MEASUREMENT, the question this file exists for, and
    it is reported whether or not any certificate changes. Over every
    (segment, test, grow-offset) triple the census reaches arm C with,
    tally the integer action's fate within K iterations under the
    magnitude guard: FIXED POINT / CYCLE / NEITHER / OVERFLOW.
    KILL (prints as NON-DECIDABLE-ROUTE): NEITHER is the plurality --
    the fixed-point-or-cycle route does not reach the second half.
    PREDICTION FROZEN: NEITHER is a minority, under a quarter, and
    FIXED POINT is the plurality -- a free evaluation from all-zero
    needs a genuine accumulator to diverge, and a random segment's
    accumulator is usually re-zeroed by a write-constant inside the
    same segment.
    SECONDARY OBSERVABLE, no forcing claim attached: among the NEITHER
    triples, does the tested register's own read value stabilise inside
    K even though the state does not? That count names whether a
    backward SLICE of the state would recover the route, and it is an
    observation because "stable for K steps" is not "stable".

D6  THE DESIGNED ARM -- NECESSITY, one program per arm. A lock's
    antecedent is a conjunction and a random population is not built to
    meet it, so each arm gets a program built so that IT is the arm
    that decides. The three ONE arms all have to pass for a
    certificate, so necessity here is exhibited the only way it can be:
    a program where that arm is the one that correctly REFUSES, the
    other two passing.
      STATIC   loop { GROW; WC(b,1); ADD c,b,b; TEST a }
               -- a written nowhere; forced ONE with no arm consulted.
      A-REFUSE WC(b,1) ahead of the loop, then
               loop { GROW; TEST a; ADD a,a,b }
               -- young windows have b = 0 and stay 0, so B and C pass;
                  an OLD window has b = 1 and its a climbs, so the bit
                  is 1 at the first repetition and 0 after. Arm A alone
                  must refuse.
      C-REFUSE loop { GROW; TEST a; ADD a,a,c; WC(c,1) }, no GROW ahead
               of the loop, so the pool at the segment start is EMPTY
               and arm A is vacuous.
               -- the young-same read is the empty word, so B passes;
                  the integer action climbs a per repetition, so arm C
                  alone must refuse.
      Z-ORBIT  GROW x8; WC(b,1); loop { GROW; ADD a,b,b; TEST a }
               -- the genuinely data-gated grower, and the arm for the
                  ZERO lock the orbit pays: the old windows of modulus 3
                  read 2 at every repetition, so that lock fires and the
                  ONE instrument correctly does not.
    A WRITE-CONSTANT REACHES THE WINDOWS PRESENT AND NO OTHERS, so both
    programs needing an old window to differ from a young one issue a
    GROW ahead of the write. One issued to an EMPTY pool reaches nothing
    and every window is then born 0 there instead -- a property of the
    machine rather than of these programs, and the reason each carries
    its lead.
    Both refusers keep the test's target at pc+1 so the loop's shape
    does not depend on the bit -- the segment then genuinely repeats
    and the moving bit is a real refusal and not a different run.
    KILL (prints as ARM-MISS): STATIC not certified by LOCK-STATIC, or
    a refuser certified, or a refuser refused by an arm other than the
    one it was built for.

D7  THE ROBUSTNESS SWEEP. D4 is ONE draw. Seed and program length, one
    dial at a time off the census cell, with the converted count and
    the ONE instrument's share of the grow-heavy population printed per
    cell and as a range.
    KILL (prints as DRAW-BOUND): the ONE instrument's share spans more
    than 25 points across the cells -- D4 is then a statement about a
    seed. The span prints whether or not it fires.

D9  THE SEGMENT CHOICE, added by the audit round that added D8 and
    carrying no frozen prediction either. The certifier takes the FIRST
    repeated program counter holding a grow. That is ITS choice and not
    the program's -- the same arbitrariness the cut point had, one level
    up -- so "uncovered" is a statement about one segment until the
    choice is swept. Sweep it: for each uncovered program, retry the
    certificate at the 1st, 2nd, ... later repeat instead, and report
    how many certify at some later choice. Every rescue is then held to
    D1 and D2 -- replayed to 600 grows and its forcings compared against
    the bit the machine reads at every execution -- because a rescue
    that cannot pass those is a bug in the sweep and not a certificate.
    KILL (prints as CHOICE-UNSOUND): a rescued program that halts,
    stalls, or disagrees with the machine at any repetition.

D8  THE RESIDUE'S BITS, added by the audit round that caught the claim
    it replaces and carrying no frozen prediction: a REFUSAL IS NOT A
    VERDICT ON THE BIT. The instrument declining to force a ONE says
    nothing about whether the bit is constant, so reading the residue's
    reason labels as "these bits move" is an inference. Replay each
    uncovered program and collect the SET of values each of its
    segment's tests takes; a test whose set has two elements is a bit
    NO sound scheme can force, the segment not repeating with the same
    answers. The residue then splits into what this instrument misses
    and what nothing could have certified, which is the only reading
    that says whether the remaining room is the scheme's at all.

FINDINGS (entered post-run, from the printed output).

F1  THE FORCED-ONE DIRECTION IS NOT A WALL, AND THE RESIDUE COLLAPSES
    (rule for the instrument's soundness, derived above with the run a
    cross-check; observation for the coverage). On the identical census
    cell the earlier rig froze -- 600 programs, seed 11, length 12, step
    cap 4000, sqrt supply, r=3, 109 grow-heavy -- certified coverage
    goes 52 -> 102 and the uncovered residue 57 -> 7. LOCK-CARRIED
    coverage, the number that matters because a branch-free cycle costs
    the normal form nothing, goes 3 -> 53. Locks fired, by test:
    ONE 3, ZERO-C 1, ZERO-F 0, STATIC-1 34, STATIC-0 1, ONE-DYN 22,
    ZERO-ORBIT 0; by program, 32 carry STATIC-1 and 20 carry ONE-DYN.
    ZERO-C's rise from 0 to 1 is not a new reach: certification is
    all-or-nothing per program, so a program that used to be refused at
    its FIRST unforced test now gets past it and reaches a later test
    the old locks always could have forced.

F2  SOUNDNESS, AND IT IS CHECKED AT EVERY OFFSET AND NOT AT ONE
    (positive controls D1 and D2). 102 certified programs replayed:
    0 UNSOUND, none halting or stalling short of 600 grows. The
    cross-check is the one the earlier rig could not make -- a forcing
    is a claim about every repetition -- and its FIRST form was wrong in
    a way the audit round caught: it mapped each TEST INSTRUCTION to one
    bit, while a single TEST can execute twice inside one segment at two
    offsets with two different last writes, so its two bits are
    legitimately different and the check reported mismatches of its own
    making. Walking the body CYCLICALLY by offset fixes it and is
    strictly stronger, because the program counter is then checked too
    and the check becomes the claim -- the segment repeats -- rather
    than a shadow of it. Under the corrected form: 0 mismatches over the
    population, and 0 over each designed program at 3,994-5,454 checked
    offsets apiece.

F3  THE SPLIT THE EARLIER CENSUS CALLED STABLE WAS A PROPERTY OF ITS
    LOCK SET (observation). "93-100% of every draw's certificates hold
    no test at all" was true of three locks and is false of these: the
    branch-free share of certificates falls from 94% (49 of 52) to 48%
    (49 of 102) on the same draw, the 49 unchanged and the denominator
    doubled. Nothing about the population moved; the reading was about
    the instrument.

F4  HALF (b) IS ANSWERED BY FIXED POINTS, AND CYCLES NEVER APPEAR
    (observation; the prediction held). Over the 34 (segment, test,
    grow-offset) triples the census reaches arm C with, the free integer
    action's fate is FIXED 32, NEITHER 2, CYCLE 0, OVERFLOW 0. The
    frozen prediction was NEITHER under a quarter with FIXED the
    plurality; NEITHER is 6%. What was not predicted is that CYCLE is
    EMPTY: the action either stops moving or never settles, with no
    proper period in between, so the k-quantifier is collapsed by a
    fixed point or not at all. Of the 2 NEITHER triples, 1 has its
    READ VALUE settle inside the budget while its state does not --
    which names a backward SLICE of the state as the next instrument
    and is an observation, "stable for 200 steps" not being stable.

F5  THE FREE CASE CARRIES THE PLURALITY BUT NOT THE BULK, AND THE
    PREDICTION INVERTS ON ONE DIAL (observation; the prediction half
    held). Of the 53 lock-carried programs, 28 carry STATIC-1 alone, 17
    ONE-DYN alone, 3 both, and the remaining 5 an older lock (ONE 3,
    STATIC-0 1, STATIC-1 with ZERO-C 1) -- so STATIC-1 is on 32 and
    ONE-DYN on 20. The frozen prediction said the static case would
    carry the bulk and A/B/C add "few", and 20 of 53 is not few. At
    PROGRAM length 20 -- the sweep's dial, which lengthens segments only
    as a consequence -- the order REVERSES: ONE-DYN 41 against
    STATIC-1 31. So the dynamic arms are not a garnish on the static
    case, and what they carry rises with program length, a longer
    program writing the tested register inside the segment more often,
    which is exactly the case STATIC cannot take.

F6  THE EARLIER RESIDUE LABEL OVERCOUNTS THE FREE CASE BY A QUARTER
    (observation, and the reason the lock scans the whole body). The
    earlier rig's label "unwritten-in-segment" comes from a backward
    scan STARTING AT THE TEST, so a write at an offset past the test
    wears it. Of that draw's 46 so labelled, 33 are LOCK-STATIC and 13
    carry a write PAST the test -- the label and the lock are different
    predicates, and the frozen prediction that STATIC would convert at
    least half of the 46 held on the true count.

F7  TWO DESIGNED PROGRAMS WERE BUILT WRONG THE SAME WAY, AND THE FAULT
    IS A MACHINE FACT WORTH STATING (a rig correction, entered before
    F1 was read). A WRITE-CONSTANT REACHES THE WINDOWS PRESENT AND NO
    OTHERS. The first A-REFUSE program issued its write ahead of every
    GROW, so it reached an empty pool, every window was born 0 there,
    and the program certified by ONE-DYN instead of exhibiting arm A's
    necessity -- an ARM-MISS caused by the specimen and not by the arm.
    Adding one GROW ahead of the write fixes it. THE SAME FAULT SITS IN
    THE CORPUS'S OWN "DATA-GATED GROWER" (explore_growth_certificate.py
    D2), whose WC also precedes its first GROW: it is data-gated in name
    only, every window increments by zero, and this instrument certifies
    it by ONE-DYN. The frozen D3 prediction that it would certify HELD
    and the mechanism named for it -- an old window's orbit forcing a
    ZERO -- was WRONG, because the program has no old window that
    differs from a young one. The genuinely data-gated grower is the
    Z-ORBIT arm added here, eight grows ahead of the write, whose old
    windows of modulus 3 read 2 at every repetition; it is the only
    program in this file that fires ZERO-ORBIT, which fires nowhere in
    the random population.

F8  THE RESIDUE'S BITS MOVE, WHICH IS A FACT ABOUT THE SEGMENT AND NOT
    ABOUT THE PROGRAM (observation, no frozen prediction; D8, added by
    the audit round that caught the claim it replaces). Reading the
    residue's refusal labels as "these bits move" was an inference: a
    refusal says the instrument cannot force a ONE, never that the bit
    is constant. Measured instead, 6 of the 7 uncovered programs hold a
    test whose bit takes BOTH values across the replay, so THAT segment
    does not repeat with the same answers and no sound scheme can force
    that bit; 1 holds only constant bits. What this does NOT say is
    that the program is uncertifiable -- see F9.

F9  THE BINDING LIMIT WAS THE CERTIFIER'S OWN ARBITRARY CHOICE, AND
    SWEEPING IT LEAVES A RESIDUE OF ONE (observation, no frozen
    prediction; D9, and every rescue held to D1 and D2). The certifier
    takes the FIRST repeated program counter holding a grow. Retried at
    later repeats, 6 of the 7 uncovered programs CERTIFY -- at repeats
    2, 3, 4, 4, 6 and 7, by ZERO-C, STATIC-0, and ZERO-ORBIT three
    times, once with ONE and once with STATIC-1 and ONE-DYN beside it --
    each replayed to 600 grows and each agreeing with the machine at
    every offset of a 2,500-to-5,454-step cyclic check. So on this draw
    the residue is 1 of 109 grow-heavy programs, not 7, and the reason
    the last one survives is EXACTLY D5's route limit: it is a
    C/neither, its integer action neither stabilising nor cycling. That
    reverses what this file said one round earlier -- the route limit
    does not cost zero certificates, it is the ONLY thing still costing
    one. This is the cut point's arbitrariness one level up (the
    earlier rig's F6), and the same lesson: a residue tally is worth
    nothing until the certifier's own free choices are swept.

F10 THE QUESTION WAS POSED IN TWO HALVES AND THE OBJECT HAS THREE, AND
    THE MISSING ONE IS INERT (observation; D10). The forced-ONE
    direction was set as two halves -- windows ALREADY IN THE POOL and
    windows BORN IN LATER REPETITIONS. A window born at a grow inside
    the SAME repetition, before the test, is in neither: it is younger
    than the pool and it is not born later. So the decomposition the
    question carried had a gap, and a scheme built to it would have
    been unsound in principle. In fact arm B changes NOTHING here: the
    census certifies 102 with it and 102 without, with zero cross-check
    mismatches and zero unsound either way, because its antecedent is
    SHADOWED -- on an unbounded supply a non-zero read at the last grow
    before the test is LOCK-ZERO-F's, consulted first, so arm B decides
    only at an EARLIER grow or where the modulus is too small, and
    neither happens on this draw. Derived-necessary, empirically inert.
    D6 accordingly has no program built to make arm B the decider, and
    building one means going to the bounded supply, where ZERO-F is
    unavailable by construction -- which is the same place the
    supply-specificity witness lives.

WHAT THIS LEAVES. The scheme's wall has MOVED, and what is left is one
program in 109 and one named question. Once the segment choice is swept,
every arm but arm C's route is paid, and the survivor is the case where
the free integer action neither stabilises nor cycles -- where a
backward SLICE of the state is the next instrument, the state being what
fails to settle while the READ VALUE sometimes does. Two dials remain
unswept and are named rather than claimed: the segment choice was swept
only 11 repeats deep, and the whole census is one random population.
None of this touches the capacity conjecture, which asks whether EVERY
forever-growing program is certifiable: what is bounded here is a
scheme, and a program can be built to defeat any of these arms.

D10 WHAT ARM B DECIDES, added by the audit round that noticed the claim
    of reach above had no measurement under it. Run the census with arm
    B disabled and count what changes: certificates, cross-check
    mismatches, and unsoundness. A derived-necessary arm that changes
    nothing is worth saying so about, and an arm whose removal breaks
    the cross-check is load-bearing in fact and not only on paper.
    KILL (prints as B-UNSOUND): disabling arm B produces a certificate
    that fails D1 or D2 -- the arm is then load-bearing and the census
    ran without knowing it.

RUN RECORD: python explore_forced_one.py -> D3 battery pass (halting and
frozen-pulse NO-CERTIFICATE, forever-growing and data-gated CERTIFIED,
the latter by ONE-DYN); D6 arm pass -- STATIC certified by STATIC-1
alone, A-REFUSE refused by "A/old window moves", C-REFUSE by
"C/neither", Z-ORBIT certified by ZERO-ORBIT alone; D4 109 grow-heavy,
102 CERTIFIED of which 49 branch-free, locks ONE 3 / ZERO-C 1 /
ZERO-F 0 / STATIC-1 34 / STATIC-0 1 / ONE-DYN 22 / ZERO-ORBIT 0,
residue 7 = 4 C/young-earlier non-zero + 2 C/neither + 1 B/young-same
non-zero; D4 label gap 46 labelled, 33 LOCK-STATIC, 13 written past the
test; D5 34 arm-C triples, fixed 32 / neither 2 / cycle 0 / overflow 0,
1 of the 2 NEITHER with its read value settled; D8 residue bits 6 of 7
moving (B/young-same 0/1, C/neither 2/0, C/young-earlier 4/0);
D1 0 UNSOUND of 102;
D2 0 mismatches under the offset-walking form; D9 6 of 7 uncovered
rescued at repeats 2-7, every rescue passing D1 and D2, the survivor a
C/neither; D10 arm B changes 0 of 102 certificates with 0
mismatches and 0 unsound; D7 ONE-instrument share of grow-heavy 48-62% (span 14
against a kill at 25), certified 102-112 of 109-123 heavy across the
four cells; VERDICT all pass, exit 0. Wall 3 min, memory trivial
(no numpy).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_born_at_zero import (          # the machine, verbatim
    ADD, SUB, MUL, WC, GROW, TEST, JMP, HALT, SUPPLIES, VM,
)
from explore_growth_certificate import (    # the earlier rig, verbatim
    MAG_GUARD, free_eval, still_growing, random_program, classify,
)

ORBIT_BUDGET = 20000      # states enumerated per old window before declining
INT_STEPS = 200           # repetitions of the integer action before declining
ARM_B = True              # D10 flips this to measure what arm B decides


# ------------------------------------------------- evaluation helpers

def eval_from(word, col):
    """Free INTEGER evaluation of WORD starting from COL (not all-zero).
    Returns (cols, overflowed); the vector is untrustworthy when the
    guard tripped and the caller must decline."""
    col = list(col)
    over = False
    for ins in word:
        op = ins[0]
        if op in (ADD, SUB, MUL):
            _, a, b, c = ins
            v = (col[b] + col[c]) if op == ADD else \
                (col[b] - col[c]) if op == SUB else (col[b] * col[c])
            if v.bit_length() > MAG_GUARD:
                over = True
                v = 0
            col[a] = v
        elif op == WC:
            col[ins[1]] = ins[2]
    return col, over


def eval_mod(word, col, m):
    """Evaluation of WORD on one window: componentwise, modulus m."""
    col = list(col)
    for ins in word:
        op = ins[0]
        if op in (ADD, SUB, MUL):
            _, a, b, c = ins
            v = (col[b] + col[c]) if op == ADD else \
                (col[b] - col[c]) if op == SUB else (col[b] * col[c])
            col[a] = v % m
        elif op == WC:
            col[ins[1]] = ins[2] % m
    return col


def writes(word, a):
    """Does WORD write register A anywhere -- data op or write-constant?"""
    for ins in word:
        if ins[0] in (ADD, SUB, MUL, WC) and ins[1] == a:
            return True
    return False


# ------------------------------------------------- ARM A: the old windows

def orbit_reads(word, s, a, col, m):
    """Every value register A takes at the test offset, over ALL
    repetitions, for one old window of modulus M at column COL.
    Returns (values, closed): CLOSED False means the orbit did not close
    inside the budget and the arm must decline."""
    seen = set()
    vals = set()
    cur = tuple(col)
    while cur not in seen:
        if len(seen) >= ORBIT_BUDGET:
            return vals, False
        seen.add(cur)
        vals.add(eval_mod(word[:s], cur, m)[a])
        cur = tuple(eval_mod(word, cur, m))
    return vals, True


# ------------------------------------------------- ARM C: the integer action

def integer_fate(word, s, a, start):
    """The free integer action y_{k+1} = SEG(y_k) from START, read at the
    test offset. Returns (fate, all_reads_zero, read_settled) with FATE
    one of 'fixed' / 'cycle' / 'neither' / 'overflow'. ALL_READS_ZERO is
    true only when the action closed AND every read was 0. READ_SETTLED
    is an OBSERVATION -- whether the read value alone repeated inside the
    budget -- and never a forcing."""
    seen = {}
    cur = tuple(start)
    reads = []
    read_seen = set()
    read_settled = False
    for k in range(INT_STEPS):
        if cur in seen:
            fate = "fixed" if seen[cur] == k - 1 else "cycle"
            return fate, all(v == 0 for v in reads), True
        seen[cur] = k
        pre, over = eval_from(word[:s], cur)
        if over:
            return "overflow", False, read_settled
        reads.append(pre[a])
        if pre[a] in read_seen:
            read_settled = True
        read_seen.add(pre[a])
        nxt, over = eval_from(word, cur)
        if over:
            return "overflow", False, read_settled
        cur = tuple(nxt)
    return "neither", False, read_settled


# ------------------------------------------------- the segment

def find_segment(prog, supply, r, cap):
    """As explore_growth_certificate.py's, plus the COLUMNS at t1 -- half
    (a) needs the pool's contents and not only its moduli."""
    vm = VM(prog, supply, r)
    seen = {}
    executed = []
    for t in range(cap):
        if vm.halted:
            return None
        pc = vm.pc
        if not (0 <= pc < len(prog)):
            return None
        ins = prog[pc]
        bit = None
        if ins[0] == TEST:
            bit = all(col[ins[1]] == 0 for col in vm.cols)
        if pc in seen:
            t1, g1, mods, cols = seen[pc]
            if vm.g > g1:
                return (t1, t, executed, mods, cols)
        else:
            seen[pc] = (t, vm.g, list(vm.moduli),
                        [list(c) for c in vm.cols])
        executed.append((pc, ins, bit))
        vm.step()
    return None


LOCKS = ("ONE", "ZERO-C", "ZERO-F", "STATIC-1", "STATIC-0",
         "ONE-DYN", "ZERO-ORBIT")


def certify(prog, supply, r, cap, fates=None):
    """The earlier three locks, plus the forced-ONE instrument and the
    zero lock its orbit pays. Returns (verdict, detail) and, when FATES
    is a dict, tallies arm C's integer-action fates into it."""
    seg = find_segment(prog, supply, r, cap)
    if seg is None:
        return "NO-CERTIFICATE", "no cycling segment with a grow"
    t1, t2, executed, pool, cols = seg
    body = executed[t1:t2]
    if not any(ins[0] == GROW for _, ins, _ in body):
        return "NO-CERTIFICATE", "segment holds no grow"
    # rotate the cut to a GROW, carrying the pool AND its columns through
    rho = next(i for i, (_, ins, _) in enumerate(body) if ins[0] == GROW)
    g0 = sum(1 for _, i, _ in executed[:t1] if i[0] == GROW)
    for _, i, _ in body[:rho]:
        if i[0] in (ADD, SUB, MUL, WC):
            cols = [eval_mod([i], c, m) for c, m in zip(cols, pool)]
        elif i[0] == GROW:
            g0 += 1
            pool = pool + [supply(g0)]
            cols = cols + [[0] * r]
    body = body[rho:] + body[:rho]
    monotone = all(supply(g) <= supply(g + 1) for g in range(1, 400))
    unbounded = supply(400) > supply(1)
    locks = dict((k, 0) for k in LOCKS)
    word = [ins for _, ins, _ in body]
    grow_offsets = [u for u, ins in enumerate(word) if ins[0] == GROW]
    # distinct old windows: equal modulus and column means equal orbit
    distinct = sorted(set((m, tuple(c)) for m, c in zip(pool, cols)))
    for s, (_, ins, bit) in enumerate(body):
        if ins[0] != TEST:
            continue
        a = ins[1]
        forced = None
        arm = None
        if not writes(word, a):
            forced = (bit, "STATIC-1" if bit else "STATIC-0")
        if forced is None:
            last = None
            for u in range(s - 1, -1, -1):
                op = word[u]
                if op[0] in (ADD, SUB, MUL) and op[1] == a:
                    last = ("data", None)
                    break
                if op[0] == WC and op[1] == a:
                    last = ("const", op[2])
                    break
            if last is not None and last[0] == "const":
                c = last[1]
                if c == 0:
                    forced = (True, "ONE")
                elif any(m and c % m != 0 for m in pool):
                    forced = (False, "ZERO-C")
            if forced is None and monotone and unbounded:
                befores = [u for u in grow_offsets if u < s]
                if befores:
                    gpos = max(befores)
                    fresh, over = free_eval(word[gpos + 1:s], r)
                    if not over and fresh[a] != 0:
                        gb = g0 + sum(1 for u in grow_offsets if u <= gpos)
                        if supply(gb) > abs(fresh[a]):
                            forced = (False, "ZERO-F")
        if forced is None:
            # ---- THE FORCED-ONE INSTRUMENT
            # A: every old window reads 0 at every repetition
            for m, c in distinct:
                vals, closed = orbit_reads(word, s, a, c, m)
                if not closed:
                    arm = "A/orbit past budget"
                    break
                if vals != set([0]):
                    arm = "A/old window moves"
                    break
            if arm is None and ARM_B:
                # B: every young-same window's fixed integer is 0
                for d in grow_offsets:
                    if d >= s:
                        continue
                    v, over = free_eval(word[d + 1:s], r)
                    if over:
                        arm = "B/past the magnitude guard"
                        break
                    if v[a] != 0:
                        arm = "B/young-same non-zero"
                        break
            if arm is None:
                # C: the integer action, per grow offset
                for d in grow_offsets:
                    start, over = free_eval(word[d + 1:], r)
                    if over:
                        if fates is not None:
                            fates["overflow"] = fates.get("overflow", 0) + 1
                        arm = "C/past the magnitude guard"
                        break
                    fate, zero, settled = integer_fate(word, s, a, start)
                    if fates is not None:
                        fates[fate] = fates.get(fate, 0) + 1
                        if fate == "neither" and settled:
                            fates["neither-read-settled"] = \
                                fates.get("neither-read-settled", 0) + 1
                    if fate in ("neither", "overflow"):
                        arm = "C/" + fate
                        break
                    if not zero:
                        arm = "C/young-earlier non-zero"
                        break
            if arm is None:
                forced = (True, "ONE-DYN")
        if forced is None:
            # ---- the zero lock the same orbit pays
            for m, c in distinct:
                vals, closed = orbit_reads(word, s, a, c, m)
                if closed and 0 not in vals:
                    forced = (False, "ZERO-ORBIT")
                    break
        if forced is None:
            return "NO-CERTIFICATE", arm
        if forced[0] != bit:
            return "BUG", "forced %s but the run read %s" % (forced[0], bit)
        locks[forced[1]] += 1
    return "CERTIFIED", locks


# ------------------------------------------------- D2: the forcing cross-check

def cross_check(prog, supply, r, cap, reps_cap=20000):
    """Replay from the segment's start and walk the body CYCLICALLY,
    comparing the machine against the segment offset by offset: the
    program counter must match at every step and every TEST must read
    the bit the segment recorded at THAT offset.

    KEYING BY INSTRUCTION IS WRONG AND THE AUDIT ROUND CAUGHT IT: one
    TEST can execute twice inside a single segment, at two offsets with
    two different last writes, and its two bits are then legitimately
    different. A check that maps the instruction to one bit compares
    every later execution against whichever came first and reports
    mismatches that are its own. Walking the offsets also makes the
    check the claim -- the segment repeats -- rather than a weaker
    shadow of it.

    Returns (checked, mismatches)."""
    seg = find_segment(prog, supply, r, cap)
    if seg is None:
        return 0, 0
    t1, t2, executed, pool, cols = seg
    body = executed[t1:t2]
    if not body:
        return 0, 0
    vm = VM(prog, supply, r)
    for _ in range(t1):
        vm.step()
    checked = bad = 0
    for u in range(reps_cap):
        if vm.halted or not (0 <= vm.pc < len(prog)):
            break
        pc, ins, bit = body[u % len(body)]
        if vm.pc != pc:
            bad += 1
            break
        if ins[0] == TEST:
            checked += 1
            if all(col[ins[1]] == 0 for col in vm.cols) != bit:
                bad += 1
        vm.step()
    return checked, bad


# ------------------------------------------------- D3: the battery

def battery(r=3):
    p_halt = [(GROW,), (GROW,), (GROW,), (WC, 1, 1)] + \
             [(ADD, 0, 0, 1)] * 5 + [(HALT,)]
    p_pulse = [(GROW,), (GROW,), (GROW,), (WC, 1, 1),
               (ADD, 0, 0, 1), (TEST, 0, 4), (JMP, 4)]
    p_grow = [(WC, 1, 1), (GROW,), (ADD, 0, 0, 1), (JMP, 1)]
    p_gated = [(WC, 1, 1), (GROW,), (ADD, 0, 0, 1), (TEST, 0, 5),
               (JMP, 1), (JMP, 1)]
    ok = True
    misfire = unsound = mismatch = False
    for name, prog, expect in (("halting", p_halt, "NO-CERTIFICATE"),
                               ("frozen-pulse", p_pulse, "NO-CERTIFICATE"),
                               ("forever-growing", p_grow, "CERTIFIED"),
                               ("data-gated", p_gated, "CERTIFIED")):
        v, d = certify(prog, SUPPLIES["sqrt"], r, cap=4000)
        fired = ([k for k, n in d.items() if n] if v == "CERTIFIED" else d)
        print("D3 %-16s %s  (%s)" % (name, v, fired))
        if v == "CERTIFIED":
            alive, t, g = still_growing(prog, SUPPLIES["sqrt"], r,
                                        cap=40000, target=600)
            c, b = cross_check(prog, SUPPLIES["sqrt"], r, 4000)
            print("D1   replay: reached-600-grows=%s at step %d; "
                  "D2 forcings checked %d, mismatches %d" % (alive, t, c, b))
            unsound = unsound or not alive
            mismatch = mismatch or bool(b)
            if name in ("halting", "frozen-pulse"):
                misfire = True
        ok = ok and v == expect
    if misfire:
        print("D3 ** MISFIRE **")
    if unsound:
        print("D1 ** UNSOUND **")
    if mismatch:
        print("D2 ** FORCE-MISMATCH **")
    return ok and not (misfire or unsound or mismatch)


# ------------------------------------------------- D6: the designed arm

def designed_arm(r=3, lead=30):
    # STATIC: register 0 is written nowhere in the loop
    b = lead
    p_static = [(GROW,)] * lead + [(GROW,), (WC, 1, 1), (ADD, 2, 1, 1),
                                   (TEST, 0, b + 4), (JMP, b)]
    # A-REFUSE: old windows hold reg1 = 1, young ones do not. THE GROW
    # AHEAD OF THE WRITE IS THE POINT -- a write-constant reaches the
    # windows PRESENT, so one issued to an empty pool reaches nothing.
    p_a = [(GROW,), (WC, 1, 1)] + [(GROW,)] * (lead - 1) + \
          [(GROW,), (TEST, 0, lead + 3), (ADD, 0, 0, 1), (JMP, lead + 1)]
    # C-REFUSE: no grow ahead of the loop, so the pool at t1 is EMPTY
    p_c = [(GROW,), (TEST, 0, 2), (ADD, 0, 0, 1), (WC, 1, 1), (JMP, 0)]
    # ZERO-ORBIT: the genuinely data-gated grower -- eight grows, then
    # the write, so the old windows carry the increment and the young
    # ones do not, and the four of modulus 3 read 2 at every repetition.
    p_zo = [(GROW,)] * 8 + [(WC, 1, 1), (GROW,), (ADD, 0, 1, 1),
                            (TEST, 0, 12), (JMP, 9)]
    ok = True
    v, d = certify(p_static, SUPPLIES["sqrt"], r, cap=4000)
    fired = [k for k, n in d.items() if n] if v == "CERTIFIED" else []
    hit = (v == "CERTIFIED" and fired == ["STATIC-1"])
    print("D6 STATIC    arm: %s  %s%s"
          % (v, d, "" if hit else "  ** ARM-MISS **"))
    if hit:
        alive, t, g = still_growing(p_static, SUPPLIES["sqrt"], r,
                                    cap=40000, target=600)
        c, bad = cross_check(p_static, SUPPLIES["sqrt"], r, 4000)
        print("D1   replay: reached-600-grows=%s; D2 checked %d, "
              "mismatches %d" % (alive, c, bad))
        hit = hit and alive and not bad
    ok = ok and hit
    for name, prog, want in (("A-REFUSE", p_a, "A/"), ("C-REFUSE", p_c, "C/")):
        v, d = certify(prog, SUPPLIES["sqrt"], r, cap=4000)
        hit = (v == "NO-CERTIFICATE" and isinstance(d, str)
               and d.startswith(want))
        print("D6 %-9s arm: %s  (%s)%s"
              % (name, v, d, "" if hit else "  ** ARM-MISS **"))
        ok = ok and hit
    v, d = certify(p_zo, SUPPLIES["sqrt"], r, cap=4000)
    fired = [k for k, n in d.items() if n] if v == "CERTIFIED" else []
    hit = (v == "CERTIFIED" and fired == ["ZERO-ORBIT"])
    print("D6 Z-ORBIT   arm: %s  %s%s"
          % (v, d, "" if hit else "  ** ARM-MISS **"))
    if hit:
        alive, t, g = still_growing(p_zo, SUPPLIES["sqrt"], r,
                                    cap=40000, target=600)
        c, bad = cross_check(p_zo, SUPPLIES["sqrt"], r, 4000)
        print("D1   replay: reached-600-grows=%s; D2 checked %d, "
              "mismatches %d" % (alive, c, bad))
        hit = hit and alive and not bad
    return ok and hit


# ------------------------------------------------- D4 + D5: the census

def census(trials=600, r=3, length=12, seed=11, cap=4000, verbose=True):
    import random
    rng = random.Random(seed)
    heavy = []
    for _ in range(trials):
        prog = random_program(rng, r, length)
        if classify(prog, SUPPLIES["sqrt"], r, cap)[0] == "grow-heavy":
            heavy.append(prog)
    tally = dict((k, 0) for k in LOCKS)
    fates = {}
    certified = []
    trivial = one_dyn = static_one = bugs = 0
    reasons = {}
    for prog in heavy:
        v, d = certify(prog, SUPPLIES["sqrt"], r, cap, fates=fates)
        if v == "CERTIFIED":
            certified.append(prog)
            if not any(d.values()):
                trivial += 1
            for k in tally:
                tally[k] += d[k]
            if d["ONE-DYN"]:
                one_dyn += 1
            if d["STATIC-1"]:
                static_one += 1
        elif v == "BUG":
            bugs += 1
            print("D4 ** BUG ** %s" % (d,))
        else:
            reasons[d] = reasons.get(d, 0) + 1
    n = len(heavy)
    if not verbose:
        return n, len(certified), trivial, static_one, one_dyn
    print("D4 grow-heavy %d, CERTIFIED %d, of which %d hold NO TEST; "
          "locks %s" % (n, len(certified), trivial, tally))
    print("D4 ONE instrument: %d programs carry STATIC-1, %d carry "
          "ONE-DYN%s" % (static_one, one_dyn,
                         "  ** ONE-VACUOUS **"
                         if not (static_one or one_dyn) else ""))
    print("D4 residue: " + ", ".join(
        "%s %d" % (k, v)
        for k, v in sorted(reasons.items(), key=lambda x: -x[1])))
    tot = sum(v for k, v in fates.items() if k != "neither-read-settled")
    print("D5 arm-C integer action over %d triples: %s" % (tot, fates))
    if tot:
        plur = max((v, k) for k, v in fates.items()
                   if k != "neither-read-settled")[1]
        print("D5 plurality: %s%s"
              % (plur, "  ** NON-DECIDABLE-ROUTE **"
                 if plur == "neither" else ""))
    unsound = mism = 0
    for prog in certified:
        alive, t, g = still_growing(prog, SUPPLIES["sqrt"], r,
                                    cap=20000, target=600)
        if not alive:
            unsound += 1
        c, bad = cross_check(prog, SUPPLIES["sqrt"], r, cap)
        mism += bad
    print("D1 soundness: %d UNSOUND of %d certified" % (unsound, len(certified)))
    print("D2 cross-check: %d mismatches over the certified population%s"
          % (mism, "  ** FORCE-MISMATCH **" if mism else ""))
    return (bugs == 0 and unsound == 0 and mism == 0
            and bool(static_one or one_dyn))


def residue_bits(trials=600, r=3, length=12, seed=11, cap=4000):
    """D8, added by the audit round that caught the claim it replaces.
    A REFUSAL IS NOT A VERDICT ON THE BIT: the instrument declining to
    force a ONE says nothing about whether the bit is constant, so
    reading the residue's reason labels as "these bits move" is an
    inference and not a measurement. Measure it: replay each uncovered
    program and collect the SET of values each of its segment's tests
    takes. A test whose set has two elements is a bit no sound scheme
    can force -- the segment does not repeat with the same answers -- and
    the residue splits into what the instrument MISSES and what nothing
    could have certified."""
    import random
    rng = random.Random(seed)
    heavy = []
    for _ in range(trials):
        prog = random_program(rng, r, length)
        if classify(prog, SUPPLIES["sqrt"], r, cap)[0] == "grow-heavy":
            heavy.append(prog)
    moved = still = 0
    by_reason = {}
    for prog in heavy:
        v, d = certify(prog, SUPPLIES["sqrt"], r, cap)
        if v != "NO-CERTIFICATE":
            continue
        seg = find_segment(prog, SUPPLIES["sqrt"], r, cap)
        if seg is None:
            continue
        t1, t2, executed, pool, cols = seg
        tests = set(i for _, i, _ in executed[t1:t2] if i[0] == TEST)
        vm = VM(prog, SUPPLIES["sqrt"], r)
        obs = {}
        for t in range(20000):
            if vm.halted or not (0 <= vm.pc < len(prog)):
                break
            ins = prog[vm.pc]
            if t >= t1 and ins[0] == TEST and ins in tests:
                obs.setdefault(ins, set()).add(
                    all(c[ins[1]] == 0 for c in vm.cols))
            vm.step()
        m = any(len(vals) > 1 for vals in obs.values())
        moved += m
        still += not m
        by_reason.setdefault(d, [0, 0])[0 if m else 1] += 1
    print("D8 residue bits: %d of %d uncovered hold a test whose bit MOVES "
          "across repetitions -- unforceable by any sound scheme -- and %d "
          "hold only constant bits this instrument misses" % (moved,
          moved + still, still))
    print("D8 by refusal reason (moves/constant): " + ", ".join(
        "%s %d/%d" % (k, v[0], v[1]) for k, v in sorted(by_reason.items())))
    return moved, still


def segment_choice(trials=600, r=3, length=12, seed=11, cap=4000):
    """D9: is "uncovered" a fact about the program or about the segment
    the certifier happened to pick? Retry each uncovered program at
    later repeats of a program counter, and hold every rescue to D1 and
    D2 before counting it."""
    import random
    rng = random.Random(seed)
    heavy = []
    for _ in range(trials):
        prog = random_program(rng, r, length)
        if classify(prog, SUPPLIES["sqrt"], r, cap)[0] == "grow-heavy":
            heavy.append(prog)
    residue = []
    for prog in heavy:
        v, d = certify(prog, SUPPLIES["sqrt"], r, cap)
        if v == "NO-CERTIFICATE":
            residue.append((prog, d))
    default = find_segment
    rescued = 0
    unsound = 0
    rows = []
    for prog, reason in residue:
        hit = None
        for skip in range(1, 12):
            globals()["find_segment"] = _skipping(default, skip)
            v, d = certify(prog, SUPPLIES["sqrt"], r, cap)
            if v == "CERTIFIED":
                alive, t, g = still_growing(prog, SUPPLIES["sqrt"], r,
                                            cap=40000, target=600)
                c, bad = cross_check(prog, SUPPLIES["sqrt"], r, cap)
                if not alive or bad:
                    unsound += 1
                hit = (skip, sorted(k for k, n in d.items() if n), c, bad)
                break
        globals()["find_segment"] = default
        rescued += hit is not None
        rows.append((reason, hit))
    for reason, hit in rows:
        print("D9   %-32s %s" % (reason, "rescued at repeat %d by %s "
              "(D2 checked %d, mismatches %d)" % hit if hit
              else "NOT rescued at any of the next 11 repeats"))
    print("D9 segment choice: %d of %d uncovered certify at a LATER repeat "
          "-- the certifier's own choice, not the program%s"
          % (rescued, len(residue),
             "  ** CHOICE-UNSOUND **" if unsound else ""))
    return rescued, len(residue), unsound == 0


def _skipping(base, skip):
    """find_segment, but returning the (skip+1)-th qualifying segment."""
    def fs(prog, supply, r, cap):
        vm = VM(prog, supply, r)
        seen = {}
        executed = []
        hits = 0
        for t in range(cap):
            if vm.halted:
                return None
            pc = vm.pc
            if not (0 <= pc < len(prog)):
                return None
            ins = prog[pc]
            bit = None
            if ins[0] == TEST:
                bit = all(col[ins[1]] == 0 for col in vm.cols)
            snap = (t, vm.g, list(vm.moduli), [list(c) for c in vm.cols])
            if pc in seen:
                t1, g1, mods, cols = seen[pc]
                if vm.g > g1:
                    if hits == skip:
                        return (t1, t, executed, mods, cols)
                    hits += 1
                    seen[pc] = snap
            else:
                seen[pc] = snap
            executed.append((pc, ins, bit))
            vm.step()
        return None
    return fs


def arm_b_reach(trials=600, r=3, length=12, seed=11, cap=4000):
    """D10: arm B is DERIVED-necessary -- a young-same window reading a
    non-zero integer breaks a ONE forcing -- but its antecedent is
    SHADOWED. Wherever the supply is unbounded, a non-zero read at the
    LAST grow before the test is LOCK-ZERO-F's, which is consulted
    first; so arm B is the decider only for a window born at an EARLIER
    grow, or where the modulus is too small. That is a claim about
    reach and it was made without a measurement. Measure it: run the
    census with arm B disabled and count what changes."""
    global ARM_B
    import random
    rng = random.Random(seed)
    heavy = []
    for _ in range(trials):
        prog = random_program(rng, r, length)
        if classify(prog, SUPPLIES["sqrt"], r, cap)[0] == "grow-heavy":
            heavy.append(prog)
    out = {}
    for flag in (True, False):
        ARM_B = flag
        cert = bad = unsound = 0
        for prog in heavy:
            v, d = certify(prog, SUPPLIES["sqrt"], r, cap)
            if v != "CERTIFIED":
                continue
            cert += 1
            c, m = cross_check(prog, SUPPLIES["sqrt"], r, cap)
            alive, t, g = still_growing(prog, SUPPLIES["sqrt"], r,
                                        40000, 600)
            bad += bool(m)
            unsound += not alive
        out[flag] = (cert, bad, unsound)
    ARM_B = True
    print("D10 arm B: census certifies %d with it and %d without; without "
          "it, %d cross-check mismatches and %d unsound" %
          (out[True][0], out[False][0], out[False][1], out[False][2]))
    print("D10 arm B changes %d outcomes on this population -- derived-"
          "necessary, empirically inert here" % abs(out[True][0] - out[False][0]))
    return out


def label_gap(trials=600, r=3, length=12, seed=11, cap=4000):
    """D4's second reading: of the residue the earlier rig labelled
    'unwritten-in-segment' (a backward scan from the test), how many have
    a write to the tested register PAST the test -- and so are not
    LOCK-STATIC. The label and the lock are different predicates."""
    import random
    from explore_growth_certificate import certify as certify_old
    rng = random.Random(seed)
    heavy = []
    for _ in range(trials):
        prog = random_program(rng, r, length)
        if classify(prog, SUPPLIES["sqrt"], r, cap)[0] == "grow-heavy":
            heavy.append(prog)
    labelled = static = 0
    for prog in heavy:
        v, d = certify_old(prog, SUPPLIES["sqrt"], r, cap)
        if v != "NO-CERTIFICATE" or not isinstance(d, str) \
                or not d.startswith("unwritten-in-segment"):
            continue
        labelled += 1
        v2, d2 = certify(prog, SUPPLIES["sqrt"], r, cap)
        if v2 == "CERTIFIED" and (d2["STATIC-1"] or d2["STATIC-0"]):
            static += 1
    print("D4 label gap: %d residue programs labelled unwritten-in-segment, "
          "%d of them are LOCK-STATIC -- %d carry a write PAST the test"
          % (labelled, static, labelled - static))
    return labelled, static


# ------------------------------------------------- D7: the sweep

def sweep(r=3):
    rows = []
    for dial, val, seed, length in (("census", 11, 11, 12),
                                    ("seed", 23, 23, 12),
                                    ("seed", 47, 47, 12),
                                    ("length", 20, 11, 20)):
        n, cert, triv, st, od = census(seed=seed, length=length,
                                       r=r, verbose=False)
        rows.append((dial, val, n, cert, triv, st, od))
        print("D7 %-6s=%-3s heavy %3d, certified %3d (trivial %3d), "
              "STATIC-1 %3d, ONE-DYN %3d, ONE-instrument share of heavy "
              "%.0f%%" % (dial, val, n, cert, triv, st, od,
                          100.0 * (st + od) / n if n else 0.0))
    shares = [100.0 * (st + od) / n for _, _, n, _, _, st, od in rows if n]
    span = max(shares) - min(shares)
    print("D7 RANGE: ONE-instrument share of grow-heavy %.0f-%.0f%% "
          "(span %.0f, kill at 25)%s"
          % (min(shares), max(shares), span,
             "  ** DRAW-BOUND **" if span > 25 else ""))
    return span <= 25


if __name__ == "__main__":
    ok1 = battery()
    print("D3 battery: " + ("pass" if ok1 else "KILL"))
    if not ok1:
        print("VERDICT: positive control failed -- nothing below is readable")
        sys.exit(1)
    ok2 = designed_arm()
    print("D6 designed arm: " + ("pass" if ok2 else "KILL"))
    ok3 = census()
    label_gap()
    residue_bits()
    arm_b_reach()
    ok5 = segment_choice()[2]
    ok4 = sweep()
    print("VERDICT: battery %s, arm %s, census %s, sweep %s, choice %s"
          % ("pass" if ok1 else "KILL", "pass" if ok2 else "KILL",
             "pass" if ok3 else "KILL", "pass" if ok4 else "KILL",
             "pass" if ok5 else "KILL"))
    sys.exit(0 if (ok1 and ok2 and ok3 and ok4 and ok5) else 1)
