"""What plays the period at a window that has none, asked of the one
instrument the corpus trusts: the PREFIX CLOSURES, read for
stabilization.

THE QUESTION
------------
At a trailing Ostrowski window the stride-r shift's limit verdict is
settled wherever the window is purely periodic: a finite carry
automaton decides the limit column c_inf exactly, cell by cell
(explore_limit_column.py D1-D5). At the two aperiodic windows on
record the verdicts -- cbrt(2)-1 gated at r = 1, 3, 5 and bounded at
2, 4, 6, 7, 8; e-2 gated at 1, 4, 7, bounded at 2, 5, 8, delay-0 at
3, 6 -- stand at three ranges but rest on a finite-range classifier
with no fixed point in the range set or the instrument cap
(explore_cascade_rule.py H1, explore_cascade_scale.py H5), and the
run-length rule is not entitled to any scale there
(explore_cascade_scale.py H6). What is known about the law itself is
negative and exact: the verdict is a function of neither the drop
sites' positions (explore_cascade_span.py F4) nor their cap values nor
any statistic over the cap pairs (explore_cascade_roof.py H2 -- two
strides of e-2 carry identical drop multisets and opposite verdicts),
so only the absorbing environment is left.

THE CANDIDATE. For a window with quotients a_1, a_2, ... let the m-th
closure be w_m = [0; (a_1 .. a_m)^inf] -- the window's own prefix,
tiled. Every closure is purely periodic, so the automaton decides it
exactly. The candidate quantity is the EVENTUAL VERDICT of the
closure sequence at stride r, where that sequence stabilizes in m. On
a window whose quotients are themselves periodic with period P, every
closure at m a multiple of P IS the window, so the candidate reduces
to the settled periodic law -- in particular to the parity of r mod P
on the one-class family -- by construction, not by fit.

MARKED TRANSPLANT: the automaton, and the word "period", are the
periodic storey's machinery, imported here as an INSTRUMENT. The
quantity read off it is a property of the aperiodic window's own
quotient prefix. Nothing in the slate assumes the aperiodic verdict is
itself "periodic" in any sense; whether the closure sequence
stabilizes at all is one of the frozen forks.

THE HAND-ATTACK (pre-engine, on paper; the naive candidate DIES here
and the death shapes the design).

Every closure has a SEAM: the tiling wraps a_m onto a_1, and where a
late cap is larger than an early one the wrap manufactures drop sites
-- a_j > a_{j+r} read cyclically -- that the true window never has.
At e-2 (quotients 1, 2, 1, 1, 4, 1, 1, 6, ...: caps grow along one
residue class mod 3) the true window has NO drop site at any stride
r = 0 mod 3, and those strides are measured delay-0. But the closure
at m = 6 is, up to rotation, the graded window [1, 1, A, 1, 1, B]
with (A, B) = (2, 4), whose half-period cell r = 3 GATES at every
unequal pair in the limit (explore_limit_column.py L3-L4, exact). So
the bare "closure verdict" candidate is dead at e-2's r = 3 before
any engine -- killed exactly at the DROPLESS strides, by drops the
closure itself created. The candidate that survives the paper is
COMPOSITE:

    verdict(r) = DELAY-0  if the true window has no drop site at
                 stride r (read from the certified quotients);
    verdict(r) = the stabilized closure verdict  otherwise.

The first clause is trivial where it fires (no drop site means no
repair ever fires and the shift is the bare coordinate map, the
recorded delay-0 mechanism); at cbrt(2)-1 it never fires -- the
certified sequence has drop sites at every stride 1..8 -- so at the
cubic the closures decide everything.

THE VOCABULARY (fixed before any engine).
  CLOSURE w_m. The purely periodic window whose period is the first m
  quotients of the target window. Its first-digit cap is the target's
  own a_1 at every m.
  SEAM DROP. A drop site of w_m that is not a drop site of the true
  window at the same residue -- present because the tiling wraps.
  VERDICT of a cell (w_m, r), off the exact limit column: GATED if
  c_inf is infinite from some depth; DELAY-0 if the column is
  identically 0; BOUNDED otherwise (a finite never-vanishing sawtooth
  is BOUNDED -- the run-length rule's limit reading).
  STABLE AT THE SCANNED SCOPE. The verdict vector over r = 1..8 is
  identical at the top five computed closures (refusals excluded).

PREDICTIONS, FIXED BEFORE THE RUN (as observables)
  Q1 (positive control -- the reduction) at the golden window, and at
      the one-class designed windows (P, A) = (3, 2), (4, 2), (5, 3),
      every cell r = 1..2P prints the instrument's recorded residue
      law: r = 0 mod P delay-0, r mod P even and nonzero FINITE (a
      zero column is a sub-case there, per the instrument's own
      recorded run), r mod P odd gated. KILL: any cell off -- the
      instrument is miswired and nothing below is a measurement.
  Q2 (the calibration window) at e-2's class-preserving closures
      m = 6, 9, 12, 15: every cell with r in {1, 2, 4, 5, 7, 8}
      prints e-2's side of the gated/not-gated SPLIT -- gated at
      r = 1 mod 3, not gated at r = 2 mod 3 -- at every such m; the
      split is what the standing tables assert, their "bounded"
      including zero columns. KILL of the
      CANDIDATE: any such cell differing at two consecutive
      class-preserving m; the composite candidate then fails at the
      one aperiodic window whose law is independently known, and the
      cubic leg reads as instrument output only, not as a law.
  Q3 (the seam clause is real, not a story) at every class-preserving
      closure of e-2, each cell with r = 0 mod 3 and r not = 0 mod m
      carries at least one seam drop (census printed from the
      quotients alone) and reads GATED; r = 0 mod m reads DELAY-0
      (the proved period stride). KILL: such a cell reading
      otherwise -- the seam reading of the paper death is wrong and
      the composite split (dropless vs stabilized-closure) is
      unsupported.
  Q4 (the target -- the fork, no direction frozen) at cbrt(2)-1,
      closures m = 4..16, 18, 20, 23, 26, 30 at r = 1..8. The two
      observables:
      (a) whether the verdict vector is STABLE AT THE SCANNED SCOPE;
      (b) where stable, its agreement with the standing table, per
      stride. The three exits are all findings and are weighed after
      the run: stable and agreeing -- the quantity exists and the
      standing table gains its third instrument; stable and
      disagreeing, with Q2 green -- an exact instrument against a
      retired classifier, evidence the TABLE is the artifact;
      unstable -- the tail decides, and nothing finite plays the
      period at the criterion level either, completing
      explore_cascade_scale.py H6's negative answer for the run.
  Q5 (cross-instrument control) on every cell where the finite engine
      is run alongside (e-2 closures m = 6, 9; cubic closures
      m = 6, 12, 18, 23), the engine's column at range 30000 sits at
      or below the limit column at every depth. KILL: any violation
      -- the box or the automaton is wrong, run void.
  Q6 (the peak reading; added after the first recorded pass printed
      its verdict vectors and frozen before the extended ladder ran).
      The first pass showed the deep cubic closures turning the
      standing GATED strides into BOUNDED cells whose columns are
      sawtooths with peaks near the period itself -- a closure of
      period m cannot hold a column higher than what one period
      carries, so gating should surface in m as PEAK DIVERGENCE
      rather than as a per-m verdict. Frozen for the extended ladder
      (e-2 to m = 21, cubic to m = 30): at every stride the standing
      table GATES, the closure peak sequence over the deep ladder is
      unbounded-trending -- new highs keep arriving, gated cells
      counted as new highs -- and at every stride it does not gate,
      the peak sequence is bounded: no new high above the band the
      shallow ladder already printed. KILL, either direction: a
      standing-bounded stride printing ever-higher peaks, or a
      standing-gated stride whose peaks stall at a constant over the
      deep half of the ladder.
  Q7 (the witness transfer; added after the extended ladder printed
      and frozen before S4 ran). Some closures GATE a stride the
      standing table calls bounded. A gating cell hands out concrete
      witness pairs (explore_limit_column.py's witness walker), and
      the walker verifies whatever it builds against the numeration
      it is HANDED: passed the TRUE window's certified numeration, a
      pair that passes its greedy asserts is a true-window instance
      -- two explicit integers whose digit strings agree from the
      bottom to the printed depth while their stride-r images part at
      the printed position -- however it was found; a pair the seam
      corrupted fails the asserts and reports as a MISS. Frozen
      observables, one per window: at e-2, whose bounded strides
      r = 2, 5, 8 follow from the one-class parity derivation, NO
      extracted pair verifies -- a verified one would be a true
      instance against that derivation's own strides and the
      extraction would be transferring seam artifacts, voiding the
      cubic reading. At the cubic, any verified pair at a standing-
      bounded stride is a true-window instance with agreement beyond
      the classifier's whole recorded band (its bounded columns top
      at 3): the recorded table's bounded half is then a truncation
      artifact as a statement about those depths. KILL of the LEG:
      e-2 verifying, or every cubic candidate missing -- the closure
      evidence then stays closure-side and the exit is Q6's pattern
      alone. A pair only counts if its MARGIN -- input agreement
      minus the position where the recomputed true-window images
      part -- is positive; a greedy-verified pair whose images part
      above its agreement says nothing (any two integers' images part
      near where the integers do), and S4's first rehearsal printed
      exactly such pairs, which is why the margin is in the print.
  Q8 (the gated-stride harvest; added after S4's rehearsal printed
      and frozen before the recorded run). The deep closures' gates
      land only on the strides the standing table GATES. A witness
      from such a cell, greedy-verified on the true window WITH
      POSITIVE MARGIN, is a certified true-window instance at that
      stride -- two explicit integers agreeing that deep whose images
      part that low -- and each extra cycle turn that still verifies
      is an independent, deeper instance. Frozen observable: which
      cells and turns verify with positive margin, at both windows;
      every such hit upgrades a piece of the standing tables' gated
      half from classifier output to certified instances. KILL of the
      READING: zero positive-margin hits anywhere -- the transfer
      never carries content and S4 is instrument-side only.

THE DESIGN
----------
Window, Shift, limit_column, run_peak, show_col and the finite-column
control are IMPORTED from explore_limit_column.py; the certified
quotient sequences and the designed family from
explore_shift_repair.py. Nothing about the automaton is rewritten --
which is what makes Q1 and Q5 controls of this rig's wiring rather
than of the instrument's. One thing had to be re-founded: the parent
Window computes alpha in double precision and theta_phi by float
cancellation, which reaches exactly 0.0 once a convergent denominator
outruns the double mantissa -- at the cubic's closures, period 18.
PrecWindow carries alpha at 160 decimal digits (Newton on the
period's own quadratic from the exact deep-convergent seed, the
conjugate as the exact root sum minus alpha, box ratios handed back
as floats), inherits every automaton step unchanged, and is used at
EVERY cell. Its control is S0's twin check: on windows the float
instrument can reach, both instruments must print identical verdict,
state count and limit column.

S0  CONTROLS. The golden and one-class designed cells, verdicts
    against the recorded law. Q1's observable.
S1  E-2 CLOSURES. m = 3..15, r = 1..8: verdict, seam-drop census
    (total sites and large-onto-large sites per period, from the
    quotients alone), and the class-preserving rows read against
    Q2/Q3. The m not = 0 mod 3 rows carry no prediction and are
    printed for which m-subsequences stabilize at all.
S2  CUBIC CLOSURES. m = 4..16, 18, 20, 23, r = 1..8, ascending in m
    so a late blowup costs nothing earlier: verdict and seam census
    per cell, each cell's states/pairs/wall printed. A cell whose
    automaton exceeds the frozen state ceiling is REFUSED and printed
    as such -- the instrument's reach is data, not an error.
S3  ASSEMBLY. The true-window drop census per stride (certified
    quotients, sites j <= 60), the composite verdict table beside the
    standing tables, the stability read at the scanned scope, and
    Q6's peak matrices.
S4  WITNESS TRANSFER. At closure cells that GATE (chosen off S2's
    printed matrix -- standing-bounded strides for Q7, standing-gated
    for Q8), the witness walker run with the TRUE window's certified
    numeration at four cycle counts; each result printed with its
    integers, depths and MARGIN, or MISS. Q7's and Q8's observable.

STATE_CEIL = 60000 states. RESOURCE: estimate 10-25 min wall,
dominated by the deep cubic closures (period up to 23, caps to 14);
bounded, expected under 512MB but unproven at the deep cells, so the
run goes through memwatch at the default ceiling; stages print as
they complete so a late kill keeps the early legs. Nothing cheaper
decides the cubic leg: the classifier is retired, the run-length rule
is not entitled to a scale there, and the automaton is exact only
per-window, which is what the closure ladder is for.

RUN RECORD
----------
Recorded run: wall 33.8 s, peak working set 39.4 MB under memwatch's
512 MB ceiling; every cell decided, none refused, none near the state
ceiling. The estimate was tenfold conservative: the deepest cell runs
in 0.2 s. Four passes shaped the rig before anything was recorded:
  (1) The first pass stopped itself at S0 RED: Q1 had been frozen in
      the finite classifier's vocabulary -- "even nonzero residue =
      bounded" -- where the instrument's own recorded law makes a
      zero column a sub-case of finite at those cells. The control
      fired before any measurement, the expectation was re-frozen to
      the recorded law, and every agreement comparison was moved to
      the gated/not-gated split the standing tables actually assert.
  (2) The second pass died at cubic m = 18: the parent Window's float
      theta underflows to exactly 0.0 there. PrecWindow replaced it
      everywhere and the twin control entered S0.
  (3) Q6 was frozen after that pass's verdict vectors printed and
      before the extended ladder ran; the ladder grew to m = 21 and
      m = 30.
  (4) S4's first rehearsal printed margin-free "VERIFIED" lines whose
      images part ABOVE their agreement -- content-free pairs. The
      margin entered the print, and the gated-stride harvest (Q8) was
      frozen before the recorded run.
Controls in the recorded run: S0 green -- 27 reduction cells exact,
float and 160-digit instruments identical over 16 twin cells; 48 of
48 finite-engine-vs-limit checks OK; zero reconstruction or legality
failures anywhere.

FINDINGS (each at its own tier)
-------------------------------
C1  THE CONTROLS ARE GREEN AND THE INSTRUMENT REACHES EVERY CELL
    (Q1, Q5). The reduction is exact at the golden and the three
    one-class designed windows; the 160-digit and float instruments
    agree cell-for-cell where floats reach; the finite engine's
    column sits at or below the limit column at all 48 cells checked.
    Nothing was refused: the closure ladder to period 30 with caps to
    14 runs in under a second per cell, states peaking in the
    hundreds.
C2  THE COMPOSITE CANDIDATE CALLS THE CALIBRATION WINDOW WHOLE, AND
    THE SEAM WASHES OUT (rule at scanned scope; Q2 lands, Q3's kill
    fires in the direction that helps). At e-2 the closure verdict
    vector is G b b G b b G b -- gated 1, 4, 7 -- at EVERY m from 12
    through 21, ten consecutive closures, class-preserving or not,
    and the dropless clause reads r = 3, 6 (zero drop sites at
    j <= 60) as delay-0: the standing table at all eight strides,
    from an exact instrument plus one certified census. The seam
    drops the paper predicted to gate forever gate only while they
    dominate the period -- r = 3 gates at m = 4..8 and reads bounded
    from m = 9 on, r = 6 likewise from m = 10 -- so the closures
    converge to the true window's SPLIT even at the strides the seam
    corrupts, and the composite clause is needed for the fine verdict
    (delay-0 against a low bounded sawtooth), not for the split.
C3  THE PEAK SEPARATES E-2'S SPLIT AS CLEANLY AS THE VERDICT DOES
    (rule at scanned scope; Q6's e-2 half). Over the whole ladder to
    m = 21 the standing-gated strides print outright gates at every
    deep closure while the standing-bounded strides' peaks stay
    inside a band of 7 with no new high past m = 19 -- two
    independent readings of one split.
C4  E-2'S GATED HALF NOW CARRIES CERTIFIED INTEGER LADDERS (verified
    instances; Q8 lands). From deep class-preserving closures the
    walker hands out pairs that verify by pure integer arithmetic on
    the true window's certified numeration, with the parting position
    FIXED while agreement climbs with the cycle count: at r = 1,
    images part at position 1 with input agreement 13, 25, 37, 49
    (m = 12) and 31, 61, 91, 121 (m = 15); at r = 4, part 3 with the
    same agreement ladders; at r = 7, part 6 with agreement to 169
    (m = 21, integers of 108 and 110 digits). Every rung is an
    independently verified fact -- two explicit integers agreeing on
    that many bottom digits whose stride-r images part that low -- so
    the gated half of e-2's table rests on the one-class parity
    derivation plus exact certificates at depths no finite-range
    engine reached, with the retired classifier no longer load-bearing
    there.
C5  THE CUBIC REFUSES THE CLOSURE INSTRUMENT ON EVERY OBSERVABLE IT
    OFFERS (rule at scanned scope; Q4 exits at its third fork, Q6's
    kill fires both ways, Q7 exits by its kill). (a) The verdict
    vector never stabilizes: r = 3 and r = 5 flip through the deep
    ladder, and r = 1 -- three-range GATED on record -- prints bounded
    at all five of the ladder's deep rungs, m = 18 through 30. (b) The peak reading
    separates nothing: the standing-bounded strides keep printing new
    highs through the deep ladder (r = 2 reaches 15 at m = 26, r = 4
    reaches 19 there, r = 6 reaches 23 at m = 30, r = 7 reaches 16)
    exactly as the standing-gated ones do, every stride alike where
    e-2 shows a clean band. (c) The deep closures' outright gates
    land only on standing-gated strides -- r = 3 and r = 5 own every
    star from m = 18 on -- which is the one closure-side signal that
    tracks the standing split, and it is a signal about two strides.
    (d) No witness transfers: the cubic's closure gates live in
    wrapped positions, and every extracted pair either fails
    greedy-ness on the true window or re-agrees there -- margins top
    at +1 (r = 1, m = 14, turns 4; r = 3, m = 26, turns 1) with the
    parting position climbing alongside the agreement, against e-2's
    fixed-part ladders. So the closure sequence at the cubic carries
    no stable signal, transfers no certificate, and cannot be the
    third instrument its table is owed.
C6  WHAT PLAYS THE PERIOD, ANSWERED PER WINDOW (synthesis of C2-C5
    with the record). At a window whose largeness structure is
    one-class, the ONE-CLASS STRUCTURE plays it: the parity
    derivation, the closure stabilization, the peak band and the
    certified ladders all read the same split, and the composite
    candidate is the aperiodic law there -- reducing to the parity of
    r mod P on the one-class family by construction. At the cubic
    NOTHING scanned plays it: the criterion generation died at the
    drop sites (explore_cascade_span.py, explore_cascade_roof.py),
    the run generation had no scale it was entitled to
    (explore_cascade_scale.py H6), and the limit generation decides
    every closure exactly and finds the sequence of exact answers
    carries no stable signal. The cubic's standing table remains the
    retired classifier's three-range reading with its depth ceiling
    of 12 -- its gated half untouched by this rig's failures to
    transfer, its bounded half still without any exact instrument --
    and the question stays open with its price now measured at three
    instrument generations.
"""

