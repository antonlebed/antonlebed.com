"""What plays the PERIOD at a window that has none: the repair
cascade's SPAN, and whether the verdict reads the large caps'
POSITIONS or their VALUES.

THE QUESTION
------------
At a trailing Ostrowski window alpha = [0; a_1, a_2, ...] the stride-r
shift's verdict is settled at every window whose large quotients sit
on ONE residue class mod P: it is the parity of r mod P, with no
dependence on the large quotient's size (explore_shift_repair.py F4,
F8). The cubic cbrt(2) - 1 has no such class -- its quotients above 1
sit at positions 0, 2, 5, 8, 10, 12, 13, 15, 16, 17, 18, 19, 21, 22 --
so that law has no subject there, and its measured table (strides
1, 3, 5 gated, 2, 4, 6, 7, 8 bounded) is the whole evidence. This rig
asks what quantity reduces to parity of r mod P where a period exists
and calls the cubic where none does.

THE HAND-ATTACK (pre-engine, on paper; one candidate DIES here and
owes no engine, and its death is what the design below is built on).

THE GAP-PARITY CANDIDATE. The law's mechanism reading is that the
down-borrow spans TWO positions (q_{p+1} - q_{p-1}), so the repair
walks the digit lattice in steps of 2, and the verdict is whether it
can return to the positions carrying the large caps. Written as a
function of the large-cap SET rather than of a period that: a drop at
site j lands at p = j + r, and the walk in steps of 2 reaches the
nearest large-cap position at or below p exactly when the GAP
    g(j, r) = p - max{s <= p : a_{s+1} >= 2}
is EVEN. At a one-residue-class window the large-cap positions below p
are j, j - P, j - 2P, ..., so the nearest one is at distance
r mod P and the criterion IS F4 -- parity of r mod P, independent of
the cap's value, for every P and every A at once. That is the wanted
generalization, derived and not fitted, and it is a statement about a
SET with no period in it.

It is DEAD AT THE CUBIC, and no quantifier saves it. Computed from the
certified quotient sequence over the drop sites below position 40,
every stride carries BOTH gap parities:
    r = 1: 12 odd of 17 drops     r = 5:  5 of 17
    r = 2:  6 of 15               r = 6:  5 of 14
    r = 3:  4 of 15               r = 7:  8 of 17
    r = 4: 10 of 13               r = 8:  6 of 12
The measured split is gated {1, 3, 5} against bounded {2, 4, 6, 7, 8}.
An EXISTENTIAL over drop sites calls all eight gated; a UNIVERSAL
calls none; and no monotone count in between separates them either --
the stride carrying the FEWEST odd gaps is a GATED one and the second
most sits at a BOUNDED stride, and that holds at the rig's own drop
cutoff (E2's columns) as well as at the cutoff above, which are
different counts of the same refutation. So the first large-cap
position below the landing
is not where the cascade ends, and the missing quantity is not a
function of the large-cap positions alone.

WHAT THE DEATH POINTS AT. Two walk readings are available on paper and
each is refuted by the family the other fits. STOP-AT-THE-FIRST-
ABSORBER is gap parity: correct at every designed window, dead at the
cubic. PASS-THROUGH -- the walk crosses a large-cap position it did
not land on and continues to the next -- is dead at the designed
family instead: there the large-cap positions below the landing sit at
distances r, r + P, r + 2P, ..., so at odd P one of the first two
distances is always even and no stride could ever gate, where F4 says
half of them do. The truth is therefore neither, and what separates
the two families is not their positions but their VALUES: the designed
family's absorbers all carry one cap A and its transparent positions
all carry 1, so every drop is large-onto-1, while the cubic's caps
take eight distinct values among its first fourteen large positions
and its drop sites include LARGE-ONTO-LARGE ones (cap 14 landing on
cap 3) that no designed window has ever contained. A
criterion reading positions alone cannot see that difference, which is
exactly the difference the cubic has.

So this rig does two things. It MEASURES the cascade instead of
guessing it -- the span of a repair, which is the observable the whole
question is about and which no rig in this thread has printed -- and
it builds a periodic family that CONTAINS the cubic's distinguishing
structure, where a verdict can still be read against a known law.

THE VOCABULARY (fixed before any engine; the first three are
per-input, the rest are per-cell).
  REACH. The lowest position at which the repaired legal string
  differs from the bare shifted string. (The parent rig's `lowest` is
  the minimum of this over inputs.)
  TOP. The highest position at which they differ.
  SPAN. TOP - REACH: how far one repair event carries.
  FLOOR PROFILE. The minimum REACH over the repairs whose TOP is at
  least h, as h climbs. A cell whose events are all local has a floor
  profile that CLIMBS with h; a cell that carries information from
  the top of the range to the bottom has one that is FLAT.
  LARGE-ONTO-LARGE DROP. A drop site j with a_{j+1} > a_{j+r+1} >= 2
  -- an overflow landing on a position that is itself an absorber.
  Absent from every DESIGNED window in this thread, which carry one
  large value and 1 everywhere else -- and PRESENT at the cubic, which
  is where the difference this rig is chasing lives.

THE SPAN CRITERION (frozen, and it is a criterion about the LATTICE
the events sit on rather than about any one event -- the three dead
candidates before it, absorption depth, tail magnitude and landing
headroom, were all local features of a single overflow). Gating is an
EXISTENTIAL over inputs: c_min(t) unbounded says that for every depth
there are inputs agreeing that deep whose images differ below t. A
repair whose event is LOCAL cannot carry a difference from a high
position to a low one, whatever its size or count. So a cell
  READS AT BOUNDED DELAY when its repairs have bounded SPAN;
  IS GATED when repairs with unbounded TOP hold a fixed REACH floor.

PREDICTIONS, FIXED BEFORE THE RUN (as observables)
  P1 (positive control and cross-rig calibration) reconstruction and
      legality hold over every n < N at every window used; and at the
      cubic and e - 2 the repair counts and the minimum REACH per
      stride reproduce explore_shift_repair.py's recorded rows
      exactly -- cubic 99390/87743/95040/97465 at r = 1..4, e - 2
      99390/99390/0/99390. KILL: any disagreement -- the digit path
      would differ from the parent's and no table here is comparable.
  P2 (the span criterion where the verdict is already known -- eight
      cubic cells, eight at e - 2, and the nine designed windows)
      every GATED cell
      has a FLAT floor profile, and every BOUNDED cell has bounded
      span and a floor profile that climbs. KILL: a bounded cell
      whose span grows with the data cap, or a gated cell whose span
      is bounded -- the span reading would then not be the mechanism
      and this rig's instrument is the wrong one.
  P3 (the graded control -- does the law read positions or values?)
      at the window of period 2P carrying cap A at offset P - 1 and
      cap B at offset 2P - 1 with A != B, the large-cap SET is one
      residue class mod P while the VALUES on it alternate. F4's law
      reads positions, so the verdict must stay the parity of r mod P
      and depend on neither A nor B. KILL: any cell disagreeing --
      F4's measured A-independence would then be an artifact of every
      class member carrying the SAME value, and the law would read
      the values after all.
  P4 (the two-class family -- the cubic's structure inside a periodic
      window) at period P with large caps at two offsets, gap parity
      still predicts a verdict from positions alone, and where a
      stride carries a LARGE-ONTO-LARGE drop the cubic's
      distinguishing structure is present for the first time in a
      window whose verdict is measurable against a known law. Frozen
      as the fork this leg turns on: if gap parity survives every
      cell here, the cubic's failure is NOT about large-onto-large
      drops and the missing quantity is elsewhere; if it fails, the
      failing cells sit in a family with two knobs -- the offsets and
      the two cap values -- and the correction can be READ off them
      rather than fitted. KILL of the FORK: no cell in the family
      carrying a large-onto-large drop at all, which would mean the
      family does not contain what it was built to contain.
  P5 (the value sweep -- what the values DO, if P3's kill fires) at
      P = 3 with the pair (A, B) swept over both orders of several
      magnitudes, the verdict vector is read as a function of the
      pair. Its positive control is exact: A = B is literally F4's
      family, so those rows MUST print F4's parity of r mod 3, and a
      row that does not voids the sweep. Frozen: if the verdict
      depends only on the ORDER of A and B, the two orders print
      mirror tables and equal-order pairs of different magnitudes
      print identically -- the criterion is then a COMPARISON between
      a drop's cap and its absorber's, which is a quantity the cubic
      has and the one-value designed family cannot have. KILL of that
      reading: any dependence on the magnitudes beyond their order.
  P6 (the threshold, if the order reading dies) two readings of a
      value-comparison fit the P = 3 sweep and they are separable by
      construction:
        RATIO      gated iff max(A, B) >  2 min(A, B)
        DIFFERENCE gated iff max(A, B) >= min(A, B) + 3
      They agree on every pair with min = 2 -- which is why the first
      sweep cannot part them -- and disagree at (3, 6), (4, 8),
      (4, 7) and (5, 8), where the ratio reading says bounded and the
      difference reading says gated. RATIO is the favoured one and the
      reason is a precedent rather than a hunch: the absorption lemma
      one storey down (explore_odd_a_freeze.py) has a top charge c
      absorbing a comb extension a top-locally iff 2c = a - 1, a
      factor of two between a charge and the cap that must hold it.
      KILL of RATIO: (3, 6) or (4, 8) gating. KILL of DIFFERENCE:
      (4, 7) or (5, 8) reading bounded.

THE DESIGN
----------
Numeration, digit path and verdict classifier are IMPORTED from
explore_shift_repair.py rather than rewritten, which is what makes P1
a real control: the same greedy descent, the same legality check, the
same three-signal classifier, the same c_min rows from sorted
consecutive pairs. What is new here is the per-repair REACH/TOP/SPAN
record and the two designed families.

EVERY FAMILY CELL IS READ AT SEVERAL RANGES and the verdict rests on
STABILITY, never on one table: a single c_min column does not
determine its own verdict (the parent's lesson, paid for with two full
reruns), and here it must be applied in BOTH directions. A witness
depth that rises with N gates the cell however the column reads inside
one table. And a column UNCHANGED across a tenfold range while the
data cap climbs is bounded however it reads at the top of one --
which matters because the graded windows produce a shape no window in
the parent rig did: a local constant RECURRING with the window's own
period, whose top two depths are served by one witness and which the
single-range classifier's pinned signal therefore reads as unbounded.
The graded family, which carries this rig's headline, is read at
THREE ranges to 300000 for that reason. The span record is printed at
each range for the same reason -- a span that grows with the data cap
is the unbounded cascade and a span that does not is a local event.

WINDOW GENERATOR. `graded(period, caps, want)` takes a period and a
dict {offset: cap} and returns the quotient sequence that is 1
everywhere except a_(k+1) = cap at k = offset mod period. F4's family
is graded(P, {P-1: A}); the graded control is
graded(2P, {P-1: A, 2P-1: B}); the two-class family is
graded(P, {c1: A, c2: B}).

E1  CONTROLS AND CROSS-RIG CALIBRATION. Reconstruction, legality, and
    the cubic and e - 2 stride rows against the parent's recorded
    ones, at the parent's N = 100000. P1's observable.
E2  THE SPAN AT THE CELLS WHOSE VERDICT IS KNOWN. Max span and the
    floor profile per cell, at the cubic, e - 2, and the designed
    family at P = 3, 4, 5 with A = 2, 3, 5 -- read beside the
    measured verdict. P2's observable.
E3  THE TWO DESIGNED FAMILIES. The graded control (P3) and the
    two-class family (P4), each measured verdict beside gap parity's
    prediction, with the large-onto-large drop count printed per
    cell so the fork is readable rather than inferred.
E4  THE VALUE SWEEP. The graded window at P = 3 over both orders of
    several (A, B) pairs, one verdict vector per pair, with the
    A = B rows as the exact positive control. P5's observable.
    Added after E3 printed and reading only P3's kill, which is a
    verdict about POSITIONS and fixes no value law.
E5  THE THRESHOLD. The pairs that part the ratio reading from the
    difference reading, both orders, with two agree-cells beside them
    as controls. P6's observable, and the rule it scores was fixed
    before this experiment was written.

RESOURCE: estimate ~2 min wall, bounded, well under 512MB (digit
tuples, no numpy, no BLAS). Counted rather than guessed: E1/E2 share
one run of 2 windows x 8 strides x 100000 plus 9 designed windows x
~7 strides x 50000, E3 is ~14 windows x ~8 strides x 50000, and the
parent rig's 1.6M extractions in about 12 s sets the rate. The digit
table is rebuilt per window and dropped between them.

RUN RECORD
----------
Wall 205.0 s, peak working set 253.0 MB under a 512 MB ceiling. Six
runs, and the VERDICT CLASSIFIER moved three times before anything
here was recorded -- the same history the parent rig has, for the same
reason, and the verdicts moved under every one of them.
  (1) The first run read each family cell at ONE range, which the
      parent's own lesson forbids. Adding the second range moved cells
      in both families.
  (2) Two ranges are not enough by themselves: the graded windows
      produce a shape the parent's family never did, a LOCAL constant
      recurring with the window's period, whose top two depths are
      served by one witness and which the pinned signal therefore
      called unbounded. Stability was made authoritative in both
      directions.
  (3) That downgrade then over-fired, and the CONTROLS caught it
      twice. A column sitting exactly AT the lookahead ceiling reads
      as an ordinary number, so the stability test called a gated cell
      bounded -- E4's A = B row printed a verdict F4's law forbids.
      And a column with a strictly declining tail is one deep witness,
      not a local event, so the test had to ask whether the column
      RETURNS to 0 above its own nonzeros -- without that, four cells
      of F4's own designed family missed its law.
Three controls hold the final classifier: E4's A = B rows print F4's
parity of r mod 3 at A = 2, 3 and 5; the nine designed windows in E2
miss F4 at zero cells; and the cubic and e - 2 keep the parent rig's
eight verdicts each. All three are green in the recorded run, and the
first two were RED at classifier (3) -- which is what they are for.
E4 was written after E3 printed, reading only P3's kill, which is a
verdict about positions and fixes no value law; E5 after E4, and the
rule it scores was fixed before it was written. Controls: zero
reconstruction failures and zero legality failures at every window
used, at every range, and no image above the built weights anywhere.

FINDINGS (each at its own tier)
-------------------------------
F1  CONTROLS AND CROSS-RIG CALIBRATION (P1 lands). Repairs
    99390/87743/95040/97465 at the cubic r = 1..4 and 99390/99390/
    0/99390 at e - 2, with the cubic gated at r = 1, 3, 5 and e - 2
    at r = 1, 4, 7 -- explore_shift_repair.py's rows exactly, digit
    path and classifier shared. And F4's law is reproduced with zero
    misses at all nine designed windows read here (P = 3, 4, 5 by
    A = 2, 3, 5), which is what makes the families below comparable
    to it.
F2  GAP PARITY IS F4 STATED ON THE LARGE-CAP SET, AND IT IS DEAD AT
    THE CUBIC (property, no engine owed -- the derivation and the
    refutation are both on paper, and the run only scores them).
    Writing g(j, r) for the distance from a drop site's landing down
    to the nearest large-cap position at or below it, EVEN g is the
    step-of-two walk returning to a large cap. At a window whose
    large caps sit on one residue class mod P that distance is
    r mod P for every drop site at once, so gap parity IS F4 --
    every P, every A, no period in the statement. It is the
    generalization the leg was sent for, and it does not survive the
    cubic: every cubic stride carries both parities among its drop
    sites -- the stride with the fewest odd gaps is a GATED one and
    the second most sits at a BOUNDED one -- so no quantifier over
    drop sites separates the measured split. Its existential form misses the
    cubic's five bounded cells and every one of them.
F3  THE SPAN CRITERION IS DEAD, AND IT IS THE FOURTH EXTENT-SHAPED
    CANDIDATE TO DIE (P2's kill fires, both halves). Bounded cells
    have spans that GROW with the data cap -- the cubic's stride 2
    at 10 -> 11, its strides 4, 6, 7, 8 likewise -- while their
    c_min columns are identical across the two ranges at every depth
    both tables reach (the deeper table is longer, not larger); and
    their floor profiles are FLAT, repairs with top at the range's
    ceiling still reaching position 5 at the cubic's bounded stride
    7. So a repair event that spans the whole readable range carries
    no information down it, and the geometric extent of the cascade
    joins absorption depth, tail magnitude and landing headroom.
    What the four have in common is now visible: all of them measure
    the repair, and the verdict is not a property of the repair.
    THE KILL'S FIRST HALF RESTS ON THE CUBIC'S BOUNDED STRIDES BEING
    BOUNDED, and all five hold at a third range (explore_cascade_roof.py
    H1), so it keeps its instances.
F4  THE POSITIONS DO NOT DECIDE (rule at scanned scope; P3's kill
    fires, and its positive control is exact). The cleanest witness
    needs no count at all: (3, 6) and (6, 3) are the SAME window up
    to which value sits on which class member -- identical large-cap
    set, position for position, identical everything a
    position-reading criterion can see -- and they print different
    verdicts at r = 3, gated against bounded. Six of the eleven
    swapped pairs measured differ there, where one would have done.
    ** THE WITNESS AND THE COUNT ARE BOTH TWO-RANGE READINGS and the
    deeper range moves them (explore_cascade_values.py H1): (6, 3)
    gates at 300000, so THIS pair no longer witnesses anything, and
    three of the eleven swapped pairs differ rather than six --
    (4, 8), (5, 8), (4, 9) against their swaps. F4's VERDICT stands
    on those three, and (4, 8) against (8, 4) is the replacement
    witness; the 30-cell count below was read at three ranges
    already and is untouched. **
    The graded control puts a number on it: 5 of its 30 cells miss
    F4's law read on the set,
    four of them the half-period cell r = P and one a genuine
    parity-cell flip (P = 5, caps 2/4, r = 7, even residue and gated).
    ** The flip was the classifier: under the run-length rule the
    misses are 4 of 30 and all four are the half-period cell, r = 7
    at that window reading bounded as the parity law asks
    (explore_cascade_scale.py H2). F4's WITNESS is untouched -- the
    three swapped pairs still differ, 3 of 3. ** The
    control that makes this a measurement rather than an artifact:
    A = B is literally the designed family and prints F4's parity of
    r mod 3 exactly at A = 2, 3 and 5. So the verdict is not a
    function of the large-cap set, the banked candidate shape -- a
    Z/2 invariant of a walk on that set -- cannot be the aperiodic
    quantity, and the cubic's resistance has a named cause: its caps
    take eight distinct values (2, 3, 4, 5, 8, 10, 12, 14) among its
    first fourteen large positions, where every designed window
    before this one carries a single value on all of them.
F5  AND WHAT THE VALUES DO IS CONCENTRATED IN ONE CELL, WHOSE OWN
    LAW IS NEITHER ORDER, NOR RATIO, NOR DIFFERENCE (rule at scanned
    scope over 25 pairs; P5's order reading dies and P6's kills both
    fire). Grading the values leaves F4's law standing at every
    stride but ONE, and it is not every r = 0 mod P -- r = 2P is the
    graded window's true period and reads at delay 0 at every pair.
    It is r = P exactly, the HALF-period shift, the one stride
    carrying each class member onto the OTHER one: the equal family
    has NO REPAIR there and every unequal pair has a large-onto-large
    drop instead, exactly one of the two directions A -> B and
    B -> A being a drop. That cell exists only off the diagonal.
    Its verdict is where the value law lives, and what this rig read
    off 25 pairs at TWO ranges was:
      min(A, B) = 2   -> GATED in both orders, at every A tested
      min(A, B) >= 3  -> GATED unless A exceeds B by 3 or more,
                         the one direction that turns it bounded
    -- A < B gating at all 11 pairs measured and A > B splitting by
    that gap, so the surface is genuinely two-dimensional and not a
    function of the larger value or of the pair's order.
    ** THE FLOOR HALF OF THAT IS SUPERSEDED, and by the range and
    not by the pairs (explore_cascade_values.py H1, H2): six of the
    24 bounded cells here and on the full grid read bounded at 30000
    and 100000 and GATED at 300000, (6, 3) among them, so the
    "exceeds by 3" floor was a two-range reading. The three-range
    law over the whole 8..16 surface is B < A <= 2B + 1 with
    A * B >= 30 -- the roof called at 3 rows of 3, and the min = 2
    wall a consequence of the product rather than a clause. What
    stands here unchanged: the cell is r = P and only r = P, the
    A = B control, and everything below on the second observable. **
    The three frozen readings die against it: ORDER, because (5, 3)
    gates where (6, 3) does not with the order unchanged (both gate
    at three ranges; ORDER dies there instead at (7, 4) against
    (6, 5)). And on the SECOND
    observable -- which of F4's two bounded strides turns gated, if
    either -- RATIO misses 5 of 14 in both directions, silent at
    (4, 8) and (8, 5) which do move a second cell and predicting a
    move at (3, 7), (7, 3) and (9, 4) which do not; DIFFERENCE misses
    9 of 14, predicting a move at twelve pairs where only three have
    one. THREE pairs also move a SECOND cell -- (4, 8) and (4, 9)
    gate r = 5, (8, 5) gates r = 2 -- read here as a small-value fact
    and not a law, which the full grid refutes: six of 64 pairs move
    a second cell, two at min >= 6, and whole rows move r = 2 above
    the grid (explore_cascade_values.py H4).
    ** THERE IS NO SECOND CELL: all 25 swept pairs print the parity
    law with r = P the only departure, so every move recorded in this
    paragraph -- at r = 5 as well as at r = 2 -- was the classifier
    (explore_cascade_scale.py H3). What survives above is the r = P
    clause, and it survives EXACTLY rather than nearly. **
F6  THE TWO-CLASS FAMILY IS BUILT AND IT CONTAINS WHAT IT WAS BUILT
    TO CONTAIN (observation; P4's fork kill misses -- 16 cells carry
    a large-onto-large drop). Eight windows at P = 4..7 with large
    caps at two offsets, 84 cells, and gap parity disagrees at 19 of
    them at two ranges and at 17 at three (explore_cascade_roof.py H5,
    which reproduces the 19 as its control before moving it): two
    cells flip bounded -> GATED under the deeper range, both toward
    gap parity. The verdict stands on the 17 -- the position-only
    reading fails in the periodic families too and not only at the
    cubic. The fork this finding scores was never at risk from the
    range, the large-onto-large drop count being read off the
    quotient sequence.
    The family is the instrument the value law will be read on: its
    knobs are the two offsets and the two values, and unlike the
    cubic every one of its cells has a verdict that a second range
    can confirm.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_shift_repair import (          # noqa: E402
    C_MAX,
    build_q,
    build_q_positions,
    c_min_row,
    designed,
    fmt_row,
    greedy,
    legality_failures,
    measured_verdict,
    quotients_cbrt2_minus_1,
    quotients_e_minus_2,
    usable_depth,
)

T_MAX = 10
N_CAL = 100_000
N_FAM = 50_000
R_MAX = 8
EXTRA = R_MAX + 12
WANT = 80


# ------------------------------------------------------------- windows

def graded(period, caps, want=WANT):
    """Quotients 1 everywhere except a_(k+1) = cap at k = offset mod period."""
    return [caps.get(k % period, 1) for k in range(want)]


def large_positions(a, jmax):
    return [j for j in range(min(jmax, len(a))) if a[j] >= 2]


# ------------------------------------------------------- the candidate

def gap_parity(a, r, jmax):
    """Drop sites, their landing gaps, and the large-onto-large count.

    Returns (drops, odd, large_onto_large, verdict) where the verdict is
    gap parity's EXISTENTIAL form: gated iff some drop site's gap is odd.
    """
    drops = odd = lol = 0
    for j in range(jmax):
        if j + r + 1 >= len(a):
            break
        if a[j] > a[j + r]:
            drops += 1
            if a[j + r] >= 2:
                lol += 1
            p = j + r
            s = p
            while s >= 0 and a[s] < 2:
                s -= 1
            if s >= 0 and (p - s) % 2 == 1:
                odd += 1
    if drops == 0:
        return drops, odd, lol, "delay-0"
    return drops, odd, lol, ("GATED" if odd else "bounded")


# ---------------------------------------------------------- the engine

def cell_rows(name, a, n_top, rmax=R_MAX, tmax_cap=T_MAX, show=True):
    """Per stride: repairs, REACH/TOP/SPAN record, c_min row, verdict.

    The digit path, the c_min rows and the verdict classifier are the
    parent rig's; the span record is what is new.
    """
    kn = usable_depth(build_q(a, n_top), n_top)
    tmax = min(tmax_cap, kn - 1)
    depth = tmax + C_MAX + 2
    q = build_q_positions(a, kn + EXTRA)
    digits = [greedy(n, q) for n in range(n_top)]
    strings = [tuple(d[:depth]) for d in digits]
    order = sorted(range(n_top), key=lambda i: strings[i])
    qmax = q[-1]
    cap = 0
    for j in range(n_top - 1):
        s1, s2 = strings[order[j]], strings[order[j + 1]]
        p = 0
        while p < depth and s1[p] == s2[p]:
            p += 1
        if p > cap:
            cap = p
    recon = legal = 0
    for n in range(n_top):
        d = digits[n]
        if sum(d[k] * q[k] for k in range(len(q)) if d[k]) != n:
            recon += 1
        legal += legality_failures(d, a)
    if show:
        print(f"{name}   K(N) = {kn}, t <= {tmax}, CAP(N) = {cap}, "
              f"recon/legality failures {recon}/{legal}")
    out = {}
    for r in range(1, rmax + 1):
        if len(q) - r < 2:
            continue
        repairs = over = 0
        span_max = 0
        reach_min = None
        top_max = 0
        # floor profile: min REACH among repairs with TOP >= h
        floor = {}
        imgs = []
        for n in range(n_top):
            d = digits[n]
            shifted = [0] * r + d[:len(q) - r]
            v = sum(d[k] * q[k + r] for k in range(len(q) - r) if d[k])
            over += v > qmax
            leg = greedy(v, q)
            if leg != shifted:
                repairs += 1
                diff = [i for i in range(len(leg)) if leg[i] != shifted[i]]
                lo, hi = diff[0], diff[-1]
                if hi - lo > span_max:
                    span_max = hi - lo
                if reach_min is None or lo < reach_min:
                    reach_min = lo
                if hi > top_max:
                    top_max = hi
                if hi not in floor or lo < floor[hi]:
                    floor[hi] = lo
            imgs.append(tuple(leg[:tmax]))
        A = c_min_row(strings, order, imgs, tmax, depth)
        mv = measured_verdict(repairs, A, tmax, cap)
        # the profile as a monotone read: min REACH over TOP >= h
        prof = []
        run = None
        for h in range(top_max, -1, -1):
            if h in floor and (run is None or floor[h] < run):
                run = floor[h]
            prof.append((h, run))
        prof.reverse()
        drops, odd, lol, gv = gap_parity(a, r, kn + EXTRA - r - 1)
        out[r] = dict(repairs=repairs, reach=reach_min, top=top_max,
                      span=span_max, prof=prof, A=A, tmax=tmax,
                      measured=mv, gap=gv, drops=drops, odd=odd, lol=lol,
                      cap=cap, over=over)
        if show:
            reach = "-" if reach_min is None else str(reach_min)
            marks = []
            for h in (4, 8, 12, 16):
                hit = [p for (hh, p) in prof if hh >= h and p is not None]
                marks.append(str(min(hit)) if hit else "-")
            flag = "" if mv == gv else "   <<< GAP-PARITY DISAGREES"
            print(f"  r {r}: repairs {repairs:6d}  reach {reach:>2s}"
                  f"  top {top_max:2d}  span {span_max:2d}"
                  f"  floor@4/8/12/16 " + "/".join(f"{m:>2s}" for m in marks)
                  + f"  c_min " + fmt_row(A, tmax)
                  + f"  measured {mv:8s} gap-parity {gv:8s}"
                  + f" (drops {drops}, odd {odd}, l-on-l {lol}){flag}")
        if over:
            print(f"    !! {over} images above the built weights at r = {r}")
    return out


# ------------------------------------------------------- experiments

CUBIC = quotients_cbrt2_minus_1(WANT)
E2MINUS = quotients_e_minus_2(WANT)
RANGES = (30_000, 100_000)
RANGES3 = (30_000, 100_000, 300_000)


def saturates(row):
    """Does the column TOUCH the instrument's ceiling anywhere?

    Inclusive of C_MAX, and that is not a detail: the single-range
    classifier prints '>' only ABOVE C_MAX, so a column sitting exactly
    at it looks like an ordinary number while being a delay the
    lookahead cannot measure. Reading it as an ordinary number is what
    makes a stable-across-ranges test downgrade a gated cell, and the
    A = B control in E4 is what catches that.
    """
    A, tmax = row["A"], row["tmax"]
    return any(A[t] - t + 1 >= C_MAX for t in range(1, tmax + 1))


def recurring(row):
    """Does the c_min column RETURN to 0 after being nonzero?

    This is what separates the two shapes the pinned signal cannot
    tell apart, and it separates them by what a witness can be. A
    column served by ONE deep witness declines by exactly 1 per depth
    and never comes back to 0 inside the table -- the unbounded
    signature. A column whose nonzeros are LOCAL returns to 0 above
    them and rises again with the window's period, which no single
    pair agreeing to one depth can produce.
    """
    A, tmax = row["A"], row["tmax"]
    c = [max(0, A[t] - t + 1) for t in range(1, tmax + 1)]
    seen = False
    for x in c:
        if x > 0:
            seen = True
        elif seen:
            return True
    return False


def range_verdict(rows_r):
    """The verdict from a cell read at several ranges, stability first.

    The single-range classifier's PINNED signal -- the top two depths
    served by one witness -- reads an unbounded map correctly and
    misreads a LOCAL constant that recurs with the window's own period,
    which is what a graded window produces and no window in the parent
    rig did. Range stability is the authoritative call (the parent's
    own words), so it is applied in BOTH directions here: a witness
    that grows with the range gates the cell however the column reads
    inside one table, and a column that is unchanged across a tenfold
    range while the data cap climbs AND returns to 0 above its own
    nonzeros is bounded however it reads at the top of one. The second
    clause is what keeps the downgrade off the pinned signal's real
    subject: three controls hold it in place -- A = B in E4 must print
    F4's law, the nine designed windows in E2 must miss it nowhere,
    and the cubic and e - 2 must keep the parent rig's verdicts.
    """
    lo, hi = rows_r[0], rows_r[-1]
    if saturates(hi):
        return "GATED"
    if hi["repairs"] == 0:
        return "delay-0"
    if hi["A"][hi["tmax"]] > lo["A"][lo["tmax"]]:
        return "GATED"
    same = all(
        r0["A"][t] == r1["A"][t]
        for r0, r1 in zip(rows_r, rows_r[1:])
        for t in range(1, min(r0["tmax"], r1["tmax"]) + 1)
    )
    if same and recurring(hi):
        return "bounded"
    return hi["measured"]


def ranged(name, a, rmax, ranges=RANGES, expect=None):
    """One cell block per stride, read at two ranges, verdict on GROWTH.

    `expect` is a function r -> predicted verdict, printed beside the
    measurement and scored; None prints the measurement alone.
    """
    rows = [cell_rows("", a, n, rmax=rmax, show=False) for n in ranges]
    print(f"{name}   large positions {large_positions(a, 18)}")
    miss = 0
    for r in sorted(rows[0]):
        lo, hi = rows[0][r], rows[-1][r]
        v = range_verdict([row[r] for row in rows])
        span_grew = hi["span"] > lo["span"]
        reach = "-" if hi["reach"] is None else str(hi["reach"])
        print(f"  r {r}: repairs {hi['repairs']:6d}  reach {reach:>2s}"
              f"  span {lo['span']:2d}->{hi['span']:2d}"
              f"{' GROWS' if span_grew else '      '}"
              f"  drops {hi['drops']:3d} odd {hi['odd']:3d}"
              f" l-on-l {hi['lol']:3d}")
        for n, row in zip(ranges, rows):
            print(f"      N {n:6d}: c_min " + fmt_row(row[r]["A"],
                                                      row[r]["tmax"])
                  + f"  CAP {row[r]['cap']:2d}"
                  f"  A_top {row[r]['A'][row[r]['tmax']]:2d}"
                  f"  top {row[r]['top']:2d}")
        line = f"      -> measured {v:8s} gap-parity {hi['gap']:8s}"
        if hi["gap"] != v:
            line += "   <<< GAP-PARITY DISAGREES"
        if expect is not None:
            p = expect(r)
            ok = p == v
            miss += not ok
            line += f" | predicted {p:8s}" + ("" if ok else "  <<< MISS")
        print(line)
    return miss


def e1_controls():
    print("=" * 78)
    print(f"E1 CONTROLS AND CROSS-RIG CALIBRATION (N = {N_CAL})")
    print("-- explore_shift_repair.py records repairs 99390/87743/95040/"
          "97465 at the cubic r = 1..4 and 99390/99390/0/99390 at e - 2,")
    print("   with the cubic gated at r = 1, 3, 5 and e - 2 at "
          "r = 1, 4, 7 --")
    for name, a in (("W1 cbrt(2)-1 cubic", CUBIC), ("W2 e-2", E2MINUS)):
        cell_rows(name, a, N_CAL)
        print()


def e2_span_at_known_cells():
    print("=" * 78)
    print(f"E2 THE SPAN WHERE THE VERDICT IS KNOWN, N = {RANGES}")
    ranged("W1 cbrt(2)-1 cubic", CUBIC, R_MAX)
    print()
    ranged("W2 e-2", E2MINUS, R_MAX)
    print()
    print("-- the designed family, where the verdict is F4's parity of "
          "r mod P --")
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            def law(r, P=P):
                res = r % P
                return ("delay-0" if res == 0
                        else "bounded" if res % 2 == 0 else "GATED")
            miss = ranged(f"D P={P} A={A}", designed(P, A, WANT), 2 * P,
                          expect=law)
            print(f"      F4 misses at this window: {miss}")
    print()


def e3_families():
    print("=" * 78)
    print("E3 THE TWO DESIGNED FAMILIES")
    print("-- P3: the graded control. The large-cap SET is one residue "
          "class mod P; only the VALUES on it alternate, so a law")
    print("   reading positions predicts F4's parity of r mod P "
          "unchanged. (The quotient SEQUENCE has period 2P.) --")
    total = 0
    for P, A, B in ((3, 5, 2), (3, 2, 5), (4, 3, 2), (5, 2, 4)):
        def law(r, P=P):
            res = r % P
            return ("delay-0" if res == 0
                    else "bounded" if res % 2 == 0 else "GATED")
        miss = ranged(f"G P={P} caps {A}/{B}", graded(2 * P, {P - 1: A,
                                                              2 * P - 1: B}),
                      2 * P, ranges=RANGES3, expect=law)
        total += miss
        print(f"      F4-on-the-set misses at this window: {miss}")
    print(f"  P3 total misses: {total}")
    print()
    print("-- P4: the two-class family, where large-onto-large drops "
          "exist for the first time --")
    lol_cells = 0
    for P, c1, c2, A, B in ((4, 1, 3, 5, 2), (4, 1, 3, 2, 5),
                            (5, 1, 3, 5, 2), (5, 0, 2, 4, 2),
                            (6, 1, 4, 5, 2), (6, 0, 3, 5, 2),
                            (7, 1, 4, 5, 2), (7, 2, 3, 5, 2)):
        a = graded(P, {c1: A, c2: B})
        ranged(f"X P={P} caps {A}@{c1}/{B}@{c2}", a, min(2 * P, R_MAX + 4))
        for r in range(1, min(2 * P, R_MAX + 4) + 1):
            lol_cells += gap_parity(a, r, 30)[2] > 0
    print(f"  cells carrying a large-onto-large drop: {lol_cells}")


def verdict_vector(a, rmax, ranges=RANGES):
    """The verdict per stride, growth-authoritative, as a short vector."""
    rows = [cell_rows("", a, n, rmax=rmax, show=False) for n in ranges]
    out = []
    for r in sorted(rows[0]):
        v = range_verdict([row[r] for row in rows])
        out.append({"GATED": "G", "bounded": "b", "delay-0": "."}[v])
    return out


def e4_value_sweep():
    print("=" * 78)
    print("E4 THE VALUE SWEEP AT P = 3 -- graded window [1,1,A,1,1,B]^inf")
    print("   G = gated, b = bounded, . = delay-0, strides r = 1..6.")
    print("   F4's parity of r mod 3 (which A = B must print): G b . G b .")
    for A, B in ((2, 2), (3, 3), (5, 5),
                 (2, 3), (3, 2), (2, 5), (5, 2),
                 (3, 5), (5, 3), (2, 7), (7, 2)):
        v = verdict_vector(graded(6, {2: A, 5: B}), 6)
        ctrl = "   <- A = B, must be F4" if A == B else ""
        bad = ""
        if A == B and "".join(v) != "Gb.Gb.":
            bad = "   <<< CONTROL FAILS, THE SWEEP IS VOID"
        print(f"  A={A} B={B}:  " + " ".join(v) + ctrl + bad)


def e5_threshold():
    """The pairs where RATIO and DIFFERENCE part, both orders.

    The verdict read is the EXTRA gate: F4's family prints G b . G b .
    and the sweep asks which of the two bounded cells (r = 2, r = 5)
    turns gated. The rule scored here was fixed before this ran.
    """
    print("=" * 78)
    print("E5 THE THRESHOLD -- ratio vs difference, P = 3, r = 1..6")
    print("   ratio      predicts an extra gate iff max >  2 min")
    print("   difference predicts an extra gate iff max >= min + 3")
    miss_r = miss_d = 0
    for A, B in ((2, 4), (4, 2), (3, 6), (6, 3), (4, 8), (8, 4),
                 (4, 7), (7, 4), (5, 8), (8, 5), (3, 7), (7, 3),
                 (4, 9), (9, 4)):
        v = "".join(verdict_vector(graded(6, {2: A, 5: B}), 6))
        hi, lo = max(A, B), min(A, B)
        extra = v[1] == "G" or v[4] == "G"
        pr, pd = hi > 2 * lo, hi >= lo + 3
        miss_r += pr != extra
        miss_d += pd != extra
        print(f"  A={A} B={B}: {' '.join(v)}  extra gate {str(extra):5s}"
              f"  ratio {str(pr):5s}{'' if pr == extra else ' MISS'}"
              f"  difference {str(pd):5s}"
              f"{'' if pd == extra else ' MISS'}")
    print(f"  misses: ratio {miss_r}, difference {miss_d}")


if __name__ == "__main__":
    e1_controls()
    e2_span_at_known_cells()
    e3_families()
    print()
    e4_value_sweep()
    print()
    e5_threshold()
