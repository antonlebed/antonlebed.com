"""explore_ceiling_dials.py -- THE COMPARISON EVAL AND THE PRIOR DIAL
(the fifth instance of an evaluation that knows its own optimum, and
the first non-uniform-prior stress test of the ceiling anatomy;
sibling of explore_eval_ceiling.py, explore_ceiling_anatomy.py, and
explore_induction_ceiling.py).

THE QUESTION. The sibling scripts established that "knows its own
ceiling" is designable and mapped an ANATOMY: each eval family in the
corpus ships an exact dial separating floor cells (Bayes ceiling =
the no-evidence floor) from interior cells with closed-form values --
the parity dial for the sign bit, a window clause at general
thresholds, an inverted dial at the orientation relation. Every
instance so far froze ONE knob: the uniform prior. Two legs finish
the anatomy's axes:

(A) THE COMPARISON EVAL. The task [x < y] on a uniform ordered pair
    of DISTINCT elements of Z/N, evidence = both residues mod M (a
    proper divisor, unknown cofactor c = N/M). The archimedean
    comparison of two hidden elements: a fourth task shape (binary
    relation on a pair, fibers products of ladders).

(B) THE PRIOR DIAL. Replace the uniform prior on Z/N by the
    geometric tilt P(x) proportional to theta^x, theta a positive
    rational dial, and re-derive the threshold family [x >= t] from
    scratch. Chosen over other prior families because (i) it is a
    one-parameter dial with the uniform prior at theta = 1, (ii) the
    within-fiber weights form a geometric ladder in q = theta^M, so
    posteriors stay closed-form and the anatomy question stays
    answerable, (iii) everything is exact in Fraction arithmetic,
    and (iv) the exponential tilt is the canonical one-parameter
    deformation of a task distribution. Does the anatomy survive a
    non-uniform prior, and what happens to the parity dial?

An EVAL is a triple (task family with prior, evidence channel,
score); its CEILING is the Bayes-optimal expected score; the FLOOR
is the prior's best score with the evidence severed -- COMPUTED by
direct summation in every run, never assumed; NONTRIVIAL means
strictly between floor and perfect; TIGHT means a computable
achiever with stated cost matches the ceiling.

DESIGN.
  Comparison leg: every squarefree N <= 2310 that is a product of
  >= 2 primes from {2, 3, 5, 7, 11, 13} (49 rings, 362 (N, M)
  cells). Brute per cell: the pair census by an ascending prefix
  sweep (for each y, every earlier x is binned by (x mod M, y mod
  M); no ladder structure used), Bayes = the per-fiber majority sum;
  conditional entropy in nats; the computed floor. The achiever
  (reconstruct both residues, order them, fixed guess on ties) is
  enumerated exactly on every cell with N <= 210.
  Tilt leg: every cell with N <= 210 (116 cells), theta on the grid
  {1/10, 1/3, 1/2, 2/3, 1, 3/2, 2, 3, 10}, EVERY threshold
  t = 1..N-1, exact Fractions: an incremental t-sweep maintains the
  below-weight of each residue fiber (one element enters per step),
  giving brute ceiling, computed floor, conditional entropy, and the
  exact posterior-vs-prior comparison per fiber; each is asserted
  against the derived closed forms below. The plug-in achiever
  (CRT-reconstruct r, compare the fiber's below-mass to 1/2 by the
  closed form) runs on every cell with N <= 105, every t, every
  theta. Spot leg: N in {330, 462, 2310} at four subsets each,
  theta in {1/2, 2}, a structured t-sample including the predicted
  interior window.
  Controls (asserted before any scan is read): the four hand-counted
  cases in the derivations below, the reflection identity, and the
  theta = 1 grid point, which must reproduce the uniform closed
  forms of the sibling scripts on every cell -- the positive control
  against the established law.

HAND DERIVATION A (fixed before the engine; comparison). Evidence
(alpha, beta) = (x mod M, y mod M); the fiber is a product of two
full c-ladders (every residue's ladder has all c points -- zero
residues are not special here, unlike the orientation task's
difference pairs).
  alpha < beta: x < y iff i <= j (ladder indices): c(c+1)/2 of c^2,
    so P(x < y) = (c+1)/(2c). alpha > beta: x < y iff i < j:
    (c-1)/(2c). Either way the fiber's Bayes score is (c+1)/(2c) --
    the universal skew unit of the corpus, reappearing because the
    comparison fiber is again a staircase count on a c-ladder grid.
  alpha = beta: ordered distinct pairs, exactly half below:
    P = 1/2, Bayes score 1/2.
  Weights: M(M-1)c^2 unequal-residue pairs, Mc(c-1) tie pairs, of
  N(N-1). Summing:
      CEILING = 1/2 + (M-1)/(2(N-1)),
  c drops out entirely. The floor is exactly 1/2 (as many pairs
  ascend as descend). So EVERY proper subset lifts -- including
  M = 2 -- and there are NO floor cells: a third dial shape
  (the constant dial), against the sign eval (only channel 2 alive
  alone) and orientation (channel 2 dead alone). The best single
  channel is the LARGEST prime, by monotonicity in M.
  Log twin: H(b | ev) = [M(M-1)c^2 H2((c+1)/(2c))
  + Mc(c-1) log 2] / (N(N-1)) nats.
  Hand controls: N = 6, M = 3: 18 correct on unequal fibers + 3 on
  ties = 21/30 = 7/10 = 1/2 + 2/10. N = 6, M = 2: 12 + 6 = 18/30
  = 3/5 = 1/2 + 1/10.

HAND DERIVATION B (fixed before the engine; the tilt). Index
convention re-derived: x in {0..N-1}, fiber r = {r + jM : j =
0..c-1}, within-fiber weights theta^r q^j with q = theta^M. Write
t = QM + s, 0 <= s < M; the below-count B(r) = Q + [r < s] is fiber
geometry, prior-free (a marked transplant from the uniform case; the
POSTERIOR mechanics below are re-derived, not carried).
  P(below | r) = Pb(B(r)),  Pb(B) = (1 - q^B)/(1 - q^c)  [theta != 1]
  -- two fiber types (B = Q+1 for r < s, B = Q for r >= s). The type
  masses are (1 - theta^s)/(1 - theta^M) and (theta^s - theta^M)/
  (1 - theta^M) (they sum to 1 because 1 - q = 1 - theta^M scaled;
  a sign-flip trap was caught on paper here: for theta > 1 the max
  must be taken over probabilities, never over the (1-.) numerators,
  which all go negative).
      CEILING = [ (1-theta^s) max(Pb(Q+1), 1-Pb(Q+1))
                + (theta^s-theta^M) max(Pb(Q), 1-Pb(Q)) ]
                / (1 - theta^M)
      FLOOR   = max(Pg, 1-Pg),  Pg = (1-theta^t)/(1-theta^N)
      H(b|ev) = [ (1-theta^s) H2(Pb(Q+1))
                + (theta^s-theta^M) H2(Pb(Q)) ] / (1-theta^M).
  THE WINDOW LAW (the dial, deformed): Pb(B) > 1/2 iff B > Q* where
  Q* = log_q((1+q^c)/2), the same form for q < 1 and q > 1, with
  Q* -> c/2 as q -> 1. Since the two types are Q and Q+1:
      INTERIOR  iff  s != 0  AND  Pb(Q) < 1/2 < Pb(Q+1)
                iff  s != 0  AND  Q < Q* < Q+1.
  Q* lies strictly in (0, c) for every q != 1, so at every tilt the
  interior thresholds form EXACTLY ONE fiber window (floor(Q*) M,
  (floor(Q*)+1) M) -- M-1 thresholds -- unless Q* is an integer.
  THE RESONANCE READING: the uniform parity dial is the degenerate
  slice q = 1, where Q* = c/2 sits ON an integer exactly when c is
  even -- even-c deadness at all t is a resonance of the uniform
  point, not an anatomy invariant; any tilt moves Q* off the integer
  and even c comes alive in its one window. The uniform interior
  value's t-independence is a second q = 1 degeneracy: under tilt
  the interior value moves with s. DEAD CELLS: s = 0 makes every
  fiber the same type, so posterior = prior at BOTH scores, at EVERY
  theta -- the structurally dead set {M | t} is tilt-invariant, and
  it is the whole log-loss floor set (at s != 0, Pb(Q+1) > Pb(Q)
  strictly, so the posterior always moves); the 0-1 floor set adds
  every t outside the window -- the two scores' floor sets stay
  divergent at every tilt.
  SIGN-BIT COROLLARY: at t = N/2 with c even, s = 0: the sign eval's
  floor cells are dead at EVERY theta -- structural, not parity
  luck. The odd-c sign cells die when the tilt pushes Q* out of
  (m, m+1), m = (c-1)/2; the death boundary 2q^m = 1 + q^c is
  algebraic in q (c = 3: q^2 + q - 1 = 0, the reciprocal golden
  ratio). Derived bound: Q* < ln 2/ln(1/q) for q < 1, and every grid
  tilt theta <= 2/3 at M >= 2 gives q <= 4/9, hence Q* < 0.855 < 1
  <= m: the prediction is that EVERY theta != 1 on the grid kills
  EVERY sign-bit cell (theta > 1 by reflection) -- the sign eval
  survives only a narrow theta-window around uniform (the odd-c
  cells until Q* exits (m, m+1); the even-c cells never, s = 0),
  while the threshold FAMILY keeps one alive window at every tilt.
  Reflection identity (a control): x -> N-1-x maps theta to 1/theta
  and [x < t] to [x >= N-t] with evidence relabeled, so
  CEILING(theta, t) = CEILING(1/theta, N-t).
  Hand controls (theta = 1/2, N = 6, M = 3, q = 1/8): t = 3 (s = 0):
  every fiber Pb = 8/9 = the prior -- dead, ceiling = floor = 8/9.
  t = 2 (Q = 0, s = 2): type masses 6/7 and 1/7, Pb(1) = 8/9,
  Pb(0) = 0, ceiling = (6/7)(8/9) + 1/7 = 19/21 > floor = 16/21 --
  the even-c cell is INTERIOR at theta = 1/2, confirming the
  resonance on paper.

PREDICTIONS (fixed before the run).
  Comparison leg:
  CP1: brute ceiling = 1/2 + (M-1)/(2(N-1)) at every scanned cell.
  CP2: computed floor = 1/2 exactly; every cell strictly interior
       (floor < ceiling < 1): NO floor cells at any M.
  CP3: brute conditional entropy matches the log-twin formula within
       1e-12 nats; strictly below log 2 everywhere (no dead cells at
       either score).
  CP4: the order-the-residues achiever meets the ceiling exactly on
       every cell it is enumerated on; cost two CRT reconstructions
       plus one comparison.
  CP5: single channels obey the same law at M = p: value strictly
       increasing in p, largest prime best, channel 2 alive alone
       (worth 1/(2(N-1)) over the floor).
  Tilt leg:
  TT1: brute ceiling = the tilted closed form at every (N, M, theta,
       t) scanned; at theta = 1 it equals the uniform law of the
       sibling scripts.
  TT2: computed floor = max(Pg, 1-Pg) at every point.
  TT3: brute entropy matches the tilted log twin within 1e-12 nats.
  TT4: exact posterior-vs-prior census: posterior = prior on every
       fiber iff s = 0, at every theta.
  TT5: the interior set at fixed (cell, theta != 1) is exactly one
       fiber window of M-1 thresholds located at floor(Q*), for
       every cell including even c (the resonance: even-c cells are
       alive at every grid theta != 1); at theta = 1 it is M-1 for
       odd c and empty for even c.
  TT6: every sign-bit cell (t = ceil(N/2)) is dead at every grid
       theta != 1; the even-c ones are dead at every theta.
  TT7: the plug-in achiever meets the ceiling exactly at every
       (cell, theta, t) it runs on; constant cost per query.
  TT8: reflection: CEILING(theta, t) = CEILING(1/theta, N-t) on the
       grid.

KILL (observable): any scanned cell printing an accuracy, floor, or
entropy off its formula value. What such a print would mean is
weighed after the run, not encoded here. A tilt cell with no
matching closed form anywhere on the grid would be recorded as an
honest open, not paved over.

FINDINGS (tier-labeled; run record below; both kills MISSED -- every
scanned point matched its closed form).

1. THE COMPARISON CEILING (rule, proved + exhaustive on all 362
   cells, N <= 2310; every prediction CP1-CP5 confirmed). The Bayes
   0-1 ceiling of [x < y] through both residues mod M is
       1/2 + (M-1)/(2(N-1)),
   c drops out; the computed floor is exactly 1/2; there are NO
   floor cells -- every proper subset lifts, including M = 2: the
   CONSTANT DIAL, a third dial shape (sign: only channel 2 alive
   alone; orientation: channel 2 dead alone; comparison: everything
   alive). The order-the-residues achiever (two CRT reconstructions
   + one comparison) is exactly tight on all 116 cells with
   N <= 210. Single channels obey the same law at M = p, strictly
   increasing in p (at N = 2310: 1155/2309 for p = 2 rising to
   2319/4618 for p = 11) -- largest prime best. The per-fiber skew
   is again the universal unit (c+1)/(2c): every unequal-residue
   fiber is a staircase count on a c-ladder grid. Log twin within
   1e-12 nats everywhere, strictly below log 2 -- no dead cells at
   either score.

2. THE TILTED CEILING (rule, proved + exhaustive on all 116 cells
   N <= 210 x the full 9-point theta grid x EVERY threshold t, 1044
   sweeps, plus 234 spot points at N in {330, 462, 2310}; TT1-TT3,
   TT7, TT8 confirmed). Under the geometric tilt the threshold
   eval's ceiling, floor, and conditional entropy are the closed
   forms in the derivation (type-mass form); the theta = 1 grid
   point reproduces the uniform law exactly; the reflection identity
   holds; the plug-in achiever (CRT-reconstruct r, one closed-form
   comparison) is exactly tight at every (cell, theta, t) with
   N <= 105. The anatomy survives its first non-uniform prior with
   every value still closed-form.

3. THE WINDOW LAW AND THE RESONANCE (rule, proved + exhaustive; TT4,
   TT5 confirmed). At every theta the interior thresholds of a cell
   form EXACTLY ONE fiber window of M-1 thresholds, located at
   floor(Q*), Q* = log_q((1+q^c)/2); at theta = 1 the window
   parity-collapses (M-1 for odd c, EMPTY for even c). The uniform
   parity dial is a RESONANCE: Q* = c/2 sits on an integer exactly
   when c is even, and every grid tilt frees it -- all 39 even-c
   cells are alive at every theta != 1 (39/39 at each of the eight
   tilts; 0/39 at theta = 1). The structurally dead set {M | t}
   (posterior = prior at both scores) is TILT-INVARIANT, and it is
   the entire log-loss floor set at every theta, while the 0-1 floor
   set adds everything outside the window: the two scores' floor
   sets stay divergent at every prior in the family.

4. THE SIGN BIT IS MAXIMALLY PRIOR-FRAGILE (rule, proved +
   exhaustive; TT6 confirmed). Every sign-bit cell is dead at every
   grid theta != 1 (116/116 at all eight tilts, vs 39/116 -- the
   even-c cells -- at uniform): the derived bound Q* < ln 2/ln(1/q)
   pushes the window below the middle fiber at any tilt with
   q <= 4/9. The mechanism splits: the even-c sign cells sit at s = 0
   (t = N/2 on a fiber boundary), so their deadness is STRUCTURAL
   and survives every prior in the family -- the parity law's dead
   half was never about parity luck; the odd-c cells die at the
   algebraic death boundary 2q^m = 1 + q^c (c = 3: q = 1/phi, the
   reciprocal golden ratio). The threshold FAMILY, by contrast,
   keeps exactly one alive window at every tilt -- it slides away
   from the midpoint as the tilt strengthens (toward fiber 0 as
   q -> 0, toward fiber c-1 as q -> infinity). An eval built on one
   fixed threshold is prior-brittle; the family always has one
   live member, and the window law names which.

THE HEADLINE. The ceiling anatomy survives both remaining axes with
every value closed-form. The comparison eval is the cleanest
instance yet (constant dial, no floor cells, c-free formula), and
the prior dial DEFORMS the anatomy without breaking it: dials
generalize to one sliding window per tilt, the uniform prior is the
degenerate point where the window collapses by parity, deadness
splits into a structural tilt-invariant core ({M | t}, dead at both
scores, every prior) and a prior-relative remainder, and single-
threshold evals are prior-brittle while the family self-repairs.
"Knows its own ceiling" is not a uniform-prior accident.

RUN RECORD. Exit 0, ~18 s, memory trivial. Printed: controls all
reproduced (7/10, 3/5, 8/9 dead, 19/21 vs floor 16/21); comparison
362 cells all formula-exact, floor 1/2, achiever tight on N <= 210,
singles at N = 2310 as listed; tilt 1044 sweeps all formula-exact
with dead set {M | t} and one-window interior sets everywhere;
even-c alive 39/39 at each theta != 1, 0/39 at theta = 1; sign-bit
dead 116/116 at each theta != 1, 39/116 at theta = 1; reflection
confirmed; 234 spot points exact; ALL GREEN.
"""

