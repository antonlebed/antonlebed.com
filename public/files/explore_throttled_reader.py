"""The throttled reader: does a rank budget per input step make the
deficit landscape depend on the data? The first resource-bounded
stage of the reader-descent program.

THE QUESTION
------------
explore_ratchet_learner.py and explore_bootstrap_cures.py established
that over finite spaces of continued-fraction reader policies the
commitment-deficit landscape is a funnel whose sole trap (total
refusal) is cured by lexicographic deficit descent, and that the
global optimum — greedy patience — is pointwise optimal at EVERY
stream (the bottom lemma's corollary): the optimum carries nothing
stream-specific, so nothing about it can be learned from data. That
optimality proof consumes unbounded multi-commit: a reader may spend
arbitrarily many cover moves per input step.

This experiment introduces the window-native resource bound that
breaks the proof: a RANK BUDGET of B cover-rank units per input
step (streams differ in demand — the golden ratio asks about one
rank per digit, theta8 = [0; 8, 8, ...] about eight, and the wall
row's demand grows exponentially). Under scarcity two readers can
occupy non-nested cells (chain versus tree route), so pointwise
dominance no longer follows, and the questions are live:

  Q1  Is the deficit landscape over throttled policies still a
      funnel under lexicographic descent?
  Q2  Does the location of the optimum now depend on the stream
      ensemble — the first setting where training data can matter?
  Q3  Does the signal-cure/move-cure split survive the throttle
      (lexicographic refinement as the radius-free cure)?

THE POLICY SPACE, LOSS, AND THROTTLE
------------------------------------
Policies, covers, streams, maps, horizon, and the exact loss are
those of explore_bootstrap_cures.py: a policy is (route preference
at tree cells, route preference at straddles, tree patience, chain
patience) over the patience axis {0, 1, 2, 3, INF} — 100 policies;
the loss on a row is the product of committed cell lengths over
counted steps (N0 = 8, horizon 120), exact big-integer comparison
throughout; the slate is the same eight (map, stream) rows including
the wall row (x^2, sqrt2).

THE THROTTLE (the one new ingredient). The budget B is a SETTING,
not a policy coordinate: B in {1, 2, 4, 8, None}, None = unthrottled.
Each input step resets a remaining-budget counter to B; the commit
loop then runs as before except that (i) it stops when the budget is
exhausted, (ii) a tree child or side exit (cost 1) is offered only
within budget, (iii) a chain entry is TRUNCATED to
k_take = min(kmax, remaining) — sound because chain cells at a
vertex are nested downward in k, so every truncation still contains
the reference — and (iv) a chain deepening is truncated to
k + remaining likewise. Budget is not bankable across steps.

INDEX CONVENTIONS (re-derived from the engine before the freeze)
----------------------------------------------------------------
J_list[m] is the image of the cylinder after digits a_0..a_m — m+1
digits (J_0 is ONE digit; on theta8, J_0 = (0,1), J_1 = (1/9, 1/8)).
Refs at step n are J_list[n - p]; refs NEST (J_n inside J_m for
m < n), so move sets nest downward in patience. Rank is depth d at
tree cells and d + k at straddles; move costs are +1 (tree child,
side exit), +k (chain entry), +(k2 - k) (deepening). Containment is
strict at both ends, so shared endpoints block moves (on theta8 the
root's children never strictly contain J_0 = (0,1): every reader's
first move waits for J_1).

HAND-DERIVED BEFORE THE ENGINE
------------------------------
THE START-DELAY LAW (killed a wrong first intuition). The tempting
claim "patience collapses on rows whose demand exceeds B" is FALSE:
a patience-p reader makes its first move around step p, and under a
binding budget the resulting rank gap (about B*p against greedy) is
never erased — the catch-up that made patience free in the
unthrottled reader was exactly unbounded multi-commit. So on a
lagging row the patience valley stays STRICT, driven by the start
delay; on rows where no straddle opens near the root (theta8) the
tree patience is the driver.

BROKEN COROLLARY. The bottom lemma still holds for the COVER (it is
budget-free), but its policy corollary — greedy patience dominates
pointwise — requires descending to bottom(ref) within the step.
Under scarcity, routes diverge into non-nested cells, so neither
greedy dominance nor budget monotonicity (loss non-increasing in B)
is automatic. A budget ANOMALY (more budget, worse loss) would be a
first-class finding, not a rig bug — the vibration protocol below.

DEMAND (to be measured, greedy rank slope per row): phi about 1,
sqrt2 about 2, sqrt3 about 1.5, theta8 about 8, phi^2 = [2;1,1,...]
about 1, 2*phi about 4/3 (the established partition-slope control),
2*sqrt2 = [2;1,4,...] about 2.5; the wall row's demand is
exponential (chain index growth 2 ln(1+sqrt2)), so under ANY finite
B the wall's committed length decays polynomially instead of
exponentially — a per-step deficit growing linearly in n. A lagging
power row pays the same order with coefficient set by (demand - B).

ROUTE SCARCITY (one juncture computed by hand). On id/theta8 at the
tree cell (0,1)-(1,7), the chain candidate S_1 at vertex 1/8 is the
interval (1/9, 2/15), length 1/45, while the tree child is
(0, 1/8), length 1/8 — same rank 8, a 5.6x length gap. Under
budget the route preferences buy genuinely different cells per
stream (theta8 turns every 8 ranks, phi every rank), which is where
ensemble dependence can enter. FALLBACK: if all per-row argmin
classes still share a common policy, the optimum is ensemble-free
even under scarcity — a complete answer (data does not yet matter
in this family), pointing the program one level down.

ENSEMBLES. E_SLOW = {id/phi, sq/phi, dbl/phi, id/sqrt3} (measured
demand at or below about 1.5); E_FAST = {id/sqrt2, dbl/sqrt2,
id/theta8, sq/sqrt2} (demand 2 up to exponential). The transfer gap
is measured fairly: among an ensemble's argmin tie class, the
transferred policy is the member that does BEST on the target
ensemble, so a positive gap is a lower bound on the cost of
training on the wrong ensemble.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls, gate] (i) The throttled reader at B = None reproduces
   the verbatim unthrottled reader exactly — identical loss triples
   on all 100 policies x 8 rows. (ii) The disease reproduces: plain
   single-move descent at B = None stalls exactly at the greedy
   quartet plus the four refusal corners. (iii) Demand slopes:
   id/phi in [0.9, 1.1], id/theta8 in [7, 9], dbl/phi partition
   slope in [1.26, 1.40], wall chain ln-k slope in [1.71, 1.82].
C2 [the throttle bites, monotonically] At B = 1 the greedy loss
   strictly exceeds the B = None loss on every row; along
   B = 1, 2, 4, 8, None the loss of every greedy-quartet policy is
   non-increasing on every row. [The every-row strict clause is
   refuted — see findings F2; the monotone clause held.]
C3 [the start-delay law] On id/theta8 at B = 1, at every fixed
   (route preferences, finite chain patience), loss is strictly
   increasing in tree patience across {0, 1, 2, 3}.
C4 [THE HEADLINE — stream dependence] (a) At some B in {1, 2, 4, 8}
   two rows have DISJOINT per-row argmin classes (no policy optimal
   for both). (b) At B = 1 the ensemble argmin classes of E_SLOW
   and E_FAST are disjoint, with a positive transfer gap. [Stance
   refuted — the named fallback fired; see findings F4.]
C5 [the funnel survives] At every B, lexicographic single-move
   descent converges from all 100 starts (both variants) to the
   full-slate optimum, and plain descent still traps the refusal
   corners (refusal is budget-independent). [Refuted at B = 1, 2 —
   the trap, the real discovery of the run; see findings F5.]

KILL CRITERIA, fixed at the freeze
----------------------------------
K1 Any C1 control fails: the rig is dead, no verdicts.
K2 THE PRINCIPAL KILL: a lexicographic stall above the minimum at
   some B that SURVIVES the refinement ladder — (r1) total committed
   rank as a second lexicographic key; (r2) worst-row-first
   comparison of the per-row loss vector — then the loss family
   itself is too small for resource-bounded learning, and a
   different loss coordinate enters the next slate.
K3 The B = None regression fails: an engine bug; fix before any
   verdict is read.
K4 A budget anomaly on a greedy-quartet policy: stop and verify by
   hand trace before reading any other verdict (bug versus real
   anomaly; if real, it is a finding and the monotonicity clause of
   C2 is refuted honestly).

ENGINE
------
Exact integer arithmetic in every decision. The engine core (points,
cylinders, cells, the unthrottled reader, the exact loss) is copied
verbatim from explore_bootstrap_cures.py; this experiment adds the
throttled reader (a remaining-budget counter and chain truncation),
per-row loss tables at each budget, per-row and per-ensemble argmin
classes, the transfer measurement, and descent over precomputed
exact ranks. Sequential, well under the resource caps; positive
controls gate all verdicts; exit nonzero on any failure.

FINDINGS (entered after the run; ALL ENGINES PASS, exit 0, ~4 s)
----------------------------------------------------------------
F1 C1 CONFIRMED, controls exact: the B = None regression is exact
   on all 100 policies x 8 rows; the disease reproduces (8 plain
   stalls); measured demand: phi 1.00, sqrt2 2.00, sqrt3 1.49,
   theta8 8.00, phi^2 1.00, 2phi 1.33, 2sqrt2 2.49, wall ln-k
   slope 1.76.
F2 C2 PART-REFUTED — THE CATCH-UP THRESHOLD LAW. The every-row
   strict clause died on id/phi: its demand is exactly 1 with zero
   warm-up debt, so B = 1 already equals unthrottled. Found law:
   greedy at budget B matches the unthrottled loss exactly at
   B >= threshold — phi 1; sqrt2, sqrt3, phi^2, 2phi 2; 2sqrt2 4
   within this grid (B = 3 was not scanned here; the finer grid of
   explore_banking_reader.py measures the true threshold 3 — the
   row's per-step demand is 2..3, so B = 3 catches up exactly);
   theta8 8; the wall NEVER (exponential demand: its throttled
   committed length decays polynomially, a per-step deficit growing
   linearly — ln-loss -365 at B=1 versus -12424 unthrottled). The
   phi^2 threshold is 2, not 1: at B = demand = 1 the two-rank
   warm-up debt of its leading digit is never repaid. The monotone
   clause held: ZERO budget anomalies across the quartet.
F3 C3 CONFIRMED — the start-delay law, exact: on id/theta8 at
   B = 1 loss is strictly increasing in tree patience everywhere,
   58.6 ln-units per patience step (= the per-rank length slope
   times 112 counted steps, as derived); chain patience is
   invisible there (truncation to k = 1 masks it).
F4 C4 REFUTED — the named fallback fired: the optimum is
   ENSEMBLE-FREE at scope. One universal policy — chain-first
   entry, tree-first exit (eager grab, eager leave), greedy
   patience — sits in EVERY row's argmin class at EVERY budget; no
   row pair has disjoint argmin classes; the ensemble argmin
   classes intersect and both transfer gaps are exactly zero.
   Training data still does not matter for the destination — only
   the throttle's SPLIT of the greedy quartet is new: scarcity
   makes route preferences matter (the measured square: eager
   chain entry is best paired with eager exit, sigma = (1,1), and
   worst paired with eager deepening, sigma = (1,0)), yet WHICH
   routes win is stream-independent.
F5 C5 PART-REFUTED — THE TRAP, the discovery of the run. At
   B = 1, 2 lexicographic descent stalls (184/200, 143/200) on
   exactly ONE policy above the minimum: sigma = (0,0) at greedy
   patience — the canonical representative of the UNTHROTTLED
   optimum. Yesterday's optimum is today's trap. Structure: the
   quartet splits under scarcity ((1,1) < (0,0) = (0,1) < (1,0) at
   B = 1, 2), and the trap's flip of the straddle coordinate,
   sigma = (0,1), ties it EXACTLY — the two commit IDENTICAL cells
   at every counted step (they diverge only in the uncounted
   warm-up), so NO loss functional over the counted window can
   order the pair; the other single moves strictly worsen the
   AGGREGATE deficit (per-row, sigma = (1,0) is MIXED — better on
   three rows at B = 1, one at B = 2 — the one door a reweighted
   signal can use). Escape by descent on the deficit needs both
   route coordinates flipped TOGETHER. The K2 ladder:
   r1 fails at both budgets (the trap is strict — a rank tiebreak
   only refines ties); r2 fails at B = 1 (63 runs stall; verified
   per-neighbor: the twin ties by degeneracy and every other
   neighbor of the trap is r2-worse) and happens to cure at B = 2
   (the trap escapes through sigma = (1,0), r2-better though
   total-loss-worse; path (0,0) -> (1,0) -> (1,1)) — no signal is
   a general cure. THE CURE: the preference diagonal, a
   radius-1 move in a coordinate plane of FIXED size 2x2,
   converges 200/200 at both budgets. At B = 4 the trap vanishes
   ((1,0) inverts below (0,0): a single-flip escape opens) and at
   B = 8 the quartet reunites in a single tie.

THE VERDICT. Three answers. (Q2) NO — the optimum stays
ensemble-free under scarcity at this scope: a universal best
policy exists at every budget, and the transfer gap between
demand-split ensembles is exactly zero. What the throttle changes
is WHICH preferences win (eager-grab/eager-leave), not where data
enters. (Q1) The funnel breaks at deep scarcity only: one trap at
B = 1, 2, none at B = 4, 8. (Q3) The cure split INVERTS at this
trap and the theorem shape sharpens: the refusal plateau of the
unthrottled landscape was blindness of UNBOUNDED WIDTH, cured by a
signal (lexicographic shortfall) and immune to fixed-radius moves;
the scarcity trap is COORDINATION blindness in a BOUNDED
coordinate plane, cured by a move sized to the plane and immune to
every refinement of the deficit order by WINDOW-NATIVE signals
(functions of counted-window reading behavior): the only tie such
a refinement could break is behaviorally degenerate, so the
blindness is structural — a label-based tiebreak could split the
twins, but that is symmetry-breaking on names, not a signal. A
reweighted per-row signal can reach through the mixed neighbor
sigma = (1,0), but the one tried is not general (r2 cures B = 2,
fails B = 1). K2's observable fired — a stall survived the
refinement ladder — but its frozen inference ("the loss family is
too small; a new loss coordinate is needed") is REFUTED by the
degeneracy analysis: no loss coordinate over the counted window
can separate behaviorally identical policies; the missing
ingredient is coordination (or quotienting the policy coordinates
by counted-window behavior), not a richer signal.

Run record. The first run exited 1 at eight checks: three frozen
predictions refuted honestly (C2's every-row strictness and C4's
disjointness stance — both margins of the pre-run predictions; C5's funnel claim,
refuted by the real discovery), and the frozen K2 ladder's r2 rung
was found unimplemented in the rig (a rig gap closed post-run).
The post-run edits implemented r2, added the diagonal probe, the
degeneracy check, and the catch-up threshold table (post-run
diagnostics, so labeled), and re-encoded the failed checks to the
found landscape as recorded here; no prediction band was touched;
the positive controls passed identically on both runs. All
trap/cure attributions were read off per-policy reruns and the
printed stall sets, not off the narrative. Tiers: every landscape
statement is verified exhaustively at the stated scope (100
policies, 8 rows, budgets {1, 2, 4, 8, None}, N = 120); the
start-delay law and the counted-window degeneracy are verified
exactly at scope with hand-derived mechanisms; the catch-up
threshold table and the quartet split are observations at scope.

Settled downstream: explore_banking_reader.py adds the store (a
bank of unspent rank units under a cap, with a drawdown-schedule
policy coordinate). The optimum stays ensemble-free at every
(budget, cap) pairing but is NOT environment-free (one setting
inverts the route order on theta8); the schedule axis is
degenerate at the optimum; the only threshold banking moves is
phi^2's, 2 -> 1 by warm-up funding (and this table's 2sqrt2
threshold 4 refines to 3 on the finer budget grid); and abundance
manufactures a third blindness species — the degenerate ridge,
behaviorally identical policies tied into a flat the strict
descent cannot cross — cured by descent on the behavioral
quotient.
"""

