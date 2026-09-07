"""explore_jump_haar.py — THE HAAR LAW OF THE JUMP SET: is the frequency
of a readout over random Eisenstein windows a closed form, and which of
two rules breaks at the classes the census never saw?

THE QUESTION. The rung of an Eisenstein field K/Q_2 — the deepest
arrival class's landing, the μ_8 ladder on the window word's digits at
e = 4 — is the second weight of Pagano's jump set of the field (rule in
range, 120 fields; explore_jump_set.py finding 1), and at e = 4 the
census of 48 designed quartics plus ζ_8 splits over eight jump sets as
24, 6, 6, 3, 3, 3, 3, 1. Pagano's mass formula ("Jump sets in local
fields", arXiv:1810.09975, Theorems 1.7 and 1.8, Proposition 8.1) says
how often each jump set occurs: over Eisenstein polynomials of degree e
with the Haar measure on their coefficients, the probability of a jump
set (I, β) is the Haar measure of the orbit of its relation vector,
normalized over the admissible orbits (Theorem 1.6: admissible = the
jump sets some field realizes). This rig asks two things. (1) Does a
uniform population of Eisenstein polynomials reproduce that law class
by class? (2) The law has ten admissible classes at e = 4 and the
census found eight: at the two it never reached the second weight is
15 or 16, above the ladder's cap of 14 — so "the rung is the second
weight" and the ladder's cap cannot both hold there, and an exact
enumeration of the class-1 landing says which breaks.

THE OBJECTS (explore_jump_set.py's conventions). K = Q_2[x]/(F), F
Eisenstein of degree e, f = 1, π = x; T* = {i < 2i* : i odd} ∪ {2i*},
i* = e the Kummer seat at p = 2, e* = 2e; ρ(i) = min(2i, i + e). The
relation vector is 2·dlog(−1) in the basis η_a = 1 + π^a, its
coordinate at a of 2-order b_a ≥ 1; the jump set is the Pareto
frontier of {(a, b_a)} under (order, weight ρ^{b_a}(a)): (a', b') is
absorbed by (a, b) when b ≤ b' and ρ^b(a) ≤ ρ^{b'}(a'). The rung at
e = 4 is rung4 of the word's digits w_1..w_5 (the ladder); the EXACT
rung is the least landing v(u^8 − 1) over the class-1 units u
(v(u − 1) = 1) of U_1/U_amax, amax past every landing in play.

THE HAND-ATTACK (on paper, before the engine).
H1  THE LAW IS A HAND COMPUTATION. Theorem 1.7 puts the Haar measure
    on the relation vector's module, the free Z_2-module on T*, and
    the orbit of a vector is read off its coordinate orders alone
    (Theorem 1.4), so under Haar the b_a are independent with
    P(b_a = b) = 2^{−b} for b ≥ 1 (the relation is 2 times a vector,
    so no coordinate is a unit; a unit coordinate would put a β = 0
    point on the frontier, which is no jump set). Admissible
    (Theorem 1.6) is: the frontier's least weight is e* exactly. At
    e = 4, T* = {1, 3, 5, 7, 8}: the weights ρ^b(a) are 2, 4, 8, 12,
    16, … at a = 1; 6, 10, 14, … at 3; 9, 13, … at 5; 11, 15, … at
    7; 12, 16, … at 8. Least weight 8 forces b_1 = 3, b_3 ≥ 2, the
    rest ≥ 1 (automatic). Every point with b ≥ 3 is then absorbed by
    (1, 3) at weight 8, so only the b ≤ 2 points remain:
    (5, 1) at 9 absorbs everything → I = [1, 5], β = (3, 1): 1/2.
    b_5 ≥ 2 and b_7 = 1 (weight 11, absorbing 12, 13, 15): with
    b_3 = 2 (weight 10, which 11 cannot absorb) [1, 3, 7]: 1/8; with
    b_3 ≥ 3, [1, 7] β = (3, 1): 1/8. b_5, b_7 ≥ 2 and b_8 = 1 (12):
    [1, 3, 8] 1/16, [1, 8] (3, 1) 1/16. All of b_5, b_7, b_8 ≥ 2:
    b_3 = 2 → [1, 3] (3, 2) at 10: 1/16; else b_5 = 2 → [1, 5]
    (3, 2) at 13: 1/32; else b_7 = 2 → [1, 7] (3, 2) at 15: 1/64;
    else b_8 = 2 → [1, 8] (3, 2) at 16: 1/128; else [1] alone: 1/128.
    Ten classes, masses summing to 1. The census's 48-sweep counts
    24, 6, 6, 3, 3, 3 at the first six are those masses times 48
    EXACTLY; its [1, 5] (3, 2) at 3 of 48 against 1/32 and ζ_8's [1]
    at 1 of 49 against 1/128 are the sweep's design (coefficients mod
    4, six constant terms), not the law's; and [1, 7] (3, 2) and
    [1, 8] (3, 2) are admissible classes the sweep cannot see.
H2  THE HAND VALUE AT e = 2 IS THE WHOLE POPULATION. T* = {1, 3, 4},
    e* = 4: admissible is b_1 = 2, b_3 ≥ 1, b_4 ≥ 1; the classes are
    [1, 3] (2, 1) at 5 with mass 1/2, [1, 4] (2, 1) at 6 with 1/4,
    and [1] with 1/4. The six ramified quadratics of Q_2 ARE the
    population, and Serre's masses 2^{−c(K)}/|Aut K| are 1/8 at each
    of √2, √−2, √6, √10 (discriminant exponent 3) and 1/4 at each of
    √3 and √−1 (exponent 2), total 1; the census reads √2, √−2, √10,
    √6 in [1, 3], √3 in [1, 4], √−1 in [1] — so the law's 1/2, 1/4,
    1/4 IS Serre's weighting of the census, by hand, before any run.
H3  THE POPULATION. x^e + a_{e−1}x^{e−1} + … + a_0 with a_i ∈ 2Z_2
    and a_0 ∈ 2·Z_2^×, the Haar measure on the coefficients; read
    modulo 2^k it is the uniform measure on a_i mod 2^k (2^{k−1}
    classes each for i ≥ 1, 2^{k−2} for a_0), 2^{e(k−1)−1} cells.
    The jump set is locally constant on Eisenstein polynomials
    (Krasner: the field is), so at a large enough k every cell is
    pure and the counts are the law's masses times the cell count —
    at e = 4 the least mass 1/128 needs 2^{4k−5} ≥ 128, k ≥ 3, and
    purity is checked directly: a k-cell is PURE when its 2^e
    children at k + 1 share its jump set. Counts are read only at a
    precision whose every cell is pure; a split cell at k means k + 1
    is the reading and k + 2 the purity check.
H4  THE TWO RULES. The ladder (explore_mu8_grading.py ML4) reads the
    class-1 minimal landing off w_1..w_5 with unit freedom at rel-6
    and a cap of 14; the jump-set rule reads it as the second
    frontier weight. At [1, 7] (3, 2) and [1, 8] (3, 2) the second
    weight is 15 and 16, so at any field of those classes exactly one
    of the two rules is wrong, and the exact rung by enumeration
    decides. The transplant to flag: the cap of 14 is the ladder's
    derivation at the sweep's fields, and the jump-set rule is a
    census fact at 120 fields none of which sits in the two classes.
    Neither is a theorem here; the print is.
H5  WHAT THE ENUMERATOR MUST SEE. A landing L is exact only when
    amax > L: the orbit caps at amax. Rungs to 16 are in play, so
    amax = 18 (U_1/U_18, 2^17 representatives, class 1 half of them).

PREDICTIONS, fixed before the engine ran.
  PR1 (the weld). At e = 2 and e = 4, at the first pure precision,
      every class's count equals its law mass times the cell count,
      exactly. KILL: a class whose count differs from the law's by
      one cell or more at a precision whose cells are all pure.
  PR2 (purity). At e = 4 every k = 4 cell is pure (2^11 cells). KILL
      of the prediction, not of PR1: a split cell; then k = 5 reads.
  PR3 (the unseen classes exist). [1, 7] (3, 2) and [1, 8] (3, 2)
      each appear in the e = 4 population, at 1/64 and 1/128.
  PR4 (which rule breaks; one of two, the first predicted). At every
      field of the two unseen classes the exact rung is 14 and the
      ladder's rung4 agrees with it, so "the rung is the second
      weight" breaks there — the second weight (15, 16) being a level
      of the torsion relation that a class-1 landing, which reads a
      unit's eighth power against 1 and not against −1, need not
      see. KILL of PR4: an exact rung of 15 or 16 at such a field —
      which kills the ladder's cap instead.
  PR5 (positive controls, run and read before PR1–PR4).
      (a) The law's support at e = 2, 4, 8 equals the set of
          admissible jump sets enumerated from the axioms alone
          (I ⊆ T*, β ≥ 1 strictly decreasing, weights strictly
          increasing, least weight e*), and the masses sum to 1.
      (b) The census's 49 quartics reproduce explore_jump_set.py's
          partition — eight classes at 24, 6, 6, 3, 3, 3, 3, 1 — and
          rung4 equals the second weight at all 48 non-anchor fields.
      (c) The exact-rung enumerator equals rung4 at one census field
          of each rung 9..13 and reads 14 at ζ_8, before it is read
          at any unseen-class field.
      (d) H2's hand value: the e = 2 population at every precision
          read gives 1/2, 1/4, 1/4.

THE DESIGN. Stages, each its own process under memwatch:
  law     the closed form at e = 2, 4, 8 by enumeration of the orders
          (b ≤ B lumped above B = log_2 e + 2, every lumped point
          absorbed by the first frontier point — asserted), the
          admissible set from the axioms, PR5(a).
  census  PR5(b).
  pop2    e = 2 at k = 5 and 6: counts against the law, purity of the
          k = 5 cells.
  pop4    e = 4 at k = 4 (2048 cells) and k = 5 (32768): counts against
          the law at both, purity of every k = 4 cell, the unseen
          classes' cells listed.
  rung    PR5(c), then the exact rung at every k = 4 cell of the two
          unseen classes beside rung4 and the second weight.
  cap     added after the rung stage was read: rung4 against
          min(second weight, 14) at every k = 4 cell.

FINDINGS (entered post-run, copied from printed output).

1. THE WELD HOLDS EXACTLY (PR1, PR2, PR3 hit; rule, exhaustive over
   the Eisenstein cells named). At e = 2 the population reads 64, 32,
   32 of 128 cells at k = 5 and 256, 128, 128 of 512 at k = 6 over
   [1, 3], [1, 4], [1] — the law's 1/2, 1/4, 1/4 — with 0 of the 128
   k = 5 cells split. At e = 4 the ten admissible classes read 1024,
   256, 256, 128, 128, 128, 64, 32, 16, 16 of the 2048 cells at k = 4
   and 16384, 4096, 4096, 2048, 2048, 2048, 1024, 512, 256, 256 of the
   32768 at k = 5, every count the law's mass times the cell count
   exactly, no class off the law, and 0 of the 2048 k = 4 cells split
   (every cell pure). So the frequency of a jump set over Haar-random
   Eisenstein quartics of Q_2 is the frontier law of H1, the census's
   24, 6, 6, 3, 3, 3 of 48 was that law at the sweep's resolution, and
   [1, 7] (3, 2) and [1, 8] (3, 2) are real at 1/64 and 1/128 — 32 and
   16 of the 2048 cells.

2. THE JUMP-SET RULE BREAKS AND THE LADDER HOLDS (PR4 hit, the first
   of its two sides). At all 48 k = 4 cells of the two unseen classes
   the exact class-1 landing minimum over U_1/U_18 is 14 and rung4 is
   14, against second weights 15 (32 cells) and 16 (16 cells). The
   controls first: the enumerator read 9, 10, 11, 12, 13 at one
   census field per rung and 14 at zeta8, each equal to rung4. So
   "the rung is the jump set's second weight" is a rule at the 120
   census fields and false at 1/64 + 1/128 of the population; the
   statement that holds is THE RUNG IS THE SECOND WEIGHT CAPPED AT
   THE FREEDOM RUNG 7e/2, the anchors' missing second point read as
   infinity: rung4 = min(second weight, 14) at 2048 of 2048 k = 4
   cells (the cap stage), and at e = 2 the census's 5, 6, 7 are
   min(5, 7), min(6, 7), min(inf, 7). The cap is the ladder's unit
   freedom at rel-6: past five digits of the window word a class-1
   unit is free, and a torsion level deeper than that freedom is not
   a landing anything reads.

3. THE LAW AT e = 8 (the law stage; property of the recursion, its
   support the axioms' admissible set, PR5(a)). 44 admissible classes,
   [1, 9] (4, 1) at 1/2, [1, 5, 11] and [1, 11] at 1/8,
   [1, 5, 13] at 1/16, [1, 5, 15], [1, 3, 13], [1, 13] at 1/32, then
   1/64 and 1/128, down to [1] at 1/2^20; 11 of the 44 carry a second
   weight above the freedom rung 28, which the capped rule reads as
   28, and the anchor's [1] reads 28 too. The census's 65-field sample saw 16 classes; none of the 20 is
   among them, and the capped rule at e = 8 is a prediction here, not
   a reading (read since at 8192 Haar-random octics and derived for
   every 2-power e, explore_rung_theorem.py).

4. THE HAND VALUE IS THE THEOREM'S OWN CROSS-CHECK (H2): Serre's
   masses over the six ramified quadratics — 1/8 at each of sqrt 2,
   sqrt -2, sqrt 6, sqrt 10 and 1/4 at each of sqrt 3, sqrt -1 —
   weight the census's classes to exactly the law's 1/2, 1/4, 1/4,
   the Theorem 1.7 side of the equality, where the population reads
   the Theorem 1.8 side.

TIER. Finding 1 is a rule, exhaustive over every Eisenstein cell of
Q_2 at e = 2 to k = 6 and e = 4 to k = 5 with purity at k = 4 and
k = 5 read directly; the law itself is Pagano's theorem, the hand
computation of H1 its instance. Finding 2 is a rule at every k = 4
cell of e = 4 (the ladder's rung4 at all 2048, the exact landing at
the 48 unseen-class cells and six controls) and at the whole e = 2
population; at e = 8 it is a prediction. The mechanism of the cap is
the ladder's own derivation (explore_mu8_grading.py ML4), not proved
here.

RUN RECORD. HAAR_STAGES=law,census / pop2 / pop4 / rung / cap, each
python memwatch.py explore_jump_haar.py: law+census 0.5 s (the brute
force it replaced, 143 s, printed the same e = 8 list); pop2 0.8 s;
pop4 235 s at 27 MB; rung 229 s; cap 14 s. Nothing ran bare. One
pre-green fault: the first law stage enumerated 6^9 order vectors at
e = 8 and was rewritten as the frontier recursion before any number
was read.
"""
import os
import sys
import time
from fractions import Fraction
from itertools import product

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, ".")
import explore_local_clock as lc          # noqa: E402
import explore_arrival_defect as ad       # noqa: E402
import explore_jump_set as js             # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ---------------------------------------------------------------- the law