import decimal
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_shift_repair import (          # noqa: E402
    build_q_positions,
    designed,
    quotients_cbrt2_minus_1,
    quotients_e_minus_2,
)
from explore_limit_column import (          # noqa: E402
    INF,
    Shift,
    Window,
    finite_column,
    limit_column,
    run_peak,
    show_col,
    witness,
)

STATE_CEIL = 60_000
CERT_WANT = 80
CENSUS_J = 60

decimal.getcontext().prec = 160


class PrecWindow(Window):
    """Window with alpha carried at 160 decimal digits.

    The parent computes alpha as a float root of the period's quadratic
    and theta_phi = q_phi alpha - p_phi by float cancellation, which
    underflows to exactly 0.0 once q_phi outruns double precision --
    at the cubic's closures that is period 18 and up. Same quadratic,
    same lattice data, but alpha is refined by Newton in Decimal from
    the exact deep-convergent seed, the conjugate root is the exact
    root sum minus alpha, and box() hands back floats of ratios that
    are themselves moderate. Everything downstream is inherited
    unchanged."""

    def __init__(self, caps, period):
        P = period
        self.P = P
        self.a = list(caps[:P])
        assert all(caps[k] == self.a[k % P]
                   for k in range(min(len(caps), 6 * P)))
        q = {-1: 0, 0: 1}
        p = {-1: 1, 0: 0}
        for k in range(1, 3 * P + 1):
            ak = self.a[(k - 1) % P]
            q[k] = ak * q[k - 1] + q[k - 2]
            p[k] = ak * p[k - 1] + p[k - 2]
        self.q, self.p = q, p
        A2, A1, A0 = q[P - 1], q[P] - p[P - 1], -p[P]
        # exact deep-convergent seed, then Newton in Decimal
        pk2, pk1 = 1, 0
        qq2, qq1 = 0, 1
        for k in range(1, 61):
            ak = caps[k - 1]
            pk2, pk1 = pk1, ak * pk1 + pk2
            qq2, qq1 = qq1, ak * qq1 + qq2
        x = decimal.Decimal(pk1) / decimal.Decimal(qq1)
        for _ in range(200):
            fx = (A2 * x + A1) * x + A0
            dfx = 2 * A2 * x + A1
            step = fx / dfx
            x = x - step
            if abs(step) < decimal.Decimal(10) ** -150:
                break
        self.alpha = x
        self.alpha_c = -decimal.Decimal(A1) / A2 - x
        resid = (A2 * self.alpha + A1) * self.alpha + A0
        assert abs(resid) < decimal.Decimal(10) ** -120, resid
        assert abs(self.alpha - decimal.Decimal(pk1) / qq1) < \
            decimal.Decimal(1) / qq1
        self.H = ((p[P - 1], -p[P]), (-q[P - 1], q[P]))
        det = self.H[0][0] * self.H[1][1] - self.H[0][1] * self.H[1][0]
        assert det in (1, -1)
        self.Hinv = ((det * q[P], det * p[P]),
                     (det * q[P - 1], det * p[P - 1]))
        self.eta = p[P - 1] - q[P - 1] * self.alpha
        self.eta_c = p[P - 1] - q[P - 1] * self.alpha_c
        assert abs(self.eta) < 1 < abs(self.eta_c)
        self.th = {phi: (-p[phi], q[phi]) for phi in range(-1, P)}
        self.thf = {phi: q[phi] * self.alpha - p[phi]
                    for phi in range(-1, P)}
        self.thc = {phi: q[phi] * self.alpha_c - p[phi]
                    for phi in range(-1, P)}
        assert all(self.thf[phi] != 0 for phi in range(-1, P))

    def box(self, amax):
        real, conj = Window.box(self, amax)
        return ({k: float(v) for k, v in real.items()},
                {k: float(v) for k, v in conj.items()})


