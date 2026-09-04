"""
explore_five_prints.py -- five conjectures, each decided by the one print
or the one derivation frozen to end it: whether the descent dimension
survives coefficients above 1, whether a field's least split prime lands
in the class of least form minimum, whether the least prime's non-square
bias survives a census three times wider at a standard error that
resolves it, whether the flattening champion's threshold is a function
of the lattice rank, and whether a reader handed the two door
inequalities as an oracle ever drifts.

THE FIVE QUESTIONS.

  Q1. THE DESCENT LOCATOR, off the 0/1 frame. Two factorizations of a
      polynomial in the nonnegative semiring restrict to every face of
      the product's Newton polytope, and their DESCENT DIMENSION is the
      smallest face dimension at which the induced factor multisets --
      each initial form divided by its monomial content -- already
      differ (explore_menu_faces.py). The parent proved delta >= 1 on
      0/1 menus: at a vertex every initial form is a monomial of
      coefficient 1, the division empties both multisets, no vertex
      grades a collision. The question: does delta >= 1 survive factors
      with a coefficient above 1?

  Q2. THE MINIMUM ORACLE. Over the imaginary quadratic fields with a
      cyclic even class group to |D| <= 32000 (4,044 of them), the
      least odd split prime lands in a non-square class 0.657 of the
      time; the classes it CAN land in are those whose reduced form's
      minimum it clears, and that admissibility alone carries 0.095 of
      the 0.157 excess over the coin (explore_four_prints.py F2). The
      question: does the least prime's class tend to BE the
      non-principal class of least minimum -- the first class
      reduction theory opens -- beyond that class's own weight among
      the admissible classes?

  Q3. THE RANK-SEATED BIAS, refrozen. The fixed-prime rank contrast D
      -- the rank-1 non-square share minus the rank >= 2 share at the
      same prime, pooled over primes -- read +0.030 (se 0.013) at
      |D| <= 32000, neither under 0.05 at two standard errors nor at
      0.10. The question: the same D over the same bands to
      |D| <= 100000, where the standard error is expected under 0.008.

  Q4. THE CLOSED-FORM FILTER, at the next rank. At lattice ranks 5 to
      8 the least-height moment-annihilating vector is the champion
      (1+x)^(r-1) (x-1)^J from a per-rank depth J_ch = 31, 34, 59, 61
      up, and at all four J_ch = J_hi + 1, the depth after the last
      failure (explore_flatten_band.py). The question: what J_ch and
      J_hi are at ranks 9 and 10, and whether any law in the rank
      that fits the four predicts them.

  Q5. THE INDEX ORACLE. The chain-preferring nesting law is a statement
      about DECISIONS: at a convergent vertex of index sigma, where the
      tree reference's intrinsic index is at least sigma + 1 and the
      chain reference's is strictly larger, a chain-preferring run's
      chain reference has maxed the ladder and its exits never violate
      the exit-index invariant (explore_reference_families.py, R13,
      R14). No reader can execute the condition, since reading a
      reference's index needs the digits. The question: a reader
      HANDED the two inequalities as a side channel, chaining exactly
      where both hold and preferring the tree everywhere else -- does
      any exit it takes from a door where the oracle said chain
      violate the invariant, over the ten reference families?

WHOSE VOCABULARY. Q1 in the polytope's (face, initial form, induced
multiset, the semiring's atoms); Q2 and Q3 in reduced binary quadratic
forms' (a reduced definite form (a, b, c), its leading coefficient the
class's minimum, the principal class's minimum its constant term, a
square being a class whose order divides h/2); Q4 in the flattening
lattice's (rank r = M - J, height, the champion, the pure family); Q5
in the reader corpus's (tree cell, straddle, door, chain move, the
exit-index invariant, the intrinsic index).

TRANSPLANTS, MARKED.
  Q1 imports "the mechanism is where the negative factor hides" from
     the 0/1 corpus, where every coefficient is 1 and the integers
     carry nothing.
  Q2 imports "least" from the cubic seat's rank reading; a quadratic
     class's minimum is an explicit integer and the cubic place's is
     not.
  Q3 imports nothing; it is the parent's own print at its own next
     scope.
  Q4 imports "threshold as a function of the rank" from the mechanism's
     asymptotic argument in J, which says nothing about how the
     crossover depth moves with r.
  Q5 imports the chain-preferring slice's zero from R14; the oracle
     reader takes tree moves elsewhere, so its cells differ and the
     zero is not inherited.

THE HAND ATTACK, before any engine code.

  Q1. At a vertex w of the product's polytope the w-initial form of
      each factor f is one monomial c_f x^(v_f), and the monomial
      content the reader divides out is the monomial ALONE
      (explore_menu_faces.py primitive): the integer c_f stays, and
      the induced multiset keeps every c_f above 1. So a vertex grades
      a collision exactly when the multisets of vertex coefficients
      above 1 differ. Build one. Let n be a Z-irreducible with a
      negative coefficient and constant term 2, and A, B, C
      nonnegative Z-irreducibles with n*A, n*B, n*C all nonnegative
      and constant terms 1, 1, 2:

          n = x^2 - x + 2,  A = 1 + x,  B = 1 + x + x^2,  C = 2 + x,
          n*A = x^3 + x + 2,  n*B = x^4 + 2x^2 + x + 2,
          n*C = x^3 + x^2 + 4.

      The semiring's atom factorizations of P = n*A*B*C are the three
      ways of hiding n: {nA, B, C}, {nB, A, C}, {nC, A, B}. Each n*X
      is an atom: its Z-factorization is n times an irreducible, so
      its only proper regrouping exposes n, which is not in the
      semiring. At the constant vertex the induced multisets read
      (2, 2), (2, 2) and (4): the third differs from the first two,
      so delta = 0 for those pairs, a VERTEX grades the collision --
      and it grades the wrong thing, the grouping of the integer
      constants 2 and 2 against 4, while the mechanism is still where
      n hides, on the whole segment. Off the 0/1 frame the locator
      points at the coefficient ring's arithmetic and never at the
      hiding. The rig checks the identity, the nonnegativity, the
      irreducibility and the induced multisets in exact arithmetic
      through the parent's own descent reader, and reads the
      in-frame t = 6 identity and the (2,6) witness through the same
      reader as the positive control.

  Q2. Per field: S is the set of non-principal classes attaining the
      least non-principal minimum (normally a class and its inverse,
      since (a, b, c) and (a, -b, c) share a); the least odd split
      prime p1 and its class k1 are the parent's; the admissible set
      is the classes whose minimum p1 clears, k1 always among them
      (the parent's C4). The oracle's prediction is k1 in S; its
      weight under the reduction null is |S and admissible| /
      |admissible|, averaged over fields. Where p1 is below the least
      non-principal minimum both are zero and k1 is principal, so
      the same two numbers are read again over the fields where S is
      admissible. The share's null standard error is binomial, about
      0.008 at 4,044 fields, and 0.10 is twelve of them.

  Q3. The parent's bands of 4000 with per-field accumulation, carried
      from 32000 to 100000; a band above 32000 runs in 4 to 7 s, so
      the whole census is about two minutes. D's standard error is
      1/sqrt(sum of inverse variances) over the primes with at least
      15 fields in both columns; at three times the fields it falls
      by about sqrt(3) from 0.013 to about 0.0075.

  Q4. Ranks 9 and 10 through arm B's own rule: scan J upward from 2,
      past the first failure to the last, declared once the champion
      has attained h at CLEAR_RUN = 4 consecutive depths, ceiling
      140; ranks 5 to 8 rerun as the reprint. route_h is instant at
      rank 9 (timed before the freeze) and the cofactor bound is
      priced by partitions of r - 1. The four thresholds' plain
      least-squares line is 11.5r - 28.5 with residuals +2, -6.5, +7,
      -2.5, predicting 75 at rank 9 and 86.5 at rank 10; split by
      parity the odd ranks 31, 59 and even 34, 61 give 87 and 88.
      Each fit is read with the +-7 residual band of the line, and
      the union of the two is the window a rank law predicts:
      [68, 94] at rank 9 and [79, 95] at rank 10.

  Q5. The commit loop is the parent's verbatim
      (explore_seed_exclusion.py commit_step) with one line swapped:
      prefer_chain becomes a per-decision call. The oracle at a cell
      reads the cell's vertex v, its convergent index sigma in the
      family's own convergents, and the intrinsic indices ti, ci of
      the tree and chain references in play at that step; it says
      CHAIN iff sigma is defined and ti >= sigma + 1 and ci >= ti + 1,
      and TREE otherwise (a semiconvergent vertex, an undefined
      index, or either inequality failing). A door taken where the
      oracle said chain is a door with no chain move on offer -- a
      straddle at its maxed rung, where the commit loop wants a
      strict improvement -- and those are the exits the kill reads.
      The exit-index invariant is the parent's: once a run doors out
      of a vertex's family at index k, the ladder there never grows
      past k under any later chain reference. Two constant oracles
      are the controls: always-chain must reproduce the parent's
      chain-preferring exit tallies at every family, always-tree the
      tree-preferring ones.

PREDICTIONS, frozen before the run.
  P1. The identity holds exactly; the three factorizations are into
      atoms; the descent reader prints delta = 0 at the pair (1, 3)
      and (2, 3) and delta = 1 at (1, 2), where the constant-vertex
      multisets agree; the controls print 1 and 2.
  P2. The share of fields with k1 in S exceeds the weight by less
      than 0.05: minima admit, the parent's own reading, and the
      class the prime takes among the admissible ones is not the
      first one opened.
  P3. D at |D| <= 100000 lands within 0.02 of +0.030 with se under
      0.008, so the two-standard-error interval sits entirely under
      0.05.
  P4. J_ch(9) and J_ch(10) both exceed 61, J_ch = J_hi + 1 at both,
      and both fall in their windows.
  P5. The always-chain and always-tree controls reproduce the parent
      at every family; the oracle reader takes doors where the oracle
      said chain at every family, and zero of those exits violate.

KILLS AS OBSERVABLES. Each names what this rig PRINTS.
  Q1 is KILLED if the descent reader prints delta = 0 at any pair of
     the three factorizations with the identity, nonnegativity and
     atom checks all passing; it SURVIVES if every pair prints
     delta >= 1.
  Q2 is KILLED if share - weight < 2 se over all 4,044 fields
     (minima admit and never predict); CARRIED if share - weight - 2 se
     >= 0.10; BETWEEN otherwise, refrozen on the conditional read.
  Q3 is KILLED as norm-seated if D + 2 se < 0.05 at |D| <= 100000;
     CARRIED if D - 2 se >= 0.10; BETWEEN otherwise, with se printed.
  Q4 is KILLED if J_ch(9) is outside [68, 94] or J_ch(10) outside
     [79, 95] or either is not reached by J = 140 or J_ch != J_hi + 1
     at either rank; it SURVIVES otherwise, refrozen at ranks 11
     and 12 on the six-point fit.
  Q5 is KILLED if any exit from an oracle-said-chain door violates
     the invariant at any family; it SURVIVES if none does and such
     exits number above zero at every family, and is UNREAD at a
     family with none.

CONTROLS, run before any verdict is read.
  C1 (Q1) the in-frame identity (1+x^3)(1+x+x^2) = (1+x^2+x^4)(1+x)
     reads delta = 1 and the (2,6) witness of the parent reads
     delta = 2 through the same reader.
  C2 (Q2, Q3) the bands to 32000 reprint the parent: 4,044 fields,
     rank-1 share 0.657 within 0.005, reduction null 0.595 within
     0.005, D = +0.030 within 0.01; the least prime's own class
     clears its minimum at every field of every band.
  C3 (Q4) ranks 5 to 8 reprint J_ch = 31, 34, 59, 61 and J_ch = J_hi
     + 1 at each.
  C4 (Q5) the constant-chain oracle reproduces the parent's
     chain-preferring ("exit-inv", regime, held) tallies at all ten
     families and the constant-tree oracle the tree-preferring ones;
     the parent's R1 reprints (cyl: zero stale violations; dbl: some).

RESOURCE ENVELOPE. Under 512 MB (the parent's census peaked at
171 MB in 4000-bands); wall estimate five minutes: the census about
two, the rank scans and the reader sweeps a minute each.

FINDINGS (entered after the run; 15 controls run, 0 failed; 5
predictions, 1 missed; wall 155.5 s, peak working set 246.2 MB under
memwatch's 512 MB default).

  F1. A VERTEX GRADES A COLLISION OFF THE 0/1 FRAME. P = x^6 + 3x^5 +
      4x^4 + 7x^3 + 9x^2 + 8x + 4 has the three atom factorizations
      {nA, B, C}, {nB, A, C}, {nC, A, B}, every check passing; the
      reader prints delta = 1 at the pair (1, 2) and delta = 0 at
      (1, 3) and (2, 3), weight -1, induced multisets [2, 2] against
      [4]; the in-frame controls print 1 and 2. P1 held. Q1 KILLED:
      delta >= 1 is the 0/1 frame's own fact, and off it the descent
      dimension reads the integer content's grouping and never the
      hiding of n.

  F2. THE LEAST PRIME AVOIDS THE LEAST-MINIMUM CLASS. Over the 4,044
      fields the least odd split prime's class is a least-minimum
      non-principal class in 1,038, share 0.257 +- 0.007, against that
      class's weight 0.515 in the reduction null: excess -0.259, and
      1,022 of the 1,038 are fields where the prime EQUALS the minimum,
      so the least-minimum class takes the least prime almost only
      when the prime is its own minimum. The conditional read is the
      same read, since the least prime clears the least non-principal
      minimum at every field. At |D| <= 100000: 3,191 of 11,833, share
      0.270 +- 0.004, weight 0.526, excess -0.256, 3,175 at equality.
      P2 held. Q2 KILLED: minima admit and do not predict, and the
      first class reduction theory opens is the one the prime takes
      least, half the null's rate.

  F3. THE RANK CONTRAST SETTLES UNDER THE LINE. At |D| <= 100000,
      11,833 fields; rank-1 non-square share 0.640 +- 0.004, ranks 2
      to 5 at 0.582, 0.579, 0.558, 0.553; the reduction null 0.580;
      the rank-1 excess over it +0.060 (se 0.004), the same residual
      as at 32000 (+0.062) at four times the weight; the fixed-prime
      contrast D = +0.019 (se 0.0075), so D + 2 se = 0.034; the p = 5
      column reads 0.69 against 0.57 and p = 7 reads 0.55 against
      0.61, as before. Exactly one field to 100000 has its least prime
      above the principal form's line. P3 held. Q3 KILLED as
      norm-seated: what survives is a +0.060 residual over the
      reduction null that the fixed-prime rank contrast does not
      carry, so it is the form minimum wearing a rank or the
      prime-power term, and no order statistic.

  F4. THE THRESHOLD IS NO FUNCTION OF THE RANK, AND J_ch = J_hi + 1
      AT SIX RANKS. Ranks 5 to 8 reprint 31, 34, 59, 61 (C3). Rank 9:
      J_hi = 88, J_ch = 89, sixty failing depths from 12 to 88. Rank
      10: J_hi = 106, J_ch = 107, eighty-two failing depths from 24 to
      106. J_ch/r^2 reads 1.24, 0.94, 1.20, 0.95, 1.10, 1.07, so the
      parity alternation of the four dies at the fifth; 89 is inside
      [68, 94] and 107 is outside [79, 95], where the plain line said
      86.5 and the parity line 88. J_ch = J_hi + 1 at all six ranks.
      P4 MISSED at rank 10. Q4 KILLED: the closed form takes over at
      every rank swept, at a depth no fit of the ranks below predicts.
      The two rank scans took 1.6 s and 2.8 s.

  F5. THE ORACLE READER NEVER VIOLATES WHERE IT SAID CHAIN, AND DRIFTS
      MORE THAN THE READER THAT ALWAYS CHAINS. Both constant oracles
      reproduce the parent's exit tallies at all ten families (C4).
      The oracle reader takes 59,982 doors where the oracle said chain
      -- 8,687 at cyl and shift, 16,133 at mob1, 937 at tri -- every
      one in a policy-stale run, and violates the invariant at none.
      P5 held and the frozen kill MISSES. The print beside it: the
      reader's whole drift, every violating exit whatever the oracle
      said, ties always-chain at cyl and shift (15,212) and exceeds it
      at the other eight -- sb 28,610 against 27,010, mob1 29,464
      against 22,530, dbl and aff2 17,163 against 10,862, half 20,520
      against 14,045, mob2 25,523 against 16,234, tri 11,684 against
      8,054, mob3 23,083 against 15,073 -- and sits below always-tree
      everywhere. Q5 survives the kill as frozen and its headline
      fails on the same print: the reader handed the comparison does
      drift, at every family at least as much as the reader that needs
      no side channel, so the oracle buys nothing the chain preference
      did not already buy. Killed on the headline; the frozen kill was
      the narrower reading and is recorded as missed.

RUN RECORD. Two runs. The first counted the P4 miss as a control
failure -- the rig had one check function for controls and
predictions -- and printed no drift comparison; the second separated
the two and added the drift print, every number identical across
both. Second: wall 155.5 s, peak 246.2 MB. The census is 118 s of it,
the reader sweeps 30 s, the rank scans 5 s.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import math                                          # noqa: E402
import sys                                           # noqa: E402
import time                                          # noqa: E402
import itertools                                     # noqa: E402
from collections import defaultdict                  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy                                         # noqa: E402
from sympy import Poly                               # noqa: E402
import explore_menu_faces as MF                      # noqa: E402
import explore_four_prints as FP                     # noqa: E402
import explore_class_order as CO                     # noqa: E402
import explore_principal_share as PS                 # noqa: E402
import explore_flatten_band as FB                    # noqa: E402
import explore_reference_families as RF              # noqa: E402
import explore_scale_clock as SC                     # noqa: E402

CHECKS = [0, 0]
PREDS = [0, 0]


def ok(cond, msg):
    """A CONTROL: a failure here means the rig is not reading what it
    says it reads, and no verdict below it is read."""
    CHECKS[0] += 1
    if not cond:
        CHECKS[1] += 1
    print("  [%s] %s" % ("ok" if cond else "FAIL", msg))
    return bool(cond)


def pred(cond, msg):
    """A PREDICTION: a miss here is a finding, never a rig failure."""
    PREDS[0] += 1
    if not cond:
        PREDS[1] += 1
    print("  [%s] %s" % ("held" if cond else "MISSED", msg))
    return bool(cond)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# =============================================================== Q1

def nonneg(p, x):
    return all(c >= 0 for c in Poly(p, x).all_coeffs())


def z_irreducible(p, x):
    c, fl = sympy.factor_list(p, x)
    return c == 1 and len(fl) == 1 and fl[0][1] == 1


def q1():
    section("Q1  THE DESCENT LOCATOR -- does delta >= 1 survive a coefficient "
            "above 1?")
    x = sympy.symbols("x")
    n = x**2 - x + 2
    A, B, C = 1 + x, 1 + x + x**2, 2 + x
    nA, nB, nC = (sympy.expand(n * A), sympy.expand(n * B),
                  sympy.expand(n * C))
    print("  n = %s   A = %s   B = %s   C = %s" % (n, A, B, C))
    print("  n*A = %s   n*B = %s   n*C = %s" % (nA, nB, nC))
    facs = {1: [nA, B, C], 2: [nB, A, C], 3: [nC, A, B]}
    P = sympy.expand(n * A * B * C)
    ok(all(sympy.expand(sympy.prod(f)) == P for f in facs.values()),
       "the three factorizations multiply to the same P = %s" % P)
    ok(all(nonneg(f, x) for fl in facs.values() for f in fl),
       "every factor of every factorization is nonnegative")
    ok(all(z_irreducible(p, x) for p in (n, A, B, C)),
       "n, A, B, C are Z-irreducible with content 1")
    ok(any(c < 0 for c in Poly(n, x).all_coeffs()),
       "n carries a negative coefficient, so n is not in the semiring")
    for nm, p in (("n*A", nA), ("n*B", nB), ("n*C", nC)):
        _, fl = sympy.factor_list(p, x)
        ok(len(fl) == 2 and all(e == 1 for _, e in fl)
           and any(sympy.expand(f - n) == 0 for f, _ in fl),
           "%s factors over Z as n times one irreducible, so it is an "
           "atom of the semiring" % nm)
    print("  controls: the in-frame identity and the (2,6) witness")
    d_c1 = MF.descent([1 + x**3, 1 + x + x**2], [1 + x**2 + x**4, 1 + x],
                      [x])
    print("    t = 6 identity: dim %d, delta %d" % (d_c1[0], d_c1[1]))
    y0, y1 = sympy.symbols("x0 x1")
    w1 = [y0 + y1, y0**3 * y1 + y0**3 + y0**2 + y0 * y1**2 + y1**2 + y1]
    w2 = [y0 + 1, y0**3 * y1 + y0**3 + y0**2 * y1**2 + y0 * y1 + y1**3
          + y1**2]
    d_c2 = MF.descent(w1, w2, [y0, y1])
    print("    (2,6) witness: dim %d, delta %d" % (d_c2[0], d_c2[1]))
    ok(d_c1[1] == 1 and d_c2[1] == 2, "C1 the reader prints delta = 1 and "
       "delta = 2 at the two in-frame controls")
    deltas = {}
    for i, j in ((1, 2), (1, 3), (2, 3)):
        dim, d, w = MF.descent(facs[i], facs[j], [x])
        deltas[(i, j)] = d
        ind_i = MF.induced(facs[i], [x], w) if w is not None else None
        ind_j = MF.induced(facs[j], [x], w) if w is not None else None
        print("  pair (%d, %d): dim %d, delta %d, weight %s; induced %s "
              "against %s" % (i, j, dim, d, w,
                              [sympy.sympify(s) for s in ind_i]
                              if ind_i else ind_i,
                              [sympy.sympify(s) for s in ind_j]
                              if ind_j else ind_j))
    pred(deltas[(1, 2)] == 1 and deltas[(1, 3)] == 0 and deltas[(2, 3)] == 0,
         "P1 delta = 1 at (1, 2) and delta = 0 at (1, 3) and (2, 3)")
    killed = min(deltas.values()) == 0
    print("  Q1 verdict: %s -- a vertex %s a collision off the 0/1 frame"
          % ("KILLED" if killed else "SURVIVES",
             "grades" if killed else "never grades"))
    return killed, deltas


# ============================================================ Q2, Q3

class Acc2(FP.Acc):
    def __init__(self):
        FP.Acc.__init__(self)
        self.pred = [0, 0]          # k1 in S, fields
        self.weight = []            # |S and avail| / |avail|
        self.pred_c = [0, 0]        # the same over fields with S admissible
        self.weight_c = []
        self.eq_min = 0             # p1 equals the least non-principal minimum


def band_census(sign, lo, hi, plist, acc):
    """The parent's band_census with the minimum-oracle read added."""
    gen = PS.fundamental_discriminants

    def banded(a, b, s):
        for D in gen(1, b, s):
            if abs(D) > lo:
                yield D
    old_gen, old_b = CO.fundamental_discriminants, CO.DBOUND
    CO.fundamental_discriminants = banded
    CO.DBOUND = hi
    try:
        rows, _bad, _ib, _c2, _c4, _lb = CO.sweep(sign, plist)
    finally:
        CO.fundamental_discriminants = old_gen
        CO.DBOUND = old_b
    for D, hplus, recs, orders, _n0, _t0, _q, hits in rows:
        h = hplus
        if h % 2 or h < 2 or max(orders.values()) != h:
            continue
        acc.fields += 1
        triv = next(k for k, rec in recs.items() if rec[0])
        line = triv[2]
        p1, k1 = hits[0]
        if p1 > line:
            acc.above_line += 1

        def minimum(k):
            return k[2] if k == triv else k[0]
        avail = [k for k in orders if minimum(k) <= p1]
        if k1 not in avail:
            acc.own_not_avail += 1
        acc.avail_sizes.append(len(avail))
        ns_avail = sum(1 for k in avail if not FP.is_square(orders[k], h))
        acc.red_null.append(ns_avail / len(avail))
        for i, (p, k) in enumerate(hits[:8]):
            ns = not FP.is_square(orders[k], h)
            acc.rank[i + 1][0] += ns
            acc.rank[i + 1][1] += 1
            if p <= 50:
                (acc.pr1 if i == 0 else acc.prk)[p][0] += ns
                (acc.pr1 if i == 0 else acc.prk)[p][1] += 1
        # the minimum oracle
        nonp = [k for k in orders if k != triv]
        m = min(k[0] for k in nonp)
        S = [k for k in nonp if k[0] == m]
        hit = k1 in S
        wt = sum(1 for k in S if k in avail) / len(avail)
        acc.pred[0] += hit
        acc.pred[1] += 1
        acc.weight.append(wt)
        if p1 >= m:
            acc.pred_c[0] += hit
            acc.pred_c[1] += 1
            acc.weight_c.append(wt)
        if p1 == m:
            acc.eq_min += 1
    del rows


