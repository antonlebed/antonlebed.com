"""explore_flatten_offchart.py -- DOES PRODUCT EXTREMALITY SURVIVE OFF
THE EXHAUSTIVE CHART, AND AT HEIGHT >= 2? explore_flatten_height.py's F1
reads the pure-product law across a 92-cell chart plus (15, 2) and
(15, 3), exhaustively and IN RANGE ONLY: its meet-in-the-middle costs
(2k+1)^M, so the k >= 2 rows stop at M <= 16 and the law has never been
asked a question it could fail off-chart.

(FLATTENING, HEIGHT, the FREE BOX and the PURE-PRODUCT family keep
explore_flatten_height.py's senses. A vector c on M atoms is the
polynomial P(x) = sum_r c_r x^r; its moments are m_j = sum_r C(r,j) c_r,
which are its coefficients in the (x-1) basis -- re-derived from the
engine before this slate was frozen: P = sum_r c_r (1+u)^r =
sum_j u^j sum_r C(r,j) c_r with u = x - 1, so the flattening J(c), the
least j with m_j nonzero, IS the multiplicity of the root 1. The HEIGHT
is the sup-norm max_r |c_r|, and h(M, J) is the least height of a
nonzero M-atom vector of flattening >= J.)

THE QUESTION. Is h(M, J) equal to the least height of a pure product
prod_i (x^{d_i} - 1) fitting in M atoms with at least J factors -- at
cells no exhaustive route reaches?

THE HAND ATTACK, worked on paper before any engine code.

FIRST, WHY THE INVERSE IS THE SAME CLAIM. The parent states its law on
the CEILING J*(M, k), the deepest flattening in the free box of height
k; this rig states it on h. The two are inverses --
J*(M, k) = max{J : h(M, J) <= k} -- and both sides are NONDECREASING in
J, h because L_{M,J+1} is contained in L_{M,J}, the product side because
its multiset constraint |D| >= J only tightens. Two nondecreasing
functions with the same {J : f(J) <= k} for every k are equal, so
testing h against the product minimum tests exactly F1's claim and not a
weaker relative. This rides on the parent's finding and is therefore
re-derived here rather than cited.

SECOND, THE QUOTIENT READING, AND IT IS WHAT MAKES THE RANGE OPEN. The
flattening->=J vectors are the lattice L_{M,J} = (x-1)^J Z[x] cut at
degree < M, so EVERY member is (x-1)^J q with q an integer polynomial of
degree < M - J (the degrees agree: J + (M - J - 1) = M - 1). So the
search is over the QUOTIENT q and not over the vector, in M - J free
integers rather than M, with no feasibility constraint at all -- every q
is admissible and every admissible vector is some q. A search over q is
a search over the whole lattice.

THIRD, WHY A ONE-SIDED INSTRUMENT IS ENOUGH. Both sides of the claim are
UPPER bounds on h: the product family exhibits vectors, and a search over
q exhibits vectors. A q whose (x-1)^J q has sup-norm BELOW the best
product's height refutes the law outright and prints its own witness. No
lower bound is needed, and none is claimed -- which is exactly why this
rig reaches M = 30 where an exhaustive route stops at 16. The cost is
that a NEGATIVE result is only as good as the search, which is what the
controls are for and what the record must say.

FOURTH, THE PRODUCT FAMILY'S OWN ARITHMETIC. For P = prod_i (x^{d_i} - 1)
over a multiset D, P = (x-1)^|D| q with q(1) = prod_i d_i, so
|m_{|D|}| = prod d_i exactly. Its degree is sum D, so D fits in M atoms
iff sum D <= M - 1. Multiplication by (x^d - 1) is one shifted
subtraction, so the family is enumerable by DFS over nondecreasing parts
with the convolution carried incrementally.

FIFTH, THE ROOT-OF-UNITY BOUND, which is the mechanism the classical
proof runs on, arriving early here. At any root of unity w, |P(w)| <=
height * (deg + 1). For
a pure product P(w) = prod_i (w^{d_i} - 1), which VANISHES as soon as one
part is divisible by w's order. At w = -1 that reads: an all-ODD pure
product has |P(-1)| = 2^|D| exactly, so a height-1 one needs
2^|D| <= deg + 1 and must otherwise carry an EVEN part. The threshold is
a function of the degree allowed and not a constant: inside degree 61 it
bites at |D| = 6 (64 > 62), inside degree 69 at |D| = 7 (128 > 70).
Used here only as a check on the enumerator's output, never as a prune.

SIXTH, THE RANK-1 TAIL. At J = M - 1 the lattice has rank 1 and is
spanned by (x-1)^{M-1}, so h(M, M-1) = C(M-1, floor((M-1)/2)) exactly --
an independent closed form the exact route must reproduce.

SEVENTH, THE INCUMBENT, AND WHERE IT SAYS WE HOLD NOTHING. The classical
determination is the HEIGHT-1 statement: the minimal DEGREE d(n) of a
height-1 multiple of (x-1)^n, Borwein-Mossinghoff (Experimental
Mathematics 9:3, 2000), carried by OEIS A059753 as
1, 3, 6, 11, 15, 22, 30, 41, 48, 61, 69, 93, 112, 120 at n = 1..14 and
minimal through 14 since 2025. Nothing here tries to extend that. It
enters as a CONTROL: the product enumerator, run at height 1, must
reproduce d(n) within its reach, and the paper's reported finding that
every extremal there is a pure product is exactly what predicts it will.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. PRODUCT EXTREMALITY SURVIVES OFF-CHART (TRANSPLANT: imported from
      the parent's in-range 94-cell chart and flagged as such). At every
      probed cell M = 17..30, J = 2..M-1, the quotient search's best
      height EQUALS the best pure-product height and never falls below.
  P2. THE SEARCH IS EXACT ON THE CONTROL. At every cell where the exact
      route decides h (M <= 12, all J), the quotient search attains it.
  P3. THE INCUMBENT CROSS-CHECK. For n = 2..9 the least degree at which
      the pure-product family reaches height 1 is A059753(n) =
      3, 6, 11, 15, 22, 30, 41, 48.
  P4. RANK-1 TAIL PARITY. h(M, M-1) = C(M-1, floor((M-1)/2)) at every
      M <= 12 by the exact route.
  P5. THE SEARCH'S MISSES, IF ANY, ARE HIGH-RANK. Any control cell the
      search fails to attain has rank M - J >= 5.

KILLS, as observables rather than inferences.
  K-A. A cell where the quotient search prints a vector of sup-norm
       STRICTLY BELOW the best pure-product height -- the cell, the
       vector, its quotient and both heights are printed.
  K-B. A control cell where the search's height exceeds the exact h --
       the cell, the exact h and the search's h are printed. ANY K-B
       FIRING BARS READING K-A's ABSENCE AS EVIDENCE FOR P1, and the
       record says so rather than reporting a survival.
  K-C. A disagreement between the product enumerator's least height-1
       degree and A059753 at n <= 9 -- the n, both degrees, and the
       enumerator's best multiset are printed.
  K-D. The exact route disagreeing with the rank-1 closed form at
       J = M - 1, or with brute force at M <= 7.

CONTROLS, run and read BEFORE any verdict, each printing how many cases
it exercised.
  C1 (POSITIVE, PARITY). The pruned exact route agrees with full brute
     force over [-k, k]^M at M <= 7, k <= 3, on the decision h <= k.
  C2 (REPRODUCTION). The exact route reproduces explore_flatten_height.py's
     recorded column h(9, J) = 2, 3, 9, 14 at J = 4..7.
  C3 (TAIL). The exact route matches the rank-1 closed form at J = M - 1
     for every M <= 12.
  C5 (INDEPENDENT ALGORITHM), added after the first run and recorded as
     such. C1 was the only check on the exact route and it stops at
     M <= 7, full brute force being (2k+1)^M -- so the route deciding
     every cell here was licensed nowhere near the widths it runs at.
     explore_flatten_height.py's mim_exists answers the SAME predicate
     by meet-in-the-middle on moment keys, sharing no code and no cost
     law with the interval-pinned quotient DFS. Compared cell by cell
     over M = 4..13, J = 1..M-1, k = 1..3.

THE ARMS.
  1. THE EXACT ROUTE. h(M, J) by iterative deepening in k over the
     INTERVAL-PINNED QUOTIENT DFS the hand attack's second section
     derives -- coefficient t of (x-1)^J q depends only on q_0..q_t and
     carries q_t with a unit leading coefficient, so each q_t is pinned
     to an interval of width 2k+1 and the cost is (2k+1)^(M-J), the RANK
     rather than the width. The deepening's ceiling is the product bound,
     so it always terminates; the first nonzero q is pinned positive.
     Run at every control cell (M <= 12) AND at every off-chart cell
     under a node cap. An ABORTED deepening is not a dead loss: every
     level it finished was infeasible, so the level it aborted on is a
     genuine LOWER bound on h, and a lower bound meeting the product
     ceiling DECIDES the cell exactly (C1, C2, C3, P4, K-A, K-D).
  2. THE PRODUCT FAMILY. Least height over multisets D with |D| >= J and
     sum D <= M - 1, by DFS over nondecreasing parts with incremental
     convolution; and, at height 1, the least degree reaching it per
     depth (P3, K-C). Enumerated to degree 69, which carries the
     height-1 read two depths PAST P3's frozen n <= 9; those two rows
     are printed OFF-SLATE, no prediction covering them, because they
     also sit past the range where the classical determination reports
     every extremal to be a pure product.
  3. THE QUOTIENT SEARCH. Greedy sup-norm descent on q in M - J integers,
     tie-broken by the 2-norm, with restarts seeded from the product
     quotients, from zero-plus-a-unit and from random boxes, plus random
     kicks on stall (P1, P2, P5, K-A, K-B).
  4. THE OFF-CHART SWEEP. Arms 2 and 3 at every cell M = 17..30,
     J = 2..M-1, printing every cell where they disagree in either
     direction (P1, K-A).
  5. THE INCUMBENT AS A LOWER BOUND, added after the first run and
     recorded as such: its brackets showed A059753 closing many of them
     for free. d(J) is the LEAST degree of a height-1 multiple of
     (x-1)^J, so a cell with M <= d(J) holds no height-1 vector at all
     and h(M, J) >= 2 there. That is the whole height-1 boundary of the
     chart, exactly, at no compute -- and paired with a product bound of
     2 it DECIDES the cell. It bounds nothing above height 2, which is
     precisely where the classical reading stops being usable.

RESOURCE NOTE. Exact integer arithmetic, no numpy, so no BLAS arenas.
The exact route is the only exponential arm; it runs everywhere but is
held by a node cap per deepening level, which is what turns an
unaffordable cell into a bracket rather than a hang. The product family
is one DFS over multisets to degree 69 and the quotient search is bounded
by its own restart and step budget. Estimated two to six minutes wall,
well under the 512 MB default; run under memwatch.

RUN RECORD (final run: wall 206.1 s, peak working set 26.9 MB, peak
commit 21.2 MB under memwatch's 512 MB default; the product table alone
is ~118 s of it, 2415 multiset keys to degree 69, and C5 another ~26 s
with the meet-in-the-middle's dictionaries accounting for the working
set). SEVEN runs. The
first ran the slate as frozen. ARM 5 DID NOT EXIST UNTIL THAT RUN
PRINTED: its sweep left 88 cells bracketed, and reading the brackets
rather than the verdict showed the incumbent closing many of them at no
compute, so the arm was added and the slate's ARM list says where it
came from. The second run mis-ATTRIBUTED one counter -- it credited arm
5 with two cells (M = 17 and 18 at J = 6) whose floor the deepening had
raised on its own -- and the attribution was split three ways before any
verdict was read. The fourth and fifth runs added no arm and moved no
result: the fourth made C1 PRINT the split between its value comparisons
and its consistency-only cells, and the fifth fixed C3's own count of
how many rows P3 covers -- it had said nine where P3 names n = 2..9,
which is eight, n = 1 being exercised by no prediction. Both are
reporting faults in CONTROLS, which is where they cost the most. The
sixth added C5, on the plainest reading of the same worry: C1 was the
only check the exact route had and it stops at M <= 7, so the route
deciding every cell out to M = 30 had no independent check anywhere near
the widths it runs at. The seventh removed a SILENT FALLBACK rather than a
number: the deepening used to return its ceiling if it fell out of the
loop, a path reachable only when `feasible` is wrong -- and one stuck at
False would then have reported h = the product bound at every cell,
which is the answer the rig tests for, so the sweep would have read
green and meant nothing. It raises now. C5 already covers the failure
(225 predicates against an independent algorithm), but a control that
catches a bug and a code path that cannot express it are different
guarantees. No prediction or kill was touched at any point.

F1. EVERY CONTROL PASSES AND EVERY KILL IS SILENT. C1 (parity) 18 cases,
0 mismatches, at M <= 6 under a height cap of 3 and M = 7 under 2 -- the
brute route is (2k+1)^M and pays for the whole cap, which is the scope
line. READ THE SPLIT AND NOT THE 18: only 13 of them compare a VALUE
against brute force, exercising h = 1, 2 and 3; the other 5 sit above the
cap, where brute finds nothing and the check is consistency alone. The
13 are what licenses the exact route, and a control reported as 18 would
have claimed a third more than it did. C2 (reproduction) recovers
explore_flatten_height.py's recorded
column h(9, J) = 2, 3, 9, 14 at J = 4..7 exactly, from an algorithm with
a different cost law. C4 9 cases, K-D 0: the rank-1 tail equals
C(M-1, floor((M-1)/2)) at every M <= 12. K-C 0, K-B 0, K-A 0.
AND C5 IS THE ONE THAT LICENSES THE REST: 225 (M, J, k) predicates over
M = 4..13, J = 1..M-1, k = 1..3, the interval-pinned quotient DFS
against explore_flatten_height.py's meet-in-the-middle, 0 mismatches.
Two algorithms sharing no code and no cost law agree on the predicate
every verdict here is built from, at widths C1 cannot pay for -- and
C1's own 13 value comparisons stop at M = 7, which is the gap C5
exists to close.

F2. P3 HOLDS 8 FOR 8 -- it covers n = 2..9, EIGHT rows and not the nine
the run's first count implied, n = 1 being exercised by no prediction --
AND THE OFF-SLATE ROWS CARRY IT ONE STEP PAST THE PROVED RANGE
(observation, exhaustive over products of degree <= 69).
The least degree at which a pure product reaches height 1 equals
A059753(n) at every n = 1..11: 1, 3, 6, 11, 15, 22, 30, 41, 48, 61, 69.
Every witness has DISTINCT parts --
(1,2,3,4,5,7,8,11) at n = 8, (1,2,3,4,5,6,7,9,11) at n = 9,
(1,2,3,4,5,6,7,9,11,13) at n = 10, (1,2,3,4,5,6,7,8,9,11,13) at n = 11.
The classical determination proves every extremal a pure product for
m <= 10, so n = 11 is the row that is NEW here: a pure product attains
the known minimum 69 there too. What this is NOT: it does not show the
n = 11 extremal is unique, nor that no other shape attains 69 -- an
attaining product is an upper bound meeting a known lower bound, and
that is the whole of it. Every witness carries an EVEN part, and the
root-of-unity bound ACCOUNTS for it at every depth but the first: an
all-odd height-1 product needs 2^n <= d(n) + 1, which holds at n = 2
(4 <= 4) and fails at every n >= 3 (8 > 7, 16 > 12, 32 > 16, and worse
after), so the even part is FORCED from n = 3 on. Only n = 2's witness
(1, 2) carries one the bound would have let it omit, and no all-odd
rival exists there either -- (1, 1) is height 2. Read as a prediction
rather than a coincidence, that is the classical proof's own mechanism
showing up in the enumerator's output.

F3. THE CONTROL CHART REBUILDS THE LAW ON THE OTHER DIAL (rule,
exhaustive over the 63 cells M = 4..12, J = 1..M-1): exact h(M, J)
equals the pure-product bound at EVERY cell, K-A silent throughout. The
parent charts the CEILING J*(M, k) by width and height; this charts h by
width and DEPTH, by a route whose cost is (2k+1)^(M-J) rather than
(2k+1)^M, and the hand attack's first section derives that the two
statements are the same claim rather than relatives. Since h at every J
determines J* at every k, this settles the parent's own chart AT M <= 12
for every height, where the parent charted k <= 4 at the widest of them
and no higher than k <= 10 anywhere -- and that far and no further: its
k = 1 row runs to M = 24 and its k = 2 row to
M = 16, neither of which a 63-cell chart ending at 12 reconfirms.

F4. P2 HOLDS, P5 IS VACUOUS, AND THE MECHANISM IS WEAKER THAN THE SCORE.
The quotient search attains the exact h at all 63 control cells, 0 K-B
firings -- so there are no misses and P5's rank claim has nothing to
range over. But the search is SEEDED from the product quotient, so what
a clean sweep says is that the product quotient is a local minimum under
single-coefficient moves which the random restarts never beat. That is
real evidence and it is not the exhaustive evidence the count reads
like, and no off-chart negative below rests on it alone.

F5. P1 HOLDS WHERE THE SWEEP DECIDES, AND THE DECIDED SET IS 18 CELLS
AND NOT 82 (rule at the decided cells, observation elsewhere). Over 154
cells at M = 17..30, J = 2..12 -- not all of them off-chart, the
parent's k = 1 row reaching M = 24 -- 82 decided, K-A 0, and the
search never once fell below OR above the product bound. But 64 of the
82 carry a product bound of 1, where h = 1 follows from h >= 1 for any
nonzero integer vector and nothing whatever is measured. THE
INFORMATIVE COUNT IS 18, every one of them a cell where h = 2 exactly
and every one of them beyond the parent's k = 2 reach of M <= 16, so the
informative set is off-chart entire even though the sweep is not; of the
64 trivial ones only 30 sit past the k = 1 row at all. 16 of the 18
needed arm 5's incumbent floor to close -- only M = 17 and 18 at J = 6
were closed by the deepening's own. 72 cells stay
bracketed, the widest [7, 77] at M = 17, J = 12. So product extremality
now stands DECIDED at 18 cells beyond the parent's range, all at height
2 -- and DECIDED is the word rather than EXHAUSTIVELY, because 16 of the
18 close on a CITED lower bound (A059753, itself proved elsewhere)
against an exhibited product, and only the 2 at J = 6 close on a sweep
this rig ran. The other 136 carry a locally-optimal-and-unbeaten reading
and nothing stronger.

F6. WHAT THIS RIG HANDS BACK IS A NAMED INSTRUMENT AND NOT A VERDICT, AND
THE BRACKETS SAY WHICH. The deepening's cost is (2k+1)^rank, so it
decides by RANK and not by width -- which is what opened M = 30 at all.
The 72 that stay bracketed are stopped by that same cost with its two
factors traded against each other, and the two ends fail for OPPOSITE
reasons: the 14 width-1 brackets are small-ceiling and large-rank
(M = 18, J = 7 is [2, 3] at rank 11), while the widest is the reverse,
[7, 77] at M = 17, J = 12 and rank 5. The rank end is NOT out of
compute's reach, which a later probe measured rather than assumed: run
at a 60-million-node cap, M = 18, J = 7 decides in 34 s -- h <= 2 is
false, so h = 3, the product bound, one more cell where the law holds.
But that frontier is ONE rank wide, and its far side was measured too
rather than extrapolated: at rank 12 (M = 19, J = 7) and rank 13
(M = 20, J = 7) the same test is still undecided at a 150-million-node
cap after 167 s each. So the rank end yields exactly that one cell and
is then spent. (Those probes are later measurements and not prints of
this run, whose counts stand as printed.) Everything else needs a LOWER
bound: arm 5 priced what one is worth -- the classical height-1
boundary closed 16 cells for free and then stopped dead, saying nothing
above height 1. THE OBJECT THE QUESTION NEEDS IS THEREFORE NAMED BY ITS
ABSENCE: d_k(J), the least degree of a multiple of (x-1)^J of height AT
MOST k, of which the literature contacted here holds only k = 1 and of
which this chart is the inverse. Read honestly, and as the run left it,
d_2 would
settle the VALUE at 14 of the 72, decide the "is it 2" half at 48 more,
and say nothing at the 10 whose floor already exceeds 2, which need d_3
and up; the probe above takes one of the 14, so the standing partition
is 13 + 48 + 10 over 71.

(SETTLED SINCE, by explore_flatten_d2.py, which built the object this
paragraph names by its absence: d_2(J) = 1, 2, 4, 7, 11, 16, 22, 26 at
J = 1..8, exhaustively, and every one of the eight is the least-degree
pure product of height at most 2 -- so the law F3 and F5 test survives
the second dial as well. Its route searches the COEFFICIENTS under a
propagation bound rather than the quotient, so its cost falls with the
height where this rig's falls with the rank, and it settles the k = 2
boundary of the chart at every width for J <= 8 -- including M = 19 and
M = 20 at J = 7, the two cells F6's probe measured as undecided at a
150-million-node cap. The partition above is left as this run printed
it and is NOT re-derived there, that rig sweeping its own wider range;
what is superseded is the sentence calling d_2 absent, not the
counts. What F6 calls the object's absence above height 2 still
stands: d_3 and up remain uncontacted.)
"""
import os
import random
import time
from math import comb