# ------------------------------------------------------------- helpers

def tile(prefix, m, want=None):
    """The closure's cap list: the first m quotients, tiled."""
    if want is None:
        want = max(6 * m, 70)
    return [prefix[k % m] for k in range(want)]


def verdict_of(lc):
    if lc["inf_from"] is not None:
        return "GATED"
    if all(c == 0 for c in lc["col"]):
        return "delay-0"
    return "bounded"


def seam_census(prefix, m, r):
    """Drop sites of w_m over one period, read cyclically, and which of
    them are seam drops (not drops of the true window at the same j)."""
    total = lol = seam = 0
    for j in range(m):
        cap_src = prefix[j]
        cap_dst = prefix[(j + r) % m]
        if cap_src > cap_dst:
            total += 1
            if cap_dst >= 2:
                lol += 1
            if j + r < len(prefix) and not (prefix[j] > prefix[j + r]):
                seam += 1
            elif j + r >= len(prefix):
                seam += 1
    return total, lol, seam


def true_census(prefix, r, jmax=CENSUS_J):
    """Drop sites of the true window at stride r, j <= jmax."""
    sites = [j for j in range(min(jmax + 1, len(prefix) - r))
             if prefix[j] > prefix[j + r]]
    return sites


def read_closure(name, prefix, m, r, check_finite=False):
    """One cell: build, decide, print. Returns the verdict or REFUSED."""
    caps = tile(prefix, m)
    t0 = time.time()
    win = PrecWindow(caps, m)
    sh = Shift(win, r)
    if len(sh.states) > STATE_CEIL:
        print(f"  {name} m {m:2d} r {r}: REFUSED "
              f"(states {len(sh.states)} > {STATE_CEIL})")
        return dict(v="REFUSED", peak=None)
    lc = limit_column(sh)
    wall = time.time() - t0
    v = verdict_of(lc)
    tot, lol, seam = seam_census(prefix, m, r)
    fin = ""
    if check_finite:
        fcol, _rep = finite_column(caps, m, r)
        ok = True
        if lc["inf_from"] is None:
            ext = lc["col"][:]
            while len(ext) <= len(fcol) + 1:
                ext.append(ext[lc["pre"] + (len(ext) - lc["pre"])
                               % lc["per"]])
            ok = all(fcol[t - 1] <= ext[t] for t in range(1, len(fcol) + 1))
        else:
            ok = all(fcol[t - 1] <= lc["col"][t]
                     if t < len(lc["col"]) else True
                     for t in range(1, len(fcol) + 1))
        fin = f"  finite<=limit {'OK' if ok else 'VIOLATED'}"
    _run, peak = run_peak(lc)
    print(f"  {name} m {m:2d} r {r}: {v:7s} drops/period {tot} "
          f"(lol {lol}, seam {seam})  states {len(sh.states):5d} "
          f"pairs {lc['pairs']:7d} wall {wall:5.1f}s{fin}")
    print(f"      c_inf: {show_col(lc)}")
    return dict(v=v, peak=peak)


