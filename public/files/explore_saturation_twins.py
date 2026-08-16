"""Can the saturation clause's ceiling be replaced by a property of the
column? The twin exhibit, and the calibration reading of C_MAX.

THE QUESTION
------------
The run-length rule (explore_cascade_rule.py H3) carries one constant:
a column whose excess peak reaches C_MAX = 10 reads SATURATED. Every
other clause of the rule is derived -- the run-against-period threshold
from locality, the refusal from the room a signature needs -- but the
saturation threshold is a number, and it is the one clause the rule has
at an aperiodic window, where the period is absent and only saturation
can fire (explore_cascade_rule.py C3). If the ceiling could be replaced
by a property of the column itself, the rule would reach the aperiodic
windows cap-free. This rig asks whether any such property exists. The
kill, fixed before the work: the replacement property turns out to
consult the cap anyway -- a bound that moves when C_MAX does.

THE HAND-ATTACK (pre-engine, on paper and on specimen columns
the existing engines printed)
-------------------------------------------------------------
D1  THE TRUNCATION ROLE OF C_MAX IS VACUOUS AT THE DEEP READING. C_MAX
    enters the instrument twice: as the verdict threshold, and as the
    string truncation depth = tmax + C_MAX + 2 (explore_cascade_span.py
    cell_rows). At the deep reading tmax = K(N) - 1, greedy digits of
    n < N vanish at every position whose weight exceeds n, and digits
    reconstruct n exactly, so two distinct n differ at some position at
    or below K(N) < depth: the truncation never censors anything. The
    only live C_MAX in the rule is the threshold. S1 checks this
    mechanically rather than trusting the derivation.
D2  THE CANDIDATE PROPERTIES DIE ON SPECIMENS BEFORE ANY SWEEP. Three
    intrinsic column properties were attacked by hand against columns
    the existing engines print, and each dies on a specimen:
    - THE CEILING TOUCH (the peak's witness is the table's deepest
      agreement, A = CAP): dies at the graded window (8, 5), whose
      r = 1 column -- saturation's own lineage -- has witness depth 8
      against CAP 11 at N = 10000; and dies in the other direction at
      any bounded cell whose deepest pair splits just below its
      agreement depth, which touches CAP near the table top with small
      excess.
    - THE PINNED COLUMN (witness depth constant over its defined
      range): the graded (8, 4) column at r = 3 -- trusted BOUNDED by
      the value law -- is constant at 8 over its whole defined range;
      one dominant witness pair is generic, not a signature.
    - CLOSURE (the run returns to zero inside the table): already
      killed at the designed family, where a stride gated by the
      family's own law closes with four depths to spare
      (explore_cascade_rule.py H4); phase-dependent at the graded one.
D3  THE TWIN. What remains after D2 is the run multiset -- the lengths
    and peaks of the maximal nonzero runs -- plus their PLACEMENT. And
    the corpus already prints a collision on the multiset: the graded
    window (8, 4) at r = 3, trusted bounded (B < A <= 2B + 1 with
    A * B >= 30), prints the single run 5 4 3 2 1 at table depth 11
    (N = 30000); the cubic window at r = 5, gated on the retired
    classifier's record, prints the single run 5 4 3 2 1 at table
    depth 11 (N = 100000). Identical multiset, identical depth,
    different placement -- and placement is the axis closure died on.
    A property of the column that catches the cubic stride must
    misread the trusted bounded cell, and one that spares the bounded
    cell must miss the stride.
D4  BEYOND RUN 5 THE TRUSTED CORPUS IS SILENT BY CONSTRUCTION. Every
    trusted bounded verdict lives at a periodic window of period 3 to
    6, where the rule itself reclassifies any run reaching the period
    as gated. So no trusted bounded column can carry a run of 6 or
    more, and a closed run's peak is at most its length (the excess
    declines by at most 1 per depth). The bounded population's ceiling
    is therefore capped by the corpus's own periods -- which means a
    threshold catching the cubic r = 3 run of 9 extrapolates past
    every trusted specimen in existence, and a threshold inside the
    bounded range collides with the twins of D3. Between the two
    zones there is nothing for a derivation to grip.
D5  WHAT C_MAX THEN IS. If S2 confirms the bounded ceiling and S3 the
    aperiodic peaks, the threshold is revealed as CALIBRATION: a
    constant sitting just above every excess peak the corpus's trusted
    bounded cells have ever printed, doing cross-window inductive work
    -- "no trusted bounded cell ever printed this" -- rather than
    reading anything intrinsic to the column in front of it. That is
    an honest clause at tier pattern, and it is not a cap that a
    column property could replace: the information is not in the
    column.
D6  THE RUN HALF IS ALREADY IMPLIED AT THE DEEPEST RANGE; THE PEAK HALF
    IS NOT. Every trusted-bounded LABEL at N = 300000 is a recorded
    verdict -- the graded map's 210 cells read bounded there
    (explore_cascade_rule.py H1) and the value law's bounded cells
    re-read there (explore_cascade_values.py). The designed family is
    the weaker warrant of the three and is named as one: its labels come
    from the residue law, which carries no range set, so at this range
    the label is a law applied and not a verdict recorded, and whether
    the rule still agrees with it there is something the arm's own print
    answers (F6). And the rule gates any run reaching the
    window's period, 6 at the graded window and 3 to 5 at the designed
    one. So longest run <= 5 follows from the labels themselves and no
    measurement can move it. PEAK does not follow: the excess
    c(t) = A(t) - t + 1 rises with A's jumps and is capped by the run
    length only where the run CLOSES, since a closed run must decline to
    zero at no more than 1 per depth. The whole informative content of a
    third range therefore sits on the EDGE-OPEN bounded columns, where a
    run of 5 or less can carry a peak anywhere below the saturation
    threshold. Their count is known to be nonzero at the shallower
    ranges (Q1), so this is not a formality.
D7  WHY THIS IS NOT S2 WITH A THIRD RANGE. S2's bounded ranges are
    chosen to match the aperiodic table depths the twin hunt needs, and
    enlarging the twin store would move F3's twin COUNTS as a side
    effect of asking a different question. The ceiling is a statement
    over the trusted corpus AT the range it is read at, so the third
    range is read as its own stage over the same three populations,
    built from the same population generators, and the twin exhibit is
    left at the depths it was designed for. Whether the twins survive at
    N = 300000 is a separate question and is not asked here.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what it would mean)
  P1 (the positive control, run FIRST; nothing below is read if it is
      red) at every specimen cell, the A row and CAP recomputed at
      string truncation K(N) + 2 equal the ones at the standard
      truncation tmax + C_MAX + 2, entry for entry. KILL: any
      difference -- the truncation binds, D1 is wrong, and the fixed
      kill fired at the first check.
  P2 (the bounded ceiling) over every trusted-bounded specimen -- the
      graded map's 210 cells at r = 2, the value grid's bounded cells
      at r = 3, the designed family's even-residue strides -- the
      longest run is at most 5 and every closed run's peak is at most
      its length; columns still open at the table edge counted and
      predicted 0.
  P3 (the twin) the cubic r = 5 column finds at least one exact twin
      -- same table depth, same run multiset -- among the trusted
      bounded specimens.
  P4 (the silent zone) the cubic r = 3 (run 9) and e - 2 r = 7 (run 6)
      columns find ZERO trusted-bounded twins, and the reason is P2's
      cap: no trusted bounded run reaches 6 anywhere in the corpus.
  P5 (the calibration gap) C_MAX = 10 sits strictly above every
      trusted bounded peak; among the aperiodic strides the retired
      classifier gated, the peaks at N = 100000 (cubic 10, 9, 5;
      e - 2 12, 10, 7) split three ways -- at or above C_MAX
      (currently saturated), between the bounded ceiling and C_MAX
      (the gap where the corpus is silent), and inside the bounded
      range (indistinguishable from trusted bounded columns by any
      placement-free read).
  Q1 (the edge-open count) columns whose excess is still positive at
      the table's last depth, per population: a bounded specimen open
      at the edge would weaken D4's ceiling argument; the count is an
      observable either way.
  Q2 (placement) for every twin found, the placement offset between
      the aperiodic run and its bounded twin -- whether the offsets
      even share a sign, since placement is the one residue a column
      property could still try to read.
  P6 (the third-range arm's own positive control, run FIRST; nothing
      in P7 is read if it is red) at N = 100000 the arm's reading path
      prints exactly 210 graded, 18 value and 24 designed
      trusted-bounded columns, with graded's maximum (longest run,
      peak) at most (3, 3), value's exactly (5, 5) and designed's at
      most (2, 2) -- F2's recorded reading at the range where it
      attains its ceiling. KILL: any disagreement; the arm is not
      reading F2's populations and nothing below it is read.
  P7 (the ceiling at the deepest range) at N = 300000 every
      trusted-bounded column prints peak at most 5. The observable is
      the maximum peak over the three populations' bounded labels, and
      its live half is the maximum over the EDGE-OPEN bounded columns,
      those being the only ones a run bound does not already cap (D6).
      KILL: a bounded maximum peak of 6 or more.
  Q3 (the edge-open count at depth) how many bounded columns are still
      open at the table's last depth at N = 300000, per population,
      and what peaks they carry; an observable either way.

FINDINGS (each at its own tier)
-------------------------------
F1  THE TRUNCATION NEVER BINDS (property, checked; S1 green at all six
    specimens). The A rows and CAP recomputed at string truncation
    K(N) + 2 equal the standard tmax + C_MAX + 2 reading entry for
    entry at every specimen -- graded, designed and aperiodic alike.
    So C_MAX's truncation role is vacuous at the deep reading, exactly
    as D1 derives, and the threshold is the constant's only live use.
    The ceiling is NOT an instrument artifact to be engineered away;
    whatever it is doing, it is doing as a verdict.
F2  THE BOUNDED CEILING IS (5, 5) AND THE POPULATIONS OVERLAP BELOW IT
    (measurement at scanned scope, 480 trusted-bounded cells; S2).
    Max peak 5 and max run 5, attained at the value grid's (8, 4) --
    the very cell the hand-attack picked -- with the graded map's 420
    bounded columns never exceeding (3, 3) and the designed family's
    24 never exceeding (2, 2). C_MAX = 10 sits strictly above all of
    it. But the trusted GATED populations reach DOWN below the
    ceiling: the value law's gated cells print (3, 3) at 10 cells and
    (5, 5) at 13, colliding with 350 and 36 bounded columns at the
    same histogram cells -- a gated cell's column passes THROUGH
    bounded-looking states at shallow ranges as its runs grow, which
    is the one-way law seen from the other side. So no threshold on
    (run, peak) separates gated from bounded even at periodic windows;
    there, the period and the placement do the work. And Q1's
    edge-open count kills the last intrinsic candidate: 118
    trusted-bounded columns are still open at the table edge (113
    graded, 4 value, 1 designed), so openness at the edge implies
    nothing.
F3  THE TWINS EXIST, AND PLACEMENT READS NOTHING CONSISTENT (fact; S4,
    predicted by D3). The cubic r = 5 column at N = 100000 -- single
    run 5 4 3 2 1 at depth 11, gated on the retired classifier's
    record -- has FOUR exact twins (same depth, same multiset) among
    trusted-bounded columns: the value grid's (8, 4) and (6, 5) at
    30000 and (9, 7) and (10, 6) at 100000, every one bounded by the
    value law. The bounded-on-record cubic strides r = 2, 4, 6 have
    graded-map twins of their own. Placement offsets run +2 at the
    r = 5 twins and -3 at the others: no sign, no reading. A property
    of the column that catches the stride misreads the law's own
    cells; one that spares them stays silent.
F4  BEYOND RUN 5 THE CORPUS IS SILENT, BY ITS OWN PERIODS (property of
    the corpus, with the measured zero; S4, predicted by D4). The
    cubic r = 3 (run 9, then 10 at the deeper range) and e - 2 r = 7
    (run 6, then 7) columns find zero
    exact twins AND zero near-twins at any depth: no trusted bounded
    column anywhere carries a run of 6 or more, because every trusted
    bounded verdict lives at a window of period at most 6, where the
    rule itself reclassifies such a run as gated. A threshold catching
    run 9 extrapolates past every trusted specimen in existence; a
    threshold inside the bounded range walks into F3's twins. The
    derivation has nothing to grip in either zone, and the fixed kill
    fires in this sharpened form: the replacement does not consult the
    cap -- it consults the CORPUS, a bound that moves when the corpus
    grows.
F5  WHAT C_MAX IS, AND THE INSTRUMENT THE CALIBRATION LEAVES (pattern).
    The threshold is CALIBRATION: an inductive constant sitting above
    every excess peak the corpus's trusted bounded cells have ever
    printed, not a property of the column in front of it. Read
    honestly, the calibrated ceiling is 6 -- one past the bounded
    maximum -- and at the deepest range scanned that clause
    reproduces the retired classifier's whole aperiodic split with
    nothing else moving: at N = 300000 the on-record gated strides
    print peaks 12, 9, 7 (cubic r = 1, 3, 5) and 12, 10, 7 (e - 2
    r = 1, 4, 7), every one at or past 6, while every bounded-on-record
    stride prints 3 or less; at the trusted corpus no bounded cell
    reaches 6, so nothing crosses the gated/bounded divide -- the
    gated cells with peaks 6 to 9 relabel from gated to saturated,
    which every scoring the cascade runs treats as one side. At
    N = 100000 the cubic r = 5
    still prints peak 5 -- inside the bounded range, invisible to any
    calibrated read, its twins dissolving only at the deeper range
    (peak 7, run 6, no twin possible). The tier is the finding: this
    third instrument is INDUCTION over 732 specimens across three
    ranges (F6) and stays pattern
    forever -- F4 says the corpus cannot back it with a derivation
    beyond run 5 -- so the aperiodic verdicts it issues are
    calibrated readings, never rules, and the saturation clause is
    not, and cannot be made, cap-free.
F6  THE CEILING IS UNMOVED AT THE DEEPEST RANGE, AND ONLY THE GATED
    SIDE MOVES (measurement at scanned scope, 252 trusted-bounded
    columns at N = 300000; S5, its control at 100000 green). Max peak
    5 and max run 5, attained where F2 attains them, at the value
    grid's (8, 4) -- so the deepest range's bounded peaks are now
    MEASURED below 6, where the rule's own verdicts bounded them only
    below the saturation threshold of 10. The live half is well inside
    that: the edge-open bounded columns, the only ones D6 leaves
    uncapped by a run bound, number 58 graded, 1 designed and 0 value,
    and the largest peak among all of them is 3. The margin is two
    values and not one: the constant is one past the bounded ceiling and
    the shallowest aperiodic peak the split needs saturated is 7, so a
    ceiling of 6 would still issue 7 and still reproduce the split, and
    only a bounded column at 7 or above would have forced a choice.
    One thing about the control is worth the reader's attention, since
    its PASS does not say it: P6's verdict is invariant on the very axis
    this arm varies. It passes at N = 3000 as readily as at 100000 --
    the cell counts are range-free and the ceilings hold at every range
    read -- so a run that silently used the wrong N would still print
    GREEN. What witnesses the range is the OBSERVABLE and not the
    verdict: the graded and value keys carry n, and the gated maxima
    move with it. Read those, not the GREEN.
    D6's weakest warrant also holds at this range: the designed family's
    bounded strides print max run 2 against periods of 3, 4 and 5, so
    the rule agrees with the residue label at every one of them and the
    label applied there is not a label the reading has to assume.
    And the bounded side does not MOVE with depth while the gated side
    does. Between the two ranges the arm printed, the graded map's
    (longest run, peak) histogram is identical entry for entry --
    (0,0)x18, (1,1)x17, (3,3)x175 -- and all 18 bounded value cells
    print (5, 5) at both; over that same depth the GATED maxima rise,
    the value grid's from 13 to 15 and the designed family's from 18
    to 19, and the graded population's edge-open count falls from 73
    to 58 with its spectrum unchanged. That last pair is an AGGREGATE
    reading and not a per-column one: an unchanged histogram with a
    lower open count is what closure without growth looks like, but it
    is equally consistent with one column growing while another
    shrinks, and the arm stores no column-to-column correspondence
    across ranges to tell those apart. Depth moves the gated
    populations AWAY from the ceiling and does not move the bounded
    ones at all, so the gap the constant sits in widens with the
    reading rather than closing.
    What this settles is what F5's reading was missing: the calibrated
    ceiling of 6 is calibration over the corpus at the range its
    verdicts are issued at, and not a number chosen between the corpus
    and the aperiodic split it reproduces. It does not make the clause
    derivable -- F4's silence past run 5 is untouched, and the tier
    stays pattern.

THE DESIGN
----------
Everything is read through explore_cascade_rule.py's cell() -- the same
window builder, digit path and excess column as the rule itself -- so a
column here is the column the rule reads, not a reimplementation. The
trusted populations and their labels:
  - the graded map, B = 3..12, A = 4..24, r = 2: bounded at every cell
    (explore_cascade_rule.py H1, rule at scanned scope);
  - the value grid, 92 cells at r = 3, labels from the value law
    B < A <= 2B + 1 with A * B >= 30 (explore_cascade_values.py H2,
    reproduced instrument-independently at zero misses);
  - the designed family [1^(P-1), A]^inf, P = 3, 4, 5, A = 2, 3, 5,
    labels from the residue law (delay-0 / bounded / gated by r mod P).
The aperiodic windows cbrt(2) - 1 and e - 2 are read at strides 1..8.
Ranges: the bounded populations at N = 30000 and 100000 (a bounded
cell's column only shrinks at smaller N, so any N yields a trusted
bounded specimen; matching the aperiodic table depths is what the twin
hunt needs); the aperiodic windows at N = 100000 and 300000. A twin is
an exact match on (table depth, run multiset); a near-twin matches the
multiset at any depth and is reported separately.

The third-range arm (S5) reads the SAME three populations at ONE range
through the same generators S2 uses, so the corpus is defined once; it
carries its own control stage at N = 100000 (P6) and the reading stage
at N = 300000 (P7), and it touches neither the twin store nor S2's
ranges (D7). Every peak it reports is a peak at the data's own depth,
the deep reading throughout.

RUN RECORD (the estimate first, then what it cost)
Estimate: S2 graded 210 cells at two ranges ~4.5 min, value grid 92
cells at two ranges ~4 min, designed 9 windows ~3 min, S3 aperiodic
~1.5 min, S1 seconds: ABOUT 13 MINUTES, stop at 30. The necessity is
the claim's own shape: the ceiling is a statement over every trusted
bounded specimen, and a sample caps nothing. Peak memory ~300 MB at
N = 300000 (the parent rig's figure), under memwatch at 512. Stages
run one at a time (argv) so no single call is open-ended.
Ran: S1 14.0 s at 105 MB peak; S2 with S3/S4 455.0 s at 257 MB peak
commit, both under memwatch at 512 -- eight minutes against the
thirteen estimated, inside the stop.
The third-range arm, estimated off timed cells rather than scaled from
the above: a graded cell costs 2.86 s and a value cell 4.05 s at
N = 300000 against 0.89 and 1.22 at 100000, so s5c (the control at
100000) ABOUT 6 MINUTES and s5 (the reading at 300000) ABOUT 19, each
its own call, stop at 2x. Memory is the parent rig's 257 MB at
N = 300000, under memwatch at 512. The necessity is the claim's shape:
the ceiling is a statement over EVERY trusted bounded specimen at the
range it is read at, a sample caps nothing, and the deepest range is
the one the calibrated verdicts are issued at.
Ran: s5c 341.9 s at 104.4 MB peak commit; s5 1117.7 s at 299.4 MB peak
commit, both under memwatch at 512 -- 5.7 and 18.6 minutes against the
6 and 19 estimated, each inside its stop.
"""