from explore_flatten_height import mim_exists

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

BUDGET = 69            # largest product degree enumerated (A059753(11))
CTRL_M = 12            # exact-route control ceiling
SWEEP_M = range(17, 31)
SWEEP_J = range(2, 13)
SWEEP_CAP = 400000     # node cap per deepening level in the sweep
A059753 = {1: 1, 2: 3, 3: 6, 4: 11, 5: 15, 6: 22, 7: 30, 8: 41, 9: 48,
           10: 61, 11: 69, 12: 93, 13: 112, 14: 120}


class NodeCap(Exception):
    pass


# ------------------------------------------------------ polynomials

def mul_shift(p, d):
    """p * (x^d - 1), one shifted subtraction."""
    res = [0] * (len(p) + d)
    for i, c in enumerate(p):
        if c:
            res[i + d] += c
            res[i] -= c
    return res


def pow_xm1(J):
    """Coefficients of (x-1)^J, low degree first."""
    return [comb(J, m) * (-1) ** (J - m) for m in range(J + 1)]


def height(p):
    return max((abs(c) for c in p), default=0)


def divide_xm1(p, J):
    """Exact quotient p / (x-1)^J by synthetic division; callers pass
    products of at least J factors, so the division is exact."""
    e = pow_xm1(J)
    work = list(p)
    R = len(p) - J
    q = [0] * R
    for t in range(R):
        qt = work[t] // e[0]
        q[t] = qt
        if qt:
            for m, em in enumerate(e):
                work[t + m] -= em * qt
    assert all(c == 0 for c in work), "non-exact division"
    return q