# ------------------------------------------------------------------ s0

def s0_controls():
    print("=" * 78)
    print("S0 CONTROLS: the reduction -- one-class windows print the"
          " parity law (Q1)")
    ok = True
    cells = [("golden", [1] * 70, 1, (1, 2, 3))]
    for P, A in ((3, 2), (4, 2), (5, 3)):
        cells.append((f"designed({P},{A})", designed(P, A, 70), P,
                      tuple(range(1, 2 * P + 1))))
    for name, caps, P, rs in cells:
        for r in rs:
            win = PrecWindow(caps, P)
            sh = Shift(win, r)
            lc = limit_column(sh)
            v = verdict_of(lc)
            if P == 1 or r % P == 0:
                want = "delay-0"
                good = (v == "delay-0")
            elif (r % P) % 2 == 0:
                want = "finite"
                good = (v != "GATED")
            else:
                want = "GATED"
                good = (v == "GATED")
            ok &= good
            print(f"  {name} r {r}: {v:7s} want {want:7s} "
                  f"{'ok' if good else 'MISS'}")
    # twin check: PrecWindow against the float Window where floats reach
    e2 = quotients_e_minus_2(CERT_WANT)
    cub = quotients_cbrt2_minus_1(CERT_WANT)
    twins = [("e-2 m6", tile(e2, 6), 6), ("cubic m10", tile(cub, 10), 10)]
    for name, caps, P in twins:
        for r in range(1, 9):
            lcs = []
            for cls in (Window, PrecWindow):
                sh = Shift(cls(caps, P), r)
                lc = limit_column(sh)
                lcs.append((verdict_of(lc), len(sh.states), lc["col"]))
            same = lcs[0] == lcs[1]
            ok &= same
            if not same:
                print(f"  twin {name} r {r}: float vs prec DIFFER")
        print(f"  twin {name}: float and 160-digit instruments "
              f"{'identical over r = 1..8' if ok else 'DIFFER'}")
    print(f"S0 {'GREEN' if ok else 'RED -- RUN VOID'}")
    return ok


