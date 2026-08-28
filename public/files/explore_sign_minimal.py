"""Is the sign automaton's state count minimal, and does it answer to the
same normalized reach that prices addition's slack?

THE QUESTION. A signed-digit system (b, a) reads digits {-a..a} in radix b,
most-significant-first. Sign is finite-state: the clamped automaton
v <- b*v + d, absorbing once |v| > K with K = floor(a/(b-1)), reproduces
brute-force sign exactly, on 2K+3 states (explore_order_wall_shape.py F2).
That count is an UPPER BOUND and no minimality was claimed for it. The
derivation licenses absorbing at |v| >= ceil(a/(b-1)) while the rig absorbs
at floor(a/(b-1)) + 1; the two coincide except where (b-1) divides a, where
the rig carries one surplus state-pair. Surplus states cost correctness
nothing, so the brute-force agreement check cannot see them -- which is why
the question is still open after that rig ran clean.

It matters beyond bookkeeping because of a seam the same rig recorded (F4,
"one dial, two costs"). ADDITION's locality criterion prices a side of reach
x at ceil(x/(b-1)) slack units, and its winning-set endpoint is
a - ceil(a/(b-1)) (explore_lookahead_proof.py). SIGN's state count is stated
through floor(a/(b-1)). Both read the same ratio a/(b-1) -- the NORMALIZED
REACH, how many radix steps of headroom one side of the digit set buys --
under two different roundings. F4 filed sign's cost as answering to a
parameter addition's dial does not carry. If sign's MINIMAL count turns out
to be keyed on the CEILING, the two costs are two rounding modes of one
ratio and the seam sharpens into a single object; if the minimal count is
keyed on the floor, or on neither, they are genuinely separate costs and the
seam stands as filed.

THE SLATE, frozen before any engine code.

The object: the Moore machine over the alphabet {-a..a} whose state after
reading s is the clamped value of s and whose output is sgn(value(s)).
Minimality is Myhill-Nerode: u ~ v iff sgn(value(u.w)) = sgn(value(v.w)) for
every suffix w. This is exactly decidable by partition refinement -- there is
no sampling and no scope caveat in the state count, only in how wide a sweep
of (b, a) is run.

HAND-ATTACK, done on paper before this file was written. A tail of length m
takes every integer value in [-T_m, T_m] with T_m = a(b^m - 1)/(b-1), the
interval being full because 2a+1 >= b (the covering condition every system
below satisfies, controls included). Reading a tail after a prefix of value v
lands at v*b^m + t. So v can be driven to output 0 by some tail iff
|v|*b^m <= T_m for some m, i.e. iff |v| <= (a/(b-1))*(1 - b^-m) for some m.
As m grows the bound climbs to a/(b-1) but never reaches it. Hence:
  - if (b-1) does not divide a, every |v| <= floor(a/(b-1)) is strictly below
    a/(b-1) and is driven to 0 at large enough m, so no non-absorbing state
    can merge with an absorbing one;
  - if (b-1) divides a, the states v = +-a/(b-1) sit AT the bound, are never
    driven to 0, and every tail leaves their sign intact -- so each is
    output-equivalent to the absorbing state of its own sign and the pair
    merges away.
Both branches give the same closed form, 2*ceil(a/(b-1)) + 1, which is the
prediction below. The two branches are the reason the sweep must contain
cells on both sides of the divisibility: a sweep landing only on
(b-1) | a cells would confirm the formula while testing one branch.

PREDICTIONS, fixed here and weighed only after the run.
  P1 The minimal state count is 2*ceil(a/(b-1)) + 1 at every system swept.
  P2 It is strictly below the shipped 2K+3 exactly at the cells where
     (b-1) divides a, and equal to it elsewhere.
  P3 The merged states, where a merge happens, are exactly +-a/(b-1).
  P4 The minimal count therefore separates the redundant systems from the
     non-redundant controls no better than the shipped count did -- the
     controls (3,1) and (5,2) have a/(b-1) = 1/2, so ceil = 1 and the count
     is 3, which redundant (5,3) also carries. F4's verdict that the count
     CUTS ACROSS the redundancy boundary survives minimization.

KILLS, named as things this file PRINTS, not as what they would mean.
  K1 Any swept cell whose printed minimal count differs from
     2*ceil(a/(b-1)) + 1 kills P1, and the closed form with it.
  K2 A merge at a cell with (b-1) not dividing a, or no merge at a cell
     where it does, kills P2.
  K3 A merged pair other than +-a/(b-1) kills P3.
  K4 Any disagreement between the minimized automaton and brute-force sign
     kills the run itself, not a prediction -- see the controls.

CONTROLS, run and read BEFORE any count is weighed.
  C1 EXACTNESS. The minimized automaton is replayed against brute-force
     sign on every digit string up to the widest width the budget allows.
     A minimizer that merges too eagerly shows up here as a disagreement.
  C2 PADDING. A deliberately inflated automaton -- the same machine with
     every state duplicated -- is minimized and must come back to the SAME
     count as the unpadded one. A minimizer that merges too timidly returns
     the inflated count and is caught here. C1 and C2 fail in opposite
     directions, which is why both are run.
  C3 The non-redundant controls (3,1) and (5,2) are swept alongside, as in
     the rig this question comes from, so the count is read against the
     redundancy boundary rather than only within it.
  C5 THE CLAMP IS NOT THE COUNT. The whole finding here is that the earlier
     rig's state count was an artifact of where IT clamped, so this file
     owes the same check against itself. The machine is rebuilt with the
     clamp pushed out by 3 states on each side -- which can only ADD states
     the minimizer must then merge away -- and the minimal count must not
     move. This is the control that makes the count a fact about sign
     rather than about a builder's constant, and it is strictly stronger
     than C1 for that purpose: C1 can only see a clamp error that changes
     the LANGUAGE, while a clamp that truncates states the minimizer would
     have merged anyway changes no string's sign at all.

SCOPE. The sweep runs b = 2..12 and a = 1..12 restricted to covering sets
(2a+1 >= b), which is every system the corpus's redundant reading admits
plus the balanced non-redundant controls at 2a+1 = b. Both divisibility
branches are populated by construction. Memory is a few thousand integer
states; runtime is seconds.

RUN RECORD: one run, 107 cells (b = 2..12, a = 1..12, covering), plus the
nine recorded systems under the controls. 2 s, well under the analysis
ceiling. All three kills missed; C1, C2 and C5 clean.

FINDINGS.

F1 THE MINIMAL STATE COUNT IS 2*ceil(a/(b-1)) + 1, AND THE ROUNDING IS THE
   CEILING (theorem for symmetric contiguous covering sets, proof in the
   hand-attack above; verified exhaustively at all 107 swept cells, K1 = 0).
   The proof is complete and general over the family, not a fit to the
   sweep: tails of length m fill [-T_m, T_m] exactly because 2a+1 >= b, so
   a state is distinguishable from an absorbing one iff it can be driven to
   value 0, which happens iff |v| < a/(b-1) strictly. Every remaining pair
   is separated by the tail that zeroes one of them. REACHABILITY is the
   step this rests on and it is one line HERE: every state v with
   |v| <= K is reached by the single digit v, because K = floor(a/(b-1))
   <= a for b >= 2, so the digit v is in the set. Without that step the
   formula would be an upper bound rather than the count, which is the
   whole distinction this file is about. The sweep's role is to
   populate both divisibility branches and to catch an error in the
   argument, and it found none. C5 is what rules out the reading this file
   levels at its predecessor -- widening the clamp by 3 on each side moves
   the minimal count at ZERO cells of either grid, so the count is a fact
   about sign and not about a builder's constant.

   A note on what the controls can and cannot see, measured rather than
   asserted. Deliberately clamping one state early and re-running catches
   at 128 of 288 eligible cells, under C1 and under C5 alike, and the two
   agree cell for cell. That is not weakness: at the other 160 the early
   clamp is not an error at all, because the state it removes is one the
   minimizer merges into the absorbing class anyway -- which is the surplus
   phenomenon F2 is about, seen from the other side. An injected fault that
   the object itself makes harmless is not a missed detection.

F2 SO THE SHIPPED COUNT WAS NOT MINIMAL, AT 34 OF THE 107 CELLS -- exactly
   the cells where (b-1) divides a, K2 = 0, and the merged pair is exactly
   +-a/(b-1) at every one of them, K3 = 0. On the nine systems the
   order-wall rig printed, the count falls at five of the seven redundant
   ones -- (2,1), (3,2), (4,3) from 5 to 3, (2,2) from 7 to 5, (2,3) from
   9 to 7 -- while (5,3) and (3,3) were already minimal. That is the same
   five-of-seven split that rig derived from the divisibility, reached here
   by minimizing rather than by deriving, which is what makes it a check on
   both files rather than a restatement of one.

F3 THE SEAM SHARPENS, AND FURTHER THAN "TWO ROUNDING MODES". The open
   reading was that sign's floor and addition's ceiling might be two
   roundings of one normalized reach. They are not two: both are the
   CEILING. Addition's criterion spends ceil(x/(b-1)) slack units on a side
   of reach x; sign's minimal automaton spends ceil(a/(b-1)) states per
   side, plus the one state that is the all-zeros class. The floor was an
   artifact of where the earlier rig chose to clamp -- an implementation
   constant -- and never a fact about sign. So the two costs are ONE
   function of the normalized reach read at two arguments, and F4 of
   explore_order_wall_shape.py ("sign's state answers to a/(b-1), which
   appears in neither of addition's parameters") is corrected in its
   attribution while its point survives intact: the shared object is the
   reach a/(b-1), and it is rho -- the redundancy dial -- that carries
   neither cost. The bundled-faculties reading stands; what it is bundled
   ON is now named.

F4 AND THE MINIMAL AUTOMATON MEETS THE LEADING-NONZERO LAW EXACTLY.
   The count is 3 precisely at a <= b-1 (equivalently ceil(a/(b-1)) = 1),
   which is verbatim the regime where the corpus states the sign as "the
   first nonzero digit's" -- and 3 states is that law's own machine: seen
   only zeros, negative, positive. explore_order_wall_shape.py records that
   the MONOID does not shrink to meet the law (10, 8, 8, 3 below the line)
   and reads that as the law's product not being needed rather than
   collapsing. THAT READING DOES NOT SURVIVE ITS OWN OBJECT BEING
   MINIMIZED, and the correction is this file's shape applied one level up:
   those are the CLAMPED machine's maps, and the SYNTACTIC monoid is 3 at
   every cell below the line (explore_sign_monoid.py). So the law is not a
   shortcut past the product either -- below the line the three-state
   machine IS the whole algebra, and the wide monoid was the surplus pair
   F2 is about, counted in the other currency.

F5 P4 SURVIVES MINIMIZATION: the count still cuts across the redundancy
   boundary rather than marking it. Both non-redundant controls print 3,
   and so do redundant (5,3), (4,2), (6,3), (7,5) and every other cell with
   a <= b-1. Minimizing sharpened the formula without making it a
   redundancy detector, which is the verdict the earlier rig reached with
   the looser count.

SCOPE, and it is the front this leaves. Every system here is a SYMMETRIC
contiguous set {-a..a}. Addition's law needed ASYMMETRIC sets to expose its
endpoint clause -- the clause is invisible to symmetric sweeps -- so the
per-side reading in F3 is tested on exactly the half of the grid that
cannot see an endpoint effect. Whether sign's minimal count over
{-a^-..a^+} is ceil(a^-/(b-1)) + ceil(a^+/(b-1)) + 1, and whether it
carries an endpoint exception of its own, is untested and is the cheap next
probe: the same minimizer, an asymmetric build.

================================================================
PART II -- THE ASYMMETRIC SETS. Slate frozen before the engine below was
written, findings entered only after it ran.

THE QUESTION. Part I's per-side reading -- sign spends ceil(a/(b-1)) states
per side -- was measured on symmetric sets alone, where the two sides are
equal by construction and a per-side law is indistinguishable from a law
about the single number a. Over D = {-a^-..a^+} the two sides come apart
and the reading becomes falsifiable. It matters because ADDITION's law over
exactly these sets carries an ENDPOINT EXCEPTION invisible to symmetric
sweeps: c = 1 iff rho >= 2 AND b >= 3 AND D is not a rho = 2 set with an
endpoint at 1, the endpoint clause arising because a side of reach 1 spends
a full slack unit while a side of reach 0 spends none. If sign's cost is
genuinely the same object, the natural question is whether it inherits that
exception or not.

HAND-ATTACK, on paper before the engine. The clamp is no longer symmetric.
A tail of length m now fills [-T_m^-, T_m^+] with T_m^± = a^±(b^m - 1)/(b-1),
the interval still being a full run of integers provided a^- + a^+ + 1 >= b
-- the covering condition, which is what bridges consecutive multiples of b
in the induction, and it is NOT 2a+1 >= b transcribed. A prefix of value v
is driven to 0 by some tail iff v*b^m lands inside that interval for some m:
for v > 0 that needs v*b^m <= T_m^-, i.e. v < a^-/(b-1); for v < 0 it needs
|v|*b^m <= T_m^+, i.e. |v| < a^+/(b-1). SO THE SIDES CROSS -- a POSITIVE
prefix is killed by the NEGATIVE reach, because it is a negative tail that
must pull it back to zero. The count is then
ceil(a^-/(b-1)) + ceil(a^+/(b-1)) + 1 with the two ceilings attached to the
OPPOSITE sides from the naive reading, which coincides with Part I's formula
on symmetric sets and is why symmetric sweeps cannot see the attachment.
This is a TRANSPLANT from Part I and is flagged as one: the per-side
intuition was formed where the sides are equal.

PREDICTIONS, fixed here.
  Q1 The minimal count is ceil(a^-/(b-1)) + ceil(a^+/(b-1)) + 1 at every
     covering asymmetric cell swept.
  Q2 It reduces to Part I's 2*ceil(a/(b-1)) + 1 at a^- == a^+.
  Q3 There is NO endpoint exception: no cell's count departs from Q1 on
     account of a reach of 1 or 0. Addition's exception comes from slack
     units being a shared budget that an endpoint rounds up out of; sign's
     states are counted per side and never share, so the mechanism that
     produces addition's clause has nothing to act on here.
  Q4 The surviving states are exactly the integers v with
     -a^+/(b-1) < v < a^-/(b-1), the crossed form -- so at a^- = 0 (digits
     {0..a^+}, unsigned) only v = 0 survives and the count is 2.

KILLS, as things this file PRINTS.
  L1 Any covering cell whose printed count differs from Q1 kills the
     crossed form.
  L2 A count matching the UNCROSSED form ceil(a^+/(b-1)) + ceil(a^-/(b-1))
     attached the other way at a cell where the two differ would also
     print as L1; the crossed and uncrossed forms are the same SUM, so the
     sum cannot separate them. The separator is the printed surviving-state
     interval, Q4 -- which is why the state list is printed and not just
     the count.
  L3 Any cell whose surviving interval is not the crossed one kills Q4
     independently of the count.

CONTROLS. C1 and C2 as in Part I -- exact replay against brute force, and
padding minimizing back -- run over the asymmetric grid before any count is
weighed. The symmetric diagonal is included in the sweep as C4, where the
answer is already known from Part I: a disagreement there is a bug in the
asymmetric build rather than a finding.

SCOPE. b = 2..9, a^- and a^+ = 0..8 restricted to covering sets with at
least one of the two nonzero. Both the a^- = 0 unsigned edge and the
reach-1 cells addition's exception lives on are inside the grid by
construction.

RUN RECORD: 528 covering cells (b = 2..9, reaches 0..8), all 528 replayed
against brute force and all 528 padded-and-reminimized, 0 control failures
after the build fix recorded in G0. Under 30 s. Split 456 signed cells
(both reaches >= 1) and 72 unsigned-edge cells (one reach 0).

FINDINGS.

G0 THE CONTROL EARNED ITS KEEP, AND THE BUG IT CAUGHT IS THE FINDING'S OWN
   SHAPE. The first build clamped the positive side at floor(ap/(b-1)) and
   the negative at floor(am/(b-1)) -- the NAIVE attachment, each side
   clamped by its own reach. C1 fired at 184 of 528 cells. The hand-attack
   above had already derived the opposite and the builder was written
   against it anyway, which is the transplant it flagged: the per-side
   intuition was formed on symmetric sets, where the two attachments are
   indistinguishable. A run without C1 would have printed counts from a
   wrong machine, and no count-vs-formula comparison would have caught it,
   because both the machine and the formula would have been wrong the same
   way.

G1 THE REACHES CROSS, AND THAT IS THE CONTENT (rule, exhaustive over the
   456 signed cells; L3 = 0 there). A prefix of value v > 0 survives as a
   distinguishable state exactly while v < am/(b-1) -- the NEGATIVE reach --
   because only a negative tail can pull it back to zero; a prefix v < 0
   answers to ap the same way. The printed survivor set is that crossed
   interval at every signed cell, which is what separates the crossed form
   from the uncrossed one: the two give the SAME SUM and so the same count,
   and only the state list tells them apart. That is why L2 was written as
   a non-separator rather than a kill.

G2 THE COUNT IS ceil(am/(b-1)) + ceil(ap/(b-1)) + 1 (RULE, exhaustive over
   the 456 signed cells; L1 = 0 there) -- and the tier is a rule rather
   than a theorem for one identified reason, which is worth naming because
   the symmetric half IS a theorem. The distinguishing argument carries
   over unchanged; REACHABILITY does not. Symmetric sets reach every state
   by a single digit, since the top state floor(a/(b-1)) never exceeds a.
   Asymmetric ones need not: at b = 2 with reaches (8, 1) the top state is
   8 while the largest digit is 1, so it is reached only through a chain,
   and the sweep confirms it is reached without proving it must be. An
   unreachable state would make the formula an upper bound instead of the
   count. So the closed form is verified over the grid and derived except
   at that step. (Settled: explore_sign_sparse.py G3 proves the step by
   descent -- an integer of the interval beyond the digits, stepped by the
   largest same-residue digit, stays on its side and strictly decreases
   into the digits -- so the count is a theorem over signed contiguous
   covering sets.) Reducing to Part I's
   2*ceil(a/(b-1)) + 1 on the symmetric diagonal at every cell of it
   (C4 = 0). So Part I's per-side reading survives the only sweep that
   could have broken it, and F3's weld holds in the general form: addition
   spends ceil(x/(b-1)) slack units per side, sign spends ceil(x/(b-1))
   states per side, plus one. The SIDES the two attach to differ -- sign's
   cross, addition's do not -- which is a genuine asymmetry between the two
   costs and does not disturb the shared ceiling.

G3 SIGN HAS NO ENDPOINT EXCEPTION (rule, over the swept grid). Addition's
   law carries one: a rho = 2 set with an endpoint at 1 loses its c = 1
   grant, because slack is a SHARED budget and a reach-1 side rounds a full
   unit out of it. Sign's states are counted per side and never share, so
   the mechanism has nothing to act on -- and the grid agrees: of the 156
   cells with a reach of 0 or 1, every cell with min reach exactly 1 matches
   the formula, and the 56 departures are all min reach ZERO. Q3 predicted
   this and named that mechanism in advance.

G4 THE UNSIGNED EDGE IS A DIFFERENT REGIME, NOT A COUNTEREXAMPLE, AND Q1
   WAS WRONG TO CLAIM IT. Q1 was frozen as "every covering asymmetric cell"
   and the edge kills it as stated: at am = 0 the digits are {0..ap}, no
   value is ever negative, and the minimal machine has TWO states -- the
   all-zeros class and one absorbing state -- whatever ap is, against a
   formula predicting ceil(ap/(b-1)) + 1. The mechanism is that the crossed
   rule reads the OTHER side's reach, so at reach 0 no positive state can
   ever be driven back to zero and all of them collapse, while NEG is
   unreachable and the second absorbing state does not exist. The 16 edge
   cells that do match match coincidentally, at ap <= b-1 where the formula
   also returns 2. This is a scope correction to a prediction, recorded as
   a miss rather than folded into the claim: the closed form is a law about
   SIGNED sets, both reaches >= 1, and the edge is the unsigned numeration
   where "sign" has one nontrivial value and the question degenerates.
"""

