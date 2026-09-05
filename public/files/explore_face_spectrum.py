"""explore_face_spectrum.py -- the term-count spectrum of the shared-form
collisions, derived: why no delta = 2 object sits at 12.

THE QUESTION. explore_face_accident.py's search (its S3) walks the
shared-form collisions over p = 1 + t: F = B.q with B a 0/1 univariate
divisible by 1 + t whose quotient n = B/(1 + t) carries a negative
coefficient, and q = q0 + y.q1 + y^2.q2 a three-layer 0/1 polynomial whose
bottom layer is t^a (1 + t), each layer's product with n and with B again
0/1, q not divisible by 1 + t. Its finding 5 is a property: the descent
dimension delta is 2 exactly when BOTH outermost y-layers of q are
t^a (1 + t). Its finding 4 recorded, in the box of degrees at most 6,
138 such objects at term counts 14 (80 of them) and 18 (58) and none at
12 -- and left why 12 is empty underived. This file derives the whole
spectrum and checks the derivation against the box.

THE HAND-ATTACK, fixed before the engine.
 (1) A 0/1 polynomial's term count is its value at 1. F = B.q is 0/1, so
     |F| = B(1).q(1) = |B|.|q| exactly -- the term-count law.
 (2) delta = 2 forces q2 present with |q0| = |q2| = 2 (two layers both
     multiples of 1 + t make q = (1 + t)(t^a + y^j t^c), divisible by
     1 + t and excluded), so |q| = 4 + |q1| and |F| = |B|.(4 + |q1|).
 (3) B(-1) = 0 says B has as many even-degree terms as odd-degree ones,
     so |B| is EVEN and at least 2.
 (4) 12 = |B|.(4 + |q1|) with |B| even leaves |B| = 2, |q1| = 2 only.
 (5) |B| = 2 is B = 1 + t^k with k odd (n = B/(1 + t) needs a negative
     coefficient, so k >= 3), n = 1 - t + t^2 - ... + t^(k-1); a 2-term
     middle layer is q1 = t^b (1 + t^m), m >= 1, and the coefficient of
     t^(b+1) in n.q1 is -1 + [m = 1], so n.q1 0/1 forces m = 1 -- and then
     every layer of q is a multiple of 1 + t, q is divisible by 1 + t,
     excluded. So 12 is empty, at every degree bound: the argument never
     consulted D.
 (6) The same algebra reads the rest of the spectrum. 14 = 2 x 7 is a
     binomial B with a 3-term middle layer; 18 = 2 x 9 is a binomial B
     with a 5-term middle layer (6 x 3 needs |q| = 3 < 6); 16 = 2 x 8 or
     4 x 4 needs a 4-term middle layer or a 4-term B with |q1| = 0; 20 =
     2 x 10 or 4 x 5.

PREDICTIONS (fixed before any run).
  P1  no delta = 2 object at term count 12 at any D walked (D = 4..8).
  P2  at D = 6 every delta = 2 object has a BINOMIAL B, and the counts
      reproduce finding 4: 80 at 14, 58 at 18, 138 in all, of 628
      distinct collisions.
  P3  (a SUSPICION, not derived) at a binomial B the admissible middle
      layers that keep q off 1 + t have ODD term counts, so the delta = 2
      spectrum at binomial B is {2.(4 + odd)} = {14, 18, 22, ...}: 16 and
      20 empty at D <= 8 unless a 4-term B enters at delta = 2.
KILLS, as observables.
  K1  a delta = 2 object printed at 12 -- the derivation is wrong.
  K2  a delta = 2 object with |B| = 4 or 6 -- steps (2)-(4) are wrong.
  K3  a 4-term admissible middle layer at a binomial B off 1 + t -- P3
      falls, P1 stands.
POSITIVE CONTROL: the box at D = 6 must print 628 distinct collisions and
138 at delta = 2 with 80 at 14 and 58 at 18, off the slate's definitions
alone (finding 5 being a property, no face reading is run here; the
collision count itself is explore_face_accident.py's, reproduced by the
same enumeration and the same dedup on the product's support up to
translation).

THE DESIGN. Univariate 0/1 polynomials as bitmasks over degrees <= D.
Enumerate B; keep those with B(-1) = 0 and a negative coefficient in
n = B/(1 + t). For each B the admissible layers are the 0/1 r with n.r and
B.r 0/1. Bottoms are the r = t^a (1 + t). Build q = q0 + y q1 + y^2 q2 with
q1, q2 in {0} + admissible, not both 0, min t-exponent 0, q(-1, y) != 0
identically (some layer nonzero at t = -1), dedup F = B.q on its support up
to translation. delta = 2 iff the top nonzero layer is a bottom shape (q0
always is). Print, per D, the distinct count, the delta = 2 count and the
spectrum as (|B|, |q1|, |F|) -> count, then the checks.

FINDINGS (post-run edit; every number copied from the printed output).
 1. TWELVE IS EMPTY, AND IT IS A THEOREM (property, the derivation above;
    P1 held at D = 4..9, K1 shut). Every delta = 2 cell printed obeys
    |F| = |B|.(4 + |q1|) with |B| even, at all six D, and no cell reads
    12 at any of them. The argument never consulted the degree bound.
 2. THE POSITIVE CONTROL REPRODUCES FINDING 4 EXACTLY: D = 6 prints 7
    admissible B, 628 distinct collisions, 138 at delta = 2, 80 at term
    count 14 and 58 at 18 -- the same enumeration and the same dedup,
    with no face reading run. D = 4 and 5 print 96/30 and 336/86 as the
    predecessor recorded.
 3. THE BINOMIAL B IS A BOX FACT AND NOT A LAW (P2 held at D = 6 as
    predicted; K2 FIRED at D = 9 and its clause does not follow). Every
    delta = 2 object at D <= 8 has |B| = 2; at D = 9 a 4-term B enters --
    200 objects at term count 28 = 4 x 7 -- so the spectrum's first
    non-binomial cell sits at degree 9. K2 was frozen too broad: steps
    (2)-(4) bound only the cell reading 12, and a 4-term B at 28 touches
    none of them; the kill's observable was right and its inference was
    written from the D = 6 print, where every B is binomial.
 4. THE ODD MIDDLE LAYER IS A BOX FACT TOO, AND P3 FALLS (observation).
    The middle layers at binomial B, off 1 + t, have term counts {3} at
    D = 4, {3, 5} at 5 and 6, {3, 5, 7} at 7 -- and at D = 8 a 6-term
    layer appears, 1 + t + t^2 + t^6 + t^7 + t^8 = (1 + t + t^2)(1 + t^6),
    carrying 64 objects at term count 20 (98 at D = 9). K3 as frozen
    named a 4-term layer, and none appears through D = 9: 16 = 2 x 8 is
    empty in the box walked and NOT derived, the only term count below
    28 the theorem above does not decide.
 5. THE SPECTRUM AT D = 9 (observation, exact in the box): 92 admissible
    B, 13,796 distinct collisions, 1,580 at delta = 2 -- 14: 200, 18: 852,
    20: 98, 22: 132, 26: 98 (all at binomial B), 28: 200 (|B| = 4,
    |q1| = 3).

RUN RECORD. python explore_face_spectrum.py 4 5 6 7 (0.1 s wall) and
8 9 (0.7 s); every check ok, FAILS: 0, at both invocations. No memwatch:
the enumeration holds one set of supports, kilobytes at D = 9.
"""
import sys
import time
from collections import Counter


