"""The golden POSITIONAL control: the trailing base-phi window on Z
is rigid — the fourth window's positionality axis isolated.

THE QUESTION
------------
The Zeckendorf window varied ONE axis against b-adic trailing: the
cells stopped being cosets while the arithmetic stayed golden. The
control that varies the OTHER axis — positional cells, same golden
arithmetic — is the base-phi (Bergman) expansion of the integers:
n = sum d_k phi^k over k in Z, digits {0,1}, no adjacent 1s, finite
(the golden ratio has the finiteness property). What window do
positional golden cells make — and what completion, since the
continuity refinement (explore_zeckendorf_window.py, the two gates)
predicts the gate from the completion's structure?

THE WINDOW'S OWN VOCABULARY (fixed before any engine). There is NO
bottom position: expansions descend to -m(n) with m(n) growing like
log_phi n, so trailing depth cannot count digits up from a floor as
b-adic and Zeckendorf trailing both do. The trailing cell at CUTOFF c
is agreement on ALL positions k <= c; cells refine as c rises.

THE DERIVATION (hand, before the engine; the rig checks it). Two
integers in one cutoff-c cell differ only at positions > c, so
n - n' = sum_{k>c} (d_k - e_k) phi^k, and applying the conjugation
phi -> psi = -1/phi (which fixes Z) gives the same sum over psi.
With coefficients in {-1, 0, 1}:
|n - n'| <= sum_{k>=c+1} |psi|^k = |psi|^{c+1}/(1-|psi|) = phi^{1-c}.
  c >= 2: bound < 1, so n = n' — CELLS ARE SINGLETONS.
  c = 1: bound = 1, attained only by an infinite tail — singletons.
  c = 0: bound = phi, so difference 1 is possible and difference 2 is
  not: cells have size <= 2, members consecutive. The realized move:
  2 = phi + phi^{-2} and 3 = phi^2 + phi^{-2} share every digit at
  k <= 0, difference phi^2 - phi = 1 — the polynomial x^2 - x =
  (x^2 - x - 1) + 1 takes value 1 at BOTH roots, which is why one
  rewrite moves the integer by exactly 1 at the phi-place and the
  psi-place simultaneously.
  c = -P: diameter <= phi^{P+1} — every cell FINITE, size O(phi^P).
CONSEQUENCE: refining finite cells that reach singletons complete to
NOTHING NEW — the completion of Z at this window is Z itself,
discrete. Trivially a ring, every map continuous, no gate: the window
is RIGID, and the reading question is vacuous. The b-adic supply of
infinite trailing cells is the index of b^t Z — a NON-unit base;
at a unit base a positional trailing window has no index to spend,
and the Zeckendorf window buys its infinite cells (the Fibonacci
roof) by going non-positional. The continuity refinement's
trichotomy, each cell as its own window realizes it: ring
completion (base-b — all integer mult continuous), odometer
completion (Zeckendorf — units only), discrete completion (golden
positional — no window at all); general beyond these three windows
it is the conjecture the next storey tests.

PREDICTIONS, FIXED BEFORE THE RUN (as observables)
--------------------------------------------------
G1 (engine sanity) greedy base-phi terminates for every n < N with
   golden digits and exact reconstruction in Z[phi] coordinates.
G2 (rigidity) at cutoffs c = 1 and c = 2, every cell over n < N is a
   singleton.
G3 (the collision census) at cutoff 0, every cell has size <= 2 and
   every size-2 cell is a consecutive pair; (2,3) is the positive
   control. CANDIDATE characterization, tested rather than assumed:
   the pairs are exactly the n whose expansion has d_1 = 1, d_2 =
   d_3 = 0, with n+1 the same string rewritten phi^1 -> phi^2.
G4 (finiteness with rate) at cutoffs c = 0..-8, max cell size grows
   with successive-max ratio -> phi, and max cell diameter stays
   <= phi^{1-c}.
TRANSPLANT MARKS: G4's rate is imported from the conjugate bound in
the derivation, not from a measured neighbour; G3's characterization
is a guess past the derivation, marked as a test.

THE DESIGN. Exact arithmetic in Z[phi] as integer pairs (a, b) =
a + b*phi (phi^2 = phi + 1; conjugation psi = 1 - phi). Greedy
expansion by exact comparison (sign of a + b*phi via (2a+b) and
5b^2); no floats anywhere in the digit path. Exhaustive over
n < N = 5000.

RUN RECORD
----------
One run after a one-line engine fix caught by G1 itself (the
downward phi-power recurrence had its pair order swapped; 4998
guard failures, zero after). Instant, trivial memory. ALL CHECKS
GREEN.

FINDINGS (post-run)
-------------------
G1 zero failures: greedy terminates with golden digits and exact
   reconstruction for every n < 5000 — the finiteness property in
   range.
G2 CONFIRMED: cutoffs 1 and 2 give singleton cells only. The window
   is rigid exactly as the conjugate bound says.
G3 CONFIRMED in shape, REFUTED in the tested characterization: 1381
   multi-member cells, every one a consecutive pair, (2,3) present —
   but the pairs are NOT only the phi^1 -> phi^2 rewrites. First
   counterexample (6,7): 6 = phi^3 + phi + phi^{-4}, 7 = phi^4 +
   phi^{-4}, difference phi^4 - phi^3 - phi = 1 — the polynomial
   x^4 - x^3 - x = (x^2 + 1)(x^2 - x - 1) + 1 takes value 1 at
   both roots. The general collision move is any golden-realizable
   {-1,0,1} polynomial congruent to 1 mod x^2 - x - 1; the pair lows
   (2, 6, 9, 13, 17, 20, 24, 27, ...) step 3/4 quasi-periodically,
   mean step 1 + phi^2 (observation; not chased).
G4 CONFIRMED: max cell size ratios settle at 1.617 -> phi; max
   diameters sit tight under phi^{1-c} (75 vs 76.0 at c = -8), and
   at every cutoff the printed max size equals the printed max
   diameter + 1 — consistent with the extremal cells being full
   integer intervals, a per-cell shape the rig did not check
   (observation on the maxima only).
THE READING: the control lands as derived. The golden POSITIONAL
trailing window on Z is rigid — no infinite cells anywhere, cells
singleton from cutoff 1 up, completion = Z discrete, no gate
question. The positionality axis is isolated: at a unit base the
positional trailing window degenerates, and the Zeckendorf window's
infinite cells are bought by non-positionality alone. Trichotomy on
the completion, each cell as its own window realizes it: ring
(base-b), odometer (Zeckendorf), discrete (golden positional).
"""

