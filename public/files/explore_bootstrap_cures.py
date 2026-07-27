"""The bootstrap cures: which cure for the refusal corner's blind
plateau scales when the reader-policy space grows — a refined signal
(lexicographic tiebreak) or a wider move set (patience diagonals)?

THE QUESTION
------------
explore_ratchet_learner.py established that the commitment-deficit
landscape over a finite space of continued-fraction reader policies
is a funnel with one blind corner: every committing policy descends
by exact monotone moves to the exact global optimum (greedy
patience, route-free), and the sole trap is total refusal — the
corner policy sits on a flat infinite plateau where every
single-coordinate neighbor also has infinite deficit, so strict
descent gets no signal. The blindness is move-set-relative, and two
window-native cures are visible in that experiment's own prints:

  LEX (the signal cure): keep the single-coordinate moves; refine
      the comparator lexicographically — finite deficit always
      beats infinite, and two infinite-deficit policies compare by
      their COMMITTED-SCALE SHORTFALL, the exact product of the
      finite committed cell lengths over counted steps (the finite
      part of the infinite loss, already computed by the loss
      aggregation; no new machinery, only a comparator).
  WIDE (the move cure): keep the plain comparator (infinite ties
      infinite); widen the move set with the four patience
      DIAGONALS — both patience coordinates step one place
      simultaneously. No corner special-casing: the diagonal is
      available everywhere.

Both cures must converge from EVERY start, including the corner,
staying monotone, decidable, and window-native. The experiment runs
both in one rig, first on the original policy space (patience axis
0,1,2,3,INF; 100 policies), then on a GROWN space (patience axis
0..7,INF; 324 policies — the axis extended to its maximum within
the counted window, since a reference J_{n-p} needs n - p >= 1 at
the first counted step n = 8). The datum is which cure survives
the growth.

THE POLICY SPACE AND LOSS (unchanged)
--------------------------------------
Policies, covers, streams, maps, horizon, and the exact loss are
exactly those of explore_ratchet_learner.py: a policy is (route
preference at tree cells, route preference at straddles, tree
patience, chain patience); the loss of a policy on the slate is
the product of its committed cell lengths over counted steps
(exact big-integer comparison; an infinite-length cell at a
counted step makes the loss infinite). Slate: eight (map, stream)
rows including the wall row (x^2, sqrt2). Horizon N = 120, loss
counted from n0 = 8.

HAND-DERIVED BEFORE THE ENGINE
------------------------------
THE BOTTOM LEMMA (proved; the engine verifies its statement at
every counted step). Fix a bounded nondegenerate open interval R
in (0, inf). Consider the commit moves on the mediant-straddle
cover, each move's target required to contain R strictly: from a
tree cell with endpoints (l, r) and vertex v = mediant(l, r), the
tree children (l, v), (v, r) and the chain entries S_k(v); from a
straddle S_k(v), the deepenings S_k'(v), k' > k, and the two side
exits (the index-k side pieces). Then:
 (1) Cells containing R are finitely many: the containing tree
     cells are an initial segment of the Stern-Brocot path toward
     R (at most one per depth; spine cells (a, inf) contain R only
     for the finitely many integers a below R; non-spine path
     cells shrink below len(R)); a chain cell S_k(v) containing R
     forces S_1(v) to contain R, and S_1(v) lies inside the cell
     of v, so chain vertices lie ON the containing path, each with
     finitely many admissible k. Side pieces are tree cells.
 (2) Every move strictly increases rank, so every commit sequence
     terminates.
 (3) Local confluence, three real cases. (A) tree child (v, r) vs
     chain entry S_k(v): R lies right of v and inside S_k, hence
     inside the side piece P_k = (v, r + kv); from S_k one side
     exit lands P_k; from (v, r) the run of children toward v —
     (v, r + v), (v, r + 2v), ... — descends to P_k with every
     intermediate containing R. (B) two chain cells at one vertex:
     deepen the shallower. (C) deepening S_k' vs side exit P_k:
     R lies in P_k', reached from S_k' by one side exit and from
     P_k by descending the run. Two tree children are disjoint,
     and two side pieces lie on opposite sides of v — those pairs
     cannot both contain R.
 (4) By Newman's lemma the normal form is unique; every containing
     cell is reachable from the root by containment-preserving
     moves, every maximal path ends at the same normal form, and
     every move shrinks the cell — so the normal form is contained
     in EVERY cell containing R: the containing sub-poset has an
     inclusion MINIMUM, bottom(R), and greedy multi-commit reaches
     it in any preference order.
Corollaries. (i) CONFLUENCE: at greedy patience the committed
sequence is preference-free — the cell-level identity that
explore_ratchet_learner.py measured at 355 route choices is a
theorem of the cover. (ii) POINTWISE GLOBAL OPTIMALITY: any
policy's committed cell at step n contains its reference interval,
which contains J_n, hence contains bottom(J_n) — greedy patience
dominates every policy at every step, in ANY policy space of this
family; the global minimum set is exactly the greedy quartet.
(iii) THE DIAGONAL VALLEY: along equal patience p the committed
cell is bottom(J_{n-p}), monotone under interval nesting.
TIGHTNESS: at MIXED patience the two references differ and the
fixed point can depend on preference — witness derived by hand at
(pt, pc) = (7, 6) on the identity-phi row, step 8: tree ref
J_1 = (3/2, 2), chain ref J_2 = (3/2, 5/3); from the root both
candidates exist, tree-first commits the spine cell (1, inf) and
is stuck (the chain at vertex 2 needs a reference strictly inside
(3/2, 3), and J_2 shares the endpoint 3/2), while chain-first
commits S_1(1) = (1/2, 2), finite. The single-reference
hypothesis of the lemma is tight.

THE PARTITION VALLEY (proved, all patience values). In the
partition cover the containing cells form one nested chain and
bottom = the greedy cell. By induction the partition reader at
patience p commits greedy(J_{n-p}) at every step n >= p, and
J_{n-p} inside J_{n-p'} for p < p' gives pointwise domination:
loss is monotone in patience, every p, every stream; strict
wherever the greedy rank grows inside the counted window; total
refusal (never committing) is the worst. [The strictness clause
as first frozen lacked one hypothesis — see findings F4: infinite
losses tie, so strictness needs the compared losses finite.]

THE WALL-ROW LAG LAW (hand-derived; REFUTED BY THE RUN — the
threshold rested on an indexing slip, see findings F4 and the run
record; kept as frozen). On the wall row the image points converge to 2; tree
moves stop at the spine cell (1, inf) forever, and the cure is
the chain at vertex 2, which requires a chain reference strictly
inside S_1(2) = (3/2, 3) — true of J_m exactly when m >= 2. At
the first counted step n = 8 a policy therefore commits a finite
cell on the wall row iff 8 - pc >= 2, i.e. pc <= 6: EVERY policy
with pc in {7, INF} holds an infinite cell at a counted step. In
the grown space the infinite region is thus an L-shaped THICK
region — all of {pc in {7, INF}} plus all of {pt = INF} (chain
readers cannot make the first tree move) — with a jagged,
partially preference-dependent fringe of strays (the (7, 6)
witness above at tree-first preference), set per-row by which
early references bottom on spine cells.

THE SEPARATION (the predicted headline; its CORE confirmed, its
census refuted downstream of the lag law — see findings F5). In the grown space the
corner's ENTIRE neighborhood — (7, INF), (INF, 7), the diagonal
(7, 7), the preference flips — lies in the infinite region (the
diagonal lands on chain ref J_1, which no straddle strictly
contains), so WIDE stalls at the corner: a wider move set cures
the plateau only while its landing policies already read at every
counted step, and growing the patience axis pushes the finite
region outside any fixed move radius. The same argument stalls
WIDE on the whole tree-only column (every neighbor stays in the
column or lands pc in {7, INF}) and at (INF, 7). LEX, by
contrast, orders the plateau by the shortfall regardless of its
width: the derived escape routes are corner -> tree-only column
(the tree-only finite part, a product of partition cells, is far
below the corner's empty product) -> descend patience -> exit at
pc = 7 (the wall row's later steps add finite factors) -> the
finite funnel. Predicted plateau order at the base space:
tree-only << corner < chain-only (the chain-only readers commit
only root-vertex straddles of lengths 3/2, 5/6, 3/2 on the three
identity rows near 1 — a per-step product of 15/8 > 1, WORSE
than committing nothing).

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls] The four controls of explore_ratchet_learner.py
   reproduce (wall freeze, chain slope 2 ln(1+sqrt2), deficit
   band, 4/3 rank slope), and so does the disease: plain
   single-move descent on the base space stalls exactly at the
   greedy quartet plus the four corner policies.
C2 [base cures] LEX and WIDE both converge from every base start
   (both descent variants). The corner's improving directions
   under LEX are exactly the tree-patience step; the
   chain-patience step strictly worsens; preference flips tie.
   Plateau order: every tree-only < every corner < every
   chain-only in the lexicographic comparison.
C3 [bottom lemma, engine leg] At every counted step of every row,
   the greedy committed cell is contained in every independently
   enumerated containing cell (path cells + the deepest chain at
   each path vertex), and the four preference orders commit
   identical cell sequences. No sampling.
C4 [grown landscape] The global minimum of the grown space is
   still the greedy quartet (pointwise, corollary ii). The
   partition valley is strict along patience 0..7 then INF at
   every non-wall row. The infinite region contains the full L
   ({pc >= 7} union {pt = INF}); (7, 6) is infinite at tree-first
   preference with the identity-phi row among its killers, while
   (7, 5) and (6, 6) are finite. No finite policy stalls above
   the minimum under any rule (the funnel survives growth on the
   reading region).
C5 [the separation] In the grown space WIDE's above-minimum
   stalls are exactly the derived forty policies — the tree-only
   column {(pt, INF)} for all nine pt including INF, plus
   (INF, 7), times four preferences — and LEX converges from all
   324 starts, both variants.

KILL CRITERIA, fixed at the freeze
----------------------------------
K1 Any control in C1 fails: the rig is dead, no verdicts.
K2 THE PRINCIPAL KILL: BOTH cures stall off-optimum somewhere in a
   scanned space — then bootstrap needs more than a tiebreak or
   wider moves, and a different loss coordinate (the scale clock)
   enters the next slate.
K3 The bottom/confluence check fails anywhere: the lemma's proof
   has a hole; find it before reading any other verdict.
K4 A FINITE off-optimum stall appears in any space: an
   unpredicted trap in the reading region; measure its gap at 2N
   (bounded gap = shallow basin, growing gap = real trap) before
   reading any cure verdict.

ENGINE
------
Exact integer arithmetic in every decision, as in
explore_ratchet_learner.py (the engine core — points, cylinders,
cells, the reader loop, the exact loss — is copied verbatim; this
experiment adds only comparators, move sets, descent over
precomputed exact ranks, and the containing-cell enumerator).
Descents precompute one exact total preorder per comparator
(sorting the space with big-integer cross-multiplication), then
walk ranks. The containing-cell enumerator walks the
Stern-Brocot path toward the reference and takes the deepest
straddle at each path vertex via the closed-form chain index.
Sequential, well under the resource caps; positive controls gate
all verdicts; exit nonzero on any failure.

FINDINGS (entered after the run; ALL ENGINES PASS, exit 0, ~9 s)
----------------------------------------------------------------
F1 C1 CONFIRMED, controls exact: chain ln-k slope 1.7627 =
   2 ln(1+sqrt2) to four decimals; partition wall freeze at
   rank 1; (2x, phi) partition rank slope 1.3333 = 4/3; base
   plain descent stalls exactly at the greedy quartet plus the
   four corners (8 stalls) — the disease is present.
F2 C2 CONFIRMED: both cures converge from every base start,
   200/200 runs each. The corner's LEX-improving directions are
   exactly the tree-patience step; the chain-patience step
   strictly WORSENS (committing root straddles of lengths 3/2,
   5/6, 3/2 loses to committing nothing); the plateau order
   tree-only < corner < chain-only holds at all 36 policies.
   The corner's LEX escape walks the tree-only column down, then
   the chain-patience axis: (INF,INF) -> (3,INF) -> ... ->
   (0,INF) -> (0,3) -> ... -> (0,0).
F3 C3 CONFIRMED — the bottom lemma's engine leg: the four
   preference orders commit identical cell sequences on every
   row, and the greedy cell is contained in every independently
   enumerated containing cell at every counted step of every row:
   169082 containments, 0 violations, 1420 route choices faced
   across the quartet.
F4 C4 PART-REFUTED, the honest half of the mint. The global
   minimum of the grown space is the greedy quartet (as the
   pointwise-optimality corollary demands), the funnel survives
   growth (no finite policy stalls above the minimum anywhere),
   and (7,6)/(7,5)/(6,6) behave as derived — but THE WALL-ROW
   LAG LAW IS REFUTED: its threshold was computed against a
   phantom one-digit J_1 = (1, 4), when J_1 carries two digits,
   (16/9, 9/4), which the wall chain accepts (kmax = 3). Chain
   patience 7 at greedy tree patience is FINITE; the wall row
   kills only chain REFUSAL (per-row rerun). The pc = 7 column
   dies only at pt in {6, 7, INF} (12 policies), and the killers
   are the phi-family rows, per-row reruns: (6,7) dies by
   doubling-phi ALONE (its tree refs J_1 = (3, 4) and
   J_2 = (3, 10/3) share the left endpoint 3 and stick at
   (2, inf); its chain ref J_1 shares the endpoint 4 with
   S_1(3) = (5/2, 4)); (7,6) at tree-first dies by identity-phi
   AND squared-phi. The valley strictness needed its finite-loss
   hypothesis: the refusal endpoint is infinite on every row, and
   five rows ALSO saturate at high finite patience (infinite
   entries per row, refusal included: id/phi 2, id/sqrt2 1,
   id/sqrt3 2, id/theta8 1, sq/phi 2, dbl/phi 3, dbl/sqrt2 2),
   where infinite losses tie; below saturation the valley is
   strict everywhere, as proved.
F5 C5 CORE CONFIRMED, CENSUS REFUTED — THE HEADLINE. The cures
   SEPARATE in the grown space: LEX converges from ALL 324
   starts, both variants (648/648); WIDE stalls above the
   minimum at EXACTLY the corner's all-infinite neighborhood —
   the corner and (7, INF) at every preference plus (INF, 7) at
   tree-first preference only, 10 policies, not the predicted
   forty. The tree-only column ESCAPES sideways (the frozen
   forty rested on the refuted lag law: the pc = 7 column is
   finite at pt <= 5, so (pt, INF) -> (pt, 7) is a strict plain
   improvement for pt <= 5), and the (INF, 7) stall is
   sigma-holed: the single preference-dependent frontier cell
   (7,6) — infinite at tree-first, finite at chain-first — is
   reachable by diagonal from (INF, 7), so chain-first policies
   escape through it. Plain single-move stalls above minimum: 20
   (the same neighborhood, one cell wider without diagonals).

THE VERDICT. The signal cure SCALES; the move cure is
RADIUS-BOUNDED. WIDE stalls precisely where its whole
neighborhood is infinite — the blind region near the corner
grows with the patience axis while any move set's radius stays
fixed, so widening moves cures only the plateau widths it was
sized against. LEX needs no radius: the committed-scale
shortfall (the finite part of the infinite loss) orders the
plateau at ANY width, and the one experiment-wide rule
"lexicographic deficit descent: finite deficit first, shortfall
among the infinite" converges from every start in both spaces,
monotone, decidable, window-native. Alongside: THE BOTTOM LEMMA
upgrades the measured confluence of explore_ratchet_learner.py
to a proof — the containing
sub-poset of the mediant-straddle cover has an inclusion minimum
and greedy multi-commit reaches it in any preference order (so
greedy patience is pointwise optimal in ANY policy space of this
family) — and its single-reference hypothesis is TIGHT: the
frontier cell (7,6) is a policy-level witness that mixed
references break preference-independence.

Run record. The first run exited 1 at four checks — two frozen
hand-derivations refuted (the wall-row lag law, born of the
indexing slip above; the valley strictness clause, missing its
finite-loss hypothesis) and their two downstream census errors
(the forty-policy WIDE stall set; the full-column pc = 7 kill).
The refuting evidence is the run's own frontier map and per-row
attribution reruns (a neighbor's fate is an experiment, not a
narrative). Post-run edits: those four checks now encode the
found landscape as recorded here; nothing else changed; no
prediction band was touched. Tiers: the landscape and separation
statements are verified exhaustively at the stated scope (100 +
324 policies, 8 rows, N = 120); THE BOTTOM LEMMA and the
partition valley (with the corrected strictness hypothesis) are
proved for this cover and move set, with the lemma's engine leg
at 169082 containments; the tightness witness and the plateau
order are observations at scope.

Settled downstream: explore_throttled_reader.py adds the
resource-bounded stage (a rank budget per input step). Under
scarcity the greedy quartet splits by route preference, the
unthrottled optimum's canonical representative becomes the sole
trap of the landscape, and the cure split inverts: no loss signal
can order the trap's counted-window-degenerate twin, while the
bounded preference-diagonal move cures every start; the optimum
stays ensemble-free at every budget.
"""

