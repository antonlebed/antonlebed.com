"""explore_working_amnesiac.py -- THE WORKING AMNESIAC
(sequel of explore_forgetting_certificate.py; growth conventions of
explore_one_way.py).

THE QUESTION. The amnesia certificate's working clause, made formal:
a "still-working" system must RETAIN a required function g of its
history -- the state must compute g -- while certifying that it no
longer contains X. For which pairs (g, X) does a WORKING AMNESIAC
exist: a designable state map Phi that computes g and carries a
certificate for X, at which grade, and at what state-size price?
The bracketing specimens: the reader-descent corpus (g = optimal
reading, X = the stream, coexisting at the robust grade --
explore_scale_clock.py) and the tuned amnesiac (g = growth goes on,
X = the route, the tuned grade -- explore_one_way.py). The trivial
bound: X a function of g forces readable.

THE WORKING CLAUSE (definition, fixed before the run). Phi computes
g iff g factors through Phi (g = h o Phi) -- equivalently, Phi's
partition of the history space REFINES g's partition. A working
amnesiac for (g, X) is a Phi computing g whose every fiber is
SPREAD (meets >= 2 X-classes; a one-class fiber reads X off the
state) and FLAT (X-posterior uniform on the fiber's consistent
values) at the grade claimed:
  W-R    the g-fiber carries one X-class, so every admissible Phi
         reads X there (no working amnesiac);
  W-T(w) every Phi-fiber spread + flat at the named weight w;
  W-S    every Phi-fiber spread + flat at every w in the family.
MIN-STATES (the price): the number of Phi-fibers, minimized over
working amnesiacs at the grade.

THE LATTICE FRAME. Admissible Phi = the interval [g, discrete] in
the partition lattice of the history space: the working amnesiac
question is whether that interval contains a spread + flat
partition -- a transversality question between g's fibers and X's
fibers under the weight family's measure.

THE LEMMAS (proved on paper before the run; the engine instances
and cross-checks them, it does not prove them).

  L1 (fiber-locality). Phi may be chosen freely inside each
  g-fiber, so existence and price decompose per g-fiber: a working
  amnesiac exists iff every g-fiber separately admits a partition
  into spread flat blocks; min-states is the sum of per-fiber
  minima. The census below is per-g-fiber.

  L2 (the trivial bound). If X is a function of g -- even just
  constant on one g-fiber -- every block inside that fiber has one
  X-class: W-R forced there. No working amnesiac hides what the
  retained function pins.

  L3 (two-class conservation). On a g-fiber carrying exactly two
  X-classes with masses m1, m2, every spread block contains both
  classes and flat means its two class-masses are equal; summing
  over blocks gives m1 = m2. So a two-class fiber is curable iff
  Phi = g is already flat there: REFINEMENT NEVER CURES A
  TWO-CLASS LEAK. Holds per weight, hence also robustly.

  L4 (the no-majority criterion; uniform-weight fibers). If all
  histories in a g-fiber have equal mass and the X-class counts
  are c_1 >= ... >= c_r (r >= 2, total N), a spread flat partition
  exists IFF c_1 <= N - c_1 (no class holds a strict majority).
  Necessity: a block containing class 1 takes t from it and >= t
  from the rest combined; sum. Sufficiency: N even -- lay tokens
  in a line sorted by class and pair token i with token i + N/2
  (no class spans half the line, so every pair is two classes);
  N odd -- then r >= 3, remove one triple from the three largest
  classes (checking c_1 - 1 <= (N-3)/2 in both branches of the
  new maximum) and recurse into the even case. The counts (1,1,1)
  show why the odd step is a triple: pairing would strand a token.
  WEIGHTED SCOPE: with unequal masses only NECESSITY survives
  (max class mass <= half the fiber mass, same argument);
  sufficiency becomes subset-mass matching and is NOT claimed --
  the census measures the gap (fibers passing the mass test with
  no cure found: THE MATCHING GAP).

  L5 (robust blocks = the rigidity mechanism at block scope). A
  block is flat at every beta iff its per-class sums of interior
  normalizer products agree as Dirichlet series in beta -- in a
  constant-menu world every block of a DATED-endpoint fiber
  qualifies (weights equal there; age fibers keep their numerators);
  in breadth it needs exact product coincidences, never scanned at
  block level before this run (kill K2's home).

  L6 (retention monotonicity). Phi computes g implies Phi computes
  any coarsening g' of g, so the admissible set grows as g
  coarsens and existence transfers from finer to coarser retained
  functions. The (g, X) existence region is upward-closed in
  g-coarseness. What does NOT transfer is the baseline: the
  coarsest state Phi = g' conditions on bigger fibers, and bigger
  fibers can be more skewed (see the numerator effect below).

  L7 (identity-X shortcut). For X = the full route, classes are
  singletons, a flat block is one whose members all have EQUAL
  mass, so a cure at w exists iff no route's mass is unique in its
  fiber, and min-states = the number of mass level-sets. Hiding
  the whole route from a working state is exactly the mass-tie
  structure -- computable at any fiber size, no partition search.

THE NUMERATOR EFFECT (hand-derived before the run; the reversal
that redesigned this census). Conditioning on a DATED ENDPOINT
cancels the Boltzmann numerators -- the moves' product is the
endpoint, common to the fiber -- so constant-menu fibers are
route-uniform. Conditioning on AGE ALONE mixes endpoints: the
numerators survive, and in the depth world the first move is
majority-readable (mass 3^beta/(2^beta + 3^beta) > 1/2, exactly).
Retaining LESS can expose MORE: the certificate's difficulty is
not monotone in the retained function even though admissibility is
(L6) -- because the mass-majority obstruction (L4 necessity) is
partition-free, no refinement recovers what the coarse
conditioning surfaced.

MODEL + CENSUS DESIGN. Growth conventions of explore_one_way.py:
state N, move m multiplies, weight m^-beta / Z_N; dated-endpoint
fibers weigh routes by the product of interior 1/Z (numerators
cancel); age fibers weigh routes by full path probability. Worlds
as in explore_forgetting_certificate.py:
  W_T  tuned k = 2 amnesiac: menu(1) = {2,3}, menu(2) = {3,5,15},
       menu(3) = {2,10}; ages <= 2.
  W_D  depth column: constant menu {2,3}; ages <= 5.
  W_B  plain breadth: squarefree moves 2..30 coprime to the state;
       ages <= 3.
  W_RIG rigged control: menu(2) = {3}, menu(3) = {2}.
Retained functions g: the dated endpoint (N, age); the age alone
(W_D and W_T only -- breadth age fibers are out of scope by size).
Forgotten X per fiber: the route, the first move, the first two
moves, the move multiset. Betas 1, 2, 3; exact Fractions
throughout. Exhaustive partition search on fibers of <= 8 routes
(Bell(8) = 4140); uniform-weight fibers above the cap get the L4
verdict (proved); non-uniform fibers above the cap print
SKIPPED-BY-SIZE -- no silent caps. Verdict per fiber: W-R (one
class), W-S (one partition flat at every beta jointly), W-T (cured
at beta = 1, short of a joint all-beta cure), W-ODD (cured only at
betas != 1 -- watched observable),
W-LEAK (no cure anywhere); STRICT marks cures where the baseline
Phi = g is not flat (refinement strictly beats the coarsest
working state).

PREDICTIONS (fixed before the run; PW2 and PW5 were corrected by
the pre-engine hand attack -- the numerator effect above -- and
are frozen here in corrected form).
  PW1 (W_D dated, X = first move): mixed fibers a != b print
      W-LEAK (L3: two classes, masses a : b); fibers a = b print
      W-S at price 1 (already flat, uniform weights); pure powers
      print W-R.
  PW2 (W_D age, X = first move): every age fiber prints W-LEAK at
      every beta, by mass-majority 3^beta/(2^beta+3^beta) > 1/2
      exactly -- the numerator effect, partition-free.
  PW3 (W_D dated, X = first two moves): (a,b) = (2,1) prints W-S
      price 1 (counts (1,1,1), baseline flat); (3,1) and (1,3)
      print W-S price 2 STRICT (counts (2,1,1): baseline skewed,
      pairing cures); (2,2) prints W-S price 2 STRICT (counts
      (1,2,2,1)); (4,1) and (1,4) print W-LEAK (counts (3,1,1):
      majority).
  PW4 (W_T dated): fiber (6,2) with X = route and fiber (30,2)
      with X = first move print W-T at beta = 1 with min-states 1
      and NO cure at beta = 2, 3 -- two-history fibers, the
      partition interval is trivial: the tuned grade is
      refinement-stable.
  PW5 (W_T age, X = first move): the age-2 fiber prints W-LEAK at
      beta = 1 by mass-majority (class-2 mass 3/10 of total 1/2);
      betas 2, 3 printed by the engine.
  PW6 (W_D dated, X = move multiset): W-R at every fiber (L2: the
      endpoint determines the multiset).
  PW7 (W_B dated, X = route): the S-cure count prints 0 (kill K2
      watches the opposite); the T-cure count at beta = 1 is
      MEASURED, no prediction -- a cure means exact Z-product
      ties exist in breadth, none means the order leak of the
      certificate census extends down the whole lattice interval.
  PW8 (W_D age, X = first two moves; MEASURED): necessity passes
      at beta = 1 (class masses (9,6,6,4)/25, no majority); cure
      existence is the run's question -- writing u_a for the
      common weight of the age fiber's words with a twos
      (u_a proportional to (3/2)^a at beta = 1), the tie
      arithmetic 3 u_a = 2 u_{a+1} exists at beta = 1 and is
      beta-specific, so any cure is at most W-T: partition-tuning
      in a symmetric world without touching menus, if it
      assembles.

KILLS (observables with live failure modes, weighed after the
run). K1: on every uniform-weight fiber within the search cap the
engine runs BOTH the L4 verdict and the exhaustive search; any
disagreement prints MISMATCH (fires iff the no-majority proof or
its implementation is wrong). K2: any breadth block-cure flat at
ALL grid betas prints the tied routes with their normalizer
products (fires iff exact product coincidence exists at scope).

CONTROLS (positive, run first). C1: the rigged world's fiber
(6,2) prints odds 3 : 2 at beta = 1 and 9 : 4 at beta = 2 (hand
values). C2: the partition search on planted uniform count
vectors -- (3,1,1) no cure; (2,1,1) cured at min-states 2;
(1,1,1) cured at min-states 1 (the triple).

FINDINGS (tiers per the standard naming scale; run record below).

1. THE STRICT WORKING AMNESIAC EXISTS (observation, exhaustive at
   scope -- the census's existence answer). In the depth world
   with the dated endpoint retained and X = the first two moves,
   five fibers cure STRICTLY: the coarsest working state Phi = g
   leaks, and a refinement of it is spread + flat at every beta --
   e.g. (a,b) = (3,1) (counts (2,1,1), baseline posterior
   (1/2, 1/4, 1/4)) cures at min-states 2 by pairing, grade W-S.
   Refinement is not decoration: partition design alone buys a
   robust certificate the coarse state does not have. The
   no-majority criterion (L4, criterion at uniform-weight scope)
   decides every uniform fiber, cross-validated against the
   exhaustive search on all 49 in-cap uniform fibers with zero
   mismatches (kill K1 ran and missed). Depth dated X = first-two
   verdict table: W-R 8, W-S 8 (5 strict), W-LEAK 2.

2. TWO-CLASS CONSERVATION MAKES THE COUNT LEAK PERMANENT (rule,
   proved -- L3 plus the census instance). A two-class fiber is
   curable iff already flat, so the count leak of
   explore_forgetting_certificate.py (first-move posterior
   a/(a+b)) is not just undescended but UNREMOVABLE while the
   dated endpoint is retained: every mixed a != b fiber prints
   W-LEAK (8 of 20), the diagonal prints W-S at price 1, pure
   powers W-R. Deleting a record's attribute while keeping the
   record has a parity-style obstruction no state design crosses.

3. THE NUMERATOR EFFECT -- RETAINING LESS EXPOSES MORE (rule at
   scope; mechanism proved). Dated-endpoint conditioning cancels
   Boltzmann numerators (the moves' product is the endpoint);
   age-only conditioning surfaces them: in the depth world the
   posterior of FIRST MOVE 2 at an age fiber is EXACTLY
   3^beta/(2^beta + 3^beta) (3/5 at beta = 1, 27/35 at beta = 3)
   -- a strict majority at every beta, and mass-majority is
   partition-free (L4 necessity), so every age fiber prints
   W-LEAK at every beta. Admissibility is monotone in retention
   coarseness (L6) but the certificate is NOT: coarsening the
   retained function from the dated endpoint to the age alone
   converts route-uniform fibers into majority-readable ones. The
   same reversal holds in the tuned world (age-2 posterior 3/5 vs
   2/5, majority at betas 1, 2, 3). PW8 sharpens it: even where
   necessity passes (first-two masses (9,6,6,4)/25, no majority)
   and the tie arithmetic 3 u_a = 2 u_{a+1} exists pointwise
   (u_a as defined at PW8), no cure assembles at ages 2-3 -- the
   numerator effect is robust, not a majority artifact.

4. BREADTH IS A TIE DESERT -- NOTHING CURES (observation,
   exhaustive at scope; the run's strongest negative). Across all
   363 multi-route breadth fibers: for X = the route, ZERO fibers
   contain even ONE tied route pair at beta = 1 (measured
   directly: 0 fibers with any two routes of equal
   interior-normalizer product, hence 0 at all betas jointly) --
   the normalizer product is INJECTIVE on every fiber at scope,
   so by L7 no working state hides the route anywhere, and kill
   K2 ran and missed. For X = the first move: of the 291 fibers
   within the search cap, 173 die by mass majority and 118 pass
   necessity but admit no exact-tie partition (THE MATCHING GAP),
   0 cure; the remaining 72 print SKIPPED-BY-SIZE (> 8 routes;
   none carries an all-beta mass majority -- the partition-free
   test runs at any size -- so they stay genuinely open rather
   than decidably leaking). The footprint leak extends down the whole lattice
   interval: working amnesia in breadth is not designable by
   state choice at all at scope -- symmetry (depth) or menu
   tuning (the tuned world) are the only doors seen, and
   partition design never manufactures the exact ties it needs.

5. THE TUNED GRADE IS REFINEMENT-STABLE (property at its scope).
   The tuned world's two-history fibers have trivial partition
   intervals (the only spread partition is the whole fiber), so
   the working clause neither upgrades nor downgrades them: (6,2)
   with X = route and (30,2) with X = first move print W-T at
   beta = 1, min-states 1, no cure at betas 2, 3. What tuning
   bought, refinement cannot extend; what tuning missed,
   refinement cannot add -- there.

6. THE MATCHING GAP QUANTIFIED (observation). Necessity (no mass
   majority) is far from sufficiency once weights are unequal:
   ALL 118 searchable non-majority breadth fibers fail to cure
   (the 72 over-cap fibers were never majority-tested and stay
   outside this count). In uniform-weight fibers necessity IS
   sufficiency (L4); the gap between the two is exactly the
   exact-subset-sum structure of the weight family -- the working
   clause's true price surface.

THE HEADLINE. The working clause is governed by three proved laws
and one existence proof (the census's search settles the cells the
laws leave open): two-class conservation (refinement never cures a
binary leak -- the count leak is permanent under retention),
the no-majority criterion (uniform fibers: curable iff no class
majority, price measured), and the numerator effect (coarser
retention exposes what dated conditioning cancels -- the
certificate is not monotone in what is retained). Between them
sits the strict working amnesiac: real, cheap (price 2), and
confined at scope to worlds with exact weight ties -- in plain
breadth the tie desert leaves nothing designable, so a working
system that must keep g hides X only where symmetry or tuning
supplies the ties partition design cannot manufacture.

HONEST LIMITS. (a) Exhaustive only at scope: worlds W_T/W_D/W_B
as stated, ages <= 2/5/3, betas {1,2,3}, search cap 8 routes --
72 breadth fibers unresolved by size, printed as such. (b) W-S
claims on uniform-weight fibers rest on the equal-weight witness
(all betas at once), not the beta grid; breadth S-verdicts rest
on the grid plus K2's injectivity scan. (c) The tie desert and
the matching gap are scope facts, not theorems -- no argument yet
says breadth Z-products can never tie. (d) g = age is scanned
only in W_D and W_T (breadth age fibers exceed the cap by far).
(e) Min-states is exact only on searched (<= 8 route) fibers.

RUN RECORD (this file, python explore_working_amnesiac.py, ~1 s).
Run 1: exit 1, 14/15 -- the one red was the PW5 CHECK's own
bookkeeping: it compared the engine's normalized posterior (3/5,
2/5, ratio 3 : 2) against unnormalized hand constants (3/10, 1/5,
the same ratio short of the 1/Z(1) factor); the predicted verdict
(majority, W-LEAK) held as printed. The same read caught a print
label showing the last-beta mass under a beta = 1 label in S2
(the per-beta assertions themselves passed). Both harness slips
fixed -- check now asserts the normalized values, print shows
both betas; engine untouched. Run 2: exit 0, 15/15 green. Run 3
(the audit round): the tie-desert claim as first drafted rested
on the CURE counts, which only show some route unique per fiber,
not pairwise injectivity -- a pairwise tied-route census was
added to the breadth section (no new assertion, measured only)
and printed 0 fibers with any tied pair at beta = 1 (hence 0
jointly); exit 0, 15/15. Run 4 (the close): the 72 over-cap
fibers got the partition-free mass-majority test (measured only)
-- 0 carry an all-beta majority, so all 72 stay open; exit 0,
15/15. Post-run edits: this findings section, the two run-1
harness lines, the run-3 tie census, the run-4 over-cap majority
probe, and one print label naming which first move's mass is
shown (move 2's); nothing else.
"""