import sys

N = 5000
GUARD_LOW = -80          # greedy failure flag if a remainder descends past this


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def sign(x):
    """Exact sign of a + b*phi."""
    a, b = x
    if a == 0 and b == 0:
        return 0
    t = 2 * a + b           # a + b*phi > 0  iff  t + b*sqrt5 > 0
    if b >= 0:
        if t >= 0:
            return 1
        return 1 if t * t < 5 * b * b else -1
    if t <= 0:
        return -1
    return 1 if t * t > 5 * b * b else -1


def phi_pow(k):
    """phi^k as (a, b), any integer k."""
    if k >= 0:
        x, y = (1, 0), (0, 1)       # phi^0, phi^1
        if k == 0:
            return x
        for _ in range(k - 1):
            x, y = y, add(x, y)
        return y
    x, y = (0, 1), (1, 0)           # phi^1, phi^0
    for _ in range(-k):
        x, y = y, sub(x, y)         # phi^{j-1} = phi^{j+1} - phi^j
    return y


def greedy_phi(n):
    """Canonical base-phi digits of n as a set of positions, or None
    on guard failure."""
    rem = (n, 0)
    if n == 0:
        return set()
    k = 1
    while sign(sub(rem, phi_pow(k + 1))) >= 0:
        k += 1
    while sign(sub(rem, phi_pow(k))) < 0:
        k -= 1
    pos = set()
    while sign(rem) > 0:
        if k < GUARD_LOW:
            return None
        if sign(sub(rem, phi_pow(k))) >= 0:
            rem = sub(rem, phi_pow(k))
            pos.add(k)
            k -= 2
        else:
            k -= 1
    return pos


