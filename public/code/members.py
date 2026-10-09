"""members.py -- what the least-height polynomials are made of where
products of x^d - 1 lose: the factor they carry that is not cyclotomic,
the construction that rebuilds them from a pure product, and whether
the inverse dial's break is the same phenomenon.

QUESTION. flatten.py finds h(M, J) < ph(M, J) at 83 cells of the chart
and one break on the inverse dial, d_8(15) = 55 against a least pure
degree of 56, where the witness is a pure product with ten degrees of
it traded for a factor that is not cyclotomic. Are the chart's
failures the same trade? If so, what are the traded factors, can the
trade be run forward as a construction with no lattice reduction in
it, and is the dial -- one lattice decision per cell, stopping at the
first vector found -- a cheaper place to hunt for new factors than the
chart?

THE OBJECTS (flatten.py's senses). A vector of width M is P(x) =
sum c_i x^i of degree < M; its HEIGHT is max |c_i|; h(M, J) is the
least height of a nonzero P with (x - 1)^J | P; the PURE PRODUCTS are
prod (x^{g_i} - 1); ph is the least admissible pure height; a cell
FAILS when h < ph; d_k(J) is the least degree of a nonzero multiple
of (x - 1)^J of height at most k. The RANK is r = M - J and the COFACTOR
of a lattice vector is q = P / (x - 1)^J, of degree at most r - 1.
  THE SPLIT. Dividing out every cyclotomic factor and any power of x
      leaves the RESIDUAL, well defined up to sign; its irreducible
      factors are the vector's NON-CYCLOTOMIC FACTORS.
  THE SEED. A = 2 + 4x + 5x^2 + 4x^3 + 2x^4, B = 2 + 3x + 2x^2 and
      Q = 3 + 5x + 3x^2, the three non-cyclotomic factors an older
      enumeration of the same chart exhibited at its failing cells.
  THE FAMILY W_v = v + (2v - 1)x + vx^2, v >= 2: W_2 = B, W_3 = Q.
  THE SWAP FAMILY at a cell. An admissible pure cofactor is
      q = (x - 1)^t prod_{d in E} [d]_x, [d]_x = 1 + x + ... + x^(d-1),
      E a multiset of parts >= 2, with t + sum (d - 1) <= r - 1 and
      |E| <= J + t (the other J + t - |E| parts are 1s). Its cyclotomic
      multiset S is {1}^t with every divisor e > 1 of every d in E, and
      prod_{n in S} Phi_n = q. A SWAP drops a sub-multiset of S and
      brings in a MULTIPLIER -- a product of seed factors, the empty
      product included -- of exactly the dropped degree:
          (prod_{n in S'} Phi_n) * m * (x - 1)^J,   S' within S,
          deg m = deg q - sum_{n in S'} phi(n).
      hs(M, J) is the least height over every swap of every admissible
      q. With the seed replaced by the SHAM A~ = 5 + 4x + 4x^2 + 2x^3 +
      2x^4, B~ = 3 + 2x + 2x^2, Q~ = 5 + 3x + 3x^2 -- the same degrees,
      heights and values at 1, not reciprocal -- it is hst.

THE HAND ATTACK, on paper before the engine.
  (1) h <= hs <= ph. A swap is a nonzero multiple of (x - 1)^J of
      degree deg q + J < M, so a lattice vector: hs >= h. The empty
      swap is q itself, so the pure family is inside and hs <= ph. At a
      clean cell hs = h is forced and is no evidence; only the failing
      cells test the construction, and the same holds for hst.
  (2) THE CIRCLE TEST, exact. An irreducible integer polynomial with
      every root on |z| = 1 is reciprocal up to sign (a root z on the
      circle has 1/z = conj(z) as a root too), and one of even degree
      2n is x^n S(x + 1/x) with S of degree n; its roots lie on the
      circle exactly when S has n real roots in [-2, 2], counted by a
      Sturm sequence. A MONIC one is a product of cyclotomics
      (Kronecker), so a non-cyclotomic factor on the circle is
      NON-MONIC. W_v is on the circle for every v: its trace
      polynomial is vy + 2v - 1, whose root 1/v - 2 lies in [-2, 2];
      W_v(1) = 4v - 1 and W_v(-1) = 1. So the unit-circle class with
      value 1 at -1 is infinitely generated, and a finite seed is a
      specimen, never the class.
  (3) THE END VALUE IS NOT FORCED BY SIZE. P(-1) = (-2)^J q(-1) and
      |P(-1)| <= M h, so 2^J > M h forces Phi_2 | q; that constrains
      the cyclotomic part at -1 and says nothing about a residual
      factor's value there. Any end-value regularity is read, never
      derived here.
  (4) THE DIAL AS A HUNT. At a dial cell the pure walk supplies dp, the
      least degree of a J-part pure product of height <= k, and one
      lattice question at width dp -- is there a vector of height <= k
      below degree dp? -- stops at the FIRST vector it meets when the
      answer is yes, whereas a chart cell needs its enumeration run to
      the end. So a break is cheap to find and a clean cell costs the
      full proof; a node cap marks the clean cells it cannot afford as
      undecided, never as clean.

THE SLATE, frozen before the engine ran. The older enumeration's
figures are TRANSPLANTS: its minimisers came from other code and a
lattice minimum need not be unique, so the census may differ.
  P1 THE SPLIT. The exhibited minimiser has a non-trivial residual at
     all 83 failing cells.
  P2 THE SEED SUFFICES ON THE CHART. Every non-cyclotomic factor
     exhibited at the 83 is A, B or Q (the older census read B at 51
     cells, A at 29, A*B at 2 and Q at 1; reported, not predicted).
  P3 THE CLASS. Every non-cyclotomic factor exhibited at the 83 and at
     the break is reciprocal, on the circle, non-monic and has value 1
     at -1. At the break this was READ before the freeze (the break's
     residual, 2 + 3x + 3x^2 + 3x^3 + 4x^4 + 5x^5 + 4x^6 + 3x^7 + 3x^8
     + 3x^9 + 2x^10, is irreducible with every root on the circle), so
     P3 at the break is a restatement, not a prediction.
  P4 THE SWAP BUILDS THE MINIMUM. hs = h at all 83 failing cells.
  P5 THE SEED CARRIES IT. The sham reaches h at fewer than 83.
  P6 THE DIAL MINTS. Past the columns flatten.py reads, the columns
     k = 9..12 break at least once within their walls, and every break's
     non-cyclotomic factors pass P3's tests.
  P7 THE BREAKS ARE NEW. At least one break on those columns carries a
     factor outside A, B, Q and the height-8 break's residual.

KILLS, as prints.
  K1 A non-cyclotomic factor at a failing chart cell outside {A, B, Q}
     (P2 dies: the chart mints beyond the seed under this enumerator).
  K2 A factor at a failing cell or a break printing reciprocal False,
     circle False, leading coefficient +-1, or a value at -1 other than
     1 (P3 dies at that factor).
  K3 hs > h at a failing cell (P4 dies at that cell).
  K4 hst = h at all 83 (P5 dies: the seed's shape carries nothing).
  K5 No break on the columns k = 9..12 (P6 dies).
  K6 Every break on those columns factors inside {A, B, Q, the height-8
     residual} (P7 dies).
  KB (bugs, never findings) hs < h or hs > ph or hst outside [h, ph];
     a split whose cyclotomic part times residual is not the vector
     itself up to sign and a power of x; a residual with a cyclotomic
     factor; a break witness not of height <= k or not cleared by J
     divisions.

CONTROLS, run before any verdict is read.
  C1 (POSITIVE, THE CIRCLE TEST) W_v for v = 2..9 prints reciprocal,
     circle True, value 4v - 1 at 1 and 1 at -1; x^2 - 3x + 1 prints
     circle False; Phi_15 prints circle True and monic.
  C2 (POSITIVE, THE SPLIT) The planted vector A * B * Phi_3 * Phi_1^2
     * x^3 splits to {1: 2, 3: 1} with non-cyclotomic factors {A, B}.
  C3 (POSITIVE, THE FAMILY) At every cell of the rectangle the empty
     swap alone gives ph, and every swap's value is rebuilt and checked
     for J divisions at the failing cells.
  C4 (POSITIVE, THE HUNT) The hunt's route, run at k = 8, J = 15,
     re-finds a vector of height <= 8 below degree 56.

THE DESIGN. The chart's minimisers are flatten.least_height's, the
same witnesses flatten.py reports. Factoring the residual over the
integers is sympy's; the circle test is the Sturm count of hand attack
(2), also sympy's. The swap family is enumerated exactly: the distinct
cyclotomic multisets S of every admissible q, then every sub-multiset
S' of each with the dropped degree matched by a multiplier, deduplicated
on (S', dropped degree). The rectangle is the chart's failing ranks,
5..18, at every chart cell of those ranks. The hunt runs each column
k = 9..12 from J = 1 upward, with a node cap per lattice question and a
wall per column; a break is stepped down to the exact d_k(J) only when
the step-down fits the cap.

RESOURCE NOTE. Estimated before any run: the split a few seconds (the
chart is 2.5 s); the swap unknown, priced by a rehearsal at the
rank-18 cells first; the hunt capped at 60 s per column, four columns.
Run under a 512 MB memory guard.

FINDINGS (copied from the printed output).
  F1 THE CONTROLS PASS. C1: W_2..W_9 on the circle with values 4v - 1
     and 1; x^2 - 3x + 1 circle False; Phi_15 circle True, lead 1. C2:
     the planted vector splits to [(1, 2), (3, 1)] with factors A, B;
     the height-8 break's residual R is one irreducible factor,
     reciprocal, circle True, lead 2, value 35 at 1 and 1 at -1.
     C3: the empty swaps give ph at all 370 cells of the rectangle.
     C4: the hunt re-finds k = 8, J = 15 as a break, d = 55 against 56.
  F2 THE SPLIT (P1, P2 hold; K1 never fired). 83 failing cells, 0 with
     residual 1, KB 0. Residual B at 51 cells, A at 29, A*B at 2 and Q
     at 1 -- the older census to the cell count, from other code.
     The failing heights run from 9 to 6323160.
  F3 THE CLASS ON THE CHART (P3 holds there). A, B and Q each print
     reciprocal, circle True, leading coefficient 2, 2, 3, value at 1
     17, 7, 11 and value 1 at -1.
  F4 THE SWAP (P4 holds). hs = h at 83 of 83 failing cells, K3 never
     fired, KB 0.
  F5 THE SHAM (P5 holds, and more). hst = h at 0 of the 83: the same
     degrees, heights and values at 1 without reciprocity rebuild no
     failing cell at all.
  F6 THE HUNT (P6, P7 hold; P3 DIES at a break). Two breaks on the
     columns k = 9..12. d_9(10) = 22 against a least pure degree of 23,
     the traded factor A: the chart's first failure h(23, 10) = 9 read
     from the dial. d_11(15) = 48 against 49, parts of the pure product
     (1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7), cyclotomic part
     Phi_1^15 Phi_2^3 Phi_3^3 Phi_4 Phi_5^2 Phi_7, and a NEW factor
     N = 1 + x + 2x^2 + 3x^3 + 3x^4 + 3x^5 + 2x^6 + x^7 + x^8:
     reciprocal, MONIC, circle False, value 17 at 1 and 1 at -1 (K2
     fires at N; its roots, read separately, are four on the circle and
     four off it, of moduli 1.2408 and its inverse, Mahler measure
     1.540). The
     columns read, rows J = 1 upward, '?' undecided at the cap:
       k=9  1 2 3 4 6 7 10 12 17 22<23 24 31 37 45 53 58 69? 77? 84? 94?
       k=10 1 2 3 4 5 7 10 12 17 20 24 27 36 40 51 54 67? 73? 83? 94?
       k=11 1 2 3 4 5 7 10 12 16 20 24 27 36 40 48<49 54 59 73? 83? 90?
       k=12 1 2 3 4 5 7 10 12 16 20 24 27 34 39 43 54 59 69? 80? 88?

THE DEEP CELLS, added after the findings above: an exploratory read
printed them before this stage was written, so they are a REPLICATION
of the older record's figures, never a prediction. At rank 22 the older
record exhibited h(52, 30) = 42222 with the factor
D = 3 + 9x + 15x^2 + 17x^3 + 15x^4 + 9x^5 + 3x^6 beside A, and
h(54, 32) = 108376 with E = 3 + 11x + 24x^2 + 37x^3 + 43x^4 + 37x^5 +
24x^6 + 11x^7 + 3x^8, the first factor it found off the circle. At
width 61 it exhibited h(61, 34) = 140702 with F = 3 + 10x + 20x^2 +
29x^3 + 33x^4 + 29x^5 + 20x^6 + 10x^7 + 3x^8 beside A, and h(61, 33) =
67323 with G = 3 + 6x + 8x^2 + 6x^3 + 3x^4 alone, the first factor it
found with a value other than 1 at -1.
  F7 THE DEEP CELLS REPLICATE. h(52, 30) = 42222, factors A and D, D
     reciprocal, circle True, lead 3, value 71 at 1 and 1 at -1;
     h(54, 32) = 108376, factor E, reciprocal, circle False, lead 3,
     value 193 at 1 and 1 at -1; h(61, 34) = 140702, factors A and F,
     F reciprocal, circle True, lead 3, value 157 at 1 and 1 at -1;
     h(61, 33) = 67323, factor G, reciprocal, circle True, lead 3,
     value 26 at 1 and 2 AT -1. 0.4 s, 0.1 s, 5.4 s and 1.7 s, as the
     deep print times them.

RUN RECORD. split and swap: 66.8 s, the swap 64.3 s of it, peak
working set 77.4 MB; the deep cells 8.5 s, peak 61.2 MB; the three are
the default run. hunt: 305.5 s against an estimate of about five
minutes, peak 62.2 MB. Both under a memory guard at the 512 MB default.
These runs split with flatten.py's cyclotomic split before it was
found stopping at the first Phi_n longer than what was left; every
factor printed here (A, B, Q, R, D, E, F, G, N) has leading
coefficient above 1 or roots off the circle, so none is cyclotomic and
no figure moves.
"""
import sys
import time

