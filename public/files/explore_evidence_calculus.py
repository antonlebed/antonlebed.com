"""
THE STATS THREAD -- evidence on the ring: the e-calculus and
the semiring family.

THE TARGET (motivated by an earlier question: "what comes after
frequentist/Bayesian?"). Two questions. (1) Does
"sum-product vs max-product = one algorithm in two semirings" extend
to a semiring-indexed family of inference calculi with a tower home?
(2) The third-pillar candidate is the e-value / game-theoretic
calculus -- what does it attach to on the ring? (the working guess: the
graded logic's delta-measurement.)

Survey anchors (standard material, named so nothing here poses as new):
the generalized distributive law (Aji-McEliece 2000: one message-passing
algorithm over ANY commutative semiring; sum-product = Bayesian
marginals, max-product = MAP/Viterbi, Boolean = feasibility/CSP), factor
graphs (Kschischang-Frey-Loeliger 2001), valuation algebras
(Shenoy-Shafer local-computation axioms 1990; Kohlas: probability,
possibility, belief functions, constraints are all instances --
the family question is answered YES classically), provenance semirings
(Green-Karvounarakis-Tannen 2007: the polynomial semiring N[X] is free;
every instance is its homomorphic image), Maslov dequantization /
idempotent probability (Litvinov-Maslov: the tropical semiring is the
log-limit of the probability semiring; Dubois-Prade possibility theory
is the maxitive point), and the third pillar itself: game-theoretic
probability and e-values (Shafer-Vovk 2001/2019: probability = price of
a bet; Ville 1939: optional stopping; Vovk-Wang 2021: an e-variable is
E >= 0 with mean <= 1 under the null, evidence = capital of a bet
against the null, the only essential symmetric merge is the arithmetic
mean; Grunwald-de Heide-Koolen "safe testing"; Ramdas et al.
anytime-valid inference). The SAME Shafer stands on both sides
(Shenoy-Shafer locality, Shafer-Vovk betting). Ours is the tower-side
composition: the rung as the exact finite home of the family, and the
ring objects (idempotents, mu-valuation, delta, collapse) as the
e-calculus's carriers.

PREDICTIONS (stated before computing, per protocol):
  P1 (one algorithm, any semiring): for product-form f the
     ring-total factorizes per channel in ALL of sum/max/Boolean
     (GDL + CRT; expect trivially exact), and the marginal
     reconstruction test "f == (tensor of its own channel marginals,
     normalized)" is the semiring-indexed rank-1/product-form test.
  P2 (the conjunctive split is semiring-stable): the earlier conjunctive
     test's Boolean verdicts (equality, divisibility conjunctive; order not) are the
     verdicts at EVERY semiring point -- for 0/1-valued f the three
     verdicts provably coincide (a 0/1 product form can be taken with
     0/1 factors). The walls do not depend on the temperature.
  P3 (rank levels): order's channel flattening at Z/6 (a 4x9 matrix
     over (x2,y2) x (x3,y3)) has FULL Boolean rank 4 and full real
     rank 4 -- the earlier "maximal failure" as a rank statement;
     equality's flattening has rank 1 in both; the size function's
     2x3 matrix has full rank 2 in both real and tropical senses.
  P4 (cylinder e-variables): normalized support-cylinder indicators
     E_S = 1[x e_S = x]/mu(e_S) are EXACT e-variables (mean = 1);
     E_S E_T = E_{S int T} / mu(e_{S union T}) pointwise (the
     multiplicative law mu(S^T)mu(SvT) = mu(S)mu(T) is the
     bookkeeping); the product is e-valid iff S union T = all
     channels iff the two events are CRT-independent: THE PRODUCT
     RULE OF THE RING'S E-CALCULUS IS CRT INDEPENDENCE of read-sets.
  P5 (delta is what the e-variable reads): the classicality test
     ("x is idempotent-valued on S") has the exact e-variable
     1[C_S] prod_{p in S} p/2; its payoff region is read off the
     delta-measurement (C_S = {supp delta(x) disjoint from S}); its
     log on success is the tropical/log-mass valuation (Maslov,
     exact at the rung -- no limit needed); composing with the
     collapse x -> x^lambda yields mean prod p/2 > 1: the
     measurement FABRICATES classicality, and the e-calculus is
     exactly the frame that rejects it (bets must precede collapse).
  P6 (the merge asymmetry): power-mean merges of e-variables are
     e-valid exactly up to the arithmetic point (q <= 1; classical
     power-mean inequality), and die on the max side: max-merge
     means approach the union bound 2 on cylinder pairs as the rung
     grows. min loses evidence but stays valid; max fabricates.
     The third pillar is NOT a third semiring point -- it is a
     second-order axis (bets over masses) anchored at the summing
     end, with the tropical valuation as its log-shadow.

Findings preview:
  1. ONE TEST, EVERY SEMIRING (rule): product-form totals factorize
     per channel in sum/max/Boolean; the marginal-reconstruction
     test is exact in each; the earlier conjunctive test IS the Boolean
     instance, and the verdicts are semiring-stable on relations.
  2. RANK LEVELS (observation): at Z/6, equality flattens to rank
     1/1 (Boolean/real), order to rank 4/4 (full/full); size's 2x3
     matrix is full rank really and tropically. Whether the earlier
     failure modes always sort by rank level was an open hook here;
     RESOLVED, REFUTED (the rank-sorting record block below + section
     VI: what order's full rank detected was the LIFT).
  3. THE PRODUCT RULE IS CRT INDEPENDENCE (rule): cylinder and
     classicality e-variables are exact (mean = 1); a product of two
     is an e-variable iff their EFFECTIVE read-sets are disjoint --
     cylinders read complements (valid iff S u T = all), classicality
     reads S minus {2} (channel 2's classicality is the VACUOUS bet:
     every residue mod 2 is already in {0,1} -- the decality as the
     trivial e-variable), mixed valid iff T subset S u {2}. The
     multiplicative law is the excess bookkeeping: E[E_S E_T] = 1/mu(S v T).
  4. LOG E-VALUE = TROPICAL VALUATION (rule): evidence factors are
     1/P per independent channel read; log-evidence is the log-mass
     excluded -- the counting valuation IS the e-calculus's
     log-shadow, exact at every rung.
  5. COLLAPSE BREAKS ANYTIME-VALIDITY (rule): E_cl(x^lambda) =
     prod_{p in S} p/2 for EVERY x -- the measurement manufactures
     classicality evidence; e-processes must be adapted to the
     pre-collapse filtration.
  6. THE MERGE ASYMMETRY (rule + classical): min/harmonic/arithmetic
     merges e-valid on all tested pairs (arithmetic exactly tight);
     quadratic and max fail with exact witnesses; worst max-merge
     mean over cylinder pairs is exactly 2 - 1/N (59/30 at Z/30,
     419/210 at Z/210) -- the union bound approached at rate 1/N.
     Evidence on the ring is ONE-DIRECTIONAL (lose: allowed;
     fabricate: forbidden) -- the same arrow as the ring's OR
     interference and the collapse, and the betting calculus is the
     formalism that enforces it.

THE RANK SORTING RECORD (finding 2's open hook):
RESOLVED, REFUTED in both directions, with two proved fragments and
the gap (no properly-failing relation's rank computed) filled.
The hook asked whether the conjunctive failure modes sort by rank
level (proper = rank gap, maximal = full). Hand-proofs first,
mechanical confirmation in section VI:
  (a) CRITERION (proved): R is conjunctive iff its flattening at
      every single-channel split has Boolean rank <= 1. Rank <= 1 at
      a split = rectangle = R is a product across that split (the
      row/col supports ARE the projections); conversely rectangles at
      all k single-channel splits intersect to the full product
      (induction on k: a rectangle at channel 1 passes the rectangle
      property to the complementary factor).
  (b) FOLD LEMMA (proved): a difference-invariant relation (R(x,y)
      iff y - x in D) has identical rows within a difference class,
      so rank(flatten at S) = rank(T_D) with T_D[u][v] =
      1_D(crt(u,v)) -- bounded by min(prod_S p, prod_rest p), the
      SQUARE ROOT of full: a difference-invariant relation never
      reaches full rank at any split, yet the thresholded family
      |x-y|_circ <= d fails MAXIMALLY once 2d+1 >= p_k. Witnesses:
      d = 1 at Z/6 (the rank coda's own rung) fails maximally at
      rank 2, Boolean and real, of full 4; at Z/30's {2}-split the
      mode crosses proper -> maximal (d = 1 -> 2) with rank pinned
      at 2.
  (c) PROPER AT RANK 1 (witness): the grading ord(x) | ord(y) fails
      properly, yet its {2}-split is a RECTANGLE (rank exactly 1) --
      channel 2 is a dummy coordinate (every unit-part order there
      is 1), so the relation splits off the full square. Rank is a
      PER-SPLIT quantity, the modes are GLOBAL verdicts: they do not
      live on the same object.
  (d) ZERO-ROW CAP (proved -- the one true fragment): a missed
      residue pair (proper failure at a channel) is a zero row of
      that channel's split, capping rank strictly below full on that
      side. The grading's numbers (the named gap, measured at every
      single split of BOTH rungs): the {2}-split is a rectangle
      (rank 1) at both rungs, rank 3 at every non-dummy split --
      Z/30: {3} 3 of 9, {5} 3 of 25 (6 zero rows); Z/210: {3}/{5}/{7}
      3 of 9/25/49 (zero rows 0/6/12, (3,1) among the {7}-split's).
  (e) WHAT FULL RANK WAS DETECTING: the LIFT. Order's ranks at Z/30
      are 4 / 7 / 13 at the {2}/{3}/{5}-splits, all above the fold
      caps 2/3/5. Above-cap certifies non-difference-invariance
      (one-directional: the grading is also non-difference-invariant
      yet stays below its caps), and order's non-invariance is
      exactly the lift. Order is FULL only at the {2}-split (4 = the
      saturated small side; 7 of 9 and 13 of 25 elsewhere): even the
      lift-borne maximal relation is not full away from the smallest
      split. The Z/6 specimen's "maximal = full" was the archimedean
      lift speaking through a tiny side.
  Classical contact: the split flattening IS the communication
  matrix of R under the CRT split (Alice holds the S-residues, Bob
  the complement); Boolean rank = the rectangle cover number, whose
  log is nondeterministic communication complexity (Yao 1979;
  Kushilevitz-Nisan), and rank-vs-cover is log-rank territory
  (Lovasz-Saks). The size wall in communication dress: the
  lift-borne relations are the expensive ones.

Run: python prime/code/explore_evidence_calculus.py   (~1 s, tiny memory)
"""