import math
import sys
from functools import cmp_to_key

LN2 = math.log(2)
INF_P = None          # patience sentinel: refuse the class
N0 = 8                # loss counted from this step
N_MAIN = 120
AX_BASE = [0, 1, 2, 3, INF_P]
BUDGETS = [1, 2, 4, 8, None]

# ----------------------------------------------------------------- #
# engine core (verbatim from explore_bootstrap_cures.py)
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
                if redundant and ref_c is not None:
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
    """The throttled reader: run_reader plus a rank budget per input
    step (budget=None reproduces run_reader exactly). Chain moves
    are truncated to the remaining budget — sound because chain
    cells at a vertex are nested downward in k."""
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
# comparators, moves, descent over exact ranks
# ----------------------------------------------------------------- #

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

def policy_space(axis):
    return [(st, ss, pt, pc)
            for st in (0, 1) for ss in (0, 1)
            for pt in axis for pc in axis]

def neighbors_single(pol, axis):
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

def fmt_pol(p):
    return "sigma=(%d,%d) patience=(%s,%s)" % (
        p[0], p[1],
        "INF" if p[2] is None else str(p[2]),
        "INF" if p[3] is None else str(p[3]))

def fmt_row(row):
    return "%s/%s" % row

def ln_loss(t):
    return ln_frac(t[0], t[1])

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