import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_shift_repair import (          # noqa: E402
    C_MAX,
    build_q,
    build_q_positions,
    c_min_row,
    designed,
    greedy,
    quotients_cbrt2_minus_1,
    quotients_e_minus_2,
    usable_depth,
)
from explore_cascade_span import (          # noqa: E402
    WANT,
    cell_rows,
    graded,
)
from explore_cascade_rule import (          # noqa: E402
    DEEP,
    PERIOD,
    cell,
    law_says,
    window,
)

CUBIC = quotients_cbrt2_minus_1(WANT)
E2MINUS = quotients_e_minus_2(WANT)
BOUNDED_RANGES = (30_000, 100_000)
APERIODIC_RANGES = (100_000, 300_000)


def column(row):
    """The excess column c(t) for t = 1..tmax, from a cell() row."""
    A, tmax = row["A"], row["tmax"]
    return [max(0, A[t] - t + 1) for t in range(1, tmax + 1)]


def runs_multiset(c):
    """Sorted (length, peak) pairs of the maximal nonzero runs."""
    out, i, n = [], 0, len(c)
    while i < n:
        if c[i] == 0:
            i += 1
            continue
        j = i
        while j < n and c[j] > 0:
            j += 1
        out.append((j - i, max(c[i:j])))
        i = j
    return tuple(sorted(out))