import sys

# The nine systems the order-wall rig swept, kept so the counts here can be
# read directly against the ones it printed. The first seven are redundant
# (2a+1 > b), the last two the balanced non-redundant controls (2a+1 == b).
RECORDED = [(2, 1), (3, 2), (4, 3), (5, 3), (2, 2), (2, 3), (3, 3)]
CONTROLS = [(3, 1), (5, 2)]

BRUTE_BUDGET = 200_000  # digit strings enumerated per cell in control C1


def value(digits, b):
    """Exact value of an MSB-first digit string."""
    v = 0
    for d in digits:
        v = v * b + d
    return v


def sgn(x):
    return (x > 0) - (x < 0)


def build(b, a):
    """The shipped clamped automaton, on 2K+3 states, K = floor(a/(b-1)).

    States are the integers -K..K plus two absorbing states named by their
    sign. Returns (states, delta, out, start) with delta[state][digit].
    """
    K = a // (b - 1)
    NEG, POS = ("NEG", "POS")
    states = list(range(-K, K + 1)) + [NEG, POS]
    digits = list(range(-a, a + 1))

    def step(s, d):
        if s in (NEG, POS):
            return s
        v = b * s + d
        if v > K:
            return POS
        if v < -K:
            return NEG
        return v

    delta = {s: {d: step(s, d) for d in digits} for s in states}
    out = {s: (-1 if s == NEG else 1 if s == POS else sgn(s)) for s in states}
    return states, delta, out, 0


