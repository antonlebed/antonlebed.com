"""The banking reader: if a throttled reader may SAVE unspent rank
budget in a bank and spend it later, does the optimal saving
schedule depend on the data? The second resource-bounded stage of
the reader-descent program.

THE QUESTION
------------
explore_throttled_reader.py established that under a rank budget of
B cover-rank units per input step the deficit landscape's optimum
stays ensemble-free: one universal policy (chain-first entry,
tree-first exit, greedy patience) sits in every row's argmin class
at every budget, so training data does not pick the destination.
That reader's budget is use-it-or-lose-it: unspent units evaporate
at the step boundary.

This experiment adds the natural store: a BANK of capacity W. Unspent
units deposit automatically (overflow above W is lost); banked units
may be drawn later, subject to a per-step drawdown ceiling — the one
new policy coordinate, a SAVING SCHEDULE. Saving before a demand
burst and spending through it is stream-shaped almost by definition,
so this is the first knob where the optimum SHOULD go
stream-dependent if it ever does. The questions:

  Q1  Does the optimal schedule depend on the stream ensemble — is
      a saving schedule the first learned object of this program?
  Q2  Where does banking move the catch-up thresholds (the least
      budget at which the throttled loss equals the unthrottled
      loss)?
  Q3  Does the deficit landscape stay a funnel under lexicographic
      descent plus the preference-diagonal move (the cure set
      established by explore_throttled_reader.py), and does the
      scarcity trap found there survive the bank?

THE POLICY SPACE, LOSS, AND SETTINGS
------------------------------------
Policies, covers, streams, maps, horizon, and the exact loss are
those of explore_throttled_reader.py: base coordinates (route
preference at tree cells, route preference at straddles, tree
patience, chain patience) over the patience axis {0, 1, 2, 3, INF};
the loss on a row is the product of committed cell lengths over
counted steps (N0 = 8, horizon 120), exact big-integer comparison
throughout; the slate is the same eight (map, stream) rows including
the wall row (x^2, sqrt2). Settings: budget B in {1, 2, 3, 4} (3 is
new — the mean-demand test income for the one row whose threshold
banking should move) crossed with cap W in {0, 2, 4, 8}.

BANKING SEMANTICS (frozen before the engine)
--------------------------------------------
Bank level b in [0, W]; the cap W is a SETTING like B (the cap is
physical, the schedule is policy). The bank starts EMPTY — no free
warm-up capital; warm-up (uncounted) steps may bank their surplus,
which is part of the object. Per input step:

  avail     = B + b
  spendable = min(avail, B + delta)     [delta = schedule coord]
  the commit loop runs with rem = spendable, chain candidates
  truncated to rem exactly as in explore_throttled_reader.py
  spent     = spendable - rem_final
  b'        = min(W, avail - spent)     [deposit automatic;
                                         overflow above W is LOST]

THE SCHEDULE COORDINATE delta is the per-step drawdown ceiling over
income: spend at most B + delta this step. delta = 0 never draws
the bank (banking inert by construction); delta = INF is spend-all
(draw whatever is needed); finite delta is a drip-feed drawdown.
A policy is (s_t, s_s, pt, pc, delta).

THE DEGENERACY QUOTIENT (design-time, not post-hoc). Two collapse
facts are provable by hand and build the space:
  (i)  delta >= W is behaviorally delta = INF exactly: spendable =
       min(B + b, B + delta) with b <= W <= delta always resolves
       to B + b. So the delta axis at cap W is
       {d in {0, 1, 2, 4} : d < W} + {INF}; at W = 0 the whole axis
       collapses to one class (b = 0 always) — the throttled reader
       verbatim, the embedded control, counted once.
  (ii) Wherever the bank is never drawn on a row (uniform demand at
       or above B, caught-up rows, empty-bank rows), the delta axis
       is behaviorally flat there. The engine therefore also
       quotients argmin classes by counted-window behavioral
       signature (the committed-cell trace over counted steps) and
       reports raw and quotiented sizes side by side.
A REJECTED COORDINATE, killed at design time by the same guard: a
reserve floor ("keep at least rho banked, spend only the surplus")
is behaviorally a cap reduction W -> W - rho plus a warm-up debt to
build a never-spent floor — dominated by and near-degenerate with a
smaller cap, so it never entered the space.

HAND-DERIVED BEFORE THE ENGINE
------------------------------
THE EAGER-SPEND EXCHANGE (why spend-all is hard to beat). Delaying
an affordable commit never obviously helps: references nest, so any
move available now remains available later; chain costs are
incremental (enter k now and deepen to k2 later costs k2 total,
the same as waiting, and the eager reader holds strictly narrower
cells in between); candidacy is budget-independent for rem >= 1, so
the schedule changes only when units flow, not what is offered; an
eager side exit from a deeper chain lands deeper. The ONE mechanism
that could break the exchange is route-locking: an early cheap
commit steering the preference-fixed route into a branch that later
blocks a better cell (under scarcity routes diverge into non-nested
cells). The exchange argument does not close at route junctures
whose candidate sets differ between the two trajectories, so
spend-all universality is a prediction, not a lemma — a row where a
finite delta strictly wins would be the route-locking discovery and
the first stream-dependent optimum candidate.

THE SMOOTHING ARITHMETIC (where banking can move a threshold at
all). Banking pays only through demand fluctuation around B:
surplus steps fund deficit steps. Per row, from the demand slopes
measured by explore_throttled_reader.py:
  - phi, sqrt2, theta8: uniform demand (1, 2, 8) — no fluctuation,
    banking inert in steady state, thresholds should stay 1, 2, 8.
  - sqrt3 (alternating ~1,2): at B = 1 the 1-steps carry zero
    surplus, so nothing funds the 2-steps — threshold stays 2.
  - sq/phi = phi^2 (leading digit 2, then uniform 1): the warm-up
    debt falls at the first step, when the bank is born empty, and
    demand = B = 1 thereafter leaves no surplus — stays 2. The
    bank-born-empty clause is load-bearing.
  - dbl/phi (mean 4/3): no surplus at B = 1 — stays 2.
  - dbl/sqrt2 (alternating ~1,4, mean 2.49, unthrottled-catch-up
    threshold 4): THE ONE MOVING ROW. At B = 3 the surplus of the
    1-steps covers the deficit of the 4-steps with a small bank —
    the threshold should drop 4 -> 3 at every scanned W >= 2. The
    exact minimal cap is left unclaimed (W = 1 is not scanned).
  - the wall (exponential demand): banking buys a transient only —
    no finite budget ever catches up.
Law shape: the banked threshold is at least the ceiling of the mean
demand, reached only when fluctuation is bounded and warm-up debt
is coverable by pre-burst surplus.

WARM-UP BANKING (flagged open, not frozen): rows whose greedy
reader waits during early steps (on theta8 the root's children
never strictly contain J_0, so the first move waits) have zero
demand there and bank their full income even at B = 1 — so B = 1
banking need not be inert everywhere, and the scarcity trap's
neighborhood may genuinely shift at W > 0. The engine prints
per-step demand minima; no prediction is frozen on this.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls, gate] (i) The banking reader at W = 0 reproduces the
   throttled reader exactly — identical loss triples on all 100
   base policies x 8 rows at every B in {1, 2, 3, 4}. (ii) The
   delta = 0 slice at every W > 0 reproduces the W = 0 tables
   exactly (never-draw = no bank). (iii) The excluded delta values
   reproduce delta = INF exactly (the collapse proof holds in the
   engine: sampled at the greedy quartet, all rows, all B, pairs
   (W=2, d=2), (W=2, d=4), (W=4, d=4)). (iv) The disease
   reproduces: plain single-move descent on the unthrottled slate
   stalls exactly at the greedy quartet plus the four refusal
   corners. (v) Demand slopes: id/phi in [0.9, 1.1], id/theta8 in
   [7, 9], dbl/phi partition slope in [1.26, 1.40], wall chain
   ln-k slope in [1.71, 1.82].
C2 [the smoothing law] The banked catch-up thresholds match the
   frozen table: phi 1, sqrt2 2, sqrt3 2, phi^2 2, dbl/phi 2 at
   every W; theta8 and the wall never catch up in the scanned
   budgets at any W; dbl/sqrt2 stays 4 at W = 0 and drops to 3 at
   every W in {2, 4, 8}. Banked loss never beats unthrottled.
   [Refuted twice — the two rows named as movers were both wrong
   ways round; see findings F2.]
C3 [THE PRINCIPAL QUESTION — the kill observable] delta = INF sits
   in every row's argmin class at every (B, W); stronger frozen
   form (the exchange argument): delta = INF is pointwise weakly
   optimal — at every fixed (s_t, s_s, pt, pc), row, and setting,
   no finite delta strictly beats it. The universal policy
   (chain-first entry, tree-first exit, greedy patience,
   spend-all) sits in every row's argmin class at every setting;
   the two demand-split ensembles' argmin classes intersect and
   both transfer gaps are exactly zero. [The pointwise clause is
   refuted — route-locking is real (F3); the universal candidate
   fails at exactly one setting (F4); the ensemble clauses held.]
C4 [the trap under the bank] At W > 0 and B = 1, 2 the landscape
   still funnels under the cure set (lexicographic descent, single
   moves + the preference diagonal) from every start at every
   setting; where banking is inert the sigma = (0,0) trap of
   explore_throttled_reader.py persists unchanged (whether B = 1
   is inert everywhere is the flagged open question above).
   [The every-setting funnel clause is refuted at (B,W) = (3,8) —
   the degenerate ridge, the discovery of the run (F5).]
C5 [monotonicity] On the greedy quartet at spend-all, loss is
   non-increasing in W at fixed B and non-increasing in B at fixed
   W, on every row — zero anomalies.

KILL CRITERIA, fixed at the freeze
----------------------------------
K1 Any C1 control fails: the rig is dead, no verdicts.
K2 THE PRINCIPAL KILL (an observable, not an inference): a universal
   policy sits in every row's argmin class at every scanned
   (B, W). What that means for the program — whether the
   time-allocation layer is exhausted and a scale axis enters the
   next slate — is weighed after the run, not encoded here.
K3 A stall above the minimum that survives the cure set
   (lexicographic + single moves + diagonal) at some setting: a
   new blindness type beyond the two catalogued; its structure
   becomes the finding.
K4 A W-anomaly or B-anomaly on the greedy quartet at spend-all:
   stop and hand-trace before reading any other verdict (bug
   versus real anomaly; if real, C5 is refuted honestly and the
   anomaly is a first-class finding).

ENGINE
------
Exact integer arithmetic in every decision. The engine core
(points, cylinders, cells, the unthrottled and throttled readers,
the exact loss) is copied verbatim from
explore_throttled_reader.py; this experiment adds the banking
reader, the per-setting policy spaces over the quotiented delta
axis, behavioral signatures, per-row and per-ensemble argmin
classes with raw and quotiented sizes, the transfer measurement,
descent over precomputed exact ranks with the cure set, the banked
threshold table, and the bank-level watch (bank traces and
drain-event sizes for the greedy reader — a stored resource pool
feeding two drivers is worth one print). Sequential, well under
the resource caps (settings processed one at a time, tables
discarded between; estimated run a few minutes); positive controls
gate all verdicts; exit nonzero on any failure.

FINDINGS (entered after the run; ALL ENGINES PASS, exit 0, ~31 s)
----------------------------------------------------------------
F1 C1 CONFIRMED, controls exact: the W = 0 regression is exact at
   all four budgets (0 mismatches); the collapse sample exact; the
   delta = 0 slice equals W = 0 at every setting; the disease
   reproduces (8 stalls); demand slopes as before. Per-step demand
   ranges: phi, sqrt2, theta8 uniform (1, 2, 8); sqrt3 1..2;
   sq/phi steady 1..1 with ONE warm-up zero step; dbl/phi 1..2;
   dbl/sqrt2 2..3 — not the hand-guessed 1..4.
F2 C2 REFUTED TWICE, the two named movers both wrong ways round:
   (a) sq/phi drops 2 -> 1 at every W > 0: the single warm-up wait
   step banks one unit, which repays the leading digit's two-rank
   debt — the frozen "bank born empty means the warm-up debt is
   uncurable" clause was wrong because the warm-up wait IS the
   pre-burst surplus. (b) dbl/sqrt2 is 3 at EVERY cap including
   W = 0: its per-step demand is 2..3, so B = 3 catches up with no
   bank — the threshold "4" recorded by explore_throttled_reader.py
   was budget-grid resolution (B = 3 unscanned there), corrected
   here, not a banking effect. So banking moves exactly ONE
   threshold on this slate and by warm-up funding, not smoothing.
   Banked never beats unthrottled; C5 held (zero anomalies).
F3 C3's pointwise clause REFUTED — ROUTE-LOCKING IS REAL: 83
   strict wins for withholding over spend-all at scope — sq/phi 36
   (gaps 0.016..0.041 ln), id/sqrt2 36 (gaps 14.00..14.51 ln),
   dbl/sqrt2 6 (0.37..0.91), id/theta8 5 (below 1e-4 but
   exact-strict). The failing bases are patient-tree readers
   (pt in {2, 3}) on sq/phi, id/sqrt2, and dbl/sqrt2, and
   sigma = (1,0) bases with pc = pt + 1 on theta8; at B = 2 even
   never-draw
   (delta = 0) beats spend-all on sq/phi. All 83 are off-optimum:
   every per-row argmin class contains a spend-all policy at every
   setting — the destination is schedule-free.
F4 C3's universal clause REFUTED at ONE setting — THE ENVIRONMENT
   SHIFT: (1,1, greedy, spend-all) is universal at 15/16 settings;
   at (B, W) = (4, 2) the route order inverts on theta8 (greedy
   square: sigma = (0,0) = (0,1) at -14920.6, (1,1) -14909.1,
   (1,0) -14901.0 ln) and the universal set becomes sigma in
   {(0,0), (0,1)} at greedy patience, delta >= 1. The optimum is
   ensemble-free but NOT environment-free: what a policy must
   track is the resource pair (B, W), never the stream. Transfer
   gaps exactly zero at every setting.
F5 C4 REFUTED at (B, W) = (3, 8) — THE DEGENERATE RIDGE, the
   discovery of the run, a THIRD blindness species. The cure set
   stalls on exactly {sigma = (1,1), patience = (0,2),
   delta >= 2} (rank 3, aggregate gap 163.54 ln, worse than the
   bottom only on the two dbl rows); 640/1000 cure-set descents
   converge. The stall's tie class contains behaviorally IDENTICAL
   twins at chain patience 1 — the full bank smooths chain
   patience 1 vs 2 into the same committed cells at every counted
   step — so the strict exit (chain patience 1 -> 0, the cliff
   onto greedy) sits one TIE-move away and strict descent cannot
   cross the flat. Abundance manufactures the flatness: the ridge
   lives exactly in the smoothing window (B = 3 is dbl/sqrt2's
   catch-up income, W = 8 the full bank; at B = 2 the bank starves
   and the gradient returns, at B = 4 the rows catch up and the
   ridge dissolves into the bottom tie). Elsewhere the scarcity
   trap of explore_throttled_reader.py persists at B = 1, 2 and
   FATTENS along the delta and chain-patience axes as the cap
   grows (single-move stalls 1 -> 12 as W goes 0 -> 8 at B = 1),
   all diagonal-cured. THE CURE FOR THE RIDGE IS THE QUOTIENT:
   descent allowed to tie-walk along behavioral identity (descent
   on the quotient poset of counted-window behaviors) converges
   from every start at (3, 8) and at every other setting — the
   trap is an artifact of unquotiented coordinates.
F6 The bank watch: on this slate bank dynamics never oscillate —
   three regimes, zero or one drain event per row. HOARD (surplus
   steps and no deficit steps: the bank climbs to the cap and
   pins, means 7.67-7.92 at W = 8); FLAT (demand equals income at
   every steady step: id/sqrt2 at B = 2 holds its banked warm-up
   units, constant 2.00, never drawn); ONE-SHOT DRAIN (net
   deficit: the warm-up stock drains in a single event of 1-3
   units and the bank runs dry). No save/spend cycle exists under
   periodic demand; event-size statistics would need bursty
   streams.

THE VERDICT. Three answers.
(Q1) NO again, third stage running — and sharper: at every
setting a universal policy exists, transfer gaps are exactly zero,
and the schedule axis is degenerate at the optimum (every
delta >= 1 ties in the argmin classes; the greedy reader draws the
bank at most once per row here). Training data still does not pick
the destination. What IS new: the destination depends on the
resource ENVIRONMENT — at (4, 2) the route order inverts — so a
reader at scarcity must track its own metabolism (B, W), never the
stream.
(Q2) Banking moves exactly one threshold, by warm-up funding, not
smoothing: sq/phi 2 -> 1 (the wait step is the surplus). The
predicted smoothing drop was an upstream budget-grid artifact.
(Q3) The funnel survives everywhere except the smoothing window
(3, 8), where the third blindness species appears: the DEGENERATE
RIDGE — flatness manufactured by resource abundance, invisible to
every window-native signal by construction (the tied policies are
behaviorally identical, so no loss over the counted window can
order them), cured by descent on the behavioral QUOTIENT. The
species table: plateau blindness (unbounded width — signal cure),
coordination blindness (bounded plane — move cure), degeneracy
ridges (flat quotient fibers — quotient cure).

Run record. The first run exited 1 at four checks: C2 refuted
twice (F2), C3's pointwise and universal clauses refuted (F3, F4),
C4's funnel clause refuted (F5); every control passed on every
run. Post-run edits added the diagnostics (the pointwise census,
the intersection prints, the theta8 square, the ridge anatomy, the
quotient-descent probe) and re-encoded the failed checks to the
found landscape as recorded here; no prediction band was touched;
attributions are read off printed censuses and per-policy grids,
not off narrative. Tiers: every landscape statement is verified
exhaustively at the stated scope (spaces of 100-500 policies over
the quotiented delta axis, 8 rows, B in {1,2,3,4} x W in
{0,2,4,8}, N = 120); the ridge's twin identity is exact behavioral
equality of committed cells at scope; the threshold table and the
route-locking census are observations at scope.

Settled downstream: explore_scale_clock.py replaces the loss
layer — the deficit gives way to a lag counted on the stream's
own clock (steps behind, an integer per counted step), descended
on the quotient space of counted-window behaviors built at design
time. The answer holds on both rulers: a per-setting universal
policy at every (budget, cap), transfer gaps exactly zero, and
the (4, 2) environment shift reappearing verbatim — loss-
invariant. On the quotient the deficit landscape has NO stalls at
any setting (this experiment's scarcity trap was an artifact of
unquotiented coordinates), and the clock loss creates exactly one
of its own — the disagreement stall, a fourth blindness species
where the coarse ruler dams the fine ruler's gradient.
"""

