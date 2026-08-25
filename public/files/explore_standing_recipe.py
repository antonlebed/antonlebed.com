"""
explore_standing_recipe.py -- THE STANDING FAMILY'S COORDINATE (a sibling
of explore_standing_move.py, whose helpers it imports; the second-instance
question that record's dichotomy left open).

THE QUESTION. explore_standing_move.py proves a dichotomy for greedy
walks: give the walk a family of STANDING recipes -- each admissible at
every reachable state (S1), each priced by one nondecreasing function
f_i of one integer coordinate x_i of the state (S2), under
norm-finiteness (S3) -- and it pays at most min_i f_i(x_i) per step, so
either some coordinate stays bounded and a bounded-cost move recurs
(the walk LOCKS) or every coordinate diverges at once. Its record files
depth over Z on the constant-price branch (the door at q priced by the
excess x_q, floored at -1) and reads breadth as OUTSIDE the schema,
"by consumption": every fixed move of bounded cost is dead after a
finite stage, "so D-IND has no standing family at all". Every instance
of the GROWING-price branch charted so far is the cascade's number-ring
escape. This script asks whether a growing-price standing family exists
over a corpus walk other than the cascade -- and what the schema's
coordinate has to be for the family to say anything.

THE HAND-ATTACK (paper, before this engine; the rig checks it).

(a) A RECIPE, NOT A MOVE. The sibling's own design correction makes
    availability a property of a recipe: the door at a fixed q is a
    different integer from state to state and is standing all the same.
    Read breadth the same way and R(N) = the least prime not dividing N
    is admissible at every state (Euclid), its cost IS the greedy cost
    (the least-new lemma, explore_growth_laws.py), and it is priced by
    the coordinate omega(N) through an increasing f. So breadth carries
    a standing family and sits INSIDE the schema, on the escape branch;
    consumption is why no bounded-price recipe exists there (no move
    ever recurs), which selects the branch rather than voiding the cell.

(b) THE HOLE, AND WHAT PLUGS IT. In any world whose state is one
    integer, the greedy move itself is a recipe, N is an integer
    coordinate, and f = the walk's own cost sequence satisfies (S2)
    wherever that sequence is nondecreasing along the walk. That family
    reads every walk, locked or not, as "the coordinate diverges": the
    dichotomy's lock branch is a SUFFICIENT condition, and its other
    branch says the coordinates diverge, not that the walk escapes. So a
    family carries information only where its coordinates can REPEAT a
    value along the walk -- the depth doors' excess repeats -1 along a
    locked tail while N never repeats. A family all of whose coordinates
    are injective along the walk is BLIND, and (a)'s one-recipe family
    is blind too: omega(N) rises by one at every step.

(c) THE NON-BLIND FAMILY ON THE BREADTH WALK. Fix m >= 3. For each
    reduced class c mod m let R_c(N) = the least prime p == c (mod m)
    not dividing N, x_c(N) = the number of primes dividing N in class c
    beyond the seed's own (the walk's count; at seed 1 the count over N
    itself), and f_c(x) = the (x+1)-th prime of class c among those not
    dividing the seed -- a fixed increasing function per walk. (S1) for R_c is
    Dirichlet's theorem for the class, a classical import; (S3) is
    norm-finiteness of the primes. The cap min_c f_c(x_c(N)) bounds the
    greedy cost at every step and EQUALS it except at the steps whose
    pick is a prime dividing m (a prime in no reduced class), finitely
    many. For m >= 3 the family has at least two recipes, each
    coordinate repeats its value whenever the walk picks another class,
    and every coordinate rises: escape as a CONJUNCTION over classes --
    the schema's Corollary B with real conjuncts -- over Z and on a
    walk that is not the cascade.

THE DESIGN. Four stages over the sibling's eleven seeds
(1, 3, 5, 7, 9, 15, 71, 100, 121, 210, 1001), twelve breadth steps and
six depth steps each, everything computed from the sibling's helpers
(lambda as a factor dict, the demands, the greedy step, the door and the
excess).

  S1 POSITIVE CONTROL. The breadth walk reproduces the healing rule at
     every seed (the picks are the primes not dividing the seed, in
     increasing order); the depth walk from seed 71 pays 5, 7, 17, 17,
     17, 17; the door closed form agrees with the brute door at every
     visited depth state and odd prime up to 50.
  S2 THE ONE-RECIPE BREADTH FAMILY. At every visited breadth state:
     R(N) admissible, cost(R(N)) = greedy cost, omega(N) strictly
     greater than at the previous state. Prints the admissible count,
     the equality count and the number of repeated coordinate values
     (blindness).
  S3 THE CLASS FAMILY, m in {3, 4, 5, 8}. At every visited breadth
     state and reduced class c: R_c(N) found inside the sieve, cap =
     min_c f_c(x_c) against the greedy cost (>= at every step, the
     steps with strict inequality listed), the number of repeated
     coordinate values per class, and each class's coordinate at the
     end of the walk against its start.
  S4 THE VACUOUS FAMILY IN THE DEPTH CELL. Per seed the six greedy
     costs, whether the sequence is nondecreasing (the vacuous family
     meets (S2) exactly there), and the contrast on the locked tails:
     the excess at the lock prime repeated along the tail while N never
     repeats.

PREDICTIONS (fixed before the engine).
  PR1 S2: admissible and cost-equal at all 132 visited states; zero
      repeated omega values at every seed (blind).
  PR2 S3: cap >= greedy at every step for every m and seed; strict
      exactly at the steps picking a prime dividing m, so from seed 1
      exactly one step for each of m = 3, 4, 5, 8 (the pick 3, 2, 5,
      2 respectively) and at most one at every other seed; every class
      coordinate repeats at least once and ends strictly above its
      start at every seed for every m -- the non-blind, growing,
      escaping family the shelf's event asks for.
  PR3 S4: seed 1's depth costs read 3, 5, 3, ... so the vacuous family
      fails (S2) at seed 1; it qualifies (nondecreasing costs) at
      between 6 and 10 of the 11 seeds; at every seed that locks within
      six steps the lock prime's excess is -1 at every tail step (the
      sibling's finding 2) while N is strictly increasing.
  PR4 The verdict: the sibling's finding 5 is wrong as stated
      ("no standing family at all") and right in its consequence (no
      lock); finding 6's third axis -- consumption -- decides the
      BRANCH, not membership.

KILL-SHAPES (observables). KILL-A: a greedy cost strictly above the
class cap at any step (the least-new lemma's reading, or the recipe,
is wrong). KILL-B: R_c(N) not found inside the sieve at a visited state
for a reduced class -- (S1) failing in range. KILL-C: a class
coordinate that never repeats or never rises over the twelve steps at
seed 1 for some m -- the family blind or a class starved in range.
KILL-D: the S1 control failing, which voids every verdict.

FINDINGS (tiers per the standard naming scale; run record below; every
section asserts).

1. BREADTH CARRIES A STANDING FAMILY AND SITS INSIDE THE SCHEMA (rule,
   proved; verified S2). The recipe "the least prime not dividing N" is
   admissible at 132 of 132 visited breadth states over the eleven
   seeds and its cost equals the greedy cost at every one of them (the
   least-new lemma read as a recipe). The sibling's finding 5 -- "D-IND
   has no standing family at all" -- is the FIXED-MOVE reading, which
   the sibling's own design correction had already retired for the
   depth cell; under the recipe reading breadth is on the escape
   branch, and consumption is the reason no bounded-price recipe
   exists there (no move recurs), i.e. consumption SELECTS the branch
   and does not void the cell. The sibling's consequence stands: no
   lock.

2. A FAMILY WHOSE COORDINATES NEVER REPEAT READS NOTHING -- BLINDNESS
   (rule, proved; verified S2, S4). The one-recipe breadth family
   repeats no coordinate value along any walk (0 of 121 transitions,
   omega rising by one at every step). And the schema's hole is wider
   than the slate predicted: the greedy move ITSELF, priced by N through
   the walk's own cost sequence, meets (S1)-(S2) at 11 of 11 depth seeds
   -- every census walk has nondecreasing costs, PR3's predicted dip at
   seed 1 does not exist (its costs read 3, 3, 3, 3, 3, 3: deepening 3
   grows lambda at every step from N = 3, and 5 is never needed) --
   while N strictly increases at every step of every walk. So the
   vacuous family reads all eleven LOCKED walks as "the coordinate
   diverges" and is never false: the lock branch is a sufficient
   condition and the other branch says nothing about escape. What
   separates a reading family from a blind one is that its coordinate
   can REPEAT: at every seed the lock prime's excess sits at -1 along
   the locked tail (the opening step reads 0 at seeds 1, 7, 71, 121,
   where the lock prime is freshly seated, and -1 from the first
   deepening on) while N never repeats. The dichotomy's content is
   therefore never in the dichotomy: it is in choosing coordinates that
   are PROJECTIONS of the state, bounded along a lock.

3. THE CLASS FAMILY IS THE GROWING BRANCH'S SECOND INSTANCE, OVER Z, ON
   A WALK THAT IS NOT THE CASCADE (rule in range, m in {3, 4, 5, 8},
   eleven seeds, twelve steps; (S1) a classical import; verified S3).
   One recipe per reduced class c mod m, the least unused prime in the
   class, priced by the walk's class count x_c through the class's own
   prime sequence: every recipe found at every visited state (264, 264,
   528, 528 lookups at the four moduli); cap >= greedy at every step;
   strict at exactly ONE step per seed -- the pick of the prime dividing
   m -- and at NO step at the seeds that prime already divides (seeds 3,
   9, 15, 210 at m = 3; 100, 210 at m = 4 and 8; 5, 15, 100, 210 at
   m = 5), so the cap is exact off a finite set the moduli name; every
   class coordinate repeats (58 to 106 repeated values per class) and
   every class coordinate ends above its start at every seed. So the
   family is standing, coordinate-priced, GROWING in every coordinate,
   non-blind, and its walk escapes with every coordinate diverging --
   Corollary B with real conjuncts, over Z: the breadth walk's escape is
   the conjunction "every reduced class is picked without end", which
   is Dirichlet's theorem in the schema's own vocabulary, and (S1) is
   that same theorem read per class. The shelf's event -- a standing
   family whose price grows in its coordinate over a corpus walk other
   than the cascade -- is met by a print.

4. THE DIAL, RESTATED (synthesis). Over Z the two fates the schema
   reaches are its two branches under NON-BLIND families: depth under
   the per-prime door menu, whose coordinate floors at -1 and locks
   (the sibling's finding 2); breadth under the per-class menu, whose
   coordinates are unfloored and all diverge. Mortality is the lock
   branch with its coordinate driven to 1 (the sibling's finding 7). The
   cascade's number-ring escape is the same growing branch, the door's
   price growing with the state (explore_module_law.py). What decides
   the branch is whether SOME coordinate stays BOUNDED along the walk:
   over Z the excess is held at its floor (the lock) while the class
   counts are driven up without end by the healing rule (breadth) -- a
   floor the walk sits on is the lock's instance here, not the
   criterion, and consumption is one way for no coordinate to stay
   bounded.

SCOPE + HONESTY. Everything is over Z at eleven seeds; twelve breadth
and six depth steps; (S1) for the class recipes is Dirichlet's theorem
and is checked only inside the sieve (200,000); the growth of the class
coordinates is read at twelve steps and is unbounded only through that
same theorem. The class family is a DECOMPOSITION of the breadth walk
and not a new dynamics; its content is that the schema's growing branch
has an instance whose conjuncts are real, and that the reading needs a
choice of coordinate the schema itself does not make. Finding 2's
blindness criterion is a NECESSARY condition on a family for the
dichotomy to carry information and is not claimed sufficient.

PREDICTIONS (outcomes). PR1 confirmed. PR2 confirmed, and sharpened: the
strict step is absent wherever the prime dividing m already divides the
seed. PR3 REFUTED in both parts -- no dip at seed 1 and 11 of 11
qualifying rather than 6 to 10; its tail clause confirmed (excess -1
along every locked tail from the first deepening). PR4 confirmed by
findings 1 and 2. No kill-shape fired.

RUN RECORD (python 3, one process, 0.3 s wall, 14 MB peak under
memwatch; exit 0, 4,788 checks).
  S1 healing rule 11/11 seeds; seed 71 costs 5, 7, 17, 17, 17, 17;
     door closed form vs brute 924/924
  S2 132 states; recipe admissible 132; cost = greedy 132; repeated
     omega values 0
  S3 m = 3: 264 lookups, strict at seeds 1, 5, 7, 71, 100, 121, 1001
     (pick 3), repeats {1: 70, 2: 58}; m = 4: 264, strict at 1, 3, 5,
     7, 9, 15, 71, 121, 1001 (pick 2), repeats {1: 69, 3: 61}; m = 5:
     528, strict at 1, 3, 7, 9, 71, 121, 1001 (pick 5), repeats {1: 97,
     2: 83, 3: 91, 4: 99}; m = 8: 528, strict at the m = 4 seeds (pick
     2), repeats {1: 106, 3: 92, 5: 84, 7: 90}; every class rises at
     every seed at every m
  S4 nondecreasing costs at 11/11 seeds; locks at 3 (seeds 1, 3, 9, 15),
     5 (5, 7, 100, 210), 7 (121, 1001), 17 (71); N strictly increasing
     at every step
  TOTAL 4,788 checks, exit 0.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_standing_move import (  # noqa: E402
    PRIMES, PRIMESET, factorize, walk, dyn_admissible, ind_admissible,
    door_closed_form, door_brute, excess, to_int,
)

CHECKS = 0


def check(cond, msg=""):
    global CHECKS
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)
    CHECKS += 1


SEEDS = [1, 3, 5, 7, 9, 15, 71, 100, 121, 210, 1001]
BREADTH_STEPS = 12
DEPTH_STEPS = 6
MODULI = [3, 4, 5, 8]


def seed_factors(n):
    return factorize(n) if n > 1 else {}


def omega(Nf):
    return sum(1 for e in Nf.values() if e > 0)


def least_new_prime(Nf):
    for p in PRIMES:
        if Nf.get(p, 0) == 0:
            return p
    return None


def least_new_prime_in_class(Nf, c, m):
    for p in PRIMES:
        if p % m == c and Nf.get(p, 0) == 0:
            return p
    return None


def reduced_classes(m):
    from math import gcd
    return [c for c in range(1, m) if gcd(c, m) == 1]


def class_count(Nf, c, m, seed_f=None):
    """x_c: class-c primes dividing N beyond the seed's own."""
    base = 0 if seed_f is None else sum(
        1 for q, e in seed_f.items() if e > 0 and q % m == c)
    return sum(1 for q, e in Nf.items() if e > 0 and q % m == c) - base