def main():
    ok_all = True

    # G1 — engine sanity
    expansions = {}
    bad_term = bad_golden = bad_recon = 0
    for n in range(N):
        pos = greedy_phi(n)
        if pos is None:
            bad_term += 1
            continue
        if any(k + 1 in pos for k in pos):
            bad_golden += 1
        tot = (0, 0)
        for k in pos:
            tot = add(tot, phi_pow(k))
        if tot != (n, 0):
            bad_recon += 1
        expansions[n] = pos
    print("G1 sanity over n < %d: non-terminating %d, adjacency %d, "
          "reconstruction failures %d" % (N, bad_term, bad_golden, bad_recon))
    ok_all &= bad_term == bad_golden == bad_recon == 0

    def cells(cutoff):
        groups = {}
        for n, pos in expansions.items():
            key = tuple(sorted(k for k in pos if k <= cutoff))
            groups.setdefault(key, []).append(n)
        return groups

    # G2 — rigidity at c = 1, 2
    for c in (1, 2):
        mx = max(len(v) for v in cells(c).values())
        print("G2 cutoff %d: max cell size = %d (predicted 1)" % (c, mx))
        ok_all &= mx == 1

    # G3 — the collision census at cutoff 0
    g = cells(0)
    multi = sorted(v for v in g.values() if len(v) > 1)
    sizes = sorted(set(len(v) for v in multi))
    consec = all(len(v) == 2 and v[1] - v[0] == 1 for v in multi)
    print("G3 cutoff 0: %d multi-member cells, sizes %s, all consecutive "
          "pairs: %s" % (len(multi), sizes, consec))
    print("   first pairs: %s" % [tuple(v) for v in multi[:8]])
    ctrl = any(tuple(v) == (2, 3) for v in multi)
    print("   positive control (2,3) present: %s" % ctrl)
    # the tested characterization
    char_ok = True
    pair_lows = set(v[0] for v in multi)
    for n in range(N - 1):
        pos = expansions.get(n)
        pred = pos is not None and 1 in pos and 2 not in pos and 3 not in pos
        if pred != (n in pair_lows):
            char_ok = False
            print("   characterization FAILS first at n = %d "
                  "(predicted %s, census %s)" % (n, pred, n in pair_lows))
            break
    print("   characterization d_1=1, d_2=d_3=0 <-> collides with n+1: %s"
          % char_ok)
    ok_all &= consec and ctrl

    # G4 — finiteness with rate
    print("G4 cutoff descent: max cell size and diameter vs phi^{1-c}")
    phi = (1 + 5 ** 0.5) / 2
    prev = None
    for c in range(0, -9, -1):
        g = cells(c)
        interior = [v for v in g.values() if max(v) < N - int(phi ** (1 - c))]
        mx = max(len(v) for v in interior)
        dia = max(max(v) - min(v) for v in interior)
        ratio = ("%.3f" % (mx / prev)) if prev else "  -  "
        bound_ok = dia <= phi ** (1 - c)
        print("   c=%2d: max size %4d (ratio %s), max diameter %5d "
              "<= phi^%d = %.1f: %s"
              % (c, mx, ratio, dia, 1 - c, phi ** (1 - c), bound_ok))
        ok_all &= bound_ok
        prev = mx

    print("ALL CHECKS: %s" % ("GREEN" if ok_all else "RED"))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
