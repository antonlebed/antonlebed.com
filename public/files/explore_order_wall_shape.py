"""The shape of the order wall: finite state against finite window.

THE QUESTION. Redundant digit sets buy constant-time addition, and the
order reads -- sign, equality and comparison -- are non-local at EVERY
lookahead (the order wall). This slate was frozen reading those two as
a purchase and its price; F3 below withdraws the second half, the
non-locality being no more redundancy's than any signed-digit
window's. A live engineering stream asserts
the opposite-sounding thing in the same representation: four patents on
comparison and equality of redundant-form numbers, whose independent
claims recite that the comparator "generate[s] said second result prior
to completion of a carry signal propagation from the least significant
digit to the most significant digit" (US 7395304 claim 1; US 6763368
claim 1 recites the same bound as "independent of any propagation path
to facilitate carry signal propagation from the least significant digit
to the most significant digit"; US 6813628 and US 6826588 carry it in
their abstracts as "without requiring carry propagation", the last of
the four reaching magnitude comparison and not equality alone).

Both are true and they are not the same quantity. Reading all four at
their claims settles which quantity each names, and the answer is not
the width and not the direction of flow:

  - CARRY CHAIN. Theirs. Information flowing from the least significant
    digit toward the most significant one, along a data-dependent chain
    whose length is what a propagation delay measures.
  - WINDOW. Ours. The number of positions of right context an output is
    a function of.

These flow the SAME way -- the leading-end lookahead reads positions
below its own, which is where a carry comes from -- and on ADDITION they
coincide outright: a bounded carry chain and a bounded lookahead are one
condition, which is why the addition cell is the field's already
(explore_redundant_lookback.py).

They part on what the OUTPUT is. Addition is a digit-output map; sign,
equality and comparison are single-bit REDUCTIONS over the whole
numeral. A reduction has no data-dependent chain -- so the carry measure
charges it nothing -- and is never a function of a bounded prefix -- so
the window measure charges it everything. This script asks what the
order wall is then made OF, at fixed width, where both measures are
defined and the corpus's proof (an unbounded all-zero prefix) does not
directly apply.

TRANSPLANT, marked. Every prediction below transports an intuition from
the unbounded-stream setting, where the wall was proved, to fixed width,
which is a different parameter value. The all-zero-prefix argument is
not available at a fixed n: there the prefix has a last digit.

CONVENTIONS. Radix b, symmetric digit set D = {-a..a}, redundant iff
2a + 1 > b. A width-n string d_0..d_{n-1} is read most-significant
first, with value sum_i d_i * b^(n-1-i). Slack rho = 2a - b + 1.

THE SLATE, frozen before the engine.

P-A THE LEADING-NONZERO LAW. Where a <= b - 1, the sign is the sign of
    the first nonzero digit, at every width. The tail below position j
    is bounded by a*(b^j - 1)/(b - 1) <= b^j - 1 < b^j, so it cannot
    overturn a unit at j. Consequence: x = 0 iff every digit is 0, so
    equality-to-zero is an AND over a per-digit predicate reading a
    window of ZERO.

P-B THE LAW BREAKS AT a >= b, and the smallest witness is hand-derived:
    at (b,a) = (2,2) the string (1,-2) has value 2 - 2 = 0 with a
    nonzero leading digit. Above the line the leading digit decides
    nothing and no per-digit predicate decides zero.

P-C FINITE STATE SURVIVES THE BREAK. Sign is computed by a
    most-significant-first automaton over a bounded state: run
    v <- b*v + d, and once |v| > a/(b-1) the tail can never overturn it
    (|tail| < a*b^m/(b-1) against |v|*b^m), so the state clamps to two
    absorbing verdicts. The live states are the integers |v| <= K with
    K = floor(a/(b-1)), giving 2K + 3 states in all. This is predicted
    to reproduce brute-force sign EXACTLY, at every system and width.

P-D FINITE WINDOW DOES NOT. The minimal number of leading digits that
    determines the sign is the FULL WIDTH n, at every system and every
    n -- never n - 1, and so never bounded as n grows. That is the
    order wall transported, and it is what P-C is not.

P-E THE FACTORIZATION IS THE FINDING, if P-C and P-D both hold. Sign is
    then a MONOID PRODUCT of per-digit transitions: each digit maps to a
    function on the bounded state set, the numeral's verdict is their
    composite, and function composition is associative -- so the verdict
    is computable by a reduction of depth log n with no chain at all.
    The wall lives entirely in that reduction. The monoid is the bridge
    object: it is what a carry-free comparator reduces over, and it is
    exactly what a bounded window cannot see.

KILLS, as observables.

K-1 P-A prints a counterexample at any system with a <= b - 1.
K-2 The automaton of P-C disagrees with brute force on any string.
K-3 Some system prints a minimal determining window BELOW its width.
    Any one of these ends the reading; K-3 in particular would put the
    wall itself at fixed width in question, not merely its shape.

POSITIVE CONTROLS, run and read BEFORE any verdict above.
C-1 At (2,1) the sign must equal the sign of the first nonzero digit on
    every string -- hand-derived above, one line, independent of the rig.
C-2 The (1,-2) zero at (2,2) must appear in the rig's own break census.
Both are facts established away from this engine; if the rig misses
either, nothing else it prints is read.

RESOURCE. Pure-Python integer enumeration, no numpy. Per cell the
enumeration is capped near 3e5 strings; whole run is seconds and a few
MB, far inside the 512MB default.

FINDINGS. Both positive controls passed and every prediction held. Nine
symmetric systems, exhaustive to the widths the budget allows (b,a,n).
Seven REDUNDANT, four of them at a <= b-1 and three above: (2,1,11),
(3,2,7), (4,3,6), (5,3,6), (2,2,7), (2,3,6), (3,3,6). Two BALANCED and
non-redundant, the slack-zero control: (3,1,11), (5,2,7). Run: 5.7 s.

F1 THE LEADING-NONZERO LAW (rule, exhaustive at the stated widths).
   Where a <= b - 1 the sign is the sign of the first nonzero digit on
   every string, zero violations at all four such systems, and no
   nonzero string has value zero -- so equality-to-zero there is an AND
   over the window-ZERO predicate "this digit is 0". Above the line the
   law fails and fails abundantly: 5000 of 78125 strings at (2,2),
   10272 of 117649 at (2,3) and 3316 of 117649 at (3,3) carry a sign the
   leading nonzero digit gets wrong. Of those, 238, 480 and 98 are
   strings of value ZERO with a nonzero lead — the sub-census that also
   kills the per-digit equality predicate, and a small fraction of the
   breakage rather than the bulk of it. P-A and P-B confirmed as stated.

F2 SIGN IS FINITE-STATE AT EVERY SYSTEM (rule, exhaustive at the
   stated widths). The clamped MSB-first automaton -- v <- b*v + d,
   absorbing once |v| > K with K = floor(a/(b-1)) -- reproduces
   brute-force sign with ZERO disagreements everywhere, including at
   all three systems where F1's law is broken. State counts 2K+3 are
   3 to 9 across the seven: 5, 5, 5, 3, 7, 9, 5. The count is an UPPER
   BOUND and no minimality is claimed for it. The derivation licenses
   absorbing at |v| >= ceil(a/(b-1)) while the rig absorbs at
   floor(a/(b-1)) + 1, and those two coincide EXCEPT where (b-1)
   divides a, where the rig carries one surplus state-pair -- five of
   the seven systems here, (5,3) and (3,3) being the two that sit at
   the licensed threshold exactly. Surplus states cost correctness
   nothing, which is why the brute-force check cannot detect them and
   is not evidence of minimality.

F3 SIGN IS NOT FINITE-WINDOW AT ANY OF THEM (rule, exhaustive). The
   minimal number of leading digits determining the sign is the FULL
   WIDTH at every system and every width run, 49 cells, no exception --
   never n-1, so nothing bounded as n grows. K-3 did not fire. This is
   the order wall transported to fixed width, where the corpus's
   all-zero-prefix argument is unavailable, and it holds regardless.
   **AND IT IS NOT A PRICE REDUNDANCY PAYS**, which is what the
   one-variable control settles. At slack ZERO -- balanced
   ternary (3,1) and (5,2), non-redundant, everything else about the
   read identical -- the full cone holds just the same, 18 further
   cells. So a full cone for SIGN is generic to a boundary read on a
   signed-digit stream and not something redundancy buys or spends,
   which is consistent with the corpus's own account: sign is
   comparison against zero, zero sits on a cell boundary, and the
   non-redundant window's ambiguity of one cell is already enough to
   put it out of reach. Without this row the finding would have been
   filed as a redundancy price by its placement alone.

F4 AND THE STATE DOES NOT MARK THE REGIME EITHER (rule at the swept
   systems). Sign's whole cost sits in the state, the cone being
   constant everywhere -- but the state count 2K+3, K = floor(a/(b-1)),
   CUTS ACROSS the redundancy boundary rather than marking it: 3 at
   both non-redundant controls AND at (5,3), which is redundant, while
   (3,2) shares (5,3)'s slack rho = 2 and carries 5, a/(b-1) being 1 at
   one and 0.75 at the other. Monoid sizes tell the same story one step
   coarser -- 3 and 3 at the controls, 10, 8, 8, 3 below a = b-1, and
   31, 65, 14 above it -- and K alone does not fix them either, since
   10, 8, 8 and 14 all sit at K = 1.
   **AND THE GENERAL FORM OF THAT IS WORTH STATING**: count the COSTS
   an object actually pays against the PARAMETERS the family gives you
   to pay them with. A digit set's redundancy is normally dialled as
   the one scalar rho, which governs ADDITION's lookahead; sign's state
   answers to a/(b-1) instead. And the word "redundant" is exactly
   rho >= 1, a coarsening of the FIRST parameter -- so it reports on
   the cost addition pays and carries nothing about the cost sign pays.
   One dial, two costs, the dial a blunt reading of one of them -- and
   no amount of turning it finds the other, the loss being in the
   parameterization rather than in the values.

F5 THE FACTORIZATION, and it is the finding. Sign is the product of
   per-digit state maps in a finite TRANSITION MONOID -- sizes 10, 8,
   8, 3, 31, 65, 14 over the seven systems -- and computing that
   product with a BALANCED TREE bracketing rather than a left-to-right
   scan agrees with brute force on every string at every system. So the
   order reads factor as [window-0 map] then [associative reduction]:
   the reduction is what the wall is made of, it has no data-dependent
   chain, and a log-depth circuit evaluates it.

F6 WHAT THAT SETTLES ABOUT THE PATENTS' CLAIM. Their measure charges
   the reduction NOTHING, because a monoid product is not a carry
   chain; ours charges it EVERYTHING, because F3 says no bounded window
   sees it. Both claims are true of the same object and neither is a
   functional of the other. The two measures coincide exactly on
   digit-output maps -- addition, where a bounded carry chain and a
   bounded lookahead are one condition -- and part exactly on the
   reductions. Which is where the corpus's holdings sit: coincidence at
   the cell already saturated (explore_redundant_lookback.py, the
   field's own threshold) and divergence at the cell where the corpus
   has a wall. The bridge holds only where there is nothing to sell.
"""