from fractions import Fraction
from math import log, fsum
from itertools import combinations

PRIMES = [2, 3, 5, 7, 11, 13]
TOL = 1e-12
THETA_GRID = [Fraction(1, 10), Fraction(1, 3), Fraction(1, 2),
              Fraction(2, 3), Fraction(1), Fraction(3, 2),
              Fraction(2), Fraction(3), Fraction(10)]


def family(cap):
    """All (N, prime tuple) with N squarefree from >= 2 of PRIMES, N <= cap."""
    out = []
    for k in range(2, len(PRIMES) + 1):
        for combo in combinations(PRIMES, k):
            N = 1
            for p in combo:
                N *= p
            if N <= cap:
                out.append((N, combo))
    return sorted(out)


def proper_moduli(combo):
    """Every proper nonempty channel subset's modulus."""
    ms = []
    for k in range(1, len(combo)):
        for sub in combinations(combo, k):
            M = 1
            for p in sub:
                M *= p
            ms.append(M)
    return sorted(ms)


def H2(p):
    p = float(p)
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log(p) - (1.0 - p) * log(1.0 - p)


# ----------------------------------------------------------------- leg A

def comparison_brute(N, M):
    """Pair census by prefix sweep; returns (ceiling, floor, entropy,
    achiever score or None). No ladder structure is used: every
    ordered pair (x, y), x != y, is binned by (x mod M, y mod M) via
    'for each y, add all earlier x'."""
    less = [[0] * M for _ in range(M)]
    seen = [0] * M
    for y in range(N):
        b = y % M
        row_add = seen
        for a in range(M):
            less[a][b] += row_add[a]
        seen[b] += 1
    total = N * (N - 1)
    correct = 0
    ascend = 0
    ent_terms = []
    ach = 0
    for a in range(M):
        for b in range(M):
            # pair count from the COUNTED class sizes, not the known c
            pairs = seen[a] * seen[b] - (seen[a] if a == b else 0)
            l = less[a][b]
            ascend += l
            correct += max(l, pairs - l)
            ent_terms.append((pairs / total) * H2(Fraction(l, pairs)))
            # achiever: guess x<y iff a<b; x>y iff a>b; fixed x<y on ties
            ach += l if a <= b else pairs - l
    ent = fsum(ent_terms)
    floor = Fraction(max(ascend, total - ascend), total)
    return (Fraction(correct, total), floor, ent, Fraction(ach, total))