import math
import sys
from functools import cmp_to_key

LN2 = math.log(2)
INF_P = None          # patience sentinel: refuse the class
N0 = 8                # loss counted from this step
N_MAIN = 120
N_LONG = 240
AX_BASE = [0, 1, 2, 3, INF_P]
AX_PROBE = [0, 1, 2, 3, 4, 5, 6, 7, INF_P]

# ----------------------------------------------------------------- #
# engine core (verbatim from explore_ratchet_learner.py)
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
    """Run one policy over one image stream. Returns
    (loss_num, loss_den, inf_flag, trace, n_choices)."""
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
                trace.append((rank(C), C[5] if C[0] == "S" else 0, None,
                              (clo, chi)))
                continue
            num *= lp[0]
            den *= lp[1]
            jn = J[1][0] * J[0][1] - J[0][0] * J[1][1]
            jd = J[0][1] * J[1][1]
            trace.append((rank(C), C[5] if C[0] == "S" else 0,
                          ln_frac(lp[0], lp[1]) - ln_frac(jn, jd),
                          (clo, chi)))
        else:
            trace.append((rank(C), C[5] if C[0] == "S" else 0, None,
                          (clo, chi)))
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
NONWALL = [r for r in ROWS if r != WALL]

def build_images(horizon):
    cyl = {s: cylinders(cf_digits(*STREAMS[s], count=horizon))
           for s in STREAMS}
    return {(m, s): images(cyl[s], m) for (m, s) in ROWS}