import itertools
import sys

# (radix, a). Redundant iff 2a+1 > b. The first four sit at a <= b-1
# (the leading-nonzero regime), the last three at a >= b (the break).
SYSTEMS = [(2, 1), (3, 2), (4, 3), (5, 3), (2, 2), (2, 3), (3, 3)]

# THE ONE-VARIABLE CONTROL. Slack rho = 2a - b + 1 is 0 here: the digit
# set is balanced and exactly covers the radix, so these are NOT
# redundant. Everything else about the reading is identical -- signed
# digits, most-significant-first, the same value map. If the full cone
# survives here it is a fact about reading SIGN off a signed-digit
# stream and not a price redundancy pays, and the finding may not be
# filed as one.
CONTROLS = [(3, 1), (5, 2)]

BUDGET = 300_000  # strings enumerated per (system, width) cell


def value(digits, b):
    """Exact value of an MSB-first digit string."""
    v = 0
    for d in digits:
        v = v * b + d
    return v


def sgn(x):
    return (x > 0) - (x < 0)


def max_width(b, a, budget=BUDGET):
    """Largest n with (2a+1)^n <= budget."""
    n, size = 0, 1
    while size * (2 * a + 1) <= budget:
        size *= 2 * a + 1
        n += 1
    return n


def strings(a, n):
    return itertools.product(range(-a, a + 1), repeat=n)