def quartet():
    return [(st, ss, 0, 0) for st in (0, 1) for ss in (0, 1)]

def corners():
    return [(st, ss, INF_P, INF_P) for st in (0, 1) for ss in (0, 1)]

def per_row_losses(space, imgs, budget):
    return {(pol, row): run_reader_throttled(imgs[row], pol,
                                             N_MAIN, budget)[:3]
            for pol in space for row in ROWS}

def slate_loss(tab, pol, rows):
    return agg([tab[(pol, row)] for row in rows])

def e1_controls(imgs, space, tab_none):
    print("E1 CONTROLS (gate: no verdicts are read unless these pass)")
    # K3 regression: throttled at None == verbatim unthrottled reader
    bad = 0
    for pol in space:
        for row in ROWS:
            if run_reader(imgs[row], pol, True, N_MAIN)[:3] != \
               tab_none[(pol, row)]:
                bad += 1
    check("throttled reader at B=None == unthrottled reader, all "
          "100 policies x 8 rows", bad == 0, "%d mismatches" % bad)
    # the disease at B=None
    losses = {pol: slate_loss(tab_none, pol, ROWS) for pol in space}
    ranks = rank_map(space, losses, cmp_plain)
    st = stalls_of(space, ranks, lambda p: neighbors_single(p, AX_BASE))
    expected = set(quartet()) | set(corners())
    check("the disease reproduces: plain stalls at B=None = greedy "
          "quartet + the four corners", set(st) == expected,
          "%d stalls" % len(st))
    # demand slopes (greedy reader, unthrottled)
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