import math
import sys
from functools import cmp_to_key

LN2 = math.log(2)
INF_P = None          # patience sentinel: refuse the class
INF_D = None          # drawdown sentinel: spend-all
N0 = 8                # loss counted from this step
N_MAIN = 120
AX_BASE = [0, 1, 2, 3, INF_P]
BUDGETS = [1, 2, 3, 4]
CAPS = [0, 2, 4, 8]

# ----------------------------------------------------------------- #
# engine core (verbatim from explore_throttled_reader.py)
# points: integer pairs (p, q), q >= 0; (1, 0) = +infinity
# ----------------------------------------------------------------- #

def lt(a, b):
    return a[0] * b[1] < b[0] * a[1]

def mediant(a, b):
    return (a[0] + b[0], a[1] + b[1])

def ln_int(x):
    """ln of a positive big integer without overflow."""
    b = x.bit_length()
    if b <= 900:
        return math.log(x)
    return math.log(x >> (b - 64)) + (b - 64) * LN2

def ln_frac(num, den):
    return ln_int(num) - ln_int(den)

def cf_digits(head, period, count):
    digs = list(head)
    while len(digs) < count:
        digs.extend(period)
    return digs[:count]

STREAMS = {
    "phi":   ([1], [1]),
    "sqrt2": ([1], [2]),
    "sqrt3": ([1], [1, 2]),
    "theta8": ([0], [8]),
}