def comparison_formula(N, M):
    return Fraction(1, 2) + Fraction(M - 1, 2 * (N - 1))


def comparison_entropy_formula(N, M):
    c = N // M
    total = N * (N - 1)
    return (M * (M - 1) * c * c * H2(Fraction(c + 1, 2 * c))
            + M * c * (c - 1) * log(2.0)) / total


# ----------------------------------------------------------------- leg B

def tilt_formula(N, M, theta, t):
    """(ceiling, floor, entropy) closed forms at threshold t."""
    c = N // M
    Q, s = divmod(t, M)
    if theta == 1:
        ceil_ = Fraction(s * max(Q + 1, c - Q - 1)
                         + (M - s) * max(Q, c - Q), N)
        floor_ = Fraction(max(t, N - t), N)
        ent = (Fraction(s, M) * H2(Fraction(Q + 1, c))
               + Fraction(M - s, M) * H2(Fraction(Q, c)))
        return ceil_, floor_, ent
    q = theta ** M
    den = 1 - q ** c

    def Pb(B):
        return (1 - q ** B) / den

    pb1, pb0 = Pb(Q + 1), Pb(Q)
    w1 = (1 - theta ** s) / (1 - theta ** M)
    w0 = (theta ** s - theta ** M) / (1 - theta ** M)
    ceil_ = w1 * max(pb1, 1 - pb1) + w0 * max(pb0, 1 - pb0)
    pg = (1 - theta ** t) / (1 - theta ** N)
    floor_ = max(pg, 1 - pg)
    ent = float(w1) * H2(pb1) + float(w0) * H2(pb0)
    return ceil_, floor_, ent