def run_starts(c):
    """1-based start depth of each maximal nonzero run."""
    out, i, n = [], 0, len(c)
    while i < n:
        if c[i] == 0:
            i += 1
            continue
        j = i
        while j < n and c[j] > 0:
            j += 1
        out.append(i + 1)
        i = j
    return out


def summarize(row):
    c = column(row)
    ms = runs_multiset(c)
    return {
        "tmax": row["tmax"],
        "c": c,
        "multiset": ms,
        "peak": max(c) if c else 0,
        "longest": max((L for L, _ in ms), default=0),
        "edge_open": bool(c) and c[-1] > 0,
        "starts": run_starts(c),
        "repairs": row["repairs"],
    }


# ------------------------------------------------------------------ S1

SPECIMENS = (
    ("graded (8,5)", lambda: window(8, 5), 30_000, 2),
    ("graded (10,4)", lambda: window(10, 4), 30_000, 3),
    ("graded (8,4)", lambda: window(8, 4), 30_000, 3),
    ("designed P5 A3", lambda: designed(5, 3, WANT), 100_000, 8),
    ("cbrt(2)-1", lambda: CUBIC, 100_000, 8),
    ("e-2", lambda: E2MINUS, 100_000, 8),
)


def read_at_depth(a, n_top, rmax, depth_of):
    """The A rows and CAP with the string truncation chosen by depth_of,
    replicating cell_rows' pipeline exactly except for that one number.
    """
    kn = usable_depth(build_q(a, n_top), n_top)
    tmax = min(DEEP, kn - 1)
    depth = depth_of(kn, tmax)
    q = build_q_positions(a, kn + 20)
    digits = [greedy(n, q) for n in range(n_top)]
    strings = [tuple(d[:depth]) for d in digits]
    order = sorted(range(n_top), key=lambda i: strings[i])
    cap = 0
    for j in range(n_top - 1):
        s1, s2 = strings[order[j]], strings[order[j + 1]]
        p = 0
        while p < depth and s1[p] == s2[p]:
            p += 1
        cap = max(cap, p)
    out = {}
    for r in range(1, rmax + 1):
        imgs = []
        for n in range(n_top):
            d = digits[n]
            v = sum(d[k] * q[k + r] for k in range(len(q) - r) if d[k])
            imgs.append(tuple(greedy(v, q)[:tmax]))
        out[r] = c_min_row(strings, order, imgs, tmax, depth)
    return kn, tmax, cap, out