def pad(states, delta, out, start):
    """C2's inflated machine: every state duplicated into a twin with the
    same output, transitions alternating between the two copies. Same
    language-with-output, exactly twice the states."""
    new_states = [(s, i) for s in states for i in (0, 1)]
    new_delta = {}
    for s in states:
        for i in (0, 1):
            new_delta[(s, i)] = {d: (t, 1 - i) for d, t in delta[s].items()}
    new_out = {(s, i): out[s] for s in states for i in (0, 1)}
    return new_states, new_delta, new_out, (start, 0)


def reachable(states, delta, start):
    seen, stack = {start}, [start]
    while stack:
        s = stack.pop()
        for t in delta[s].values():
            if t not in seen:
                seen.add(t)
                stack.append(t)
    return seen


def minimize(states, delta, out, start):
    """Moore-machine minimization by partition refinement over the reachable
    part. Returns (count, classes) with classes a dict state -> block id."""
    live = reachable(states, delta, start)
    block = {s: out[s] for s in live}
    while True:
        signature = {s: (block[s], tuple(block[delta[s][d]]
                                         for d in sorted(delta[s])))
                     for s in live}
        order = {}
        for s in sorted(live, key=lambda x: str(x)):
            order.setdefault(signature[s], len(order))
        new = {s: order[signature[s]] for s in live}
        if len(set(new.values())) == len(set(block.values())):
            return len(set(new.values())), new
        block = new