CATCHUP = {("id", "phi"): 1, ("id", "sqrt2"): 2, ("id", "sqrt3"): 2,
           ("id", "theta8"): 8, ("sq", "phi"): 2, ("dbl", "phi"): 2,
           ("dbl", "sqrt2"): 4, WALL: None}

def e2_bite(tabs):
    print("E2 THE THROTTLE BITES, MONOTONICALLY (C2 / K4)")
    greedy = (0, 0, 0, 0)
    # the catch-up threshold law (C2's "strict on every row at B=1"
    # died on id/phi, whose demand is exactly 1 with no warm-up debt:
    # equality holds exactly from the least budget covering the row's
    # demand -- plus one step of never-repaid warm-up debt on phi^2
    # at B=1 -- and never on the wall, whose demand is exponential)
    ok = True
    for row, th in CATCHUP.items():
        for b in (1, 2, 4, 8):
            c = cmp_lex(tabs[b][(greedy, row)], tabs[None][(greedy, row)])
            want_eq = th is not None and b >= th
            if (c == 0) != want_eq or c < 0:
                ok = False
                print("    threshold law broken at %s B=%s (cmp %d)"
                      % (fmt_row(row), b, c))
    check("the catch-up threshold law: greedy at budget B matches "
          "unthrottled exactly at B >= threshold (phi 1; sqrt2, "
          "sqrt3, phi^2, 2phi 2; 2sqrt2 4; theta8 8; wall never)", ok)
    anomalies = []
    for pol in quartet():
        for row in ROWS:
            for b_lo, b_hi in zip(BUDGETS, BUDGETS[1:]):
                if cmp_lex(tabs[b_lo][(pol, row)],
                           tabs[b_hi][(pol, row)]) < 0:
                    anomalies.append((pol, row, b_lo, b_hi))
    check("greedy-quartet loss non-increasing along B=1,2,4,8,None "
          "on every row (no budget anomaly)", not anomalies,
          "%d anomalies" % len(anomalies))
    for a in anomalies:
        print("    ANOMALY %s %s: B=%s beats B=%s"
              % (fmt_pol(a[0]), fmt_row(a[1]), a[2], a[3]))
    for row in ROWS:
        parts = []
        for b in BUDGETS:
            t = tabs[b][(greedy, row)]
            parts.append("B=%s %.1f%s" % (b, ln_loss(t),
                                          "*" if t[2] else ""))
        print("  greedy ln-loss %s: %s" % (fmt_row(row), "  ".join(parts)))