def tstar(p, e):
    estar = p * e // (p - 1)
    return [i for i in range(1, estar) if i % p] + [estar]


def rho_k(p, e, i, k):
    for _ in range(k):
        i = min(p * i, i + e)
    return i


def frontier(p, e, orders):
    """The Pareto frontier of {(a, b_a)}; orders is {a: b}, b >= 1."""
    pts = [(a, b) for a, b in orders.items()]
    front = []
    for (a, b) in pts:
        wt = rho_k(p, e, a, b)
        dominated = any((b2 <= b and rho_k(p, e, a2, b2) <= wt)
                        for (a2, b2) in pts if (a2, b2) != (a, b))
        if not dominated:
            front.append((a, b))
    front.sort()
    return tuple(front)


def absorb(front, pt, p, e):
    """The Pareto frontier of front + {pt}."""
    a, b = pt
    w = rho_k(p, e, a, b)
    for (a2, b2) in front:
        if b2 <= b and rho_k(p, e, a2, b2) <= w:
            return front
    kept = [(a2, b2) for (a2, b2) in front
            if not (b <= b2 and w <= rho_k(p, e, a2, b2))]
    return tuple(sorted(kept + [pt]))


def law(p, e):
    """{jump set: mass}, the Haar law of the frontier normalized over
    admissible vectors, by a recursion over the coordinates whose state
    is the frontier so far; orders above B are lumped at B + 1, and no
    lumped order may survive on an admissible frontier (asserted)."""
    T = tstar(p, e)
    estar = p * e // (p - 1)
    B = 1
    while rho_k(p, e, 1, B) < estar:
        B += 1
    B += 1
    states = {(): Fraction(1)}
    for a in T:
        nxt = {}
        for front, m in states.items():
            for b in range(1, B + 2):
                w = Fraction(p - 1, p ** b) if b <= B else Fraction(1, p ** B)
                f2 = absorb(front, (a, b), p, e)
                nxt[f2] = nxt.get(f2, Fraction(0)) + m * w
        states = nxt
    masses = {}
    for fr, m in states.items():
        if min(rho_k(p, e, a, b) for a, b in fr) != estar:
            continue
        ok(all(b <= B for _a, b in fr),
           "a lumped order sits on an admissible frontier at e = %d" % e)
        masses[fr] = m
    total = sum(masses.values())
    return {fr: m / total for fr, m in masses.items()}