def cylinders(digs):
    """Exact cylinder intervals: after digits a_0..a_n the interval
    spans p_n/q_n to (p_n+p_{n-1})/(q_n+q_{n-1})."""
    p2, q2, p1, q1 = 0, 1, 1, 0
    out = []
    for a in digs:
        p, q = a * p1 + p2, a * q1 + q2
        e1, e2 = (p, q), (p + p1, q + q1)
        out.append((e1, e2) if lt(e1, e2) else (e2, e1))
        p2, q2, p1, q1 = p1, q1, p, q
    return out

MAPS = {
    "id":  lambda e: e,
    "sq":  lambda e: (e[0] * e[0], e[1] * e[1]),
    "dbl": lambda e: (2 * e[0], e[1]),
}

def images(rows_digits, map_name):
    f = MAPS[map_name]
    out = []
    for lo, hi in rows_digits:
        a, b = f(lo), f(hi)
        out.append((a, b) if lt(a, b) else (b, a))
    return out

ROOT = ("T", (0, 1), (1, 0), 0)

def interval(cell):
    if cell[0] == "T":
        return cell[1], cell[2]
    _, v, l, r, _, k = cell
    mL = (l[0] + k * v[0], l[1] + k * v[1])
    mR = (r[0] + k * v[0], r[1] + k * v[1])
    return mL, mR

def rank(cell):
    return cell[3] if cell[0] == "T" else cell[4] + cell[5]

def contains(cell, J):
    lo, hi = interval(cell)
    return lt(lo, J[0]) and lt(J[1], hi)

def length_pair(cell):
    """(num, den) of the interval length, or None for infinite."""
    lo, hi = interval(cell)
    if hi[1] == 0:
        return None
    return hi[0] * lo[1] - lo[0] * hi[1], hi[1] * lo[1]

def max_k(A, B):
    """Largest k >= 1 with k*A < B; 0 if none; None if all k."""
    if A <= 0:
        return None if A < B else 0
    if B <= A:
        return 0
    return (B - 1) // A

def chain_kmax(v, l, r, J):
    """Largest k >= 1 with S_k(v) containing J; 0 if none."""
    (a, b), (c, d) = J
    kL = max_k(b * v[0] - a * v[1], a * l[1] - b * l[0])
    kR = max_k(c * v[1] - d * v[0], d * r[0] - c * r[1])
    if kL == 0 or kR == 0:
        return 0
    if kL is None and kR is None:
        raise AssertionError("straddle contains J at every index")
    if kL is None:
        return kR
    if kR is None:
        return kL
    return min(kL, kR)

