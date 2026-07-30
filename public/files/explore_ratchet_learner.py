"""The ratchet learner: is the commitment-deficit landscape over a
finite policy space of continued-fraction readers free of bad local
minima at quadratic streams?

THE QUESTION
------------
A reader of a continued-fraction stream is a COMMITMENT POLICY on
the window's refinement structure: at each input step the certified
knowledge is the image interval J_n = f(I_n) (I_n the input
cylinder; the J_n nest), and the reader commits cover cells
containing J_n — commitments are ratchets, never undone, and any
cell containing J_n contains every later J_m. The commitment
deficit D(n) = scale(J_n) - scale(committed cell), scale =
ln(1/length), is an exact, window-native loss (explore_cf_flow.py:
the commitment bound prices its optimum). Both covers are in hand:
the partition cover (Stern-Brocot cells) and the mediant-straddle
redundant cover (explore_cf_redundant.py). This experiment asks
whether a MONOTONE local update rule over a finite policy space —
move to a neighboring policy only when its exactly-compared loss is
strictly lower, a decidable ratchet with no gradients and no floats
in any decision — converges to the minimal-deficit policy at
quadratic streams, i.e. whether the deficit landscape is free of
bad local minima.

VOCABULARY NOTE. "Landscape", "local minimum", and "descent" are
used here as finite-graph notions only: a neighbor relation on a
finite policy set, strict-improvement moves, and a stall = a policy
with no strictly better neighbor. Loss comparisons are exact
rational-product comparisons (sums of logarithms of rationals
compare by cross-multiplying big integers). Nothing is
differentiated.

THE POLICY SPACE (the design, fixed first)
------------------------------------------
The cover's child relations give the choice structure
(explore_cf_redundant.py): from a TREE cell, T = descend to the
tree child, E = enter the straddle chain at the cell's vertex
(greedy chain index); from a STRADDLE S_k(v), L = deepen the chain
(greedy jump), X = side-exit into a run-node tree cell. At most two
move types are simultaneously available (T/E at tree cells, L/X at
straddles), so the WHICH coordinate is two binary preferences. The
WHEN coordinate is a patience per target class: a cell class
(tree / straddle) with patience p commits a candidate C at step n
only when C already contained J_{n-p} (the J's nest, so this says C
has contained the image interval for p+1 consecutive steps);
patience INF refuses the class outright.

  policy = (sigma_T in {T-first, E-first},
            sigma_S in {L-first, X-first},
            p_tree  in {0, 1, 2, 3, INF},
            p_chain in {0, 1, 2, 3, INF})

Redundant space: 2 x 2 x 5 x 5 = 100 policies. Partition space
(chains disabled): p_tree alone, 5 policies. Neighbors: flip one
preference bit, or step one patience by one place along
(0, 1, 2, 3, INF). Loss of a policy = the sum over a fixed stream
slate of sum_{n=n0}^{N} D(n); since the J_n are policy-independent,
policies compare exactly by the product of committed-cell lengths
(big-integer cross-multiplication; a policy holding an
infinite-length cell at a counted step has infinite loss).

HAND-DERIVED BEFORE THE ENGINE
------------------------------
H1 (partition valley). In the partition cover the cells containing
   an interval form one nested chain, so the greedy commitment
   (p = 0) is pointwise optimal: with patience p the committed cell
   is the greedy cell of J_{n-p}, whose scale is at most the greedy
   scale of J_n. Loss is pointwise monotone in patience, and the
   cumulative excess grows like p x (scale rate) x N. The partition
   landscape should be a monotone valley with its minimum at p = 0.
H2 (the route plateau, O(1)). The redundant cover's grading (every
   child relation steps rank by +1; stepwise routes between two
   cells have equal length; a jump commit only shortens) and the
   interleaving law (the side piece at chain index k IS the run-node
   cell one grade deeper) make the two routes past a vertex
   scale-equivalent up to O(1): chain cells and run cells descend
   the same harmonic ladder, offset by one grade. So the WHICH
   coordinate moves cumulative loss by O(1) while one patience step
   moves it linearly in N. Shallow O(1)-deep basins in the WHICH
   coordinate are possible (at the golden stream, entering the chain
   versus taking the tree child commits same-rank cells of different
   lengths); a stall O(1) above the global minimum is convergence to
   within a constant of the priced optimum, not a trap at scale.

PREDICTIONS, fixed before the engine ran
----------------------------------------
P1 [control] The greedy policy (p = 0) reproduces the known prints:
   at (x -> x^2, sqrt2) the partition reader freezes at the wall
   node's depth (rank 1) forever, while the redundant reader never
   freezes and its chain index grows at ln-slope = the input scale
   rate (2 ln(1+sqrt2) = 1.7627, band [1.71, 1.82]) with deficit
   bounded (band [0, 1.5], exact nonnegativity everywhere); at
   (2x, phi) the partition reader's rank slope is 4/3 (band
   [1.26, 1.40]) — the stalled pair read in tree units.
P2 [from H1] Partition landscape: loss strictly increases along
   p_tree = 0, 1, 2, 3, INF at EVERY slate stream (exact
   comparisons); descent from every start reaches p = 0; no other
   stall.
P3a [the main verdict] Redundant landscape: strict descent
   (first-improvement and best-improvement, all 100 starts) stalls
   only at losses whose gap from the global minimum is BOUNDED in
   the horizon: measured at N and 2N, no stall gap grows
   proportionally.
P3b [stronger, expected] All stalls sit exactly in the global
   minimum set, and the global minimum has p = (0, 0).
P4 [from H2] The plateau print: at p = (0, 0) the loss spread over
   the four preference combinations, measured at N and 2N, does not
   double — route choice carries O(1) cost, not linear.

KILL CRITERIA, fixed at the freeze
----------------------------------
K1 Any control in P1 fails: the rig is dead, no verdicts are read.
K2 THE HEADLINE KILL (scale-aware): a stall whose loss gap from the
   global minimum GROWS with N (about doubles when N doubles) — a
   linear trap reachable by no monotone rule; the verdict would be
   that the deficit is the wrong loss for learning in reader space.
   P3b failing while P3a holds is a reported finding (shallow route
   basins), not this kill.
K3 The spread in P4 grows linearly with N: route choice carries
   linear cost and the grading's learning reading is wrong — its
   own autopsy before any successor experiment.

ENGINE
------
Exact integer arithmetic in every decision: points are integer
pairs (p, q) with q >= 0 and (1, 0) = +infinity; streams are
periodic continued fractions generated as exact convergent
cylinders; maps (identity, x^2, 2x) act on rational endpoints;
containment and all loss comparisons are big-integer
cross-multiplications. Chain indices are solved in closed form from
the straddle endpoint law (one linear inequality per side). Floats
appear only in printed reports (slopes, deficit bands), computed
from bit-length logarithms so no underflow occurs. Stream slate
(all corpus witnesses): identity on phi, sqrt2, sqrt3, [0; 8, 8,
...]; (x^2, sqrt2) the wall; (x^2, phi); (2x, phi); (2x, sqrt2).
Horizon N = 120 input digits, loss counted from n0 = 8; the
horizon-growth checks rerun the needed policies at 2N = 240.
Sequential, seconds, trivial memory; positive controls run and
gate before any verdict is read; exit nonzero on any failure.

FINDINGS (entered after the run; ALL ENGINES PASS, exit 0, ~10 s)
----------------------------------------------------------------
P1 CONFIRMED, controls exact: chain ln-k slope 1.7627 =
   2 ln(1+sqrt2) to four decimals; partition wall freeze at rank 1;
   (2x, phi) partition rank slope 1.3333 = 4/3. One unpredicted
   sharpening: at the cured wall the greedy chain reader's deficit
   is asymptotically ZERO (D range [0.000, 0.000] from n0 = 8) —
   the straddle chain is scale-dense (consecutive lengths ratio
   (k+1)/k -> 1), so at a cured wall the reader commits not just
   boundedly but exactly, below the generic commitment-bound
   constant.
P2 CONFIRMED: loss strictly increases along patience at every one
   of the seven non-wall rows — the partition landscape is the
   monotone valley of H1, minimum at greedy.
P3b REFUTED — THE HEADLINE. The global minimum set is patience
   (0, 0) times ALL FOUR route preferences, tied EXACTLY. The
   above-minimum stalls are EXACTLY the four refusal-corner
   policies (INF, INF): their loss is infinite, and both
   single-refusal neighbor families are also infinite — tree-only
   readers freeze exactly at the wall row's infinite-length cell
   (1, inf); chain-only readers freeze at the ROOT on every row
   whose image stream never approaches the root vertex (five of
   eight rows, the wall row included — chains cannot descend the
   tree, so the first tree move is a prerequisite everywhere else)
   — so every corner neighbor ties at INF and the corner sits on a
   FLAT INFINITE PLATEAU where deficit comparisons carry no
   signal. The wall row alone already suffices: on that single row
   the corner and both neighbor families are infinite together.
   Of 100 policies, 36 are infinite-deficit; 32 of those have a
   strictly improving neighbor; only the corner stalls. Descent
   (both variants, all starts): 192 of 200 runs reach the exact
   global minimum; the eight others are the corner starting in
   itself.
CONFLUENCE (unpredicted, stronger than H2): the four preference
   combinations faced 355 real route choices across the slate,
   tie exactly in loss, AND commit the IDENTICAL cell sequence at
   every step of every row (verified cell-by-cell) — the fixed
   point of greedy multi-commit is route-independent. H2 predicted
   an O(1)-tilted plateau; the plateau is exactly flat at greedy
   patience.
P3a / K2, the horizon reading: the corner stays infinite-deficit at
   2N, and its committed-scale shortfall grows QUADRATICALLY
   (95526 -> 388327 nats, ratio 4.07 ~ (2N/N)^2) — the
   frozen-reader signature (a stalled reader's per-step deficit
   grows ~ n x rate, so the sum is ~ N^2/2 x rate). K2 fires AT THE
   LETTER on the corner alone.

THE VERDICT. The deficit landscape is a FUNNEL WITH ONE BLIND
CORNER. On the reading region — any policy that ever commits — the
deficit is a perfect loss: monotone strict descent converges from
every start to the exact optimum, and the optimum is route-free by
confluence. The deficit is blind exactly on total refusal UNDER
THE SINGLE-COORDINATE MOVE SET: every one-coordinate neighbor of
the corner ties at infinite deficit, so strict descent over these
moves cannot bootstrap a reader from nothing. The blindness
belongs to the move set, not to the signal in the abstract — the
diagonal move (both patiences off refusal at once) lands on a
finite-loss policy and compares strictly. Two cures are visible in
this run's own prints: widen the moves (the diagonal), or add a
second signal — the finite parts of the infinite losses (the
committed-scale shortfall) already order the plateau, and "among
infinite-deficit policies, descend the committed-scale shortfall"
is window-native and monotone. Which cure scales is the next
question, not a different loss wholesale.

Run record. The first run exited 1 at the original P3b assert
("every stall sits in the global minimum set") — the refusal-corner
discovery. The pre-engine hand-analysis had asserted single-refusal
policies escapable (a strictly improving finite-patience neighbor)
without running the neighbor's own per-row fate; the rig refuted
it. An earlier draft of this record then attributed the two kills
to two DIFFERENT rows (a conjunction story); a per-row rerun of
both families corrected that too — the kill is broad (chain-only
dies on five rows, tree-only at the wall row, one row suffices for
both), not a conspiracy of rows. Post-run edits: the landscape
asserts now encode the found state (P3b above stands refuted as
recorded); a route-choice counter and a cell-sequence identity
check were added so the confluence claim is non-vacuous and
cell-level; the INF stalls' printed "gap" was relabeled as the
committed-scale shortfall (the finite part of an infinite loss). No
prediction band was changed. Tier: the landscape statements are
verified exhaustively at the stated scope (100 policies, 8 rows,
N = 120 and 240); the confluence (cell-by-cell at scope) and the
zero-deficit-at-the-wall sharpening are observations.

Settled downstream: explore_bootstrap_cures.py answers the cure
question — the lexicographic tiebreak scales while the widened
move set is radius-bounded — and upgrades the confluence
observation to a proof (the bottom lemma: the cover's containing
sub-poset has an inclusion minimum, reached by greedy
multi-commit in any preference order).
"""