def admissible_sets(p, e):
    """Every (I, beta) satisfying the axioms with least weight e*."""
    T = tstar(p, e)
    estar = p * e // (p - 1)
    out = set()
    bmax = 1
    while rho_k(p, e, 1, bmax) < estar:
        bmax += 1

    def rec(idx, cur, last_b, last_w):
        if idx == len(T):
            if cur and min(rho_k(p, e, a, b) for a, b in cur) == estar:
                out.add(tuple(cur))
            return
        rec(idx + 1, cur, last_b, last_w)
        a = T[idx]
        for b in range(1, bmax + 1):
            w = rho_k(p, e, a, b)
            if cur and not (b < last_b and w > last_w):
                continue
            rec(idx + 1, cur + [(a, b)], b, w)
    rec(0, [], None, None)
    return out


def fmt(fr):
    return "I=%s b=%s" % ([a for a, _ in fr], [b for _, b in fr])


def stage_law():
    print("[law] the Haar law of the jump set, f = 1, p = 2")
    for e in (2, 4, 8):
        L = law(2, e)
        A = admissible_sets(2, e)
        ok(set(L) == A, "law support != admissible set at e = %d" % e)
        ok(sum(L.values()) == 1, "masses do not sum to 1 at e = %d" % e)
        print("  e = %d: %d admissible classes, masses sum %s" %
              (e, len(L), sum(L.values())))
        for fr, m in sorted(L.items(), key=lambda kv: -kv[1]):
            wts = [rho_k(2, e, a, b) for a, b in fr]
            print("    %-28s wt=%-16s %s" % (fmt(fr), wts, m))


