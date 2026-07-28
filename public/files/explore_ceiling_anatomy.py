"""explore_ceiling_anatomy.py -- THE CEILING ANATOMY AT GENERAL
THRESHOLDS AND AT A RELATION TASK (the third and fourth instances of
an evaluation that knows its own optimum; sibling of
explore_eval_ceiling.py and explore_induction_ceiling.py).

THE QUESTION. explore_eval_ceiling.py showed that "knows its own
ceiling" is designable: the sign bit [2x >= N] read through a proper
channel subset of a squarefree ring ships a provable closed-form
Bayes ceiling, with an exact one-bit dial (the parity of the unknown
cofactor c = N/M) separating dead cells from interior cells. Both
instances so far share an ANATOMY -- an exact dial partitioning the
eval family into floor cells and interior cells with closed-form
interior values. Two stress tests of that anatomy:

(A) THE THRESHOLD FAMILY. The sign bit is the threshold predicate
    [x >= t] at the midpoint t = ceil(N/2). What is the ceiling at
    GENERAL t, as a closed form in (t, M, N)? Does the parity dial
    survive off the midpoint, or deform into a t-indexed family?

(B) THE ORIENTATION TASK. A relation instance whose evidence fibers
    are NOT intervals: a uniform ordered triple of distinct points
    of Z/N, read through all three residues mod M; the task is the
    triple's cyclic orientation. Coarsening a cyclic group hides
    orientation totally -- both orientations occur in every fiber
    that contains a triple, so the ceiling is never 1 -- but the
    POSTERIOR SKEW inside a fiber is unpriced. Price it.

An EVAL is a triple (task family with prior, evidence channel,
score); its CEILING is the Bayes-optimal expected score; the FLOOR
is the prior's best score with the evidence severed -- for [x >= t]
that is max(t, N-t)/N, and for orientation it is EXACTLY 1/2
(swapping the last two points of an ordered distinct triple is an
orientation-reversing involution, so the prior is balanced);
NONTRIVIAL means strictly between floor and perfect; TIGHT means a
computable achiever with stated cost matches the ceiling.

DESIGN. Scan family: every squarefree N <= 500 that is a product
of >= 2 primes from {2, 3, 5, 7, 11, 13}, every proper nonempty
channel subset (modulus M, unknown cofactor c = N/M). Exact probabilities
(integer counts, Fraction); entropies in nats, tolerance 1e-12.
  Threshold leg: brute Bayes accuracy and conditional entropy at
  EVERY t in 1..N-1 on every scanned cell, against the derived
  closed forms; the plug-in achiever (CRT-reconstruct r, guess by
  the fiber majority) at every t on every cell with N <= 210 and at
  a structured boundary t-sample on every scanned cell; a second
  spot leg checks formula-vs-brute at the boundary t-sample on the
  wider family of explore_eval_ceiling.py capped at N <= 2310.
  Orientation leg: brute over all (N-1)(N-2) difference pairs
  (a, b) = (y-x, z-x) mod N -- the triple's x-residue is carried by
  the evidence but is independent of (a, b) and carries no
  orientation information, a reduction verified by the full-triple
  control below; per-fiber census against the derived class values;
  the difference-compare achiever; the log twin; single-channel
  prices.
  Controls (run and asserted before any scan is read): hand-computed
  threshold cells (N=6 M=2 t=2,3; N=30 M=6 t=13), the hand-counted
  orientation cell (N=6, M=3: ceiling 3/5, fiber skews 3/4 and 1/4,
  the empty all-zero fiber), and the FULL-TRIPLE control: at N = 30,
  every proper divisor M, the Bayes accuracy computed from the raw
  triple evidence (x, y, z mod M) over all N(N-1)(N-2) triples must
  equal the difference-pair ceiling and the closed form.

HAND DERIVATION (fixed before the engine; the index convention
re-derived, not recalled: x in {0..N-1}, residue r has fiber
{r + jM : j = 0..c-1}).

(A) Write t = qM + s, 0 <= s < M. The below-count in fiber r is
    B(r) = q + [r < s], so exactly two fiber types exist. Ceiling =
    (1/N)[s*max(q+1, c-q-1) + (M-s)*max(q, c-q)]. Case analysis:
    c EVEN: for every q, no fiber's majority side ever differs from
    the prior's majority side, so the ceiling collapses to the floor
    max(t, N-t)/N at EVERY threshold t -- the dead half of the
    parity dial survives verbatim off the midpoint.
    c ODD, c = 2m+1: ceiling = floor unless q = m and s != 0 (the
    threshold strictly inside the MIDDLE fiber window
    (mM, (m+1)M)), where every fiber scores (m+1)/c: ceiling =
    (c+1)/(2c), INDEPENDENT of t within the window, and the lift
    over the floor is the tent min(s, M-s)/N, maximal at the
    midpoint -- the sign bit is the extremal member of the family.
    Log loss: H(b|r) = (s/M)*H2((q+1)/c) + ((M-s)/M)*H2(q/c);
    posterior = prior iff s = 0. So the LOG floor set {s = 0} is
    thin while the 0-1 floor set is everything outside the odd-c
    middle windows: the two scores' floor sets DIVERGE at general t
    (their agreement at the midpoint is a coincidence of that
    family), and 0-1 deadness does not imply posterior = prior --
    off the middle window the posterior moves but never crosses 1/2.

(B) Translate the triple's base point to 0: a = (y-x) mod N,
    b = (z-x) mod N; (a, b) is uniform on ordered distinct nonzero
    pairs, independent of x, and orientation is positive iff a < b
    as integers. Given (alpha, beta) = (a, b) mod M, the posterior
    is uniform on a product of ladders, and the positive count is a
    staircase threshold count on a c-ladder grid:
    - alpha != beta, both nonzero (c x c grid): P(positive) =
      (c+1)/(2c) if alpha < beta, (c-1)/(2c) if alpha > beta -- the
      per-fiber skew is EXACTLY the sign eval's interior value;
      fiber Bayes score (c+1)/(2c).
    - alpha = beta, or exactly one of them zero: exactly 1/2 (the
      zero ladder's missing endpoint cancels the skew).
    - alpha = beta = 0 at c = 2: the one empty fiber.
    Weights give THE ORIENTATION CEILING
        1/2 + c(M-1)(M-2) / (2(N-1)(N-2)),
    nontrivial iff M >= 3: the sole dead proper subset is {2} --
    THE DIAL INVERTS between the two instances (the sign bit lives
    in channel 2 alone; orientation is blind through channel 2
    alone). Never perfect: every triple-containing fiber is skewed
    or balanced, never determined. Single channels obey the same
    formula at M = p, worth (p-1)(p-2)N/p up to shared scale --
    zero at p = 2 and strictly increasing in p, so the best single
    channel is the LARGEST prime read: the channel ordering also
    inverts against the sign eval, where channel 2 was the only
    single channel worth anything. Hand-counted case N = 6, M = 3:
    ceiling 3/5 (the kill below is refuted on paper before the
    engine runs).

PREDICTIONS (fixed before the run):
  TP1: c even: brute ceiling = max(t, N-t)/N at every t, every cell.
  TP2: c odd: brute ceiling = (c+1)/(2c) iff floor(t/M) = (c-1)/2
       and t mod M != 0, else max(t, N-t)/N; the interior lift is
       exactly min(t mod M, M - t mod M)/N.
  TP3: brute H(b|r) matches the two-point closed form (tol 1e-12);
       the log floor set is exactly {t : M | t}.
  TP4: the threshold achiever meets the brute ceiling exactly at
       every (cell, t) it runs on; constant cost per query (one CRT
       reconstruction, O(|S|) modular ops, one comparison).
  OP1: the orientation fiber census prints the four class values
       exactly ((c+1)/2c, (c-1)/2c, 1/2, empty); determined
       fraction 0.
  OP2: orientation ceiling = 1/2 + c(M-1)(M-2)/(2(N-1)(N-2)) on
       every cell; floor cells exactly the subset-{2} cells; every
       M >= 3 cell strictly interior; no cell perfect.
  OP3: the orientation log twin matches (tol 1e-12).
  OP4: the difference-compare achiever meets the ceiling exactly.
  OP5: single-channel values obey OP2's formula at M = p; channel 2
       worth exactly zero; values strictly increasing in p; joint
       ceiling >= best single on every multi-channel subset.

KILL (observables): (A) any scanned (cell, t) printing a brute value
off its formula -- the closed form fails at the stated bar. (B)
every scanned orientation cell printing Bayes accuracy exactly 1/2
-- the relation family is dead at scanned scope. What either print
would mean is weighed after the run, not encoded here.

FINDINGS (tier-labeled; run record below; the scan is exhaustive
over the stated family -- 194 (N, subset) cells over 37 rings
N <= 500, every threshold t -- and exact in probability; neither
kill fired).

1. THE THRESHOLD THEOREM (rule, proved + exhaustive on all 40914
   (cell, t) slices + 2508 wider-family spot slices; T1, T4). The
   Bayes 0-1 ceiling of [x >= t] through a proper channel subset is
   the no-evidence floor max(t, N-t)/N everywhere EXCEPT when the
   unknown cofactor c is odd AND t lies strictly inside the middle
   fiber window (mM, (m+1)M), m = (c-1)/2, where it is (c+1)/(2c)
   -- INDEPENDENT of t within the window. The parity dial survives
   at every threshold (even c is dead at ALL t); the odd half
   deforms into a window condition. The interior lift is the tent
   min(t mod M, M - t mod M)/N (verified on all 2697 interior
   slices), maximal at the midpoint: the sign eval of
   explore_eval_ceiling.py is the EXTREMAL member of the threshold
   family, sitting at the top of the tent.

2. THE TWO SCORES DISAGREE ABOUT DEADNESS (rule; T2, tol 1e-12).
   The log-loss ceiling is the two-point form
   (s/M)H2((q+1)/c) + ((M-s)/M)H2(q/c), and its floor set is the
   THIN set {t : M | t} (4599 slices) while the 0-1 floor set is
   almost everything (38217 of 40914 slices). At the midpoint the
   two floor sets happen to coincide (both = even c); at general t
   they diverge: 0-1 deadness does not mean posterior = prior --
   off the middle window the posterior moves but never crosses 1/2.
   Which score you ask decides whether the evidence is worthless.

3. TIGHT, WITH COST (rule + computed; T3). The plug-in solver (one
   CRT reconstruction, O(|S|) modular ops, one comparison) meets
   the ceiling exactly on all 12090 slices with N <= 210 (every t)
   and all 1137 boundary-sample slices above.

4. THE ORIENTATION CEILING (rule, proved + exhaustive on all 194
   cells; O1, plus the full-triple control S0b). The cyclic
   orientation of a uniform distinct triple read through modulus M
   has Bayes ceiling exactly
       1/2 + c(M-1)(M-2) / (2(N-1)(N-2)).
   The hiding is total (determined fraction 0 on every cell -- no
   fiber ever decides) yet the posterior skew is real and priced:
   every mixed fiber leans (c+1)/(2c) toward the residue order.
   Floor cells are EXACTLY the subset-{2} cells (19 of 194): THE
   DIAL INVERTS between instances -- the sign bit lives in channel
   2 alone, orientation is blind through channel 2 alone. The log
   twin matches (tol 1e-12) and the difference-compare achiever
   (two residue subtractions, one comparison) is exactly tight.

5. THE SKEW UNIT IS UNIVERSAL (observation across the two
   instances). The orientation eval's per-fiber value (c+1)/(2c)
   IS the sign eval's interior ceiling: inside a fiber, the
   relation question is again a staircase threshold count on a
   c-point ladder grid, and the whole-eval ceiling is that one
   quantity diluted by the mixed-fiber mass
   (M-1)(M-2)c^2/((N-1)(N-2)). The anatomy's interior values keep
   reducing to one skew unit.

6. CHANNEL VALUES ARE TASK-RELATIVE (rule; O2). Single channels
   obey the orientation formula at M = p: channel 2 worth exactly
   zero, value strictly increasing in p, so the best single channel
   is the LARGEST prime read -- the exact inverse of the sign
   eval's ordering, where channel 2 was the only paying channel.
   Worked example N = 210, S = {3, 5}: joint ceiling 885/1672 =
   1/2 + 49/1672, best single 5497/10868, price 511/21736.

THE HEADLINE. The anatomy survives both stress tests, deformed but
intact: an exact dial still partitions each family into floor cells
and interior cells with closed-form interior values -- at general
thresholds the dial gains a window clause ((c odd) AND (t inside
the middle window)) while the interior VALUE stays t-independent;
at the relation task the dial is simply M >= 3, with the sole dead
subset {2}. What changes between evals is WHICH channels pay: the
dial is task-relative, and the interior values of both families are
built from the same skew unit (c+1)/(2c).

HONEST LIMITS. (a) Exhaustive caps as stated (N <= 500 full,
N <= 2310 spot); the closed forms are proved for every N and proper
divisor M, so the caps touch only the confirmations. (b) 0-1 and
log scores only. (c) Uniform prior only (the ring's Haar measure);
skewed priors move the floor and are untested here -- since
explored (explore_ceiling_dials.py): under a geometric tilt
the threshold ceiling stays closed-form, the interior collapses to
ONE sliding fiber window, and the even-c deadness of this file is a
RESONANCE of the uniform point (Q* = c/2 integral iff c even) that
every tilt lifts. (d) The orientation
model is ordered distinct triples; cyclic relabelings preserve
orientation, so each cyclically-labeled instance is counted three
times and the quotient leaves every fiber value and the ceiling
unchanged (orientation of an UNLABELED point set is undefined --
any transposition flips it).

RUN RECORD (this file, python explore_ceiling_anatomy.py, ~3.5 s):
  S0 controls: threshold 2/3, 2/3, 3/5; orientation 3/5 -- pass.
  S0b full-triple control: raw-evidence Bayes = difference-pair
     ceiling = formula at N = 30, all 6 proper divisors -- pass.
  scan family: 194 (N, subset) cells over 37 rings, N <= 500.
  T1 threshold law on all 40914 slices; 2697 interior, lift =
     min(s, M-s)/N on every one -- pass.
  T2 log twin (tol 1e-12); log floor set = {M | t} exactly (4599
     slices) vs 0-1 floor set 38217 slices -- pass.
  T3 tight: achiever exact, 12090 all-t slices + 1137 sampled --
     pass.
  T4 spot leg: 2508 slices, NCAP < N <= 2310 -- pass.
  O1 orientation ceiling on all 194 cells; determined fraction 0;
     19 floor cells = exactly the subset-{2} cells; 175 interior;
     log twin + achiever exact -- pass.
  O2 price: channel 2 zero, value increasing in p; worked example
     N = 210, S = (3, 5): joint 885/1672, best single 5497/10868,
     price 511/21736 -- pass.
  all asserts green.

RUN: python explore_ceiling_anatomy.py  (exhaustive at the stated
caps, exact in probability; the controls are hand-computed cases
asserted before any scan is read).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from fractions import Fraction
from itertools import combinations
from math import log

PRIMES = (2, 3, 5, 7, 11, 13)
NCAP = 500        # exhaustive scan: every ring N <= NCAP
SPOT_NCAP = 2310  # threshold spot leg on the wider six-prime family
ACH_ALL_T_CAP = 210  # achiever runs at every t up to this N


def product(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def h2(p):
    """Binary entropy in nats; p a float or Fraction."""
    p = float(p)
    if p in (0.0, 1.0):
        return 0.0
    return -p * log(p) - (1 - p) * log(1 - p)


# ---------------- the threshold leg ----------------

def brute_threshold(N, M, t):
    """Exact Bayes 0-1 accuracy for guessing [x >= t] from x mod M,
    by direct fiber count."""
    c = N // M
    correct = 0
    for r in range(M):
        below = sum(1 for j in range(c) if r + j * M < t)
        correct += max(below, c - below)
    return Fraction(correct, N)


def threshold_formula(N, M, t):
    """The derived closed form: (c+1)/2c inside the odd-c middle
    window, the no-evidence floor everywhere else."""
    c = N // M
    q, s = divmod(t, M)
    if c % 2 == 1 and q == (c - 1) // 2 and s != 0:
        return Fraction(c + 1, 2 * c)
    return Fraction(max(t, N - t), N)


def threshold_floor(N, t):
    return Fraction(max(t, N - t), N)


def brute_threshold_entropy(N, M, t):
    """Exact-in-probability H([x >= t] | x mod M) in nats."""
    c = N // M
    total = 0.0
    for r in range(M):
        below = sum(1 for j in range(c) if r + j * M < t)
        total += h2(below / c) / M
    return total


def threshold_entropy_formula(N, M, t):
    c = N // M
    q, s = divmod(t, M)
    return (s * h2((q + 1) / c) + (M - s) * h2(q / c)) / M


def crt_weights(subset):
    """Precomputed CRT reconstruction weights for a channel subset."""
    M = product(subset)
    return M, [(M // p) * pow(M // p, -1, p) % M for p in subset]


def threshold_achiever(N, subset, t):
    """Run the plug-in solver on every x: read the subset residues,
    CRT-reconstruct r (O(|S|) modular ops), guess below iff the
    fiber's below-count is a majority. Returns exact accuracy."""
    M, weights = crt_weights(subset)
    c = N // M
    q, s = divmod(t, M)
    correct = 0
    for x in range(N):
        r = sum(w * (x % p) for w, p in zip(weights, subset)) % M
        assert r == x % M  # the reconstruction self-check
        guess_below = 2 * (q + (1 if r < s else 0)) >= c
        correct += guess_below == (x < t)
    return Fraction(correct, N)