import math
import sys
from functools import cmp_to_key

LN2 = math.log(2)
INF_P = None          # patience sentinel: refuse the class
N0 = 8                # loss counted from this step
N_MAIN = 120
N_LONG = 240
PATIENCE_AXIS = [0, 1, 2, 3, INF_P]

# ----------------------------------------------------------------- #
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

# ----------------------------------------------------------------- #
# streams: periodic continued fractions -> exact input cylinders
# ----------------------------------------------------------------- #

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
    p2, q2, p1, q1 = 0, 1, 1, 0     # p_{-2}/q_{-2}, p_{-1}/q_{-1}
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

# ----------------------------------------------------------------- #
# cover cells
#   tree cell  ('T', l, r, d): the cell of node v = mediant(l, r),
#              interval (l, r), rank d = depth(v)
#   straddle   ('S', v, l, r, d, k): S_k(v), v's parents (l, r),
#              d = depth(v), interval (m_kL, m_kR), rank d + k
# ----------------------------------------------------------------- #

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

# ----------------------------------------------------------------- #
# the reader
# ----------------------------------------------------------------- #

def run_reader(J_list, policy, redundant, horizon):
    """Run one policy over one image stream. Returns
    (loss_num, loss_den, inf_flag, trace, n_choices) with trace a
    list of (rank, chain_index_or_0, D_float or None, interval) per
    step and n_choices the number of commit decisions where BOTH
    move types were simultaneously available (real route choices
    faced)."""
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
        # soundness: the committed cell must contain the image
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