# ------------------------------------------------------------- the fields

def read_field(eis, e):
    """(jump set, second weight, rung4 or None) of x^e + ... from eis."""
    F = js.field("eis", eis)
    fr, _c = js.jump_set(F, js.pi_el(F))
    wts = [js.rho_k(F, a, b) for a, b in fr]
    second = wts[1] if len(wts) > 1 else None
    r4 = None
    if e == 4:
        d = js.digits(F, js.w_element(F), 6)
        r4 = js.rung4(d)
    return fr, second, r4


def cells(e, k):
    """Every Eisenstein cell mod 2^k: a_i/2 in 0..2^{k-1}-1, a_0/2 odd."""
    half = 2 ** (k - 1)
    for a0 in range(1, half, 2):
        for rest in product(range(half), repeat=e - 1):
            yield [2 * a0] + [2 * r for r in rest] + [1]


def children(eis, k):
    """The 2^e refinements of a k-cell at k + 1."""
    step = 2 ** k
    e = len(eis) - 1
    for bits in product((0, 1), repeat=e):
        yield [c + b * step for c, b in zip(eis[:-1], bits)] + [1]


def stage_census():
    print("[census] the 49 quartics of explore_jump_set.py")
    counts = {}
    agree = 0
    for name, eis in js.QUARTS:
        fr, second, r4 = read_field(eis, 4)
        counts[fr] = counts.get(fr, 0) + 1
        if name != "zeta8":
            agree += (r4 == second)
    for fr, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print("  %-28s %d" % (fmt(fr), n))
    print("  classes %d, rung4 == second weight at %d of 48" %
          (len(counts), agree))
    ok(len(counts) == 8 and sorted(counts.values()) == [1, 3, 3, 3, 3, 6, 6, 24],
       "census partition not reproduced")
    ok(agree == 48, "rung4 != second weight in the census")