# ------------------------------------------------------------------ s1

def s1_e2():
    print("=" * 78)
    print("S1 E-2 CLOSURES: m = 3..21, r = 1..8 (Q2, Q3, Q6)")
    prefix = quotients_e_minus_2(CERT_WANT)
    table = {}
    for m in range(3, 22):
        for r in range(1, 9):
            table[(m, r)] = read_closure("e-2", prefix, m, r,
                                         check_finite=(m in (6, 9)))
    print("-" * 78)
    print("e-2 closure verdict vectors (rows m, cols r = 1..8):")
    for m in range(3, 22):
        row = " ".join({"GATED": "G", "bounded": "b", "delay-0": ".",
                        "REFUSED": "?"}[table[(m, r)]["v"]]
                       for r in range(1, 9))
        tag = "  <- class-preserving" if m % 3 == 0 else ""
        print(f"  m {m:2d}: {row}{tag}")
    return table


# ------------------------------------------------------------------ s2

def s2_cubic():
    print("=" * 78)
    print("S2 CUBIC CLOSURES: m = 4..16, 18, 20, 23, 26, 30, r = 1..8"
          " (Q4, Q6)")
    prefix = quotients_cbrt2_minus_1(CERT_WANT)
    table = {}
    ms = list(range(4, 17)) + [18, 20, 23, 26, 30]
    for m in ms:
        for r in range(1, 9):
            table[(m, r)] = read_closure("cubic", prefix, m, r,
                                         check_finite=(m in (6, 12, 18,
                                                             23)))
    print("-" * 78)
    print("cubic closure verdict vectors (rows m, cols r = 1..8):")
    for m in ms:
        row = " ".join({"GATED": "G", "bounded": "b", "delay-0": ".",
                        "REFUSED": "?"}[table[(m, r)]["v"]]
                       for r in range(1, 9))
        print(f"  m {m:2d}: {row}")
    return table, ms