def run_reader(J_list, policy, redundant, horizon):
    """Run one policy over one image stream, unthrottled. Returns
    (loss_num, loss_den, inf_flag, rank_trace, n_choices)."""
    s_t, s_s, pt, pc = policy
    C = ROOT
    num, den, inf = 1, 1, False
    n_choices = 0
    trace = []
    for n in range(horizon):
        J = J_list[n]
        ref_t = J_list[n - pt] if pt is not None and n - pt >= 0 else None
        ref_c = J_list[n - pc] if pc is not None and n - pc >= 0 else None
        guard = 0
        while True:
            guard += 1
            if guard > 10 ** 6:
                raise AssertionError("commit loop runaway")
            cand_tree = cand_chain = None
            if C[0] == "T":
                _, l, r, d = C
                v = mediant(l, r)
                if ref_t is not None:
                    for ch in (("T", l, v, d + 1), ("T", v, r, d + 1)):
                        if contains(ch, ref_t):
                            cand_tree = ch
                            break
                if ref_c is not None:
                    k = chain_kmax(v, l, r, ref_c)
                    if k >= 1:
                        cand_chain = ("S", v, l, r, d, k)
                prefer_chain = (s_t == 1)
            else:
                _, v, l, r, d, k = C
                if ref_c is not None:
                    k2 = chain_kmax(v, l, r, ref_c)
                    if k2 > k:
                        cand_chain = ("S", v, l, r, d, k2)
                if ref_t is not None:
                    mL, mR = interval(C)
                    for ch in (("T", mL, v, d + k + 1),
                               ("T", v, mR, d + k + 1)):
                        if contains(ch, ref_t):
                            cand_tree = ch
                            break
                prefer_chain = (s_s == 0)
            if cand_tree is None and cand_chain is None:
                break
            if cand_tree is not None and cand_chain is not None:
                n_choices += 1
            if cand_chain is not None and (cand_tree is None or prefer_chain):
                C = cand_chain
            else:
                C = cand_tree
        clo, chi = interval(C)
        if lt(J[0], clo) or lt(chi, J[1]):
            raise AssertionError("commitment lost the image")
        if n >= N0:
            lp = length_pair(C)
            if lp is None:
                inf = True
            else:
                num *= lp[0]
                den *= lp[1]
        trace.append((rank(C), C[5] if C[0] == "S" else 0, (clo, chi)))
    return num, den, inf, trace, n_choices

def run_reader_throttled(J_list, policy, horizon, budget):
    """The throttled reader (verbatim): a rank budget per input step,
    unspent units lost at the step boundary."""
    s_t, s_s, pt, pc = policy
    C = ROOT
    num, den, inf = 1, 1, False
    n_choices = 0
    trace = []
    for n in range(horizon):
        J = J_list[n]
        ref_t = J_list[n - pt] if pt is not None and n - pt >= 0 else None
        ref_c = J_list[n - pc] if pc is not None and n - pc >= 0 else None
        rem = budget
        guard = 0
        while True:
            guard += 1
            if guard > 10 ** 6:
                raise AssertionError("commit loop runaway")
            if rem is not None and rem <= 0:
                break
            cand_tree = cand_chain = None
            if C[0] == "T":
                _, l, r, d = C
                v = mediant(l, r)
                if ref_t is not None:
                    for ch in (("T", l, v, d + 1), ("T", v, r, d + 1)):
                        if contains(ch, ref_t):
                            cand_tree = ch
                            break
                if ref_c is not None:
                    k = chain_kmax(v, l, r, ref_c)
                    if rem is not None:
                        k = min(k, rem)
                    if k >= 1:
                        cand_chain = ("S", v, l, r, d, k)
                prefer_chain = (s_t == 1)
            else:
                _, v, l, r, d, k = C
                if ref_c is not None:
                    k2 = chain_kmax(v, l, r, ref_c)
                    if rem is not None:
                        k2 = min(k2, k + rem)
                    if k2 > k:
                        cand_chain = ("S", v, l, r, d, k2)
                if ref_t is not None:
                    mL, mR = interval(C)
                    for ch in (("T", mL, v, d + k + 1),
                               ("T", v, mR, d + k + 1)):
                        if contains(ch, ref_t):
                            cand_tree = ch
                            break
                prefer_chain = (s_s == 0)
            if cand_tree is None and cand_chain is None:
                break
            if cand_tree is not None and cand_chain is not None:
                n_choices += 1
            prev = rank(C)
            if cand_chain is not None and (cand_tree is None or prefer_chain):
                C = cand_chain
            else:
                C = cand_tree
            if rem is not None:
                rem -= rank(C) - prev
        clo, chi = interval(C)
        if lt(J[0], clo) or lt(chi, J[1]):
            raise AssertionError("commitment lost the image")
        if n >= N0:
            lp = length_pair(C)
            if lp is None:
                inf = True
            else:
                num *= lp[0]
                den *= lp[1]
        trace.append((rank(C), C[5] if C[0] == "S" else 0, (clo, chi)))
    return num, den, inf, trace, n_choices

# ----------------------------------------------------------------- #
# the banking reader (the one new machine)
# ----------------------------------------------------------------- #

def run_reader_banking(J_list, policy, horizon, budget, cap):
    """The banking reader: the throttled commit loop plus a bank of
    unspent rank units (level in [0, cap], deposits automatic,
    overflow lost) and a per-step drawdown ceiling delta over income
    (delta = None: spend-all). Returns (loss_num, loss_den,
    inf_flag, sig, bank_trace, draw_trace) where sig is the hash of
    the counted-window committed-cell trace."""
    s_t, s_s, pt, pc, delta = policy
    assert budget is not None
    C = ROOT
    num, den, inf = 1, 1, False
    bank = 0
    bank_trace = []
    draw_trace = []
    counted = []
    for n in range(horizon):
        J = J_list[n]
        ref_t = J_list[n - pt] if pt is not None and n - pt >= 0 else None
        ref_c = J_list[n - pc] if pc is not None and n - pc >= 0 else None
        avail = budget + bank
        if delta is None:
            spendable = avail
        else:
            spendable = min(avail, budget + delta)
        rem = spendable
        guard = 0
        while True:
            guard += 1
            if guard > 10 ** 6:
                raise AssertionError("commit loop runaway")
            if rem <= 0:
                break
            cand_tree = cand_chain = None
            if C[0] == "T":
                _, l, r, d = C
                v = mediant(l, r)
                if ref_t is not None:
                    for ch in (("T", l, v, d + 1), ("T", v, r, d + 1)):
                        if contains(ch, ref_t):
                            cand_tree = ch
                            break
                if ref_c is not None:
                    k = chain_kmax(v, l, r, ref_c)
                    k = min(k, rem)
                    if k >= 1:
                        cand_chain = ("S", v, l, r, d, k)
                prefer_chain = (s_t == 1)
            else:
                _, v, l, r, d, k = C
                if ref_c is not None:
                    k2 = chain_kmax(v, l, r, ref_c)
                    k2 = min(k2, k + rem)
                    if k2 > k:
                        cand_chain = ("S", v, l, r, d, k2)
                if ref_t is not None:
                    mL, mR = interval(C)
                    for ch in (("T", mL, v, d + k + 1),
                               ("T", v, mR, d + k + 1)):
                        if contains(ch, ref_t):
                            cand_tree = ch
                            break
                prefer_chain = (s_s == 0)
            if cand_tree is None and cand_chain is None:
                break
            prev = rank(C)
            if cand_chain is not None and (cand_tree is None or prefer_chain):
                C = cand_chain
            else:
                C = cand_tree
            rem -= rank(C) - prev
        spent = spendable - rem
        draw_trace.append(max(0, spent - budget))
        bank = min(cap, avail - spent)
        bank_trace.append(bank)
        clo, chi = interval(C)
        if lt(J[0], clo) or lt(chi, J[1]):
            raise AssertionError("commitment lost the image")
        if n >= N0:
            lp = length_pair(C)
            if lp is None:
                inf = True
            else:
                num *= lp[0]
                den *= lp[1]
            counted.append((clo, chi))
    return num, den, inf, hash(tuple(counted)), bank_trace, draw_trace