def stage_pop(e, ks, purity_k):
    L = law(2, e)
    reads = {}
    for k in ks:
        t0 = time.time()
        counts = {}
        by_cell = {}
        for eis in cells(e, k):
            fr, second, r4 = read_field(eis, e)
            counts[fr] = counts.get(fr, 0) + 1
            by_cell[tuple(eis)] = (fr, second, r4)
        N = sum(counts.values())
        reads[k] = by_cell
        print("[pop%d] k = %d: %d cells, %.1f s" % (e, k, N, time.time() - t0))
        off = 0
        for fr, m in sorted(L.items(), key=lambda kv: -kv[1]):
            n = counts.get(fr, 0)
            want = m * N
            flag = "" if n == want else "  <-- off by %s" % (n - want)
            off += (n != want)
            print("    %-28s %6d  law %8s%s" % (fmt(fr), n, want, flag))
        extra = [fr for fr in counts if fr not in L]
        print("    classes off the law: %d; classes off the count: %d"
              % (len(extra), off))
        ok(not extra, "a jump set outside the admissible set at e = %d" % e)
    if purity_k in reads and purity_k + 1 in reads:
        fine = reads[purity_k + 1]
        split = 0
        for eis, (fr, _s, _r) in reads[purity_k].items():
            kids = [fine[tuple(c)][0] for c in children(list(eis), purity_k)]
            if any(kf != fr for kf in kids):
                split += 1
        print("    purity at k = %d: %d of %d cells split" %
              (purity_k, split, len(reads[purity_k])))
    return reads


