"""explore_eval_ceiling.py -- THE SIGN-READOUT CEILING (an evaluation
that knows its own optimum, second instance; sibling of
explore_induction_ceiling.py).

THE QUESTION. explore_induction_ceiling.py exhibited one benchmark
whose Bayes-optimal score is exactly computable and exactly achieved:
growth-world induction knows its own ceiling. Is that a DESIGNABLE
property of an evaluation, or an accident of that corpus? Design a
second instance from entirely different material -- the archimedean
wall: a uniform element of a squarefree ring Z/N is read through a
proper subset of its residue channels (modulus M | N), and the task
is to guess the sign bit [x >= N/2]. The known fiber is an arithmetic
progression of c = N/M elements, so the posterior is closed-form and
the ceiling should be provable, nontrivial, and cheaply achieved.
An EVAL here is a triple (task family with prior, evidence channel,
score); its CEILING is the Bayes-optimal expected score; NONTRIVIAL
means strictly better than the no-evidence floor (the PRIOR's best
score, evidence severed -- for the sign bit this floor is
ceil(N/2)/N, not a rhetorical 1/2) and strictly worse than perfect;
TIGHT means a computable achiever with stated cost matches it (the
Bayes posterior "achieving" the Bayes optimum is definitional and
claims nothing; the content is exact computability plus the price of
doing less).

DESIGN. Prior: x uniform on Z/N, N a product of >= 2 distinct primes
from {2, 3, 5, 7, 11, 13} (all 57 such N, largest 30030). Evidence:
r = x mod M for every proper divisor M with 1 < M < N (every proper
nonempty channel subset). Task: the sign bit b(x) = [2x >= N].
Scores: 0-1 accuracy, then log-loss. All probabilities exact
(Fraction); entropies in nats, tolerance 1e-12.

HAND DERIVATION (fixed before the engine; index convention: x in
{0..N-1}, fiber {r + jM : j = 0..c-1}, below-count = #{j : 2(r+jM)
< N} = ceil(c/2 - r/M)). If c is EVEN the count is c/2 for every r:
posterior = prior on every fiber, the evidence carries zero sign
information. If c is ODD the count is (c+1)/2 when r < M/2 and
(c-1)/2 otherwise, so the Bayes rule thresholds r at M/2 and scores
(c+1)/(2c) on every fiber. Since N is squarefree, c is even exactly
when 2 | N and 2 does not divide M: the dead cells are exactly the
cells where channel 2 is among the unknowns -- the sharp form of the
sign-hiding fact (the walls corpus: fiber bias at most half an
element, exactly zero without channel 2).

PREDICTIONS (fixed before the run):
  PR1 (the parity law): exact Bayes accuracy = (c+1)/(2c) if c odd,
      1/2 if c even, at every scanned (N, M) -- no third behavior.
  PR2 (the floor cells): accuracy equals the no-evidence floor
      ceil(N/2)/N exactly on the cells with 2 | N and 2 not | M, and
      strictly exceeds it on every other cell; at odd N every proper
      subset is strictly off the floor (c is always odd and
      (c+1)/(2c) > (N+1)/(2N) iff c < N iff M > 1).
  PR3 (the second score): brute conditional entropy H(b | r) =
      H2((c+1)/(2c)) nats for c odd, log 2 for c even, within 1e-12.
  PR4 (tight, with cost): the plug-in achiever -- CRT-reconstruct
      r mod M from the |S| residues, guess below iff 2r < M -- meets
      the ceiling exactly on every cell it is run on. Cost: one CRT
      reconstruction (O(|S|) modular ops) plus one comparison.
  PR5 (the price of doing less): the best single-channel solver
      (threshold one residue x mod p) obeys the SAME law at M' = p,
      c' = N/p: accuracy 1/2 + [c' odd]/(2c'). At even N a lone odd
      channel has c' even and sits at the floor -- channel 2 is the
      only single channel worth anything (1/2 + 1/N) -- while at odd
      N every single channel earns 1/2 + p/(2N). The plug-in price
      of dropping to one channel is the difference of the two
      formulas, zero only where both sit at the floor.

KILL (observable): any scanned cell printing an accuracy or entropy
off its formula value. What such a print would mean is weighed after
the run, not encoded here.

FINDINGS (tier-labeled; run record below; the scan is exhaustive over
the stated family -- 57 squarefree rings from the first six primes,
602 (N, subset) cells -- and exact in probability).

1. THE PARITY LAW (rule, proved + exhaustive at all 602 cells;
   verified E1). The Bayes 0-1 ceiling for the sign bit read through
   a proper channel subset is (c+1)/(2c) when the unknown cofactor
   c = N/M is odd and exactly 1/2 when c is even -- no third
   behavior. The hand proof is three lines (the known fiber is an
   arithmetic progression; the below-count is ceil(c/2 - r/M)); the
   engine confirms every cell.

2. THE FLOOR CELLS ARE THE 2-UNKNOWN CELLS (rule, proved +
   exhaustive; verified E2). Ceiling = the no-evidence floor
   ceil(N/2)/N on exactly the 211 cells where 2 | N and channel 2 is
   among the unknowns; the other 391 cells are strictly interior
   (floor < ceiling < 1). At odd N there are NO floor cells: every
   proper subset lifts strictly off the floor. Designability's dial
   at this family is a single arithmetic bit -- whether channel 2 is
   read.

3. THE LOG-LOSS TWIN (rule; verified E3, tol 1e-12). The second
   score's ceiling is the same dichotomy in entropy dress:
   H(b | r) = H2((c+1)/(2c)) nats for c odd, log 2 for c even.

4. TIGHT, WITH COST (rule + computed; verified E4). The plug-in
   solver -- CRT-reconstruct r mod M (O(|S|) modular ops), one
   comparison 2r < M -- meets the ceiling EXACTLY on all 362 cells
   with N <= 2310 it was run on. The eval knows its optimum and a
   solver of stated constant cost per query attains it; nothing
   about the achiever is definitional.

5. THE PRICE OF DOING LESS IS SELF-SIMILAR (rule; verified E5). A
   single-channel solver obeys the SAME law one level coarser
   (M' = p, c' = N/p): at even N every lone odd channel sits at the
   floor and only channel 2 earns (1/2 + 1/N); at odd N every
   channel earns 1/2 + p/(2N). Worked example N = 2310,
   S = {2, 3, 5}: joint ceiling 39/77 = 1/2 + 1/154, best single
   channel 578/1155, price 1/165. The plug-in price is a difference
   of two instances of the parity law -- the eval family prices its
   own degradations.

THE HEADLINE. "Knows its own ceiling" is DESIGNABLE, second instance
confirmed from unrelated material: the archimedean wall yields an
eval family every cell of which ships a provable, closed-form Bayes
ceiling; an exact one-bit dial (is channel 2 read?) separates dead
cells (posterior = prior) from interior cells; the interior value
1/2 + 1/(2c) decays to the floor as the unknown complement grows;
a constant-cost achiever is exactly tight; and the family prices its
own cheaper solvers by its own law. Where the growth instance bought
its provable ceiling with finite path ENUMERABILITY, this one buys
it with CLOSED-FORM FIBERS -- two mechanisms, one designable object.

HONEST LIMITS. (a) The scan is the first six primes; the parity law
itself is proved for every squarefree N and proper divisor M, so the
scope limit touches only the exhaustive confirmations. (b) 0-1 and
log scores only; other proper scores untested. (c) The achiever ran
exhaustively at N <= 2310 and by formula elsewhere. (d) One prior
(uniform = the ring's Haar measure); skewed priors move the floor
and are unexplored here -- since explored
(explore_ceiling_dials.py): under a geometric tilt this
file's even-c deadness is a RESONANCE of the uniform point that any
tilt lifts, and the sign bit specifically is maximally
prior-fragile (dead at every tilt off uniform, the floor cells here
being the s = 0 / structural core).

RUN RECORD (this file, python explore_eval_ceiling.py, ~0.6 s):
  S0 controls: 2/3, 1/2, 3/5, boundary fiber count 2 -- pass.
  cell family: 602 (N, subset) cells over 57 rings.
  E1 parity law on all 602 cells -- pass.
  E2 floor cells: 211 at the floor, all exactly the 2-unknown
     cells; 391 strictly interior -- pass.
  E3 log-loss ceiling matches on all 602 cells (tol 1e-12) -- pass.
  E4 tight: ceiling met exactly on all 362 cells with N <= 2310 --
     pass.
  E5 price: worked example N = 2310, S = (2, 3, 5): joint 39/77,
     best single 578/1155, price 1/165 -- pass.
  all asserts green.

RUN: python explore_eval_ceiling.py  (exhaustive, exact; the S0
controls are hand-computed cases asserted before any scan is read).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from fractions import Fraction
from itertools import combinations
from math import log

PRIMES = (2, 3, 5, 7, 11, 13)


def product(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def brute_bayes(N, M):
    """Exact Bayes 0-1 accuracy for guessing [2x >= N] from x mod M."""
    c = N // M
    correct = 0
    for r in range(M):
        below = sum(1 for j in range(c) if 2 * (r + j * M) < N)
        correct += max(below, c - below)
    return Fraction(correct, N)


def formula(N, M):
    c = N // M
    return Fraction(c + 1, 2 * c) if c % 2 == 1 else Fraction(1, 2)


def floor_score(N):
    """The no-evidence floor: the prior's best guess, evidence severed."""
    return Fraction((N + 1) // 2, N)


def h2(p):
    """Binary entropy in nats; p a Fraction or float."""
    p = float(p)
    if p in (0.0, 1.0):
        return 0.0
    return -p * log(p) - (1 - p) * log(1 - p)


def brute_cond_entropy(N, M):
    """Exact-in-probability conditional entropy H(b | r) in nats."""
    c = N // M
    total = 0.0
    for r in range(M):
        below = sum(1 for j in range(c) if 2 * (r + j * M) < N)
        total += h2(Fraction(below, c)) / M
    return total


def crt_reconstruct(residues, moduli):
    """CRT: the unique r mod prod(moduli) with r = residues[i] mod
    moduli[i]. O(len) modular ops."""
    M = product(moduli)
    r = 0
    for res, p in zip(residues, moduli):
        w = M // p
        r = (r + res * w * pow(w, -1, p)) % M
    return r


def achiever_accuracy(N, subset):
    """Run the plug-in solver on every x: read the subset residues,
    CRT-reconstruct r, guess below iff 2r < M. Returns exact accuracy."""
    M = product(subset)
    correct = 0
    for x in range(N):
        residues = [x % p for p in subset]
        r = crt_reconstruct(residues, subset)
        assert r == x % M
        guess_below = 2 * r < M
        correct += guess_below == (2 * x < N)
    return Fraction(correct, N)


def main():
    # ---- S0: positive controls (hand-computed before the engine) ----
    assert brute_bayes(6, 2) == Fraction(2, 3)
    assert brute_bayes(6, 3) == Fraction(1, 2)
    assert brute_bayes(30, 6) == Fraction(3, 5)
    below_r3 = sum(1 for j in range(5) if 2 * (3 + j * 6) < 30)
    assert below_r3 == 2
    print("S0 controls: 2/3, 1/2, 3/5, boundary fiber count 2 -- pass")

    # ---- the cell family: all N, all proper channel subsets ----
    cells = []
    for size in range(2, len(PRIMES) + 1):
        for ps in combinations(PRIMES, size):
            N = product(ps)
            for ssize in range(1, size):
                for sub in combinations(ps, ssize):
                    cells.append((N, ps, sub))
    print(f"cell family: {len(cells)} (N, subset) cells over "
          f"{sum(1 for s in range(2, 7) for _ in combinations(PRIMES, s))} rings")

    # ---- E1: the parity law + E2: the floor classification ----
    n_floor = n_interior = 0
    for N, ps, sub in cells:
        M = product(sub)
        c = N // M
        acc = brute_bayes(N, M)
        assert acc == formula(N, M), (N, M, acc)
        at_floor = acc == floor_score(N)
        two_unknown = (2 in ps) and (2 not in sub)
        assert at_floor == two_unknown, (N, M)
        if at_floor:
            n_floor += 1
        else:
            assert acc > floor_score(N) and acc < 1
            n_interior += 1
    print(f"E1 parity law: accuracy = (c+1)/2c [c odd] / 1/2 [c even] "
          f"on all {len(cells)} cells -- pass")
    print(f"E2 floor cells: {n_floor} at the floor, all exactly the "
          f"2-unknown cells; {n_interior} strictly interior -- pass")

    # ---- E3: log-loss, the second score ----
    for N, ps, sub in cells:
        M = product(sub)
        c = N // M
        want = h2(Fraction(c + 1, 2 * c)) if c % 2 == 1 else log(2)
        got = brute_cond_entropy(N, M)
        assert abs(got - want) < 1e-12, (N, M, got, want)
    print(f"E3 log-loss ceiling: H(b | r) matches the closed form on "
          f"all {len(cells)} cells (tol 1e-12) -- pass")

    # ---- E4: the achiever meets the ceiling (run on N <= 2310) ----
    n_run = 0
    for N, ps, sub in cells:
        if N > 2310:
            continue
        acc = achiever_accuracy(N, sub)
        assert acc == formula(N, product(sub)), (N, sub)
        n_run += 1
    print(f"E4 tight: the CRT-threshold solver meets the ceiling "
          f"exactly on all {n_run} cells with N <= 2310 -- pass")

    # ---- E5: the price of doing less (single-channel plug-in) ----
    worked_example = None
    for N, ps, sub in cells:
        if len(sub) < 2:
            continue
        M = product(sub)
        joint = formula(N, M)
        singles = [formula(N, p) for p in sub]
        best_single = max(singles)
        assert best_single <= joint, (N, sub)
        if 2 in ps:
            for p, s in zip(sub, singles):
                if p != 2:
                    assert s == Fraction(1, 2), (N, p)
                else:
                    assert s == Fraction(1, 2) + Fraction(1, N)
        if worked_example is None and N == 2310 and sub == (2, 3, 5):
            worked_example = (N, sub, joint, best_single)
    N, sub, joint, best = worked_example
    print(f"E5 price: single channels obey the same law at M' = p; at "
          f"even N only channel 2 lifts off the floor -- pass")
    print(f"   worked example N = {N}, S = {sub}: joint ceiling "
          f"{joint} = 1/2 + {joint - Fraction(1, 2)}, best single "
          f"channel {best}, price {joint - best}")

    print("all asserts green")


if __name__ == "__main__":
    main()