def expand(q, e, M):
    """(x-1)^J q as an M-atom vector."""
    P = [0] * M
    for i, qi in enumerate(q):
        if qi:
            for m, em in enumerate(e):
                P[i + m] += em * qi
    return P


# ------------------------------------------- arm 2: the product family

def product_table(budget):
    """Min height over multisets of parts, keyed (count, degree sum),
    with a witness multiset per key."""
    best, wit, cur = {}, {}, []

    def dfs(start, poly, count, s):
        if count:
            H = height(poly)
            key = (count, s)
            if key not in best or H < best[key]:
                best[key] = H
                wit[key] = tuple(cur)
        for d in range(start, budget - s + 1):
            cur.append(d)
            dfs(d, mul_shift(poly, d), count + 1, s + d)
            cur.pop()

    dfs(1, [1], 0, 0)
    return best, wit


class Products(object):
    """Query layer over the product table."""

    def __init__(self, budget):
        self.best, self.wit = product_table(budget)
        self.budget = budget

    def bound(self, M, J):
        """(least height, witness multiset) over |D| >= J, sum D <= M-1."""
        bh, bw = None, None
        for (c, s), H in self.best.items():
            if c >= J and s <= M - 1 and (bh is None or H < bh):
                bh, bw = H, self.wit[(c, s)]
        return bh, bw

    def least_degree_height1(self, n):
        """Least degree of a height-1 product with at least n factors."""
        bd, bw = None, None
        for (c, s), H in self.best.items():
            if H == 1 and c >= n and (bd is None or s < bd):
                bd, bw = s, self.wit[(c, s)]
        return bd, bw