import time
import random
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd

T0 = time.perf_counter()
random.seed(53)

# ---------------------------------------------------------------- helpers

def primorial(ps):
    return reduce(lambda a, b: a * b, ps, 1)

def crt(ps, residues):
    """The element of Z/prod(ps) with the given residues."""
    N = primorial(ps)
    x = 0
    for p, r in zip(ps, residues):
        M = N // p
        x += r * M * pow(M, -1, p)
    return x % N

def idem(ps, S):
    """e_S: 1 on channels in S, 0 elsewhere."""
    return crt(ps, [1 if p in S else 0 for p in ps])

def subsets(ps):
    out = []
    for r in range(len(ps) + 1):
        out.extend(frozenset(c) for c in combinations(ps, r))
    return out

def section(title):
    print()
    print("=" * 68)
    print(title)
    print("=" * 68)

PASS = []
def report(label, ok, detail=""):
    PASS.append((label, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f" -- {detail}" if detail else ""))

# Semirings: (name, add, mul, zero, one, div). Values are Fractions
# (SUM, MAX) or 0/1 ints (BOOL). div is exact where defined.
SUM = ("sum", lambda a, b: a + b, lambda a, b: a * b,
       Fraction(0), Fraction(1), lambda a, b: a / b)
MAX = ("max", max, lambda a, b: a * b,
       Fraction(0), Fraction(1), lambda a, b: a / b)