# ----------------------------------------------------------------- #
# exact loss comparison and aggregation
# ----------------------------------------------------------------- #

def agg(losses):
    """Aggregate (num, den, inf) triples by multiplying."""
    num, den, inf = 1, 1, False
    for n, d, i in losses:
        if i:
            inf = True
        else:
            num *= n
            den *= d
    return num, den, inf

def cmp_loss(a, b):
    """-1 if loss a < loss b (smaller cells = smaller loss)."""
    if a[2] and b[2]:
        return 0
    if a[2]:
        return 1
    if b[2]:
        return -1
    left = a[0] * b[1]
    right = b[0] * a[1]
    return -1 if left < right else (1 if left > right else 0)

# ----------------------------------------------------------------- #
# the slates
# ----------------------------------------------------------------- #

ROWS = [
    ("id",  "phi"), ("id", "sqrt2"), ("id", "sqrt3"), ("id", "theta8"),
    ("sq",  "sqrt2"),                     # the wall row
    ("sq",  "phi"), ("dbl", "phi"), ("dbl", "sqrt2"),
]
NONWALL = [r for r in ROWS if r != ("sq", "sqrt2")]

def build_images(horizon):
    cyl = {s: cylinders(cf_digits(*STREAMS[s], count=horizon))
           for s in STREAMS}
    return {(m, s): images(cyl[s], m) for (m, s) in ROWS}