import sympy as sp

from flatten import (pow_xm1, height, clears, least_height, exists_at_most,
                     NodeCap, pure_table, ph_of, least_pure_degree, phi,
                     cyclotomic_split)

X = sp.Symbol("x")
SEED = {"A": [2, 4, 5, 4, 2], "B": [2, 3, 2], "Q": [3, 5, 3]}
SHAM = {"A~": [5, 4, 4, 2, 2], "B~": [3, 2, 2], "Q~": [5, 3, 3]}
BREAK8 = [2, 3, 3, 3, 4, 5, 4, 3, 3, 3, 2]


# ------------------------------------------------------------ polynomials

def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def normal(p):
    """Strip powers of x, sign to a positive leading coefficient."""
    p = trim(p)
    while len(p) > 1 and p[0] == 0:
        p.pop(0)
    return [-c for c in p] if p[-1] < 0 else p


def value(p, x):
    return sum(c * x ** i for i, c in enumerate(p))


def factors(p):
    """Irreducible factors over Z of a residual, each normalised, with
    multiplicity, as a sorted list of tuples."""
    p = normal(p)
    if len(p) == 1:
        return []
    _, fl = sp.factor_list(sp.Poly(list(reversed(p)), X).as_expr())
    out = []
    for f, m in fl:
        c = [int(v) for v in reversed(sp.Poly(f, X).all_coeffs())]
        out += [tuple(normal(c))] * m
    return sorted(out)


