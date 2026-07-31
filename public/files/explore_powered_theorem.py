"""Is the eigenvalue fingerprint distinct on EVERY powered tower?

THE QUESTION. The powered-rung scan (explore_powered_fingerprint.py)
proved distinctness for the towers with channels 8, 9, 25, 49, 11, 13,
17 — exponents at most 2 — by enumerating each channel's rational
pair differences exactly and checking that no nonzero choice sums to
zero. The per-channel sets it found look EXPONENT-INDEPENDENT:
{0, +-2, +-4} at the 2-power, {0, +-3} at the 3-power, empty at every
p >= 5 power. If that is a law of the prime and not of the exponent,
the k = 4..7 rule is an all-powered-towers theorem: any finite set of
prime-power channels over distinct primes, any exponents, any k.

THE PROOF, four steps, no computation at specific values — which is
what makes the claim below a THEOREM and this scan its cross-check.

(1) ISOLATION (unchanged from the powered rig): the moduli are pairwise
    coprime, so Gal(Q(zeta_N)/Q) is the product of the per-channel
    groups, and averaging a vanishing class-sum difference while fixing
    one channel makes that channel's own difference rational. Any
    collision forces EVERY per-channel difference rational.

(2) THE PER-CHANNEL LAW, uniform over all prime powers m = p^e: a
    NONZERO rational difference of two class values occurs only between
    classes whose values are BOTH rational. Proof by layers. The class
    value 2cos(2*pi*c/m) with d = v_p(c) equals 2cos(2*pi*c'/p^(e-d)),
    c' coprime to its layer n = p^(e-d), and when it is irrational it
    generates the real subfield Q(zeta_n)+, degree phi(n)/2 (standard:
    its Galois conjugates are exactly the phi(n)/2 coprime-class
    cosines). If v - v' is rational and v' is rational then v is
    rational — so only two irrational values need a case. There
    Q(v) = Q(v'), so both sit in one layer n = p^a (phi(p^a) is
    strictly increasing in a). Within that layer, average over
    Gal(Q(zeta_n)): each coprime-class cosine has the SAME orbit sum
    2*c_n(coprime) = 2*mu(n) (Ramanujan) — 0 at a >= 2, -2 at a = 1 —
    so the rational difference equals its own averaged value, 0, and
    2cos is strictly decreasing on the class range, so the classes are
    equal and the difference was not nonzero.

(3) NIVEN pins the rational values at every prime power: 2cos(theta)
    is rational for theta in [0, pi] only at theta in {0, pi/3, pi/2,
    2pi/3, pi}, i.e. c/m in {0, 1/6, 1/4, 1/3, 1/2}. A prime power is
    never divisible by 6; it is divisible by 4 only at p = 2, e >= 2,
    and by 3 only at p = 3. So the rational class values are — p = 2:
    {2, -2}, plus 0 when e >= 2, differences inside {0, +-2, +-4};
    p = 3: {2, -1}, differences {0, +-3}; p >= 5: {2} alone,
    differences empty. The exponent enters nowhere except 4 | 2^e.

(4) THE LATTICE CLASH, now over all towers: a tower holds at most one
    2-power and one 3-power channel. A nonzero choice from the sets in
    (3) is a nonzero even number of magnitude <= 4, a +-3, or their
    sum — odd, hence nonzero. No choice sums to zero, and a zero sum
    would BE an explicit collision (CRT realizes any choice of
    per-channel classes). Distinctness holds for every powered tower.

THE CLAIM (theorem): at every powered tower — channels p_i^(e_i) over
distinct primes, any k, any exponents — the prod(floor(m_i/2) + 1)
eigenvalue classes are pairwise distinct real numbers.

WHAT THIS SCAN IS FOR. The proof's new content against the powered rig
is step (2)'s layer law and step (3)'s exponent-independence; the rig
only ever ran e <= 2. This scan runs the SAME exact instrument (psi_m
from folding Phi_{p^e}, Rabin-certified, Dickson differences reduced
mod psi_m) at e = 2..5 — moduli 16, 32, 27, 81, 125 at depth 3..5,
plus 121, the second p >= 5 square — where every
constant reduction it finds either lands on a Niven pair (confirming)
or is a counterexample to (2)/(3) (killing the theorem in print).

THE TRANSPLANT, marked: every polynomial helper below is copied
verbatim from explore_powered_fingerprint.py (a module-level script,
not importable without running). The new territory is exponent depth:
the fold at e >= 3 (Phi_{p^e} sparser still), degrees up to 55, and
layer structure three deep — exercised by the positive controls at
16, 32, 27, 81 before any verdict is read.

FROZEN PREDICTIONS (fixed before any code ran):
  PR1 (instrument identities, exact): psi_m monic of degree phi(m)/2
      (4, 8, 9, 27, 50, 55 for m = 16, 32, 27, 81, 125, 121);
      psi_m(2) = p (from Phi_{p^e}(1) = p, not p^e); psi_m irreducible
      mod a small prime q (Rabin); float tie |psi_m(2cos(2*pi/m))|
      under 1e-9 at every modulus.
  PR2 (positive controls, read FIRST): constant pairs at exactly the
      Niven classes — m = 16: (4,0), (8,0), (8,4) with constants
      -2, -4, -2; m = 32: (8,0), (16,0), (16,8) with -2, -4, -2;
      m = 27: exactly (9,0), constant -3; m = 81: exactly (27,0),
      constant -3. A detector blind at depth 3 reads nothing.
  PR3 (the scan): m = 125 and m = 121 are SILENT — every pair
      difference reduces nonconstant (1953 and 1830 pairs).
  PR4 (the sets): rational-difference sets {0, +-2, +-4} at 16 and 32,
      {0, +-3} at 27 and 81, empty at 125 and 121 — equal to the
      powered rig's sets at 8, 9, 25, 11: exponent-independent, as
      step (3) derives.
  PR5 (the verdict, step (4) as an observable): over the two nonempty
      set shapes {0, +-2, +-4} x {0, +-3}, zero-sum choices with a
      nonzero entry: none. KILL OBSERVABLE for the whole claim: a
      printed constant pair at any modulus outside its Niven classes
      (kills (2)/(3)), or a printed nonzero zero-sum choice (kills
      (4)).

Memory trivial (integer coefficient lists, degree <= 55); wall-clock
estimate well under a minute. Run:
python prime/code/explore_powered_theorem.py

FINDINGS (entered by the post-run edit; the creating write ended at
the design).

  F1 (PR1 CONFIRMED, one frozen bound repaired). All six moduli: psi_m
      monic of the predicted degree (4, 8, 9, 27, 50, 55), psi_m(2) = p
      exactly, Rabin certificates mod q = 3 (16, 32) and q = 2 (the
      rest). The frozen float bound 1e-9 was the SLATE's error, not the
      instrument's: evaluating a degree-27+ polynomial at x near 2
      carries condition sum |c_i| x^i (2.0e10 at 81, 1.3e19 at 125,
      1.1e21 at 121), so the residual is read against that — 1.7e-07 vs
      2.0e10 at 81, 1.3e+02 vs 1.3e19 at 125, 2.4e+03 vs 1.1e21 at
      121, all at or under 1e-13 of condition (a wrong psi would sit AT
      the condition scale). The exact identities carry the
      certification; the float tie saturates double precision by
      degree 50 and is only a sanity cross-check there.

  F2 (PR2 CONFIRMED — the detector fires at depth 3..5). m = 16:
      constant at exactly (4,0), (8,0), (8,4), constants -2, -4, -2;
      m = 32: exactly (8,0), (16,0), (16,8), constants -2, -4, -2;
      m = 27: exactly (9,0), constant -3; m = 81: exactly (27,0),
      constant -3. The predicted Niven pairs, the predicted constants,
      and nothing else.

  F3 (PR3 CONFIRMED). m = 125 (1953 pairs) and m = 121 (1830 pairs):
      constant at none — 4,866 pairs scanned in all.

  F4 (PR4 + PR5 CONFIRMED — the verdict). Per-modulus sets with 0:
      [-4,-2,0,2,4] at 16 AND 32, [-3,0,3] at 27 AND 81, [0] at 125
      and 121 — equal to the powered rig's sets at 8, 9, 25, 11:
      exponent-independent, exactly as step (3) derives. Zero-sum
      choices over the two nonempty shapes: 0. VERDICT:
      EXPONENT-INDEPENDENT, DISTINCT. With steps (1), (2), (4) proved
      uniformly in the docstring, the claim stands at THEOREM: every
      powered tower — any distinct primes, any exponents, any k — has
      all prod(floor(m_i/2) + 1) eigenvalue classes distinct.

  RUN RECORD: python prime/code/explore_powered_theorem.py — 0.076 s
      real, all sections green, verdict EXPONENT-INDEPENDENT, DISTINCT.
      Two pre-verdict repairs, both to PR1's float-tie tolerance (an
      absolute 1e-9, then max-coefficient scaling — both mis-frozen;
      the condition-number scaling above is what a near-2 evaluation
      point actually warrants); no verdict-path change. Re-run whole
      after the audit corrected the stated exponent range (121 is
      e = 2, not 3..5; prints and prose now say e = 2..5): 0.096 s,
      same verdict, same sets, 4,866 pairs.
"""

