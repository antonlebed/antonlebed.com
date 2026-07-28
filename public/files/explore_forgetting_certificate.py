"""explore_forgetting_certificate.py -- THE AMNESIA CERTIFICATE
(sibling of explore_one_way.py; reader-space counterpart
explore_scale_clock.py).

THE QUESTION. When is "this state provably no longer contains X" a
designable property of a still-working system? First step: ONE
definition of an amnesia certificate covering the two proved
specimens in hand -- the information-theoretic one (route-posterior
flatness of grown worlds: explore_one_way.py, the balance criterion)
and the structural one (destination universality of exact reader
descent: explore_scale_clock.py -- the adapted reader is a function
of its metabolism, never its data, under every loss tried) -- then a
toy-exact census over small grown worlds: which states carry which
certificate, and where the two kinds DISAGREE (a state hiding X
information-theoretically with no structural witness, or the
reverse). The proved impossibilities ride along restated: exchange
rigidity and the footprint law (explore_one_way.py) as certificate
NON-EXISTENCE. Definition, lemmas, and predictions fixed before the
run; census exact (Fractions throughout).

THE DEFINITION (fixed before the run). Data: a history space H; the
forgotten datum X : H -> XX (any function of history); a state map
Phi : H -> S (the still-working system's present); a weight family
{pi_w} (the grower's temperatures beta; the learner's losses). The
posterior of X at state s is the pi_w-conditional of X on the fiber
Phi^-1(s). A certificate for X at Phi is a witness at one of four
grades:

  R (readable -- no certificate): X is a function of Phi.
  P (possibilistic): every fiber meets >= 2 X-classes -- X is not
    recoverable as a value. Strongest witness: STATE-SIDE FACTORING,
    a presented split H = XX x R with Phi constant in the XX slot
    (weight-free, uniform over fibers).
  T (tuned-flat): at one named weight w0 the posterior of X is
    UNIFORM on every fiber's consistent X-values. Witness: the mass
    equations solved (a balance-criterion instance).
  S (robust-flat): uniform at EVERY w in the family. Witness kinds:
    (alpha) state-side factoring with X independent of R -- flatness
    inherited, prior-free (Lemma B); (beta) WEIGHT-SIDE SYMMETRY --
    the interior-normalizer multisets coincide along every route of
    the fiber (Lemma C).

  Flatness clause, resolved before the run: the canonical clause is
  FIBER-UNIFORMITY (maximum entropy behind what the living state
  logically pins), not posterior = prior -- a grower's state IS its
  present and always informs the past possibilistically. When the
  state-side factoring is TOTAL (the reader-descent case: the
  destination is a function of metabolism alone), flatness upgrades
  to posterior = prior for EVERY prior -- an annotation on grade S,
  not the base clause.

THE LEMMAS (proved on paper before the run; the engine instances
them, it does not prove them).

  LEMMA A (witness collapse). A quotient q with Phi factoring
  through q and every q-class meeting every X-class exists IFF
  every Phi-fiber meets every X-class. Proof: (<=) take q = Phi;
  (=>) fibers are unions of q-classes. So "factors through a
  quotient killing X" is extensionally the full-spread
  possibilistic grade; the split witness adds provenance
  (weight-freeness), never extension.

  LEMMA B (inheritance). If H = XX x R with pi_w(x, r) =
  mu(x) nu_w(r) (X independent of R, X-prior weight-free) and
  Phi(x, r) = f(r), then P(X = x | S = s) = mu(x) for every s and
  w: posterior = prior, robustly over the family. Proof: the fiber
  of s is XX x f^-1(s), so the conditional of X on it is mu.
  Destination universality's certificate is grade S by this route
  -- inherited and prior-free, no tuning: the two specimens are one
  lemma apart, not one construction apart.

  LEMMA C (weight-side symmetry). If the multiset of interior
  normalizers is the same along every route of a fiber, the route
  posterior is uniform at every beta. Proof: route weight is
  proportional to the product of interior 1/Z (numerators cancel:
  the moves' product is the endpoint), and equal multisets have
  equal products at each beta. The constant-menu depth world
  instances it: every normalizer is the same polynomial.

RESTATEMENTS (proved elsewhere; no new proof here).
  Exchange rigidity (explore_one_way.py) = grade-S NON-EXISTENCE
  for X = route in many-window growth with >= 2 routes, at that
  theorem's proved scope (age-2 route pairs in full generality;
  exchange-closed route sets at any age): flatness at
  all beta forces menu coincidence, which coprimality bars. The
  footprint law = the T-grade failure QUANTIFIED in plain breadth
  (the leak's unique first-order source: the used primes' menu-mass
  footprint). The general obstruction, named and OPEN: does robust
  flatness FORCE the weight-side witness beyond the exchange class?
  (Equal products of Dirichlet polynomials at every beta -- a
  factoriality question about the normalizer semiring.) (Settled
  both ways since, explore_rogue_world.py: NO for designed worlds
  free to recycle primes -- the rogue world realizes all-beta
  flatness with distinct normalizer multisets -- and vacuously YES
  under coprimality, where the quarantine theorem bars multi-route
  all-beta flatness at every age.)

MODEL + CENSUS DESIGN. Growth conventions of explore_one_way.py:
state N, move m multiplies, weight m^-beta / Z_N, route posterior
at a dated endpoint (N, tau) proportional to the product of
interior 1/Z. Worlds:
  W_T  the tuned k = 2 amnesiac: menu(1) = {2,3}, menu(2) =
       {3,5,15}, menu(3) = {2,10}; ages <= 2.
  W_D  the depth column: constant menu {2,3} at every state;
       ages <= 5.
  W_B  plain breadth: squarefree moves 2..30 coprime to the state;
       ages <= 3.
  W_RIG the rigged control: menu(1) = {2,3}, menu(2) = {3},
       menu(3) = {2} -- fiber (6, 2) odds 3^beta : 2^beta by hand.
X-columns per fiber: the route (full identity), the move multiset,
the order within each multiset class, the first move. Betas 1, 2, 3.
Flatness exact; the weight-side witness checked as menu-multiset
coincidence along routes.

PREDICTIONS (fixed before the run).
  PR1 (W_T): fiber (6, 2) route-uniform exactly at beta = 1, odds
      117 : 70 at beta = 2; fiber (30, 2) multiset-posterior
      uniform at beta = 1 ({2,15} vs {3,10}), non-uniform at
      beta = 2, and each multiset class carries exactly ONE
      admissible order (the tuned world hides the SET at 30 and the
      ORDER at 6); the weight-side witness is ABSENT at both.
  PR2 (W_D): every fiber (2^a 3^b, a+b) with a, b >= 1 is
      route-uniform at every tested beta with the witness PRESENT;
      the first-move posterior is EXACTLY (a/(a+b), b/(a+b)),
      beta-free -- THE COUNT LEAK: route-uniformity does not
      coarsen to feature-uniformity; fiber counting leaks features
      even where weights are perfectly symmetric.
  PR3 (W_B): the count of multi-route fibers uniform at BOTH
      beta = 1 and beta = 2 prints 0 (the rigidity shadow at two
      points -- weaker than the interval theorem, so a nonzero
      count is a finding, not only a bug; the control runs first).
  PR4 (W_B): the count of multi-route fibers uniform at beta = 1
      alone prints 0 (accidental exact tuning implausible; LOW
      CONFIDENCE -- the print decides).
  PR5 (the disagreement census, the point of the run): species (a)
      -- structural kill without flatness -- instanced by W_B
      order-fibers (commutativity kills order at every fiber, the
      posterior still leaks); species (b) -- flatness without any
      structural witness -- instanced by W_T at beta = 1 (flat,
      witness absent: the tuned signature). Both must PRINT from
      the census, not be narrated.
  KILL (observable): a fiber grading the four-grade table cannot
      express -- e.g. flat at beta = 2 but not beta = 1 with no
      witness (tuned at an unintended temperature) -- prints as
      UNGRADED; any UNGRADED line means the definition as frozen is
      incomplete, weighed after the run.

FINDINGS (tiers per the standard naming scale; run record below).

1. THE DEFINITION LANDS WHOLE (observation at scope). Zero UNGRADED
   fibers across all 406 census fibers (W_T 5, W_D 20, W_B 381):
   every fiber grades as R, P, T, or S under the frozen table.
   Every census S fiber carries the weight-side witness; the
   state-side kind enters by the reader-descent row (Lemma B plus
   the cited corpus), not as a census fiber.
   Grade tables: W_T R:3 T(beta=1):2; W_D R:10 (pure powers)
   S(weight-side):10 (every mixed fiber); W_B R:18 (age 1) P:363.

2. THE TWO SPECIMENS ARE ONE LEMMA APART (the frame the census
   confirms). Destination universality is grade S by Lemma B --
   state-side factoring plus independence, flatness inherited
   prior-free, no tuning (explore_scale_clock.py supplies the
   factoring: the destination is a function of metabolism alone,
   under every loss tried). The depth column is grade S by Lemma C
   -- weight-side symmetry, verified mechanically (witness present
   at every mixed fiber). The tuned amnesiac is grade T: flat at
   beta = 1 with the witness ABSENT -- the census distinguishes
   tuned from structural flatness by inspection, not narrative. And
   plain breadth is grade P: the state-side kill (commutativity)
   holds everywhere while flatness fails everywhere. One slogan
   covers both corpora, directions kept honest: structural
   witnesses BUY robustness over the weight family (Lemmas B and
   C); tuning buys single-weight flatness; whether robustness
   FORCES a structural witness is the named open obstruction --
   forced in the exchange class by the rigidity theorem, and true
   without exception at this census's scope.

3. THE DISAGREEMENT CENSUS (observation, exhaustive at scope; the
   run's point). Both species print: (a) structural kill WITHOUT
   flatness -- 363 of 363 order-carrying multi-route W_B fibers
   leak order at beta = 1 (the state factors through the
   commutative quotient at every one, and the posterior still
   reads order through the normalizers); (b) flatness WITHOUT any
   structural witness -- W_T (6, 2), flat at beta = 1, witness
   absent. The information-theoretic and structural certificate
   kinds are independent axes at scope, crossing in both
   directions.

4. THE COUNT LEAK (rule at its scope -- the a/(a+b) law is proved
   for the two-move constant menu and verified at every mixed
   fiber; the two-channel naming is the observation).
   Route-uniformity does NOT coarsen to feature-uniformity: in the
   perfectly symmetric depth world the first-move posterior is
   EXACTLY (a/(a+b), b/(a+b)) at 2^a 3^b -- beta-free, verified at
   every mixed fiber to age 5. Two leak channels now stand named:
   the WEIGHT leak (breadth's footprint -- measure asymmetry) and
   the COUNT leak (fiber geometry -- a uniform posterior counted
   over unequal coarse classes). Design consequence: a certificate
   for X does not descend to functions of X; every coarsening
   needs its own flatness clause.

5. THE HIDDEN DATUM IS A PER-FIBER FACT (observation). One tuned
   world hides DIFFERENT things at different endpoints: (6, 2)
   hides order (the move set is determined), (30, 2) hides the SET
   ({2,15} vs {3,10}, each with exactly one admissible order).
   "What is forgotten" is fiber-local even in a single world.

6. THE RIGIDITY SHADOW (observation, PR3/PR4). Zero of 363
   multi-route breadth fibers are flat at beta = 1; zero are flat
   at beta = 1 and 2 jointly (at this outcome the second count is
   implied by the first; PR3 had independent force only had PR4
   failed). Accidental exact tuning does not occur at scope:
   two-point flatness already fails everywhere in plain breadth,
   consistent with the interval theorem's shadow.

THE HEADLINE. The amnesia certificate is one object with two
independent clauses -- a structural witness (state-side factoring
or weight-side symmetry) and a measure clause (fiber-uniformity,
upgrading to prior-freeness exactly when the factoring is total) --
and the corpus's two proved forgetting specimens sit at the same
grade by different witnesses, one lemma apart. Structural witnesses
buy robustness over the weight family; tuning buys one temperature
-- and cannot buy more where the rigidity theorem's scope reaches
(the tuned amnesiac's age-2 fibers sit inside it); the census
separates the two mechanically. The open obstruction is
named: whether robust flatness FORCES a weight-side witness beyond
the exchange class (Dirichlet-polynomial factoriality).

HONEST LIMITS. (a) The census is exhaustive only at its scope
(worlds W_T/W_D/W_B as stated, ages <= 2/5/3, betas {1,2,3});
grade-S "flat at all beta" claims rest on the witness (proved), not
the beta grid. (b) The reader-descent row enters by Lemma B plus
the cited corpus, not by a rerun -- the factoring premise is that
corpus's measured headline at its own toy-exact scope. (c) Lemma A
makes the split-free structural certificate extensionally the
full-spread possibilistic grade; split witnesses add provenance
only. (d) The count-leak law a/(a+b) is proved for the two-move
constant menu (equal route weights + binomial fiber counting);
other menus were not scanned. (e) PR4 was low-confidence and
happened to hold; nothing rests on it.

RUN RECORD (this file, python explore_forgetting_certificate.py,
~1 s). Run 1: exit 0, 27/27 checks green on the first run --
controls first (W_RIG odds 3/2 and 9/4 exact, W_D flat), then PR1
(117/70 reproduced), PR2 (count leak 3/4 at (24, 4)), PR3/PR4
(0/363, 0/363), PR5 (both species instanced), kill missed (zero
UNGRADED). Post-run edits: this findings section only; engine and
checks untouched.
"""

