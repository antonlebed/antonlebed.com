"""explore_arrival_defect.py — the arrival-defect chart's classical identity
(explore_local_clock.py's open remainder).

THE QUESTION. The two-gear census found the
per-class splice landings of the breathing clock's transient. Seat-STARTER
classes (v(u-1) = i*) land at p*i*+1 universally (dying seats). ARRIVAL
classes (level-c units whose Frobenius segment reaches the seat, e = c*2^m
at p = 2) land DEEPER by an extra {0, 0, 1, 2, 5} across the censused
fields — finer than (e, f, different-exponent). WHAT CLASSICAL INVARIANT
IS THE ARRIVAL LANDING?

THE CANDIDATE LAW (hand-derived, before this file
existed): factor u^{2^m} + 1 = prod (u - zeta) over the primitive
2^{m+1}-th roots of unity, all at v(zeta - 1) = c. The landing
L(c) = e + A(c), A(c) = min over class-c u of v(u^{2^m} + 1), is the
AVOIDANCE VALUE of the torsion constellation: each root is approached
exactly as deep as K's structure FORCES (integer levels, F_2 residues).
The forcing ends at a fractional level (K(zeta)/K ramified), at a non-F_2
residue (unramified), or at the constellation's own branching when the
torsion is IN K (a tree game on the pairwise distances v(zeta - zeta') —
the higher-unit filtration of the torsion; the identity
i - 1 = sqrt2 * zeta8^3 pins the expansion of i over every K). The
arrival extras thereby grade the SPLITTING OF THE 2-POWER CYCLOTOMIC
TOWER over K: the transient reads the ramification of K(mu_{2^{m+1}})/K.

THE PREDICTIONS (fixed and hand-attacked
before this file existed; one pre-engine correction — AD6's class-4 value,
where the escape-branch e+c was beaten by tree avoidance, the e=2/zeta8
agreement having been the coincidence e = c+2):

AD1 (regression): every dying-seat starter lands at p*i*+1.
AD2 (out-of-sample fields): Q2(sqrt10), Q2(sqrt-10): landing minima
    {2: 5, 1: 5}, and their E-chains equal Q2(sqrt2)'s.
AD3 (the trichotomy — the classical identity at e = 2): across all six
    ramified quadratics of Q2, extra(class 1) = 0 / 1 / 2 iff K(i)/K is
    RAMIFIED / UNRAMIFIED / SPLIT, the label computed INDEPENDENTLY of
    any orbit: split iff -1 is a square in K, unramified iff -5 is a
    square in K (Delta = 5 the unramified generator; both by exhaustive
    unit search with the Hensel threshold v > 2e), else ramified.
    Expected labels: sqrt2/sqrt-2/sqrt10/sqrt-10 ram, sqrt-5 unram
    (the unique one), i split.
AD4 (rigidity grading): the class-1 landing SPECTRUM is single-valued
    {5} at the four ram fields and {6} at sqrt-5 (the forced approach to
    i is rigid: fractional-level resp. F_4-residue cutoff); graded with
    min 7 and torsion members at CAP in Q2(i).
AD5 (the tree game at zeta8): class minima {4: 9, 2: 10, 1: 14}; the
    achieving class-1 unit's factor multiset {v(u - zeta8^k), k odd} =
    {2, 2, 3, 3} (collide one antipodal pair, avoid the other); the
    class-2 achieving unit's {v(u - i), v(u + i)} = {3, 3}; and the
    escape identity (zeta8 - zeta8^7)^2 = -2 exactly.
AD6 (out-of-sample tower, sampled tier): Q2(zeta16), e = 8: landing
    minima classes (8, 4, 2, 1) = (17, 18, 20, 28)
    [floor; +-i tree: collide at 4, avoid at 5, A = 10; prim-8th tree:
    4 x 3 = 12; prim-16th tree: 4*2 + 4*3 = 20].
AD7 (cross-p, out-of-sample): Q3(zeta9), e = 6, i* = 3: class 2 NAIVE
    (the tripling gear jumps 2 -> 6 past the seat), landing minima
    {3: 10, 1: 12} [floor 3*3+1; F_3 tree: six prim-9th roots in two
    mod-3 clusters at internal distance 3, u collides exactly one
    cluster (2,2,2), avoids the other (1,1,1): 3 + 9 = 12].
AD8 (the Hensel cap): at every censused p=2 f=1 field with i not in K
    and an arrival class c = e/2: A(e/2) <= 2e (quadratic-defect
    boundedness read dynamically).

THE DESIGN. Fields as monogenic Eisenstein orders via the LF machinery of
explore_local_clock (imported; convention f=1: g = [0,1]). Exhaustive
census (every representative of U_1/U_amax) at Q2, the six ramified
quadratics, x^3-2, x^6-2, zeta8; SAMPLED census at zeta16 (e=8) and
zeta9 (p=3, e=6), where exhaustive enumeration at the needed amax is out
of reach — per-class random units (seeded rng; class-c leading
coefficient forced nonzero), minima over the sample asserted against the
slate (the avoidance branch is generic, miss probability vanishing in
the sample size; a sampled min BELOW prediction falsifies the law
outright). Landing extraction: an orbit passing through the seat
contributes o[n+1] keyed by its start class o[0]. Trichotomy labels by
exhaustive max of v(u^2 + 1) and v(u^2 + 5) against the 2e threshold.
Run: python prime/code/explore_arrival_defect.py

FINDINGS (entered post-run, copied from printed output).

1. THE TRICHOTOMY IS EXACT (rule, exhaustive over ALL SIX ramified
   quadratic extensions of Q2): extra(class 1) = 0 / 1 / 2 iff K(i)/K is
   ramified / unramified / split, both sides computed independently —
   sqrt-5 the unique unramified field (extra 1), Q2(i) split (extra 2),
   sqrt2 / sqrt-2 / sqrt10 / sqrt-10 ramified (extra 0). The two fields
   an earlier census never saw, sqrt10 and sqrt-10, were predicted extra 0
   on sqrt2's E-chain and measured exactly so (chains identical,
   landings {2: 5, 1: 5}).

2. THE RIGIDITY GRADING (rule in range): the class-1 landing spectrum is
   single-valued exactly where the approach to i is blocked — {5} at the
   four ramified fields (fractional-level cutoff: i - 1 = sqrt2*zeta8^3
   departs at 3e/4, a half-level), {6} at sqrt-5 (F_4-residue cutoff at
   level 2), and graded {7, ..., CAP} at Q2(i) (torsion in-field; CAP =
   the dying torsion members). The sextic's class-3 spectrum {14, 15} is
   the i-expansion read off exactly: terms at 3 and 9/2 only, so avoid
   gives A = 4+4 and follow gives A = 9/2+9/2, nothing deeper.

3. THE TREE GAME (rule in range at zeta8; sampled at zeta16): where the
   torsion is IN K the landing is the avoidance value of the
   constellation's own branching, factor-exact — the achieving class-1
   unit at zeta8 approaches the four primitive 8th roots with multiset
   {2, 2, 3, 3} (collide one antipodal pair at the level-2 fork, avoid
   the other), the class-2 unit {3, 3}; minima {4: 9, 2: 10, 1: 14};
   (zeta8 - zeta8^7)^2 = -2 exactly (the escape identity). The
   out-of-sample tower Q2(zeta16) hits all four predictions
   (17, 18, 20, 28) — including class 4's 18, where tree avoidance
   BEATS the escape branch e+c = 12 (the e=2/zeta8 agreement of the two
   was the coincidence e = c+2, caught in the pre-engine hand re-check).

4. THE CROSS-p FACE (sampled): Q3(zeta9) — the F_3 tree value 12 hits
   (six primitive 9th roots in two mod-3 clusters at internal distance
   3: collide exactly one cluster (2,2,2), avoid the other (1,1,1),
   landing 3 + 9), the starter floor 10 hits, and class 2 is naive as
   the gear demands (500 sampled orbits, the tripling gear jumps
   2 -> 6 past the seat i* = 3).

5. THE CLASSICAL IDENTITY (this file's answer; rule in range over the
   census, synthesis of 1-4): the
   arrival landing is the avoidance value of the primitive p^{m+1}-th
   torsion constellation over K — the breathing clock's transient reads
   the RAMIFICATION OF THE p-POWER CYCLOTOMIC TOWER: the forced approach
   to each root ends at a fractional level iff K(zeta)/K is ramified, at
   a non-F_p residue iff unramified, and at the constellation's own
   higher-unit branching iff zeta is in K. The Hensel cap A(e/2) <= 2e
   (i not in K) held everywhere — the dynamical face of quadratic-defect
   boundedness. (GENERALIZED in a later run: the cut level is delta/p,
   delta the Kummer defect of the storey-down root, and the break is
   p*i* - delta — the O'Meara/Hasse-Herbrand contact landed;
   explore_cutoff_ladder.py.)

RUN RECORD (python explore_arrival_defect.py, 6.3 s, exit 0): 551 checks
passed. Landings as printed (spectra truncated at six values):
  quadratics    class 1: {5} {5} {5} {5} / {6} / {7,8,9,10,11,12,...}
                class 2 (seat): {5,6,7,8,9,10,...} all six
  Q2 {1: 3...}  cube {3: 7...}   sextic {3: {14,15}, 6: {13,...,CAP}}
  zeta8         1->{14,CAP} 2->{10,13,14,15,16,CAP} 4->{9,10,...}
  zeta16 (400/class) 1->{28,CAP} 2->{20,26,28,30,CAP} 4->{18,20,22,...}
                8->{17,18,...}
  zeta9  (sampled)   1->{12,CAP} 3->{10,11,12,13,14,CAP}, class 2 naive
Green on the first run; no pre-green failures.
"""