def policy_space():
    out = []
    for s_t in (0, 1):
        for s_s in (0, 1):
            for pt in PATIENCE_AXIS:
                for pc in PATIENCE_AXIS:
                    out.append((s_t, s_s, pt, pc))
    return out

def neighbors(pol):
    s_t, s_s, pt, pc = pol
    out = [(1 - s_t, s_s, pt, pc), (s_t, 1 - s_s, pt, pc)]
    it, ic = PATIENCE_AXIS.index(pt), PATIENCE_AXIS.index(pc)
    if it > 0:
        out.append((s_t, s_s, PATIENCE_AXIS[it - 1], pc))
    if it < 4:
        out.append((s_t, s_s, PATIENCE_AXIS[it + 1], pc))
    if ic > 0:
        out.append((s_t, s_s, pt, PATIENCE_AXIS[ic - 1]))
    if ic < 4:
        out.append((s_t, s_s, pt, PATIENCE_AXIS[ic + 1]))
    return out

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

def e1_controls(imgs):
    print("E1 CONTROLS (gate: no verdicts are read unless these pass)")
    greedy = (0, 0, 0, 0)
    # partition freeze at the wall
    tr = run_reader(imgs[("sq", "sqrt2")], greedy, False, N_MAIN)[3]
    ranks = [t[0] for t in tr]
    check("partition reader freezes at the wall (rank 1 forever)",
          all(r == 1 for r in ranks[5:]),
          "final rank %d" % ranks[-1])
    # redundant chain reader never freezes; slope and deficit bands
    _, _, inf, tr, _ = run_reader(imgs[("sq", "sqrt2")], greedy, True, N_MAIN)
    ks = [(n, t[1]) for n, t in enumerate(tr) if t[1] > 0]
    lnk = [(n, math.log(k)) for n, k in ks if n >= 20]
    sl = slope([y for _, y in lnk], [n for n, _ in lnk])
    check("redundant chain reader never freezes (no infinite cell)",
          not inf and len(ks) > 50, "chain commits at %d steps" % len(ks))
    check("ln k slope in [1.71, 1.82] (2 ln(1+sqrt2) = 1.7627)",
          1.71 <= sl <= 1.82, "slope %.4f" % sl)
    ds = [t[2] for t in tr if t[2] is not None]
    check("wall-row deficit in [0, 1.5], exact nonnegativity",
          all(-1e-9 <= d <= 1.5 for d in ds),
          "D range [%.3f, %.3f]" % (min(ds), max(ds)))
    # the stalled pair in tree units
    tr = run_reader(imgs[("dbl", "phi")], greedy, False, N_MAIN)[3]
    rk = [(n, t[0]) for n, t in enumerate(tr) if n >= 20]
    sl = slope([r for _, r in rk], [n for n, _ in rk])
    check("(2x, phi) partition rank slope in [1.26, 1.40] (4/3)",
          1.26 <= sl <= 1.40, "slope %.4f" % sl)
    return not FAILURES