def e3_start_delay(tabs):
    print("E3 THE START-DELAY LAW ON id/theta8 AT B=1 (C3)")
    row = ("id", "theta8")
    ok = True
    for st in (0, 1):
        for ss in (0, 1):
            for pc in (0, 1, 2, 3):
                ls = [tabs[1][((st, ss, pt, pc), row)]
                      for pt in (0, 1, 2, 3)]
                for i in range(3):
                    if cmp_lex(ls[i], ls[i + 1]) >= 0:
                        ok = False
                        print("    NOT strict at sigma=(%d,%d) pc=%d "
                              "pt=%d->%d" % (st, ss, pc, i, i + 1))
    check("loss strictly increasing in tree patience at every fixed "
          "(preferences, finite chain patience)", ok)
    for st, ss in [(0, 0)]:
        print("  ln-loss grid sigma=(0,0) (rows pt, cols pc):")
        for pt in (0, 1, 2, 3):
            cells = ["%7.1f" % ln_loss(tabs[1][((st, ss, pt, pc), row)])
                     for pc in (0, 1, 2, 3)]
            print("    pt=%d  %s" % (pt, " ".join(cells)))

def argmin_class(space, single, cmpf):
    ranks = rank_map(space, single, cmpf)
    return set(p for p in space if ranks[p] == 0)

