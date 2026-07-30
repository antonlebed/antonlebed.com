"""
THE WALLS PROVENANCE AUDIT -- which obstruction needs which
structure.

The walls corpus measures what the deleted archimedean
place costs. Three of its rules in a row proved generic BELOW the tower
(total orientation hiding = a cyclic-group fact; the Zech wall = a
single-field fact; the channel-quantifier wall = a product fact).
The audit question: pin EVERY wall to the MINIMAL
structure that carries it -- cyclic group + proper quotient / single
field / product of >= 2 windows / product of fields (squarefree) /
primorial trajectory -- by citing the existing proof's hypotheses where
they decide it, and exhibiting the wall (or its failure) on the smaller
structure here where they don't. The deleted-place reading keeps only
what it earns.

Predictions (stated in advance of any run):
  P1. THE SIZE WALL IS A QUOTIENT FACT. The sign bit [x >= N/2] is
      undetermined through EVERY proper window x mod M of EVERY cyclic
      Z/N -- every window fiber contains both signs -- with per-fiber
      bias EXACTLY 0 when c = N/M is even and exactly +-1/2 element
      when c is odd. Prime-power moduli included: no product, no
      fields, no squarefree-ness. (The hiding lemma's "exactly
      zero whenever channel 2 is among the unknowns" is the even-c
      case.)
  P2. THE QUANTIFIER WALL IS A QUOTIENT FACT TOO. No polynomial over
      Z/N computes [a = 0] for ANY composite N: polynomials are
      compatible with every divisor quotient (a == b mod d implies
      f(a) == f(b) mod d), and [a=0] demands 1 == 0 mod d at the pair
      (0, d). At a single field window the wall VANISHES: [a = 0] =
      1 - a^(p-1) (Fermat). This re-homes the product fact one
      level down: the carrier is any nontrivial proper quotient.
  P3. THE TYPE OBSTRUCTION LIVES AT ONE WINDOW. x^y is ill-defined on
      residue pairs already at a single prime field F_p -- exactly the
      p - 2 residues x outside {0, 1} witness, via (y, y + p) -- and
      well-defined as F_p x Z/(p-1) -> F_p. The third wall's TYPE half
      needs no product; its existence grades (Gauss cyclicity, the
      U(2^k) blocker) are classical facts about the index ring one
      level down (cited, not re-run).
  P4. ORDER'S MAXIMAL FAILURE IS A WINDOW-COUNT FACT. The conjunctive
      test kills order at the minimal product Z/6 and at the NON-FIELD
      product Z/36 (windows mod 4 and mod 9) identically: every
      projection saturates. Fields are not needed; two coprime windows
      are.
  P5. THE GRADING IS A SHARED-TORSION GROUP FACT. Over a product
      G_1 x G_2 of finite cyclic groups (exhaustive sweep n_i = 2..10),
      ord(x) | ord(y) is conjunctive iff gcd(exp G_1, exp G_2) = 1;
      when it fails, the mode is PROPER iff some exp(G_i) does not
      divide the other's (a torsion level only one window can supply),
      else MAXIMAL. No ring, no fields, no integers. Ring instances:
      Z/6 (rung 2) PASSES (unit exps 1, 2 coprime), Z/15 and Z/30
      (rung 3) fail properly; the minimal proper carrier is
      C_2 x C_4 = U(15); C_2 x C_2 fails maximally.
  P6. THE SQUAREFREE BOUNDARY. The Clifford identity x^(lambda+1) = x
      fails at Z/4 (witness x = 2): the meadow/Clifford carrier is
      exactly the squarefree locus (full criterion m <= 300 in
      explore_super_log.py; cited).

RESULTS (the record; checks below encode the measured law):
  All six predictions CONFIRMED as stated, first run. P1: every (N, M)
  pair, N <= 240, M | N, 1 <= M < N -- both signs in every fiber, bias
  law exact (|2*count - c| = 0 iff c even, else 1). P2: poly-function
  spaces enumerated whole at N = 4 (64 fns) and N = 6 (the criterion's
  108): [a=0] in neither; compatibility lemma sampled at the five
  moduli N = 4, 6, 12, 30, 60.
  P3: ill-defined witness count = p - 2 exactly at p = 3..13. P4: Z/6
  and Z/36 projections saturate identically. P5: the two-factor law
  holds on all 45 pairs 2 <= n1 <= n2 <= 10; ring verdicts as
  predicted (Z/6 conjunctive; Z/15, Z/30 proper). P6: 2^3 = 0 != 2 in
  Z/4. Later extensions (claim-test alignment): betweenness
  (ternary, plain carrier) verified maximally failing at Z/6 and Z/36
  -- the chart had claimed it on order's evidence alone; and
  C2 x C2 x C2 verified maximal, sealing C2 x C4 as the minimal
  proper carrier among products of cyclic windows (smaller cases all
  in the sweep).

THE PROVENANCE CHART (the deliverable; tier: rule unless noted):
  cyclic group, no product, no     size/sign hiding (sec I; bias law;
  fields (the hiding facts read    reads through a proper window),
  through a proper window)         orientation hiding, the
                                   quantifier wall (sec II -- vanishes
                                   at one field), rigidity's coordinate
                                   census (classical primary decomp.;
                                   no window needed)
  single field (one window)        Zech wall, type obstruction
                                   (sec III), division-ladder floors
                                   (per-channel proofs, CRT lifts
                                   trivially), super-log grades (index
                                   ring one level down; Gauss, U(2^k))
  product of >= 2 windows          order/betweenness maximal failure
  (fields unneeded)                (sec IV), fold/rank caps (the
                                   proof's hypotheses: coprime split +
                                   difference invariance)
  product of two abelian groups    the grading's failure + its mode
  (no ring at all)                 (sec V: shared torsion fails it,
                                   exponent coverage sets the mode;
                                   two cyclic windows, swept whole
                                   n <= 10 + the size-8 cases)
  product of fields (squarefree)   the locality criterion local =
                                   compatible = polynomial (Z/4: 64 of
                                   256 -- explore_size_transform.py),
                                   Clifford/meadow (sec VI boundary
                                   witness; criterion in
                                   explore_super_log.py), Euclid's
                                   loop death, e-calculus carriers
  primorial trajectory             the t = 1 selection ONLY (anchor +
                                   Bertrand gaps) -- no WALL in
                                   the corpus needs the trajectory;
                                   every carrier sits at or below the
                                   squarefree floor, the tower's
                                   purchases are the criterion
                                   (squarefree) and the selection
                                   (trajectory)

Runs exhaustively at small moduli + closed sweeps. ~2 s, ~20 MB.
"""