def read_oracle(acc, tag):
    sh = acc.pred[0] / acc.pred[1]
    se = math.sqrt(sh * (1 - sh) / acc.pred[1])
    wt = sum(acc.weight) / len(acc.weight)
    print("  %s: least prime's class IS a least-minimum non-principal "
          "class in %d of %d fields, share %.3f +- %.3f; that class's "
          "weight in the reduction null %.3f; excess %+.3f"
          % (tag, acc.pred[0], acc.pred[1], sh, se, wt, sh - wt))
    shc = acc.pred_c[0] / acc.pred_c[1]
    sec = math.sqrt(shc * (1 - shc) / acc.pred_c[1])
    wtc = sum(acc.weight_c) / len(acc.weight_c)
    print("    over the %d fields where that class is admissible: share "
          "%.3f +- %.3f, weight %.3f, excess %+.3f; the least prime EQUALS "
          "the least non-principal minimum in %d fields"
          % (acc.pred_c[1], shc, sec, wtc, shc - wtc, acc.eq_min))
    return sh, se, wt, shc, sec, wtc


def q23():
    section("Q2, Q3  THE MINIMUM ORACLE and THE RANK-SEATED BIAS -- the "
            "imaginary fields to |D| <= 100000")
    plist = PS.primes_upto(CO.PCAP)
    acc = Acc2()
    t0 = time.time()
    for lo in range(0, 32000, 4000):
        band_census(-1, lo, lo + 4000, plist, acc)
    print("  bands to 32000 done, %d fields (%.1fs)"
          % (acc.fields, time.time() - t0))
    (sh, se), nl, (Dc, Dse) = FP.read_acc(acc, "C2 reprint, |D| <= 32000")
    ok(acc.fields == 4044 and abs(sh - 0.657) <= 0.005
       and abs(nl - 0.595) <= 0.005 and abs(Dc - 0.030) <= 0.01,
       "C2 reprint of 4,044 fields, 0.657, null 0.595, D = +0.030")
    ok(acc.own_not_avail == 0, "C2 the least prime's own class clears "
       "its minimum at every field to 32000")
    o = read_oracle(acc, "Q2 at |D| <= 32000")
    exc = o[0] - o[2]
    if exc < 2 * o[1]:
        v2 = "KILLED -- minima admit and never predict"
    elif exc - 2 * o[1] >= 0.10:
        v2 = "CARRIED"
    else:
        v2 = "BETWEEN"
    pred(exc < 0.05, "P2 the share exceeds the weight by less than 0.05")
    print("  Q2 verdict: %s (excess %+.3f, se %.3f)" % (v2, exc, o[1]))
    for lo in range(32000, 100000, 4000):
        band_census(-1, lo, lo + 4000, plist, acc)
        print("  band (%d, %d] done, %d fields (%.1fs)"
              % (lo, lo + 4000, acc.fields, time.time() - t0))
    ok(acc.own_not_avail == 0, "C2 the least prime's own class clears "
       "its minimum at every field to 100000")
    (sh, se), nl, (Dc, Dse) = FP.read_acc(acc, "Q3 at |D| <= 100000")
    o100 = read_oracle(acc, "the oracle read again at |D| <= 100000")
    if Dc + 2 * Dse < 0.05:
        v3 = "KILLED -- norm-seated"
    elif Dc - 2 * Dse >= 0.10:
        v3 = "CARRIED"
    else:
        v3 = "BETWEEN"
    pred(Dse < 0.008, "P3 D's standard error under 0.008 (%.4f)" % Dse)
    print("  Q3 verdict: %s (D %+.3f se %.3f; rank-1 excess over the "
          "reduction null %+.3f se %.3f; %d fields)"
          % (v3, Dc, Dse, sh - nl, se, acc.fields))
    return v2, v3, (sh, se, nl, Dc, Dse, acc.fields, o, o100)