def trace_poly(p):
    """S with p = x^n S(x + 1/x), p reciprocal of degree 2n."""
    n = (len(p) - 1) // 2
    y = sp.Symbol("y")
    V = [sp.Integer(2), y]
    for k in range(2, n + 1):
        V.append(sp.expand(y * V[-1] - V[-2]))
    S = p[n] + sum(p[n + k] * V[k] for k in range(1, n + 1))
    return sp.Poly(sp.expand(S), y)


def describe(f):
    """The class tests of hand attack (2) on one irreducible factor."""
    f = list(f)
    recip = f == f[::-1] or f == [-c for c in f[::-1]]
    circle = False
    if recip and (len(f) - 1) % 2 == 0 and len(f) > 1:
        S = trace_poly(f)
        circle = S.count_roots(-2, 2) == S.degree()
    elif recip and len(f) == 2:
        circle = True                      # x + 1 or x - 1
    return {"deg": len(f) - 1, "lead": f[-1], "recip": recip,
            "circle": circle, "at1": value(f, 1), "atm1": value(f, -1)}


def in_class(d):
    return d["recip"] and d["circle"] and abs(d["lead"]) > 1 \
        and d["atm1"] == 1


def split_check(v):
    """Split, then rebuild: cyclotomic part times residual must be the
    vector up to sign and a power of x."""
    mult, res = cyclotomic_split(v)
    back = res
    for n, m in mult.items():
        for _ in range(m):
            back = pmul(back, phi(n))
    ok = normal(back) == normal(v)
    fs = factors(res)
    ok = ok and not any(cyclotomic_split(list(f))[0] for f in fs)
    return mult, res, fs, ok