# ---------------------------------------------------------------- P-A/P-B

def leading_nonzero_census(b, a, n):
    """Does the first nonzero digit decide the sign? Returns
    (violations, smallest witness or None)."""
    bad, witness = 0, None
    for d in strings(a, n):
        lead = 0
        for x in d:
            if x:
                lead = x
                break
        if sgn(value(d, b)) != sgn(lead):
            bad += 1
            if witness is None:
                witness = d
    return bad, witness


def zero_census(b, a, n):
    """Nonzero digit strings whose value is zero -- the per-digit
    equality predicate failing. Returns (count, first witness, the
    full witness set). The set is what a control may test against: the
    witnesses come in negation pairs, so which one an enumeration meets
    first is an artifact of digit order and not a fact about the ring.
    """
    bad, witness, found = 0, None, set()
    for d in strings(a, n):
        if value(d, b) == 0 and any(d):
            bad += 1
            found.add(d)
            if witness is None:
                witness = d
    return bad, witness, found


# ------------------------------------------------------------------- P-C

def clamp_bound(b, a):
    """K: beyond |v| = K the tail cannot overturn the sign."""
    return a // (b - 1)


def step(v, d, b, K):
    """One MSB-first transition on the clamped state. States are the
    integers |v| <= K plus the absorbing verdicts K+1 and -(K+1)."""
    if abs(v) > K:
        return v  # absorbing
    w = b * v + d
    if w > K:
        return K + 1
    if w < -K:
        return -(K + 1)
    return w