import random

import explore_local_clock as lc

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ---------------------------------------------------------------- helpers


def esub(F, A, B):
    return tuple(F.cadd(a, F.cint(b, -1)) for a, b in zip(A, B))


def const_el(F, n):
    el = [list(F.zero_c) for _ in range(F.e)]
    el[0][0] = n % F.pM
    return tuple(tuple(c) for c in el)


def landing_spectra(F, units_iter, keep_orbits=False):
    """Per-start-class landing spectra {class: set of post-seat values}."""
    spec, orbits = {}, []
    for u in units_iter:
        o = F.orbit(u)
        if keep_orbits:
            orbits.append(o)
        if F.seat is not None and F.seat in o:
            n = o.index(F.seat)
            if n + 1 < len(o):
                spec.setdefault(o[0], set()).add(o[n + 1])
    return spec, orbits


def sq_approach(F, n):
    """max over U_1/U_amax representatives u of v(u^2 - n)."""
    tgt = const_el(F, n)
    best = 0
    for u in F.units():
        vv = F.val(esub(F, F.emul(u, u), tgt))
        if vv > best:
            best = vv
    return best


def sample_class(F, c, count, rng):
    """count random units with v(u-1) = c exactly (f = 1 fields only)."""
    monos = []
    for i in range(F.M):
        for j in range(F.e):
            n = F.e * i + j
            if c <= n < F.amax:
                monos.append((i, j, n))
    for _ in range(count):
        u = [list(cc) for cc in F.one]
        for (i, j, n) in monos:
            a = rng.randrange(1, F.p) if n == c else rng.randrange(F.p)
            if a:
                u[j][0] = (u[j][0] + a * (F.p ** i)) % F.pM
        yield tuple(tuple(cc) for cc in u)