# ----------------------------------------------------------------- #
# comparators, move sets, descent over exact ranks
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
    """The tiebreak cure: finite beats infinite; two infinites
    compare their finite parts (the committed-scale shortfall)."""
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

def neighbors_wide(pol, axis):
    """Single moves plus the four patience diagonals."""
    out = neighbors_single(pol, axis)
    st, ss, pt, pc = pol
    it, ic = axis.index(pt), axis.index(pc)
    for dt in (-1, 1):
        for dc in (-1, 1):
            jt, jc = it + dt, ic + dc
            if 0 <= jt < len(axis) and 0 <= jc < len(axis):
                out.append((st, ss, axis[jt], axis[jc]))
    return out

def all_losses(space, imgs, horizon):
    return {pol: agg([run_reader(imgs[row], pol, True, horizon)[:3]
                      for row in ROWS])
            for pol in space}

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

def quartet(axis=None):
    return [(st, ss, 0, 0) for st in (0, 1) for ss in (0, 1)]

def corners():
    return [(st, ss, INF_P, INF_P) for st in (0, 1) for ss in (0, 1)]

def e1_controls(imgs, base_losses, base_ranks):
    print("E1 CONTROLS (gate: no verdicts are read unless these pass)")
    greedy = (0, 0, 0, 0)
    tr = run_reader(imgs[WALL], greedy, False, N_MAIN)[3]
    ranks_ = [t[0] for t in tr]
    check("partition reader freezes at the wall (rank 1 forever)",
          all(r == 1 for r in ranks_[5:]),
          "final rank %d" % ranks_[-1])
    _, _, inf, tr, _ = run_reader(imgs[WALL], greedy, True, N_MAIN)
    ks = [(n, t[1]) for n, t in enumerate(tr) if t[1] > 0]
    lnk = [(n, math.log(k)) for n, k in ks if n >= 20]
    sl = slope([y for _, y in lnk], [n for n, _ in lnk])
    check("redundant chain reader never freezes",
          not inf and len(ks) > 50, "chain commits at %d steps" % len(ks))
    check("ln k slope in [1.71, 1.82] (2 ln(1+sqrt2) = 1.7627)",
          1.71 <= sl <= 1.82, "slope %.4f" % sl)
    tr = run_reader(imgs[("dbl", "phi")], greedy, False, N_MAIN)[3]
    rk = [(n, t[0]) for n, t in enumerate(tr) if n >= 20]
    sl = slope([r for _, r in rk], [n for n, _ in rk])
    check("(2x, phi) partition rank slope in [1.26, 1.40] (4/3)",
          1.26 <= sl <= 1.40, "slope %.4f" % sl)
    # the disease: plain single-move descent stalls at quartet+corners
    space = policy_space(AX_BASE)
    st = stalls_of(space, base_ranks,
                   lambda p: neighbors_single(p, AX_BASE))
    expected = set(quartet()) | set(corners())
    check("the disease reproduces: base plain stalls = greedy quartet "
          "+ the four corner policies exactly",
          set(st) == expected, "%d stalls" % len(st))
    check("the corner policies are above-minimum (infinite deficit)",
          all(base_losses[c][2] and base_ranks[c] > 0 for c in corners()))
    return not FAILURES