def automaton_sign(d, b, K):
    v = 0
    for x in d:
        v = step(v, x, b, K)
    return sgn(v)


def automaton_check(b, a, n):
    """Automaton against brute force on every string. Returns
    (disagreements, witness or None)."""
    K = clamp_bound(b, a)
    bad, witness = 0, None
    for d in strings(a, n):
        if automaton_sign(d, b, K) != sgn(value(d, b)):
            bad += 1
            if witness is None:
                witness = d
    return bad, witness


# ------------------------------------------------------------------- P-D

def determines(b, a, n, c):
    """Do the leading c digits determine the sign of every width-n
    string? Returns (bool, colliding pair or None)."""
    seen = {}
    for d in strings(a, n):
        key = d[:c]
        s = sgn(value(d, b))
        if key in seen:
            if seen[key][0] != s:
                return False, (seen[key][1], d)
        else:
            seen[key] = (s, d)
    return True, None


def minimal_window(b, a, n):
    """Smallest c such that the leading c digits determine the sign of
    every width-n string, with a colliding pair one below it.

    Determination is UPWARD CLOSED in c -- a longer prefix refines the
    partition it induces -- so the boundary is found by bisection and
    the whole enumeration runs a handful of times instead of n times.
    """
    lo, hi = 0, n  # c = n always determines; c = lo may or may not
    ok0, collide = determines(b, a, n, 0)
    if ok0:
        return 0, None
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        ok, pair = determines(b, a, n, mid)
        if ok:
            hi = mid
        else:
            lo, collide = mid, pair
    return hi, collide


# ------------------------------------------------------------------- P-E

def transition_monoid(b, a):
    """The monoid generated by the per-digit state maps. Returns
    (element count, generator count)."""
    K = clamp_bound(b, a)
    states = list(range(-(K + 1), K + 2))
    gens = []
    for d in range(-a, a + 1):
        gens.append(tuple(step(v, d, b, K) for v in states))
    idx = {s: i for i, s in enumerate(states)}
    identity = tuple(states)
    elements = {identity}
    frontier = [identity]
    while frontier:
        f = frontier.pop()
        for g in gens:
            # apply f then g (MSB-first: earlier digits act first)
            h = tuple(g[idx[f[i]]] for i in range(len(states)))
            if h not in elements:
                elements.add(h)
                frontier.append(h)
    return len(elements), len(set(gens)), len(states)


def monoid_product_check(b, a, n):
    """Sign as a monoid product, bracketed as a balanced tree rather
    than a left-to-right scan -- the log-depth reduction. Must agree
    with brute force on every string."""
    K = clamp_bound(b, a)
    states = list(range(-(K + 1), K + 2))
    idx = {s: i for i, s in enumerate(states)}
    gen = {d: tuple(step(v, d, b, K) for v in states) for d in range(-a, a + 1)}

    def compose(f, g):
        return tuple(g[idx[f[i]]] for i in range(len(states)))

    def tree(seq):
        if len(seq) == 1:
            return seq[0]
        m = len(seq) // 2
        return compose(tree(seq[:m]), tree(seq[m:]))

    bad, witness = 0, None
    for d in strings(a, n):
        f = tree([gen[x] for x in d])
        if sgn(f[idx[0]]) != sgn(value(d, b)):
            bad += 1
            if witness is None:
                witness = d
    return bad, witness


# ------------------------------------------------------------------- main