from fractions import Fraction
from math import gcd
from collections import defaultdict

BETAS = (1, 2, 3)
CAP = 8


# ---------------------------------------------------------------- worlds

def squarefree(n):
    d = 2
    while d * d <= n:
        if n % (d * d) == 0:
            return False
        d += 1
    return True


SF30 = tuple(m for m in range(2, 31) if squarefree(m))


def menu_tuned(state):
    return {1: (2, 3), 2: (3, 5, 15), 3: (2, 10)}.get(state, ())


def menu_depth(state):
    return (2, 3)


def menu_breadth(state):
    return tuple(m for m in SF30 if gcd(m, state) == 1)


def menu_rigged(state):
    return {1: (2, 3), 2: (3,), 3: (2,)}.get(state, ())


WORLDS = {
    "W_T": (menu_tuned, 2),
    "W_D": (menu_depth, 5),
    "W_B": (menu_breadth, 3),
    "W_RIG": (menu_rigged, 2),
}


# ------------------------------------------------------------- machinery

def histories(menu, max_age):
    out = defaultdict(list)
    frontier = [((), 1)]
    for age in range(1, max_age + 1):
        nxt = []
        for route, state in frontier:
            for m in menu(state):
                r2 = route + (m,)
                out[age].append(r2)
                nxt.append((r2, state * m))
        frontier = nxt
    return out