import math
from itertools import product

def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)

PRIMES = [2, 3, 5, 7, 11, 13]

# ----------------------------------------------------------------------
section("I. THE SIZE WALL IS A QUOTIENT FACT (cyclic + proper window)")
# ----------------------------------------------------------------------
# Sign [x >= N/2] vs the window x mod M, for EVERY cyclic Z/N and every
# proper divisor M (M = 1 is the empty window; M < N proper). Fibers are
# arithmetic progressions {r, r+M, ..., r+(c-1)M}, c = N/M >= 2. The
# ceiling argument gives the exact per-fiber count of sign-1 elements;
# the assertions encode it.
worst_examples = []
for N in range(3, 241):
    thr = (N + 1) // 2                      # x >= N/2  <=>  x >= thr
    for M in (d for d in range(1, N) if N % d == 0):
        c = N // M
        for r in range(M):
            fiber = range(r, N, M)
            ones = sum(1 for x in fiber if x >= thr)
            assert 0 < ones < c             # both signs in EVERY fiber
            assert abs(2 * ones - c) == (0 if c % 2 == 0 else 1)
        if (N, M) in ((4, 2), (8, 4), (9, 3), (27, 9)):
            worst_examples.append((N, M, c))
print("  sign is undetermined through EVERY proper window of EVERY")
print("  cyclic Z/N, N <= 240: both signs in every fiber, per-fiber")
print("  bias exactly 0 (c = N/M even) or 1/2 element (c odd)")
print(f"  prime-power moduli included: {worst_examples} all walled --")
print("  no product, no fields, no squarefree-ness in the carrier;")
print("  the 'exactly zero with channel 2 unknown' case = the even-c case")

# ----------------------------------------------------------------------
section("II. THE QUANTIFIER WALL IS A QUOTIENT FACT (vanishes at a field)")
# ----------------------------------------------------------------------
# (a) At one field window the quantifier is a polynomial: Fermat.
for p in PRIMES:
    assert all((1 - pow(a, p - 1, p)) % p == (1 if a == 0 else 0)
               for a in range(p))
print("  [a = 0] = 1 - a^(p-1) at every prime field p <= 13: at ONE")
print("  window the global quantifier is Fermat's polynomial -- no wall")
# (b) Polynomials are compatible with every divisor quotient (sampled
# whole at small N): a == b mod d  =>  f(a) == f(b) mod d.
import random
random.seed(68)
for N in (4, 6, 12, 30, 60):
    for _ in range(40):
        coeffs = [random.randrange(N) for _ in range(5)]
        f = [sum(cf * pow(a, i, N) for i, cf in enumerate(coeffs)) % N
             for a in range(N)]
        for d in (d for d in range(2, N) if N % d == 0):
            assert all(f[a] % d == f[a % d] % d for a in range(N))
