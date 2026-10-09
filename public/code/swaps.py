"""swaps.py -- how an optimum that abandons an atom turns into one that
serves it: the two mass bounds, the level-excess identity, and the
exchange every serving optimum is, with the arithmetic that can forbid
the simple ones.

QUESTION. fates.py reads which atoms the marginal optimum abandons.
An atom abandoned by SOME optimum but not by every one has a serving
optimum too; what exchange carries the one to the other, and what
decides whether a simple exchange exists? And how far does the level
alone confine which atoms can be abandoned at all?

THE OBJECTS (sets.py's and fates.py's). A rule takes the top R_q
labels at atom q, costing sum w_q R_q and covering sum w_q P(q, R_q),
P(q, s) the sum of q's s largest posteriors. D_R = cov(R) - T is a
rule's overshoot, D the certificate's. For the pairs A above t* and B
below it, the EXCESS of a pair is w |p - t*|; E_A is the whole excess
above, e(X) the excess of the above pairs X a rule drops, f(Y) of the
below pairs Y it buys. psi_q is the posterior mass q holds at or above
t*, psi_max the largest.

THE ARGUMENT (written before the engine).
  (A) TWO MASS BOUNDS (property). A rule abandoning r covers T from the
      other atoms, whose whole mass is 1 - w_r: so w_r <= 1 - T for
      every atom any feasible rule abandons. An atom wholly below t*
      holds none of the pairs {p >= t*} that cover T, so
      T <= sum_{q != r} w_q psi_q <= (1 - w_r) psi_max, and
      w_r <= 1 - T/psi_max, the stronger bound since psi_max <= 1.
  (B) THE LEVEL-EXCESS IDENTITY (property). Splitting each pair's cost
      as w = w p/t* + w (t* - p)/t* and summing over a rule R,
          t* cost(R) = cov(R) - E_A + e(X) + f(Y),
      so, the certificate dropping and buying nothing,
          t* (cost(R) - CERT) = e(X) + f(Y) + D_R - D.
      A rule beats the certificate iff its dropped excess, bought
      excess and own overshoot together fall under D. The price-gap
      test of sets.py is the case D < least single-pair excess.
  (C) THE EXCHANGE (property). Let R abandon r and R' serve it at size
      s, both optima. On the partners where R' is lower it DROPS d_i
      labels, where higher it GAINS a_j; both costing OPT,
          sum_S w_i d_i - sum_G w_j a_j = s w_r
      exactly. The DOMINATED exchanges are G empty; the SWAP is one
      partner at depth 1. So a dominated rescue is a divisibility
      fact: some depth-capped drop-set (d_i <= R_i) weighs exactly
      s w_r. Where none does (NO-DROP), every rescue gains somewhere.
  (D) THE SWAP LEMMA (property). If R abandons r and holds on a
      partner r' a lowest label of posterior p with s w_r <= w_r' and
      w_r' p <= w_r P(r, s) + D_R, the rule trading that label for r's
      top s costs at most OPT and covers T: an optimum serving r, and
      by (C) then s w_r = w_r'.
  (E) THE FULL PARTNER (property). If R serves a partner i fully
      (R_i = k) and w_i d = s w_r with d, s <= k, dropping i's lowest d
      loses at most w_i d/k of coverage (the lowest d of k posteriors
      average at most 1/k) and r's top s gain at least s w_r/k: so the
      trade is an optimum serving r with no coverage condition to check.

DESIGN. The cells of fates.py (sets.py's sweep and the four-atom arm),
every optimum enumerated. At every optimum: (A) at every abandoned
atom and every wholly-below atom ((B) and the signed balance of (C) are
argued, no longer computed: see the ruling after KILL). At every atom
some optimum abandons and some serves: every pair of the two and its
shape; each abandoning optimum's
dominated rescue or its kind of gain case, ARITHMETIC (NO-DROP) or
COVERAGE (a drop-set balances and every dominated rule falls short);
(D) and (E) fired wherever their hypotheses hold and the traded rule
checked.

PREDICTIONS (fixed before the engine).
  K1 CONTROL: the lemma fires at some abandoning optimum and some
     abandoning optimum is NO-DROP (the readers can print both).
  P1 (A) both bounds hold at every atom they read; the tightest ratio
     to each bound is printed.
  P2 (B) the identity holds at every optimum of every cell.
  P3 (C) the balance holds at every pair; no NO-DROP optimum has a
     dominated rescue.
  P4 (D), (E) every rule they build is an optimum serving r.
  P5 some atom abandoned by some optimum is rescued only by gain
     exchanges, an ARITHMETIC case among them.

KILL. K1 off: nothing is read. P1 to P4 off: an argument above is
wrong. P5 off: at this sweep the dominated exchange is the whole rescue.
[Read later, on a code read: P2's identity holds for every rule by the
algebra of (B), and P3's balance and its NO-DROP clause follow from both
rules costing OPT, so neither is checked now; K1 runs first and stops
the run if it fails, and P1' counts the atoms with a label at or above
t* that an optimum abandons past 1 - T/psi_max.]

FINDINGS. No kill fired. One frozen phrase overreached: (A)'s second
bound covers the atoms wholly below t*, not the abandoned ones, so it
is not a stronger bound on the same set (an optimum can abandon an
atom above it). K1 is read in the same section as P3 to P5 and
holds.
  bounds   both hold, and both are attained: the largest abandoned
            mass equals 1 - T and the largest wholly-below mass equals
            1 - T/psi_max (ratio 1.0000 each).
  excess    the identity held at all 6,832 optima (run 1; no longer
            computed).
  exchange  2,065 (abandoning, serving) pairs of optima, the balance
            exact at every one (run 1; no longer computed). Of the
            1,047 (atom, abandoning optimum)
            pairs with a serving optimum, 908 have a dominated rescue,
            37 are ARITHMETIC (NO-DROP) and 102 COVERAGE gain cases; no
            NO-DROP optimum has a dominated rescue. The lemma fired 991
            times and the full-partner trade 123, every built rule an
            optimum serving r. The first ARITHMETIC case: w = (1/20,
            1/2, 9/20), rows (4/5, 1/10, 1/10), (3/5, 2/5, 0),
            (3/5, 1/5, 1/5), t* = 2/5, OPT 29/20; atom 0, above the
            level, is abandoned by (0, 2, 1), covering 0.77, and served
            only by (1, 1, 2), covering 0.70: one label of mass 1/2
            dropped, one of mass 9/20 gained, 1/2 - 9/20 = 1/20, while
            no drop-set of R weighs 1/20, 1/10 or 3/20.

RUN RECORD. python swaps.py: run 1, 6 of 6, 1.8 s, peak commit 31.2 MB.
After a code read, 5 of 5, 1.8 s, peak commit 30.8 MB: both bounds
attained exactly (ratios 1 and 1), P1' at 18 (atom, cell) cases, and
the ARITHMETIC case's rules covering 77/100 and 7/10.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from fractions import Fraction as F

from fates import Fates, four_arm
from sets import T, sweep

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail
                                                     else ""))


def section(title):
    print()
    print(title)
    print("-" * len(title))


def cost(x, R):
    return sum(x.an.sc.W[q] * R[q] for q in range(x.cell.M))


def cov(x, R):
    return sum(x.an.sc.V[q][R[q]] for q in range(x.cell.M))


def is_opt(x, R):
    return cov(x, R) >= x.an.sc.TQ and cost(x, R) == x.opt


def no_drop(x, R, r):
    """True when no drop-set d_q <= R_q over the partners weighs s w_r."""
    sc, k = x.an.sc, x.cell.k
    parts = [q for q in range(x.cell.M) if q != r and R[q] > 0]
    sums = {0}
    for q in parts:
        sums = {v + d * sc.W[q] for v in sums for d in range(R[q] + 1)}
    return not any(s * sc.W[r] in sums for s in range(1, k + 1))


def section_mass_bounds(fates):
    section("TWO MASS BOUNDS (A)")
    bad, past, t1, t2 = 0, 0, F(0), F(0)
    for x in fates:
        t = x.an.t
        psi = [sum(p for p in row if p >= t) for row in x.cell.srt]
        pmax = max(psi)
        for r in range(x.cell.M):
            w = x.cell.w[r]
            if any(R[r] == 0 for R in x.opts):
                bad += w > 1 - T
                t1 = max(t1, w / (1 - T))
                past += x.cell.srt[r][0] >= t and w > 1 - T / pmax
            if x.cell.srt[r][0] < t:
                bad += w > 1 - T / pmax
                t2 = max(t2, w / (1 - T / pmax))
    print(f"  tightest abandoned mass over 1 - T: {t1}; tightest "
          f"wholly-below mass over 1 - T/psi_max: {t2}")
    check("P1 both bounds hold at every atom they read, each attained",
          bad == 0 and t1 == t2 == 1, f"{bad} violations")
    check("P1' (after a code read) some atom with a label at or above t* "
          "is abandoned past 1 - T/psi_max", past > 0,
          f"{past} (atom, cell) cases")


def section_exchange(fates):
    section("THE EXCHANGE (C), THE SWAP (D), THE FULL PARTNER (E)")
    lemma_bad = full_bad = 0
    lemma = full = pairs = 0
    kinds = {"dominated": 0, "arithmetic": 0, "coverage": 0}
    nodrop_seen = 0
    example = None
    for x in fates:
        sc, M, k = x.an.sc, x.cell.M, x.cell.k
        for r in range(M):
            ab = [R for R in x.opts if R[r] == 0]
            sv = [R for R in x.opts if R[r] > 0]
            for R in ab:
                nd = no_drop(x, R, r)
                nodrop_seen += nd
                dom = False
                for R2 in sv:
                    pairs += 1
                    if all(R2[q] <= R[q] for q in range(M) if q != r):
                        dom = True
                if sv:
                    if dom:
                        kinds["dominated"] += 1
                    else:
                        kinds["arithmetic" if nd else "coverage"] += 1
                        if nd and example is None:
                            example = (x, r, R, sv)
                DR = cov(x, R) - sc.TQ
                for q in range(M):
                    if q == r or R[q] == 0:
                        continue
                    low = sc.V[q][R[q]] - sc.V[q][R[q] - 1]
                    for s in range(1, k + 1):
                        if (s * sc.W[r] <= sc.W[q]
                                and low <= sc.V[r][s] + DR):
                            lemma += 1
                            R2 = list(R)
                            R2[q] -= 1
                            R2[r] = s
                            lemma_bad += not (is_opt(x, R2)
                                              and s * sc.W[r] == sc.W[q])
                    if R[q] == k:
                        for d in range(1, k + 1):
                            for s in range(1, k + 1):
                                if d * sc.W[q] == s * sc.W[r]:
                                    full += 1
                                    R2 = list(R)
                                    R2[q] -= d
                                    R2[r] = s
                                    full_bad += not is_opt(x, R2)
    print(f"  {pairs} (abandoning, serving) pairs of optima; (atom, "
          f"abandoning optimum) pairs with a serving one: {kinds}")
    print(f"  the swap lemma fired {lemma} times, the full-partner trade "
          f"{full} times")
    check("K1 the lemma fires and a NO-DROP optimum occurs",
          lemma > 0 and nodrop_seen > 0)
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        sys.exit(1)
    check("P4 every rule the lemma and the full-partner trade build is an "
          "optimum serving r", lemma_bad == 0 and full_bad == 0,
          f"{lemma_bad} and {full_bad} failures")
    if example:
        x, r, R, sv = example
        print(f"  first ARITHMETIC case: w {[str(v) for v in x.cell.w]}, "
              f"rows {[[str(v) for v in row] for row in x.cell.srt]}, t* "
              f"{x.an.t}, OPT {x.value(x.opt)}")
        print(f"     atom {r}: abandoning {R}, covering "
              f"{x.value(cov(x, R))}; serving {sv}, covering "
              f"{[str(x.value(cov(x, R2))) for R2 in sv]}")
    check("P5 an atom rescued only by gain exchanges, an ARITHMETIC case "
          "among them", kinds["arithmetic"] > 0)


def main():
    t0 = time.time()
    fates = [Fates(c) for c in sweep() + four_arm()]
    section_exchange(fates)
    section_mass_bounds(fates)
    print()
    print(f"{sum(CHECKS)} of {len(CHECKS)} checks, "
          f"{time.time() - t0:.1f} s")
    sys.exit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
