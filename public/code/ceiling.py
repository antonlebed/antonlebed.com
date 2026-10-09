"""ceiling.py -- evaluations whose Bayes-optimal score is derived, not
estimated: an integer read through a proper set of its residue channels
and asked one question about its size or its order.

QUESTION. Take x in Z/N, N = Mc, and let the evidence be the residue
r = x mod M, read through the channels whose product is M; the FIBER
over r is the c integers r + jM, j = 0..c-1, and c is the COFACTOR. An
EVAL is a task with a prior, this evidence and a score. Its CEILING is
the Bayes-optimal expected score, its FLOOR the best score with the
evidence severed, and a cell (N, M) is DEAD when the two coincide. For
which tasks is the ceiling a closed form in (N, M), which cells are
dead, what does a solver that attains the ceiling cost, and what
happens to all of it when the uniform prior is tilted to theta^x?

THE TASKS.
  SIGN       [2x >= N], one size bit.
  THRESHOLD  [x >= t] at every t, written t = QM + s, 0 <= s < M.
  ORIENTATION  the cyclic orientation of a uniform ordered triple of
             distinct points, all three read mod M; positive iff
             (y - x) mod N < (z - x) mod N.
  COMPARISON [x < y] on a uniform ordered pair of distinct points,
             both read mod M.
  MAGNITUDE  the class Y = floor(kx/N) out of k, the sign bit at k = 2.
Scores: 0-1 accuracy, and log-loss (conditional entropy in nats).
The tilted prior puts weight theta^x on x; q = theta^M is the ratio
between neighbours within a fiber, and theta = 1 is uniform.

THE ARGUMENT (written before the engine).
  (A) SIGN. The below-count of fiber r is #{j : 2(r + jM) < N} =
      ceil(c/2 - r/M). At even c it is c/2 on every fiber, so the
      posterior is the prior. At odd c it is (c+1)/2 for r < M/2 and
      (c-1)/2 otherwise, so every fiber scores (c+1)/2c. Hence the
      ceiling is (c+1)/2c at odd c and 1/2 at even c, the log-loss
      twin H2((c+1)/2c) and log 2. With N squarefree and even, c is
      even iff 2 does not divide M: the dead cells are exactly those.
      At odd N every c is odd and (c+1)/2c > (N+1)/2N whenever M > 1. A lone
      channel p is the same law at M = p. The achiever reconstructs r
      from the channels read (one CRT combination) and compares 2r
      with M.
  (B) THRESHOLD. Fiber r holds Q + [r < s] points below t, so only two
      fiber types exist. At even c no fiber's majority differs from the
      prior's, so the ceiling is the floor max(t, N - t)/N at every t.
      At c = 2m + 1 the ceiling leaves the floor exactly when Q = m and
      s != 0, where every fiber scores (m+1)/c = (c+1)/2c whatever t
      is, and the lift over the floor is the tent min(s, M - s)/N,
      largest at the midpoint: the sign bit is the family's extremal
      member. The log-loss is (s/M) H2((Q+1)/c) + ((M-s)/M) H2(Q/c),
      equal to the prior's entropy iff s = 0; so the log-loss floor set
      is the thin set {M | t} while the 0-1 floor set is everything
      outside the odd-c middle range. Off that range the posterior
      moves but never crosses 1/2.
  (C) ORIENTATION. Translate x to 0: (a, b) = (y - x, z - x) mod N is
      uniform on ordered distinct nonzero pairs, independent of x, and
      the orientation is [a < b]. With (alpha, beta) = (a, b) mod M,
      a fiber with alpha != beta, both nonzero, is a c-by-c ladder
      grid and holds (c+1)/2c positives when alpha < beta, (c-1)/2c
      otherwise; alpha = beta, or one of them zero, is balanced (the
      zero residue's ladder lacks the point 0, which cancels the
      skew). Weighting: ceiling 1/2 + c(M-1)(M-2)/(2(N-1)(N-2)), floor
      1/2, dead iff M = 2, never 1. A lone channel p is worth a value
      increasing in p, zero at p = 2. The achiever subtracts residues
      channel by channel, CRT-combines the two differences and
      compares them.
  (D) COMPARISON. With (r_x, r_y) = (x, y) mod M, both ladders are
      full: r_x < r_y gives (c+1)/2c, r_x > r_y (c-1)/2c, r_x = r_y
      exactly 1/2. Weighting:
      ceiling 1/2 + (M-1)/(2(N-1)), free of c; floor exactly 1/2; no
      dead cell, M = 2 included. The achiever CRT-combines both
      residues and compares them.
  (E) THE SKEW UNIT. In (A)-(D) every interior fiber is a staircase
      count on a c-point ladder and scores (c+1)/2c. Four tasks carry
      three gauge shapes: the RANGE (sign and threshold; at the
      midpoint the range condition is c odd), the INVERTED gauge
      (orientation, dead only at M = 2) and the CONSTANT gauge
      (comparison, never dead).
  (F) THE TILT. Fiber r's weights are theta^r q^j, so the probability
      that a fiber of below-count J lies below t is
      Pb(J) = (1 - q^J)/(1 - q^c), increasing in J. A fiber leans
      below iff Pb(J) > 1/2 iff J > Q*, Q* = log_q((1 + q^c)/2), and
      Q* lies strictly in (0, c) for q != 1. With the two types Q and
      Q + 1, a threshold is live iff s != 0 and Q < Q* < Q + 1:
      THE THRESHOLD-RANGE LAW, one fiber range of M - 1 thresholds at
      floor(Q*), empty iff Q* is an integer J, i.e. iff q is a root of
      f(q) = q^c - 2q^J + 1. At s = 0 every fiber has one type and the
      posterior is the prior at every theta: the seam {M | t} is
      tilt-invariant and is the whole log-loss floor set. The map
      x -> N - 1 - x sends theta to 1/theta and t to N - t, so the
      ceiling at (theta, t) equals the ceiling at (1/theta, N - t).
  (G) THE RESONANCE CRITERION. f is monic with constant term 1, so its
      only rational roots are +-1: no rational q other than 1, hence
      no rational tilt off uniform, is resonant. Its signs +, -, +
      allow two positive roots (Descartes), one of them q = 1, with
      f'(1) = c - 2J; from f(0) = 1 and f -> infinity, at 2J < c the
      other root lies in (0, 1) and at 2J > c in (1, infinity). At
      2J = c q = 1 is a double root and the only one: the uniform
      point is where the whole 2J = c family collapses, which is the
      even-c deadness of (A). q -> 1/q exchanges J and c - J. At
      (J, c) = (1, 3), f = (q - 1)(q^2 + q - 1): the reciprocal golden
      ratio.
  (H) MAGNITUDE. Write c = ak + v, 0 <= v < k. Y is nondecreasing in j,
      so at fixed r the classes are contiguous blocks of fiber indices.
      With f = r/M the block of class y has length
      a + ceil((y+1)v/k - f) - ceil(yv/k - f), which is a or a + 1,
      with exactly v heavy (length a + 1) classes, the heavy set being
      {floor(k(l + f)/v) : l = 0..v-1} and the first heavy class
      y1(r) = floor(kr/(vM)). At uniform every atom's best class
      carries ceil(c/k)/c, so the ceiling is ceil(c/k)/c and the floor
      ceil(N/k)/N; the cell is dead iff M ceil(c/k) = ceil(Mc/k), iff
      v = 0 or M(k - v) < k (SATURATION, class 0 heavy at every atom,
      possible only at k > M). At k = 2 this is (A). Guessing y1(r)
      attains the ceiling. Under the tilt a block starting at lo of
      length w carries mass q^lo (1 - q^w): q's powers are monotone, so
      among blocks of equal length the first wins at q < 1, and a heavy
      block beats every later light one. So off uniform an atom's best
      class is 0 or y1(r) at q < 1, and by the same count from the top
      the last heavy class or k - 1 at q > 1: at most four classes are
      ever optimal at an atom off uniform. At q < 1 the floor's guess
      is class 0, and an atom with y1 >= 1 overrules it iff
      g(q) = 1 - q^a - q^L + q^(L+a+1) < 0, L = a y1(r); g has signs
      +, -, -, +, a root at 1 with g'(1) = 1, and g(0) = 1 at a >= 1,
      so one root in (0, 1), and the atom overrules above it. At a = 0
      an atom with y1 >= 1 has an empty class 0 and overrules at every
      q < 1. The partition Y is a floor partition, NOT symmetric under
      x -> N - 1 - x, so the q > 1 side is read on its own: an atom
      whose top class is light overrules the floor's guess k - 1 above
      1/root of g at L = a(k - 1 - ylast), and at a = 0 an empty top
      class overrules at every q > 1. So every cell is alive on one
      open arc (q_lo, q_up) of q and dead off it: at v = 0 the arc is
      empty; q_lo = 1 at saturation; q_up is infinite at a = 0. When
      M > k and a >= 1 some atom has y1 = 1, so L = a and the lower
      edge is the root of q^(2a+1) - 2q^a + 1 in (0, 1), the resonance
      root rho_a of (G) at (J, c) = (a, 2a + 1), a function of
      floor(c/k) alone; the upper edge is 1/rho_a. The sign bit is the
      k = 2 row: at odd c = 2m + 1 it is alive exactly for q in
      (rho_m, 1/rho_m).

DESIGN. Every probability is an exact integer count or Fraction; a tilt
theta = num/den is carried as the integer weight num^x den^(N-1-x), so
tilted ceilings are exact. Entropies are floats checked to 1e-12. The
rings are the squarefree N built from two or more of 2, 3, 5, 7, 11, 13,
each read through every proper nonempty channel subset.
  sign        every ring (57 rings, N to 30030), every subset; the
              achiever run from the channel residues at N <= 2310.
  threshold   every ring N <= 500, every subset, every t, by an
              incremental sweep of the per-fiber below-counts; the
              achiever at N <= 210.
  orientation every ring N <= 210, every subset, over all difference
              pairs; the full-triple control at N = 30.
  comparison  every ring N <= 210, every subset, over all pairs.
  tilt        every ring N <= 105, every subset, theta on {1/10, 1/3,
              1/2, 2/3, 1, 3/2, 2, 3, 10}, every t.
  resonance   every q = num/den with num, den <= 40 coprime and
              num != den, every c <= 12, every 0 < J < c, in
              integers; each (J, c) pair's roots located by bisection
              and a sign scan of (0, 8].
  magnitude   uniform: M in {2, 3, 6, 15, 35}, c in 2..12, k in 2..9;
              tilted: M in {2, 3, 6, 15}, c in 2..10, k in 2..6, on
              {1/5, 1/2, 4/5, 9/10, 199/200, 201/200, 10/9, 2, 5},
              plus rational tilts 5% inside and outside each finite
              arc end; every exact verdict is read against the arc and
              against overrules(), alive at the first atom whose g is
              negative.
Controls run first and gate the rest: C0's sign, threshold, orientation
and comparison cells, the threshold and comparison ones counted inline,
so they check the hand values and not the sweep; the tilt and
magnitude hand cells run inside their sections.

PREDICTIONS (fixed before the engine).
  C0 hand cells: sign N = 6, M = 3 gives 2/3 and N = 6, M = 2 gives
     1/2 (WRONG as frozen, the two cells swapped: see FINDINGS);
     threshold N = 30, M = 6, t = 13 gives 3/5; orientation
     N = 6, M = 3 gives 3/5; comparison N = 6 gives 7/10 at M = 3 and
     3/5 at M = 2; at theta = 1/2, N = 6, M = 3 the threshold t = 3 is
     dead at 8/9 and t = 2 scores 19/21 against the floor 16/21;
     magnitude M = 15, c = 7, k = 2 gives 4/7 and M = 2, c = 3, k = 5
     is dead at 1/3.
  P1 (A) at every sign cell: ceiling, floor set, log twin, achiever.
  P2 (B) at every threshold slice: ceiling, the tent, the two floor
     sets, the achiever.
  P3 (C) at every orientation cell, the determined fraction 0, and the
     full-triple control equal to the difference-pair ceiling.
  P4 (D) at every comparison cell.
  P5 (F) at every tilted slice: posterior = prior iff M | t; the
     live set exactly one range of M - 1 thresholds at the J the
     exact test Pb(J) < 1/2 < Pb(J + 1) names, empty at theta = 1 for
     even c; every even-c cell alive at every theta != 1; reflection.
  P6 (G): no rational root; one root per 2B != c pair on the side
     sign(2B - c) names; the double root alone at 2B = c; reflection
     of the roots; the golden control.
  P7 (H): block lengths and heavy set, uniform ceiling and floor, the
     dead-cell equivalence, the achiever, the four-class set off
     uniform, the arc law at every v >= 1 tilted cell, the band
     (rho_a, 1/rho_a) at M > k, and the sign-bit row.

KILL. Any printed ceiling, floor, entropy, count or root off its
predicted value, at any cell. Only the printed value decides.

FINDINGS. No kill fired; every law (A)-(H) held at every cell. One
frozen control was wrong: C0 swapped the sign-bit hand cells. At
N = 6, M = 3 the cofactor is 2, even, so the cell is dead at 1/2; at
M = 2 it is 3, odd, and scores 2/3. The engine printed the law's
values, and the control was rewritten to them. Two other first-run
FAILs were errors in the checks, not the law: the lone-channel check
read the smallest prime present as channel 2, and a literal carried
c = 7 for c = 14.
  sign        602 cells over 57 rings: 211 dead, exactly the cells
              with N even and M odd, 391 interior; the achiever exact
              on 362 cells; N = 2310 read at {2, 3, 5} scores 39/77,
              its best lone channel 578/1155, a price of 1/165.
  threshold   194 cells, 40,914 slices: 2,697 interior, each on the
              tent; the log-loss floor set 4,599 slices, exactly
              {M | t}, against the 0-1 floor set's 38,217.
  orientation 116 cells, 15 dead, exactly M = 2; no fiber decides;
              N = 210 read at {3, 5} scores 885/1672 against its best
              lone channel's 5497/10868.
  comparison  116 cells, floor exactly 1/2, none dead.
  tilt        64 cells x 9 tilts: one range of M - 1 at every tilt
              off uniform; every even-c cell alive at every theta != 1
              (20 of 20 at each), none at theta = 1.
  resonance   64,548 rational tuples, no root; 60 pairs with one root
              each on the predicted side, 6 double roots at 2J = c
              (P6 writes B for J).
  magnitude   428 uniform cells, 144 dead, 44 of them saturated; the
              arc law at 1,938 exact probes; the band (rho_a, 1/rho_a)
              at all 44 cells with M > k and a >= 1, rho_1..rho_6 =
              0.618034, 0.848375, 0.920568, 0.951425, 0.967305,
              0.976518. The sign bit M = 15, c = 3 is alive at
              theta = 199/200 (q = 0.928) and dead at 24/25 (q = 0.542),
              either side of rho_1.

RUN RECORD. python ceiling.py: 47 of 47 checks, 1.6 s, peak commit
16.8 MB; after an audit, the controls gating the rest, 47 of 47,
1.6 s, 17.3 MB.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from fractions import Fraction
from itertools import combinations
from math import ceil, log, prod, gcd

from crt import Ring, decode_from

PRIMES = (2, 3, 5, 7, 11, 13)
TOL = 1e-12
THETAS = [Fraction(1, 10), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3),
          Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3),
          Fraction(10)]
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tag = "ok  " if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))


def section(title):
    print()
    print(title)


def H2(p):
    p = float(p)
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log(p) - (1 - p) * log(1 - p)


def cells(cap):
    """Every (N, S): N squarefree from >= 2 of PRIMES, N <= cap, S a
    proper nonempty subset of N's primes (the channels read)."""
    out = []
    for n in range(2, len(PRIMES) + 1):
        for ps in combinations(PRIMES, n):
            N = prod(ps)
            if N > cap:
                continue
            for m in range(1, n):
                for S in combinations(ps, m):
                    out.append((N, ps, S))
    return out