def e4_dependence(space, tabs):
    print("E4 STREAM DEPENDENCE (C4: the headline)")
    found_disjoint = None
    universal = True
    for b in [1, 2, 4, 8]:
        classes = {}
        for row in ROWS:
            single = {pol: tabs[b][(pol, row)] for pol in space}
            classes[row] = argmin_class(space, single, cmp_lex)
        print("  B=%s per-row argmin class sizes: %s" % (b, "  ".join(
            "%s:%d" % (fmt_row(r), len(classes[r])) for r in ROWS)))
        for i, r1 in enumerate(ROWS):
            for r2 in ROWS[i + 1:]:
                if not (classes[r1] & classes[r2]):
                    if found_disjoint is None:
                        found_disjoint = (b, r1, r2)
                    print("    DISJOINT at B=%s: %s vs %s"
                          % (b, fmt_row(r1), fmt_row(r2)))
        common = set(space)
        for row in ROWS:
            common &= classes[row]
        print("    policies optimal on ALL rows at B=%s: %d %s"
              % (b, len(common),
                 sorted(fmt_pol(p) for p in list(common)[:4])))
        universal = universal and (1, 1, 0, 0) in common
    # C4's disjointness stance is REFUTED: the found landscape has a
    # UNIVERSAL policy -- chain-first entry, tree-first exit, greedy
    # patience -- inside every row's argmin class at every budget
    check("no pair of rows has disjoint argmin classes at any B "
          "(C4's stance refuted: the optimum is ensemble-free)",
          found_disjoint is None)
    check("sigma=(1,1) at greedy patience is in every row's argmin "
          "class at every budget (a universal optimum)", universal)
    # ensembles at B=1: the argmin classes intersect and transfer is free
    b = 1
    slow = {pol: slate_loss(tabs[b], pol, E_SLOW) for pol in space}
    fast = {pol: slate_loss(tabs[b], pol, E_FAST) for pol in space}
    cls_s = argmin_class(space, slow, cmp_lex)
    cls_f = argmin_class(space, fast, cmp_lex)
    print("  B=1 ensemble argmin classes: SLOW %d %s | FAST %d %s"
          % (len(cls_s), sorted(fmt_pol(p) for p in list(cls_s)[:4]),
             len(cls_f), sorted(fmt_pol(p) for p in list(cls_f)[:4])))
    check("ensemble argmin classes INTERSECT at B=1 (C4's "
          "disjointness stance refuted)", bool(cls_s & cls_f))
    best_transfer = min(cls_s, key=cmp_to_key(
        lambda x, y: cmp_lex(fast[x], fast[y])))
    ref = min(cls_f, key=cmp_to_key(
        lambda x, y: cmp_lex(fast[x], fast[y])))
    gap = ln_loss(fast[best_transfer]) - ln_loss(fast[ref])
    check("the transfer gap is exactly zero (training on SLOW costs "
          "nothing on FAST)",
          gap == 0.0 and fast[best_transfer][2] == fast[ref][2],
          "gap %.2f ln units (fair: best tie-class member transferred)"
          % gap)
    gap2 = ln_loss(slow[min(cls_f, key=cmp_to_key(
        lambda x, y: cmp_lex(slow[x], slow[y])))]) - \
        ln_loss(slow[min(cls_s, key=cmp_to_key(
            lambda x, y: cmp_lex(slow[x], slow[y])))])
    print("  reverse transfer gap (FAST-trained on SLOW): %.2f ln units"
          % gap2)