def interiors(route):
    states = [1]
    for m in route[:-1]:
        states.append(states[-1] * m)
    return states


def zeta(menu, state, beta):
    return sum(Fraction(1, m ** beta) for m in menu(state))


def prod_inv_z(menu, route, beta):
    """Dated-endpoint fiber weight: product of interior 1/Z
    (Boltzmann numerators cancel against the common endpoint)."""
    p = Fraction(1)
    for s in interiors(route):
        p /= zeta(menu, s, beta)
    return p


def route_prob(menu, route, beta):
    """Age-fiber weight: full path probability (numerators SURVIVE
    -- endpoints differ within an age fiber)."""
    p = Fraction(1)
    for s, m in zip(interiors(route), route):
        p *= Fraction(1, m ** beta) / zeta(menu, s, beta)
    return p


def fibers_dated(menu, max_age):
    fib = defaultdict(list)
    for age, routes in histories(menu, max_age).items():
        for r in routes:
            n = 1
            for m in r:
                n *= m
            fib[(n, age)].append(r)
    return fib


def fibers_age(menu, max_age):
    return dict(histories(menu, max_age))


# X columns: label functions on routes.

def x_route(r):
    return r


def x_first(r):
    return r[0]


def x_first2(r):
    return r[:2]


def x_multiset(r):
    return tuple(sorted(r))


