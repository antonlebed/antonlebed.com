"""THE GENUS INDEX LAW -- the index of the realized triple subgroup is
3 to the number of genus lines the conductor carries.

THE QUESTION. A totally split prime of a non-cyclic cubic field K
carries three places whose classes (a, b, c) sum to zero in Cl(K);
write M for the sum-zero triples and R for the subgroup of M the
realized triples fill (explore_cubic_split_triple.py derivation (3): R
is the image of Gal(H~/N) under a homomorphism, stable under permuting
the coordinates, and every coordinate projection of R is onto Cl,
explore_cubic_transposition.py). Write d_K = f^2 d_0 with d_0
fundamental, k = Q(sqrt d_0) the resolvent and f the conductor, and
count the conductor's LINES:

    t(f) = #{ q == 1 (mod 3) : q | f } + [ 9 | f and 3 splits in k ].

explore_ray_class_lines.py derives that each line is a usable fixed
character of k's ray class group mod f and that a field with t = 0 is
uniform (R = M); explore_cubic_regime_sorter.py verifies "degenerate
iff t >= 1" on 193 fields of class number 3; and the two fields of
3-rank 2 in the box below |d_K| = 50000 (explore_rank2_hunt.py) print
index 9 at t = 2 and index 3 at t = 1.  Is [M : R] = 3^t in general?

THE DERIVATION, both halves, none of it computed here.

(1) WHAT IS FORCED. Let U be any S_3-stable subgroup of M whose first
    coordinate projection is onto Cl. For (a, b, c) in U the differences
    with its transpositions, (a-b, b-a, 0), (a-c, 0, c-a), (0, b-c, c-b),
    lie in U and sum to (3a, 3b, 3c). The set Y = {y : (y, -y, 0) in U}
    is a subgroup, and a - b and a - c lie in it (the second through the
    transposition of (a-c, 0, c-a)), so 3a = (a-b) + (a-c) lies in Y for
    every a in Cl: Y contains 3Cl, and U contains M_3 := M meet (3Cl)^3,
    since (a, b, c) = (a, -a, 0) + (0, -c, c).
    So U is the preimage of its image in M(Cl/3Cl) = V (x) St, V = Cl/3Cl
    of dimension r and St the two-dimensional permutation module over
    F_3, which is uniserial: the fixed line D = <(1,1,1)> sits under the
    sign character. Every S_3-stable subspace of V (x) St projecting onto
    V is W (x) St + V (x) D for a subspace W of V (apply 1 - sigma and
    1 + tau to a lift), of codimension r - dim W. Hence:
      - 3 does not divide h  ==>  R = M, at EVERY h, prime or composite;
      - 3-rank 1             ==>  R is M or Delta = {a == b == c mod 3Cl};
      - in general [M : R] = 3^(r - dim W_R) with
        W_R = { a - b mod 3Cl : (a, b, c) in R }.

(2) THE GENUS FIELD BOUNDS THE INDEX BELOW. For each line take the
    cyclic cubic field F over Q it names (conductor q, or 9); the local
    unit condition explore_ray_class_lines.py states makes KF/K
    unramified, so the compositum K* of K with the t fields F is an
    unramified (Z/3)^t-extension of K, the cubic GENUS FIELD, and the
    principal genus G = Gal(H/K*) has index 3^t in Cl. Each F is Galois
    over Q, so the three restrictions of any element of Gal(H~/N) to the
    three copies of K* agree: R lies in {a == b == c mod G}, of index
    3^t, so [M : R] >= 3^t -- and t <= r, the 3-rank, at every field.

(3) THE FIXED CHARACTERS BOUND IT ABOVE. Let E be the largest subfield
    of the compositum of the three copies of the 3-elementary class
    field that is abelian over k. Its group over N is R-bar/(sigma-1)R-bar
    = W_R (x) sign + (V/W_R) (x) trivial under conjugation, so the
    conjugation-FIXED cubic characters of E/k form a space of dimension
    exactly r - dim W_R, each a ray class character mod f satisfying the
    unit condition. A fixed character trivial on every local unit factors
    through Cl(k), whose 3-part conjugation inverts, so it is trivial:
    fixed usable characters inject into the sum of the fixed lines at the
    SPLIT primes of the conductor with nontrivial local 3-part, of which
    there are exactly t. So r - dim W_R <= t.

    Together: [M : R] = 3^t, and R is the set of triples that agree
    modulo the principal genus. At class number 3 this is the sorter's
    biconditional in both directions -- the Hilbert class field it was
    said to need IS the genus field KF -- and the "kill-shape" of a
    3-rank 1 field with two lines is impossible by (2).

THE SLATE, frozen before the run.

  P1  t <= r at every one of the 3133 fields of the checkpoint, so
      t = 0 at every field with trivial 3-part.  Kill: one field printing
      t > r.
  P2  At every field with 3 | h and at least ten mapped split primes, the
      generated order g satisfies g * 3^t <= h^2, the generated subgroup
      being a LOWER bound on R.  Kill: one field printing g * 3^t > h^2.
      And g * 3^t = h^2 at all but a handful: the expected number of
      fields whose primes all landed in a proper subgroup of a full R is
      under 0.09 on the sibling box (explore_rank2_hunt.py), so kill if
      three or more fields with twenty or more mapped primes print
      g * 3^t < h^2.
  P3  The two 3-rank 2 fields print t = 2 at |d| = 24843 (f = 91) and
      t = 1 at |d| = 47628 (f = 126), reproducing the two points the law
      was first read at.  A control on the conductor arithmetic, not a
      test of the law.
  P4  Positive control on the enumeration in S1: at every small group
      tried, the S_3-stable subgroups of M with onto projection number
      exactly the subspaces of Cl/3Cl, and every one contains M_3.
      Kill: any count off, or any such subgroup missing M_3.
  P5  Sanity on the decomposition: every q == 1 (mod 3) dividing f splits
      in k (Legendre (d_0 | q) = 1), which explore_ray_class_lines.py F2
      derives; kill on one violation.

Inputs: prime/code/_ckpt/r2_walk_50000.json, the rank-2 walk's checkpoint
(rebuilt by R2_CAP=50000 R2_CKPT=<path> explore_rank2_hunt.py), read
directly: per field (|d|, h, invariant factors, mapped split count, scalar
verdict, lattice verdict, generated order).  Memory trivial, wall seconds.

FINDINGS, copied from the print (28 s, memory trivial).

  F1  THE LAW HOLDS AT EVERY FIELD IT CAN BE READ AT (rule, proved above;
      verified on the 1367 fields with 3 | h and ten or more mapped split
      primes to |d_K| <= 50000): exact 1367, over-generated 0,
      under-generated 0.  By stratum (t = 0 / t = 1 / t = 2): h = 3 at
      Z/3 772 / 267; h = 6 at Z/6 145 / 50; h = 9 at Z/9 65 / 21 and at
      Z/3 x Z/3 0 / 1 / 1; h = 12 at Z/12 18 / 5 and at Z/2 x Z/6 2 / 0;
      h = 15 13 / 2; h = 18 0 / 2; h = 21 2 / 0; h = 33 1 / 0.  Both
      rank-2 fields as predicted: |d| = 24843, f = 91 = 7 * 13, t = 2,
      generated order 9, index 9; |d| = 47628, f = 126 = 2 * 3^2 * 7,
      t = 1, generated order 27, index 3.
  F2  t <= r AT ALL 3133 FIELDS (0 violations), the (r, t) census reading
      (0, 0) 1766, (1, 0) 1018, (1, 1) 347, (2, 1) 1, (2, 2) 1 -- so no
      field of trivial 3-part carries a line, and the kill-shape (3-rank
      1 with two lines) has no witness because genus theory forbids one.
      Every q == 1 (mod 3) dividing a conductor splits in k (0 violations).
  F3  THE SORTER'S BICONDITIONAL, "degenerate iff t >= 1", agrees with
      the lattice verdict at every h = 3 field of every band: 45 + 38 to
      6000, 79 + 32 to 13000, 159 + 60 to 24000, 489 + 137 to 50000
      (uniform + degenerate) -- and at every 3-rank 1 field of h = 6
      (145 + 50), 9 (65 + 21), 12 (20 + 5), 15 (13 + 2) and 18 (0 + 2),
      where it had only ever been asserted by transplant.
  F4  THE ENUMERATION CONTROL: at Cl = Z/2, Z/4, Z/5, Z/7, Z/8, Z/2 x Z/2,
      Z/2 x Z/4 exactly one S_3-stable subgroup of M projects onto Cl
      (M itself); at Z/3, Z/6, Z/9, Z/12 exactly two (indices 1, 3); at
      Z/3 x Z/3 and Z/3 x Z/6 exactly six (indices 1, 3, 3, 3, 3, 9) --
      the subspace counts 1, 2, 6 of F_3^r -- and every one contains
      M_3.  So the "composite h unchecked" gap on the image filling M was
      never a gap: off 3 the image is forced full at every h.
"""
import json
import os
import sys
from itertools import product
from collections import Counter, defaultdict

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.environ.get("R2_CKPT", os.path.join(HERE, "_ckpt", "r2_walk_50000.json"))