print("  compatibility lemma (sampled, 40 random quintics x 5 moduli):")
print("  every polynomial respects every divisor quotient")
# (c) [a = 0] does not: f(0) = 1 vs f(d) = 0 forces 1 == 0 mod d. So no
# polynomial computes it on ANY composite N. Exhaustive poly-function
# enumeration at N = 4 and N = 6 confirms the argument mechanically.
# Degree <= N-1 spans ALL polynomial functions mod N: the falling
# factorial (x)_N is a product of N consecutive integers, divisible by
# N! hence by N -- it vanishes as a function, and so does every (x)_j,
# j >= N (it contains (x)_N as a prefix), so every monomial x^m, m >= N
# reduces below degree N in the falling-factorial basis.
for N in (4, 6):
    fns = set()
    for coeffs in product(range(N), repeat=N):
        fns.add(tuple(sum(cf * pow(a, i, N) for i, cf in enumerate(coeffs))
                      % N for a in range(N)))
    target = tuple(1 if a == 0 else 0 for a in range(N))
    assert target not in fns
    print(f"  Z/{N}: {len(fns)} polynomial functions enumerated whole --")
    print(f"    [a = 0] is not among them " +
          ("(Z/4 is one prime, one window: the wall" if N == 4 else
           "(the first squarefree case: the wall"))
    print("    needs only the proper quotient, not a product)" if N == 4
          else "    persists where genuine CRT windows begin)")
print("  carrier: any nontrivial proper quotient (composite N) -- the")
print("  the product fact re-homed one level down, same shape as sec I")

# ----------------------------------------------------------------------
section("III. THE TYPE OBSTRUCTION LIVES AT ONE WINDOW (single field)")
# ----------------------------------------------------------------------
# x^y as a function of residue pairs at a SINGLE prime field: the
# exponent slot breaks it. Witness pair (y, y + p): x^(y+p) = x^y * x^p
# = x^y * x, which differs from x^y exactly when x is outside {0, 1}.
for p in PRIMES[1:]:
    bad = [x for x in range(p) if pow(x, 1, p) != pow(x, 1 + p, p)]
    assert bad == [x for x in range(2, p)] and len(bad) == p - 2
    for x in (0, 1):
        assert len({pow(x, y, p) for y in range(1, 3 * p)}) == 1
    # well-typed form: exponents mod p - 1 (y >= 1), all x including 0
    assert all(pow(x, y, p) == pow(x, y + (p - 1), p)
               for x in range(p) for y in range(1, p))
print("  x^y is ill-defined on residue pairs at every prime field")
print("  p = 3..13: exactly the p - 2 residues x outside {0, 1} flip")
print("  under y -> y + p; well-defined as F_p x Z/(p-1) -> F_p.")
print("  The third wall's TYPE half needs no product. Its existence")
print("  grades live one level down in the index ring Z/(p-1) --")
print("  Gauss cyclicity, the U(2^k) blocker: classical, cited")

# ----------------------------------------------------------------------
section("IV. ORDER'S MAXIMAL FAILURE IS A WINDOW-COUNT FACT")
# ----------------------------------------------------------------------
# The conjunctive test through arbitrary coprime windows (no fields
# required): R conjunctive iff R = AND of its window projections.
def conj_report(N, mods, rel, arity=2):
    proj = [set() for _ in mods]
    n_true = 0
    for t in product(range(N), repeat=arity):
        if rel(*t):
            n_true += 1
            for i, m in enumerate(mods):
                proj[i].add(tuple(v % m for v in t))
    n_conj = sum(1 for t in product(range(N), repeat=arity)
                 if all(tuple(v % m for v in t) in proj[i]
                        for i, m in enumerate(mods)))
    saturated = all(len(proj[i]) == m ** arity for i, m in enumerate(mods))
    return n_true, n_conj, saturated

for N, mods in ((6, (2, 3)), (36, (4, 9))):
    n_true, n_conj, sat = conj_report(N, mods, lambda x, y: x <= y)
    assert n_true == N * (N + 1) // 2 and n_conj == N * N and sat
    kind = "minimal product, field windows" if N == 6 else \
           "NON-FIELD windows mod 4 and mod 9"
    print(f"  Z/{N} ({kind}):")
    print(f"    order <= : |R| = {n_true}, conjunction of projections =")
    print(f"    {n_conj} = everything -- every projection saturates:")
    print(f"    the maximal failure, identical in shape at both")