def agg(losses):
    """Aggregate (num, den, inf) triples by multiplying. The num/den
    of the result is the FINITE PART: infinite-length steps set the
    flag and contribute no factor."""
    num, den, inf = 1, 1, False
    for n, d, i in losses:
        if i:
            inf = True
        else:
            num *= n
            den *= d
    return num, den, inf

ROWS = [
    ("id",  "phi"), ("id", "sqrt2"), ("id", "sqrt3"), ("id", "theta8"),
    ("sq",  "sqrt2"),                     # the wall row
    ("sq",  "phi"), ("dbl", "phi"), ("dbl", "sqrt2"),
]
WALL = ("sq", "sqrt2")
E_SLOW = [("id", "phi"), ("sq", "phi"), ("dbl", "phi"), ("id", "sqrt3")]
E_FAST = [("id", "sqrt2"), ("dbl", "sqrt2"), ("id", "theta8"), WALL]

def build_images(horizon):
    cyl = {s: cylinders(cf_digits(*STREAMS[s], count=horizon))
           for s in STREAMS}
    return {(m, s): images(cyl[s], m) for (m, s) in ROWS}

# ----------------------------------------------------------------- #
# spaces, comparators, moves, descent
# ----------------------------------------------------------------- #

def d_axis(cap):
    """The quotiented delta axis at a cap: finite values below the
    cap plus spend-all (values at or above the cap are behaviorally
    spend-all; at cap 0 the axis is one class)."""
    return [d for d in (0, 1, 2, 4) if d < cap] + [INF_D]

def policy_space5(axis, daxis):
    return [(st, ss, pt, pc, d)
            for st in (0, 1) for ss in (0, 1)
            for pt in axis for pc in axis for d in daxis]

def neighbors_single5(pol, axis, daxis):
    st, ss, pt, pc, d = pol
    out = [(1 - st, ss, pt, pc, d), (st, 1 - ss, pt, pc, d)]
    it, ic, idd = axis.index(pt), axis.index(pc), daxis.index(d)
    if it > 0:
        out.append((st, ss, axis[it - 1], pc, d))
    if it < len(axis) - 1:
        out.append((st, ss, axis[it + 1], pc, d))
    if ic > 0:
        out.append((st, ss, pt, axis[ic - 1], d))
    if ic < len(axis) - 1:
        out.append((st, ss, pt, axis[ic + 1], d))
    if idd > 0:
        out.append((st, ss, pt, pc, daxis[idd - 1]))
    if idd < len(daxis) - 1:
        out.append((st, ss, pt, pc, daxis[idd + 1]))
    return out

def neighbors_cure(pol, axis, daxis):
    """Single moves plus the preference diagonal (both route
    coordinates flipped together)."""
    st, ss, pt, pc, d = pol
    return neighbors_single5(pol, axis, daxis) + \
        [(1 - st, 1 - ss, pt, pc, d)]

def cmp_plain(a, b):
    """-1 if loss a < loss b; infinite ties infinite (the disease)."""
    if a[2] and b[2]:
        return 0
    if a[2]:
        return 1
    if b[2]:
        return -1
    left = a[0] * b[1]
    right = b[0] * a[1]
    return -1 if left < right else (1 if left > right else 0)

def cmp_lex(a, b):
    """Lexicographic deficit comparison: finite beats infinite; two
    infinites compare their finite parts (the shortfall)."""
    if a[2] != b[2]:
        return 1 if a[2] else -1
    left = a[0] * b[1]
    right = b[0] * a[1]
    return -1 if left < right else (1 if left > right else 0)

def policy_space4(axis):
    return [(st, ss, pt, pc)
            for st in (0, 1) for ss in (0, 1)
            for pt in axis for pc in axis]

def neighbors_single4(pol, axis):
    st, ss, pt, pc = pol
    out = [(1 - st, ss, pt, pc), (st, 1 - ss, pt, pc)]
    it, ic = axis.index(pt), axis.index(pc)
    if it > 0:
        out.append((st, ss, axis[it - 1], pc))
    if it < len(axis) - 1:
        out.append((st, ss, axis[it + 1], pc))
    if ic > 0:
        out.append((st, ss, pt, axis[ic - 1]))
    if ic < len(axis) - 1:
        out.append((st, ss, pt, axis[ic + 1]))
    return out

def rank_map(space, losses, cmpf):
    """One exact total preorder: policy -> integer rank (ties share)."""
    order = sorted(space, key=cmp_to_key(
        lambda x, y: cmpf(losses[x], losses[y])))
    ranks = {order[0]: 0}
    r = 0
    for prev, cur in zip(order, order[1:]):
        if cmpf(losses[prev], losses[cur]) < 0:
            r += 1
        ranks[cur] = r
    return ranks

def descend(start, ranks, nbr_fn, best_improve):
    p = start
    path = [p]
    while True:
        nbs = nbr_fn(p)
        if best_improve:
            nbs = sorted(nbs, key=lambda q: ranks[q])
        moved = False
        for q in nbs:
            if ranks[q] < ranks[p]:
                p = q
                path.append(p)
                moved = True
                break
        if not moved:
            return p, path

def stalls_of(space, ranks, nbr_fn):
    return [p for p in space
            if all(ranks[q] >= ranks[p] for q in nbr_fn(p))]

def fmt_pol5(p):
    return "sigma=(%d,%d) patience=(%s,%s) delta=%s" % (
        p[0], p[1],
        "INF" if p[2] is None else str(p[2]),
        "INF" if p[3] is None else str(p[3]),
        "ALL" if p[4] is None else str(p[4]))

def fmt_row(row):
    return "%s/%s" % row

def ln_loss(t):
    return ln_frac(t[0], t[1])

def quartet4():
    return [(st, ss, 0, 0) for st in (0, 1) for ss in (0, 1)]

def corners4():
    return [(st, ss, INF_P, INF_P) for st in (0, 1) for ss in (0, 1)]

UNIV = (1, 1, 0, 0, INF_D)   # chain-first entry, tree-first exit,
                             # greedy patience, spend-all
GREEDY5 = (0, 0, 0, 0, INF_D)

# ----------------------------------------------------------------- #
# engines
# ----------------------------------------------------------------- #

FAILURES = []

def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s %s" % (tag, name, detail))
    if not ok:
        FAILURES.append(name)
    return ok

def slope(ys, xs):
    return (ys[-1] - ys[0]) / (xs[-1] - xs[0])

def bank_table(imgs, space, B, W):
    """Per-(policy, row) loss triples and signatures at one setting."""
    tab, sig = {}, {}
    for pol in space:
        for row in ROWS:
            r = run_reader_banking(imgs[row], pol, N_MAIN, B, W)
            tab[(pol, row)] = r[:3]
            sig[(pol, row)] = r[3]
    return tab, sig