# ------------------------------------------- arm 1: the exact route

def feasible(M, J, k, node_cap):
    """Is there a nonzero M-atom vector of flattening >= J and height
    <= k? Interval-pinned DFS over the QUOTIENT (hand attack, second
    section): cost (2k+1)^(M-J), the RANK rather than the width."""
    R = M - J
    e = pow_xm1(J)
    s0 = e[0]
    P = [0] * M
    nodes = [0]

    def dfs(t, allzero):
        nodes[0] += 1
        if nodes[0] > node_cap:
            raise NodeCap
        if t == R:
            if allzero:
                return False
            return all(abs(P[i]) <= k for i in range(R, M))
        base = P[t]
        lo, hi = (-k - base, k - base) if s0 == 1 else (base - k, base + k)
        if allzero:
            lo = max(lo, 0)
        for qt in range(lo, hi + 1):
            if qt:
                for m, em in enumerate(e):
                    P[t + m] += em * qt
            if dfs(t + 1, allzero and qt == 0):
                return True
            if qt:
                for m, em in enumerate(e):
                    P[t + m] -= em * qt
        return False

    return dfs(0, True)


def exact_bracket(M, J, ceiling, node_cap):
    """(h, lower) for h(M, J). An aborted deepening is NOT a dead loss:
    every k it finished was infeasible, so the level it aborted on is a
    genuine LOWER bound, and a lower bound meeting the product ceiling
    decides the cell. Returns h = None when undecided. The deepening
    terminates by SUCCEEDING, the product attaining the ceiling being
    itself a witness at k = ceiling, so falling out of the loop is
    impossible unless `feasible` is wrong -- and returning the ceiling
    there, as this did, would have made a predicate stuck at False report
    h = the product bound at EVERY cell, which is exactly the answer the
    rig tests for, so the whole sweep would have read green and meant
    nothing. It raises instead."""
    if ceiling <= 1:
        return 1, 1                      # h >= 1 for any nonzero vector
    for k in range(1, ceiling + 1):
        try:
            if feasible(M, J, k, node_cap):
                return k, k
        except NodeCap:
            return None, k
    raise AssertionError(
        "h(%d, %d): the deepening exhausted its ceiling %d without finding "
        "a witness, but the product attaining that ceiling IS one -- the "
        "predicate is broken, not the cell" % (M, J, ceiling))


