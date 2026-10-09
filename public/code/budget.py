"""
budget.py -- what omitting a place frees at a global constraint.

QUESTION. A global constraint over a global field is a relation among
one local term per place: the product formula, Hilbert reciprocity,
the sum of Brauer invariants, the degree of a divisor. Read with one
place omitted -- its term never consulted -- the remaining terms are
freer than before. How much freer, is the answer a property of the
omitted place's own local group or of the whole constraint, and is
the archimedean place of Q special among the places one could omit?

THE ARGUMENT (written before this script).
  (1) THE BUDGET THEOREM. Write a constraint as a complex
      X --i--> (+)_v L_v --s--> G with s(i(x)) = 0, the sum direct
      (almost every term zero), and call it EXACT when every family
      with s = 0 is i of a global element. Omit a place w. A visible
      family l = (l_v), v != w, is the visible part of a global
      element iff some l_w in L_w has s_w(l_w) = -s(l), and at an
      exact constraint that is the only condition. So the visible
      families realized are exactly those with s(l) in s_w(L_w): the
      omitted place buys its own term's image in G and nothing else,
      and the omitted term is then fixed by the visible ones up to the
      kernel of s_w. At any constraint, with H = ker s / im i, a
      visible family is realized iff s(l) lies in s_w(L_w) and some
      completion has class 0 in H; the completions' classes fill a
      coset of the image of ker s_w, so the obstruction lives in H
      modulo that image. H is the constraint's; the omitted place
      decides how much of it its kernel absorbs.
  (2) THE FOUR CONSTRAINTS OVER Q, each exact.
      The product formula: L_p = Z (the valuation), L_inf = R (log |x|),
      s = sum_p -l_p log p + l_inf, X = Q*. Any finitely supported
      vector (e_p) is v(x) for x = prod p^(e_p) (unique factorization),
      so omitting inf buys all of R and the finite constraint is VOID.
      The additive constraint: x = sum_p {x}_p (mod 1) for x in Q, the
      partial-fraction identity, with {x}_p the p-part in Z[1/p]/Z.
      Every finite family of p-parts is realized by its sum, and the
      omitted term x mod 1 is that sum.
      Hilbert reciprocity: L_v = {+-1}, the local symbol (a, b)_v,
      s = product. The infinite symbol is -1 iff a < 0 and b < 0, so
      omitting inf buys one bit: the visible ramification set of a
      quaternion algebra over Q is any finite set of primes, odd
      exactly when a < 0 and b < 0 (Hasse's existence theorem gives
      every even set of places).
      The Brauer sum: L_v = Br(Q_v), Q/Z at p and (1/2)Z/Z at inf
      (Frobenius), s = sum, exact by Albert-Brauer-Hasse-Noether.
      Omitting inf buys (1/2)Z/Z: one bit, and 2-torsion's alone, so
      an algebra of odd degree has visible invariants summing to 0.
  (3) THE DEGREE CONTROL. Over F_q(t), L_P = Z at every place P,
      s = sum deg(P) l_P, G = Z, X = F_q(t)*; exact because every
      divisor of degree 0 on the projective line is principal. The
      place at infinity has degree 1, so omitting it buys all of Z, as
      omitting inf over Q buys all of R. Omitting a finite place P0 of
      degree d buys dZ: a visible family is realized iff its degree
      sum is 0 mod d. What makes the archimedean place of Q buy
      everything is that its term's image is the whole of G, which it
      shares with every degree-1 place of F_q(t); being archimedean is
      not used.
  (4) THE RANK FACE. Over a number field K with class group Cl,
      omitting a finite set S_f of finite places and every infinite
      place from the product formula (valuations free at S_f, zero at
      the other finite places) gives the S-units, and the sequence
      1 -> O* -> O_S* -> Z^(S_f) -> Cl is exact, the last map
      a -> class of prod P^(a_P). So each omitted finite place buys
      rank 1 (rank O_S* = r + |S_f|, r the unit rank), and the
      valuation lattice has index in Z^(S_f) equal to the order of
      the subgroup of Cl the classes [P], P in S_f, generate. The
      corrector is the class group extended by the unit torus; the
      index reads its class-group part.
  (5) THE VOLUME FACE. For K real quadratic with fundamental unit eps
      and regulator R = log eps, take a basis eps, u_1..u_s of O_S*
      mod torsion with the valuation vectors (v_P(u_i))_P a basis of
      the valuation lattice.
      Dropping one infinite place, the log matrix has rows
      (log|eps|, 0, ..., 0) and (log|u_i|, -v_P(u_i) log NP): it is
      block triangular, so R_S = R * [Z^(S_f) : lattice] * prod log NP,
      each omitted place paying its own covolume log NP (NP = p^2 at
      an inert p), with no cross term. Section V builds that matrix
      from S-units chosen to span a lattice of the index section R
      certifies, so its ratio equals the index by construction: it
      evaluates the formula and checks the arithmetic, and the proof
      is the verifier.
  (6) THE LAYER FACE. Omitting less -- cutting the local units at P
      to the residue layer (O/P)* instead of removing the place --
      gives the ray class group mod m = prod P, of order
      h * prod |(O/P)*| / |image of O* in prod (O/P)*|. The per-place
      reading predicts the image as prod |im_P|; the joint image is
      one object, and rho = prod |im_P| / |joint image| is its excess
      over the per-place product. At unit
      rank 0 with units +-1 and s places of odd residue characteristic
      each im_P = {+-1} has order 2 and the joint image is the
      diagonal, so rho = 2^(s-1), unbounded in s.

PREDICTIONS (fixed before the run). Every check prints PASS.
  Q: 200 random valuation vectors on the primes below 50, exponents in
     [-5, 5], each rebuilt as a rational whose valuations reprint the
     vector, prod_v |x|_v = 1 exactly; 200 random rationals satisfy
     x = sum_p {x}_p mod 1 exactly, and 200 random finite families of
     p-parts are realized by their sum and read back.
  H: every quaternion algebra (a, b), a and b squarefree with
     1 <= |a|, |b| <= 30 -- 38 values each, 1,444 pairs -- satisfies
     reciprocity with its symbols computed at every place, and its
     visible set is odd at exactly the 361 = 19^2 pairs with a < 0
     and b < 0. (As frozen; the script computes the symbols at
     infinity and at the primes dividing 2ab, every other symbol
     being 1.) The algebras (5, 3), (77, -1), (-1, -1), (-3, -1)
     have visible sets {3, 5}, {7, 11}, {2}, {3}. Every one of the 128
     subsets of the seven channels of 510510 is the visible set of an
     algebra with a a signed divisor of 510510 and b squarefree,
     |b| <= 200.
  D: over F_2(t), 200 random nonzero f have degree sum 0 over all
     places. With the degree place omitted, every visible vector on
     t, t + 1, t^2 + t + 1 with exponents in [-3, 3] is realized. With
     the place t^2 + t + 1 omitted (d = 2), and again t^3 + t + 1
     (d = 3), a vector on t, t + 1 and infinity with exponents in
     [-2, 2] is realized iff its degree sum is 0 mod d: 63 of 125
     at d = 2, 41 of 125 at d = 3.
  R: over Q(sqrt -5), h = 2, S_f the places over p = 2, 3, 11, 29
     (ramified, split, inert, split): ranks 1, 2, 1, 2, indices
     2, 2, 1, 1. Over Q(sqrt 10), h = 2: S_f = {P2}, {P3, P3'},
     {P41, P41'}, {P2, P41, P41'} give indices 2, 2, 1, 2. Over
     Q(sqrt 2), h = 1: every index 1. Each index 2 is certified by a
     norm equation with no solution; each index 1 by a found element.
  V: at every S-set of R over the two real fields, R_S computed from
     the log matrix of found S-units equals R * index * prod log NP
     to 1e-9; R = log(3 + sqrt 10) = 1.818446 and log(1 + sqrt 2).
  L: over Q(sqrt 2) at the seven places over 3, 7, 17, 23: the pair
     P7(r=3) * P23(r=5) gives prod 132, joint 66, rho 2; the pair
     P7(r=3) * P17(r=6) gives rho 1; of the 21 pairs 7 have rho > 1,
     each conjugate pair among them. Over Q(sqrt -5): P3 * P3' gives
     rho 2 and h_m 4; P3 * P3' * P7' gives rho 4 and h_m 24.

DESIGN. Sections of checks printing PASS or FAIL; a control runs
before what it guards and stops the run when it fails, and what holds
by construction prints instead of checking. Symbols, valuations and
images are computed from their definitions, and three prints evaluate
an argument rather than test it: section D reads the place at infinity
by degree, so its degree sums and its iff are the degree control's
arithmetic; section V evaluates (5)'s formula; section L's h_m is
(6)'s formula with h = 2. Hilbert symbols by Serre's formulas at every prime
dividing 2ab and at infinity. Valuations in Z[sqrt d] from norms: at a
split p the common p-power is stripped and the rest sits at the one
conjugate whose root it vanishes at; at an inert p the common
p-power; at a ramified p the norm's p-power. S-units found by search
over |x| <= B, 0 <= y <= B (every element of the box up to sign),
B = 120 over Q(sqrt -5) and 400 over the real fields; a lattice index
by integer elimination. Principal classes certified by a solution or
by a norm equation failing modulo 5, which divides d = 10, the one real
field certified (real), or by exhaustion (imaginary). Unit images as
closures under multiplication. F_2[t] polynomials as bit masks,
factored by trial division.
  Q  the product formula, the additive identity.
  H  the reciprocity sweep, the four algebras, the 128 patterns.
  D  the degree sums, the three omissions.
  R  the rank face on three fields.
  V  the volume face.
  L  the layer face.

RUN RECORD. First run: 22 of 23 PASS. The failure was the engine's: the
product-formula check multiplied |x| by p^(v_p) where |x|_p = p^(-v_p),
and all 200 vectors failed together. After the sign was fixed, 23 of 23
PASS. The prints read as frozen. Reciprocity held at all 1,444 pairs,
361 of them odd, and all 128 channel patterns of 510510 were found as
visible sets. Over F_2(t), the factorizer read back all 343 vectors on
t, t + 1 and t^2 + t + 1 with infinity omitted; with the places of
degree 2 and 3 omitted, 63 and 41 of 125 were realized, each exactly the
congruent ones. Indices 2, 2, 1, 1 over Q(sqrt -5), 2, 2, 1, 2 over
Q(sqrt 10) and all 1 over Q(sqrt 2). R_S over Q(sqrt 10) at S_f over 2,
3, 41 and {2, 41}: 2.520902, 4.389544, 25.077500, 34.764796, the ratio
equal to the index to 1.6e-15. The layer face's rho > 1 pairs over
Q(sqrt 2) were P3 against each place over 17 (rho 4), the conjugates
over 7, 17, 23 (rho 3, 16, 11) and P7(r=3) * P23(r=5), P7(r=4) *
P23(r=18) (rho 2). Wall 1.3 s, peak 14 MB. (Settled later, on an audit.
ARGUMENT (1) first said H "does not depend on w" and is "applied once
and not per place", which is only its definition; it is restated above
with the obstruction in H modulo the image of ker s_w, which does depend
on w, as section R's indices show. The ranks first counted places; they
now print the found valuation lattice's basis, 1, 2, 1, 2, a print
because a nonzero index already forces them. Section V reads the S-sets
its code names, not every set of section R: the single place over 7 of
Q(sqrt 2) is read in R only.) A code read then made the checks that held
by construction prints: the odd visible sets (reciprocity implies them),
D's degree sums and its iff, R's ranks, V's ratios and L's h_m
(by (6)'s formula); the four algebras and V's regulators became
controls, run first and stopping the run. The run prints 16/16.

Run: python budget.py   (seconds, pure Python)
"""