# ------------------------------------------------------------------ s3

def s3_assembly(e2_table, cubic_table, cubic_ms):
    print("=" * 78)
    print("S3 ASSEMBLY: the true-window censuses, the composite table,"
          " the stability read")
    cub = quotients_cbrt2_minus_1(CERT_WANT)
    e2 = quotients_e_minus_2(CERT_WANT)
    print("true-window drop sites, j <= 60:")
    for name, prefix in (("cubic", cub), ("e-2", e2)):
        for r in range(1, 9):
            sites = true_census(prefix, r)
            print(f"  {name} r {r}: {len(sites)} sites"
                  + ("  (NONE -> composite clause: delay-0)"
                     if not sites else ""))
    standing = {"cubic": {1: "GATED", 2: "bounded", 3: "GATED",
                          4: "bounded", 5: "GATED", 6: "bounded",
                          7: "bounded", 8: "bounded"},
                "e-2": {1: "GATED", 2: "bounded", 3: "delay-0",
                        4: "GATED", 5: "bounded", 6: "delay-0",
                        7: "GATED", 8: "bounded"}}
    print("-" * 78)
    print("stability at the scanned scope (top five computed closures)"
          " and the composite call:")
    for name, prefix, table, ms in (
            ("e-2", e2, e2_table, list(range(3, 22))),
            ("cubic", cub, cubic_table, cubic_ms)):
        print(f"{name}:")
        for r in range(1, 9):
            col = [(m, table[(m, r)]["v"]) for m in ms
                   if table[(m, r)]["v"] != "REFUSED"]
            top = col[-5:]
            vals = {v for _m, v in top}
            stable = len(vals) == 1
            closure_call = top[-1][1] if stable else "UNSTABLE"
            if not true_census(prefix, r):
                call = "delay-0 (dropless clause)"
            else:
                call = closure_call
            # the standing tables assert the gated/not-gated SPLIT
            # (their "bounded" includes delay-0 columns); compare there
            if call == "UNSTABLE":
                agree = "no call"
            else:
                call_gated = call.startswith("GATED")
                stand_gated = standing[name][r] == "GATED"
                agree = "agrees" if call_gated == stand_gated else "DIFFERS"
            print(f"  r {r}: top-5 {'stable' if stable else 'UNSTABLE'}"
                  f" -> call {call:26s} standing {standing[name][r]:7s}"
                  f" {agree}")
    print("-" * 78)
    print("Q6 peak matrices: the peak of the limit column per cell"
          " ('*' = gated at that m); the reading under test is that a"
          " stride the true window GATES has closure peaks growing"
          " without bound in m, and a stride it does not has them"
          " bounded:")
    for name, prefix, table, ms in (
            ("e-2", e2, e2_table, list(range(3, 22))),
            ("cubic", cub, cubic_table, cubic_ms)):
        print(f"{name} (rows m, cols r = 1..8; standing gated strides"
              f" marked):")
        marks = "".join(" G" if standing[name][r] == "GATED" else "  "
                        for r in range(1, 9))
        print(f"        {marks}")
        for m in ms:
            cells = []
            for r in range(1, 9):
                e = table[(m, r)]
                if e["v"] == "REFUSED":
                    cells.append("  ?")
                elif e["v"] == "GATED":
                    cells.append("  *")
                else:
                    cells.append(f"{e['peak']:3d}")
            print(f"  m {m:2d}: {''.join(cells)}")