from itertools import product as iproduct
from math import cos, pi

# (p, e) for the scan: both nonempty branches at depth >= 3 (two depths
# each), the p >= 5 branch at depth 3, and 121 as the second p >= 5
# square.
MODULI = [(2, 4), (2, 5), (3, 3), (3, 4), (5, 3), (11, 2)]


def section(title):
    print(f"\n{'=' * 72}\n  {title}\n{'=' * 72}")


# -- integer polynomial helpers (little-endian coefficient lists),
# -- transplanted verbatim from explore_powered_fingerprint.py ----------

def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(n)]


def psub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
            for i in range(n)]


def pnorm(a):
    while a and a[-1] == 0:
        a = a[:-1]
    return a


def pmod(a, m):
    """Reduce a mod monic m, exact integer division steps."""
    a = list(a)
    dm = len(m) - 1
    while len(pnorm(a)) - 1 >= dm and pnorm(a):
        a = pnorm(a)
        lead, da = a[-1], len(a) - 1
        for i, c in enumerate(m):
            a[da - dm + i] -= lead * c
    return pnorm(a)


def peval_int(a, x):
    v = 0
    for c in reversed(a):
        v = v * x + c
    return v


def peval_float(a, x):
    v = 0.0
    for c in reversed(a):
        v = v * x + c
    return v