from fractions import Fraction
from math import gcd
from collections import defaultdict

BETAS = (1, 2, 3)


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
    """All routes from state 1, grouped {age: [route, ...]}."""
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
    """The states where choices were made: 1, then each partial product
    short of the endpoint."""
    states = [1]
    for m in route[:-1]:
        states.append(states[-1] * m)
    return states


def zeta(menu, state, beta):
    return sum(Fraction(1, m ** beta) for m in menu(state))


def route_prob(menu, route, beta):
    """Exact probability of the route in the age-|route| ensemble."""
    p = Fraction(1)
    for s, m in zip(interiors(route), route):
        p *= Fraction(1, m ** beta) / zeta(menu, s, beta)
    return p


def fibers(menu, max_age):
    """{(endpoint, age): [route, ...]}"""
    fib = defaultdict(list)
    for age, routes in histories(menu, max_age).items():
        for r in routes:
            n = 1
            for m in r:
                n *= m
            fib[(n, age)].append(r)
    return fib


def prod_inv_z(menu, route, beta):
    """Posterior weight proportional to the product of interior 1/Z
    (exact; numerators cancel -- the moves' product is the endpoint)."""
    p = Fraction(1)
    for s in interiors(route):
        p /= zeta(menu, s, beta)
    return p


def uniform(weights):
    return all(w == weights[0] for w in weights)