def main():
    print("THE SHAPE OF THE ORDER WALL -- finite state against finite window")
    print("=" * 66)

    print("\n[C-1] POSITIVE CONTROL: (b,a)=(2,1), sign == sign of first")
    print("      nonzero digit, hand-derived. Rig must reproduce it.")
    n = max_width(2, 1)
    bad, w = leading_nonzero_census(2, 1, n)
    print("      width %d, %d strings: violations = %d %s"
          % (n, 3 ** n, bad, "PASS" if bad == 0 else "FAIL " + str(w)))

    print("\n[C-2] POSITIVE CONTROL: (b,a)=(2,2) must show (1,-2) = 0,")
    print("      a nonzero string of value zero, hand-derived. The")
    print("      witness set is closed under negation; both or fail.")
    bad2, w2, set2 = zero_census(2, 2, 2)
    c2ok = set2 == {(1, -2), (-1, 2)}
    print("      width 2: nonzero-but-zero strings = %d, set = %s %s"
          % (bad2, sorted(set2), "PASS" if c2ok else "FAIL"))

    if bad != 0 or not c2ok:
        print("\nCONTROLS FAILED -- nothing below is read.")
        return 1

    print("\n[P-A/P-B] THE LEADING-NONZERO LAW and its break")
    print("  The two counts are DIFFERENT quantities and the second is a")
    print("  subset of the first: a nonzero string of value zero is one")
    print("  way for the leading digit to get the sign wrong, not the")
    print("  only way. Both are printed so neither is quoted for the other.")
    print("  b   a  rho  n   regime   strings   sign!=lead   of those, =0")
    for (b, a) in SYSTEMS:
        n = max_width(b, a)
        bad, w = leading_nonzero_census(b, a, n)
        z, zw, _ = zero_census(b, a, n)
        regime = "a<=b-1" if a <= b - 1 else "a>=b  "
        print("  %-3d %-2d %-3d  %-2d  %s  %-9d %-12d %d"
              % (b, a, 2 * a - b + 1, n, regime, (2 * a + 1) ** n, bad, z))
        if bad:
            print("        first sign violation %s, first nonzero zero %s"
                  % (w, zw))

    print("\n[P-C] THE AUTOMATON against brute force")
    print("  b   a   K  states  n   disagreements")
    for (b, a) in SYSTEMS:
        n = max_width(b, a)
        K = clamp_bound(b, a)
        bad, w = automaton_check(b, a, n)
        print("  %-3d %-2d %-3d %-6d  %-2d  %d%s"
              % (b, a, K, 2 * K + 3, n, bad,
                 "" if bad == 0 else "  FAIL %s" % (w,)))

    print("\n[P-D] THE MINIMAL DETERMINING WINDOW, by width")
    print("  b   a   n   min window   verdict")
    for (b, a) in SYSTEMS:
        nmax = max_width(b, a)
        for n in range(1, nmax + 1):
            c, collide = minimal_window(b, a, n)
            tag = "= n (full cone)" if c == n else "< n  ** K-3 **"
            print("  %-3d %-2d %-3d %-12d %s%s"
                  % (b, a, n, c, tag,
                     "" if c == n or collide is None else " %s" % (collide,)))

    print("\n[P-D CONTROL] THE SAME MEASUREMENT AT SLACK ZERO -- balanced")
    print("  digit sets that are NOT redundant. One variable changed.")
    print("  b   a  rho  n   min window   sign=lead?")
    for (b, a) in CONTROLS:
        nmax = max_width(b, a)
        bad, _ = leading_nonzero_census(b, a, nmax)
        for n in range(1, nmax + 1):
            c, _ = minimal_window(b, a, n)
            print("  %-3d %-2d %-3d  %-2d  %-12d %s"
                  % (b, a, 2 * a - b + 1, n, c,
                     ("yes" if bad == 0 else "no") if n == nmax else ""))

    print("\n[P-E] THE TRANSITION MONOID and the tree-bracketed product")
    print("  Controls included: if the cone is constant across regimes,")
    print("  the STATE is where a regime difference would have to show.")
    print("  b   a  rho  states  monoid  generators   tree == brute force")
    for (b, a) in CONTROLS + SYSTEMS:
        n = max_width(b, a)
        m, g, ns = transition_monoid(b, a)
        bad, w = monoid_product_check(b, a, n)
        print("  %-3d %-2d %-3d  %-7d %-7d %-12d %s"
              % (b, a, 2 * a - b + 1, ns, m, g,
                 "yes" if bad == 0 else "NO %s" % (w,)))

    return 0


if __name__ == "__main__":
    sys.exit(main())