# ------------------------------------------------------------ sign bit

def sign_brute(N, M):
    """Exact 0-1 ceiling and conditional entropy of [2x >= N] from x mod M."""
    c = N // M
    right, ent = 0, 0.0
    for r in range(M):
        below = sum(1 for j in range(c) if 2 * (r + j * M) < N)
        right += max(below, c - below)
        ent += H2(Fraction(below, c)) / M
    return Fraction(right, N), ent


def sign_achiever(N, ps, S):
    """Reconstruct r from the channels read, guess 'below' iff 2r < M."""
    ring = Ring(ps)
    idx = [ps.index(p) for p in S]
    M = prod(S)
    right = 0
    for x in range(N):
        res = tuple(x % p for p in ps)
        r = decode_from(res, ring, idx)
        right += (2 * r < M) == (2 * x < N)
    return Fraction(right, N)


def section_sign():
    section("THE SIGN BIT: the parity law")
    fam = cells(30030)
    rings = {N for N, _, _ in fam}
    bad_ceiling = bad_floor = bad_log = 0
    dead = interior = 0
    for N, ps, S in fam:
        M = prod(S)
        c = N // M
        ceil_, ent = sign_brute(N, M)
        floor_ = Fraction(max((N + 1) // 2, N // 2), N)
        want = Fraction(c + 1, 2 * c) if c % 2 else Fraction(1, 2)
        bad_ceiling += ceil_ != want
        is_dead = ceil_ == floor_
        bad_floor += is_dead != (2 in ps and 2 not in S)
        dead += is_dead
        interior += floor_ < ceil_ < 1
        want_log = H2(want) if c % 2 else log(2)
        bad_log += abs(ent - want_log) > TOL
    print(f"  {len(fam)} cells over {len(rings)} rings")
    check("ceiling (c+1)/2c at odd c, 1/2 at even c", bad_ceiling == 0,
          f"{bad_ceiling} off")
    check("dead iff N is even and M odd", bad_floor == 0,
          f"{dead} dead, {interior} interior")
    check("log-loss H2((c+1)/2c) and log 2", bad_log == 0)
    small = [(N, ps, S) for N, ps, S in fam if N <= 2310]
    bad = sum(sign_achiever(N, ps, S) != sign_brute(N, prod(S))[0]
              for N, ps, S in small)
    check("one CRT combination and one comparison attain the ceiling",
          bad == 0, f"{len(small)} cells, N <= 2310")
    N = 2310
    joint = sign_brute(N, 30)[0]
    single = max(sign_brute(N, p)[0] for p in (2, 3, 5))
    check("N = 2310 read at {2, 3, 5}: 39/77 against the best lone "
          "channel 578/1155, price 1/165",
          (joint, single, joint - single)
          == (Fraction(39, 77), Fraction(578, 1155), Fraction(1, 165)))
    lone = [(N, p) for N in rings for p in PRIMES if N % p == 0]
    bad = 0
    for N, p in lone:
        v = sign_brute(N, p)[0]
        if N % 2 == 0:
            want = Fraction(1, 2) + Fraction(1, N) if p == 2 else \
                Fraction(1, 2)
        else:
            want = Fraction(1, 2) + Fraction(p, 2 * N)
        bad += v != want
    check("a lone channel: only 2 earns at even squarefree N (1/2 + 1/N); "
          "every p earns 1/2 + p/2N at odd N", bad == 0, f"{len(lone)} pairs")


# ----------------------------------------------------------- threshold

def section_threshold():
    section("THE THRESHOLD FAMILY: one threshold range, one tent")
    fam = cells(500)
    slices = interior = log_floor = zero_one_floor = 0
    bad_ceiling = bad_tent = bad_log = bad_core = bad_ach = 0
    for N, ps, S in fam:
        M = prod(S)
        c = N // M
        m = (c - 1) // 2
        below = [0] * M
        right = M * c                 # t = 0: every fiber all above
        hist = {0: M}
        for t in range(1, N):
            r = (t - 1) % M
            old = below[r]
            right -= max(old, c - old)
            below[r] = old + 1
            right += max(old + 1, c - old - 1)
            hist[old] -= 1
            hist[old + 1] = hist.get(old + 1, 0) + 1
            slices += 1
            Q, s = divmod(t, M)
            ceil_ = Fraction(right, N)
            floor_ = Fraction(max(t, N - t), N)
            inside = c % 2 == 1 and Q == m and s != 0
            want = Fraction(c + 1, 2 * c) if inside else floor_
            bad_ceiling += ceil_ != want
            if inside:
                interior += 1
                bad_tent += ceil_ - floor_ != Fraction(min(s, M - s), N)
            zero_one_floor += ceil_ == floor_
            ent = sum(n * H2(Fraction(b, c)) for b, n in hist.items()
                      if n) / M
            want_log = (s / M) * H2(Fraction(Q + 1, c)) \
                + ((M - s) / M) * H2(Fraction(Q, c))
            bad_log += abs(ent - want_log) > TOL
            core = all(b * N == c * t for b in below)
            log_floor += core
            bad_core += core != (s == 0)
            if N <= 210:
                # closed-form achiever: fiber r lies below iff its
                # count Q + [r < s] beats c minus it
                got = sum((Q + (rr < s)) if 2 * (Q + (rr < s)) > c
                          else c - (Q + (rr < s)) for rr in range(M))
                bad_ach += got != right
    print(f"  {len(fam)} cells, {slices} (cell, t) slices")
    check("ceiling = floor off the odd-c middle range, (c+1)/2c inside",
          bad_ceiling == 0, f"{interior} interior slices")
    check("the lift is the tent min(s, M - s)/N", bad_tent == 0)
    check("log-loss two-point form", bad_log == 0)
    check("posterior = prior iff M | t", bad_core == 0,
          f"log floor {log_floor} slices, 0-1 floor {zero_one_floor}")
    check("the closed-form achiever attains the ceiling (N <= 210)",
          bad_ach == 0)


# ------------------------------------------- orientation and comparison

def orientation_counts(N, M):
    pos, neg = {}, {}
    for a in range(1, N):
        for b in range(1, N):
            if a == b:
                continue
            key = (a % M, b % M)
            if a < b:
                pos[key] = pos.get(key, 0) + 1
            else:
                neg[key] = neg.get(key, 0) + 1
    return pos, neg


def section_orientation():
    section("ORIENTATION INVERTS THE GAUGE; COMPARISON HAS NONE")
    fam = cells(210)
    bad = bad_det = bad_dead = bad_log = bad_ach = 0
    dead = 0
    for N, ps, S in fam:
        M = prod(S)
        c = N // M
        pos, neg = orientation_counts(N, M)
        keys = set(pos) | set(neg)
        right = sum(max(pos.get(k, 0), neg.get(k, 0)) for k in keys)
        total = (N - 1) * (N - 2)
        ceil_ = Fraction(right, total)
        want = Fraction(1, 2) + Fraction(c * (M - 1) * (M - 2),
                                         2 * (N - 1) * (N - 2))
        bad += ceil_ != want
        bad_det += any(pos.get(k, 0) == 0 or neg.get(k, 0) == 0
                       for k in keys)
        is_dead = ceil_ == Fraction(1, 2)
        dead += is_dead
        bad_dead += is_dead != (M == 2)
        ent = sum((pos.get(k, 0) + neg.get(k, 0))
                  * H2(Fraction(pos.get(k, 0),
                                pos.get(k, 0) + neg.get(k, 0)))
                  for k in keys) / total
        mixed = (M - 1) * (M - 2) * c * c
        want_log = (mixed * H2(Fraction(c + 1, 2 * c))
                    + (total - mixed) * log(2)) / total
        bad_log += abs(ent - want_log) > TOL
        ach = sum(pos.get(k, 0) if k[0] < k[1] else
                  neg.get(k, 0) if k[0] > k[1] else
                  max(pos.get(k, 0), neg.get(k, 0)) for k in keys)
        bad_ach += ach != right
    check("orientation ceiling 1/2 + c(M-1)(M-2)/(2(N-1)(N-2))", bad == 0,
          f"{len(fam)} cells")
    check("no fiber's posterior reaches 0 or 1", bad_det == 0)
    check("dead iff M = 2", bad_dead == 0, f"{dead} dead")
    check("orientation log-loss", bad_log == 0)
    check("comparing the two CRT-combined differences attains it",
          bad_ach == 0)
    # the full-triple control: raw evidence (x, y, z) mod M
    N = 30
    bad = 0
    for M in (2, 3, 5, 6, 10, 15):
        pos, neg = {}, {}
        for x in range(N):
            for y in range(N):
                for z in range(N):
                    if x == y or y == z or x == z:
                        continue
                    key = (x % M, y % M, z % M)
                    d = pos if (y - x) % N < (z - x) % N else neg
                    d[key] = d.get(key, 0) + 1
        keys = set(pos) | set(neg)
        right = sum(max(pos.get(k, 0), neg.get(k, 0)) for k in keys)
        c = N // M
        want = Fraction(1, 2) + Fraction(c * (M - 1) * (M - 2),
                                         2 * (N - 1) * (N - 2))
        bad += Fraction(right, N * (N - 1) * (N - 2)) != want
    check("full triples at N = 30 give the difference-pair ceiling",
          bad == 0)
    lone_bad = 0
    for N in {N for N, _, _ in fam}:
        ps = [p for p in PRIMES if N % p == 0]
        vals = [Fraction(1, 2) + Fraction((N // p) * (p - 1) * (p - 2),
                                          2 * (N - 1) * (N - 2))
                for p in ps]
        lone_bad += (ps[0] == 2 and vals[0] != Fraction(1, 2)) or \
            any(u >= v for u, v in zip(vals, vals[1:]))
    check("a lone channel is worth more the larger its prime, 2 nothing",
          lone_bad == 0)
    N = 210
    joint = Fraction(1, 2) + Fraction(14 * 14 * 13, 2 * 209 * 208)
    single = Fraction(1, 2) + Fraction(42 * 4 * 3, 2 * 209 * 208)
    check("N = 210 read at {3, 5}: 885/1672 against 5497/10868",
          (joint, single) == (Fraction(885, 1672), Fraction(5497, 10868)))
    bad = bad_floor = bad_log = 0
    for N, ps, S in fam:
        M = prod(S)
        c = N // M
        lt, gt = {}, {}
        for x in range(N):
            for y in range(N):
                if x == y:
                    continue
                key = (x % M, y % M)
                d = lt if x < y else gt
                d[key] = d.get(key, 0) + 1
        keys = set(lt) | set(gt)
        total = N * (N - 1)
        right = sum(max(lt.get(k, 0), gt.get(k, 0)) for k in keys)
        ach = sum(lt.get(k, 0) if k[0] < k[1] else gt.get(k, 0)
                  if k[0] > k[1] else lt.get(k, 0) for k in keys)
        want = Fraction(1, 2) + Fraction(M - 1, 2 * (N - 1))
        bad += Fraction(right, total) != want or ach != right
        bad_floor += sum(lt.values()) * 2 != total
        ent = sum((lt.get(k, 0) + gt.get(k, 0))
                  * H2(Fraction(lt.get(k, 0), lt.get(k, 0) + gt.get(k, 0)))
                  for k in keys) / total
        want_log = (M * (M - 1) * c * c * H2(Fraction(c + 1, 2 * c))
                    + M * c * (c - 1) * log(2)) / total
        bad_log += abs(ent - want_log) > TOL or ent >= log(2) - TOL
    check("comparison ceiling 1/2 + (M-1)/(2(N-1)), attained by comparing "
          "the residues", bad == 0, f"{len(fam)} cells")
    check("comparison floor exactly 1/2, so no cell is dead",
          bad_floor == 0)
    check("comparison log-loss, below log 2 everywhere", bad_log == 0)


# ------------------------------------------------------------ the tilt

def weights(N, theta):
    u, v = theta.numerator, theta.denominator
    return [u ** x * v ** (N - 1 - x) for x in range(N)]


def lean(q, J, c):
    """The sign of Pb(J) - 1/2 at q = theta^M, exact."""
    d = Fraction(2 * J - c) if q == 1 else         2 * (1 - q ** J) / (1 - q ** c) - 1
    return (d > 0) - (d < 0)


def tilt_ceilings(N, M, theta):
    """(ceiling, floor, seam) at every t = 1..N-1, exact."""
    w = weights(N, theta)
    tot = [sum(w[r + j * M] for j in range(N // M)) for r in range(M)]
    W = sum(tot)
    below = [0] * M
    Wb = 0
    right = sum(tot)
    out = []
    for t in range(1, N):
        r = (t - 1) % M
        right -= max(below[r], tot[r] - below[r])
        below[r] += w[t - 1]
        right += max(below[r], tot[r] - below[r])
        Wb += w[t - 1]
        core = all(below[i] * W == tot[i] * Wb for i in range(M))
        out.append((Fraction(right, W), Fraction(max(Wb, W - Wb), W), core))
    return out


def section_tilt():
    section("THE TILT: the threshold-range law")
    fam = cells(105)
    bad_core = bad_range = bad_refl = 0
    even_alive = {th: [0, 0] for th in THETAS}
    sweeps = 0
    for N, ps, S in fam:
        M = prod(S)
        c = N // M
        for theta in THETAS:
            sweeps += 1
            q = theta ** M
            rows = tilt_ceilings(N, M, theta)
            live = [t for t, (ce, fl, _) in enumerate(rows, 1) if ce > fl]
            bad_core += sum(core != (t % M == 0)
                            for t, (_, _, core) in enumerate(rows, 1))
            Js = [J for J in range(c)
                  if lean(q, J, c) < 0 < lean(q, J + 1, c)]
            want = [J * M + s for J in Js for s in range(1, M)]
            bad_range += live != want
            if theta == 1:
                bad_range += (len(live) == M - 1) != (c % 2 == 1)
            elif len(live) != M - 1:
                bad_range += 1
            if c % 2 == 0:
                even_alive[theta][0] += bool(live)
                even_alive[theta][1] += 1
            back = tilt_ceilings(N, M, 1 / theta)
            bad_refl += any(rows[t - 1][0] != back[N - t - 1][0]
                            for t in range(1, N))
    print(f"  {len(fam)} cells x {len(THETAS)} tilts, {sweeps} sweeps")
    check("posterior = prior iff M | t, at every tilt", bad_core == 0)
    check("the live set is one range of M - 1 at the J the exact "
          "test names; at theta = 1 empty iff c even", bad_range == 0)
    print("  even-c cells alive, by theta: " + ", ".join(
        f"{th}: {a}/{n}" for th, (a, n) in even_alive.items()))
    check("every even-c cell alive at every theta != 1, none at 1",
          all((a == n) if th != 1 else a == 0
              for th, (a, n) in even_alive.items()))
    check("reflection: ceiling(theta, t) = ceiling(1/theta, N - t)",
          bad_refl == 0)
    # hand control at theta = 1/2, N = 6, M = 3
    rows = tilt_ceilings(6, 3, Fraction(1, 2))
    check("hand cell theta = 1/2, N = 6, M = 3: t = 3 dead at 8/9, t = 2 "
          "19/21 against 16/21",
          rows[2][:2] == (Fraction(8, 9), Fraction(8, 9))
          and rows[1][:2] == (Fraction(19, 21), Fraction(16, 21)))


def f_res(q, J, c):
    return q ** c - 2 * q ** J + 1


def bisect(fn, lo, hi, iters=200):
    flo = fn(lo)
    for _ in range(iters):
        mid = (lo + hi) / 2
        fm = fn(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def resonance_root(J, c):
    """The positive root of q^c - 2q^J + 1 other than 1 (2J != c)."""
    fn = lambda q: f_res(q, J, c)
    if 2 * J < c:
        return bisect(fn, 1e-12, 1 - 1e-12)
    hi = 2.0
    while fn(hi) < 0:
        hi *= 2
    return bisect(fn, 1 + 1e-12, hi)


def section_resonance():
    section("THE RESONANCE CRITERION")
    hits = tried = 0
    for u in range(1, 41):
        for v in range(1, 41):
            if u == v or gcd(u, v) != 1:
                continue
            for c in range(2, 13):
                for J in range(1, c):
                    tried += 1
                    hits += u ** c + v ** c == 2 * u ** J * v ** (c - J)
    check("no rational q != 1 is a root", hits == 0,
          f"{tried} (u, v, J, c) tuples")
    bad_count = bad_side = bad_refl = 0
    pairs = doubles = 0
    grid = [i / 400 for i in range(1, 3201)]
    for c in range(2, 13):
        for J in range(1, c):
            if 2 * J == c:
                doubles += 1
                changes = sum((f_res(a, J, c) > 0) != (f_res(b, J, c) > 0)
                              for a, b in zip(grid, grid[1:])
                              if abs(a - 1) > 1e-9 and abs(b - 1) > 1e-9)
                bad_count += changes != 0 or f_res(1, J, c) != 0
                continue
            pairs += 1
            root = resonance_root(J, c)
            bad_side += (root < 1) != (2 * J < c)
            keep = [x for x in grid
                    if abs(x - 1) > 1e-3 and abs(x - root) > 1e-3]
            changes = sum((f_res(a, J, c) > 0) != (f_res(b, J, c) > 0)
                          for a, b in zip(keep, keep[1:]))
            # the kept grid straddles both roots, 1 and the other
            bad_count += changes != 2
            bad_count += abs(f_res(root, J, c)) > 1e-9
            other = resonance_root(c - J, c)
            bad_refl += abs(root * other - 1) > 1e-9
    check("one root other than 1 per 2J != c pair, on the side 2J - c "
          "names", bad_count == 0 and bad_side == 0,
          f"{pairs} pairs, {doubles} with 2J = c")
    check("q -> 1/q exchanges J and c - J", bad_refl == 0)
    phi = (5 ** 0.5 - 1) / 2
    Qstar = log((1 + phi ** 3) / 2) / log(phi)
    check("golden control: q^3 - 2q + 1 = (q - 1)(q^2 + q - 1), "
          "Q* = 1 there",
          all(f_res(x, 1, 3) == (x - 1) * (x * x + x - 1)
              for x in range(-5, 6)) and abs(Qstar - 1) < TOL)


# ----------------------------------------------------------- magnitude

def blocks(M, c, k, r):
    """lo[0..k] of the class blocks at atom r, by definition."""
    N = c * M
    lo = [0] * (k + 1)
    counts = [0] * k
    for j in range(c):
        counts[k * (r + j * M) // N] += 1
    for y in range(k):
        lo[y + 1] = lo[y] + counts[y]
    return lo


def block_formula(M, c, k, r):
    a, b = divmod(c, k)
    f = Fraction(r, M)
    return [a + ceil((y + 1) * Fraction(b, k) - f)
            - ceil(y * Fraction(b, k) - f) for y in range(k)]


def g_poly(q, a, L):
    return 1 - q ** a - q ** L + q ** (L + a + 1)


def g_root(a, L):
    return bisect(lambda q: g_poly(q, a, L), 1e-12, 1 - 1e-12)


def magnitude_exact(M, c, k, theta):
    """(ceiling numerator, floor numerator, argmax sets) at an exact tilt."""
    N = M * c
    w = weights(N, theta)
    right = 0
    tops = []
    for r in range(M):
        mass = [0] * k
        for j in range(c):
            x = r + j * M
            mass[k * x // N] += w[x]
        best = max(mass)
        right += best
        tops.append({y for y in range(k) if mass[y] == best})
    cls = [0] * k
    for x in range(N):
        cls[k * x // N] += w[x]
    return right, max(cls), tops


def arc(M, c, k):
    """(q_lo, q_up) of the live arc, from the per-atom roots."""
    a, b = divmod(c, k)
    lows, ups = [], []
    for r in range(M):
        lo = blocks(M, c, k, r)
        n = [lo[y + 1] - lo[y] for y in range(k)]
        heavy = [y for y in range(k) if n[y] == a + 1]
        y1, ylast = heavy[0], heavy[-1]
        if y1 >= 1:
            lows.append(0.0 if a == 0 else g_root(a, a * y1))
        if n[k - 1] == a:
            ups.append(float("inf") if a == 0
                       else 1 / g_root(a, a * (k - 1 - ylast)))
    q_lo = min(lows) if lows else 1.0
    q_up = max(ups) if ups else 1.0
    return q_lo, q_up


def overrules(M, c, k, q):
    """The exact prediction of (H): some atom's best class is not the
    floor's guess, read off g's sign (q < 1: lower atoms; q > 1: atoms
    with a light top class, at 1/q)."""
    a, b = divmod(c, k)
    for r in range(M):
        lo = blocks(M, c, k, r)
        n = [lo[y + 1] - lo[y] for y in range(k)]
        heavy = [y for y in range(k) if n[y] == a + 1]
        if q < 1 and heavy[0] >= 1:
            if a == 0 or g_poly(q, a, a * heavy[0]) < 0:
                return True
        if q > 1 and n[k - 1] == a:
            if a == 0 or g_poly(1 / q, a, a * (k - 1 - heavy[-1])) < 0:
                return True
    return False


def rational_near(x, den=10 ** 6):
    return Fraction(round(x * den), den)


def section_magnitude():
    section("THE k-ARY PARENT: the arc replaces the resonance points")
    one = magnitude_exact(15, 7, 2, Fraction(1))
    zero = magnitude_exact(2, 3, 5, Fraction(1))
    check("controls: M = 15, c = 7, k = 2 gives 4/7; M = 2, c = 3, k = 5 "
          "dead at 1/3",
          Fraction(one[0], 105) == Fraction(4, 7)
          and Fraction(zero[0], 6) == Fraction(zero[1], 6)
          == Fraction(1, 3))
    grid = [(M, c, k) for M in (2, 3, 6, 15, 35) for c in range(2, 13)
            for k in range(2, 10) if k <= M * c]
    bad_blocks = bad_ceil = bad_dead = bad_ach = 0
    dead = sat = 0
    for M, c, k in grid:
        a, b = divmod(c, k)
        N = M * c
        for r in range(M):
            lo = blocks(M, c, k, r)
            n = [lo[y + 1] - lo[y] for y in range(k)]
            heavy = {y for y in range(k) if n[y] == a + 1}
            want_heavy = {k * (m * M + r) // (b * M) for m in range(b)}
            bad_blocks += n != block_formula(M, c, k, r) \
                or set(n) - {a, a + 1} != set() \
                or len(heavy) != b or (b and heavy != want_heavy)
            if b:
                bad_ach += (k * r) // (b * M) not in heavy
        right, fl, _ = magnitude_exact(M, c, k, Fraction(1))
        bad_ceil += Fraction(right, N) != Fraction(-(-c // k), c) \
            or Fraction(fl, N) != Fraction(-(-N // k), N)
        is_dead = right == fl
        saturated = b > 0 and M * (k - b) < k
        dead += is_dead
        sat += saturated
        bad_dead += is_dead != (b == 0 or saturated) \
            or (M * (-(-c // k)) == -(-(M * c) // k)) != is_dead
    check("blocks of lengths a and a + 1, exactly b heavy, at the stated "
          "heavy set", bad_blocks == 0, f"{len(grid)} cells")
    check("uniform ceiling ceil(c/k)/c, floor ceil(N/k)/N", bad_ceil == 0)
    check("dead iff k | c or M(k - b) < k", bad_dead == 0,
          f"{dead} dead, {sat} saturated")
    check("the first heavy class floor(kr/(bM)) is heavy at every atom",
          bad_ach == 0)
    tgrid = [(M, c, k) for M in (2, 3, 6, 15) for c in range(2, 11)
             for k in range(2, 7) if k <= M * c]
    tilts = [Fraction(1, 5), Fraction(1, 2), Fraction(4, 5),
             Fraction(9, 10), Fraction(199, 200), Fraction(201, 200),
             Fraction(10, 9), Fraction(2), Fraction(5)]
    bad_four = 0
    for M, c, k in tgrid:
        a, b = divmod(c, k)
        for theta in tilts:
            _, _, tops = magnitude_exact(M, c, k, theta)
            for r in range(M):
                lo = blocks(M, c, k, r)
                n = [lo[y + 1] - lo[y] for y in range(k)]
                heavy = [y for y in range(k) if n[y] == a + 1] or [0]
                allowed = {0, heavy[0]} if theta < 1 else \
                    {heavy[-1], k - 1}
                bad_four += not tops[r] <= allowed
    check("off uniform the best class is 0 or the first heavy below, the "
          "last heavy or k - 1 above", bad_four == 0,
          f"{len(tgrid)} cells x {len(tilts)} tilts")
    bad_arc = bad_g = tested = 0
    bad_band = banded = 0
    for M, c, k in tgrid:
        a, b = divmod(c, k)
        if b == 0:
            for theta in tilts:
                right, fl, _ = magnitude_exact(M, c, k, theta)
                bad_arc += right != fl
                tested += 1
            continue
        q_lo, q_up = arc(M, c, k)
        qs = []
        if 0 < q_lo < 1:
            qs += [q_lo * 0.95, q_lo + (1 - q_lo) * 0.05]
        if 1 < q_up < float("inf"):
            qs += [q_up * 1.05, q_up - (q_up - 1) * 0.05]
        probes = list(tilts) + [rational_near(x ** (1 / M)) for x in qs]
        for th in probes:
            if th == 1:
                continue
            q = float(th) ** M
            right, fl, _ = magnitude_exact(M, c, k, th)
            alive = right > fl
            bad_arc += alive != (q_lo < q < q_up)
            bad_g += alive != overrules(M, c, k, th ** M)
            tested += 1
        if M > k and a >= 1:
            banded += 1
            rho = resonance_root(a, 2 * a + 1)
            bad_band += abs(q_lo - rho) > 1e-9 or abs(q_up - 1 / rho) > 1e-9
    check("the cell is alive exactly where some atom's g < 0",
          bad_g == 0)
    check("alive exactly on one open arc (q_lo, q_up), dead off it",
          bad_arc == 0, f"{tested} exact probes")
    check("at M > k, a >= 1 the arc is (rho_a, 1/rho_a)", bad_band == 0,
          f"{banded} cells")
    rhos = [resonance_root(a, 2 * a + 1) for a in range(1, 7)]
    print("  rho_a, a = 1..6: " + ", ".join(f"{x:.6f}" for x in rhos))
    check("rho_1 is the reciprocal golden ratio",
          abs(rhos[0] - (5 ** 0.5 - 1) / 2) < TOL)
    alive = magnitude_exact(15, 3, 2, Fraction(199, 200))
    dead_ = magnitude_exact(15, 3, 2, Fraction(24, 25))
    check("sign bit M = 15, c = 3: alive at theta = 199/200, dead at 24/25",
          alive[0] > alive[1] and dead_[0] == dead_[1],
          f"q = {float(Fraction(199, 200)) ** 15:.3f} and "
          f"{float(Fraction(24, 25)) ** 15:.3f} against rho_1 = "
          f"{rhos[0]:.3f}")


def section_controls():
    section("CONTROLS")
    check("sign N = 6: 2/3 at M = 2, 1/2 at M = 3",
          sign_brute(6, 2)[0] == Fraction(2, 3)
          and sign_brute(6, 3)[0] == Fraction(1, 2))
    below = [sum(1 for j in range(5) if r + 6 * j < 13) for r in range(6)]
    got = Fraction(sum(max(x, 5 - x) for x in below), 30)
    check("threshold N = 30, M = 6, t = 13: 3/5", got == Fraction(3, 5))
    pos, neg = orientation_counts(6, 3)
    got = Fraction(sum(max(pos.get(k, 0), neg.get(k, 0))
                       for k in set(pos) | set(neg)), 20)
    check("orientation N = 6, M = 3: 3/5", got == Fraction(3, 5))
    for M, want in ((3, Fraction(7, 10)), (2, Fraction(3, 5))):
        lt, gt = {}, {}
        for x in range(6):
            for y in range(6):
                if x != y:
                    d = lt if x < y else gt
                    d[(x % M, y % M)] = d.get((x % M, y % M), 0) + 1
        got = Fraction(sum(max(lt.get(k, 0), gt.get(k, 0))
                           for k in set(lt) | set(gt)), 30)
        check(f"comparison N = 6, M = {M}: {want}", got == want)


def main():
    t0 = time.time()
    section_controls()
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        return 1
    section_sign()
    section_threshold()
    section_orientation()
    section_tilt()
    section_resonance()
    section_magnitude()
    print()
    n, ok = len(CHECKS), sum(CHECKS)
    print(f"{ok} of {n} checks pass, {time.time() - t0:.1f} s")
    return 0 if ok == n else 1


if __name__ == "__main__":
    sys.exit(main())