def menu_signature(menu, route):
    """The multiset of interior menus (each as a sorted tuple) -- equal
    signatures imply equal normalizer products at every beta (Lemma C)."""
    return tuple(sorted(tuple(sorted(menu(s))) for s in interiors(route)))


def analyze(menu, routes):
    """Full fiber analysis; exact."""
    a = {}
    a["n_routes"] = len(routes)
    a["witness"] = len({menu_signature(menu, r) for r in routes}) == 1
    sets = defaultdict(list)
    for i, r in enumerate(routes):
        sets[tuple(sorted(r))].append(i)
    a["n_sets"] = len(sets)
    a["max_orders_per_set"] = max(len(v) for v in sets.values())
    per_beta = {}
    for beta in BETAS:
        w = [prod_inv_z(menu, r, beta) for r in routes]
        total = sum(w)
        set_mass = {k: sum(w[i] for i in idx) for k, idx in sets.items()}
        first_mass = defaultdict(Fraction)
        for wi, r in zip(w, routes):
            first_mass[r[0]] += wi
        per_beta[beta] = {
            "flat_route": uniform(w),
            "flat_set": uniform(list(set_mass.values())),
            "flat_order": all(
                uniform([w[i] for i in idx])
                for idx in sets.values() if len(idx) >= 2),
            "posterior_first": {m: fm / total
                                for m, fm in first_mass.items()},
            "weights": w,
        }
    a["beta"] = per_beta
    return a