# =============================================================== Q4

RANKS = (5, 6, 7, 8, 9, 10)
WINDOW = {9: (68, 94), 10: (79, 95)}
REPRINT = {5: 31, 6: 34, 7: 59, 8: 61}


def scan_rank(r):
    """Arm B's rule, the parent's verbatim: J upward past the first
    failure to the last, declared after CLEAR_RUN depths at which the
    champion attains h."""
    fails = []
    run = 0
    first_ch = None
    seen = False
    for J in range(2, FB.HIGH_JCAP + 1):
        M = J + r
        xm1 = FB.xm1_pow(J)
        h, v, nodes, ph, pw = FB.cell(M, J, xm1)
        if h > ph:
            print("   K h above the pure bound at M=%d J=%d" % (M, J))
        if h < ph:
            seen = True
            fails.append(J)
        c = FB.champ(r, J)
        if c is not None and h == FB.height(c):
            if run == 0:
                first_ch = J
            run += 1
        else:
            run, first_ch = 0, None
        if seen and run >= FB.CLEAR_RUN:
            break
    done = seen and run >= FB.CLEAR_RUN
    return (fails[-1] if done else None), (first_ch if done else None), fails


def q4():
    section("Q4  THE CLOSED-FORM FILTER -- the champion's threshold at "
            "ranks 9 and 10")
    t0 = time.time()
    JHI, JCH = {}, {}
    for r in RANKS:
        t = time.time()
        jhi, jch, fails = scan_rank(r)
        JHI[r], JCH[r] = jhi, jch
        print("  rank %2d: J_hi %s, J_ch %s, %d failing depths %s..%s, "
              "J_ch/r^2 %s (%.1fs)"
              % (r, jhi, jch, len(fails), fails[0] if fails else "-",
                 fails[-1] if fails else "-",
                 "%.2f" % (jch / r**2) if jch else "-", time.time() - t))
    ok(all(JCH[r] == REPRINT[r] for r in REPRINT),
       "C3 ranks 5..8 reprint J_ch = 31, 34, 59, 61")
    ok(all(JCH[r] is not None and JCH[r] == JHI[r] + 1 for r in REPRINT),
       "C3 J_ch = J_hi + 1 at ranks 5..8")
    reached = all(JCH[r] is not None for r in WINDOW)
    plus1 = reached and all(JCH[r] == JHI[r] + 1 for r in WINDOW)
    inwin = reached and all(WINDOW[r][0] <= JCH[r] <= WINDOW[r][1]
                            for r in WINDOW)
    above = reached and all(JCH[r] > 61 for r in WINDOW)
    pred(above and plus1 and inwin, "P4 both thresholds above 61, both "
         "J_hi + 1, both inside their windows")
    # the fits the windows came from, printed against the prints
    rs = [5, 6, 7, 8]
    js = [JCH[r] for r in rs]
    mr, mj = sum(rs) / 4, sum(js) / 4
    slope = (sum((a - mr) * (b - mj) for a, b in zip(rs, js))
             / sum((a - mr) ** 2 for a in rs))
    print("  plain line through ranks 5..8: slope %.2f, predicts %.1f at 9 "
          "and %.1f at 10; parity lines predict 87 and 88"
          % (slope, mj + slope * (9 - mr), mj + slope * (10 - mr)))
    killed = not (reached and plus1 and inwin)
    print("  Q4 verdict: %s (J_ch(9) = %s in [68, 94]? J_ch(10) = %s in "
          "[79, 95]?) in %.1fs"
          % ("KILLED" if killed else "SURVIVES", JCH[9], JCH[10],
             time.time() - t0))
    return killed, JHI, JCH