def exact_rung(eis, amax):
    """The least class-1 landing v(u^8 - 1) over U_1/U_amax (e = 4)."""
    F = lc.LF("eis", 2, [0, 1], eis, amax)
    best = None
    for u in F.units():
        if F.val(F.esub1(u)) != 1:
            continue
        o = F.orbit(u)
        if F.seat in o:
            n = o.index(F.seat)
            if n + 1 < len(o):
                L = o[n + 1]
                if best is None or L < best:
                    best = L
    return best


def stage_rung():
    print("[rung] the exact class-1 landing against the two rules")
    picks = {}
    for name, eis in js.QUARTS:
        fr, second, r4 = read_field(eis, 4)
        picks.setdefault(r4, (name, eis, second))
    print("  PR5(c): census fields, one per rung")
    for r4 in sorted(picks):
        name, eis, second = picks[r4]
        t0 = time.time()
        ex = exact_rung(eis, 18)
        print("    %-14s rung4 %2d  second %-4s exact %s  (%.1f s)" %
              (name, r4, second, ex, time.time() - t0))
        ok(ex == r4, "enumerator disagrees with rung4 at %s" % name)
    print("  the unseen classes at k = 4")
    targets = {((1, 3), (7, 2)), ((1, 3), (8, 2))}
    found = 0
    for eis in cells(4, 4):
        fr, second, r4 = read_field(eis, 4)
        if fr in targets:
            found += 1
            ex = exact_rung(eis, 18)
            print("    %-24s %-22s second %2d  rung4 %2d  exact %s" %
                  (eis[:-1], fmt(fr), second, r4, ex))
    print("  fields read: %d" % found)


def stage_cap():
    """Post-run stage: is rung4 = min(second weight, 7e/2) at every
    k = 4 cell, the anchors' missing second point read as infinity?"""
    print("[cap] rung4 against min(second weight, 14) over the k = 4 cells")
    agree = total = 0
    off = {}
    for eis in cells(4, 4):
        fr, second, r4 = read_field(eis, 4)
        capped = min(second if second is not None else 99, 14)
        total += 1
        if r4 == capped:
            agree += 1
        else:
            off[(fmt(fr), second, r4)] = off.get((fmt(fr), second, r4), 0) + 1
    print("  agree at %d of %d cells" % (agree, total))
    for key, n in sorted(off.items()):
        print("  off: %s second %s rung4 %s  x%d" % (key[0], key[1], key[2], n))


STAGES = {
    "cap": stage_cap,
    "law": stage_law,
    "census": stage_census,
    "pop2": lambda: stage_pop(2, (5, 6), 5),
    "pop4": lambda: stage_pop(4, (4, 5), 4),
    "rung": stage_rung,
}


def main():
    names = os.environ.get("HAAR_STAGES", "law,census").split(",")
    for n in names:
        STAGES[n.strip()]()
    print("checks passed: %d" % CHECKS)


if __name__ == "__main__":
    main()