def class_price_fn(seed_f, c, m):
    """f_c: the (x+1)-th prime of class c not dividing the seed."""
    seq = [p for p in PRIMES if p % m == c and seed_f.get(p, 0) == 0]

    def f(x):
        return seq[x]
    return f


def nondecreasing(seq):
    return all(a <= b for a, b in zip(seq, seq[1:]))


def main():
    print("=" * 72)
    print("explore_standing_recipe.py -- the standing family's coordinate")
    print("=" * 72)

    # ---------------- S1: positive control ----------------
    print("\nS1 POSITIVE CONTROL")
    breadth = {}
    for s in SEEDS:
        sf = seed_factors(s)
        tr = walk(sf, ind_admissible, BREADTH_STEPS)
        picks = [m for (_, m, _) in tr]
        expected = [p for p in PRIMES if sf.get(p, 0) == 0][:BREADTH_STEPS]
        check(picks == expected, "healing rule at seed %d" % s)
        breadth[s] = tr
    print("  healing rule reproduced at %d/%d seeds (%d steps each)"
          % (len(SEEDS), len(SEEDS), BREADTH_STEPS))
    depth = {}
    for s in SEEDS:
        depth[s] = walk(seed_factors(s), dyn_admissible, DEPTH_STEPS)
    costs71 = [c for (_, _, c) in depth[71]]
    check(costs71 == [5, 7, 17, 17, 17, 17], "seed 71 depth costs")
    print("  seed 71 depth costs:", costs71)
    agree = 0
    for s in SEEDS:
        for (Nf, _, _) in depth[s]:
            for q in [p for p in PRIMES if p <= 50 and p > 2]:
                check(door_closed_form(Nf, q) == door_brute(Nf, q),
                      "door closed form vs brute")
                agree += 1
    print("  door closed form vs brute: %d/%d agreements" % (agree, agree))

    # ---------------- S2: the one-recipe breadth family ----------------
    print("\nS2 THE ONE-RECIPE BREADTH FAMILY (least prime not dividing N)")
    adm = eq = states = 0
    repeats_total = 0
    for s in SEEDS:
        prev_omega = None
        rep = 0
        for (Nf, m, c) in breadth[s]:
            states += 1
            r = least_new_prime(Nf)
            check(r is not None and ind_admissible(Nf, r),
                  "recipe admissible at seed %d" % s)
            adm += 1
            if r == c:
                eq += 1
            w = omega(Nf)
            if prev_omega is not None and w == prev_omega:
                rep += 1
            prev_omega = w
        repeats_total += rep
    check(eq == states, "recipe cost equals greedy cost everywhere")
    print("  visited states %d; recipe admissible %d; cost = greedy %d;"
          " repeated omega values %d" % (states, adm, eq, repeats_total))

    # ---------------- S3: the class family ----------------
    print("\nS3 THE CLASS FAMILY (one recipe per reduced class mod m)")
    for m in MODULI:
        classes = reduced_classes(m)
        strict_steps = {}
        found = 0
        repeats = {c: 0 for c in classes}
        rises_all = True
        for s in SEEDS:
            sf = seed_factors(s)
            fs = {c: class_price_fn(sf, c, m) for c in classes}
            tr = breadth[s]
            prev = None
            start = {c: class_count(tr[0][0], c, m, sf) for c in classes}
            for i, (Nf, mv, cost) in enumerate(tr):
                for c in classes:
                    r = least_new_prime_in_class(Nf, c, m)
                    check(r is not None, "KILL-B: class %d mod %d starved"
                          % (c, m))
                    found += 1
                    x = class_count(Nf, c, m, sf)
                    check(fs[c](x) == r,
                          "price function reads the recipe at seed %d" % s)
                cap = min(fs[c](class_count(Nf, c, m, sf)) for c in classes)
                check(cost <= cap, "KILL-A: greedy above cap")
                if cost < cap:
                    strict_steps.setdefault(s, []).append((i, mv))
                cur = {c: class_count(Nf, c, m, sf) for c in classes}
                if prev is not None:
                    for c in classes:
                        if cur[c] == prev[c]:
                            repeats[c] += 1
                prev = cur
            last = tr[-1][0]
            # the state after the last move
            end_state = dict(last)
            for p, e in factorize(tr[-1][1]).items():
                end_state[p] = end_state.get(p, 0) + e
            endf = {c: class_count(end_state, c, m, sf) for c in classes}
            for c in classes:
                if not endf[c] > start[c]:
                    rises_all = False
        strict_list = {s: [mv for (_, mv) in v]
                       for s, v in strict_steps.items()}
        all_divide_m = all(m % mv == 0 for v in strict_list.values()
                           for mv in v)
        print("  m = %d classes %s: recipes found %d; cap >= greedy at every"
              " step; strict at %s (every strict pick divides m: %s);"
              " repeated coordinate values per class %s; every class"
              " coordinate rises at every seed: %s"
              % (m, classes, found, strict_list, all_divide_m,
                 repeats, rises_all))
        check(all_divide_m, "strict steps are the primes dividing m")
        check(all(v > 0 for v in repeats.values()),
              "KILL-C: a class never repeats")
        check(rises_all, "KILL-C: a class never rises")

    # ---------------- S4: the vacuous family in the depth cell ----------
    print("\nS4 THE VACUOUS FAMILY IN THE DEPTH CELL")
    qualifies = 0
    for s in SEEDS:
        costs = [c for (_, _, c) in depth[s]]
        nd = nondecreasing(costs)
        qualifies += nd
        Ns = [to_int(Nf) for (Nf, _, _) in depth[s]]
        check(all(a < b for a, b in zip(Ns, Ns[1:])), "N strictly increases")
        tail = ""
        if len(costs) >= 3 and costs[-1] == costs[-2] == costs[-3]:
            q = factorize(costs[-1])
            if len(q) == 1:
                (qp,) = q
                xs = [excess(Nf, qp) for (Nf, _, c) in depth[s]
                      if c == costs[-1]]
                tail = " lock at %d, excess along the tail %s" % (qp, xs)
        print("  seed %5d costs %s nondecreasing=%s%s"
              % (s, costs, nd, tail))
    print("  vacuous family meets (S2) at %d of %d seeds" % (qualifies,
                                                             len(SEEDS)))

    print("\nTOTAL %d checks, exit 0" % CHECKS)


if __name__ == "__main__":
    main()