# ------------------------------------------------------------ the swap

def divisors_gt1(d):
    return [e for e in range(2, d + 1) if d % e == 0]


def pure_multisets(r, J):
    """Distinct cyclotomic multisets S (sorted tuples) of the admissible
    pure cofactors of rank r at depth J."""
    out = set()

    def walk(E, budget, last):
        # E: parts >= 2 so far; budget: degree left for t + more parts
        for t in range(0, budget + 1):
            if len(E) <= J + t:
                S = [1] * t
                for d in E:
                    S += divisors_gt1(d)
                out.add(tuple(sorted(S)))
        for d in range(last, budget + 2):
            if d - 1 > budget:
                break
            E.append(d)
            walk(E, budget - (d - 1), d)
            E.pop()

    walk([], r - 1, 2)
    return out


def sub_multisets(S):
    from collections import Counter
    items = sorted(Counter(S).items())
    res = [()]
    for n, m in items:
        res = [s + (n,) * k for s in res for k in range(m + 1)]
    return res


def multipliers(members, maxdeg):
    """{degree: [polynomials]}, every product of members of degree
    <= maxdeg, the empty product at degree 0."""
    out = {0: [[1]]}
    items = list(members.values())

    def walk(p, i):
        for j in range(i, len(items)):
            q = pmul(p, items[j])
            dq = len(q) - 1
            if dq <= maxdeg:
                out.setdefault(dq, []).append(q)
                walk(q, j)

    walk([1], 0)
    return out