BOOL = ("bool", lambda a, b: a | b, lambda a, b: a & b, 0, 1,
        lambda a, b: a)          # T = 1 whenever f is nonempty

SEMIRINGS = [SUM, MAX, BOOL]

# ---------------------------------------------------------------- I

section("I. ONE ALGORITHM, ANY SEMIRING (GDL on the rung)")

# P1a: product-form totals factorize per channel, all three semirings.
def gdl_total_check(ps, trials=8):
    N = primorial(ps)
    ok = True
    bool_totals = set()
    for name, add, mul, zero, one, _ in SEMIRINGS:
        for _ in range(trials):
            if name == "bool":
                # no forced entries: the zero branch (an all-zero channel
                # kills the total) must be exercised too
                g = {p: [random.randint(0, 1) for _ in range(p)] for p in ps}
            else:
                g = {p: [Fraction(random.randint(0, 9), random.randint(1, 9))
                         for _ in range(p)] for p in ps}
            lhs = zero
            for x in range(N):
                v = one
                for p in ps:
                    v = mul(v, g[p][x % p])
                lhs = add(lhs, v)
            rhs = one
            for p in ps:
                t = zero
                for r in range(p):
                    t = add(t, g[p][r])
                rhs = mul(rhs, t)
            ok = ok and (lhs == rhs)
            if name == "bool":
                bool_totals.add(lhs)
    return ok, bool_totals

ok3, cov3 = gdl_total_check([2, 3, 5])
ok4, cov4 = gdl_total_check([2, 3, 5, 7])
ok = ok3 and ok4 and (cov3 | cov4) == {0, 1}
report("product-form totals factorize, sum/max/bool, Z/30 + Z/210", ok,
       "8 random product forms per semiring per rung; bool hits 0 and 1")

# P1b/P2: the marginal-reconstruction test on relations (pair ring).
# f == (product of its own channel marginals) / total^(k-1) iff f is
# product-form over the channels. Boolean instance = the earlier conjunctive test.
def reconstruction_verdict(ps, f, sr):
    """f: function on pairs (x,y) of Z/N. Returns True iff f == f_hat."""
    name, add, mul, zero, one, div = sr
    N = primorial(ps)
    k = len(ps)
    marg = {p: {} for p in ps}
    total = zero
    vals = {}
    for x in range(N):
        for y in range(N):
            v = f(x, y)
            vals[(x, y)] = v
            total = add(total, v)
            for p in ps:
                key = (x % p, y % p)
                marg[p][key] = add(marg[p].get(key, zero), v)
    if total == zero:
        return True                                  # empty f is product-form
    denom = one
    for _ in range(k - 1):
        denom = mul(denom, total)
    for (x, y), v in vals.items():
        fh = one
        for p in ps:
            fh = mul(fh, marg[p][(x % p, y % p)])
        if div(fh, denom) != v:
            return False
    return True

REL = {
    "equality":     lambda x, y: x == y,
    "divisibility": None,   # filled per ring below
    "order":        lambda x, y: x < y,
}

def divides(ps):
    return lambda x, y: all((y % p == 0) or (x % p != 0) for p in ps)

ps3 = [2, 3, 5]
verdicts = {}
for rname in ["equality", "divisibility", "order"]:
    rel = divides(ps3) if rname == "divisibility" else REL[rname]
    for sr in SEMIRINGS:
        f = (lambda r: lambda x, y:
             (1 if r(x, y) else 0) if sr[0] == "bool"
             else (Fraction(1) if r(x, y) else Fraction(0)))(rel)
        verdicts[(rname, sr[0])] = reconstruction_verdict(ps3, f, sr)