def e2_base_cures(base_losses, base_ranks):
    print("E2 THE TWO CURES ON THE BASE SPACE (C2)")
    space = policy_space(AX_BASE)
    lex_ranks = rank_map(space, base_losses, cmp_lex)
    # LEX descent from every start, both variants
    n_ok = 0
    fails = []
    for start in space:
        for best in (False, True):
            end, _ = descend(start, lex_ranks,
                             lambda p: neighbors_single(p, AX_BASE), best)
            if lex_ranks[end] == 0:
                n_ok += 1
            else:
                fails.append((start, best, end))
    check("LEX converges from every base start (both variants)",
          not fails, "%d/%d runs reach the optimum" % (n_ok, 2 * len(space)))
    # WIDE descent from every start, both variants
    n_ok = 0
    fails = []
    for start in space:
        for best in (False, True):
            end, _ = descend(start, base_ranks,
                             lambda p: neighbors_wide(p, AX_BASE), best)
            if base_ranks[end] == 0:
                n_ok += 1
            else:
                fails.append((start, best, end))
    check("WIDE converges from every base start (both variants)",
          not fails, "%d/%d runs reach the optimum" % (n_ok, 2 * len(space)))
    # the corner's improving directions under LEX
    corner = (0, 0, INF_P, INF_P)
    imp = [q for q in neighbors_single(corner, AX_BASE)
           if cmp_lex(base_losses[q], base_losses[corner]) < 0]
    check("the corner's LEX-improving directions are exactly the "
          "tree-patience step", imp == [(0, 0, 3, INF_P)],
          "improving: %s" % [fmt_pol(q) for q in imp])
    check("the chain-patience step strictly WORSENS from the corner "
          "(committing root straddles loses to committing nothing)",
          cmp_lex(base_losses[(0, 0, INF_P, 3)],
                  base_losses[corner]) > 0)
    # plateau order: tree-only << corner < chain-only
    tree_only = [(st, ss, pt, INF_P) for st in (0, 1) for ss in (0, 1)
                 for pt in AX_BASE[:-1]]
    chain_only = [(st, ss, INF_P, pc) for st in (0, 1) for ss in (0, 1)
                  for pc in AX_BASE[:-1]]
    ok = (all(cmp_lex(base_losses[t], base_losses[c]) < 0
              for t in tree_only for c in corners())
          and all(cmp_lex(base_losses[c], base_losses[h]) < 0
                  for c in corners() for h in chain_only))
    check("plateau order: every tree-only < every corner < every "
          "chain-only (lexicographic)", ok)
    _, path = descend(corner, lex_ranks,
                      lambda p: neighbors_single(p, AX_BASE), False)
    print("  corner LEX escape path: %s"
          % " -> ".join(fmt_pol(p) for p in path))