_FAIL = []


def ok(cond, msg):
    print("    [%s] %s" % ("ok" if cond else "KILL", msg))
    if not cond:
        _FAIL.append(msg)


def section(t):
    print("\n" + t)


# ------------------------------------------------ discriminant arithmetic
def squarefree_part(n):
    s = -1 if n < 0 else 1
    n = abs(n)
    f, d = 1, 2
    while d * d <= n:
        while n % (d * d) == 0:
            n //= d * d
            f *= d
        d += 1
    return s * n, f


def fundamental_part(dK):
    m, f = squarefree_part(dK)
    if m % 4 == 1:
        return m, f
    assert f % 2 == 0
    return 4 * m, f // 2


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def lines(dK):
    """(t, f, d_0, bad): the genus line count of the conductor, and the
    number of q == 1 (mod 3) dividing f that fail to split in k."""
    d0, f = fundamental_part(dK)
    t, bad = 0, 0
    for q in prime_factors(f):
        if q % 3 == 1:
            t += 1
            if legendre(d0, q) != 1:
                bad += 1
    if f % 9 == 0 and d0 % 3 == 1:
        t += 1
    return t, f, d0, bad


# --------------------------------------------- S1 the enumeration control
def stable_onto_subgroups(invs):
    """All subgroups of M = sum-zero triples over Cl = prod Z/n_i that
    are stable under S_3 and project onto Cl, as frozensets."""
    Cl = list(product(*[range(n) for n in invs]))
    add = lambda x, y: tuple((a + b) % n for a, b, n in zip(x, y, invs))
    neg = lambda x: tuple((-a) % n for a, n in zip(x, invs))
    M = [(a, b, add(neg(a), neg(b))) for a in Cl for b in Cl]
    perms = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (2, 1, 0), (1, 0, 2)]

    def join(S, g):
        """S + <g> for a subgroup S: the whole subgroup lattice is reached
        from the trivial subgroup by such joins."""
        out, x = set(S), g
        while x not in S:
            out.update(tuple(add(s[i], x[i]) for i in range(3)) for s in S)
            x = tuple(add(x[i], g[i]) for i in range(3))
        return frozenset(out)

    zero = frozenset({(tuple(0 for _ in invs),) * 3})
    seen, frontier = {zero}, [zero]
    while frontier:
        nxt = []
        for S in frontier:
            for g in M:
                if g in S:
                    continue
                T = join(S, g)
                if T not in seen:
                    seen.add(T)
                    nxt.append(T)
        frontier = nxt
    out = []
    for S in seen:
        stable = all(all(tuple(x[i] for i in p) in S for p in perms) for x in S)
        onto = len({x[0] for x in S}) == len(Cl)
        if stable and onto:
            out.append(S)
    return out, M