# =============================================================== Q5

def commit_oracle(C, ref_t, ref_c, prefer):
    """explore_seed_exclusion.py commit_step, verbatim but for the one
    line that reads the preference: a per-decision call on the cell."""
    records = []
    guard = 0
    while True:
        guard += 1
        if guard > 10 ** 6:
            raise AssertionError("commit loop runaway")
        cand_tree = cand_chain = None
        if C[0] == "T":
            _, l, r, d = C
            v = SC.mediant(l, r)
            if ref_t is not None:
                for ch in (("T", l, v, d + 1), ("T", v, r, d + 1)):
                    if SC.contains(ch, ref_t):
                        cand_tree = ch
                        break
            if ref_c is not None:
                k = SC.chain_kmax(v, l, r, ref_c)
                if k >= 1:
                    cand_chain = ("S", v, l, r, d, k)
        else:
            _, v, l, r, d, k = C
            if ref_c is not None:
                k2 = SC.chain_kmax(v, l, r, ref_c)
                if k2 > k:
                    cand_chain = ("S", v, l, r, d, k2)
            if ref_t is not None:
                mL, mR = SC.interval(C)
                for ch in (("T", mL, v, d + k + 1),
                           ("T", v, mR, d + k + 1)):
                    if SC.contains(ch, ref_t):
                        cand_tree = ch
                        break
        prefer_chain = prefer(C)
        if cand_tree is None and cand_chain is None:
            records.append((C, None, None, "halt"))
            return C, records
        if cand_chain is not None and (cand_tree is None or prefer_chain):
            records.append((C, cand_tree, cand_chain, "chain"))
            C = cand_chain
        else:
            records.append((C, cand_tree, cand_chain, "door"))
            C = cand_tree