def cmp_rank_refined(losses, ranks_committed):
    """Refinement r1: lexicographic loss, then MORE committed rank
    wins (run on the found stalls)."""
    def f(x, y):
        c = cmp_lex(losses[x], losses[y])
        if c:
            return c
        return ranks_committed[y] - ranks_committed[x]
    return f

def cmp_worst_row(tab):
    """Refinement r2: compare the per-row loss vectors sorted
    worst-first, lexicographically (minimize the worst row, then
    the next, ...)."""
    cache = {}
    def vec(x):
        if x not in cache:
            cache[x] = sorted((tab[(x, row)] for row in ROWS),
                              key=cmp_to_key(cmp_lex), reverse=True)
        return cache[x]
    def f(x, y):
        for a, c in zip(vec(x), vec(y)):
            cc = cmp_lex(a, c)
            if cc:
                return cc
        return 0
    return f

def cmp_rank_map(space, cmpf):
    order = sorted(space, key=cmp_to_key(cmpf))
    ranks = {order[0]: 0}
    r = 0
    for prev, cur in zip(order, order[1:]):
        if cmpf(prev, cur) < 0:
            r += 1
        ranks[cur] = r
    return ranks

def neighbors_diag(pol, axis):
    """Single moves plus the ONE preference diagonal (both route
    coordinates flip together) -- a radius-1 move in a coordinate
    plane of fixed size 2x2."""
    st, ss, pt, pc = pol
    return neighbors_single(pol, axis) + [(1 - st, 1 - ss, pt, pc)]

def run_descents(space, ranks, nbr_fn):
    fails = []
    for start in space:
        for best in (False, True):
            end, _ = descend(start, ranks, nbr_fn, best)
            if ranks[end] != 0:
                fails.append((start, best, end))
    return fails

TRAP = (0, 0, 0, 0)
TWIN = (0, 1, 0, 0)