def dickson_polys(m):
    """D_0..D_m with D_j(z + 1/z) = z^j + z^-j."""
    D = [[2], [0, 1]]
    for _ in range(2, m + 1):
        D.append(pnorm(psub([0] + D[-1], D[-2])))
    return D[:m + 1]


def cyclotomic_pe(p, e):
    """Phi_{p^e}(z) = Phi_p(z^(p^(e-1))), little-endian, exact."""
    step = p ** (e - 1)
    out = [0] * ((p - 1) * step + 1)
    for j in range(p):
        out[j * step] = 1
    return out


def fold(P):
    """z^-d * P(z) for palindromic monic P of even degree 2d, written in
    x = z + 1/z: returns b_d + sum_{j=1..d} b_{d+j} D_j(x)."""
    d = (len(P) - 1) // 2
    assert P == P[::-1], "fold needs a palindromic polynomial"
    D = dickson_polys(d)
    out = [P[d]]
    for j in range(1, d + 1):
        if P[d + j]:
            out = padd(out, [P[d + j] * c for c in D[j]])
    return pnorm(out)


# -- Rabin irreducibility over F_q, exact (as in the powered rig) --------

def pmulmod(a, b, mod, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca:
            for j, cb in enumerate(b):
                out[i + j] = (out[i + j] + ca * cb) % q
    return [c % q for c in pmod(out, mod)]


def ppowmod(base, e, mod, q):
    r = [1]
    while e:
        if e & 1:
            r = pmulmod(r, base, mod, q)
        base = pmulmod(base, base, mod, q)
        e >>= 1
    return r


def pgcd_fq(a, b, q):
    a = [c % q for c in pnorm(a)]
    b = [c % q for c in pnorm(b)]
    while pnorm(b):
        b = pnorm(b)
        inv = pow(b[-1], q - 2, q)
        b = [c * inv % q for c in b]
        a = [c % q for c in pmod(a, b)]
        a, b = b, a
    return pnorm(a)


def rabin_irreducible(ps, q):
    m = len(ps) - 1
    mq = [c % q for c in ps]
    if mq[-1] != 1:
        return False

    def frob_iter(k):
        t = [0, 1]
        for _ in range(k):
            t = ppowmod(t, q, mq, q)
        return t

    if pnorm(psub(frob_iter(m), [0, 1])):
        return False
    ls = {l for l in range(2, m + 1) if m % l == 0
          and all(l % d for d in range(2, l))}
    for l in ls:
        g = pgcd_fq(psub(frob_iter(m // l), [0, 1]), mq, q)
        if len(g) != 1:
            return False
    return True


# -- S1: the instrument at depth 2..5, exact -----------------------------

section("S1. psi_m AT e = 2..5 — fold, identities, certificates")
SMALL_Q = [q for q in range(2, 400)
           if all(q % d for d in range(2, int(q ** 0.5) + 1))]
PSI = {}
for p, e in MODULI:
    m = p ** e
    ps = fold(cyclotomic_pe(p, e))
    deg = (p - 1) * p ** (e - 1) // 2
    assert len(ps) - 1 == deg and ps[-1] == 1, (m, ps)
    at2 = peval_int(ps, 2)
    assert at2 == p, (m, at2)                       # PR1: psi_m(2) = p
    cert = next((q for q in SMALL_Q if q != p and rabin_irreducible(ps, q)),
                None)
    assert cert is not None, m
    xf = 2 * cos(2 * pi / m)
    flt = abs(peval_float(ps, xf))
    cond = sum(abs(c) * xf ** i for i, c in enumerate(ps))
    assert flt < 1e-13 * max(1.0, cond), (m, flt, cond)  # PR1: float
    PSI[m] = (ps, dickson_polys(m // 2))            # tie, relative to
    print(f"  m={m:3d}  deg={deg:2d}  psi(2)={at2}"  # the evaluation's
          f"  irreducible mod q={cert:2d}"           # condition number
          f"  |psi(x)|={flt:.1e}  vs cond {cond:.1e}")


def reduced_diff(m, c, cp):
    """D_c - D_cp reduced mod psi_m; classes c, cp in 0..m//2."""
    ps, D = PSI[m]
    return pmod(psub(D[c], D[cp]), ps)


# -- S2: positive control — the Niven pairs at depth >= 3 ----------------

section("S2. POSITIVE CONTROL — 16, 32, 27, 81 fire at their Niven pairs")
NIVEN_PAIRS = {
    16: {(4, 0): -2, (8, 0): -4, (8, 4): -2},
    32: {(8, 0): -2, (16, 0): -4, (16, 8): -2},
    27: {(9, 0): -3},
    81: {(27, 0): -3},
}
for m, want in sorted(NIVEN_PAIRS.items()):
    found = {}
    for c in range(m // 2 + 1):
        for cp in range(c):
            r = reduced_diff(m, c, cp)
            if len(r) <= 1:
                assert r and r[0] != 0, (m, c, cp)  # a zero constant is
                found[(c, cp)] = r[0]               # a collision: abort
    print(f"  m={m:3d}  constant at exactly {sorted(found.items())}")
    assert found == want, (m, found, want)          # PR2


# -- S3: the scan — every pair at every modulus, exact -------------------

section("S3. THE SCAN — pair differences mod psi_m, all six moduli")
DIFFS = {}
total = 0
for p, e in MODULI:
    m = p ** e
    consts = set()
    pairs = 0
    for c in range(m // 2 + 1):
        for cp in range(c):
            pairs += 1
            r = reduced_diff(m, c, cp)
            if len(r) <= 1:
                assert r and r[0] != 0, (m, c, cp)
                consts.add(r[0])
                consts.add(-r[0])
    total += pairs
    DIFFS[m] = sorted(consts)
    print(f"  m={m:3d}  pairs={pairs:4d}"
          f"  rational differences: {DIFFS[m] if DIFFS[m] else 'NONE'}")
print(f"\n  total pairs scanned: {total}")


# -- S4: exponent-independence and the verdict ---------------------------

section("S4. THE VERDICT — sets exponent-independent, no zero sum")
PRIME_LAW = {2: [-4, -2, 0, 2, 4], 3: [-3, 0, 3], 5: [0], 11: [0]}
ok = True
for p, e in MODULI:
    m = p ** e
    got = sorted(set(DIFFS[m]) | {0})
    same = got == PRIME_LAW[p]
    ok = ok and same
    print(f"  m={m:3d}  set {got}  =  prime-{p} law {PRIME_LAW[p]}: {same}")
shapes = [[-4, -2, 0, 2, 4], [-3, 0, 3]]
hits = [ch for ch in iproduct(*shapes) if any(ch) and sum(ch) == 0]
print(f"  zero-sum choices over the two nonempty shapes: {len(hits)}")
for h in hits:
    print(f"    KILL: {h}")
verdict = "EXPONENT-INDEPENDENT, DISTINCT" if ok and not hits else "KILL"
print(f"\n  VERDICT: {verdict}")