def t_sample(N, M):
    """Structured boundary thresholds: window edges, midpoint, ends."""
    c = N // M
    cand = {1, 2, M - 1, M, M + 1, N // 2, N // 2 + 1, N - 2, N - 1}
    for q in ((c - 1) // 2, c // 2, (c + 1) // 2):
        cand.update({q * M - 1, q * M, q * M + 1, q * M + M // 2})
    return sorted(t for t in cand if 1 <= t <= N - 1)


# ---------------- the orientation leg ----------------

def orientation_formula(N, M):
    c = N // M
    return Fraction(1, 2) + Fraction(c * (M - 1) * (M - 2),
                                     2 * (N - 1) * (N - 2))


def orientation_entropy_formula(N, M):
    c = N // M
    T = (N - 1) * (N - 2)
    mixed = (M - 1) * (M - 2) * c * c
    return (mixed * h2(Fraction(c + 1, 2 * c)) + (T - mixed) * log(2)) / T


def orientation_scan(N, M):
    """Brute the orientation eval at one cell over all difference
    pairs. Returns (ceiling, entropy, achiever accuracy, determined
    count) and asserts the per-fiber class law."""
    c = N // M
    pos, tot = {}, {}
    for a in range(1, N):
        am = a % M
        for b in range(1, N):
            if b == a:
                continue
            key = (am, b % M)
            tot[key] = tot.get(key, 0) + 1
            if a < b:
                pos[key] = pos.get(key, 0) + 1
    T = (N - 1) * (N - 2)
    correct = ach_correct = n_det = 0
    ent = 0.0
    for key, tt in sorted(tot.items()):
        al, be = key
        pp = pos.get(key, 0)
        correct += max(pp, tt - pp)
        ent += tt * h2(pp / tt)
        if pp == 0 or pp == tt:
            n_det += tt
        if al != be and al != 0 and be != 0:
            assert tt == c * c, (N, M, key)
            want_num = c + 1 if al < be else c - 1  # P = want_num/(2c)
            assert 2 * c * pp == want_num * tt, (N, M, key)
            ach_correct += pp if al < be else tt - pp
        else:
            if al == be == 0:
                assert tt == (c - 1) * (c - 2), (N, M, key)
            elif al == be:
                assert tt == c * c - c, (N, M, key)
            else:
                assert tt == c * (c - 1), (N, M, key)
            assert 2 * pp == tt, (N, M, key)
            ach_correct += pp  # the achiever guesses positive here
    if c == 2:
        assert (0, 0) not in tot  # the one empty fiber
    return (Fraction(correct, T), ent / T, Fraction(ach_correct, T), n_det)


def full_triple_bayes(N, M):
    """Bayes accuracy from the RAW evidence (x, y, z mod M) over all
    ordered distinct triples -- the reduction control."""
    stats = {}
    for x in range(N):
        for y in range(N):
            if y == x:
                continue
            for z in range(N):
                if z == x or z == y:
                    continue
                key = (x % M, y % M, z % M)
                p, t = stats.get(key, (0, 0))
                stats[key] = (p + (((y - x) % N) < ((z - x) % N)), t + 1)
    T = N * (N - 1) * (N - 2)
    return Fraction(sum(max(p, t - p) for p, t in stats.values()), T)


def main():
    # ---- S0: positive controls (hand-computed before the engine) ----
    assert brute_threshold(6, 2, 2) == Fraction(2, 3)   # floor case
    assert brute_threshold(6, 2, 3) == Fraction(2, 3)   # window case
    assert threshold_formula(6, 2, 3) == Fraction(2, 3)
    assert brute_threshold(30, 6, 13) == Fraction(3, 5)
    assert threshold_formula(30, 6, 13) == Fraction(3, 5)
    ceil63, _, _, _ = orientation_scan(6, 3)
    assert ceil63 == Fraction(3, 5)
    print("S0 controls: threshold 2/3, 2/3, 3/5; orientation 3/5 -- pass")

    # ---- S0b: the full-triple reduction control at N = 30 ----
    for M in (2, 3, 5, 6, 10, 15):
        full = full_triple_bayes(30, M)
        pair, _, _, _ = orientation_scan(30, M)
        assert full == pair == orientation_formula(30, M), M
    print("S0b full-triple control: raw-evidence Bayes = difference-"
          "pair ceiling = formula at N = 30, all 6 proper divisors "
          "-- pass")

    # ---- the scan family ----
    rings = []
    for size in range(2, len(PRIMES) + 1):
        for ps in combinations(PRIMES, size):
            if product(ps) <= NCAP:
                rings.append(ps)
    cells = []
    for ps in rings:
        N = product(ps)
        for ssize in range(1, len(ps)):
            for sub in combinations(ps, ssize):
                cells.append((N, ps, sub))
    print(f"scan family: {len(cells)} (N, subset) cells over "
          f"{len(rings)} rings, N <= {NCAP}")

    # ---- T1: the threshold closed form at every t ----
    n_slices = n_interior = 0
    for N, ps, sub in cells:
        M = product(sub)
        c = N // M
        for t in range(1, N):
            got = brute_threshold(N, M, t)
            want = threshold_formula(N, M, t)
            assert got == want, (N, M, t, got, want)
            fl = threshold_floor(N, t)
            s = t % M
            if got > fl:
                n_interior += 1
                assert got - fl == Fraction(min(s, M - s), N), (N, M, t)
            n_slices += 1
    print(f"T1 threshold law: brute = closed form on all {n_slices} "
          f"(cell, t) slices; {n_interior} interior, lift = "
          f"min(s, M-s)/N on every one -- pass")

    # ---- T2: the log twin + the diverging floor sets ----
    n_log_floor = n_01_floor = 0
    for N, ps, sub in cells:
        M = product(sub)
        for t in range(1, N):
            got = brute_threshold_entropy(N, M, t)
            want = threshold_entropy_formula(N, M, t)
            assert abs(got - want) < 1e-12, (N, M, t)
            near_prior = abs(got - h2(t / N)) < 1e-9
            assert near_prior == (t % M == 0), (N, M, t)
            n_log_floor += near_prior
            n_01_floor += threshold_formula(N, M, t) == threshold_floor(N, t)
    print(f"T2 log twin: H matches the two-point form on all slices "
          f"(tol 1e-12); log floor set = {{M | t}} exactly "
          f"({n_log_floor} slices) vs 0-1 floor set {n_01_floor} "
          f"slices -- the two scores' floor sets diverge -- pass")

    # ---- T3: the achiever ----
    n_all = n_samp = 0
    for N, ps, sub in cells:
        M = product(sub)
        ts = range(1, N) if N <= ACH_ALL_T_CAP else t_sample(N, M)
        for t in ts:
            assert threshold_achiever(N, sub, t) == \
                threshold_formula(N, M, t), (N, sub, t)
            if N <= ACH_ALL_T_CAP:
                n_all += 1
            else:
                n_samp += 1
    print(f"T3 tight: the CRT plug-in solver meets the ceiling exactly "
          f"-- every t on N <= {ACH_ALL_T_CAP} ({n_all} slices), "
          f"boundary sample above ({n_samp} slices) -- pass")

    # ---- T4: the spot leg on the wider six-prime family ----
    n_spot = 0
    for size in range(2, len(PRIMES) + 1):
        for ps in combinations(PRIMES, size):
            N = product(ps)
            if N > SPOT_NCAP or N <= NCAP:
                continue
            for ssize in range(1, len(ps)):
                for sub in combinations(ps, ssize):
                    M = product(sub)
                    for t in t_sample(N, M):
                        assert brute_threshold(N, M, t) == \
                            threshold_formula(N, M, t), (N, M, t)
                        n_spot += 1
    print(f"T4 spot leg: formula = brute at boundary thresholds on the "
          f"wider family NCAP < N <= {SPOT_NCAP} ({n_spot} slices) "
          f"-- pass")

    # ---- O1: the orientation ceiling ----
    n_floor = n_int = 0
    for N, ps, sub in cells:
        M = product(sub)
        ceiling, ent, ach, n_det = orientation_scan(N, M)
        assert ceiling == orientation_formula(N, M), (N, sub)
        assert n_det == 0, (N, sub)
        assert ceiling < 1
        assert abs(ent - orientation_entropy_formula(N, M)) < 1e-12, (N, sub)
        assert ach == ceiling, (N, sub)
        if ceiling == Fraction(1, 2):
            n_floor += 1
            assert sub == (2,), (N, sub)
        else:
            n_int += 1
            assert M >= 3, (N, sub)
    print(f"O1 orientation ceiling = 1/2 + c(M-1)(M-2)/(2(N-1)(N-2)) "
          f"on all {len(cells)} cells; determined fraction 0 "
          f"everywhere; floor cells exactly the subset-{{2}} cells "
          f"({n_floor} of them, {n_int} interior); log twin (tol "
          f"1e-12) and difference-compare achiever exact -- pass")

    # ---- O2: single-channel prices and the inverted ordering ----
    for N, ps, sub in cells:
        if len(sub) < 2:
            continue
        M = product(sub)
        joint = orientation_formula(N, M)
        singles = [orientation_formula(N, p) for p in sub]
        assert max(singles) <= joint, (N, sub)
        for p, v in zip(sub, singles):
            if p == 2:
                assert v == Fraction(1, 2), (N, p)
        for (p1, v1), (p2, v2) in zip(list(zip(sub, singles))[:-1],
                                      list(zip(sub, singles))[1:]):
            assert v1 < v2, (N, sub, p1, p2)
    ex_N, ex_sub = 210, (3, 5)
    ex_joint = orientation_formula(ex_N, product(ex_sub))
    ex_singles = {p: orientation_formula(ex_N, p) for p in ex_sub}
    ex_best = max(ex_singles.values())
    print(f"O2 price: single channels obey the same formula at M = p; "
          f"channel 2 worth exactly zero, value strictly increasing "
          f"in p (the ordering inverts against the sign eval) -- pass")
    print(f"   worked example N = {ex_N}, S = {ex_sub}: joint ceiling "
          f"{ex_joint} = 1/2 + {ex_joint - Fraction(1, 2)}, best "
          f"single channel {ex_best}, price {ex_joint - ex_best}")

    print("all asserts green")


if __name__ == "__main__":
    main()