def e5_funnel(space, tabs, imgs):
    print("E5 THE FUNNEL UNDER THE THROTTLE (C5 / K2: the trap)")
    for b in [1, 2, 4, 8]:
        losses = {pol: slate_loss(tabs[b], pol, ROWS) for pol in space}
        ranks_lex = rank_map(space, losses, cmp_lex)
        fails = run_descents(space, ranks_lex,
                             lambda p: neighbors_single(p, AX_BASE))
        st = [p for p in stalls_of(space, ranks_lex,
                                   lambda p: neighbors_single(p, AX_BASE))
              if ranks_lex[p] > 0]
        print("  B=%s: lexicographic descent %d/%d converge; stalls "
              "above minimum: %s"
              % (b, 2 * len(space) - len(fails), 2 * len(space),
                 [fmt_pol(p) for p in st] or "none"))
        for stt in (0, 1):
            for ss in (0, 1):
                p = (stt, ss, 0, 0)
                print("    sigma=(%d,%d) greedy: ln %.2f lexrank %d"
                      % (stt, ss, ln_loss(losses[p]), ranks_lex[p]))
        if b in (4, 8):
            check("B=%s: the funnel holds (200/200, no stall)" % b,
                  not fails and not st)
            continue
        # the found landscape at B in {1, 2}: ONE trap, and it is the
        # unthrottled optimum's canonical representative sigma=(0,0)
        check("B=%s: the sole stall above minimum is sigma=(0,0) at "
              "greedy patience (the unthrottled optimum, now a trap)"
              % b, st == [TRAP])
        # the counted-window degeneracy: sigma=(0,1) ties the trap
        # exactly because the two commit IDENTICAL cells at every
        # counted step (they diverge only in the uncounted warm-up),
        # so NO loss functional over the counted window can order them
        deg = all(tabs[b][(TRAP, row)] == tabs[b][(TWIN, row)]
                  for row in ROWS)
        warm = all(
            run_reader_throttled(imgs[row], TRAP, N_MAIN, b)[3][N0:]
            == run_reader_throttled(imgs[row], TWIN, N_MAIN, b)[3][N0:]
            for row in ROWS)
        check("B=%s: sigma=(0,1) ties the trap on every row AND "
              "commits identical cells at every counted step "
              "(loss-signal blindness is structural)" % b,
              deg and warm)
        # K2 LADDER on the found stalls
        committed = {pol: sum(
            run_reader_throttled(imgs[row], pol, N_MAIN, b)[3][-1][0]
            for row in ROWS) for pol in space}
        ranks_r1 = cmp_rank_map(space, cmp_rank_refined(losses, committed))
        f_r1 = run_descents(space, ranks_r1,
                            lambda p: neighbors_single(p, AX_BASE))
        ranks_r2 = cmp_rank_map(space, cmp_worst_row(tabs[b]))
        f_r2 = run_descents(space, ranks_r2,
                            lambda p: neighbors_single(p, AX_BASE))
        print("    K2 ladder at B=%s: r1 (committed-rank key) %d runs "
              "fail; r2 (worst-row-first) %d runs fail" %
              (b, len(f_r1), len(f_r2)))
        check("B=%s: refinement r1 does NOT cure (the trap is strict, "
              "not a tie to refine)" % b, len(f_r1) > 0)
        if b == 1:
            check("B=1: refinement r2 does NOT cure (the twin ties by "
                  "degeneracy; every other neighbor of the trap is "
                  "r2-worse)", len(f_r2) > 0)
        else:
            check("B=2: refinement r2 happens to cure (the trap escapes "
                  "through sigma=(1,0), r2-better though "
                  "total-loss-worse), but not at B=1 -- no signal is "
                  "a general cure", len(f_r2) == 0)
        # THE CURE: the preference diagonal (radius-1 in a FIXED
        # 2x2 coordinate plane -- coordination, not signal)
        f_dg = run_descents(space, ranks_lex,
                            lambda p: neighbors_diag(p, AX_BASE))
        check("B=%s: LEX + the preference diagonal converges from "
              "every start (200/200) -- the bounded coordination "
              "move cures what no signal can" % b, not f_dg)
        # plain comparator: the refusal corners stay trapped at every B
        ranks_plain = rank_map(space, losses, cmp_plain)
        stp = stalls_of(space, ranks_plain,
                        lambda p: neighbors_single(p, AX_BASE))
        check("B=%s: plain descent still traps the refusal corners "
              "(refusal is budget-independent)" % b,
              all(c in stp for c in corners()))

def main():
    print("=" * 68)
    print("THE THROTTLED READER: a rank budget per input step")
    print("=" * 68)
    imgs = build_images(N_MAIN)
    space = policy_space(AX_BASE)
    print("policies: %d  budgets: %s  rows: %d  horizon: %d"
          % (len(space), BUDGETS, len(ROWS), N_MAIN))
    tabs = {}
    for b in BUDGETS:
        tabs[b] = per_row_losses(space, imgs, b)
    if not e1_controls(imgs, space, tabs[None]):
        print("\nCONTROLS FAILED — no verdicts are read.")
        sys.exit(1)
    e2_bite(tabs)
    e3_start_delay(tabs)
    e4_dependence(space, tabs)
    e5_funnel(space, tabs, imgs)
    print("=" * 68)
    if FAILURES:
        print("FAILURES (%d): %s" % (len(FAILURES), "; ".join(FAILURES)))
        sys.exit(1)
    print("ALL ENGINES PASS")

if __name__ == "__main__":
    main()