def e1_controls(imgs):
    print("E1 CONTROLS (gate: no verdicts are read unless these pass)")
    space4 = policy_space4(AX_BASE)
    # (i) W = 0 == the throttled reader, every scanned budget
    bad = 0
    for B in BUDGETS:
        for pol in space4:
            for row in ROWS:
                got = run_reader_banking(imgs[row], pol + (INF_D,),
                                         N_MAIN, B, 0)[:3]
                want = run_reader_throttled(imgs[row], pol, N_MAIN, B)[:3]
                if got != want:
                    bad += 1
    check("banking reader at W=0 == throttled reader, all 100 "
          "policies x 8 rows x B in {1,2,3,4}", bad == 0,
          "%d mismatches" % bad)
    # (iii) the collapse proof sampled: excluded delta values == ALL
    bad = 0
    for W, d in ((2, 2), (2, 4), (4, 4)):
        for B in BUDGETS:
            for pol4 in quartet4():
                for row in ROWS:
                    a = run_reader_banking(imgs[row], pol4 + (d,),
                                           N_MAIN, B, W)[:3]
                    b = run_reader_banking(imgs[row], pol4 + (INF_D,),
                                           N_MAIN, B, W)[:3]
                    if a != b:
                        bad += 1
    check("delta >= W behaves as spend-all exactly (sampled: greedy "
          "quartet, all rows, all B, (W,d) in {(2,2),(2,4),(4,4)})",
          bad == 0, "%d mismatches" % bad)
    # (iv) the disease on the unthrottled slate
    losses = {pol: agg([run_reader(imgs[row], pol, True, N_MAIN)[:3]
                        for row in ROWS]) for pol in space4}
    ranks = rank_map(space4, losses, cmp_plain)
    st = stalls_of(space4, ranks, lambda p: neighbors_single4(p, AX_BASE))
    expected = set(quartet4()) | set(corners4())
    check("the disease reproduces: plain stalls unthrottled = greedy "
          "quartet + the four corners", set(st) == expected,
          "%d stalls" % len(st))
    # (v) demand slopes + per-step minima
    greedy = (0, 0, 0, 0)
    demands = {}
    for row in ROWS:
        tr = run_reader(imgs[row], greedy, True, N_MAIN)[3]
        if row == WALL:
            ks = [(n, math.log(t[1])) for n, t in enumerate(tr)
                  if t[1] > 0 and n >= 20]
            demands[row] = ("ln-k", slope([y for _, y in ks],
                                          [n for n, _ in ks]))
        else:
            rk = [(n, t[0]) for n, t in enumerate(tr) if n >= 20]
            demands[row] = ("rank", slope([r for _, r in rk],
                                          [n for n, _ in rk]))
        steps = [tr[n][0] - tr[n - 1][0] for n in range(21, N_MAIN)]
        early = [tr[0][0]] + [tr[n][0] - tr[n - 1][0]
                              for n in range(1, 21)]
        print("  %s per-step demand: steady min %d max %d | warm-up "
              "zeros %d" % (fmt_row(row), min(steps), max(steps),
                            sum(1 for x in early if x == 0)))
    print("  greedy demand per row: " + "  ".join(
        "%s %.2f(%s)" % (fmt_row(r), d, kind)
        for r, (kind, d) in demands.items()))
    check("id/phi demand in [0.9, 1.1]",
          0.9 <= demands[("id", "phi")][1] <= 1.1)
    check("id/theta8 demand in [7, 9]",
          7 <= demands[("id", "theta8")][1] <= 9)
    check("wall chain ln-k slope in [1.71, 1.82]",
          1.71 <= demands[WALL][1] <= 1.82)
    tr = run_reader(imgs[("dbl", "phi")], (0, 0, 0, INF_P), False,
                    N_MAIN)[3]
    rk = [(n, t[0]) for n, t in enumerate(tr) if n >= 20]
    sl = slope([r for _, r in rk], [n for n, _ in rk])
    check("(2x, phi) partition rank slope in [1.26, 1.40] (4/3)",
          1.26 <= sl <= 1.40, "slope %.4f" % sl)
    return not FAILURES

def banked_threshold_expect(row, W):
    """The measured smoothing table (the frozen table died twice —
    see the findings): least scanned B with exact catch-up, None =
    never within the scanned budgets. sq/phi is the one row banking
    moves (2 -> 1: the warm-up wait step banks the unit that repays
    the leading digit's debt); dbl/sqrt2 is 3 at EVERY cap — its
    per-step demand is 2..3, so B = 3 already catches up unbanked."""
    base = {("id", "phi"): 1, ("id", "sqrt2"): 2, ("id", "sqrt3"): 2,
            ("dbl", "phi"): 2, ("id", "theta8"): None,
            ("dbl", "sqrt2"): 3, WALL: None}
    if row == ("sq", "phi"):
        return 2 if W == 0 else 1
    return base[row]

def e2_smoothing(imgs, greedy_tabs, unthr):
    print("E2 THE SMOOTHING LAW (C2 / C5 / K4)")
    ok = True
    for row in ROWS:
        for W in CAPS:
            th = banked_threshold_expect(row, W)
            for B in BUDGETS:
                c = cmp_lex(greedy_tabs[(B, W)][row], unthr[row])
                want_eq = th is not None and B >= th
                if (c == 0) != want_eq or c < 0:
                    ok = False
                    print("    smoothing law broken at %s B=%d W=%d "
                          "(cmp %d, expected %s)"
                          % (fmt_row(row), B, W, c,
                             "eq" if want_eq else "gt"))
    check("banked catch-up thresholds match the measured table "
          "(sq/phi drops 2 -> 1 at every W > 0; dbl/sqrt2 is 3 at "
          "every W including 0; all others unmoved; banked never "
          "beats unthrottled)", ok)
    # measured table print
    for row in ROWS:
        cells = []
        for W in CAPS:
            th = None
            for B in BUDGETS:
                if cmp_lex(greedy_tabs[(B, W)][row], unthr[row]) == 0:
                    th = B
                    break
            cells.append("W=%d:%s" % (W, th if th else ">4"))
        print("  measured banked threshold %s: %s"
              % (fmt_row(row), "  ".join(cells)))
    # C5 monotonicity on the greedy quartet at spend-all
    anomalies = []
    for st_, ss_ in [(s, t) for s in (0, 1) for t in (0, 1)]:
        pol = (st_, ss_, 0, 0, INF_D)
        for row in ROWS:
            for B in BUDGETS:
                for w_lo, w_hi in zip(CAPS, CAPS[1:]):
                    if cmp_lex(QTABS[(B, w_lo)][(pol, row)],
                               QTABS[(B, w_hi)][(pol, row)]) < 0:
                        anomalies.append((pol, row, "W", B, w_lo, w_hi))
            for W in CAPS:
                for b_lo, b_hi in zip(BUDGETS, BUDGETS[1:]):
                    if cmp_lex(QTABS[(b_lo, W)][(pol, row)],
                               QTABS[(b_hi, W)][(pol, row)]) < 0:
                        anomalies.append((pol, row, "B", W, b_lo, b_hi))
    check("greedy-quartet spend-all loss non-increasing in W and in "
          "B on every row (no anomaly)", not anomalies,
          "%d anomalies" % len(anomalies))
    for a in anomalies[:10]:
        print("    ANOMALY %s %s along %s at %s: %s beats %s"
              % (fmt_pol5(a[0]), fmt_row(a[1]), a[2], a[3], a[4], a[5]))

QTABS = {}   # (B, W) -> {(quartet-spend-all policy, row): triple}

PW_FAILS = []   # (B, W, base, row, d, ln-gap): finite delta beat ALL