def max_width(b, a, budget=BRUTE_BUDGET):
    n, size = 0, 1
    while size * (2 * a + 1) <= budget:
        size *= 2 * a + 1
        n += 1
    return n


def replay(b, digits, delta, out, start, width):
    """C1: the minimized machine against brute-force sign on every string.

    `digits` is the explicit digit set, so the same control serves the
    symmetric and asymmetric builds -- deriving it from a single reach was
    a harness bug the asymmetric control caught.
    """
    bad = 0
    stack = [(start, [])]
    while stack:
        s, pre = stack.pop()
        if len(pre) == width:
            if out[s] != sgn(value(pre, b)):
                bad += 1
            continue
        for d in digits:
            stack.append((delta[s][d], pre + [d]))
    return bad


def ceil_div(x, y):
    return -((-x) // y)


def sweep():
    cells = []
    for b in range(2, 13):
        for a in range(1, 13):
            if 2 * a + 1 >= b:  # covering; the hand-attack needs it
                cells.append((b, a))
    return cells


def build_margin(b, am, ap, margin=0):
    """The clamped automaton over D = {-am..ap}, am/ap the two reaches, with
    the clamp pushed OUT by `margin` extra states on each side.

    THE THRESHOLDS CROSS, which is the hand-attack's point and which this
    builder got backwards on its first write -- control C1 caught it at 184
    of 528 cells. A POSITIVE prefix is overturned only by a NEGATIVE tail,
    whose reach is am, so it survives while v < am/(b-1); a negative prefix
    answers to ap the same way.

    `margin` exists for control C5. The whole finding is that the earlier
    rig's count was an artifact of where IT clamped, so this file owes a
    check that its own count is not. Widening the clamp can only ADD states
    the minimizer must then merge away; if the minimal count is unchanged,
    nothing was being truncated.
    """
    Kp, Km = am // (b - 1) + margin, ap // (b - 1) + margin
    NEG, POS = ("NEG", "POS")
    states = list(range(-Km, Kp + 1)) + [NEG, POS]
    digits = list(range(-am, ap + 1))

    def step(s, d):
        if s in (NEG, POS):
            return s
        v = b * s + d
        if v > Kp:
            return POS
        if v < -Km:
            return NEG
        return v

    delta = {s: {d: step(s, d) for d in digits} for s in states}
    out = {s: (-1 if s == NEG else 1 if s == POS else sgn(s)) for s in states}
    return states, delta, out, 0


def build_asym(b, am, ap):
    """The asymmetric build at the tight clamp -- see build_margin."""
    return build_margin(b, am, ap, 0)


def asym_cells():
    cells = []
    for b in range(2, 10):
        for am in range(0, 9):
            for ap in range(0, 9):
                if am + ap + 1 >= b and (am or ap):
                    cells.append((b, am, ap))
    return cells


def part_two():
    print()
    print("=" * 64)
    print("PART II -- ASYMMETRIC SETS: do the two reaches CROSS?")
    print()

    cells = asym_cells()

    # ---- controls, before any count is weighed ----
    c_fail = 0
    checked = 0
    for (b, am, ap) in cells:
        st, dl, ou, s0 = build_asym(b, am, ap)
        n_min, cls = minimize(st, dl, ou, s0)
        pst, pdl, pou, ps0 = pad(st, dl, ou, s0)
        n_pad, _ = minimize(pst, pdl, pou, ps0)
        if n_pad != n_min:
            c_fail += 1
        # replay only where the string budget allows a useful width
        w = 0
        size = 1
        while size * (am + ap + 1) <= 60_000:
            size *= (am + ap + 1)
            w += 1
        if w >= 3:
            mdelta, mout = {}, {}
            for s in cls:
                mdelta.setdefault(cls[s], {})
                for d, t in dl[s].items():
                    mdelta[cls[s]][d] = cls[t]
                mout[cls[s]] = ou[s]
            if replay(b, list(range(-am, ap + 1)), mdelta, mout, cls[s0], w):
                c_fail += 1
            checked += 1
    # C5 -- the clamp is not the count. Widening it by 3 on each side can
    # only add states; if the minimal count never moves, nothing was cut.
    c5_diff = 0
    for (b, am, ap) in cells:
        n_tight, _ = minimize(*build_margin(b, am, ap, 0))
        n_wide, _ = minimize(*build_margin(b, am, ap, 3))
        if n_tight != n_wide:
            c5_diff += 1
    print(f"C1/C2: {len(cells)} covering cells, {checked} replayed against "
          f"brute force, {c_fail} failures.")
    print(f"C5   : clamp widened by 3, {c5_diff} cells where the minimal "
          f"count moved.")
    c_fail += c5_diff
    if c_fail:
        print("CONTROLS FAILED -- counts not weighed.")
        return 1
    print("Controls clean. Weighing.")
    print()

    # ---- the sweep ----
    l1 = l3 = 0
    l1_signed = l3_signed = 0   # the same two kills over am, ap >= 1 only
    n_signed = n_edge = 0
    diag_bad = 0
    endpoint_rows = []
    for (b, am, ap) in cells:
        signed = (am >= 1 and ap >= 1)
        if signed:
            n_signed += 1
        else:
            n_edge += 1
        st, dl, ou, s0 = build_asym(b, am, ap)
        n_min, cls = minimize(st, dl, ou, s0)
        pred = ceil_div(am, b - 1) + ceil_div(ap, b - 1) + 1
        if n_min != pred:
            l1 += 1
            if signed:
                l1_signed += 1
        # surviving (non-absorbing, unmerged) states, and the crossed
        # interval Q4 predicts: -ap/(b-1) < v < am/(b-1)
        # An absorbing state can be UNREACHABLE -- at am = 0 the digits are
        # unsigned and no negative value ever occurs -- so guard the lookup
        # rather than assuming both are present.
        absorbing = [cls[t] for t in ("NEG", "POS") if t in cls]
        survivors = sorted(s for s in cls
                           if isinstance(s, int) and cls[s] not in absorbing)
        # v = 0 always survives -- the EMPTY tail already reports output 0,
        # which no absorbing state does. Above it the crossed rule applies,
        # and it is restricted to states the build can actually reach: at
        # am = 0 there is no negative value anywhere in the system.
        want = [v for v in range(-Kbound(b, ap), Kbound(b, am) + 1)
                if v == 0
                or (v > 0 and v * (b - 1) < am and am > 0)
                or (v < 0 and -v * (b - 1) < ap and ap > 0)]
        want = [v for v in want
                if (v <= 0 or am > 0) and (v >= 0 or ap > 0)]
        if survivors != want:
            l3 += 1
            if signed:
                l3_signed += 1
            if l3_signed <= 6 and signed:
                print(f"  L3 at (b={b}, -{am}..{ap}): survivors {survivors} "
                      f"vs crossed {want}")
        if am == ap and n_min != 2 * ceil_div(am, b - 1) + 1:
            diag_bad += 1
        if min(am, ap) <= 1:
            endpoint_rows.append((b, am, ap, n_min, pred))

    print(f"{'cells':>8} {len(cells):>6}")
    print(f"  signed cells (am,ap >= 1): {n_signed}   unsigned edge: {n_edge}")
    print(f"L1 count != ceil(am/(b-1))+ceil(ap/(b-1))+1 : {l1} cells"
          f"  ({l1_signed} of them signed)")
    print(f"L3 survivors not the CROSSED interval       : {l3} cells"
          f"  ({l3_signed} of them signed)")
    print(f"C4 symmetric diagonal vs Part I             : {diag_bad} cells")
    print()
    print("Q3 -- the endpoint cells (min reach 0 or 1), count vs formula:")
    bad_ep = [r for r in endpoint_rows if r[3] != r[4]]
    print(f"  {len(endpoint_rows)} such cells, {len(bad_ep)} departing "
          f"from the formula.")
    for r in endpoint_rows[:8]:
        print(f"   b={r[0]} D=[-{r[1]}..{r[2]}] min={r[3]} formula={r[4]}")
    return 0


def Kbound(b, reach):
    return reach // (b - 1)


def main():
    print("SIGN'S MINIMAL AUTOMATON -- is 2K+3 minimal, and which rounding?")
    print()

    # ---- controls first, before any count is weighed ----
    print("C1/C2 CONTROLS on the nine recorded systems")
    print(f"{'(b,a)':>8} {'shipped':>8} {'minimal':>8} {'padded->':>9} "
          f"{'width':>6} {'disagree':>9}")
    c_fail = 0
    for (b, a) in RECORDED + CONTROLS:
        st, dl, ou, s0 = build(b, a)
        n_ship = len(st)
        n_min, cls = minimize(st, dl, ou, s0)
        pst, pdl, pou, ps0 = pad(st, dl, ou, s0)
        n_pad, _ = minimize(pst, pdl, pou, ps0)
        # rebuild the minimized machine explicitly, then replay it
        mdelta, mout = {}, {}
        for s in cls:
            mdelta.setdefault(cls[s], {})
            for d, t in dl[s].items():
                mdelta[cls[s]][d] = cls[t]
            mout[cls[s]] = ou[s]
        w = max_width(b, a)
        bad = replay(b, list(range(-a, a + 1)), mdelta, mout, cls[s0], w)
        if bad or n_pad != n_min:
            c_fail += 1
        print(f"{str((b,a)):>8} {n_ship:>8} {n_min:>8} {n_pad:>9} "
              f"{w:>6} {bad:>9}")
    print()
    if c_fail:
        print(f"CONTROLS FAILED at {c_fail} cells -- K4. Counts not weighed.")
        return 1
    c5 = sum(1 for (b, a) in sweep()
             if minimize(*build_margin(b, a, a, 0))[0]
             != minimize(*build_margin(b, a, a, 3))[0])
    print(f"C5   : clamp widened by 3 over the sweep, {c5} cells where the "
          f"minimal count moved.")
    if c5:
        print("C5 FAILED -- the count is an artifact of the clamp.")
        return 1
    print("Controls clean: replay exact, padding minimizes back, clamp "
          "irrelevant. Weighing.")
    print()

    # ---- the sweep ----
    print("THE SWEEP -- minimal count against both roundings")
    print(f"{'(b,a)':>8} {'a/(b-1)':>9} {'floor':>6} {'ceil':>5} "
          f"{'2K+3':>6} {'min':>5} {'2ceil+1':>8} {'div':>4} {'merged':>16}")
    k1 = k2 = k3 = 0
    n_cells = n_div = 0
    for (b, a) in sweep():
        n_cells += 1
        st, dl, ou, s0 = build(b, a)
        n_min, cls = minimize(st, dl, ou, s0)
        K = a // (b - 1)
        C = ceil_div(a, b - 1)
        divides = (a % (b - 1) == 0)
        n_div += 1 if divides else 0
        pred = 2 * C + 1
        # which non-absorbing states share a block with an absorbing one
        merged = sorted(s for s in cls
                        if isinstance(s, int)
                        and any(cls[t] == cls[s] for t in ("NEG", "POS")))
        if n_min != pred:
            k1 += 1
        if bool(merged) != divides:
            k2 += 1
        if merged and merged != sorted({-K, K}):
            k3 += 1
        print(f"{str((b,a)):>8} {a/(b-1):>9.3f} {K:>6} {C:>5} "
              f"{len(st):>6} {n_min:>5} {pred:>8} "
              f"{'yes' if divides else 'no':>4} {str(merged):>16}")
    print()
    # Printed as labelled scalars rather than left to be counted off the
    # table below, where the header line is row-shaped and miscounts.
    print(f"cells swept                   : {n_cells}")
    print(f"of them with (b-1) | a        : {n_div}")
    print(f"K1 count != 2*ceil(a/(b-1))+1 : {k1} cells")
    print(f"K2 merge/divisibility mismatch: {k2} cells")
    print(f"K3 merged pair not +-a/(b-1)  : {k3} cells")
    return part_two()


if __name__ == "__main__":
    sys.exit(main())