def brute_h(M, J, kmax):
    """Full brute force over [-k,k]^M -- the parity control."""
    from itertools import product as iproduct
    for k in range(1, kmax + 1):
        for vec in iproduct(range(-k, k + 1), repeat=M):
            if not any(vec):
                continue
            if all(sum(comb(r, j) * c for r, c in enumerate(vec)) == 0
                   for j in range(J)):
                return k
    return None


# ---------------------------------------- arm 3: the quotient search

def score(P):
    mx = s2 = 0
    for c in P:
        a = c if c >= 0 else -c
        if a > mx:
            mx = a
        s2 += c * c
    return (mx, s2)


def descend(q, e, M, steps):
    """Greedy sup-norm descent on q, tie-broken by the 2-norm."""
    R = len(q)
    P = expand(q, e, M)
    cur = score(P)
    nz = sum(1 for v in q if v)
    for _ in range(steps):
        bi = bd = None
        bs = cur
        for i in range(R):
            for delta in (1, -1):
                if nz == 1 and q[i] and q[i] + delta == 0:
                    continue          # never walk into the zero vector
                for m, em in enumerate(e):
                    P[i + m] += em * delta
                s = score(P)
                for m, em in enumerate(e):
                    P[i + m] -= em * delta
                if s < bs:
                    bs, bi, bd = s, i, delta
        if bi is None:
            break
        if q[bi] == 0:
            nz += 1
        elif q[bi] + bd == 0:
            nz -= 1
        q[bi] += bd
        for m, em in enumerate(e):
            P[bi + m] += em * bd
        cur = bs
    return cur[0], list(q)