def e2_partition(imgs):
    print("E2 PARTITION LANDSCAPE (P2: a monotone valley, minimum at 0)")
    per_stream = {}
    for row in NONWALL:
        per_stream[row] = []
        for pt in PATIENCE_AXIS:
            n, d, i = run_reader(imgs[row], (0, 0, pt, INF_P),
                                 False, N_MAIN)[:3]
            per_stream[row].append((n, d, i))
    ok = True
    for row in NONWALL:
        ls = per_stream[row]
        mono = all(cmp_loss(ls[i], ls[i + 1]) < 0 for i in range(4))
        if not mono:
            ok = False
            print("    non-monotone at row %s/%s" % row)
    check("loss strictly increasing in patience at every stream", ok)
    return per_stream

def e3_redundant(imgs):
    print("E3 REDUNDANT LANDSCAPE (P3: stalls, descent, the verdict)")
    space = policy_space()
    losses = {}
    choices = {}
    for pol in space:
        runs = [run_reader(imgs[row], pol, True, N_MAIN) for row in ROWS]
        losses[pol] = agg([r[:3] for r in runs])
        choices[pol] = sum(r[4] for r in runs)
    order = sorted(space, key=cmp_to_key(
        lambda a, b: cmp_loss(losses[a], losses[b])))
    gmin = losses[order[0]]
    gset = [p for p in space if cmp_loss(losses[p], gmin) == 0]
    print("  global minimum set (%d policies):" % len(gset))
    for p in gset:
        print("    sigma=(%d,%d) patience=(%s,%s)  route choices faced: %d"
              % (p[0], p[1], str(p[2]), str(p[3]), choices[p]))
    check("global minimum has patience (0, 0)",
          all(p[2] == 0 and p[3] == 0 for p in gset))
    check("greedy multi-commit is confluent (all four route preferences "
          "tie EXACTLY while facing real choices)",
          len([p for p in gset if p[2] == 0 and p[3] == 0]) == 4
          and all(choices[p] > 0 for p in gset),
          "choices faced: %s" % sorted(set(choices[p] for p in gset)))
    quartet = [(st, ss, 0, 0) for st in (0, 1) for ss in (0, 1)]
    seqs = [[tuple(t[3] for t in run_reader(imgs[row], p, True,
                                            N_MAIN)[3])
             for row in ROWS] for p in quartet]
    check("confluence is cell-level: the four preferences commit the "
          "IDENTICAL cell sequence at every step of every row",
          all(s == seqs[0] for s in seqs[1:]))
    # stalls of strict descent
    stalls = [p for p in space
              if all(cmp_loss(losses[q], losses[p]) >= 0
                     for q in neighbors(p))]
    bad = [p for p in stalls if cmp_loss(losses[p], gmin) > 0]
    print("  stalls: %d total, %d above the global minimum"
          % (len(stalls), len(bad)))
    for p in bad:
        part = ln_frac(losses[p][0], losses[p][1]) - ln_frac(gmin[0],
                                                             gmin[1])
        print("    stall sigma=(%d,%d) patience=(%s,%s)  loss INF, "
              "committed-scale shortfall %.1f nats"
              % (p[0], p[1], str(p[2]), str(p[3]), part))
    # the found landscape (the original prediction P3b — every stall
    # in the global minimum set — is REFUTED by exactly this set):
    check("the only above-minimum stalls are the four refusal-corner "
          "policies, every one at infinite deficit",
          len(bad) == 4
          and all(p[2] is None and p[3] is None for p in bad)
          and all(losses[p][2] for p in bad))
    inf_region = [p for p in space if losses[p][2]]
    esc = [p for p in inf_region
           if p not in bad
           and any(cmp_loss(losses[q], losses[p]) < 0
                   for q in neighbors(p))]
    check("every other infinite-deficit policy has a strictly "
          "improving neighbor (the plateau is escapable except at "
          "its corner)", len(esc) == len(inf_region) - 4,
          "%d infinite-deficit policies, %d escapable"
          % (len(inf_region), len(esc)))
    # descent from every start, both variants
    def descend(start, best_improve):
        p = start
        while True:
            nb = neighbors(p)
            if best_improve:
                nb = sorted(nb, key=cmp_to_key(
                    lambda a, b: cmp_loss(losses[a], losses[b])))
            moved = False
            for q in nb:
                if cmp_loss(losses[q], losses[p]) < 0:
                    p = q
                    moved = True
                    break
            if not moved:
                return p
    converge = 0
    stray = []
    for start in space:
        for variant in (False, True):
            end = descend(start, variant)
            if cmp_loss(losses[end], gmin) == 0:
                converge += 1
            elif end in bad and start in bad:
                pass                      # the corner, started there
            else:
                stray.append((start, variant, end))
    check("descent (both variants) from every committing start "
          "reaches the exact global minimum; only corner starts "
          "stay in the corner", not stray,
          "%d of %d runs converge, the rest are corner starts"
          % (converge, 2 * len(space)))
    lw = losses[order[-1]]
    spread = ("INF" if lw[2] else
              "%.1f" % (ln_frac(lw[0], lw[1]) - ln_frac(gmin[0], gmin[1])))
    print("  landscape span: best-to-worst gap %s nats" % spread)
    return losses, gmin, gset, stalls, bad