def s4_witnesses():
    print("=" * 78)
    print("S4 WITNESS TRANSFER: pairs from gated closure cells verified"
          " on the TRUE window's certified numeration -- bounded-stride"
          " cells are Q7's, gated-stride cells Q8's")
    plans = [
        ("e-2", quotients_e_minus_2, 200,
         [("bounded-stride", (4, 5), (7, 5), (5, 8), (7, 8)),
          ("gated-stride", (12, 1), (15, 1), (12, 4), (15, 4),
           (15, 7), (18, 7), (21, 7))]),
        ("cubic", quotients_cbrt2_minus_1, 200,
         [("bounded-stride", (6, 4), (9, 4), (8, 6), (11, 6),
           (14, 7), (16, 7), (13, 8), (16, 8)),
          ("gated-stride", (14, 1), (16, 1), (18, 3), (26, 3),
           (20, 5), (30, 5))]),
    ]
    for name, qfun, qwant, groups in plans:
        prefix = qfun(qwant)
        qtrue = build_q_positions(list(prefix), qwant - 10)
        cells = [(m, r, g[0]) for g in groups for (m, r) in g[1:]]
        for m, r, tag in cells:
            caps = tile(prefix, m)
            sh = Shift(PrecWindow(caps, m), r)
            lc = limit_column(sh)
            if lc["inf_from"] is None:
                print(f"  {name} {tag} m {m:2d} r {r}: cell not gated"
                      f" here -- skipped")
                continue
            t = lc["inf_from"]
            for turns in (1, 2, 3, 4):
                got = None
                for tt in range(t, t + 7):
                    try:
                        got = witness(sh, tt, turns, qtrue)
                    except AssertionError:
                        got = "MISS"
                    if got is not None:
                        break
                if got is None:
                    print(f"  {name} {tag} m {m:2d} r {r} turns"
                          f" {turns}: no parted infinite pair near"
                          f" t = {t}")
                elif got == "MISS":
                    print(f"  {name} {tag} m {m:2d} r {r} turns"
                          f" {turns}: MISS -- pair not greedy on the"
                          f" true window")
                else:
                    n1, n2, agree, diff, cyc = got
                    inst = agree - diff
                    big = max(n1, n2)
                    show = (f"n1 {n1} n2 {n2}" if big < 10 ** 60
                            else f"n1,n2 with {len(str(n1))},"
                                 f"{len(str(n2))} digits")
                    kind = ("POSITIVE INSTANCE" if inst > 0 else
                            "no instance (agreement below parting)")
                    print(f"  {name} {tag} m {m:2d} r {r} turns"
                          f" {turns}: greedy-verified, agree {agree}"
                          f" part {diff} margin {inst:+d} --> {kind}"
                          f" (cycle {cyc}; {show})")


if __name__ == "__main__":
    t0 = time.time()
    ok = s0_controls()
    if not ok:
        print("S0 RED: stopping -- nothing below is a measurement.")
        sys.exit(1)
    e2_table = s1_e2()
    cubic_table, cubic_ms = s2_cubic()
    s3_assembly(e2_table, cubic_table, cubic_ms)
    s4_witnesses()
    print(f"total wall {time.time() - t0:.1f}s")