# --------------------------------------------------- the partition search

def set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i] + [part[i] + [first]] + part[i + 1:]
        yield part + [[first]]


def block_ok(block, labels, weight_vectors):
    """Spread (>= 2 labels) + flat (per-label mass equal) under EVERY
    weight vector supplied."""
    labs = {labels[i] for i in block}
    if len(labs) < 2:
        return False
    for wv in weight_vectors:
        mass = defaultdict(Fraction)
        for i in block:
            mass[labels[i]] += wv[i]
        vals = list(mass.values())
        if any(v != vals[0] for v in vals[1:]):
            return False
    return True


def search_cure(labels, weight_vectors):
    """Exhaustive: does a spread+flat partition exist under all the
    weight vectors jointly? Returns (exists, min_states)."""
    n = len(labels)
    best = None
    for part in set_partitions(list(range(n))):
        if all(block_ok(b, labels, weight_vectors) for b in part):
            if best is None or len(part) < best:
                best = len(part)
    return (best is not None), best


def l4_verdict(labels):
    """The no-majority criterion for uniform-weight fibers."""
    counts = defaultdict(int)
    for lab in labels:
        counts[lab] += 1
    if len(counts) < 2:
        return False
    c = sorted(counts.values(), reverse=True)
    return c[0] <= sum(c[1:])