def swap_height(M, J, members, check=False):
    """hs(M, J) over the swap family with the given members, and hs0,
    the least height over the empty swaps alone (the pure family)."""
    r = M - J
    base = pow_xm1(J)
    mults = multipliers(members, r - 1)
    seen = set()
    best = hs0 = None
    cyc = {}
    for S in pure_multisets(r, J):
        degS = sum(len(phi(n)) - 1 for n in S)
        for Sp in sub_multisets(S):
            degSp = sum(len(phi(n)) - 1 for n in Sp)
            delta = degS - degSp
            if (Sp, delta) in seen or delta not in mults:
                continue
            seen.add((Sp, delta))
            if Sp not in cyc:
                p = base
                for n in Sp:
                    p = pmul(p, phi(n))
                cyc[Sp] = p
            for m in mults[delta]:
                v = pmul(cyc[Sp], m)
                hv = height(v)
                if check and not clears(v, J):
                    raise AssertionError("swap not flattened")
                if best is None or hv < best:
                    best = hv
                if delta == 0 and (hs0 is None or hv < hs0):
                    hs0 = hv
    return best, hs0, len(seen)


# ------------------------------------------------------------------ stages

def show(f):
    d = describe(f)
    return ("%s deg %d lead %d recip %s circle %s at1 %d atm1 %d"
            % (list(f), d["deg"], d["lead"], d["recip"], d["circle"],
               d["at1"], d["atm1"]))