def tilt_interior_predicate(N, M, theta, t):
    """The window law: interior iff s != 0 and Pb(Q) < 1/2 < Pb(Q+1)."""
    c = N // M
    Q, s = divmod(t, M)
    if s == 0:
        return False
    if theta == 1:
        return Fraction(Q, c) < Fraction(1, 2) < Fraction(Q + 1, c)
    q = theta ** M
    den = 1 - q ** c
    pb1 = (1 - q ** (Q + 1)) / den
    pb0 = (1 - q ** Q) / den
    return pb0 < Fraction(1, 2) < pb1


def tilt_cell_sweep(N, M, theta, check_achiever):
    """Exact incremental sweep over every t; asserts every prediction
    pointwise; returns the cell's interior-t list and the sign-bit
    verdict (t = ceil(N/2))."""
    c = N // M
    w = [theta ** x for x in range(N)]
    total = sum(w)
    ftot = [sum(w[r::M]) for r in range(M)]
    below = [Fraction(0)] * M
    below_all = Fraction(0)
    interior_ts = []
    sign_t = (N + 1) // 2
    sign_interior = None
    half = Fraction(1, 2)
    for t in range(1, N):
        below[(t - 1) % M] += w[t - 1]
        below_all += w[t - 1]
        num = Fraction(0)
        ach_num = Fraction(0)
        ent_terms = []
        pbs = []
        for r in range(M):
            bw = below[r]
            fw = ftot[r]
            num += max(bw, fw - bw)
            pbs.append(bw / fw)
            ent_terms.append(float(fw / total) * H2(bw / fw))
            if check_achiever:
                # plug-in: from evidence r alone, decide by closed form
                Q, s = divmod(t, M)
                B = Q + (1 if r < s else 0)
                if theta == 1:
                    guess_below = 2 * B > c
                else:
                    q = theta ** M
                    guess_below = (1 - q ** B) / (1 - q ** c) > half
                ach_num += bw if guess_below else fw - bw
        ceiling = num / total
        floor = max(below_all, total - below_all) / total
        f_ceil, f_floor, f_ent = tilt_formula(N, M, theta, t)
        assert ceiling == f_ceil, (N, M, theta, t, "ceiling")
        assert floor == f_floor, (N, M, theta, t, "floor")
        assert abs(fsum(ent_terms) - float(f_ent)) < TOL, \
            (N, M, theta, t, "H")
        # posterior = prior on every fiber iff s = 0
        pg = below_all / total
        all_prior = all(pb == pg for pb in pbs)
        assert all_prior == (t % M == 0), (N, M, theta, t, "dead-set")
        interior = ceiling > floor
        assert interior == tilt_interior_predicate(N, M, theta, t), \
            (N, M, theta, t, "window-law")
        if interior:
            interior_ts.append(t)
        if t == sign_t:
            sign_interior = interior
        if check_achiever:
            assert ach_num / total == ceiling, (N, M, theta, t, "achiever")
    return interior_ts, sign_interior