def mass_majority(labels, wv):
    """L4 necessity at unequal masses: True iff some class holds a
    strict mass majority (then no cure exists at this weight)."""
    mass = defaultdict(Fraction)
    for lab, w in zip(labels, wv):
        mass[lab] += w
    total = sum(mass.values())
    return max(mass.values()) * 2 > total


def level_set_cure(wv):
    """L7 for X = route: cure iff every mass level-set has >= 2
    members; min-states = number of level-sets."""
    levels = defaultdict(int)
    for w in wv:
        levels[w] += 1
    if any(c < 2 for c in levels.values()):
        return False, None
    return True, len(levels)


# ------------------------------------------------------- fiber verdicts

def fiber_data(menu, routes, dated):
    weigh = prod_inv_z if dated else route_prob
    return {b: [weigh(menu, r, b) for r in routes] for b in BETAS}


def uniform_weights(wv):
    return all(w == wv[0] for w in wv)


def fiber_verdict(menu, routes, xfun, dated, k1_log):
    """Returns (verdict, min_states, strict, extras)."""
    labels = [xfun(r) for r in routes]
    if len(set(labels)) < 2:
        return "W-R", None, False, {}
    wbeta = fiber_data(menu, routes, dated)
    identity_x = xfun is x_route
    cured = {}
    minst = {}
    baseline_flat = {}
    skipped = False
    for b in BETAS:
        wv = wbeta[b]
        mass = defaultdict(Fraction)
        for lab, w in zip(labels, wv):
            mass[lab] += w
        vals = list(mass.values())
        baseline_flat[b] = all(v == vals[0] for v in vals[1:])
        if identity_x:
            ok, ms = level_set_cure(wv)
        elif mass_majority(labels, wv):
            ok, ms = False, None
            if uniform_weights(wv) and len(routes) <= CAP:
                s_ok, _ = search_cure(labels, [wv])
                k1_log.append((l4_verdict(labels), s_ok))
        elif len(routes) <= CAP:
            ok, ms = search_cure(labels, [wv])
            if uniform_weights(wv):
                k1_log.append((l4_verdict(labels), ok))
        elif uniform_weights(wv):
            ok, ms = l4_verdict(labels), None
        else:
            ok, ms = None, None
            skipped = True
        cured[b] = ok
        minst[b] = ms
    if skipped and any(c is None for c in cured.values()):
        return "SKIPPED-BY-SIZE", None, False, {"baseline": baseline_flat}
    # S-cure: joint flatness across all betas.
    if all(cured[b] for b in BETAS):
        if identity_x:
            joint = defaultdict(int)
            for i in range(len(routes)):
                joint[tuple(wbeta[b][i] for b in BETAS)] += 1
            s_ok = all(c >= 2 for c in joint.values())
            s_ms = len(joint) if s_ok else None
        elif len(routes) <= CAP:
            s_ok, s_ms = search_cure(labels, [wbeta[b] for b in BETAS])
        else:
            s_ok, s_ms = all(uniform_weights(wbeta[b]) for b in BETAS), None
        if s_ok:
            strict = not all(baseline_flat.values())
            return "W-S", s_ms, strict, {"baseline": baseline_flat}
    if cured[1]:
        return "W-T", minst[1], not baseline_flat[1], \
            {"baseline": baseline_flat, "cured": cured}
    if any(cured[b] for b in BETAS):
        return "W-ODD", None, False, {"cured": cured}
    return "W-LEAK", None, False, {"baseline": baseline_flat}