ok = (all(verdicts[("equality", s)] for s in ["sum", "max", "bool"])
      and all(verdicts[("divisibility", s)] for s in ["sum", "max", "bool"])
      and not any(verdicts[("order", s)] for s in ["sum", "max", "bool"]))
report("Z/30 verdicts: equality, divisibility product-form; order NOT", ok,
       "same verdict at all three semirings (the Boolean row)")

# P2 coincidence is provable for indicators; confirm at Z/210 (bool + sum).
ps4 = [2, 3, 5, 7]
ok = True
for rname in ["equality", "order"]:
    rel = REL[rname]
    vb = reconstruction_verdict(
        ps4, lambda x, y: 1 if rel(x, y) else 0, BOOL)
    vs = reconstruction_verdict(
        ps4, lambda x, y: Fraction(1) if rel(x, y) else Fraction(0), SUM)
    ok = ok and (vb == vs == (rname == "equality"))
report("Z/210 confirm: verdicts coincide bool/sum (equality yes, order no)",
       ok, "0/1 product forms can be taken with 0/1 factors")

# Size itself (unary): not separable in any semiring.
def separable_verdict(ps, f, sr):
    name, add, mul, zero, one, div = sr
    N = primorial(ps)
    k = len(ps)
    marg = {p: {} for p in ps}
    total = zero
    for x in range(N):
        v = f(x)
        total = add(total, v)
        for p in ps:
            marg[p][x % p] = add(marg[p].get(x % p, zero), v)
    denom = one
    for _ in range(k - 1):
        denom = mul(denom, total)
    return all(div(reduce(mul, (marg[p][x % p] for p in ps), one), denom)
               == f(x) for x in range(N))

ok = (not separable_verdict(ps3, lambda x: Fraction(x), SUM)
      and not separable_verdict(ps3, lambda x: Fraction(x), MAX)
      and not separable_verdict(ps3, lambda x: 1 if x < 15 else 0, BOOL))
report("size is not product-form in any semiring (Z/30)", ok,
       "sum/max on the value, bool on the half -- the wall at every point")

# ---------------------------------------------------------------- II

section("II. RANK LEVELS AT Z/6 (the failure modes get numbers)")

def flatten_relation(rel):
    """4x9 matrix: rows (x2,y2), cols (x3,y3), entry rel(x,y) at Z/6."""
    rows = [(a, b) for a in range(2) for b in range(2)]
    cols = [(a, b) for a in range(3) for b in range(3)]
    M = []
    for (x2, y2) in rows:
        row = []
        for (x3, y3) in cols:
            x, y = crt([2, 3], [x2, x3]), crt([2, 3], [y2, y3])
            row.append(1 if rel(x, y) else 0)
        M.append(row)
    return M

def boolean_rank(M):
    """Exact: min number of all-ones rectangles covering the ones."""
    m, n = len(M), len(M[0])
    ones = {(i, j) for i in range(m) for j in range(n) if M[i][j]}
    if not ones:
        return 0
    rects = []
    for rmask in range(1, 1 << m):
        rows = [i for i in range(m) if rmask >> i & 1]
        cols = [j for j in range(n) if all(M[i][j] for i in rows)]
        if cols:
            rects.append({(i, j) for i in rows for j in cols})
    # dedupe to maximal rectangles
    rects = [r for r in rects if not any(r < s for s in rects)]
    for r in range(1, len(rects) + 1):
        for combo in combinations(rects, r):
            if set().union(*combo) >= ones:
                return r
    return None

def frac_rank(M):
    """Exact rank over Q (Gaussian elimination on Fractions)."""
    A = [[Fraction(v) for v in row] for row in M]
    m, n = len(A), len(A[0])
    rank, row = 0, 0
    for col in range(n):
        piv = next((r for r in range(row, m) if A[r][col] != 0), None)
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        for r in range(m):
            if r != row and A[r][col] != 0:
                f = A[r][col] / A[row][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[row])]
        rank += 1
        row += 1
    return rank

Meq = flatten_relation(lambda x, y: x == y)
Mord = flatten_relation(lambda x, y: x < y)
ok = boolean_rank(Meq) == 1 and frac_rank(Meq) == 1
report("equality flattening: Boolean rank 1, real rank 1", ok)

br, fr = boolean_rank(Mord), frac_rank(Mord)
ok = br == 4 and fr == 4
report(f"order flattening: Boolean rank {br}, real rank {fr} (full = 4)",
       ok, "full-rank here is the LIFT, not the maximality -- section VI")

# Size's 2x3 matrix: real rank and tropical (max,*) rank both full.
S6 = [[crt([2, 3], [a, b]) for b in range(3)] for a in range(2)]
fr = frac_rank(S6)
trop_nonsing = any(S6[0][i] * S6[1][j] != S6[0][j] * S6[1][i]
                   for i in range(3) for j in range(3) if i < j)
ok = fr == 2 and trop_nonsing
report("size 2x3 matrix: real rank 2, tropical rank 2 (both full)", ok,
       f"M = {S6}")

# ---------------------------------------------------------------- III

section("III. CYLINDER E-VARIABLES (the product rule is CRT independence)")