def s1_vacuity():
    print("=" * 78)
    print("S1 P1: THE TRUNCATION NEVER BINDS -- A rows and CAP at string")
    print(f"   depth K(N) + 2 against the standard tmax + C_MAX + 2")
    bad = 0
    for name, mk, n, rmax in SPECIMENS:
        a = mk()
        kn1, t1, cap1, rows1 = read_at_depth(
            a, n, rmax, lambda kn, tmax: kn + 2)
        kn2, t2, cap2, rows2 = read_at_depth(
            a, n, rmax, lambda kn, tmax: tmax + C_MAX + 2)
        same = cap1 == cap2 and all(rows1[r] == rows2[r] for r in rows1)
        bad += not same
        print(f"  {name:16s} N={n}  K(N)={kn1}  CAP {cap1} vs {cap2}  "
              f"A rows over r<=({rmax}): {'IDENTICAL' if same else 'DIFFER'}")
        if not same:
            for r in rows1:
                if rows1[r] != rows2[r]:
                    print(f"    r={r}: {rows1[r]} vs {rows2[r]}")
    print(f"  S1: {bad} specimens differ -- "
          + ("GREEN" if not bad else "RED, nothing below is read"))


# ------------------------------------------------------------------ S2

VALUE_GRID = ([(A, B) for B in range(2, 10) for A in range(2, 10)]
              + [(A, B) for B in range(3, 7) for A in range(10, 17)])