def trace_oracle(refs, ridx, fcvs, P, pc, mode, tally):
    """One run over one family under the oracle (mode 'oracle') or a
    constant preference ('chain', 'tree'). Tallies, per regime: doors
    and exits by what the oracle said, and the exit-index invariant."""
    reg = RF.regime(P, pc)
    h = len(refs)
    C = SC.ROOT
    exits = []
    for n in range(h):
        rt = refs[n - P] if P is not None and n - P >= 0 else None
        rc = refs[n - pc] if pc is not None and n - pc >= 0 else None
        ti = ridx[n - P] if P is not None and n - P >= 0 else None
        ci = ridx[n - pc] if pc is not None and n - pc >= 0 else None

        def prefer(cell):
            if mode == "chain":
                return True
            if mode == "tree":
                return False
            v = RF.cell_vertex(cell)[0]
            sig = RF.conv_index(fcvs, v)
            return (sig is not None and ti is not None and ci is not None
                    and ti >= sig + 1 and ci >= ti + 1)
        try:
            C, records = commit_oracle(C, rt, rc, prefer)
        except AssertionError:
            tally[("runaway", reg)] += 1
            return False
        for cell, cand_tree, cand_chain, took in records:
            if took != "door":
                continue
            said = "said-chain" if prefer(cell) else "said-tree"
            v, l, r, k = RF.cell_vertex(cell)
            tally[("door", reg, said)] += 1
            exits.append((v, l, r, k, n, said))
    for v, l, r, k, n1, said in exits:
        worst = k
        for m in range(n1 + 1, h):
            if pc is None or m - pc < 0:
                continue
            worst = max(worst, SC.chain_kmax(v, l, r, refs[m - pc]))
        held = worst <= k
        tally[("exit-inv", reg, held)] += 1
        tally[("exit", reg, said, held)] += 1
    return True