def e4_horizon(imgs_long, bad_stalls, gset, losses, gmin):
    print("E4 HORIZON GROWTH (P3a + P4: gaps and spread at 2N)")
    # sigma spread at patience (0,0), N and 2N
    def spread_at(imgs, horizon):
        ls = []
        for s_t in (0, 1):
            for s_s in (0, 1):
                ls.append(agg([run_reader(imgs[row], (s_t, s_s, 0, 0),
                                          True, horizon)[:3]
                               for row in ROWS]))
        vals = [ln_frac(l[0], l[1]) for l in ls]
        return max(vals) - min(vals)
    imgs_main = build_images(N_MAIN)
    sp1 = spread_at(imgs_main, N_MAIN)
    sp2 = spread_at(imgs_long, N_LONG)
    check("P4: sigma spread does not double from N to 2N",
          sp2 < max(2.0 * sp1, sp1 + 1.0) and sp2 < 1.5 * sp1 + 0.5,
          "spread %.4f -> %.4f nats" % (sp1, sp2))
    # the corner at 2N (the K2 reading): its loss is infinite at
    # every horizon, and its committed-scale shortfall grows
    # QUADRATICALLY — the frozen-reader signature (a reader stalled
    # at a fixed cell accumulates deficit ~ n x rate per step, so
    # the sum grows ~ N^2/2 x rate).
    if not bad_stalls:
        print("  no above-minimum stalls at N: K2 has no candidate")
        return
    ref = gset[0]
    long_losses = {}
    for p in bad_stalls + [ref]:
        long_losses[p] = agg([run_reader(imgs_long[row], p,
                                         True, N_LONG)[:3]
                              for row in ROWS])
    gl = long_losses[ref]
    check("the refusal corner stays infinite-deficit at 2N",
          all(long_losses[p][2] for p in bad_stalls))
    p = bad_stalls[0]
    part1 = (ln_frac(losses[p][0], losses[p][1])
             - ln_frac(gmin[0], gmin[1]))
    part2 = (ln_frac(long_losses[p][0], long_losses[p][1])
             - ln_frac(gl[0], gl[1]))
    check("the corner's committed-scale shortfall grows "
          "quadratically (ratio near 4 when N doubles)",
          3.0 <= part2 / part1 <= 5.0,
          "shortfall %.0f -> %.0f nats, ratio %.2f"
          % (part1, part2, part2 / part1))

def main():
    print("THE RATCHET LEARNER — deficit descent over reader policies")
    print("slate: %d rows, horizon N=%d (loss from n0=%d), 2N=%d"
          % (len(ROWS), N_MAIN, N0, N_LONG))
    imgs = build_images(N_MAIN)
    if not e1_controls(imgs):
        print("CONTROLS FAILED — rig dead, no verdicts (K1).")
        sys.exit(1)
    e2_partition(imgs)
    losses, gmin, gset, stalls, bad = e3_redundant(imgs)
    imgs_long = build_images(N_LONG)
    e4_horizon(imgs_long, bad, gset, losses, gmin)
    if FAILURES:
        print("FAILURES: %s" % ", ".join(FAILURES))
        sys.exit(1)
    print("ALL ENGINES PASS")

if __name__ == "__main__":
    main()