def grade(a):
    """Grade the fiber for X = route under the frozen table."""
    if a["n_routes"] == 1:
        return "R"
    flat = [b for b in BETAS if a["beta"][b]["flat_route"]]
    if a["witness"]:
        return "S(weight-side witness)" if len(flat) == len(BETAS) \
            else "UNGRADED(witness without flatness)"
    if len(flat) == len(BETAS):
        return "S?(flat at all tested beta, no witness)"
    if flat == [1]:
        return "T(beta=1)"
    if flat:
        return "UNGRADED(flat at %s only, no witness)" % flat
    return "P"


# ------------------------------------------------------------------ run

def main():
    checks = []

    def check(name, ok):
        checks.append((name, ok))
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))

    print("S0 machinery + positive controls")
    # total probability = 1 at max age (no dead ends before max age
    # in any world as built)
    for wname, (menu, max_age) in WORLDS.items():
        h = histories(menu, max_age)
        for beta in (1, 2):
            tot = sum(route_prob(menu, r, beta) for r in h[max_age])
            check("%s total probability age %d beta %d = 1"
                  % (wname, max_age, beta), tot == 1)
    # rigged control: (6,2) non-flat, odds 3^beta : 2^beta exactly
    fib_rig = fibers(menu_rigged, 2)
    a = analyze(menu_rigged, fib_rig[(6, 2)])
    for beta in (1, 2):
        w = a["beta"][beta]["weights"]
        routes = fib_rig[(6, 2)]
        i23 = routes.index((2, 3))
        i32 = routes.index((3, 2))
        odds = w[i23] / w[i32]
        check("W_RIG (6,2) beta=%d non-flat, odds %s" % (beta, odds),
              not a["beta"][beta]["flat_route"]
              and odds == Fraction(3 ** beta, 2 ** beta))
    # flat control: W_D (6,2) must read flat
    fib_d = fibers(menu_depth, 5)
    ad = analyze(menu_depth, fib_d[(6, 2)])
    check("W_D (6,2) flat at every beta (control)",
          all(ad["beta"][b]["flat_route"] for b in BETAS))

    print("S1 the tuned world W_T (PR1)")
    fib_t = fibers(menu_tuned, 2)
    a6 = analyze(menu_tuned, fib_t[(6, 2)])
    a30 = analyze(menu_tuned, fib_t[(30, 2)])
    routes6 = fib_t[(6, 2)]
    w2 = a6["beta"][2]["weights"]
    odds6 = w2[routes6.index((2, 3))] / w2[routes6.index((3, 2))]
    check("(6,2) route-uniform at beta=1", a6["beta"][1]["flat_route"])
    check("(6,2) beta=2 odds = 117/70", odds6 == Fraction(117, 70))
    check("(30,2) set-uniform at beta=1", a30["beta"][1]["flat_set"])
    check("(30,2) set-posterior non-uniform at beta=2",
          not a30["beta"][2]["flat_set"])
    check("(30,2) one order per set (order degenerate)",
          a30["max_orders_per_set"] == 1 and a30["n_sets"] == 2)
    check("witness ABSENT at (6,2) and (30,2)",
          not a6["witness"] and not a30["witness"])
    print("  (6,2) grade: %s   (30,2) grade: %s"
          % (grade(a6), grade(a30)))

    print("S2 the depth world W_D (PR2)")
    all_ok_flat, all_ok_wit, all_ok_first = True, True, True
    for (n, age), routes in sorted(fib_d.items()):
        # decompose n = 2^a 3^b
        a_, b_, m = 0, 0, n
        while m % 2 == 0:
            a_, m = a_ + 1, m // 2
        while m % 3 == 0:
            b_, m = b_ + 1, m // 3
        if a_ == 0 or b_ == 0:
            continue
        an = analyze(menu_depth, routes)
        all_ok_flat &= all(an["beta"][b]["flat_route"] for b in BETAS)
        all_ok_wit &= an["witness"]
        for beta in BETAS:
            pf = an["beta"][beta]["posterior_first"]
            all_ok_first &= (pf[2] == Fraction(a_, a_ + b_)
                             and pf[3] == Fraction(b_, a_ + b_))
    check("every mixed fiber route-uniform at every beta", all_ok_flat)
    check("weight-side witness present at every mixed fiber", all_ok_wit)
    check("first-move posterior = (a/(a+b), b/(a+b)) exactly, beta-free"
          " (the count leak)", all_ok_first)
    # print the leak at one fiber
    ex = analyze(menu_depth, fib_d[(24, 4)])  # 2^3 * 3
    print("  count leak at (24,4): P(first=2) = %s (hand: 3/4), beta-free"
          % ex["beta"][1]["posterior_first"][2])

    print("S3 plain breadth W_B (PR3, PR4)")
    fib_b = fibers(menu_breadth, 3)
    multi = {k: v for k, v in fib_b.items() if len(v) >= 2}
    flat1 = flat12 = 0
    nonflat_order = 0
    order_fibers = 0
    for k, routes in multi.items():
        an = analyze(menu_breadth, routes)
        if an["beta"][1]["flat_route"]:
            flat1 += 1
            if an["beta"][2]["flat_route"]:
                flat12 += 1
        if an["max_orders_per_set"] >= 2:
            order_fibers += 1
            if not an["beta"][1]["flat_order"]:
                nonflat_order += 1
    print("  multi-route fibers: %d (ages <= 3, M = 30)" % len(multi))
    print("  uniform at beta=1: %d   uniform at beta=1 AND 2: %d"
          % (flat1, flat12))
    check("PR3: double-flat count = 0 (rigidity shadow)", flat12 == 0)
    check("PR4: beta=1-flat count = 0 (low confidence)", flat1 == 0)
    # showcase fiber (30, 2): three sets, two orders each
    a30b = analyze(menu_breadth, fib_b[(30, 2)])
    print("  showcase (30,2): %d routes, %d sets, orders/set <= %d"
          % (a30b["n_routes"], a30b["n_sets"], a30b["max_orders_per_set"]))
    for m, p in sorted(a30b["beta"][1]["posterior_first"].items()):
        print("    P(first=%d | 30,2) = %s at beta=1" % (m, p))

    print("S4 the disagreement census + grades (PR5)")
    print("  species (a) structural kill WITHOUT flatness: %d of %d"
          % (nonflat_order, order_fibers)
          + " W_B order-carrying fibers leak order at beta=1"
          + " (commutativity kills order at every one)")
    check("species (a) instanced (count >= 1)", nonflat_order >= 1)
    sb = (a6["beta"][1]["flat_route"] and not a6["witness"])
    print("  species (b) flatness WITHOUT structural witness: W_T (6,2)"
          " flat at beta=1, witness absent -> %s" % sb)
    check("species (b) instanced", sb)
    # grade table over all census fibers
    print("  grade table (X = route):")
    for wname, (menu, max_age) in (("W_T", WORLDS["W_T"]),
                                   ("W_D", WORLDS["W_D"]),
                                   ("W_B", WORLDS["W_B"])):
        counts = defaultdict(int)
        for k, routes in fibers(menu, max_age).items():
            counts[grade(analyze(menu, routes))] += 1
        row = "   ".join("%s: %d" % (g, c) for g, c in sorted(counts.items()))
        print("    %-4s %s" % (wname, row))
        ungraded = sum(c for g, c in counts.items() if "UNGRADED" in g)
        check("%s: zero UNGRADED fibers (the kill observable)" % wname,
              ungraded == 0)

    n_fail = sum(1 for _, ok in checks if not ok)
    print("TOTAL: %d checks, %d failed" % (len(checks), n_fail))
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