def controls():
    bad = 0
    for c in range(2, 10):
        d = describe([c, 2 * c - 1, c])
        if not (d["recip"] and d["circle"] and d["at1"] == 4 * c - 1
                and d["atm1"] == 1):
            bad += 1
            print("  C1 FAILED at W_%d: %s" % (c, d))
    off = describe([1, -3, 1])
    cyc = describe(phi(15))
    bad += off["circle"] + (not cyc["circle"]) + (cyc["lead"] != 1)
    print("C1 circle test: W_2..W_9 on the circle with 4v - 1 and 1;"
          " x^2 - 3x + 1 circle %s; Phi_15 circle %s lead %d"
          % (off["circle"], cyc["circle"], cyc["lead"]))
    v = [0, 0, 0] + SEED["A"]
    for f in (SEED["B"], phi(3), phi(1), phi(1)):
        v = pmul(v, f)
    mult, res, fs, ok = split_check(v)
    good = ok and mult == {1: 2, 3: 1} and fs == sorted(
        [tuple(SEED["A"]), tuple(SEED["B"])])
    bad += not good
    print("C2 planted split: %s, factors %s -> %s" % (
        sorted(mult.items()), fs, "ok" if good else "FAILED"))
    fr = factors(BREAK8)
    print("  the height-8 break's residual factors as %d: %s"
          % (len(fr), "; ".join(show(f) for f in fr)))
    return bad


def chart_cells():
    return [(M, J) for M in range(4, 41) for J in range(2, min(30, M - 1) + 1)]


def stage_split(table):
    """The 83 failing cells: split each exhibited minimiser."""
    t0 = time.time()
    fails, H = [], {}
    for (M, J) in chart_cells():
        h, v, _ = least_height(M, J)
        p, _ = ph_of(table, M, J)
        H[(M, J)] = (h, p, v)
        if h < p:
            fails.append((M, J))
    kb = k1 = k2 = triv = 0
    census, seen = {}, {}
    for c in fails:
        h, p, v = H[c]
        mult, res, fs, ok = split_check(v)
        kb += not ok
        if not fs:
            triv += 1
        key = tuple(fs)
        census.setdefault(key, []).append(c)
        for f in fs:
            seen.setdefault(f, []).append(c)
    names = {tuple(v): k for k, v in SEED.items()}
    for f in sorted(seen, key=lambda f: (len(f), f)):
        d = describe(f)
        k1 += f not in names
        k2 += not in_class(d)
        print("  factor %s at %d cells: %s" % (names.get(f, "NEW"),
                                               len(seen[f]), show(f)))
    for key in sorted(census, key=lambda k: -len(census[k])):
        print("  residual %s: %d cells" % (
            "*".join(names.get(f, str(list(f))) for f in key) or "1",
            len(census[key])))
    print("P1 split: %d failing cells, %d with residual 1; KB %d (%.1f s)"
          % (len(fails), triv, kb, time.time() - t0))
    print("  failing heights: least %d, greatest %d"
          % (min(H[c][0] for c in fails), max(H[c][0] for c in fails)))
    print("P2 K1 fired %d times; P3 K2 fired %d times" % (k1, k2))
    return H, fails, kb


def stage_swap(H, fails):
    t0 = time.time()
    kb = k3 = c3 = 0
    rect = [c for c in H if 5 <= c[0] - c[1] <= 18]
    hit = sham = 0
    for c in rect:
        h, p, v = H[c]
        failing = c in fails
        hs, hs0, n = swap_height(c[0], c[1], SEED, check=failing)
        c3 += hs0 != p
        kb += not (h <= hs <= p)
        if failing:
            hst, hst0, _ = swap_height(c[0], c[1], SHAM)
            kb += not (h <= hst <= p)
            hit += hs == h
            sham += hst == h
            if hs > h:
                k3 += 1
                print("  K3 at %s: h %d, hs %d, ph %d" % (c, h, hs, p))
    print("C3 empty swaps give ph: %d rectangle cells, %d off"
          % (len(rect), c3))
    print("P4 swap: hs = h at %d of %d failing cells (K3 %d);"
          " P5 sham: hst = h at %d (K4 %s); KB %d (%.1f s)"
          % (hit, len(fails), k3, sham, sham == len(fails), kb,
             time.time() - t0))
    return kb + c3