def cylinder_data(ps):
    """For each S: the cylinder A_S = {x : x e_S = x}, mu, E_S values."""
    N = primorial(ps)
    out = {}
    for S in subsets(ps):
        e = idem(ps, S)
        A = [x for x in range(N) if (x * e) % N == x]
        mu = Fraction(len(A), N)
        out[S] = (set(A), mu)
    return out, N

ok_all = {"count": True, "point": True, "law": True,
          "evalid": True, "indep": True}
for ps in [ps3, ps4]:
    cyl, N = cylinder_data(ps)
    full = frozenset(ps)
    for S, (A, mu) in cyl.items():
        # the count law |A_S| = prod_{p in S} p is the e-variable's
        # exactness: E_S = 1[A_S] * N/prod_S p then has mean exactly 1
        # (the mean is enumeration vs CLOSED FORM, not mu vs itself)
        muF = Fraction(primorial(sorted(S)), N)
        if Fraction(len(A), N) != muF:
            ok_all["count"] = False
        if A != {x for x in range(N)
                 if all(x % p == 0 for p in ps if p not in S)}:
            ok_all["count"] = False
    for S, (A_S, mu_S) in cyl.items():
        for T, (A_T, mu_T) in cyl.items():
            I, U = S & T, S | T
            A_I, mu_I = cyl[frozenset(I)]
            mu_U = cyl[frozenset(U)][1]
            # pointwise: E_S E_T = E_I / mu_U (the multiplicative law as bookkeeping)
            if A_S & A_T != A_I:
                ok_all["point"] = False
            if mu_I * mu_U != mu_S * mu_T:
                ok_all["law"] = False
            mean = Fraction(len(A_I), N) / (mu_S * mu_T)   # E[E_S E_T]
            if mean != 1 / mu_U:
                ok_all["law"] = False
            if (mean <= 1) != (U == full):
                ok_all["evalid"] = False
            # independence of the events themselves
            indep = (Fraction(len(A_S & A_T), N)
                     == Fraction(len(A_S), N) * Fraction(len(A_T), N))
            if indep != (U == full):
                ok_all["indep"] = False

report("count law |A_S| = prod_S p, all S (Z/30 + Z/210): E_S exact",
       ok_all["count"],
       "enumeration vs closed form; mean E_S = 1 IS this law")
report("pointwise E_S E_T = E_{S^T} / mu(SvT); the collapse law is the bookkeeping",
       ok_all["point"] and ok_all["law"],
       "mu(S^T) mu(SvT) = mu(S) mu(T); E[E_S E_T] = 1/mu(SvT)")
report("product e-valid  <=>  S u T = all channels", ok_all["evalid"])
report("  ... <=>  A_S, A_T independent (CRT: read-sets S^c, T^c disjoint)",
       ok_all["indep"])

# Scale: RAD. Counting law spot-verified by enumeration, then the
# S u T criterion swept over all 128 x 128 idempotent pairs by formula.
ps7 = [2, 3, 5, 7, 11, 13, 17]
N7 = primorial(ps7)
spot = [frozenset({2, 3, 5}), frozenset({7, 17}), frozenset(ps7)]
ok = True
for S in spot:
    e = idem(ps7, S)
    cnt = sum(1 for x in range(N7) if (x * e) % N7 == x)
    ok = ok and cnt == primorial(sorted(S))
full7 = frozenset(ps7)
def mu7(S):
    return Fraction(primorial(sorted(S)), N7)
for S in subsets(ps7):
    for T in subsets(ps7):
        mean = mu7(S & T) / (mu7(S) * mu7(T))
        if (mean <= 1) != (S | T == full7):
            ok = False
            break
report("RAD: counts spot-verified by enumeration; criterion all 128^2 pairs",
       ok, "16384 products, e-valid exactly when S u T covers the 7 channels")

# ---------------------------------------------------------------- IV

section("IV. CLASSICALITY EVIDENCE (delta is what the e-variable reads)")