def fmt_spec(F, spec):
    out = {}
    for c in sorted(spec):
        vals = sorted(spec[c])
        s = ["CAP" if v >= F.CAP else str(v) for v in vals[:6]]
        if len(vals) > 6:
            s.append("...")
        out[c] = "{%s}" % ",".join(s)
    return " ".join("%d->%s" % (c, out[c]) for c in sorted(out))


# ------------------------------------------------------------------- zoo

QUADS = [
    # name           eis            expected trichotomy label, extra
    ("Q2(sqrt2)",   [-2, 0, 1],    "ram",   0),
    ("Q2(sqrt-2)",  [2, 0, 1],     "ram",   0),
    ("Q2(sqrt10)",  [-10, 0, 1],   "ram",   0),
    ("Q2(sqrt-10)", [10, 0, 1],    "ram",   0),
    ("Q2(sqrt-5)",  [6, -2, 1],    "unram", 1),
    ("Q2(i)",       [2, -2, 1],    "split", 2),
]


def run():
    rng = random.Random(184)
    print("THE ARRIVAL DEFECT — the classical identity census")
    print("=" * 64)

    # ---------------- section 1: the six ramified quadratics (e = 2)
    print("\n[1] the six ramified quadratics: trichotomy + rigidity")
    chains = {}
    for name, eis, want_label, want_extra in QUADS:
        F = lc.LF(name, 2, [0, 1], eis, 12)
        spec, orbits = landing_spectra(F, F.units(), keep_orbits=True)
        chains[name] = lc.chain_from_orbits(2, orbits, F.amax)
        # independent classical label
        split = sq_approach(F, -1) > 2 * F.e
        unram = sq_approach(F, -5) > 2 * F.e
        label = "split" if split else ("unram" if unram else "ram")
        # AD1: starter floor
        ok(min(spec[F.seat]) == 2 * F.e + 1,
           "%s: starter floor missed: %s" % (name, sorted(spec[F.seat])))
        # AD3: trichotomy, both sides independent
        extra = min(spec[1]) - (2 * F.e + 1)
        ok(label == want_label,
           "%s: classical label %s, expected %s" % (name, label, want_label))
        ok(extra == want_extra,
           "%s: extra %d, expected %d" % (name, extra, want_extra))
        # AD4: rigidity grading
        if label == "ram":
            ok(spec[1] == {5}, "%s: ram spectrum not rigid {5}: %s"
               % (name, sorted(spec[1])))
        elif label == "unram":
            ok(spec[1] == {6}, "%s: unram spectrum not rigid {6}: %s"
               % (name, sorted(spec[1])))
        else:
            ok(min(spec[1]) == 7, "%s: split min not 7" % name)
            ok(F.CAP in spec[1] and len(spec[1]) > 1,
               "%s: split spectrum not graded to CAP" % name)
        # AD8: Hensel cap
        if label != "split":
            ok(min(spec[1]) - F.e <= 2 * F.e,
               "%s: Hensel cap broken" % name)
        print("  %-12s label=%-6s extra=%d  landings %s"
              % (name, label, extra, fmt_spec(F, spec)))
    # AD2: the new fields ride the sqrt2 chain
    for nm in ("Q2(sqrt10)", "Q2(sqrt-10)"):
        ok(chains[nm] == chains["Q2(sqrt2)"],
           "%s: chain differs from sqrt2's" % nm)
    print("  sqrt10 / sqrt-10 E-chains == sqrt2's: %s" % chains["Q2(sqrt2)"])

    # ---------------- section 2: Q2, cube, sextic — floors + cap
    print("\n[2] Q2, x^3-2, x^6-2: floors, the sextic arrival")
    for name, eis, amax, floors in [
            ("Q2", [-2, 1], 10, {1: 3}),
            ("Q2(2^{1/3})", [-2, 0, 0, 1], 13, {3: 7}),
            ("Q2(2^{1/6})", [-2, 0, 0, 0, 0, 0, 1], 16, {6: 13, 3: 14})]:
        F = lc.LF(name, 2, [0, 1], eis, amax)
        spec, _ = landing_spectra(F, F.units())
        for c, want in floors.items():
            ok(min(spec[c]) == want,
               "%s: class %d min %d, expected %d"
               % (name, c, min(spec[c]), want))
        if name == "Q2(2^{1/6})":
            ok(min(spec[3]) - F.e <= 2 * F.e, "sextic: Hensel cap broken")
        print("  %-12s landings %s" % (name, fmt_spec(F, spec)))

    # ---------------- section 3: zeta8 — the tree game, factors exact
    print("\n[3] Q2(zeta8): the tree game")
    F = lc.LF("Q2(zeta8)", 2, [0, 1], [2, 4, 6, 4, 1], 16)
    spec, _ = landing_spectra(F, F.units())
    for c, want in [(4, 9), (2, 10), (1, 14)]:
        ok(min(spec[c]) == want,
           "zeta8: class %d min %d, expected %d" % (c, min(spec[c]), want))
    # zeta8 = x + 1; its powers
    z = [None] * 8
    z[1] = ((1,), (1,), (0,), (0,))
    for k in range(2, 8):
        z[k] = F.emul(z[k - 1], z[1])
    # escape identity: (zeta8 - zeta8^7)^2 + 2 = 0
    x = esub(F, z[1], z[7])
    ok(F.val(x) == 2, "zeta8: v(zeta8 - zeta8^7) != 2")
    ok(F.val(esub(F, F.emul(x, x), const_el(F, -2))) >= F.amax,
       "zeta8: (zeta8-zeta8^7)^2 != -2")
    # factor multisets at the achieving units
    got1 = got2 = None
    for u in F.units():
        o = F.orbit(u)
        if o[0] == 1 and F.seat in o and got1 is None:
            n = o.index(F.seat)
            if n + 1 < len(o) and o[n + 1] == 14:
                got1 = sorted(F.val(esub(F, u, z[k])) for k in (1, 3, 5, 7))
        if o[0] == 2 and F.seat in o and got2 is None:
            n = o.index(F.seat)
            if n + 1 < len(o) and o[n + 1] == 10:
                got2 = sorted([F.val(esub(F, u, z[2])),
                               F.val(esub(F, u, z[6]))])
        if got1 and got2:
            break
    ok(got1 == [2, 2, 3, 3],
       "zeta8: class-1 factor multiset %s != [2,2,3,3]" % got1)
    ok(got2 == [3, 3], "zeta8: class-2 factor multiset %s != [3,3]" % got2)
    print("  landings %s" % fmt_spec(F, spec))
    print("  class-1 factors %s   class-2 factors %s" % (got1, got2))

    # ---------------- section 4: zeta16, sampled (out-of-sample tower)
    print("\n[4] Q2(zeta16), e=8, sampled (400/class)")
    F = lc.LF("Q2(zeta16)", 2, [0, 1],
              [2, 8, 28, 56, 70, 56, 28, 8, 1], 30)
    spec = {}
    for c in (8, 4, 2, 1):
        sp, _ = landing_spectra(F, sample_class(F, c, 400, rng))
        if c in sp:
            spec[c] = sp[c]
    for c, want in [(8, 17), (4, 18), (2, 20), (1, 28)]:
        ok(c in spec and min(spec[c]) == want,
           "zeta16: class %d min %s, expected %d"
           % (c, sorted(spec.get(c, [])), want))
    print("  landings %s" % fmt_spec(F, spec))

    # ---------------- section 5: zeta9, sampled (cross-p)
    print("\n[5] Q3(zeta9), e=6, sampled")
    F = lc.LF("Q3(zeta9)", 3, [0, 1], [3, 9, 18, 21, 15, 6, 1], 14)
    ok(F.seat == 3, "zeta9: seat != 3")
    spec = {}
    for c, cnt in ((3, 800), (1, 1500)):
        sp, _ = landing_spectra(F, sample_class(F, c, cnt, rng))
        spec[c] = sp.get(c, set())
    for c, want in [(3, 10), (1, 12)]:
        ok(spec[c] and min(spec[c]) == want,
           "zeta9: class %d min %s, expected %d"
           % (c, sorted(spec[c]), want))
    for u in sample_class(F, 2, 500, rng):
        o = F.orbit(u)
        ok(F.seat not in o, "zeta9: class-2 orbit hit the seat: %s" % o)
    print("  landings %s   class 2: naive (500 sampled orbits skip "
          "the seat)" % fmt_spec(F, spec))

    print("\n%d checks passed" % CHECKS)


if __name__ == "__main__":
    run()