def search_h(M, J, seeds, rng, restarts, steps):
    """One-sided upper bound on h(M, J) with a witness quotient."""
    R = M - J
    e = pow_xm1(J)
    bh, bq = None, None
    starts = [list(s) for s in seeds]
    starts.append([1] + [0] * (R - 1))
    while len(starts) < restarts:
        w = rng.choice((1, 1, 2))
        cand = [rng.randint(-w, w) for _ in range(R)]
        if any(cand):
            starts.append(cand)
    for q0 in starts[:restarts]:
        H, q = descend(list(q0), e, M, steps)
        if bh is None or H < bh:
            bh, bq = H, q
    return bh, bq


def product_seed(M, J, prods):
    """The best product's quotient, cut to the cell's rank."""
    _, wit = prods.bound(M, J)
    if not wit:
        return []
    poly = [1]
    for d in wit:
        poly = mul_shift(poly, d)
    q = divide_xm1(poly, J)
    R = M - J
    return [q + [0] * (R - len(q))] if len(q) <= R else []


# ------------------------------------------------------------- main

def main():
    t0 = time.time()
    rng = random.Random(20260828)
    print("== ARM 2: the pure-product family (budget degree %d)" % BUDGET)
    prods = Products(BUDGET)
    print("   multiset keys tabulated: %d  (%.1f s)"
          % (len(prods.best), time.time() - t0))

    print("\n== C3 (INCUMBENT) / K-C / P3: least height-1 product degree"
          " vs A059753")
    print("   [P3 froze n <= 9; the n = 10, 11 rows are OFF-SLATE and no"
          " prediction covers them]")
    kc = 0
    for n in range(1, 12):
        d, w = prods.least_degree_height1(n)
        fires = (d != A059753[n]) and 2 <= n <= 9
        kc += 1 if fires else 0
        even = any(p % 2 == 0 for p in w) if w else None
        tag = "" if n <= 9 else "  OFF-SLATE"
        print("   n=%2d  product least degree %s   A059753 %3d   even part %s"
              "   parts %s%s%s"
              % (n, str(d), A059753[n], even, w, tag,
                 "   <-- K-C FIRES" if fires else ""))
    print("   cases exercised: 11; P3 covers n = 2..9, which is EIGHT of"
          " them -- n = 1 is run but no prediction claims it, and n = 10, 11"
          " are off-slate;  K-C firings: %d" % kc)

    print("\n== C1 (POSITIVE, PARITY): the exact route vs full brute force")
    print("   [scope: M <= 6 at height cap 3, M = 7 at height cap 2 -- the"
          " brute route is (2k+1)^M and pays for the whole cap]")
    c1 = c1bad = strict = 0
    seen = set()
    for M in range(4, 8):
        cap = 3 if M <= 6 else 2
        for J in range(1, M):
            pb, _ = prods.bound(M, J)
            ex, _ = exact_bracket(M, J, pb, 10 ** 7)
            br = brute_h(M, J, min(pb, cap))
            ok = (ex == br) or (br is None and ex is not None and ex > cap)
            c1 += 1
            if br is not None:
                strict += 1
                seen.add(ex)
            if not ok:
                c1bad += 1
                print("   MISMATCH M=%d J=%d exact %s brute %s" % (M, J, ex, br))
    print("   cases exercised: %d;  mismatches: %d" % (c1, c1bad))
    print("   of those, STRICT value comparisons: %d (h values %s all"
          " exercised); the other %d only check CONSISTENCY, brute finding"
          " nothing under the cap where the exact route reports h above it"
          % (strict, sorted(seen), c1 - strict))

    print("\n== C5 (INDEPENDENT ALGORITHM): the quotient DFS vs the"
          " parent's meet-in-the-middle, on the same predicate")
    c5 = c5bad = 0
    for M in range(4, 14):
        for J in range(1, M):
            for k in (1, 2, 3):
                try:
                    ours = feasible(M, J, k, 5 * 10 ** 6)
                except NodeCap:
                    continue
                c5 += 1
                theirs = mim_exists(M, k, J)
                if theirs != ours:
                    c5bad += 1
                    print("   MISMATCH M=%d J=%d k=%d  mim=%s ours=%s"
                          % (M, J, k, theirs, ours))
    print("   (M, J, k) predicates compared: %d;  mismatches: %d"
          % (c5, c5bad))

    print("\n== C2 (REPRODUCTION): h(9, J) against explore_flatten_height.py")
    want = {4: 2, 5: 3, 6: 9, 7: 14}
    c2bad = 0
    for J in range(4, 8):
        pb, _ = prods.bound(9, J)
        ex, _ = exact_bracket(9, J, pb, 10 ** 7)
        if ex != want[J]:
            c2bad += 1
        print("   h(9,%d) = %s   recorded %d   %s"
              % (J, ex, want[J], "ok" if ex == want[J] else "MISMATCH"))
    print("   cases exercised: 4;  mismatches: %d" % c2bad)

    print("\n== C4 (TAIL) / P4 / K-D: h(M, M-1) vs C(M-1, floor((M-1)/2))")
    c4 = c4bad = 0
    for M in range(4, CTRL_M + 1):
        pb, _ = prods.bound(M, M - 1)
        ex, _ = exact_bracket(M, M - 1, pb, 10 ** 7)
        cf = comb(M - 1, (M - 1) // 2)
        c4 += 1
        if ex != cf:
            c4bad += 1
            print("   MISMATCH M=%d exact %s closed form %d" % (M, ex, cf))
    print("   cases exercised: %d;  K-D firings: %d" % (c4, c4bad))

    print("\n== CONTROL CHART: exact h(M, J) vs the product bound, M <= %d"
          % CTRL_M)
    ctrl = []
    ka_ctrl = 0
    for M in range(4, CTRL_M + 1):
        row = []
        for J in range(1, M):
            pb, _ = prods.bound(M, J)
            ex, _ = exact_bracket(M, J, pb, 3 * 10 ** 6)
            row.append((J, ex, pb))
            if ex is not None and ex < pb:
                ka_ctrl += 1
                print("   K-A FIRES (exact, in control range): M=%d J=%d "
                      "exact %d product %d" % (M, J, ex, pb))
        ctrl.append((M, row))
        print("   M=%2d  " % M + "  ".join(
            "J%d:%s/%s" % (J, ex, pb) for J, ex, pb in row))
    print("   K-A firings in control range: %d" % ka_ctrl)

    print("\n== P2 / P5 / K-B: the quotient search against the exact route")
    kb = 0
    misses = []
    have = 0
    for M, row in ctrl:
        for J, ex, pb in row:
            if ex is None:
                continue
            have += 1
            sh, _ = search_h(M, J, product_seed(M, J, prods), rng, 8, 200)
            if sh != ex:
                kb += 1
                misses.append((M, J, M - J, ex, sh))
    print("   control cells with an exact value: %d" % have)
    print("   K-B firings (search above exact): %d" % kb)
    for M, J, R, ex, sh in misses:
        print("   MISS M=%2d J=%2d rank %2d  exact %3d  search %3d"
              % (M, J, R, ex, sh))
    if misses:
        print("   P5 read: minimum rank among misses = %d"
              % min(m[2] for m in misses))

    print("\n== ARM 4: the off-chart sweep, M = %d..%d, J = %d..%d"
          % (SWEEP_M[0], SWEEP_M[-1], SWEEP_J[0], SWEEP_J[-1]))
    print("   cell reads as  Jn:<h>/<product>  when h is DECIDED (the exact"
          " route, or its lower bound meeting the product ceiling),")
    print("   and  Jn:[lo,hi]  when it is not.")
    ka = decided = cells = inc_lo = by_inc = informative = 0
    by_val = by_floor = 0
    brackets = []
    over = []
    for M in SWEEP_M:
        line = []
        for J in SWEEP_J:
            if J >= M:
                continue
            cells += 1
            pb, pw = prods.bound(M, J)
            ex, lo = exact_bracket(M, J, pb, SWEEP_CAP)
            sh, sq = search_h(M, J, product_seed(M, J, prods), rng, 5, 120)
            hi = min(pb, sh)
            lo_dfs = lo                  # the exact route's OWN floor
            if J in A059753 and M <= A059753[J] and lo < 2:
                lo = 2                   # arm 5: no height-1 vector fits
                inc_lo += 1
            if ex is not None:
                by_val += 1
            elif lo >= hi:
                ex = hi                  # a floor meeting the ceiling
                by_floor += 1
                if lo_dfs < hi:
                    by_inc += 1          # and only arm 5 could raise it
            if ex is not None:
                decided += 1
                if pb > 1:
                    informative += 1
                line.append("J%d:%d/%d" % (J, ex, pb))
                if ex < pb:
                    ka += 1
                    vec = expand(sq, pow_xm1(J), M) if sh == ex else None
                    print("   K-A FIRES: M=%d J=%d  product %d  attained %d"
                          % (M, J, pb, ex))
                    print("      product multiset %s" % (pw,))
                    print("      quotient %s" % (sq,))
                    print("      vector   %s" % (vec,))
            else:
                brackets.append((M, J, lo, hi))
                line.append("J%d:[%d,%d]" % (J, lo, hi))
            if sh > pb:
                over.append((M, J, pb, sh))
        print("   M=%2d  " % M + "  ".join(line))
    print("\n   cells swept: %d;  cells DECIDED off-chart: %d;  bracketed: %d"
          % (cells, decided, len(brackets)))
    print("   of the decided, cells whose product bound EXCEEDS 1:"
          " %d -- the informative subset, a product bound of 1 forcing"
          " h = 1 with no measurement at all;" % informative)
    print("   read that number and not the other.")
    print("   how the decided were decided: %d carry an exact value from the"
          " deepening, %d by a FLOOR meeting the product ceiling" % (by_val, by_floor))
    print("   arm 5 raised the floor to 2 at %d cells; %d of the decided"
          " needed it, the rest having a deepening floor that reached"
          % (inc_lo, by_inc))
    print("   K-A firings: %d" % ka)
    print("   cells where the search overshot the product bound: %d"
          % len(over))
    for M, J, pb, sh in over[:20]:
        print("      M=%2d J=%2d product %3d search %3d" % (M, J, pb, sh))
    if brackets:
        wr = max(brackets, key=lambda b: b[3] - b[2])
        print("   widest bracket: M=%d J=%d [%d, %d]"
              % (wr[0], wr[1], wr[2], wr[3]))
    print("\n   wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