# betweenness, the ternary form (plain carrier relation, no
# distinctness side-condition): btw(a,b,c) = (b-a) % N < (c-a) % N.
for N, mods in ((6, (2, 3)), (36, (4, 9))):
    n_true, n_conj, sat = conj_report(
        N, mods, lambda a, b, c: (b - a) % N < (c - a) % N, arity=3)
    assert n_true == N * N * (N - 1) // 2 and n_conj == N ** 3 and sat
print("  betweenness (ternary, plain carrier): every window projection")
print("  saturates at Z/6 and Z/36 alike -- the same maximal failure")
print("  (added later: claim-test alignment)")
print("  carrier: two coprime windows -- fields play no role in the")
print("  conjunctive kill (the fold/rank caps inherit the same carrier:")
print("  the fold-cap proof's hypotheses are the coprime split + difference")
print("  invariance, never primality)")

# ----------------------------------------------------------------------
section("V. THE GRADING IS A SHARED-TORSION GROUP FACT (no ring at all)")
# ----------------------------------------------------------------------
# ord(x) | ord(y) over a product of two finite cyclic groups C_n1 x C_n2.
# Exhaustive sweep 2 <= n1 <= n2 <= 10; the law:
#   conjunctive      <=>  gcd(n1, n2) = 1          (no shared torsion)
#   else PROPER      <=>  n1 does not divide n2 or n2 does not divide n1
#                          at the relevant factor (exponent coverage)
#   else MAXIMAL.
def group_grading_report(ns):
    elems = list(product(*(range(n) for n in ns)))
    def ordg(t):
        return math.lcm(*(n // math.gcd(n, a) for n, a in zip(ns, t)))
    proj = [set() for _ in ns]
    n_true = 0
    for x in elems:
        for y in elems:
            if ordg(y) % ordg(x) == 0:
                n_true += 1
                for i in range(len(ns)):
                    proj[i].add((x[i], y[i]))
    n_conj = sum(1 for x in elems for y in elems
                 if all((x[i], y[i]) in proj[i] for i in range(len(ns))))
    sat = all(len(proj[i]) == n * n for i, n in enumerate(ns))
    return n_true, n_conj, sat

print("  sweep n1 <= n2 <= 10 (45 group products):")
for n1 in range(2, 11):
    for n2 in range(n1, 11):
        nR, nC, sat = group_grading_report((n1, n2))
        conj = nR == nC
        assert conj == (math.gcd(n1, n2) == 1)
        if not conj:
            proper_pred = (n2 % n1 != 0) or (n1 % n2 != 0)
            # one factor holds an exponent the other cannot cover
            assert (not sat) == proper_pred
print("    law confirmed on all 45: conjunctive <=> gcd(n1, n2) = 1;")
print("    failing mode PROPER <=> exponents not mutually covering")
print("    (n1 != n2 here), MAXIMAL <=> n1 = n2 (each window's torsion")
print("    coverable by the other)")
nR, nC, sat = group_grading_report((2, 2))
assert nR < nC and sat
nR, nC, sat = group_grading_report((2, 4))
assert nR < nC and not sat
nR, nC, sat = group_grading_report((2, 2, 2))
assert nR < nC and sat
print("  C2 x C2: fails MAXIMALLY; C2 x C2 x C2 (the size-8 three-window")
print("  product) also MAXIMAL; C2 x C4: fails PROPERLY -- the minimal")
print("  proper carrier among products of cyclic windows (all smaller")
print("  cases [2,2], [2,3] and the size-8 alternative checked), and")
print("  C2 x C4 = U(15):")
u15 = sorted(min(t for t in range(1, 100)
                 if pow(a, t, 15) == 1) for a in range(15)
             if math.gcd(a, 15) == 1)
c2c4 = sorted(math.lcm(2 // math.gcd(2, i), 4 // math.gcd(4, j))
              for i in range(2) for j in range(4))
assert u15 == c2c4
print(f"    order multisets agree: {u15}")

# ring instances (0 conflated to order 1, the corpus convention):
def ring_grading_report(N, mods):
    def ordm(r, m):
        if math.gcd(r, m) != 1:
            return 1                        # unit-part convention
        t, a = 1, r
        while a != 1:
            a = a * r % m
            t += 1
        return t
    def per(x):
        return math.lcm(*(ordm(x % m, m) for m in mods))
    proj = [set() for _ in mods]
    n_true = 0
    for x in range(N):
        for y in range(N):
            if per(y) % per(x) == 0:
                n_true += 1
                for i, m in enumerate(mods):
                    proj[i].add((x % m, y % m))
    n_conj = sum(1 for x in range(N) for y in range(N)
                 if all((x % m, y % m) in proj[i]
                        for i, m in enumerate(mods)))
    sat = all(len(proj[i]) == m * m for i, m in enumerate(mods))
    return n_true, n_conj, sat

nR, nC, sat = ring_grading_report(6, (2, 3))
assert nR == nC
print("  Z/6 (rung 2): the grading IS conjunctive -- unit exponents")
print("  1 and 2 share no torsion; the rung-2 tower has no grading wall")
for N, mods in ((15, (3, 5)), (30, (2, 3, 5))):
    nR, nC, sat = ring_grading_report(N, mods)
    assert nR < nC and not sat
    print(f"  Z/{N}: fails PROPERLY (unit exponents share 2; the 4-level")
    print(f"    at channel 5 is coverable nowhere else)")
print("  -> on the trajectory the grading wall first appears at rung 3")
print("  (Z/30), because every odd prime brings even unit torsion; the")
print("  wall itself is a finite-abelian-group fact, not a ring fact")

# ----------------------------------------------------------------------
section("VI. THE SQUAREFREE BOUNDARY (what genuinely needs the meadow)")
# ----------------------------------------------------------------------
lam4 = 2                                    # lambda(4)
assert pow(2, lam4 + 1, 4) == 0 != 2
print("  x^(lambda+1) = x fails at Z/4 (witness x = 2, 2^3 = 0): the")
print("  Clifford/meadow blueprint -- and with it Euclid's-loop death,")
print("  the e-calculus carriers, the locality criterion's polynomial")
print("  equation -- lives exactly on the squarefree locus (criterion")
print("  x^(lambda+1) = x <=> m squarefree, validated m <= 300:")
print("  explore_super_log.py; Z/4's 64-of-256 polynomial boundary:")
print("  explore_size_transform.py)")

# ----------------------------------------------------------------------
section("FINDINGS (tier-labeled) -- THE PROVENANCE CHART")
# ----------------------------------------------------------------------
print("""
Each wall pinned to its minimal carrier (rule unless noted):

  CYCLIC GROUP, NO PRODUCT, NO FIELDS (the hiding facts are
  coarsening facts, read through a proper window):
    - size/sign hiding: undetermined through every proper window,
      bias 0 iff N/M even (sec I; exhaustive N <= 240, all windows)
    - orientation hiding: total, every cyclic group (proved)
    - the quantifier wall [a = 0]: no polynomial on any composite N;
      VANISHES at one field (Fermat) (sec II) -- re-homed
    - rigidity's +-local coordinate census: the coprime factorizations
      (classical primary decomposition; no window needed; exhaustive
      k = 3, explore_index_transform.py)

  SINGLE FIELD (one window):
    - the Zech wall (proved: linear-fraction count)
    - the type obstruction x^y (sec III: p - 2 witnesses, no product)
    - the division-ladder floors: nilpotents, meadow split, MP
      decality -- per-channel proofs, CRT lifts trivially
    - super-log existence grades: the index ring one level down
      (Gauss cyclicity, U(2^k) 2-adic blocker -- classical)

  PRODUCT OF >= 2 COPRIME WINDOWS (fields unneeded):
    - order/betweenness maximal conjunctive failure (sec IV: Z/6 and
      non-field Z/36 identical)
    - the fold/rank caps (coprime split + difference invariance)

  PRODUCT OF TWO ABELIAN GROUPS (no ring at all):
    - the grading's failure and its mode (sec V: shared torsion fails
      it -- conjunctive iff gcd of exponents 1; exponent coverage sets
      proper vs maximal; two cyclic windows, swept whole n <= 10 +
      the size-8 cases; minimal proper carrier C2 x C4 = U(15))

  PRODUCT OF FIELDS (squarefree -- the blueprint's own floor):
    - the locality criterion local = compatible = polynomial (thin
      boundary Z/4: 64 of 256)
    - Clifford/meadow, Euclid's-loop death, e-calculus carriers
      (sec VI boundary witness; criterion in explore_super_log.py)

  PRIMORIAL TRAJECTORY:
    - the t = 1 selection alone (2-anchor + Bertrand gaps) --
      NO WALL in the corpus needs the trajectory. Every carrier sits
      at or below the squarefree floor; what the tower buys is the
      criterion (squarefree: channel-parallel = polynomial) and the
      selection theorem (trajectory). The deleted-place reading keeps
      what it earns: the deletion names WHICH window is missing; the
      hiding itself is generic to coarsening.
""")
print("explore_walls_provenance.py: ALL CHECKS PASSED")