def containing_cells(J):
    """All cover cells containing J: the Stern-Brocot path cells plus
    the deepest straddle at each path vertex (deeper straddles at a
    vertex are contained in shallower ones, so the deepest suffices
    for the bottom check)."""
    out = []
    C = ROOT
    while True:
        out.append(interval(C))
        _, l, r, d = C
        v = mediant(l, r)
        k = chain_kmax(v, l, r, J)
        if k >= 1:
            out.append(interval(("S", v, l, r, d, k)))
        nxt = None
        for ch in (("T", l, v, d + 1), ("T", v, r, d + 1)):
            if contains(ch, J):
                nxt = ch
                break
        if nxt is None:
            return out
        C = nxt

def incl(a, b):
    """Interval a inside interval b (not necessarily strictly)."""
    return not lt(a[0], b[0]) and not lt(b[1], a[1])

def e3_bottom(imgs):
    print("E3 THE BOTTOM LEMMA, ENGINE LEG (C3 / K3)")
    quartet_pols = quartet()
    seqs = [[tuple(t[3] for t in run_reader(imgs[row], p, True,
                                            N_MAIN)[3])
             for row in ROWS] for p in quartet_pols]
    check("the four preference orders commit identical cell "
          "sequences on every row",
          all(s == seqs[0] for s in seqs[1:]))
    n_cells = 0
    bad = 0
    for row in ROWS:
        tr = run_reader(imgs[row], (0, 0, 0, 0), True, N_MAIN)[3]
        for n in range(N0, N_MAIN):
            fp = tr[n][3]
            for X in containing_cells(imgs[row][n]):
                n_cells += 1
                if not incl(fp, X):
                    bad += 1
    check("the greedy cell is contained in EVERY containing cell at "
          "every counted step of every row (bottom property)",
          bad == 0, "%d containments checked, %d violations"
          % (n_cells, bad))
    ch = sum(run_reader(imgs[row], p, True, N_MAIN)[4]
             for p in quartet_pols for row in ROWS)
    check("the identity is non-vacuous (real route choices faced)",
          ch > 300, "%d route choices across the quartet" % ch)