# ----------------------------------------------------------------- main

def main():
    # ---- controls first (hand values; asserted before any scan is read)
    ceil63, floor63, _, ach63 = comparison_brute(6, 3)
    assert ceil63 == Fraction(7, 10) and floor63 == Fraction(1, 2)
    ceil62, floor62, _, _ = comparison_brute(6, 2)
    assert ceil62 == Fraction(3, 5) and floor62 == Fraction(1, 2)
    assert ach63 == Fraction(7, 10)
    th = Fraction(1, 2)
    c3, f3, _ = tilt_formula(6, 3, th, 3)
    assert c3 == f3 == Fraction(8, 9)
    c2, f2, _ = tilt_formula(6, 3, th, 2)
    assert c2 == Fraction(19, 21) and f2 == Fraction(16, 21)
    print("controls: comparison 7/10, 3/5; tilt dead 8/9, interior "
          "19/21 vs floor 16/21 -- all hand values reproduced")

    # ---- leg A: the comparison eval, all 362 cells N <= 2310
    fam = family(2310)
    cells = 0
    for N, combo in fam:
        for M in proper_moduli(combo):
            ceiling, floor, ent, ach = comparison_brute(N, M)
            f = comparison_formula(N, M)
            assert ceiling == f, (N, M, "CP1")
            assert floor == Fraction(1, 2), (N, M, "CP2 floor")
            assert Fraction(1, 2) < ceiling < 1, (N, M, "CP2 interior")
            assert abs(ent - comparison_entropy_formula(N, M)) < TOL, \
                (N, M, "CP3")
            assert ent < log(2.0) - 1e-15, (N, M, "CP3 strict")
            if N <= 210:
                assert ach == ceiling, (N, M, "CP4")
            cells += 1
    # CP5: single channels, worked at N = 2310
    singles = sorted((comparison_formula(2310, p), p) for p in
                     [2, 3, 5, 7, 11])
    assert [p for _, p in singles] == [2, 3, 5, 7, 11], "CP5 order"
    print("comparison: %d cells, every ceiling = 1/2 + (M-1)/(2(N-1)),"
          " floor exactly 1/2, no floor cells; entropy twin < log 2"
          " everywhere; achiever tight on all N <= 210 cells" % cells)
    print("comparison single channels at N = 2310: " +
          ", ".join("p=%d: %s" % (p, v) for v, p in singles) +
          " (largest prime best)")

    # ---- leg B: the tilt scan, all cells N <= 210, full theta grid
    fam210 = [(N, combo) for N, combo in fam if N <= 210]
    cellcount = 0
    even_alive = {}
    sign_dead = {}
    for theta in THETA_GRID:
        even_alive[theta] = [0, 0]   # [even-c cells alive, even-c cells]
        sign_dead[theta] = [0, 0]    # [sign-bit-dead cells, cells]
    for N, combo in fam210:
        for M in proper_moduli(combo):
            c = N // M
            for theta in THETA_GRID:
                check_ach = N <= 105
                interior_ts, sign_int = tilt_cell_sweep(
                    N, M, theta, check_ach)
                # TT5: the interior set is one fiber window
                if theta == 1:
                    expected = 0 if c % 2 == 0 else M - 1
                    assert len(interior_ts) == expected, \
                        (N, M, theta, "TT5 uniform")
                else:
                    assert len(interior_ts) == M - 1, (N, M, theta, "TT5")
                    fibers = {t // M for t in interior_ts}
                    assert len(fibers) == 1, (N, M, theta, "TT5 window")
                    assert all(t % M != 0 for t in interior_ts)
                if c % 2 == 0:
                    even_alive[theta][1] += 1
                    if interior_ts:
                        even_alive[theta][0] += 1
                sign_dead[theta][1] += 1
                if not sign_int:
                    sign_dead[theta][0] += 1
                cellcount += 1
    print("tilt: %d (cell, theta) sweeps, every t; ceiling, floor,"
          " entropy all = closed form; dead set = {M | t} at every"
          " theta; interior set = one fiber window everywhere" % cellcount)
    for theta in THETA_GRID:
        ea, sd = even_alive[theta], sign_dead[theta]
        print("  theta=%-5s even-c cells alive %3d/%3d   sign-bit dead"
              " %3d/%3d" % (theta, ea[0], ea[1], sd[0], sd[1]))

    # TT8: reflection on a sample of cells and the paired grid values
    pairs = [(Fraction(1, 2), Fraction(2)), (Fraction(1, 3), Fraction(3)),
             (Fraction(1, 10), Fraction(10)),
             (Fraction(2, 3), Fraction(3, 2))]
    for N, combo in [(30, (2, 3, 5)), (105, (3, 5, 7)), (210, (2, 3, 5, 7))]:
        for M in proper_moduli(combo):
            for th1, th2 in pairs:
                for t in range(1, N):
                    a, _, _ = tilt_formula(N, M, th1, t)
                    b, _, _ = tilt_formula(N, M, th2, N - t)
                    assert a == b, (N, M, th1, t, "TT8")
    print("reflection: CEILING(theta, t) = CEILING(1/theta, N-t) on the"
          " sampled cells, all t, four theta pairs")

    # ---- spot leg: larger N, sampled t, theta in {1/2, 2}
    spot = [(330, (2, 3, 5, 11), [2, 11, 30, 165]),
            (462, (2, 3, 7, 11), [2, 11, 42, 231]),
            (2310, (2, 3, 5, 7, 11), [2, 11, 210, 1155])]
    spots = 0
    for N, combo, Ms in spot:
        for M in Ms:
            c = N // M
            for theta in [Fraction(1, 2), Fraction(2)]:
                w = [theta ** x for x in range(N)]
                total = sum(w)
                ftot = [sum(w[r::M]) for r in range(M)]
                # structured t sample incl. the predicted window fiber
                q = theta ** M
                den = 1 - q ** c
                mstar = None
                for Q in range(c):
                    if ((1 - q ** Q) / den < Fraction(1, 2)
                            < (1 - q ** (Q + 1)) / den):
                        mstar = Q
                        break
                Qs = {0, c // 2, c - 1}
                if mstar is not None:
                    Qs |= {mstar, max(mstar - 1, 0)}
                ss = {0, 1, M // 2, M - 1}
                ts = sorted({Q * M + s for Q in Qs for s in ss
                             if 1 <= Q * M + s <= N - 1} | {(N + 1) // 2})
                for t in ts:
                    # direct below-weight per fiber, no sweep
                    below = []
                    for r in range(M):
                        bw = Fraction(0)
                        for x in range(r, N, M):
                            if x < t:
                                bw += w[x]
                        below.append(bw)
                    num = sum(max(bw, fw - bw)
                              for bw, fw in zip(below, ftot))
                    ceiling = num / total
                    f_ceil, f_floor, _ = tilt_formula(N, M, theta, t)
                    assert ceiling == f_ceil, (N, M, theta, t, "spot")
                    ba = sum(below)
                    assert max(ba, total - ba) / total == f_floor
                    spots += 1
    print("spot: %d (N, M, theta, t) points at N in {330, 462, 2310},"
          " brute = closed form at every one" % spots)

    print("ALL GREEN")


if __name__ == "__main__":
    main()