def val(mask, x):
    return sum(x ** i for i in range(mask.bit_length()) if mask >> i & 1)


def coeffs(mask, D):
    return [mask >> i & 1 for i in range(D + 1)]


def div_1pt(c):
    """Exact quotient of the coefficient list c by 1 + t, or None."""
    q = []
    carry = 0
    for a in c:
        b = a - carry
        q.append(b)
        carry = b
    if carry != 0:
        return None
    return q[:-1] if q and q[-1] == 0 else q


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return out


def is01(c):
    return all(x in (0, 1) for x in c)


def terms(c):
    return sum(1 for x in c if x)


def run(D):
    t0 = time.time()
    Bs = []
    for mask in range(1, 1 << (D + 1)):
        if not mask & 1:
            continue
        c = coeffs(mask, D)
        n = div_1pt(c)
        if n is None or all(x >= 0 for x in n):
            continue
        Bs.append((c, n))
    layers = [coeffs(m, D) for m in range(1, 1 << (D + 1))]
    seen = set()
    spec = Counter()
    d2 = 0
    mids = {}
    for B, n in Bs:
        adm = [r for r in layers if is01(pmul(n, r)) and is01(pmul(B, r))]
        bottoms = [r for r in adm if terms(r) == 2
                   and [i for i, x in enumerate(r) if x][1]
                   - [i for i, x in enumerate(r) if x][0] == 1]
        adm0 = [None] + adm
        for q0 in bottoms:
            for q1 in adm0:
                for q2 in adm0:
                    if q1 is None and q2 is None:
                        continue
                    lay = [q0, q1, q2]
                    mn = min(min(i for i, x in enumerate(r) if x)
                             for r in lay if r is not None)
                    if mn != 0:
                        continue
                    if all(val(sum(x << i for i, x in enumerate(r)), -1) == 0
                           for r in lay if r is not None):
                        continue
                    F = [pmul(B, r) if r is not None else [] for r in lay]
                    key = []
                    for j, row in enumerate(F):
                        for i, x in enumerate(row):
                            if x:
                                key.append((i, j))
                    key = tuple(sorted(key))
                    if key in seen:
                        continue
                    seen.add(key)
                    top = q2 if q2 is not None else q1
                    if top in bottoms:
                        d2 += 1
                        nq1 = terms(q1) if q1 is not None else 0
                        nF = sum(terms(row) for row in F)
                        spec[(terms(B), nq1, nF)] += 1
                        if terms(B) == 2 and q1 is not None:
                            mids.setdefault(tuple(q1), 0)
                            mids[tuple(q1)] += 1
    print("D = %d: admissible B %d, distinct collisions %d, delta = 2: %d"
          "   [%.1fs]" % (D, len(Bs), len(seen), d2, time.time() - t0))
    for (nb, nq1, nF), cnt in sorted(spec.items(), key=lambda kv: kv[0][2]):
        print("    |B| = %d  |q1| = %d  |F| = %2d  : %d   (|B|.(4+|q1|) = %d)"
              % (nb, nq1, nF, cnt, nb * (4 + nq1)))
    if mids:
        sizes = Counter(terms(list(m)) for m in mids)
        print("    middle layers at binomial B, off 1 + t, by term count: %s"
              % dict(sorted(sizes.items())))
        for m in sorted(mids):
            if terms(list(m)) % 2 == 0:
                print("      even-size middle layer: %s"
                      % " + ".join("t^%d" % i for i, x in enumerate(m) if x))
    return spec, len(seen), d2