# ------------------------------------------------------------------ run

def main():
    checks = []

    def check(name, ok):
        checks.append((name, ok))
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))

    # ---- S0: controls.
    print("S0 controls")
    menu, _ = WORLDS["W_RIG"]
    fib = fibers_dated(menu, 2)
    r62 = fib[(6, 2)]
    w1 = [prod_inv_z(menu, r, 1) for r in r62]
    w2 = [prod_inv_z(menu, r, 2) for r in r62]
    by_first = {r[0]: i for i, r in enumerate(r62)}
    odds1 = w1[by_first[2]] / w1[by_first[3]]
    odds2 = w2[by_first[2]] / w2[by_first[3]]
    check("C1 rigged odds 3:2 at beta=1", odds1 == Fraction(3, 2))
    check("C1 rigged odds 9:4 at beta=2", odds2 == Fraction(9, 4))

    unit = [Fraction(1)] * 5
    ok, ms = search_cure(list("aaabc"), [unit])
    check("C2 (3,1,1) no cure", not ok)
    ok, ms = search_cure(list("aabc"), [unit[:4]])
    check("C2 (2,1,1) cured at 2 states", ok and ms == 2)
    ok, ms = search_cure(list("abc"), [unit[:3]])
    check("C2 (1,1,1) cured at 1 state (the triple)", ok and ms == 1)

    k1_log = []

    # ---- S1: W_D dated, X = first (PW1).
    print("S1 W_D dated, X = first move (PW1)")
    menu, max_age = WORLDS["W_D"]
    fibD = fibers_dated(menu, max_age)
    pw1_ok = True
    tallies = defaultdict(int)
    for (n, age), routes in sorted(fibD.items()):
        a = sum(1 for m in routes[0] if m == 2)
        b = age - a
        v, ms, strict, _ = fiber_verdict(menu, routes, x_first, True, k1_log)
        tallies[v] += 1
        if a == 0 or b == 0:
            pw1_ok &= (v == "W-R")
        elif a == b:
            pw1_ok &= (v == "W-S" and ms == 1)
        else:
            pw1_ok &= (v == "W-LEAK")
    print("  verdicts: %s" % dict(tallies))
    check("PW1 pure=W-R, diagonal=W-S price 1, mixed=W-LEAK", pw1_ok)

    # ---- S2: W_D age, X = first (PW2).
    print("S2 W_D age, X = first move (PW2)")
    fibA = fibers_age(menu, max_age)
    pw2_ok = True
    for age, routes in sorted(fibA.items()):
        if age < 2:
            continue
        labels = [x_first(r) for r in routes]
        for b in BETAS:
            wv = [route_prob(menu, r, b) for r in routes]
            mass = defaultdict(Fraction)
            for lab, w in zip(labels, wv):
                mass[lab] += w
            total = sum(mass.values())
            frac2 = mass[2] / total
            expect = Fraction(3 ** b, 2 ** b + 3 ** b)
            pw2_ok &= (frac2 == expect) and (frac2 * 2 > 1)
        v, _, _, _ = fiber_verdict(menu, routes, x_first, False, k1_log)
        pw2_ok &= (v == "W-LEAK")
        wv1 = [route_prob(menu, r, 1) for r in routes]
        m1 = defaultdict(Fraction)
        for lab, w in zip(labels, wv1):
            m1[lab] += w
        print("  age %d: %s, first-move-2 mass %s at beta=1, %s at beta=3"
              % (age, v, m1[2] / sum(m1.values()), mass[2] / total))
    check("PW2 age fibers majority-leak, mass 3^b/(2^b+3^b) exact",
          pw2_ok)

    # ---- S3: W_D dated, X = first two (PW3).
    print("S3 W_D dated, X = first two moves (PW3)")
    hand = {(2, 1): ("W-S", 1, False), (3, 1): ("W-S", 2, True),
            (1, 3): ("W-S", 2, True), (2, 2): ("W-S", 2, True),
            (4, 1): ("W-LEAK", None, False),
            (1, 4): ("W-LEAK", None, False)}
    pw3_ok = True
    tallies = defaultdict(int)
    strict_count = 0
    for (n, age), routes in sorted(fibD.items()):
        if age < 2:
            continue
        a = sum(1 for m in routes[0] if m == 2)
        b = age - a
        v, ms, strict, _ = fiber_verdict(menu, routes, x_first2, True, k1_log)
        tallies[v] += 1
        strict_count += strict
        if (a, b) in hand:
            hv, hms, hstrict = hand[(a, b)]
            ok_here = (v == hv and ms == hms and strict == hstrict)
            pw3_ok &= ok_here
            print("  (a,b)=(%d,%d): %s price %s strict %s [%s]"
                  % (a, b, v, ms, strict, "ok" if ok_here else "FAIL"))
    print("  verdicts: %s, strict cures: %d" % (dict(tallies), strict_count))
    check("PW3 hand fibers match (prices, strictness)", pw3_ok)

    # ---- S4: W_T dated (PW4).
    print("S4 W_T dated (PW4)")
    menu, max_age = WORLDS["W_T"]
    fibT = fibers_dated(menu, max_age)
    v6, ms6, _, ex6 = fiber_verdict(menu, fibT[(6, 2)], x_route, True, k1_log)
    v30, ms30, _, ex30 = fiber_verdict(menu, fibT[(30, 2)], x_first, True,
                                       k1_log)
    print("  (6,2) X=route: %s price %s cured %s"
          % (v6, ms6, ex6.get("cured")))
    print("  (30,2) X=first: %s price %s cured %s"
          % (v30, ms30, ex30.get("cured")))
    check("PW4 (6,2) W-T price 1, beta=1 only",
          v6 == "W-T" and ms6 == 1 and ex6["cured"] == {1: True, 2: False,
                                                        3: False})
    check("PW4 (30,2) W-T price 1, beta=1 only",
          v30 == "W-T" and ms30 == 1 and ex30["cured"] == {1: True, 2: False,
                                                           3: False})

    # ---- S5: W_T age, X = first (PW5).
    print("S5 W_T age, X = first move (PW5)")
    fibTA = fibers_age(menu, max_age)
    routes = fibTA[2]
    labels = [x_first(r) for r in routes]
    wv = [route_prob(menu, r, 1) for r in routes]
    mass = defaultdict(Fraction)
    for lab, w in zip(labels, wv):
        mass[lab] += w
    print("  age-2 masses at beta=1: %s (total %s)"
          % (dict(mass), sum(mass.values())))
    v, _, _, _ = fiber_verdict(menu, routes, x_first, False, k1_log)
    maj = {b: mass_majority(labels,
                            [route_prob(menu, r, b) for r in routes])
           for b in BETAS}
    print("  age-2: %s, majority per beta %s" % (v, maj))
    check("PW5 age-2 posterior 3/5 vs 2/5 (ratio 3:2), majority, W-LEAK",
          mass[2] == Fraction(3, 5) and mass[3] == Fraction(2, 5)
          and maj[1] and v == "W-LEAK")

    # ---- S6: W_D dated, X = multiset (PW6).
    print("S6 W_D dated, X = move multiset (PW6)")
    menu, max_age = WORLDS["W_D"]
    pw6_ok = all(
        fiber_verdict(menu, routes, x_multiset, True, k1_log)[0] == "W-R"
        for routes in fibD.values())
    check("PW6 all W-R (the trivial bound instanced)", pw6_ok)

    # ---- S7: W_B dated (PW7 + K2).
    print("S7 W_B dated, X = route (PW7) + X = first")
    menu, max_age = WORLDS["W_B"]
    fibB = fibers_dated(menu, max_age)
    multi = {k: v for k, v in fibB.items() if len(v) >= 2}
    t_cures = 0
    s_cures = 0
    k2_pairs = []
    tie1_fibers = 0
    tie_all_fibers = 0
    for key, routes in sorted(multi.items()):
        wv1 = [prod_inv_z(menu, r, 1) for r in routes]
        ok1, _ = level_set_cure(wv1)
        t_cures += ok1
        tie1_fibers += (len(set(wv1)) < len(wv1))
        joint = defaultdict(list)
        for i, r in enumerate(routes):
            joint[tuple(prod_inv_z(menu, r, b) for b in BETAS)].append(r)
        tie_all_fibers += (len(joint) < len(routes))
        if all(len(v) >= 2 for v in joint.values()):
            s_cures += 1
            k2_pairs.append((key, dict(joint)))
    print("  multi-route fibers: %d; X=route T-cures at beta=1: %d; "
          "S-cures: %d" % (len(multi), t_cures, s_cures))
    print("  [measured] fibers with ANY tied route pair: %d at beta=1, "
          "%d at all betas jointly" % (tie1_fibers, tie_all_fibers))
    for key, tied in k2_pairs[:5]:
        print("  K2 FIRING at %s: %s" % (key, tied))
    check("PW7 S-cure count 0 (K2 silent)", s_cures == 0)
    print("  [measured] X=route T-cure count at beta=1: %d" % t_cures)

    xfirst_counts = defaultdict(int)
    gap = 0
    skipped = 0
    skipped_majority = 0
    for key, routes in sorted(multi.items()):
        labels = [x_first(r) for r in routes]
        if len(set(labels)) < 2:
            xfirst_counts["one-class"] += 1
            continue
        if len(routes) > CAP:
            skipped += 1
            # the majority test is partition-free at any size
            skipped_majority += all(
                mass_majority(labels,
                              [prod_inv_z(menu, r, b) for r in routes])
                for b in BETAS)
            continue
        wv1 = [prod_inv_z(menu, r, 1) for r in routes]
        if mass_majority(labels, wv1):
            xfirst_counts["majority"] += 1
            continue
        ok, ms = search_cure(labels, [wv1])
        if ok:
            xfirst_counts["cured"] += 1
        else:
            gap += 1
    print("  [measured] X=first at beta=1: %s, matching gap %d, "
          "skipped-by-size %d (of which %d have a mass majority at "
          "every beta: W-LEAK without search)"
          % (dict(xfirst_counts), gap, skipped, skipped_majority))

    # ---- S8: W_D age, X = first two (PW8, measured).
    print("S8 W_D age, X = first two moves (PW8, measured)")
    menu, max_age = WORLDS["W_D"]
    fibA = fibers_age(menu, max_age)
    pw8_necessity = True
    for age in (2, 3):
        routes = fibA[age]
        labels = [x_first2(r) for r in routes]
        wv1 = [route_prob(menu, r, 1) for r in routes]
        mass = defaultdict(Fraction)
        for lab, w in zip(labels, wv1):
            mass[lab] += w
        total = sum(mass.values())
        norm = {k: v / total for k, v in mass.items()}
        pw8_necessity &= not mass_majority(labels, wv1)
        expect = {(2, 2): Fraction(9, 25), (2, 3): Fraction(6, 25),
                  (3, 2): Fraction(6, 25), (3, 3): Fraction(4, 25)}
        pw8_necessity &= (norm == expect)
        ok, ms = search_cure(labels, [wv1])
        v, vms, strict, _ = fiber_verdict(menu, routes, x_first2, False,
                                          k1_log)
        print("  age %d: masses %s; cure at beta=1: %s (min-states %s); "
              "verdict %s" % (age, norm, ok, ms, v))
    check("PW8 necessity passes, masses (9,6,6,4)/25 exact",
          pw8_necessity)

    # ---- K1: criterion vs search.
    print("K1 criterion-vs-search cross-check")
    mismatches = [(a, b) for a, b in k1_log if a != b]
    print("  uniform fibers cross-checked: %d, mismatches: %d"
          % (len(k1_log), len(mismatches)))
    check("K1 zero MISMATCH", not mismatches)

    # ---- summary.
    print()
    n_ok = sum(1 for _, ok in checks if ok)
    print("CHECKS: %d/%d green" % (n_ok, len(checks)))
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