def e3_argmin(tab, sig, space, B, W):
    print("  -- setting B=%d W=%d (space %d)" % (B, W, len(space)))
    ok_pw = True
    daxis = d_axis(W)
    finite_ds = [d for d in daxis if d is not None]
    # pointwise: spend-all weakly best at every fixed base coordinate
    for st_ in (0, 1):
        for ss_ in (0, 1):
            for pt in AX_BASE:
                for pc in AX_BASE:
                    for row in ROWS:
                        base = tab[((st_, ss_, pt, pc, INF_D), row)]
                        for d in finite_ds:
                            other = tab[((st_, ss_, pt, pc, d), row)]
                            if cmp_lex(base, other) > 0:
                                ok_pw = False
                                PW_FAILS.append(
                                    (B, W, (st_, ss_, pt, pc), row, d,
                                     ln_loss(base) - ln_loss(other)))
    # per-row argmin classes
    univ_ok = True
    spendall_ok = True
    inter = None
    row_classes = {}
    for row in ROWS:
        best = None
        for pol in space:
            if best is None or cmp_lex(tab[(pol, row)],
                                       tab[(best, row)]) < 0:
                best = pol
        cls = [p for p in space
               if cmp_lex(tab[(p, row)], tab[(best, row)]) == 0]
        row_classes[row] = set(cls)
        if not any(p[4] is None for p in cls):
            spendall_ok = False
        qsigs = len(set(sig[(p, row)] for p in cls))
        print("    argmin %s: raw %d, quotiented %d%s"
              % (fmt_row(row), len(cls), qsigs,
                 "" if UNIV in row_classes[row] else "  [UNIV ABSENT]"))
        if UNIV not in row_classes[row]:
            univ_ok = False
        inter = row_classes[row] if inter is None \
            else inter & row_classes[row]
    # ensembles + transfer
    gaps = []
    for src, dst in ((E_SLOW, E_FAST), (E_FAST, E_SLOW)):
        el = {p: agg([tab[(p, r)] for r in src]) for p in space}
        dl = {p: agg([tab[(p, r)] for r in dst]) for p in space}
        bs = min(space, key=cmp_to_key(
            lambda x, y: cmp_lex(el[x], el[y])))
        cls = [p for p in space if cmp_lex(el[p], el[bs]) == 0]
        bd = min(space, key=cmp_to_key(
            lambda x, y: cmp_lex(dl[x], dl[y])))
        tr_pol = min(cls, key=cmp_to_key(
            lambda x, y: cmp_lex(dl[x], dl[y])))
        gaps.append((cmp_lex(dl[tr_pol], dl[bd]),
                     ln_loss(dl[tr_pol]) - ln_loss(dl[bd])))
    print("    universal-in-every-argmin %s | intersection %d | "
          "transfer gaps %s"
          % (univ_ok, len(inter),
             " ".join("%.2f%s" % (g[1], "=" if g[0] == 0 else ">")
                      for g in gaps)))
    if len(inter) <= 8:
        print("    intersection members: %s"
              % "; ".join(fmt_pol5(p) for p in sorted(
                  inter, key=lambda p: (p[0], p[1],
                                        99 if p[2] is None else p[2],
                                        99 if p[3] is None else p[3],
                                        99 if p[4] is None else p[4]))))
    return ok_pw, univ_ok, inter, \
        all(g[0] == 0 for g in gaps), spendall_ok

def e4_landscape(tab, sig, space, B, W):
    losses = {p: agg([tab[(p, r)] for r in ROWS]) for p in space}
    ranks = rank_map(space, losses, cmp_lex)
    daxis = d_axis(W)
    nbr_s = lambda p: neighbors_single5(p, AX_BASE, daxis)
    nbr_c = lambda p: neighbors_cure(p, AX_BASE, daxis)
    st_single = [p for p in stalls_of(space, ranks, nbr_s)
                 if ranks[p] > 0]
    st_cure = [p for p in stalls_of(space, ranks, nbr_c)
               if ranks[p] > 0]
    conv = 0
    total = 0
    for variant in (True, False):
        for start in space:
            p, _ = descend(start, ranks, nbr_c, variant)
            total += 1
            if ranks[p] == 0:
                conv += 1
    sig_of = {p: tuple(sig[(p, r)] for r in ROWS) for p in space}
    qconv = 0
    for variant in (True, False):
        for start in space:
            p = descend_qwalk(start, ranks, nbr_c, sig_of, variant)
            if ranks[p] == 0:
                qconv += 1
    print("    landscape B=%d W=%d: single-move stalls above min %d "
          "%s | cure-set stalls above min %d | cure-set descent "
          "%d/%d | quotient descent %d/%d to bottom"
          % (B, W, len(st_single),
             [fmt_pol5(p) for p in st_single[:4]],
             len(st_cure), conv, total, qconv, total))
    return set(st_cure), conv == total, qconv == total

def summarize_class(cls):
    """Group a policy class by (sigma, delta), counting patiences."""
    groups = {}
    for p in cls:
        groups.setdefault((p[0], p[1], p[4]), []).append((p[2], p[3]))
    parts = []
    for (st, ss, d) in sorted(groups,
                              key=lambda k: (k[0], k[1],
                                             99 if k[2] is None
                                             else k[2])):
        parts.append("sigma=(%d,%d) delta=%s x%d"
                     % (st, ss, "ALL" if d is None else d,
                        len(groups[(st, ss, d)])))
    return "; ".join(parts)

def e6_diagnostics(imgs):
    """Post-run probes, added after the first run to read the two
    refuting structures: the theta8 optimum shift at B=4 W=2 and
    the cure-surviving stalls at B=3 W=8."""
    print("E6 POST-RUN DIAGNOSTICS")
    # (a) the theta8 shift at B=4, W=2
    B, W = 4, 2
    daxis = d_axis(W)
    space = policy_space5(AX_BASE, daxis)
    tab, sig = bank_table(imgs, space, B, W)
    row = ("id", "theta8")
    best = min(space, key=cmp_to_key(
        lambda x, y: cmp_lex(tab[(x, row)], tab[(y, row)])))
    cls = [p for p in space if cmp_lex(tab[(p, row)],
                                       tab[(best, row)]) == 0]
    print("  (a) theta8 argmin at B=4 W=2: %s" % summarize_class(cls))
    for st_ in (0, 1):
        for ss_ in (0, 1):
            cells = []
            for d in daxis:
                p = (st_, ss_, 0, 0, d)
                cells.append("d=%s %.3f"
                             % ("ALL" if d is None else d,
                                ln_loss(tab[(p, row)])))
            print("    sigma=(%d,%d) greedy ln-loss: %s"
                  % (st_, ss_, "  ".join(cells)))
    inter = None
    for r in ROWS:
        b = min(space, key=cmp_to_key(
            lambda x, y: cmp_lex(tab[(x, r)], tab[(y, r)])))
        c = set(p for p in space
                if cmp_lex(tab[(p, r)], tab[(b, r)]) == 0)
        inter = c if inter is None else inter & c
    print("    all-rows intersection at B=4 W=2: %s"
          % summarize_class(sorted(
              inter, key=lambda p: (p[0], p[1],
                                    99 if p[2] is None else p[2],
                                    99 if p[3] is None else p[3]))))
    print("    intersection patiences: %s"
          % sorted(set((p[2], p[3]) for p in inter)))
    # (b) the cure-surviving stalls at B=3, W=8
    B, W = 3, 8
    daxis = d_axis(W)
    space = policy_space5(AX_BASE, daxis)
    tab, sig = bank_table(imgs, space, B, W)
    losses = {p: agg([tab[(p, r)] for r in ROWS]) for p in space}
    ranks = rank_map(space, losses, cmp_lex)
    nbr_c = lambda p: neighbors_cure(p, AX_BASE, daxis)
    stalls = [p for p in stalls_of(space, ranks, nbr_c)
              if ranks[p] > 0]
    bottom = [p for p in space if ranks[p] == 0]
    rep = bottom[0]
    print("  (b) B=3 W=8 bottom class: %s" % summarize_class(bottom))
    for p in stalls:
        print("    cure-set stall %s rank %d aggregate ln-gap %.4f"
              % (fmt_pol5(p), ranks[p],
                 ln_loss(losses[p]) - ln_loss(losses[rep])))
        ties = [q for q in space if cmp_lex(losses[q], losses[p]) == 0]
        twins = [q for q in ties if q != p and
                 all(sig[(q, r)] == sig[(p, r)] for r in ROWS)]
        print("      LEX ties %d | behavioral twins %s"
              % (len(ties), [fmt_pol5(q) for q in twins]))
        rowcmp = " ".join(
            "%s%s" % (fmt_row(r),
                      {-1: "<", 0: "=", 1: ">"}[
                          cmp_lex(tab[(p, r)], tab[(rep, r)])])
            for r in ROWS)
        print("      per-row vs bottom rep: %s" % rowcmp)
    ends = {}
    for variant in (True, False):
        for start in space:
            p, _ = descend(start, ranks, nbr_c, variant)
            key = "BOTTOM" if ranks[p] == 0 else fmt_pol5(p)
            ends[key] = ends.get(key, 0) + 1
    for k in sorted(ends, key=lambda k: -ends[k]):
        print("    descent endpoint %s: %d" % (k, ends[k]))
    # (c) QUOTIENT DESCENT: strict moves plus tie-walks along
    # behavioral identity (identical signatures on every row) —
    # descent on the quotient poset of counted-window behaviors
    sig_of = {p: tuple(sig[(p, r)] for r in ROWS) for p in space}
    conv = 0
    for variant in (True, False):
        for start in space:
            p = descend_qwalk(start, ranks, nbr_c, sig_of, variant)
            if ranks[p] == 0:
                conv += 1
    print("  (c) quotient descent (tie-walks along behavioral "
          "identity) at B=3 W=8: %d/%d to bottom"
          % (conv, 2 * len(space)))