def e4_probe(imgs):
    print("E4 THE GROWN SPACE (C4 + C5: the separation)")
    space = policy_space(AX_PROBE)
    losses = all_losses(space, imgs, N_MAIN)
    ranks_plain = rank_map(space, losses, cmp_plain)
    ranks_lex = rank_map(space, losses, cmp_lex)
    gset = [p for p in space if ranks_plain[p] == 0]
    check("the global minimum of the grown space is the greedy "
          "quartet (pointwise optimality corollary)",
          set(gset) == set(quartet()), "%d policies at rank 0" % len(gset))
    # the partition valley along the full axis (the proved law;
    # strictness scoped post-run: infinite losses tie, so the top
    # of the column SATURATES where high patience already commits
    # spine cells)
    ok = True
    sat = []
    for row in NONWALL:
        ls = [run_reader(imgs[row], (0, 0, pt, INF_P), False,
                         N_MAIN)[:3] for pt in AX_PROBE]
        sat.append("%s/%s:%d" % (row[0], row[1],
                                 sum(1 for l in ls if l[2])))
        for i in range(len(ls) - 1):
            c = cmp_plain(ls[i], ls[i + 1])
            if c > 0 or (c == 0 and not ls[i][2]):
                ok = False
                print("    valley broken at row %s/%s" % row)
                break
    check("partition valley: loss monotone along the patience axis "
          "at every non-wall row, strict among finite-loss "
          "patiences", ok)
    print("  saturated (infinite) patience entries per row: %s"
          % "  ".join(sat))
    # the frontier map with preference-disagreement flags
    print("  frozen-start frontier (pt rows, pc cols; F finite, "
          "I infinite, ! preference-dependent):")
    hdr = "      " + " ".join("%3s" % ("INF" if pc is None else pc)
                              for pc in AX_PROBE)
    print(hdr)
    n_disagree = 0
    for pt in AX_PROBE:
        cells = []
        for pc in AX_PROBE:
            flags = set(losses[(st, ss, pt, pc)][2]
                        for st in (0, 1) for ss in (0, 1))
            if len(flags) == 2:
                cells.append("!")
                n_disagree += 1
            else:
                cells.append("I" if flags.pop() else "F")
        print("  %3s   %s" % ("INF" if pt is None else pt,
                              "  ".join("%2s" % c for c in cells)))
    print("  preference-dependent frontier cells: %d" % n_disagree)
    # the frontier law (the frozen lag law was REFUTED: J_1 carries
    # two digits and fits the wall chain — see the run record)
    check("chain REFUSAL is infinite everywhere: every pc = INF "
          "policy is infinite-deficit",
          all(losses[p][2] for p in space if p[3] is None))
    kill_ref = [row for row in ROWS
                if agg([run_reader(imgs[row], (0, 0, 0, INF_P), True,
                                   N_MAIN)[:3]])[2]]
    check("refusal attribution: the wall row ALONE kills chain "
          "refusal (full per-row rerun)", kill_ref == [WALL],
          "killed by: %s" % ["%s/%s" % r for r in kill_ref])
    check("the refuted-lag-law witness: chain patience 7 at greedy "
          "tree patience is FINITE (J_1 fits the wall chain)",
          not losses[(0, 0, 0, 7)][2])
    pc7_inf = set(p for p in space if p[3] == 7 and losses[p][2])
    exp7 = set((st, ss, pt, 7) for st in (0, 1) for ss in (0, 1)
               for pt in (6, 7, INF_P))
    check("the pc = 7 column dies only at pt in {6, 7, INF} -- the "
          "corner-adjacent patch, not a full column",
          pc7_inf == exp7, "%d infinite" % len(pc7_inf))
    kill67 = [row for row in ROWS
              if agg([run_reader(imgs[row], (0, 0, 6, 7), True,
                                 N_MAIN)[:3]])[2]]
    check("(6,7) attribution includes the doubling-phi row (tree "
          "refs J_1, J_2 stuck at (2, inf); chain ref J_1 = (3, 4) "
          "shares the endpoint 4 with S_1(3)) (per-row rerun)",
          ("dbl", "phi") in kill67,
          "killed by: %s" % ["%s/%s" % r for r in kill67])
    # the strays and the tightness witness
    check("(7,6) is infinite at tree-first preference",
          losses[(0, 0, 7, 6)][2])
    kill_rows = [row for row in ROWS
                 if agg([run_reader(imgs[row], (0, 0, 7, 6), True,
                                    N_MAIN)[:3]])[2]]
    check("(7,6) tree-first attribution includes the identity-phi row "
          "(per-row rerun)", ("id", "phi") in kill_rows,
          "killed by: %s" % ["%s/%s" % r for r in kill_rows])
    check("(7,5) and (6,6) are finite (the fringe is one cell wide "
          "here)", not losses[(0, 0, 7, 5)][2]
          and not losses[(0, 0, 6, 6)][2])
    print("  tightness witness: (7,6) chain-first infinite = %s "
          "(tree-first True by the check above; a difference is the "
          "mixed-reference preference-dependence made policy-level)"
          % losses[(1, 0, 7, 6)][2])
    # K4 guard: no finite policy stalls above minimum under any rule
    plain_st = stalls_of(space, ranks_plain,
                         lambda p: neighbors_single(p, AX_PROBE))
    fin_bad = [p for p in plain_st
               if not losses[p][2] and ranks_plain[p] > 0]
    if fin_bad:
        imgs_long = build_images(N_LONG)
        gref = quartet()[0]
        llong = {p: all_losses([p], imgs_long, N_LONG)[p]
                 for p in fin_bad + [gref]}
        for p in fin_bad:
            g1 = (ln_frac(losses[p][0], losses[p][1])
                  - ln_frac(losses[gref][0], losses[gref][1]))
            g2 = (ln_frac(llong[p][0], llong[p][1])
                  - ln_frac(llong[gref][0], llong[gref][1]))
            print("    FINITE STALL %s gap %.1f -> %.1f nats (x%.2f)"
                  % (fmt_pol(p), g1, g2, g2 / g1 if g1 else float("nan")))
    check("no finite policy stalls above the minimum (the funnel "
          "survives growth on the reading region)", not fin_bad)
    print("  plain single-move stalls above minimum: %d"
          % len([p for p in plain_st if ranks_plain[p] > 0]))
    # C5: the separation
    wide_st = stalls_of(space, ranks_plain,
                        lambda p: neighbors_wide(p, AX_PROBE))
    wide_bad = set(p for p in wide_st if ranks_plain[p] > 0)
    # the found stall set (the frozen forty was refuted: the
    # tree-only column escapes sideways because the pc = 7 column
    # is finite at pt <= 5; what stalls is the corner's
    # all-infinite neighborhood, sigma-holed at (7,6))
    found = set((st, ss, INF_P, INF_P) for st in (0, 1)
                for ss in (0, 1))
    found |= set((st, ss, 7, INF_P) for st in (0, 1) for ss in (0, 1))
    found |= set((0, ss, INF_P, 7) for ss in (0, 1))
    check("WIDE stalls are EXACTLY the corner's all-infinite "
          "neighborhood: the corner and (7,INF) at every "
          "preference, plus (INF,7) at tree-first only (the "
          "(7,6) hole admits chain-first diagonals)",
          wide_bad == found, "%d above-minimum WIDE stalls"
          % len(wide_bad))
    n_ok = 0
    fails = []
    for start in space:
        for best in (False, True):
            end, _ = descend(start, ranks_lex,
                             lambda p: neighbors_single(p, AX_PROBE),
                             best)
            if ranks_lex[end] == 0:
                n_ok += 1
            else:
                fails.append((start, best))
    check("LEX converges from ALL grown-space starts (both variants) "
          "-- the signal cure scales", not fails,
          "%d/%d runs reach the optimum" % (n_ok, 2 * len(space)))
    n_ok = 0
    fails = []
    for start in space:
        if start in found:
            continue
        for best in (False, True):
            end, _ = descend(start, ranks_plain,
                             lambda p: neighbors_wide(p, AX_PROBE),
                             best)
            if ranks_plain[end] == 0:
                n_ok += 1
            else:
                fails.append((start, best, end))
    check("WIDE converges from every start OUTSIDE its stall set",
          not fails, "%d runs reach the optimum" % n_ok)
    corner = (0, 0, INF_P, INF_P)
    _, path = descend(corner, ranks_lex,
                      lambda p: neighbors_single(p, AX_PROBE), False)
    print("  corner LEX escape path (grown space): %s"
          % " -> ".join(fmt_pol(p) for p in path))

def main():
    print("THE BOOTSTRAP CURES -- which corner cure scales")
    print("slate: %d rows, N=%d (loss from n0=%d); base axis %s; "
          "grown axis 0..7+INF"
          % (len(ROWS), N_MAIN, N0, "0..3+INF"))
    imgs = build_images(N_MAIN)
    base_space = policy_space(AX_BASE)
    base_losses = all_losses(base_space, imgs, N_MAIN)
    base_ranks = rank_map(base_space, base_losses, cmp_plain)
    if not e1_controls(imgs, base_losses, base_ranks):
        print("CONTROLS FAILED -- rig dead, no verdicts (K1).")
        sys.exit(1)
    e2_base_cures(base_losses, base_ranks)
    e3_bottom(imgs)
    e4_probe(imgs)
    if FAILURES:
        print("FAILURES: %s" % ", ".join(FAILURES))
        sys.exit(1)
    print("ALL ENGINES PASS")

if __name__ == "__main__":
    main()