def s1_enumeration():
    section("S1  P4 THE ENUMERATION CONTROL -- stable subgroups of M with "
            "onto projection, against the subspaces of Cl/3Cl")
    cases = [(2,), (4,), (5,), (7,), (8,), (3,), (6,), (9,), (12,),
             (2, 2), (2, 4), (3, 3), (3, 6)]
    for invs in cases:
        subs, M = stable_onto_subgroups(invs)
        r = sum(1 for n in invs if n % 3 == 0)
        # number of subspaces of F_3^r
        nsub = {0: 1, 1: 2, 2: 6}[r]
        three = lambda x: tuple((3 * a) % n for a, n in zip(x, invs))
        cubes = {three(a) for a in product(*[range(n) for n in invs])}
        M3 = frozenset(x for x in M if all(x[i] in cubes for i in range(3)))
        contain = all(M3 <= S for S in subs)
        idx = sorted(len(M) // len(S) for S in subs)
        print("  Cl = %-14s r = %d  |M| = %4d  stable-onto subgroups %2d "
              "(subspaces %d)  indices %s  all contain M_3: %s"
              % ("x".join("Z/%d" % n for n in invs), r, len(M), len(subs),
                 nsub, idx, contain))
        ok(len(subs) == nsub and contain,
           "Cl = %s: %d subgroups against %d subspaces, M_3 contained %s"
           % (invs, len(subs), nsub, contain))


# ------------------------------------------------ S2-S4 the checkpoint
def load():
    with open(CKPT) as fh:
        blob = json.load(fh)
    return [tuple(f) for f in blob["fields"]], blob["cap"]


def s2_lines_vs_rank(fields):
    section("S2  P1, P5 THE LINE COUNT AGAINST THE 3-RANK, every field")
    over, badsplit = [], 0
    tab = Counter()
    for absd, h, invs, nmap, sc, lat, g in fields:
        t, f, d0, bad = lines(-absd)
        r = sum(1 for n in invs if n % 3 == 0)
        tab[(r, t)] += 1
        badsplit += bad
        if t > r:
            over.append((absd, h, invs, f, d0, t))
    print("  (3-rank, lines) census over %d fields:" % len(fields))
    for (r, t), n in sorted(tab.items()):
        print("    r = %d  t = %d : %5d" % (r, t, n))
    for row in over[:20]:
        print("    OVER: |d| %d h %d Cl %s f %d d0 %d t %d" % row)
    ok(not over, "t <= r at every field (%d violations)" % len(over))
    ok(badsplit == 0, "every q == 1 (mod 3) dividing f splits in k "
       "(%d violations)" % badsplit)
    return tab


def s3_index(fields):
    section("S3  P2, P3 THE INDEX AGAINST 3^t, fields with 3 | h and ten "
            "or more mapped split primes")
    overgen, under, exact = [], [], 0
    strata = defaultdict(Counter)
    for absd, h, invs, nmap, sc, lat, g in fields:
        if h % 3 or nmap < 10 or g is None:
            continue
        t, f, d0, _ = lines(-absd)
        r = sum(1 for n in invs if n % 3 == 0)
        pred = h * h // 3 ** t
        key = "h=%d Cl=%s" % (h, "x".join("Z/%d" % n for n in invs))
        if g > pred:
            overgen.append((absd, h, invs, nmap, f, t, g, pred))
            strata[key]["over"] += 1
        elif g < pred:
            under.append((absd, h, invs, nmap, f, t, g, pred))
            strata[key]["under"] += 1
        else:
            exact += 1
            strata[key]["t=%d exact" % t] += 1
        if invs == [3, 3] or tuple(invs) == (3, 3):
            print("  RANK 2: |d| %d  f = %d = %s  d0 = %d  t = %d  generated "
                  "order %d  predicted %d  index %d"
                  % (absd, f, "*".join(map(str, prime_factors(f))), d0, t, g,
                     pred, h * h // g))
    print("  exact %d   over-generated %d   under-generated %d"
          % (exact, len(overgen), len(under)))
    for key in sorted(strata, key=lambda k: (int(k[2:].split()[0]), k)):
        print("    %-22s %s" % (key, dict(strata[key])))
    for row in overgen[:20]:
        print("    OVER: |d| %d h %d Cl %s mapped %d f %d t %d generated %d "
              "predicted %d" % row)
    for row in under[:40]:
        print("    under: |d| %d h %d Cl %s mapped %d f %d t %d generated %d "
              "predicted %d" % row)
    ok(not overgen, "no field generates more than h^2 / 3^t (%d do)"
       % len(overgen))
    big_under = [u for u in under if u[3] >= 20]
    ok(len(big_under) < 3, "fields with >= 20 mapped primes generating less "
       "than h^2 / 3^t: %d (expected under 0.09)" % len(big_under))
    r2 = {absd: lines(-absd)[0] for absd, h, invs, *_ in fields
          if tuple(invs) == (3, 3)}
    ok(r2.get(24843) == 2 and r2.get(47628) == 1,
       "the two 3-rank 2 fields print t = %s" % r2)


def s4_sorter(fields):
    section("S4  THE SORTER REPRODUCED -- 'degenerate iff t >= 1' against "
            "the lattice verdict at h = 3, by band")
    for lo, hi in [(0, 6000), (6000, 13000), (13000, 24000), (24000, 50000)]:
        tab = Counter()
        for absd, h, invs, nmap, sc, lat, g in fields:
            if h != 3 or nmap < 10 or not (lo < absd <= hi):
                continue
            t = lines(-absd)[0]
            tab[(t >= 1, bool(lat))] += 1
        print("  %5d < |d| <= %5d : (line, degenerate) %s"
              % (lo, hi, dict(sorted(tab.items()))))
        ok(all(a == b for (a, b) in tab),
           "band (%d, %d]: predicate and verdict agree at every field" % (lo, hi))
    section("S4b THE SAME AT h = 6 AND h = 9 (3-rank 1), where the sorter "
            "was never checked")
    for hh in (6, 9, 12, 15, 18):
        tab = Counter()
        for absd, h, invs, nmap, sc, lat, g in fields:
            if h != hh or nmap < 10 or sum(1 for n in invs if n % 3 == 0) != 1:
                continue
            t = lines(-absd)[0]
            tab[(t >= 1, bool(lat))] += 1
        if tab:
            print("  h = %2d : (line, degenerate) %s" % (hh, dict(sorted(tab.items()))))
            ok(all(a == b for (a, b) in tab),
               "h = %d: predicate and lattice verdict agree at every field" % hh)


def main():
    fields, cap = load()
    print("checkpoint %s: %d fields with h > 1 to |d| <= %d"
          % (os.path.relpath(CKPT), len(fields), cap))
    s1_enumeration()
    s2_lines_vs_rank(fields)
    s3_index(fields)
    s4_sorter(fields)
    print("\n%s" % ("ALL OK" if not _FAIL else "KILLS: %d\n  " % len(_FAIL)
                     + "\n  ".join(_FAIL)))
    return 0 if not _FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