def graded_pop(n):
    """The graded map's 210 cells at r = 2, bounded at every cell."""
    for B in range(3, 13):
        for A in range(4, 25):
            c = cell(window(A, B), n, 2, PERIOD)
            yield ("graded-r2", "bnd", (A, B, n), summarize(c[2]))


def value_pop(n):
    """The value grid at r = 3, labelled by the value law."""
    for A, B in VALUE_GRID:
        c = cell(window(A, B), n, 3, PERIOD)
        yield ("value-r3", law_says(A, B), (A, B, n), summarize(c[3]))


def designed_pop(n):
    """The designed family, labelled by the residue law."""
    for P in (3, 4, 5):
        for A in (2, 3, 5):
            c = cell(designed(P, A, WANT), n, 2 * P, P)
            for r in sorted(c):
                res = r % P
                lab = ("delay0" if res == 0
                       else "bnd" if res % 2 == 0 else "gated")
                yield ("designed", lab, (P, A, r), summarize(c[r]))


def bounded_specimens():
    """Yield (population, label, key, summary) over the trusted corpus.

    Labels come from the owning law, never from this rig: the graded
    map's r = 2 cells are all bounded, the value grid's labels are the
    value law's, the designed family's are the residue law's.
    """
    for n in BOUNDED_RANGES:
        yield from graded_pop(n)
    for n in BOUNDED_RANGES:
        yield from value_pop(n)
    yield from designed_pop(100_000)