import random
from fractions import Fraction
from itertools import combinations
from math import log, sqrt, prod

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" +
          (f"  [{detail}]" if detail else ""))


def control(name, ok, detail=""):
    check(name, ok, detail)
    if not ok:
        print("  control failed: run stopped")
        raise SystemExit(1)


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def factorize(n):
    n, out, d = abs(n), {}, 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def squarefree(n):
    return n != 0 and all(e == 1 for e in factorize(n).values())


def vp(n, p):
    if n == 0:
        return 10 ** 9
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


# ---------------------------------------------------------------- Q
def section_q():
    print("Q  the product formula and the additive constraint over Q")
    rng = random.Random(1)
    P = primes_upto(50)
    bad = unit = 0
    for _ in range(200):
        vec = {p: rng.randint(-5, 5) for p in rng.sample(P, 4)}
        x = Fraction(rng.choice([-1, 1]))
        for p, a in vec.items():
            x *= Fraction(p) ** a
        back = {p: vp(x.numerator, p) - vp(x.denominator, p) for p in P}
        want = {p: vec.get(p, 0) for p in P}
        full = abs(x)
        for p in P:
            full *= Fraction(p) ** -back[p]
        bad += back != want
        unit += full == 1
    check("200 random valuation vectors read back from their rationals",
          bad == 0, f"{bad} failures")
    print(f"    prod_v |x|_v = 1 at {unit} of 200 (algebra, once the "
          "vector reads back)")

    def p_part(x, p):
        b, e = x.denominator, vp(x.denominator, p)
        if e == 0:
            return Fraction(0)
        pe = p ** e
        c = x.numerator * pow(b // pe, -1, pe) % pe
        return Fraction(c, pe)

    bad = 0
    for _ in range(200):
        x = Fraction(rng.randint(-10 ** 6, 10 ** 6),
                     rng.randint(1, 10 ** 5))
        s = sum(p_part(x, p) for p in factorize(x.denominator))
        if (x - s).denominator != 1:
            bad += 1
    check("x = sum_p {x}_p mod 1", bad == 0, f"200 rationals, {bad}")
    bad = 0
    for _ in range(200):
        fam = {}
        for p in rng.sample(P, 3):
            e = rng.randint(1, 3)
            fam[p] = Fraction(rng.randrange(p ** e), p ** e)
        x = sum(fam.values())
        if any(p_part(x, p) != c for p, c in fam.items()):
            bad += 1
    check("200 random families of p-parts realized by their sum",
          bad == 0, f"{bad} failures")


# ---------------------------------------------------------------- H
def legendre(a, p):
    r = pow(a % p, (p - 1) // 2, p)
    return -1 if r == p - 1 else r


def hilbert(a, b, p):
    if p == 0:
        return -1 if a < 0 and b < 0 else 1
    al, u = vp(a, p), a // p ** vp(a, p)
    be, v = vp(b, p), b // p ** vp(b, p)
    if p != 2:
        s = (-1) ** (al * be * ((p - 1) // 2))
        if be % 2:
            s *= legendre(u, p)
        if al % 2:
            s *= legendre(v, p)
        return s
    eps = lambda z: ((z - 1) // 2) % 2
    om = lambda z: ((z * z - 1) // 8) % 2
    return (-1) ** ((eps(u) * eps(v) + al * om(v) + be * om(u)) % 2)


def visible_set(a, b):
    ps = {2} | set(factorize(a)) | set(factorize(b))
    return frozenset(p for p in ps if hilbert(a, b, p) == -1)


def section_h():
    print("H  Hilbert reciprocity: the parity bit")
    want = {(5, 3): {3, 5}, (77, -1): {7, 11}, (-1, -1): {2},
            (-3, -1): {3}}
    got = {k: set(visible_set(*k)) for k in want}
    control("the four algebras' visible sets", got == want, str(got))
    vals = [s * n for n in range(1, 31) if squarefree(n) for s in (1, -1)]
    recip = odd = 0
    quad_ok = True
    for a in vals:
        for b in vals:
            vis = visible_set(a, b)
            if (-1) ** len(vis) * hilbert(a, b, 0) != 1:
                recip += 1
            o = len(vis) % 2 == 1
            odd += o
            quad_ok &= o == (a < 0 and b < 0)
    check("reciprocity at every pair", recip == 0,
          f"{len(vals)} values, {len(vals) ** 2} pairs, {recip} breaks")
    print(f"    visible set odd at {odd} pairs, "
          f"{'exactly' if quad_ok else 'NOT exactly'} those with a < 0 "
          "and b < 0 (reciprocity implies it: the symbol at infinity "
          "is -1 there only)")
    PRIMES7 = [2, 3, 5, 7, 11, 13, 17]
    divs = [prod(c) for r in range(8) for c in combinations(PRIMES7, r)]
    found = set()
    bs = [s * n for n in range(1, 201) if squarefree(n) for s in (1, -1)]
    for a0 in divs:
        for a in (a0, -a0):
            for b in bs:
                vis = visible_set(a, b)
                if vis <= set(PRIMES7):
                    found.add(vis)
    check("all 128 channel patterns of 510510 are visible sets",
          len(found) == 128, f"{len(found)} found")


# ---------------------------------------------------------------- D
def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pdivmod(a, b):
    q, db = 0, b.bit_length()
    while a and a.bit_length() >= db:
        s = a.bit_length() - db
        q ^= 1 << s
        a ^= b << s
    return q, a


def deg(a):
    return a.bit_length() - 1


def irreducibles(maxdeg):
    out = []
    for f in range(2, 1 << (maxdeg + 1)):
        if all(pdivmod(f, g)[1] for g in out if 2 * deg(g) <= deg(f)):
            out.append(f)
    return out


IRR = irreducibles(12)


def pfactor(f):
    out = {}
    for g in IRR:
        if deg(g) > deg(f):
            break
        while deg(f) >= 1:
            q, r = pdivmod(f, g)
            if r:
                break
            out[g] = out.get(g, 0) + 1
            f = q
    assert f == 1
    return out


def valuations(num, den):
    v = {}
    for g, e in pfactor(num).items():
        v[g] = v.get(g, 0) + e
    for g, e in pfactor(den).items():
        v[g] = v.get(g, 0) - e
    v["inf"] = deg(den) - deg(num)
    return {k: e for k, e in v.items() if e}


def build(exps):
    num = den = 1
    for g, e in exps.items():
        for _ in range(abs(e)):
            if e > 0:
                num = pmul(num, g)
            else:
                den = pmul(den, g)
    return num, den


def section_d():
    print("D  the degree control over F_2(t)")
    rng = random.Random(2)
    bad = 0
    for _ in range(200):
        num = rng.randrange(1, 1 << 11)
        den = rng.randrange(1, 1 << 11)
        v = valuations(num, den)
        if sum((1 if g == "inf" else deg(g)) * e for g, e in v.items()):
            bad += 1
    print(f"    degree sum 0 at {200 - bad} of 200 random f (v_inf is "
          "deg den - deg num, so it is by construction)")
    T, T1, Q2, Q3 = 0b10, 0b11, 0b111, 0b1011
    bad = cnt = 0
    for a in range(-3, 4):
        for b in range(-3, 4):
            for c in range(-3, 4):
                cnt += 1
                v = valuations(*build({T: a, T1: b, Q2: c}))
                v.pop("inf", None)
                if v != {k: e for k, e in {T: a, T1: b, Q2: c}.items()
                         if e}:
                    bad += 1
    check("the factorizer reads back every vector built on t, t + 1, "
          "t^2 + t + 1, exponents in [-3, 3]", bad == 0,
          f"{cnt} vectors, {bad}")
    for P0, d, want in ((Q2, 2, 63), (Q3, 3, 41)):
        real = cong = 0
        bad = 0
        for a in range(-2, 3):
            for b in range(-2, 3):
                for ai in range(-2, 3):
                    ok = False
                    for c in range(-8, 9):
                        v = valuations(*build({T: a, T1: b, P0: c}))
                        if v.get("inf", 0) == ai:
                            ok = True
                    real += ok
                    cg = (a + b + ai) % d == 0
                    cong += cg
                    bad += ok != cg
        print(f"    place of degree {d} omitted: {real} of 125 realized "
              f"(want {want}), {cong} with degree sum 0 mod {d}, {bad} "
              "disagreeing (by the degree of v_inf, one condition)")


# ------------------------------------------------ quadratic fields
class Quad:
    """Z[sqrt d], d squarefree, d = 2, 3 mod 4."""

    def __init__(self, d):
        self.d = d

    def norm(self, x, y):
        return x * x - self.d * y * y

    def kind(self, p):
        if (4 * self.d) % p == 0:
            return "ram"
        return "split" if legendre(self.d, p) == 1 else "inert"

    def roots(self, p):
        return [r for r in range(p) if (r * r - self.d) % p == 0]

    def places(self, p):
        k = self.kind(p)
        if k == "split":
            return [(p, r) for r in self.roots(p)]
        return [(p, k)]

    def NP(self, P):
        return P[0] ** 2 if P[1] == "inert" else P[0]

    def v(self, P, x, y):
        p, t = P
        c = min(vp(x, p), vp(y, p))
        if t == "inert":
            return c
        if t == "ram":
            return vp(self.norm(x, y), p)
        x1, y1 = x // p ** c, y // p ** c
        if (x1 + y1 * t) % p:
            return c
        return c + vp(self.norm(x1, y1), p)

    def search(self, primes, B):
        out = []
        for x in range(-B, B + 1):
            for y in range(0, B + 1):
                n = self.norm(x, y)
                if n == 0:
                    continue
                m = abs(n)
                for p in primes:
                    while m % p == 0:
                        m //= p
                if m == 1:
                    out.append((x, y))
        return out


def lattice_index(vectors, s):
    rows = [list(v) for v in vectors if any(v)]
    basis = []
    for col in range(s):
        piv = [r for r in rows if r[col]]
        rest = [r for r in rows if not r[col]]
        while len(piv) > 1:
            piv.sort(key=lambda r: abs(r[col]))
            h = piv[0]
            nxt = [h]
            for r in piv[1:]:
                q = r[col] // h[col]
                r2 = [a - q * b for a, b in zip(r, h)]
                (nxt if r2[col] else rest).append(r2)
            piv = nxt
        if not piv:
            return 0, basis
        basis.append(piv[0])
        rows = rest
    return abs(prod(b[i] for i, b in enumerate(basis))), basis


def s_unit_data(K, S, B):
    primes = sorted({P[0] for P in S})
    others = [Q for p in primes for Q in K.places(p) if Q not in S]
    found = []
    for x, y in K.search(primes, B):
        if any(K.v(Q, x, y) for Q in others):
            continue
        found.append((x, y, tuple(K.v(P, x, y) for P in S)))
    idx, _ = lattice_index([f[2] for f in found], len(S))
    return found, idx


def principal_certificate(K, P):
    n = K.NP(P)
    if K.d < 0:
        sols = [(x, y) for x in range(60) for y in range(60)
                if K.norm(x, y) == n]
        return bool(sols)
    for x in range(-400, 401):
        for y in range(0, 401):
            if abs(K.norm(x, y)) == n:
                return True
    squares5 = {z * z % 5 for z in range(5)}
    assert all((n * s) % 5 not in squares5 for s in (1, -1))
    return False


def section_r():
    print("R  the rank face: one rank per omitted place, the class-"
          "group part of the corrector")
    K = Quad(-5)
    ranks, idxs = [], []
    for p in (2, 3, 11, 29):
        S = K.places(p)
        found, idx = s_unit_data(K, S, 120)
        ranks.append(len(lattice_index([f[2] for f in found], len(S))[1]))
        idxs.append(idx)
    cert = [principal_certificate(K, K.places(p)[0])
            for p in (2, 3, 11, 29)]
    print(f"    Q(sqrt -5): ranks {ranks} at p = 2, 3, 11, 29 (a nonzero "
          "index forces |S_f|)")
    check("Q(sqrt -5): indices 2, 2, 1, 1, the 2s certified",
          idxs == [2, 2, 1, 1] and cert == [False, False, True, True],
          f"{idxs}, principal {cert}")
    K = Quad(10)
    sets = [K.places(2), K.places(3), K.places(41),
            K.places(2) + K.places(41)]
    idxs = [s_unit_data(K, S, 400)[1] for S in sets]
    cert = [principal_certificate(K, K.places(p)[0]) for p in (2, 3, 41)]
    check("Q(sqrt 10): indices 2, 2, 1, 2, the 2s certified",
          idxs == [2, 2, 1, 2] and cert == [False, False, True],
          f"{idxs}, principal at 2, 3, 41: {cert}")
    K = Quad(2)
    sets = [K.places(2), K.places(3), K.places(7), K.places(7)[:1]]
    idxs = [s_unit_data(K, S, 400)[1] for S in sets]
    check("Q(sqrt 2): every index 1", idxs == [1, 1, 1, 1], str(idxs))


# ---------------------------------------------------------------- V
def det(m):
    m = [row[:] for row in m]
    n, d = len(m), 1.0
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(m[r][i]))
        if abs(m[piv][i]) < 1e-300:
            return 0.0
        if piv != i:
            m[i], m[piv] = m[piv], m[i]
            d = -d
        d *= m[i][i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            for c in range(i, n):
                m[r][c] -= f * m[i][c]
    return d


def fundamental_unit(K):
    best = None
    for y in range(1, 200):
        for x in range(1, 2000):
            if abs(K.norm(x, y)) == 1:
                val = x + y * sqrt(K.d)
                if best is None or val < best[0]:
                    best = (val, x, y)
                break
    return best


def section_v():
    print("V  the volume face: R_S = R * index * prod log NP")
    for d, sets_p, want_R in ((10, [[2], [3], [41], [2, 41]], 1.818446),
                              (2, [[2], [3], [7]], log(1 + sqrt(2)))):
        K = Quad(d)
        eps, ex, ey = fundamental_unit(K)
        R = log(eps)
        control(f"Q(sqrt {d}): R = {R:.6f}", abs(R - want_R) < 1e-6,
                f"eps = {ex} + {ey} sqrt {d}")
        rd = sqrt(d)
        worst = 0.0
        for ps in sets_p:
            S = [P for p in ps for P in K.places(p)]
            found, idx = s_unit_data(K, S, 400)
            vecs = {f[2]: f for f in found if any(f[2])}
            pick = None
            for combo in combinations(list(vecs), len(S)):
                if lattice_index(combo, len(S))[0] == idx:
                    pick = [vecs[c] for c in combo]
                    break
            rows = [[log(abs(ex + ey * rd))] + [0.0] * len(S)]
            for x, y, vv in pick:
                rows.append([log(abs(x + y * rd))] +
                            [-vv[i] * log(K.NP(P)) for i, P in
                             enumerate(S)])
            RS = abs(det(rows))
            ratio = RS / (R * prod(log(K.NP(P)) for P in S))
            worst = max(worst, abs(ratio - idx))
            rank = 1 + len(lattice_index([f[2] for f in found],
                                         len(S))[1])
            print(f"      S_f over {ps}: rank {rank}, index {idx},"
                  f" R_S {RS:.6f}, ratio {ratio:.9f}")
        print(f"    Q(sqrt {d}): ratio = index to {worst:.1e} (equal by "
              "construction; the arithmetic)")


# ---------------------------------------------------------------- L
def residue(P, x, y):
    p, t = P
    if t == "inert":
        return (x % p, y % p)
    return (x + y * t) % p


def rmul(K, P, a, b):
    p, t = P
    if t == "inert":
        return ((a[0] * b[0] + K.d * a[1] * b[1]) % p,
                (a[0] * b[1] + a[1] * b[0]) % p)
    return a * b % p


def closure(gens, mul, one):
    seen, frontier = {one}, [one]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                z = mul(g, h)
                if z not in seen:
                    seen.add(z)
                    nxt.append(z)
        frontier = nxt
    return seen


def unit_residues(K, places, units):
    one = tuple(((1, 0) if P[1] == "inert" else 1) for P in places)
    gens = [tuple(residue(P, x, y) for P in places) for x, y in units]

    def mul(a, b):
        return tuple(rmul(K, P, u, v) for P, u, v in zip(places, a, b))
    return closure(gens, mul, one)


def group_order(K, P):
    return K.NP(P) - 1


def section_l():
    print("L  the layer face: the unit image is one joint corrector")
    K = Quad(2)
    units = [(-1, 0), (1, 1)]
    places = (K.places(3) + K.places(7) + K.places(17) + K.places(23))
    im = {P: len(unit_residues(K, [P], units)) for P in places}
    rows = {}
    for P, Q in combinations(places, 2):
        joint = len(unit_residues(K, [P, Q], units))
        rows[(P, Q)] = (im[P] * im[Q], joint, im[P] * im[Q] // joint)
    w = rows[((7, 3), (23, 5))]
    c = rows[((7, 3), (17, 6))]
    check("witness P7(r=3) * P23(r=5): prod 132, joint 66, rho 2",
          w == (132, 66, 2), str(w))
    check("P7(r=3) * P17(r=6) factors: rho 1", c[2] == 1, str(c))
    ent = [k for k, r in rows.items() if r[2] > 1]
    conj = [k for k in rows if k[0][0] == k[1][0] and k[0][1] != "inert"]
    check("7 of 21 pairs entangled, every conjugate pair among them",
          len(ent) == 7 and set(conj) <= set(ent),
          f"rho > 1 at {[(a, b, rows[(a, b)][2]) for a, b in ent]}")
    K = Quad(-5)
    units = [(-1, 0)]
    P3, P3c = K.places(3)
    P7c = K.places(7)[1]
    out = []
    for m in ([P3, P3c], [P3, P3c, P7c]):
        per = prod(len(unit_residues(K, [P], units)) for P in m)
        joint = len(unit_residues(K, m, units))
        hm = 2 * prod(group_order(K, P) for P in m) // joint
        out.append((per // joint, hm))
    check("Q(sqrt -5): rho 2 at two places, 4 at three",
          [r for r, _ in out] == [2, 4], str(out))
    print(f"    h_m by (6)'s formula with h = 2: "
          f"{[h for _, h in out]}")


def main():
    section_q()
    section_h()
    section_d()
    section_r()
    section_v()
    section_l()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