def main():
    Ds = [int(a) for a in sys.argv[1:]] or [4, 5, 6, 7, 8]
    fails = 0

    def check(name, ok):
        nonlocal fails
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))
        fails += not ok

    results = {}
    for D in Ds:
        results[D] = run(D)
    if 6 in results:
        spec, dist, d2 = results[6]
        at = lambda nF: sum(c for (nb, nq1, f), c in spec.items() if f == nF)
        check("positive control: D = 6 prints 628 distinct, 138 at delta = 2",
              dist == 628 and d2 == 138)
        check("positive control: 80 at 14 and 58 at 18", at(14) == 80 and at(18) == 58)
        check("P2: every delta = 2 object at D = 6 has a binomial B",
              all(nb == 2 for (nb, nq1, f) in spec))
    for D, (spec, dist, d2) in results.items():
        check("P1 at D = %d: no delta = 2 object at 12" % D,
              all(f != 12 for (nb, nq1, f) in spec))
        check("term-count law at D = %d: |F| = |B|.(4 + |q1|) at every cell" % D,
              all(f == nb * (4 + nq1) for (nb, nq1, f) in spec))
        check("|B| even at D = %d" % D, all(nb % 2 == 0 for (nb, nq1, f) in spec))
    print("\n%d/%d checks" % (sum(1 for _ in range(0)), 0) if False else
          "\nFAILS: %d" % fails)
    return fails


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