def descend_qwalk(start, ranks, nbr_fn, sig_of, best_improve):
    """Strict descent, but ties may be crossed when the tied
    neighbor is behaviorally identical (a plateau of one quotient
    node); a visited set prevents cycling."""
    p = start
    visited = {p}
    while True:
        nbs = nbr_fn(p)
        if best_improve:
            nbs = sorted(nbs, key=lambda q: ranks[q])
        moved = False
        for q in nbs:
            if ranks[q] < ranks[p]:
                p = q
                visited.add(p)
                moved = True
                break
        if moved:
            continue
        for q in nbs:
            if q not in visited and ranks[q] == ranks[p] \
                    and sig_of[q] == sig_of[p]:
                p = q
                visited.add(p)
                moved = True
                break
        if not moved:
            return p

def e5_bank_watch(imgs):
    print("E5 THE BANK WATCH (bank traces, greedy spend-all, W=8)")
    for B in (2, 3):
        for row in ROWS:
            r = run_reader_banking(imgs[row], GREEDY5, N_MAIN, B, 8)
            bt, dt = r[4], r[5]
            events = []
            cur = 0
            for x in dt:
                if x > 0:
                    cur += x
                elif cur:
                    events.append(cur)
                    cur = 0
            if cur:
                events.append(cur)
            print("  B=%d %s: bank min %d max %d mean %.2f | drain "
                  "events %d sizes %s"
                  % (B, fmt_row(row), min(bt), max(bt),
                     sum(bt) / len(bt), len(events), events[:14]))

def main():
    imgs = build_images(N_MAIN)
    if not e1_controls(imgs):
        print("CONTROLS FAILED — no verdicts")
        return 1

    print("E3/E4 THE PRINCIPAL QUESTION + THE LANDSCAPE, per setting")
    unthr = {row: run_reader(imgs[row], (0, 0, 0, 0), True,
                             N_MAIN)[:3] for row in ROWS}
    greedy_tabs = {}
    all_inter = all_gap = all_spendall = all_q = True
    delta0_ok = True
    univ_map = {}
    inter_map = {}
    cure_stalls_map = {}
    for B in BUDGETS:
        w0_tab = None
        for W in CAPS:
            daxis = d_axis(W)
            space = policy_space5(AX_BASE, daxis)
            tab, sig = bank_table(imgs, space, B, W)
            greedy_tabs[(B, W)] = {row: tab[(GREEDY5, row)]
                                   for row in ROWS}
            QTABS[(B, W)] = {((st_, ss_, 0, 0, INF_D), row):
                             tab[((st_, ss_, 0, 0, INF_D), row)]
                             for st_ in (0, 1) for ss_ in (0, 1)
                             for row in ROWS}
            if W == 0:
                w0_tab = {(p4, row): tab[(p4 + (INF_D,), row)]
                          for p4 in policy_space4(AX_BASE)
                          for row in ROWS}
            else:
                # C1 (ii): the delta = 0 slice == the W = 0 tables
                for p4 in policy_space4(AX_BASE):
                    for row in ROWS:
                        if tab[(p4 + (0,), row)] != w0_tab[(p4, row)]:
                            delta0_ok = False
            pw, univ, inter, gap, spendall = \
                e3_argmin(tab, sig, space, B, W)
            st_cure, cure_conv, q_conv = \
                e4_landscape(tab, sig, space, B, W)
            univ_map[(B, W)] = univ
            inter_map[(B, W)] = inter
            cure_stalls_map[(B, W)] = st_cure
            all_inter &= len(inter) > 0
            all_gap &= gap
            all_spendall &= spendall
            all_q &= q_conv
    if PW_FAILS:
        print("  pointwise failures (finite delta beats spend-all): "
              "%d total" % len(PW_FAILS))
        rows_hit = {}
        for f in PW_FAILS:
            rows_hit.setdefault(f[3], []).append(f)
        for r, fs in rows_hit.items():
            print("    %s: %d failures, ln-gaps %.4f..%.4f, bases %s"
                  % (fmt_row(r), len(fs),
                     min(x[5] for x in fs), max(x[5] for x in fs),
                     sorted(set(x[2] for x in fs))))
    check("C1(ii): delta=0 slice reproduces W=0 exactly at every "
          "(B, W>0), all 100 base policies x 8 rows", delta0_ok)
    # C3's frozen pointwise clause is REFUTED (route-locking is
    # real); the found census is encoded so reruns guard the record
    census = {}
    for f in PW_FAILS:
        census[f[3]] = census.get(f[3], 0) + 1
    check("route-locking census: withholding strictly beats "
          "spend-all exactly 83 times at scope (sq/phi 36, "
          "id/sqrt2 36, dbl/sqrt2 6, id/theta8 5)",
          census == {("sq", "phi"): 36, ("id", "sqrt2"): 36,
                     ("dbl", "sqrt2"): 6, ("id", "theta8"): 5})
    check("the destination is schedule-free: every per-row argmin "
          "class contains a spend-all policy at every setting",
          all_spendall)
    check("per-setting universality: the all-rows argmin "
          "intersection is nonempty at every setting", all_inter)
    # C3's frozen universal candidate is REFUTED at one setting;
    # the found environment-dependence is encoded
    b42 = set((0, ss_, 0, 0, d) for ss_ in (0, 1)
              for d in (1, INF_D))
    check("the throttled universal (1,1,greedy,spend-all) is "
          "universal at every setting EXCEPT (B,W)=(4,2), where "
          "the universal set is sigma in {(0,0),(0,1)} at greedy "
          "patience, delta >= 1 (route order inverts on theta8)",
          all(univ_map[k] == (k != (4, 2)) for k in univ_map)
          and inter_map[(4, 2)] == b42)
    check("C3 ensembles: transfer gaps exactly zero at every "
          "setting", all_gap)
    # C4's frozen funnel clause is REFUTED at (3,8); the found
    # degenerate ridge and its quotient cure are encoded
    ridge = set((1, 1, 0, 2, d) for d in (2, 4, INF_D))
    check("the cure set converges everywhere except (B,W)=(3,8), "
          "whose stalls are exactly the degenerate ridge "
          "{sigma=(1,1) patience=(0,2) delta>=2}",
          all(cure_stalls_map[k] == (ridge if k == (3, 8) else set())
              for k in cure_stalls_map))
    check("THE QUOTIENT FUNNEL: quotient descent (strict moves + "
          "tie-walks along behavioral identity) converges from "
          "every start at every setting", all_q)
    e2_smoothing(imgs, greedy_tabs, unthr)
    e5_bank_watch(imgs)
    e6_diagnostics(imgs)

    print()
    if FAILURES:
        print("RESULT: %d FAILURES %s" % (len(FAILURES), FAILURES))
        return 1
    print("RESULT: ALL ENGINES PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