def sweep(name, mode):
    tally = defaultdict(int)
    for alpha, hh in RF.SCANS:
        for digs in itertools.product(alpha, repeat=hh):
            fam = RF.build_family(name, digs)
            if fam is None:
                continue
            refs, fdigs, fcvs, fcyls = fam
            ridx = [RF.intrinsic_index(iv, fcyls) for iv in refs]
            for P, pc in RF.RUNS:
                trace_oracle(refs, ridx, fcvs, P, pc, mode, tally)
    return tally


def exitinv(tally):
    return {k: v for k, v in tally.items() if k[0] == "exit-inv" and v}


def q5():
    section("Q5  THE INDEX ORACLE -- a reader handed the door inequalities")
    t0 = time.time()
    print("  C4 the constant oracles against the parent's two slices "
          "(exit-inv tallies, all regimes)")
    allok = True
    for name in RF.FAMILIES:
        tp_c = RF.scan_family(name, pref=RF.CHAIN_PREF)[0]
        tp_t = RF.scan_family(name, pref=RF.TREE_PREF)[0]
        mc = sweep(name, "chain")
        mt = sweep(name, "tree")
        same = (exitinv(tp_c) == exitinv(mc) and exitinv(tp_t) == exitinv(mt))
        allok &= same
        print("    %-6s chain %s  tree %s  %s"
              % (name, sorted(exitinv(mc).items()),
                 sorted(exitinv(mt).items()), "same" if same else "DIFFER"))
    ok(allok, "C4 both constant oracles reproduce the parent at all ten "
       "families")
    cyl = sweep("cyl", "chain")
    dbl = sweep("dbl", "chain")
    ok(cyl[("exit-inv", "stale", False)] == 0
       and cyl[("exit-inv", "stale", True)] > 0
       and dbl[("exit-inv", "stale", False)] > 0,
       "C4 R1 reprints: cyl zero stale violations, dbl some")
    print("  the oracle reader, exits by what the oracle said at the door")
    print("  %-6s %10s %10s %10s %10s %10s %10s"
          % ("family", "chainExit", "chainVIOL", "treeExit", "treeVIOL",
             "stChainEx", "stChainVI"))
    tot_ce = tot_cv = 0
    unread = []
    drift = []
    for name in RF.FAMILIES:
        t = sweep(name, "oracle")
        tc = sweep(name, "chain")
        tt = sweep(name, "tree")
        drift.append((name,
                      sum(v for k, v in t.items()
                          if k[0] == "exit-inv" and not k[2]),
                      sum(v for k, v in tc.items()
                          if k[0] == "exit-inv" and not k[2]),
                      sum(v for k, v in tt.items()
                          if k[0] == "exit-inv" and not k[2])))
        ce = sum(v for k, v in t.items() if k[0] == "exit"
                 and k[2] == "said-chain")
        cv = sum(v for k, v in t.items() if k[0] == "exit"
                 and k[2] == "said-chain" and not k[3])
        te = sum(v for k, v in t.items() if k[0] == "exit"
                 and k[2] == "said-tree")
        tv = sum(v for k, v in t.items() if k[0] == "exit"
                 and k[2] == "said-tree" and not k[3])
        sce = t[("exit", "stale", "said-chain", True)] \
            + t[("exit", "stale", "said-chain", False)]
        scv = t[("exit", "stale", "said-chain", False)]
        print("  %-6s %10d %10d %10d %10d %10d %10d"
              % (name, ce, cv, te, tv, sce, scv))
        tot_ce += ce
        tot_cv += cv
        if ce == 0:
            unread.append(name)
    pred(tot_ce > 0 and tot_cv == 0 and not unread,
         "P5 oracle-said-chain exits at every family, none violating")
    if tot_cv > 0:
        v5 = "KILLED"
    elif unread:
        v5 = "SURVIVES, UNREAD at %s" % unread
    else:
        v5 = "SURVIVES"
    print("  Q5 verdict on the frozen kill: %s (%d oracle-said-chain "
          "exits, %d violating)" % (v5, tot_ce, tot_cv))
    # THE PRINT BESIDE THE KILL: the reader's whole drift, every
    # violating exit whatever the oracle said, against the two constant
    # readers that need no side channel. Read after the verdict above
    # and never folded into it; the docstring says what it found.
    print("  the whole drift, violating exits over every door: oracle "
          "reader / always-chain / always-tree")
    worse = 0
    for name, a, b, c in drift:
        print("    %-6s %8d %8d %8d   oracle %s always-chain"
              % (name, a, b, c,
                 "above" if a > b else ("ties" if a == b else "below")))
        worse += a >= b
    print("  the oracle reader drifts at least as much as always-chain at "
          "%d of %d families (%.1fs)" % (worse, len(drift),
                                          time.time() - t0))
    return v5, tot_ce, tot_cv, drift


# ============================================================== main

def main():
    t0 = time.time()
    print("explore_five_prints.py -- five kills at one sweep")
    r1 = q1()
    r23 = q23()
    r4 = q4()
    r5 = q5()
    section("SUMMARY")
    print("  Q1 descent locator:  %s" % ("KILLED" if r1[0] else "SURVIVES"))
    print("  Q2 minimum oracle:   %s" % r23[0])
    print("  Q3 rank-seated bias: %s" % r23[1])
    print("  Q4 closed-form filter: %s" % ("KILLED" if r4[0] else "SURVIVES"))
    print("  Q5 index oracle:     %s" % r5[0])
    print("  controls: %d run, %d failed; predictions: %d, %d missed; "
          "wall %.1fs" % (CHECKS[0], CHECKS[1], PREDS[0], PREDS[1],
                          time.time() - t0))
    return 0 if CHECKS[1] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
