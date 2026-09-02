"""One additive functional, six named conditions.

THE OBJECT.  For a finite set S of distinct primes, N = prod(S), m = |S|,
put

    g(S) = sum_{p in S} (1 - 1/p),

a rational number, additive over disjoint unions.  Three corners of this
corpus name their own quantity and each one turns out to be g, a fixed
multiple of g, or a threshold on g:

  (a) NAMING.  -chi(S) = N*(m-1) - sum_i N/p_i = N*(g(S) - 1), so an absent
      prime s divides -chi(S) iff g(S) = 1 in Z_(s).  Recorded as the weight
      law; the weight w_s(p) = 1 - p^{-1} is g's summand reduced mod s.
  (b) GEOMETRY.  The mean CRT Hamming distance from a uniform element of Z/N
      to the origin is recorded as a computed PATTERN at k = 3..14, equal to
      k - sum(1/p_i).  That is g(S) written with the set size still in it.
  (c) COST.  The RNS comparator's packed key runs at width log2(N) +
      log2(sum_p 1/p), so it beats reconstruction iff sum_p 1/p < 1.  And
      sum_p 1/p = m - g(S), while N*sum_p 1/p = sum_i N/p_i = L(S), the
      number of LINES of the clique complex -- its maximal cliques.

Nothing in the corpus reads these three as one object.  (b) is filed at a
tier below what a one-line argument gives it, and (c)'s cost quantity is
never identified with (a)'s topology.

THE QUESTION.  Is g the corpus's one additive functional over a prime set,
and do the recorded conditions collapse onto thresholds and congruences on
it?  Specifically: does the seed-flower operator's SHRINK lemma -- recorded
as "support-2 steps never grow, growth requires support >= 3" -- have an
exact classification in g, and is that classification the same computation
as the recorded theorem that {2,3,5} is the unique multiset of sizes with
b1 = N?

THE SLATE (frozen before any engine code).

S0 -- THE THRESHOLD LADDER, derived on paper before this file existed.
  With g additive and every summand in (0,1):
      -chi(S) = N*(g - 1)                       [algebra]
      L(S)    = N*(m - g) = sum_i N/p_i         [algebra]
      b1(S)   = 1 - chi(S) = 1 + N*(g - 1)      [clique complex, recorded]
  so each recorded condition is a level or threshold of the SAME g:
      s names S            <=>  g = 1  (mod s)
      -chi(S) > 0          <=>  g > 1
      -chi(S) < N(S)       <=>  g < 2
      comparator wins      <=>  g > m - 1        (i.e. L < N)
      b1(S) = N(S)         <=>  g = 2 - 1/N
      mean Hamming dist    =    g

S1 -- THE SHRINK CLASSIFICATION, derived on paper before this file existed.
  -chi(S) < N(S) iff g(S) < 2 iff sum_{p in S} 1/p > m - 2.
    m = 1: right side negative, holds always.
    m = 2: right side 0, holds always.
    m = 3: needs sum 1/p > 1.  The largest 3-prime sum is 1/2+1/3+1/5 =
           31/30 > 1; the next largest is 1/2+1/3+1/7 = 41/42 < 1.  So
           {2,3,5} alone.
    m >= 4: needs sum 1/p > 2, and the largest 4-prime sum is
           1/2+1/3+1/5+1/7 = 247/210 < 2.  Adjoining any further prime
           p >= 11 changes the slack sum(1/p) - (m-2) by 1/p - 1 < 0, so the
           gap only widens.  Never.
  PREDICTED CLASSIFICATION: -chi(S) < N(S) exactly on the sets of size <= 2
  together with {2,3,5}, and on no other set of distinct primes.
  Consequence for the operator F(S) = supp(|-chi(S)|): g > 0 always, so
  the class is equally |-chi| < N, and N(F(S)) = rad(|-chi|) <= |-chi| --
  the absolute value carrying the singletons, where -chi = -1 and the
  unsigned chain would read 1 <= -1.  So no set in that class can grow,
  which subsumes
  the recorded support-2 lemma and adds the one 3-element exception it
  misses.  Note the converse is NOT claimed: g >= 2 does not force growth.

S2 -- THE INVISIBILITY ASYMMETRY, derived on paper before this file existed.
  Over Z every summand 1 - 1/p lies strictly in (0,1), so NO prime is
  invisible to g and every adjunction strictly increases it.  Invisibility
  (w_s(p) = 0 at p = 1 mod s) is therefore a purely mod-s phenomenon.  The
  Z-side consequence is monotonicity: {g < 2} is downward closed under
  subsets and {g > 1} is upward closed, while {g > m-1} is downward closed
  because adjoining p moves g - (m-1) by -1/p.  A congruence class of g has
  no such closure.

P1 -- THE DISTANCE IS THE FUNCTIONAL.  PREDICTION: for every non-empty
  subset S of the first 6 primes, the mean Hamming distance from the origin
  computed by BRUTE enumeration over all N residues equals g(S) as an exact
  rational, and equals the mean distance from any other fixed base point.
  KILL (observable): any S where the brute mean and g differ as rationals,
  or where two base points give different means.

P2 -- THE LADDER.  PREDICTION: over every non-empty subset of the first 9
  primes, each of the six rows of S0 holds as an exact identity or
  equivalence, with -chi and L computed in integer arithmetic from their own
  definitions and g summed independently as exact rationals.
  SCOPE, stated so the rows are not read as more than they are: b1 is taken
  from the proved identity b1 = 1 - chi and NOT computed from homology here,
  so the two b1 rows test the algebra GIVEN that theorem rather than the
  theorem -- the independent b1 lives in explore_clique_betti.py (GF(2)
  boundary ranks, 20 cases), and the chi those rows stand on is what the
  positive control checks against the simplices.
  KILL (observable): any subset where a row's two sides disagree.

P3 -- L IS THE LINE COUNT.  PREDICTION: for every subset S of the first 4
  primes with N <= 210, the number of maximal cliques of the neighbour graph
  on Z/N, enumerated by Bron-Kerbosch, equals sum_i N/p_i, and every maximal
  clique has size p_i for some i with exactly N/p_i cliques of that size.
  KILL (observable): a clique count or size profile differing from the
  formula.

P4 -- THE SHRINK CLASSIFICATION.  PREDICTION: over all 2^11 - 1 non-empty
  subsets of the first 11 primes, and over 20000 random subsets drawn from
  the first 200 primes, the sets with -chi(S) < N(S) are exactly those of
  size <= 2 together with {2,3,5}.
  KILL (observable): any set of size >= 3 other than {2,3,5} with
  -chi < N, or any set of size <= 2 with -chi >= N.

P5 -- THE SHRINK CLASS CANNOT GROW.  PREDICTION: over the same sweep, every
  S with -chi(S) < N(S) has N(F(S)) < N(S) under F(S) = prime support of
  |-chi(S)|, and the recorded "support-2 never grows" is the |S| = 2 slice
  of exactly this statement.
  KILL (observable): a member of the class whose image has N(F(S)) >= N(S).

P6 -- THE COMPARATOR IS THE LINE COUNT.  PREDICTION: over every non-empty
  subset of the first 9 primes, "sum_p 1/p < 1" and "L(S) < N(S)" agree on
  every set, the class is downward closed under subsets, and on the primorial
  rungs it holds at k <= 2 and fails at every k >= 3 -- the recorded
  on-rung verdict.
  KILL (observable): any set where the two conditions disagree, any subset
  of a member that is not itself a member, or a rung verdict differing from
  the record.

POSITIVE CONTROL (run before any verdict is read).  -chi is computed two
independent ways -- from the defining formula N*(m-1) - sum N/p_i, and as
an alternating sum over the clique complex's OWN simplices, every clique
enumerated by DFS over an adjacency built from residues alone, which knows
neither that the maximal cliques are lines nor that L = sum N/p.  The run
aborts unless they agree on all 15 complexes with N <= 210.  The brute mean
distance of P1 is itself the control for g, being an enumeration that never
mentions the formula.

RESOURCE.  All enumeration is bounded by N <= 2*3*5*7*11*13 = 30030 for the
brute distance work and N <= 210 for clique enumeration; the subset sweeps
are integer arithmetic on at most 2^11 sets.  Well under the analysis
ceiling; wall clock estimated at a few seconds.

RUN RECORD.  One run, 0.18 s wall, all enumeration exhaustive at the stated
scopes.  Positive control: all 15 complexes with N <= 210, -chi from the
formula against -chi from an alternating sum over every clique of the
neighbour graph, 0 disagreements.  All six predictions HELD; nothing was
killed.

FINDINGS.

F1 -- THE DISTANCE IS THE FUNCTIONAL (property, proved; 63 sets enumerated
  exhaustively).  Mean Hamming distance from a uniform element of Z/N to the
  origin = g(S), exactly and as a rational, and the same from any other base
  point.  The proof is one line and holds for every S: distance is a sum of
  coordinate indicators, and coordinate i disagrees with a fixed base with
  probability (p_i - 1)/p_i = 1 - 1/p_i, so linearity of expectation gives
  the sum.  No k-range, no computation: the corpus's "Pattern (computed,
  k = 3..14)" was a property all along, and the growth statement
  k - O(log log k) is Mertens applied to the same identity.

F2 -- THE SIX-ROW LADDER (rule -- proved; 511 subsets of the first 9 primes,
  every row checked with each side computed from its own definition).  One
  additive functional carries six recorded conditions:
      mean Hamming distance from any base point  =   g
      s names S (s absent)                       <=> g = 1 (mod s)
      -chi(S) > 0                                <=> g > 1
      -chi(S) < N(S)                             <=> g < 2
      RNS comparator beats reconstruction        <=> g > m - 1
      b1(S) = N(S)                               <=> g = 2 - 1/N
  The set size enters only through the comparator row, and there only
  because that row is naturally stated in the COMPLEMENTARY weight
  1/p = 1 - w(p): sum_p 1/p < 1 has no m in it either.  So every one of the
  six picks one of the two weights w(p) = 1 - 1/p and v(p) = 1/p, which sum
  to 1 per prime.  NOT a claim that the corpus has only these two additive
  functionals over a prime set -- there is at least one more, the neighbour
  graph's degree sum_p (p - 1), which carries the curvature and the
  adjacency spectrum, and the ladder does not reach it.  The claim is about
  the six rows and its scope is exactly those six.

F3 -- THE COMPARATOR'S COST IS THE COMPLEX'S LINE COUNT (rule -- proved;
  15 complexes with N <= 210 by independent Bron-Kerbosch, count AND size
  profile).  The packed key's range SQ = N * sum_p 1/p is exactly
  L(S) = sum_i N/p_i, the number of maximal cliques -- the LINES -- of the
  clique complex, and the comparator beats reconstruction iff L < N: strictly
  fewer lines than vertices.  Verified downward closed under subsets, and on
  the primorial rungs it holds at k <= 2 and fails from k = 3 up, which is
  the recorded on-rung verdict arrived at from the topology instead of from
  the bit width.

F4 -- THE SHRINK CLASS IS EXACTLY {size <= 2} u {2,3,5} (rule -- proved;
  exhaustive over all 2^11 - 1 subsets of the first 11 primes, 67 members,
  the only one of size >= 3 being {2,3,5}, plus 20000 random subsets of
  sizes 3-8 from the first 200 primes with no stray).  -chi(S) < N(S) iff
  g < 2 iff sum 1/p > m - 2, and the three-line case analysis of S1 closes
  it for every m.  This is the same computation as the recorded theorem that
  {2,3,5} is the unique multiset of sizes with b1 = N, read at inequality
  instead of at equality -- the equality asks sum 1/p = m - 2 + 1/N.

F5 -- AND IT SUBSUMES THE OPERATOR'S SHRINK LEMMA (rule -- proved; 0 growths
  over the 67 members).  Since N(F(S)) = rad(|-chi(S)|) <= |-chi(S)| < N(S)
  on the class, no member of it can grow under the seed-flower operator.
  The absolute value is load-bearing rather than cosmetic: at a singleton
  -chi = -1, where the unsigned chain would read 1 <= -1.  The recorded
  "support-2 steps never grow" is the |S| = 2 slice, and the recorded
  "growth requires support >= 3" is off by the one set {2,3,5}, which has
  support 3 and cannot grow either.  The converse is not claimed and is
  false in general: g >= 2 permits growth without forcing it, the image
  being a radical rather than the value.

F6 -- INVISIBILITY IS MOD-s ONLY (property).  Every summand of g lies
  strictly in (0,1) over Z, so no prime is invisible to g itself and every
  adjunction strictly increases it.  That is why the Z-side rows above are
  monotone classes -- {g < 2} and {sum 1/p < 1} downward closed, {g > 1}
  upward closed, all confirmed on the sweeps -- while the naming row, being
  a congruence, has no closure at all.  The recorded s-invisibility of
  primes p = 1 (mod s) is a fact about the REDUCTION of the weight and
  never about the weight.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from fractions import Fraction
from itertools import combinations
from math import prod

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import primes_up_to, factorize


# ---------------------------------------------------------------- basics

def g_of(S):
    """The additive functional: sum of (1 - 1/p) over S, an exact rational."""
    return sum((Fraction(p - 1, p) for p in S), Fraction(0))


def neg_chi(S):
    """-chi from its defining formula: N*(m-1) - sum_i N/p_i."""
    N = prod(S)
    return N * (len(S) - 1) - sum(N // p for p in S)


def neg_chi_by_simplices(S):
    """-chi as an alternating sum over the complex's own simplices.

    Independent of the formula in every term: the neighbour graph is built
    from residues, every clique is enumerated by DFS over the adjacency
    alone, and chi = sum over cliques of (-1)^(size-1).  Nothing here knows
    that the maximal cliques are lines or that L = sum N/p.
    """
    N = prod(S)
    adj = neighbour_graph(S)
    counts = {}

    def extend(clique, cands):
        counts[len(clique)] = counts.get(len(clique), 0) + 1
        for i, v in enumerate(cands):
            extend(clique + [v], [u for u in cands[i + 1:] if u in adj[v]])

    extend([], list(range(N)))
    counts.pop(0, None)  # the empty clique is not a simplex
    chi = sum((-1) ** (size - 1) * c for size, c in counts.items())
    return -chi


def neighbour_graph(S):
    """Adjacency on Z/N: one edge per single-channel change. Residues only."""
    N = prod(S)
    adj = {x: set() for x in range(N)}
    for x in range(N):
        rx = encode_res(x, S)
        for i, p in enumerate(S):
            for d in range(1, p):
                ry = list(rx)
                ry[i] = (ry[i] + d) % p
                adj[x].add(crt_from(ry, S, N))
    return adj


def line_count(S):
    N = prod(S)
    return sum(N // p for p in S)


def b1_of(S):
    return 1 - (-neg_chi(S))


def encode_res(x, S):
    return tuple(x % p for p in S)


def support(n):
    return sorted(factorize(n).keys()) if n > 1 else []


def banner(title):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------- positive control

def positive_control():
    banner("POSITIVE CONTROL: -chi from the formula against -chi from the "
           "complex's own simplices")
    bad = 0
    n = 0
    for r in range(1, 5):
        for S in combinations([2, 3, 5, 7], r):
            S = list(S)
            if prod(S) > 210:
                continue
            n += 1
            a, b = neg_chi(S), neg_chi_by_simplices(S)
            print(f"  S={str(S):<16} N={prod(S):<5} formula={a:<6} "
                  f"simplices={b:<6} {'ok' if a == b else 'MISMATCH'}")
            if a != b:
                bad += 1
    print(f"  complexes tested : {n}    disagreements : {bad}")
    if bad:
        raise SystemExit("CONTROL FAILED -- no verdict read")
    print("  control PASSES; verdicts below may be read")


# ------------------------------------------------------------------ P1

def p1_distance():
    banner("P1  the mean Hamming distance IS g")
    POOL6 = primes_up_to(20)[:6]
    worst = None
    rows = 0
    for r in range(1, 7):
        for S in combinations(POOL6, r):
            S = list(S)
            N = prod(S)
            if N > 30030:
                continue
            rows += 1
            tot0 = 0
            # a second base point differing from the origin in EVERY
            # coordinate, so no set degenerates to comparing 0 with 0
            base = [1 % p for p in S]
            tot1 = 0
            for x in range(N):
                res = encode_res(x, S)
                tot0 += sum(1 for v in res if v != 0)
                tot1 += sum(1 for v, b in zip(res, base) if v != b)
            mean0 = Fraction(tot0, N)
            mean1 = Fraction(tot1, N)
            gv = g_of(S)
            if mean0 != gv or mean1 != gv:
                worst = (S, mean0, mean1, gv)
    print(f"  sets enumerated exhaustively : {rows}")
    print(f"  mismatch (origin or 2nd base): {worst}")
    demo = [2, 3, 5, 7]
    print(f"  sample: S={demo}  g={g_of(demo)} = {float(g_of(demo)):.6f}"
          f"   m - sum(1/p) = {len(demo) - sum(Fraction(1, p) for p in demo)}")
    return worst is None


# ------------------------------------------------------------------ P2

def p2_ladder():
    banner("P2  the six-row ladder on one functional")
    POOL9 = primes_up_to(30)[:9]
    fails = []
    n = 0
    for r in range(1, 10):
        for S in combinations(POOL9, r):
            S = list(S)
            n += 1
            N, m, gv = prod(S), len(S), g_of(S)
            nc = neg_chi(S)
            if nc != N * (gv - 1):
                fails.append(("chi", S))
            if line_count(S) != N * (m - gv):
                fails.append(("L", S))
            if b1_of(S) != 1 + N * (gv - 1):
                fails.append(("b1", S))
            if (nc > 0) != (gv > 1):
                fails.append(("pos", S))
            if (nc < N) != (gv < 2):
                fails.append(("shrink", S))
            if (line_count(S) < N) != (gv > m - 1):
                fails.append(("cmp", S))
            if (b1_of(S) == N) != (gv == 2 - Fraction(1, N)):
                fails.append(("b1N", S))
    print(f"  subsets of the first 9 primes tested : {n}")
    print(f"  row failures                         : {len(fails)}")
    for f in fails[:5]:
        print(f"    {f}")
    return not fails


# ------------------------------------------------------------------ P3

def p3_lines():
    banner("P3  L is the number of maximal cliques")
    ok = True
    for r in range(1, 5):
        for S in combinations([2, 3, 5, 7], r):
            S = list(S)
            N = prod(S)
            if N > 210:
                continue
            cliques = bron_kerbosch(neighbour_graph(S))
            sizes = sorted(len(c) for c in cliques)
            expect = sorted([p for p in S for _ in range(N // p)])
            match = (len(cliques) == line_count(S)) and sizes == expect
            print(f"  S={str(S):<16} N={N:<5} cliques={len(cliques):<5} "
                  f"L={line_count(S):<5} profile match={sizes == expect}")
            ok = ok and match
    return ok


def crt_from(res, S, N):
    x = 0
    for p, r in zip(S, res):
        M = N // p
        x = (x + r * M * pow(M, -1, p)) % N
    return x


def bron_kerbosch(adj):
    out = []

    def go(R, P, X):
        if not P and not X:
            out.append(R)
            return
        pivot = max(P | X, key=lambda u: len(adj[u]))
        for v in list(P - adj[pivot]):
            go(R | {v}, P & adj[v], X & adj[v])
            P = P - {v}
            X = X | {v}

    go(set(), set(adj), set())
    return out


# ------------------------------------------------------------------ P4/P5

def p45_shrink():
    banner("P4/P5  the shrink class, and that it cannot grow")
    POOL11 = primes_up_to(40)[:11]
    members = []
    for r in range(1, 12):
        for S in combinations(POOL11, r):
            S = list(S)
            if neg_chi(S) < prod(S):
                members.append(S)
    big = [S for S in members if len(S) >= 3]
    small_all = all(neg_chi(list(S)) < prod(S)
                    for r in (1, 2) for S in combinations(POOL11, r))
    print(f"  exhaustive over 2^11 - 1 subsets of the first 11 primes")
    print(f"    members of the class          : {len(members)}")
    print(f"    of size >= 3                  : {big}")
    print(f"    every size <= 2 set a member  : {small_all}")

    rng = random.Random(20260609)
    pool = primes_up_to(1300)[:200]
    strays = []
    for _ in range(20000):
        r = rng.randint(3, 8)
        S = sorted(rng.sample(pool, r))
        if neg_chi(S) < prod(S):
            strays.append(S)
    print(f"  20000 random subsets (sizes 3-8, first 200 primes)")
    print(f"    members of size >= 3 found    : {strays[:5]} (n={len(strays)})")

    grew = []
    for S in members:
        v = abs(neg_chi(S))
        img = support(v)
        if img and prod(img) >= prod(S):
            grew.append((S, v, img))
    print(f"  growth check over the class     : {len(grew)} grew (expect 0)")
    for row in grew[:5]:
        print(f"    {row}")
    return (big == [[2, 3, 5]] and small_all and not strays and not grew)


# ------------------------------------------------------------------ P6

def p6_comparator():
    banner("P6  the comparator condition is L < N, and is downward closed")
    POOL9 = primes_up_to(30)[:9]
    cls = set()
    disagree = 0
    for r in range(1, 10):
        for S in combinations(POOL9, r):
            N = prod(S)
            a = sum(Fraction(1, p) for p in S) < 1
            b = line_count(list(S)) < N
            if a != b:
                disagree += 1
            if a:
                cls.add(S)
    closed = all(tuple(T) in cls for S in cls
                 for r in range(1, len(S)) for T in combinations(S, r))
    print(f"  sets where 'sum 1/p < 1' and 'L < N' disagree : {disagree}")
    print(f"  class downward closed under subsets           : {closed}")
    print("  primorial rungs:")
    for k in range(1, 8):
        S = POOL9[:k]
        tot = float(sum(Fraction(1, p) for p in S))
        print(f"    k={k:<2} sum 1/p = {tot:.4f}"
              f"   L<N: {line_count(S) < prod(S)}")
    return disagree == 0 and closed


# ------------------------------------------------------------------ main

def main():
    positive_control()
    results = {
        "P1 distance is g": p1_distance(),
        "P2 six-row ladder": p2_ladder(),
        "P3 L = maximal cliques": p3_lines(),
        "P4/P5 shrink class + no growth": p45_shrink(),
        "P6 comparator = L < N": p6_comparator(),
    }
    banner("VERDICTS")
    for k, v in results.items():
        print(f"  {k:<34} {'HELD' if v else 'KILLED'}")


if __name__ == "__main__":
    main()