def s2_spectra():
    print("=" * 78)
    print("S2 P2/Q1: THE TRUSTED SPECTRA -- what bounded and gated columns")
    print("   actually print, per population")
    pop = defaultdict(lambda: {"n": 0, "peak": 0, "longest": 0,
                               "edge": [], "peak_at": None, "long_at": None,
                               "hist": defaultdict(int)})
    store = defaultdict(list)
    for popname, lab, key, s in bounded_specimens():
        g = pop[(popname, lab)]
        g["n"] += 1
        if s["peak"] > g["peak"]:
            g["peak"], g["peak_at"] = s["peak"], key
        if s["longest"] > g["longest"]:
            g["longest"], g["long_at"] = s["longest"], key
        if s["edge_open"]:
            g["edge"].append(key)
        g["hist"][(s["longest"], s["peak"])] += 1
        if lab == "bnd":
            store[(s["tmax"], s["multiset"])].append((popname, key))
    for (popname, lab), g in sorted(pop.items()):
        print(f"  {popname:10s} {lab:6s} cells {g['n']:4d}  "
              f"max peak {g['peak']:2d} at {g['peak_at']}  "
              f"max run {g['longest']:2d} at {g['long_at']}  "
              f"edge-open {len(g['edge'])}"
              f"{'  ' + str(g['edge'][:6]) if g['edge'] else ''}")
    print("  (longest run, peak) histograms:")
    for (popname, lab), g in sorted(pop.items()):
        row = " ".join(f"{k}x{v}" for k, v in sorted(g["hist"].items()))
        print(f"    {popname:10s} {lab:6s}: {row}")
    bmax_peak = max(g["peak"] for (p, l), g in pop.items() if l == "bnd")
    bmax_run = max(g["longest"] for (p, l), g in pop.items() if l == "bnd")
    print(f"  THE BOUNDED CEILING: max peak {bmax_peak}, max run {bmax_run},"
          f" against C_MAX = {C_MAX}")
    return store