def hunt_cell(k, J, cap):
    """One dial cell: the least J-part pure degree dp, and a vector of
    height <= k below it (stopping at the first), stepped down to the
    exact d_k(J) while the cap allows. Returns (dp, parts, verdict, v,
    d) with verdict 'clean', 'break' or 'undecided'."""
    dp, parts = least_pure_degree(J, k, 400)
    if dp is None:
        return dp, parts, "undecided", None, None
    if dp == J:
        return dp, parts, "clean", None, dp
    try:
        v, _ = exists_at_most(dp, J, k, cap=cap)
    except NodeCap:
        return dp, parts, "undecided", None, None
    if v is None:
        return dp, parts, "clean", None, dp
    M, exact = dp, True
    while True:
        try:
            w, _ = exists_at_most(M - 1, J, k, cap=cap)
        except NodeCap:
            exact = False
            break
        if w is None:
            break
        v, M = w, M - 1
    return dp, parts, "break", v, (M - 1 if exact else -(M - 1))


def stage_hunt(cap, wall):
    t0 = time.time()
    known = {tuple(v) for v in SEED.values()} | {tuple(BREAK8)}
    kb = breaks = new = k2 = 0
    # C4: the route re-finds the height-8 break
    dp, parts, verdict, v, d = hunt_cell(8, 15, 200000000)
    c4 = verdict == "break" and d == 55
    print("C4 the hunt re-finds k=8 J=15: %s, d = %s against %s"
          % (verdict, d, dp))
    for k in range(9, 13):
        tcol, J, row = time.time(), 0, []
        while time.time() - tcol < wall:
            J += 1
            dp, parts, verdict, v, d = hunt_cell(k, J, cap)
            if verdict == "clean":
                row.append(dp)
                continue
            if verdict == "undecided":
                row.append("%s?" % ("none" if dp is None else dp))
                continue
            breaks += 1
            row.append("%s<%d" % (d if d > 0 else "<=%d" % -d, dp))
            ok = height(v) <= k and clears(v, J)
            kb += not ok
            mult, res, fs, sok = split_check(v)
            kb += not sok
            print("  BREAK k=%d J=%d: d %s against pure %d %s; cyclotomic"
                  " part %s" % (k, J, d if d > 0 else "<= %d" % -d, dp,
                                parts, sorted(mult.items())))
            for f in fs:
                new += f not in known
                k2 += not in_class(describe(f))
                print("    factor %s: %s" % ("known" if f in known
                                             else "NEW", show(f)))
                known.add(f)
        print("k=%d: %s (%.1f s)" % (k, row, time.time() - tcol))
    print("P6 hunt: %d breaks on k = 9..12 (K5 %s); P3 K2 at the breaks %d;"
          " P7 new factors %d (K6 %s); KB %d (%.1f s)"
          % (breaks, breaks == 0, k2, new, new == 0, kb, time.time() - t0))
    return kb + (not c4)


def stage_deep():
    """The older record's four deep cells, replicated."""
    want = {(52, 30): (42222, [SEED["A"], [3, 9, 15, 17, 15, 9, 3]]),
            (54, 32): (108376, [[3, 11, 24, 37, 43, 37, 24, 11, 3]]),
            (61, 34): (140702, [SEED["A"],
                                [3, 10, 20, 29, 33, 29, 20, 10, 3]]),
            (61, 33): (67323, [[3, 6, 8, 6, 3]])}
    bad = 0
    for (M, J), (hw, fw) in want.items():
        t0 = time.time()
        h, v, nodes = least_height(M, J)
        mult, res, fs, ok = split_check(v)
        good = ok and h == hw and fs == sorted(tuple(f) for f in fw)
        bad += not good
        print("deep h(%d, %d) = %d (%d nodes, %.1f s): %s" % (
            M, J, h, nodes, time.time() - t0,
            "replicates" if good else "DIFFERS"))
        for f in fs:
            print("    factor %s" % show(f))
    return bad


if __name__ == "__main__":
    t_all = time.time()
    stages = sys.argv[1:] or ["split", "swap", "deep"]
    bad = controls()
    table = pure_table(39)
    if "split" in stages or "swap" in stages:
        H, fails, kb = stage_split(table)
        bad += kb
    if "swap" in stages:
        bad += stage_swap(H, fails)
    if "deep" in stages:
        bad += stage_deep()
    if "hunt" in stages:
        bad += stage_hunt(cap=5000000, wall=60)
    print("wall %.1f s" % (time.time() - t_all))
    sys.exit(1 if bad else 0)