ok_delta, ok_mean, ok_factor, ok_rule, ok_collapse = (True,) * 5
collapse_means = {}
for ps in [ps3, ps4]:
    N = primorial(ps)
    lam = reduce(lambda a, b: a * b // gcd(a, b), [p - 1 for p in ps], 1)
    singles = {p: Fraction(sum(1 for x in range(N) if x % p in (0, 1)), N)
               for p in ps}
    for S in subsets(ps):
        if not S:
            continue
        evidence = reduce(lambda a, b: a * b,
                          (Fraction(p, 2) for p in sorted(S)), Fraction(1))
        C = [x for x in range(N) if all(x % p in (0, 1) for p in S)]
        # payoff region = delta-support read: C_S = {supp delta(x) ^ S = 0}
        delta_read = [x for x in range(N)
                      if all((x * x - x) % p == 0 for p in S)]
        ok_delta = ok_delta and C == delta_read
        ok_mean = ok_mean and Fraction(len(C), N) * evidence == 1
        # channel independence (the real factorization content --
        # pointwise E_cl_S = prod E_cl_{p} is true by definition):
        # P(C_S) = prod_{p in S} P(C_{p})
        ok_factor = ok_factor and Fraction(len(C), N) == reduce(
            lambda a, b: a * b, (singles[p] for p in sorted(S)), Fraction(1))
        # collapse: E_cl_S(x^lambda) = evidence for EVERY x
        ok_collapse = ok_collapse and all(
            pow(x, lam, N) % p in (0, 1)
            for x in range(N) for p in S)
        collapse_means[(N, frozenset(S))] = evidence

report("C_S = {supp delta(x) disjoint from S}: the e-variable reads delta",
       ok_delta, "delta(x) = x^2 - x; exhaustive Z/30 + Z/210, all S")
report("E_cl_S = 1[C_S] prod_S p/2 has mean exactly 1, all S", ok_mean,
       "|C_S| enumerated vs the closed form N prod_S 2/p")
report("classicality events independent across channels: P(C_S) = prod P(C_p)",
       ok_factor)

# The product rule across families: read-sets must be disjoint.
# cylinder reads S^c; classicality reads S. Verify all three pair types.
ok_rule = True
for ps in [ps3, ps4]:
    N = primorial(ps)
    full = frozenset(ps)
    cyl, _ = cylinder_data(ps)
    cls = {}
    for S in subsets(ps):
        ev = reduce(lambda a, b: a * b,
                    (Fraction(p, 2) for p in sorted(S)), Fraction(1))
        cls[S] = ([x for x in range(N) if all(x % p in (0, 1) for p in S)],
                  ev)
    two = frozenset({2})
    for S in subsets(ps):
        for T in subsets(ps):
            # classicality x classicality: valid iff (S^T) subset {2}
            # (channel 2's classicality is vacuous -- the trivial bet)
            CS, evS = cls[S]
            CT, evT = cls[T]
            both = [x for x in CS if x in set(CT)]
            mean = Fraction(len(both), N) * evS * evT
            if (mean <= 1) != ((S & T) <= two):
                ok_rule = False
            # mixed cylinder(S) x classicality(T): valid iff T subset S u {2}
            A_S, mu_S = cyl[S]
            mixed = [x for x in A_S if all(x % p in (0, 1) for p in T)]
            mean = Fraction(len(mixed), N) / mu_S * evT
            if (mean <= 1) != (T <= S | two):
                ok_rule = False

report("product rule, all three pair types: e-valid <=> EFFECTIVE read-sets"
       " disjoint", ok_rule,
       "cyl reads S^c, cls reads S\\{2} (channel 2 = the vacuous bet)")

ex = collapse_means[(210, frozenset({2, 3, 5, 7}))]
report("collapse fabricates: E_cl_S(x^lambda) = prod_S p/2 for EVERY x",
       ok_collapse, f"e.g. Z/210, S = all: mean post-collapse = {ex} > 1")

# ---------------------------------------------------------------- V

section("V. THE MERGE ASYMMETRY (temperature axis vs evidence axis)")

# Merge M(E1, E2) over all cylinder pairs: exact means via region algebra.
# Regions for (E_S, E_T): A_I (both pay), A_S\A_I, A_T\A_I, rest.
def merge_means(ps, merge):
    N = primorial(ps)
    cyl, _ = cylinder_data(ps)
    means = {}
    for S, (A_S, mu_S) in cyl.items():
        for T, (A_T, mu_T) in cyl.items():
            A_I = A_S & A_T
            a, b = 1 / mu_S, 1 / mu_T
            m = (Fraction(len(A_I), N) * merge(a, b)
                 + Fraction(len(A_S) - len(A_I), N) * merge(a, Fraction(0))
                 + Fraction(len(A_T) - len(A_I), N) * merge(Fraction(0), b)
                 + Fraction(N - len(A_S) - len(A_T) + len(A_I), N)
                 * merge(Fraction(0), Fraction(0)))
            means[(S, T)] = m
    return means

def harmonic(a, b):
    return Fraction(0) if (a == 0 or b == 0) else 2 / (1 / a + 1 / b)

ok_min = ok_har = ok_ari = True
worst = {}
for ps in [ps3, ps4]:
    ok_min = ok_min and all(m <= 1 for m in merge_means(ps, min).values())
    ok_har = ok_har and all(m <= 1 for m in merge_means(ps, harmonic).values())
    ari = merge_means(ps, lambda a, b: (a + b) / 2)
    ok_ari = ok_ari and all(m == 1 for m in ari.values())
    mx = merge_means(ps, max)
    worst[primorial(ps)] = max(mx.values())

report("min-merge and harmonic-merge e-valid on ALL cylinder pairs",
       ok_min and ok_har, "q <= 1 valid (power-mean <= arithmetic, classical)")
report("arithmetic merge exactly tight: mean = 1 on every pair", ok_ari,
       "the Vovk-Wang canonical merge, exact on the ring")

# quadratic merge q = 2: exact rational lower bound on the mean > 1.
from math import isqrt

def sqrt_lb(fr):
    """Rational lower bound for sqrt of a nonneg Fraction (exact)."""
    scale = 10 ** 12
    return Fraction(isqrt(fr.numerator * fr.denominator * scale * scale),
                    fr.denominator * scale)

ps = ps4
N = primorial(ps)
cyl, _ = cylinder_data(ps)
S, T = frozenset({2, 3, 5}), frozenset({2, 3, 7})
A_S, mu_S = cyl[S]
A_T, mu_T = cyl[T]
a, b = 1 / mu_S, 1 / mu_T
A_I = A_S & A_T
mean_lb = (Fraction(len(A_I), N) * sqrt_lb((a * a + b * b) / 2)
           + Fraction(len(A_S) - len(A_I), N) * sqrt_lb(a * a / 2)
           + Fraction(len(A_T) - len(A_I), N) * sqrt_lb(b * b / 2))
ok = mean_lb > 1
report("quadratic merge (q = 2) INVALID: exact witness with mean > 1", ok,
       f"S={{2,3,5}}, T={{2,3,7}} at Z/210: mean > "
       f"{int(mean_lb * 1000) / 1000:.3f} (a lower bound, rounded down)")

# general: mean(max(E_S, E_T)) = 2 - mu(S^T) * min(1/mu_S, 1/mu_T)
# <= 2 - 1/N (min(1/mu) >= 1; mu(S^T) >= 1/N since 0 is in every A);
# attained at S = full (E_S = 1), T = empty (the point mass at 0)
ok = (worst[30] == 2 - Fraction(1, 30)
      and worst[210] == 2 - Fraction(1, 210))
report("max-merge worst mean = 2 - 1/N exactly (59/30, 419/210) -> 2", ok,
       "the tropical merge fabricates; min only loses -- one-directional")

# ---------------------------------------------------------------- VI

section("VI. RANK READS THE SPLIT, NOT THE MODE (the sorting question)")

# Machinery. Flattening R at a channel bipartition S | rest gives the
# matrix M[(residue pairs on S)][(residue pairs on the rest)] = R(x,y);
# CRT fills every entry exactly once. Hand-proofs in the rank-sorting
# record block of the docstring; this section is the mechanical confirmation.

import math

def flatten_split(ps, S, rel):
    """M + row/col index maps at the bipartition S | ps\\S."""
    N = primorial(ps)
    inS = [p in S for p in ps]
    rows, cols, data = {}, {}, {}
    for x in range(N):
        for y in range(N):
            r = tuple((x % p, y % p) for p, f in zip(ps, inS) if f)
            c = tuple((x % p, y % p) for p, f in zip(ps, inS) if not f)
            ri = rows.setdefault(r, len(rows))
            ci = cols.setdefault(c, len(cols))
            data[(ri, ci)] = 1 if rel(x, y) else 0
    M = [[0] * len(cols) for _ in range(len(rows))]
    for (i, j), v in data.items():
        M[i][j] = v
    return M, rows, cols

def dedup(M):
    """Distinct nonzero rows, then distinct nonzero cols. Duplicate and
    zero lines change neither real nor Boolean rank; the result is
    small enough for exact work."""
    rows = [t for t in dict.fromkeys(tuple(r) for r in M) if any(t)]
    if not rows:
        return [[0]]
    cols = [t for t in dict.fromkeys(zip(*rows)) if any(t)]
    if not cols:
        return [[0]]
    return [list(r) for r in zip(*cols)]

def is_rectangle(M):
    """Boolean rank <= 1: ones exactly on (row support) x (col support)."""
    rs = [i for i, row in enumerate(M) if any(row)]
    if not rs:
        return True
    cs = [j for j in range(len(M[0])) if any(M[i][j] for i in rs)]
    return all(M[i][j] for i in rs for j in cs)

def conj_mode(ps, rel):
    """The relations chart's verdict: conjunctive / maximal / proper."""
    N = primorial(ps)
    proj = [set() for _ in ps]
    nR = 0
    for x in range(N):
        for y in range(N):
            if rel(x, y):
                nR += 1
                for i, p in enumerate(ps):
                    proj[i].add((x % p, y % p))
    nC = sum(1 for x in range(N) for y in range(N)
             if all((x % p, y % p) in proj[i] for i, p in enumerate(ps)))
    if nC == nR:
        return "conjunctive"
    sat = all(len(proj[i]) == p * p for i, p in enumerate(ps))
    return "maximal" if sat else "proper"

def fold_matrix(ps, S, Dset):
    """T_D at the bipartition: rank of a difference-invariant relation's
    flattening folds onto this prod_S p x prod_rest p matrix."""
    a = primorial(sorted(S))
    b = primorial([p for p in ps if p not in S])
    return [[1 if crt([a, b], [u, v]) in Dset else 0 for v in range(b)]
            for u in range(a)]

def ordp(r, p):
    """Multiplicative order in F_p^*; 0 contributes 1 (the chart's
    convention: the powering cycle of 0 has length 1)."""
    if r == 0:
        return 1
    t, a = 1, r % p
    while a != 1:
        a = a * r % p
        t += 1
    return t

def period_table(ps):
    N = primorial(ps)
    return [math.lcm(*(ordp(x % p, p) for p in ps)) for x in range(N)]

PER30 = period_table(ps3)
grading30 = lambda x, y: PER30[y] % PER30[x] == 0
order30 = lambda x, y: x < y

def circ_rel(d, N):
    return lambda x, y: min((x - y) % N, (y - x) % N) <= d

# (a) the criterion, mechanically, both directions, over the census:
# conjunctive <=> Boolean rank <= 1 (= rectangle) at EVERY single split.
census = [("equality", lambda x, y: x == y, "conjunctive"),
          ("divisibility", divides(ps3), "conjunctive"),
          ("order", order30, "maximal"),
          ("grading", grading30, "proper")]
census += [(f"R_{d}", circ_rel(d, 30),
            "conjunctive" if d == 0 else ("proper" if d == 1 else "maximal"))
           for d in range(15)]
ok = True
split_rank = {}
for name, rel, expected in census:
    mode = conj_mode(ps3, rel)
    ok = ok and mode == expected
    all_rect = True
    for p in ps3:
        M, _, _ = flatten_split(ps3, {p}, rel)
        r = frac_rank(dedup(M))
        split_rank[(name, p)] = r
        all_rect = all_rect and is_rectangle(M) and r <= 1
    ok = ok and (all_rect == (mode == "conjunctive"))
report("criterion: conjunctive <=> rank <= 1 at every single split", ok,
       "19-relation census at Z/30 (4 candidates + R_0..R_14), modes as charted")

# (c) proper failure at split rank 1: the grading's {2}-split.
M2, _, _ = flatten_split(ps3, {2}, grading30)
ok = (conj_mode(ps3, grading30) == "proper" and is_rectangle(M2)
      and split_rank[("grading", 2)] == 1)
report("PROPER-failing grading is a RECTANGLE at the {2}-split (rank 1)", ok,
       "channel 2 is a dummy coordinate: the relation splits off the full square")

# (b) the fold lemma + the family: rank(flatten) == rank(fold), capped.
ok_fold = True
for d in range(15):
    rel = circ_rel(d, 30)
    Dset = {z for z in range(30) if min(z, 30 - z) <= d}
    for p in ps3:
        M, _, _ = flatten_split(ps3, {p}, rel)
        T = fold_matrix(ps3, {p}, Dset)
        rM, rT = frac_rank(dedup(M)), frac_rank(dedup(T))
        cap = min(len(T), len(T[0]))
        full = min(p * p, (30 // p) ** 2)
        ok_fold = ok_fold and rM == rT and rM <= cap and cap < full
report("fold lemma: rank(flatten) = rank(difference fold) <= cap < full", ok_fold,
       "all 15 d-values x 3 splits at Z/30: difference-invariance forbids full rank")

ok = split_rank[("R_1", 2)] == 2 == split_rank[("R_2", 2)]
report("the mode crosses (proper d=1 -> maximal d=2), the rank does not move",
       ok, "{2}-split rank 2 = 2, full = 4")

# (b) witness at the rank coda's own rung: R_1 at Z/6 is maximal, rank 2.
ps2 = [2, 3]
rel6 = circ_rel(1, 6)
M6, _, _ = flatten_split(ps2, {2}, rel6)
ok = (conj_mode(ps2, rel6) == "maximal"
      and frac_rank(dedup(M6)) == 2 and boolean_rank(M6) == 2)
report("Z/6 (the coda's rung): |x-y|_circ <= 1 fails MAXIMALLY at rank 2/2",
       ok, "Boolean and real, full = 4: maximal does NOT force full rank")

# (d) the zero-row cap + the named gap: the grading's actual ranks.
M5, rows5, _ = flatten_split(ps3, {5}, grading30)
zero5 = {r for r, i in rows5.items() if not any(M5[i])}
r5 = frac_rank(dedup(M5))
r3 = split_rank[("grading", 3)]
ok = ((2, 1),) in zero5 and r5 < 25
report(f"grading at Z/30: {{5}}-split rank {r5} of 25 ({len(zero5)} zero rows),"
       f" {{3}}-split rank {r3} of 9", ok,
       "the witness pair (2,1) is a zero row -- the cap is the true fragment")

PER210 = period_table(ps4)
grading210 = lambda x, y: PER210[y] % PER210[x] == 0
g210 = {}
for p in ps4:
    M, rows, _ = flatten_split(ps4, {p}, grading210)
    g210[p] = (frac_rank(dedup(M)), is_rectangle(M),
               {r for r, i in rows.items() if not any(M[i])})
ok = (conj_mode(ps4, grading210) == "proper"
      and g210[2][0] == 1 and g210[2][1]
      and all(g210[p][0] == 3 for p in [3, 5, 7])
      and (len(g210[3][2]), len(g210[5][2]), len(g210[7][2])) == (0, 6, 12)
      and ((3, 1),) in g210[7][2])
report("grading at Z/210, all splits: {2} rank 1 (rectangle), {3}/{5}/{7}"
       " rank 3 of 9/25/49", ok,
       "zero rows 0/6/12, the chart's witness (3,1) among the {7}-split's;"
       " proper failure caps its own split")

# (e) what full rank detects: the lift. Order exceeds the fold cap.
oranks = {p: split_rank[("order", p)] for p in ps3}
ok = oranks[2] > 2 and oranks[3] > 3 and oranks[5] > 5
report(f"order's split ranks at Z/30: {oranks} exceed the fold caps 2/3/5", ok,
       "above-cap certifies non-difference-invariance; order's is the lift")

# ---------------------------------------------------------------- summary

section("SUMMARY")
n_ok = sum(1 for _, ok in PASS if ok)
print(f"  {n_ok}/{len(PASS)} checks pass   "
      f"({time.perf_counter() - T0:.1f} s)")
if n_ok == len(PASS):
    print("  ALL GREEN")
else:
    for label, ok in PASS:
        if not ok:
            print(f"  FAILED: {label}")