# ------------------------------------------------------------------ S3/S4

ON_RECORD = {"cbrt(2)-1": {1, 3, 5}, "e-2": {1, 4, 7}}


def s3_s4_aperiodic_and_twins(store):
    print("=" * 78)
    print("S3/S4 P3/P4/P5/Q2: THE APERIODIC COLUMNS AND THEIR TWINS")
    print("   (the retired classifier's split is context, not a label)")
    for name, q in (("cbrt(2)-1", CUBIC), ("e-2", E2MINUS)):
        for n in APERIODIC_RANGES:
            c = cell(q, n, 8, PERIOD)
            for r in sorted(c):
                s = summarize(c[r])
                if s["repairs"] == 0:
                    continue
                old = "SAT" if s["peak"] >= C_MAX else "   "
                rec = "gated-on-record" if r in ON_RECORD[name] else ""
                twins = store.get((s["tmax"], s["multiset"]), [])
                print(f"  {name:10s} N={n:6d} r={r} t<={s['tmax']:2d} "
                      f"peak {s['peak']:2d} run {s['longest']:2d} "
                      f"{'edge-open' if s['edge_open'] else 'closed   '} "
                      f"{old} {rec:16s} starts {s['starts']}")
                if s["multiset"]:
                    if twins:
                        print(f"      TWINS (same depth, same multiset): "
                              f"{len(twins)}: {twins[:8]}")
                        for tp, tk in twins[:8]:
                            tc = (cell(window(tk[0], tk[1]), tk[2], 3, PERIOD)
                                  if tp == "value-r3" else
                                  cell(window(tk[0], tk[1]), tk[2], 2, PERIOD))
                            tr = 3 if tp == "value-r3" else 2
                            ts = summarize(tc[tr])
                            off = [a - b for a, b in
                                   zip(s["starts"], ts["starts"])]
                            print(f"        {tp} {tk}: starts {ts['starts']}"
                                  f"  offset {off}")
                    else:
                        near = sum(len(v) for k, v in store.items()
                                   if k[1] == s["multiset"])
                        print(f"      no exact twin; near-twins (multiset at"
                              f" any depth): {near}")


# ------------------------------------------------------------------ S5

CONTROL_RANGE = 100_000
DEEPEST_RANGE = 300_000

# F2's recorded reading at CONTROL_RANGE, per population: the bounded
# cell count, and the (longest run, peak) ceiling with the comparison
# the finding states it at -- "exactly" where F2 names the attaining
# cell, "at most" where it states a bound.
CONTROL = {
    "graded-r2": (210, (3, 3), "<="),
    "value-r3": (18, (5, 5), "=="),
    "designed": (24, (2, 2), "<="),
}


def ceiling_at(n):
    """Per (population, label): count, ceiling, edge-open, histogram."""
    pop = defaultdict(lambda: {"n": 0, "peak": 0, "longest": 0,
                               "peak_at": None, "long_at": None,
                               "open": [], "open_peak": 0, "open_at": None,
                               "hist": defaultdict(int)})
    for popname, lab, key, s in (list(graded_pop(n)) + list(value_pop(n))
                                 + list(designed_pop(n))):
        g = pop[(popname, lab)]
        g["n"] += 1
        if s["peak"] > g["peak"]:
            g["peak"], g["peak_at"] = s["peak"], key
        if s["longest"] > g["longest"]:
            g["longest"], g["long_at"] = s["longest"], key
        if s["edge_open"]:
            g["open"].append((key, s["peak"], s["longest"]))
            if s["peak"] > g["open_peak"]:
                g["open_peak"], g["open_at"] = s["peak"], key
        g["hist"][(s["longest"], s["peak"])] += 1
    return pop


def s5_report(n, control):
    print("=" * 78)
    head = ("P6 THE ARM'S POSITIVE CONTROL" if control
            else "P7/Q3 THE BOUNDED CEILING AT THE DEEPEST RANGE")
    print(f"S5 {head} -- N = {n}")
    pop = ceiling_at(n)
    for (popname, lab), g in sorted(pop.items()):
        print(f"  {popname:10s} {lab:6s} cells {g['n']:4d}  "
              f"max peak {g['peak']:2d} at {g['peak_at']}  "
              f"max run {g['longest']:2d} at {g['long_at']}  "
              f"edge-open {len(g['open']):3d}")
    print("  (longest run, peak) histograms:")
    for (popname, lab), g in sorted(pop.items()):
        row = " ".join(f"{k}x{v}" for k, v in sorted(g["hist"].items()))
        print(f"    {popname:10s} {lab:6s}: {row}")
    bnd = {p: g for (p, lab), g in pop.items() if lab == "bnd"}
    if control:
        bad = 0
        for popname, (cells, (run, peak), how) in sorted(CONTROL.items()):
            g = bnd.get(popname)
            got = (g["n"], (g["longest"], g["peak"])) if g else None
            ok = bool(g) and g["n"] == cells and (
                (g["longest"], g["peak"]) == (run, peak) if how == "=="
                else g["longest"] <= run and g["peak"] <= peak)
            bad += not ok
            print(f"  {popname:10s} expected {cells} cells, ceiling {how} "
                  f"{(run, peak)}; got {got}: {'OK' if ok else 'MISMATCH'}")
        print(f"  S5 CONTROL: {bad} populations disagree -- "
              + ("GREEN" if not bad else "RED, P7 is not read"))
        return
    print("  Q3 THE EDGE-OPEN BOUNDED COLUMNS -- the only ones a run bound"
          " does not cap (D6):")
    for popname, g in sorted(bnd.items()):
        capped = "  (deepest 8 by peak listed)" if len(g["open"]) > 8 else ""
        print(f"    {popname:10s} open {len(g['open']):3d}  "
              f"max peak among them {g['open_peak']:2d} at {g['open_at']}"
              f"{capped}")
        for key, pk, ln in sorted(g["open"], key=lambda x: -x[1])[:8]:
            print(f"      {key} peak {pk} run {ln}")
    cmax_peak = max(g["peak"] for g in bnd.values())
    cmax_run = max(g["longest"] for g in bnd.values())
    cells = sum(g["n"] for g in bnd.values())
    print(f"  P7 THE BOUNDED CEILING AT N = {n}: over {cells} trusted-bounded"
          f" columns, max peak {cmax_peak}, max run {cmax_run},"
          f" against C_MAX = {C_MAX}")
    print("  P7 " + ("HOLDS -- the calibrated ceiling of 6 stays one past"
                     " every trusted bounded peak"
                     if cmax_peak <= 5 else
                     "FAILS -- a bounded column reaches 6 or more"))


STAGES = {}


def s2_then_s34():
    store = s2_spectra()
    s3_s4_aperiodic_and_twins(store)


STAGES["s1"] = s1_vacuity
STAGES["s2"] = s2_then_s34
STAGES["s5c"] = lambda: s5_report(CONTROL_RANGE, control=True)
STAGES["s5"] = lambda: s5_report(DEEPEST_RANGE, control=False)


if __name__ == "__main__":
    for name in (sys.argv[1:] or ["s1", "s2"]):
        STAGES[name]()
