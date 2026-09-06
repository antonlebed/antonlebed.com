r"""THE RAMIFIED TERM -- are the residuals the all-principal triple keeps
after the unramified prime powers are put back the explicit formula's
RAMIFIED prime powers, read by their inertia cosets? (child of
explore_triple_cube_term.py, whose F2 left the h = 2 excess and the
h = 3 deficit open inside an unallocated bound; sibling of
explore_ceiling_squares.py, which put the ramified ideals back at
degree 2 as 1/(2k) on the class k.r.)

THE QUESTION. Over the complex cubic fields to |d| <= 24000 with h > 1
and the prime powers q^k < 1000, the count of totally split primes
whose three places are all principal, corrected by the unramified
prime powers landing on the identity, sits OVER the uniform share 1/h^2
at h = 2 (level 1.058 +- 0.017, z = +3.46) and UNDER it at h = 3's
full-image regime (0.877 +- 0.033, z = -3.74). The ramified primes'
powers were walked by no class map there and printed as a bound. This
file walks them.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE SETTING. K non-Galois cubic, L its S_3 closure, F its
      quadratic resolvent, H its Hilbert class field, M the Galois
      closure of H over Q, G = Gal(M/Q) = N x| S_3 with N the sum-zero
      subgroup of Cl^3 (the parent's (1)). M/L is unramified, so the
      inertia group I of a prime of M over a ramified q injects into
      S_3, and the Frobenius at q is a COSET sigma.I. The explicit
      formula weights q^k on a conjugacy-stable X by
          (1/k) . |sigma^k I ∩ X| / |I|,   every k >= 1,
      the ramified prime itself included, which the raw count never
      holds. The lift u is the Frobenius in M/L of a prime Q_L of L
      over q; its i-th coordinate is the Artin symbol of N_{L/K_i} Q_L.

  (2) THE FOUR CELLS.
      P^2 Q, I = C_2, f_L = 1: L has three primes over q, each lying
          over P in two of the conjugate fields and over Q in the third
          (six incidences over P, three over Q), so u = ([P],[P],[Q])
          with 2[P] + [Q] = 0. sigma = u, the coset is {k.u, k.u tau},
          and the weight is (1/2)[k.u in X].
      P^3, F split, I = C_3, f_L = 1: two primes of L over q, each with
          f = 1, so u = ([P],[P],[P]) with 3[P] = 0; the coset u^k I
          meets N in u^k alone; weight (1/3)[k.u in X].
      P^3, F inert, I = C_3, f_L = 2: one prime Q_L of L, f(Q_L|P) = 2,
          so Frob_{M/L}(Q_L) = (2[P],2[P],2[P]). A Frobenius sigma of
          M/Q maps to a transposition, and sigma^2 is that element
          EXACTLY (sigma^2 lies in Gal(M/L) ∩ D, which meets I
          trivially). Odd k: sigma^k I is three transposition-elements,
          none in N, weight 0 on N, {e} and D. Even k: sigma^k =
          (k[P],k[P],k[P]) and the coset meets N in it alone; weight
          (1/3)[k.u in X] with u = ([P],[P],[P]). The split cell gated
          by [k even].
      q = 3 with I = S_3 (3 | d_F and 3 = P^3): f_L = 1, u =
          ([P],[P],[P]), and u^k I meets N in u^k alone: (1/6)[k.u in X].
      THE LAW: weight(q^k on X) = (1/k)(1/|I|)[f_L | k][k.u in X].
      Its S_3 SHADOW (X = N, no class map) is (1/k)(1/|I|)[f_L | k],
      Chebotarev for L/Q at a ramified prime. Checked against zeta_K's
      local factors: P^2 Q carries two degree-1 places, so Tr(sigma^k
      on V^I) = 1 = (chi(e) + chi(t))/2; P^3 carries one, Tr = 0 =
      (2 - 1 - 1)/3 in both resolvent cells and (2 - 1 - 1)/6 at S_3.

  (3) THE RESOLVENT TYPE of a tame P^3 (q != 3): L/F is a cyclic cubic
      in which the F-prime over q is totally and tamely ramified, so
      N(q_F) = q^f == 1 mod 3; q == 2 mod 3 FORCES f = 2 (inert), q == 1
      mod 3 allows both. The engine reads it from the Kronecker symbol
      (d_F / q) and asserts the forced direction only. 2 = P^3 occurs
      (Q(cbrt 2), d = -108) and is always the inert cell. At q = 3 with
      3 = P^3, 3 | d_F means I = S_3 and 3 ∤ d_F means I = C_3 with the
      resolvent read by (d_F / 3).

  (4) WHAT THE TERM DOES TO THE LEVEL, priced by hand. The level is
      (n3 + c3 + R_e) / ((ns + cN + R_N) . share), R the ramified
      weights. At h = 2, 3[P] = 0 forces [P] = 0 at every P^3, whose
      weight then lands on {e} whenever it lands on N (net +1/3 - 1/12
      per k = 1 split-resolvent prime), and at P^2 Q, [Q] = -2[P] = 0
      with [P] free, net (1/2)[[P] = 0] - 1/8 per k = 1 prime. So h = 2
      moves UP unless the P^2 Q place is principal in under a quarter
      of the pairs, and up regardless through the P^3 primes. At h = 3
      M, [Q] = [P] and u lies in D always; the deficit is 113 on 928;
      the P^2 Q pairs give (rho/2 - 1/18) each at k = 1 and a ramified
      2 (178 of 283 fields) 1.26 at [P] = 0 and 0.09 at [P] != 0, rho
      the principal share of the P^2 Q place: within 2 sigma of 1 needs
      rho above roughly 0.15 to 0.2.

  (5) THE STATISTIC'S ALGEBRA is the parent's (5): the corrected count
      over the corrected total times the share, sigma Poisson on the
      expectation. The ramified weights on N are at most half the
      parent's bound (|I| >= 2), so the denominator moves by under 8 %
      of the count at h = 2 and the level's sigma by under 4 %.

  (6) WHAT IS NOT CONTROLLED. (a) A ramified place the map does not
      place stays in the bound and is printed. (b) The oscillatory
      remainder and the window below the discriminant, the parent's
      (6b)-(6c), unchanged. (c) The class of Q at P^2 Q is read by the
      map AND by the relation [Q] = -2[P]; a disagreement is a bug in
      the map and stops the run (C3).

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_triple_cube_term.py: the population, the class
    reading, the per-field reader, the unramified walk, the regime
    sorting and the bins are IMPORTED, not re-implemented; C1 must
    reprint its F1 levels before any ramified weight is read.
 T2 FROM explore_ceiling_squares.py: the degree-2 convention, every
    k >= 1 for a ramified prime at 1/|I| on the lifted class, is the
    shadow of (2) and was re-derived above, not copied.
 T3 The generator places over primes <= 29 already hold the ramified
    places of norm <= 30 (explore_cubic_field_shop.py
    relation_generators), so those classes are unit vectors against
    the lattice; larger ramified places go through the parents' map,
    which is generic in the place and was never run on one.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE FRONT'S KILL-SHAPE, printed: on the wide population the
      h = 2 and h = 3 M corrected all-principal levels with the
      ramified terms in. Both within 2 sigma of 1 closes the front;
      either beyond 2 sigma rewrites it with these powers ruled out.
  P2  THE DIRECTION AT h = 2: the level RISES, by between +0.01 and
      +0.06, and stays beyond 2 sigma above 1.
  P3  THE DIRECTION AT h = 3 M: the level RISES toward 1; it lands
      within 2 sigma of 1 iff the printed principal share of the P^2 Q
      place at h = 3 M exceeds about 0.15.
  P4  THE h >= 4 STRATA, all above 1 without the term, do not fall.
  P5  THE RESOLVENT RULE: no tame P^3 prime q == 2 mod 3 has (d_F/q) =
      +1, at every field of the population (a property, asserted).

THE CONTROLS, run before any prediction is read.

  C1  REPRODUCTION. The unramified walk reprints the parent's F1: on
      the wide population 1.058 at h = 2 and 0.877 at h = 3 M, on the
      parents' box 1.030 and 0.909, to three decimals; the sum of the
      ramified 1/k weights this file walks (placed or not) equals the
      parent's unallocated bound per stratum.
  C2  THE S_3 SHADOW, the positive control: over EVERY field of the
      population (h = 1 included), per field, the totally split count
      among the odd primes below a cut, unramified powers in, minus a
      sixth of the whole group's count, regressed on the law's own
      ramified contribution rN - rG/6 read off the splitting types
      alone (no class map). The law says the slope is -1; no ramified
      term says 0. PRINTED at cuts 100, 250, 500 and 1000, slope and
      intercept, and asserted nowhere: the first draft asserted the
      pooled share within 2 sigma of 1/6 with the term in, on a
      binomial bar and with the parent's N-only denominator, and
      failed at z = +5.65 on the base run (the field-spread bar and the
      whole-group denominator read +3.43); the second asserted the
      slope within 2 sigma of -1, passed on the parents' box and
      failed on the wide population at cut 100 (-0.83 +- 0.04). The
      comparison of N against the whole group carries the family's own
      bias (F3), so the shadow reads and does not control; the term's
      normalisation is fixed by zeta_K's local factors, (2).
  C3  THE LIFT RELATION: at every mapped P^2 Q prime the map's class
      of Q equals -2[P] modulo the lattice; at every mapped P^3 prime
      3[P] = 0.
  C4  THE TYPE FROM THE DISCRIMINANT: for odd q | d the factorization's
      type agrees with v_q(d): odd valuation is P^2 Q, valuation 2 at
      q != 3 is P^3; at q = 3, valuation 1 is P^2 Q and 3, 4, 5 are P^3.

THE DESIGN. The parent's population (base, or `--wide`) and its
per-field reader; for each field with h > 1 the parent's unramified
walk (C1), then one ramified walk: every q | d factored by
maximal_places, the type read off the ramification indices, the
degree-1 places' classes read as generator columns or through the
map, the resolvent from the Kronecker symbol, and the weights of (2)
landed per bin on N, {e} and D. Levels printed three ways per
stratum: unramified only, ramified in, and by bin; by box on the wide
run; the h = 3 M all-equal event and the degenerate regime beside.
The ramified census per stratum: pairs by type, the principal shares
of P and of Q, the unplaced. Estimate: the parent's wall plus the
map on two or three ramified places per field -- about 4 minutes
base, 14 minutes wide; the wide run is the one whose residuals are
the question, so it is necessary, and the base run rehearses every
stage first.

FINDINGS. Two populations as the parent's: the parents' box (|d| <=
6000, 1103 fields, 94 + 45 + 18 + 18 at h = 2, 3 M, 4, 5) and the
wide one (|d| <= 24000, 4865 fields, 1367 with h > 1); the wide
figures are the claim's. C1 reprinted the parent's F1 to the third
decimal on both, the walked ramified weights equalling the parent's
bound in every stratum; C3 held at every ramified prime mapped (479
base, 3004 wide, no map disagreement); C4 agreed at every odd
ramified prime (376, 2446); P5 held at every tame P^3 prime (92, 472).
No ramified place went unplaced.

  F1. THE TERM LANDS AS DERIVED, AND THE CLASSES IT LANDS ON ARE THE
      SEAT'S SHAPE (the weights a property; the census an observation; C3-C4,
      P5 pass). The ramified pairs (field, q) by type on the wide
      population, with the principal share of the P^2 Q place P:

          h = 2     863 P^2Q, P principal 0.474, Q principal 1.000;
                    87 P^3 inert, 24 S_3, every P principal
          h = 3 D   191 P^2Q, 0.194;  130 P^3 split (44 principal),
                    28 inert, 7 S_3
          h = 3 M   491 P^2Q, 0.208;  0 P^3 split, 192 inert (50), 57 S_3
          h = 4     219 P^2Q, 0.142 (Q 0.269); 13 inert, 4 S_3, all principal
          h = 5     207 P^2Q, 0.068;  6 inert, 4 S_3, all principal
          h = 6 M    87 P^2Q, 0.126;  32 inert, 6 S_3
          h = 7      99 P^2Q, 0.051;  h = 8 49, 0.143;  h = 9 M 63, 0.048

      What the algebra forces prints as forced: [Q] = -2[P] is principal
      at every P^2 Q pair of h = 2 and every P^3 place is principal at
      every h prime to 3. What it leaves free sits below uniform:
      0.474 against 1/2 at h = 2, then 0.21, 0.14, 0.07, 0.05 against
      1/3, 1/4, 1/5, 1/7. The regime census is the conductor criterion
      seen through inertia: every P^3 prime split in the resolvent sits
      in a degenerate field (130 over the 130 fields of h = 3 D, none
      over the 283 of h = 3 M), and 2 is P^3 in 145 of the 283 full-image
      fields at h = 3 against 22 of 130 degenerate and 66 of 484 at h = 2.

  F2. THE TERM OVER-CORRECTS AT EVERY READABLE CLASS NUMBER PRIME TO 3
      AND CLOSES h = 3 (observation; P1 KILLED as frozen: the front
      rewrites; P2, P3, P4 SURVIVE). Wide, the all-principal level
      without and with the ramified term:

          h = 2     1.058 (z +3.46) -> 1.099 (z +5.99)  +281.7 e, +496.1 N
          h = 3 D   0.968 (z -1.10) -> 0.971 (z -1.03)
          h = 3 M   0.877 (z -3.74) -> 0.943 (z -1.77)  +101.4 e, +382.4 N
          h = 4     1.061 (z +0.85) -> 1.143 (z +2.03)
          h = 5     1.068 (z +0.70) -> 1.129 (z +1.38)
          h = 6 M   1.117 (z +0.74) -> 1.282 (z +1.82)
          h = 7     1.114 (z +0.52) -> 1.205 (z +0.97)
          h = 8     1.294 (z +0.94) -> 1.347 (z +1.13)
          h = 9 M   1.200 (z +0.64) -> 1.425 (z +1.40)

      h = 2 rises by +0.041 (P2's band +0.01 to +0.06) and stays beyond
      2 sigma; h = 3 M rises by +0.066 to within 2 sigma at a principal
      share of 0.208 (P3's threshold 0.15); no h >= 4 stratum falls
      (P4); the strata too thin to read, h = 10, 11, 13 and 17, fall
      and stay above 1, and h = 16 reads 0 on one field. At h = 2 the
      ramified weights land on the identity at 0.57
      of their weight on N against a share of 1/4, because 3[P] = 0
      puts the P^3 places and [Q] = -2[P] the Q places there; by bin the
      excess is now [3, 30) at 1.250 (z +4.6, where the small ramified
      primes' powers land) and [300, 1000) at 1.126 (z +5.9, where the
      raw count already stands near the model); by box 1.065 (z +1.7) in the
      parents' box and 1.107 (z +5.8) in the increment. The h = 3 M
      all-equal event reads 0.934 (z -3.5) -> 1.025 (z +1.3), its
      non-principal equal triples 1.066 (z +2.9). The parents' box alone
      reads both strata within 2 sigma with the term in (1.065, 0.922).

  F3. THE RESIDUAL IS THE FAMILY'S: THE RAW SPLIT SHARE MOVES WITH THE
      DISCRIMINANT BOX, WHICH NO PER-FIELD TERM DOES (observation, no
      class map; S6 over 4865 fields). The share of fields in a box
      where a fixed unramified prime is totally split, against 1/6:

        p = 3    0.080 +- 0.014  0.088 +- 0.014  0.119 +- 0.011  0.120 +- 0.008
        p = 5    0.086 +- 0.014  0.106 +- 0.014  0.103 +- 0.010  0.129 +- 0.007
        p = 7    0.082 +- 0.013  0.120 +- 0.014  0.119 +- 0.010  0.113 +- 0.007
        p = 13   0.089 +- 0.013  0.114 +- 0.014  0.124 +- 0.010  0.136 +- 0.007
        p = 997  0.173 +- 0.017  0.169 +- 0.016  0.149 +- 0.010  0.148 +- 0.007
                  |d| <= 3000     3000-6000       6000-12000      12000-24000

      and the band [300, 1000) pooled per box reads 0.1635 +- 0.0016,
      0.1559 +- 0.0015, 0.1530 +- 0.0010, 0.1541 +- 0.0007: at 1/6 only
      where the window is above the discriminant. The small primes
      climb toward 1/6 as the box widens and the large ones descend
      from it, the crossing somewhere in the hundreds. A per-field
      explicit formula says nothing about a share at a fixed prime
      across fields and a box-independent thing about a band; the count
      of cubic fields by discriminant has a secondary term whose local
      densities per splitting type are the natural suspect, unread
      here. The S_3 shadow (C2) reads the same: on the parents' box the
      slope of the per-field residual on the law's own contribution is
      -1.03 +- 0.09, -1.14 +- 0.13, -0.92 +- 0.16, -1.06 +- 0.23 at cuts
      100, 250, 500, 1000, the law's -1 at every cut, with an intercept
      of -0.01, -0.03, -0.22, +0.47 per field; on the wide population
      the slope reads -0.83 +- 0.04, -1.24 +- 0.06, -1.28 +- 0.08,
      -1.32 +- 0.10 and the intercept +0.28, +0.48, +0.42, +0.67, so the
      N-against-G share sits over 1/6 at every cut with the term in
      (z +18, +12, +6, +8 on the field-to-field bar). The shadow is not
      a control of the term's normalisation: its comparison carries the
      family's bias, which the level's comparison of the identity
      against N need not, and the term's own normalisation is fixed by
      zeta_K's local factors (2).

RUN RECORD. 2026-09-06, Windows 11, Python 3, `python
prime/code/memwatch.py python prime/code/explore_triple_ramified_term.py`
and the same with `--wide`. One process, CPython, no BLAS. Base: 255
checks, 216.8 s wall, peak working set 77.7 MB against memwatch's 512
MB ceiling; the class reading 157.5 s of it, the shadow 16 s, the two
walks 25 s. Wide: 1428 checks, 1182.7 s wall, peak working set 126.6
MB; enumeration 52 s, class reading 903.6 s (3 fields excluded, the
sibling's own T4 policy), the shadow 72 s, the walks 107 s. The first
base run stopped at the first draft of C2 (the docstring's C2 records
it) and the first wide run at its second draft's slope assertion; the
wide population's records were then cached once in a scratch driver
while the sections were completed, and the record runs reprinted every
figure above to the last digit.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_class_map as CCM
import explore_cubic_field_shop as CFS
import explore_cubic_principal as ECP
import explore_cubic_split_triple as ST
import explore_cubic_zero_tilt as ZT
import explore_triple_cube_term as CT

CHECKS = 0
PRIME_CAP = ECP.PRIME_CAP
ODD_PRIMES = ECP.ODD_PRIMES
BIN_EDGES = ECP.BIN_EDGES
MIN_SPLIT = ST.MIN_SPLIT
HIGH_FRAC = ST.HIGH_FRAC
MIN_READ = CT.MIN_READ
TYPES = ('p2q', 'p3s', 'p3i', 'p3w')     # P^2 Q, P^3 split, inert, S_3
F1_WIDE = {(2, 'A'): 1.058, (3, 'M'): 0.877}   # the parent's F1, C1
F1_BASE = {(2, 'A'): 1.030, (3, 'M'): 0.909}


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ------------------------------------------------------ the discriminant
def prime_factors(n):
    n = abs(n)
    out = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        out.append(n)
    return out


def fundamental(d):
    """d_F: the discriminant of Q(sqrt d)."""
    s = 1 if d > 0 else -1
    n = abs(d)
    core = 1
    q = 2
    while q * q <= n:
        while n % (q * q) == 0:
            n //= q * q
        if n % q == 0:
            core *= q
            n //= q
        q += 1
    core *= n
    core *= s
    return core if core % 4 == 1 else 4 * core


def kronecker(D, q):
    """(D / q) for q prime, D the discriminant of a quadratic field."""
    if q == 2:
        if D % 2 == 0:
            return 0
        return 1 if D % 8 in (1, 7) else -1
    r = D % q
    if r == 0:
        return 0
    return 1 if pow(r, (q - 1) // 2, q) == 1 else -1


# -------------------------------------------------------- the ramified walk
def new_rcell():
    return dict(cN=0.0, c3=0.0, cE=0.0, walked=0.0, unplaced=0.0,
                src=dict((t, 0.0) for t in TYPES))


def merge_r(into, cell):
    for key in ('cN', 'c3', 'cE', 'walked', 'unplaced'):
        into[key] += cell[key]
    for t in TYPES:
        into['src'][t] += cell['src'][t]


def new_census():
    c = dict(n=0, pp=0, qp=0, unplaced=0, two=0)
    return dict((t, dict(c)) for t in TYPES)


def place_class(O, P, q, rec, gp, piv, k, rows, gbp, prime_set):
    """The class vector of a degree-1 place P over q: a generator column
    where the place is one, else the map's first vector; None where the
    map placed nothing. Every extra vector the map returns is checked
    against the first modulo the lattice (the parents' C4)."""
    for col, (p, e, f, name, Q) in enumerate(gp):
        if p == q and [tuple(r) for r in Q] == [tuple(r) for r in P]:
            v = [0] * k
            v[col] = 1
            return v, 0
    (d, cx, a, b, c, _O, h, kind, _gp, rel) = rec
    got, _saw = CCM.map_place(O, P, q, rows, cx, gp, gbp, prime_set, k)
    if not got:
        return None, 0
    bad = sum(1 for v in got[1:] if not ST.same_class(got[0], v, piv, k))
    return got[0], bad


def walk_ramified(rec, piv, k, census, checks):
    """One field's ramified primes: per-bin ramified weights on N, {e}
    and D by the law of (2). checks accumulates C3-C5 counters."""
    (d, cx, a, b, c, O, h, kind, gp, rel) = rec
    rows = ECP.t2_rows(O, a, b, c)
    gbp = {}
    for col, (q, e, f, name, Q) in enumerate(gp):
        gbp.setdefault(q, []).append((col, f, Q))
    prime_set = sorted(gbp)
    dF = fundamental(d)
    ok((d // dF) * dF == d and int(round(math.sqrt(d // dF))) ** 2
       == d // dF, "d = %d is not d_F . f^2 with d_F = %d" % (d, dF))
    cells = {}
    for q in prime_factors(d):
        pl = CFS.maximal_places(O, q)
        es = sorted(e for (_P, e, _f) in pl)
        vq = CFS.v_p(abs(d), q)
        if es == [3]:
            typ = 'p3'
        elif es == [1, 2]:
            typ = 'p2q'
        else:
            raise AssertionError("q = %d divides d = %d but %s"
                                 % (q, d, es))
        # C4: the type against the valuation
        if q % 2:
            if q == 3:
                want = 'p2q' if vq == 1 else 'p3' if vq in (3, 4, 5) else '?'
            else:
                want = 'p2q' if vq % 2 else 'p3' if vq == 2 else '?'
            checks['c4_agree' if want == typ else 'c4_disagree'] += 1
        # the places and their classes
        if typ == 'p2q':
            P = [Q for (Q, e, f) in pl if e == 2][0]
            Qp = [Q for (Q, e, f) in pl if e == 1][0]
            vP, badP = place_class(O, P, q, rec, gp, piv, k, rows, gbp,
                                   prime_set)
            vQ, badQ = place_class(O, Qp, q, rec, gp, piv, k, rows, gbp,
                                   prime_set)
            checks['c4map_disagree'] += badP + badQ
            inert_order, fL = 2, 1
        else:
            P = pl[0][0]
            vP, badP = place_class(O, P, q, rec, gp, piv, k, rows, gbp,
                                   prime_set)
            vQ = None
            checks['c4map_disagree'] += badP
            kr = kronecker(dF, q)
            if kr == 0:
                ok(q == 3, "q = %d totally ramified and ramified in F"
                   % q)
                typ, inert_order, fL = 'p3w', 6, 1
            elif kr == 1:
                typ, inert_order, fL = 'p3s', 3, 1
            else:
                typ, inert_order, fL = 'p3i', 3, 2
            if q != 3:
                checks['c5_tame'] += 1
                if q % 3 == 2 and kr == 1:
                    checks['c5_bad'] += 1
        cen = census[typ]
        cen['n'] += 1
        if q == 2:
            cen['two'] += 1
        placed = vP is not None and (typ != 'p2q' or vQ is not None)
        if placed:
            # C3: the lift relation
            if typ == 'p2q':
                s = [2 * x + y for x, y in zip(vP, vQ)]
                checks['c3_ok' if ST.is_principal(s, piv, k)
                       else 'c3_bad'] += 1
                if ST.is_principal(vQ, piv, k):
                    cen['qp'] += 1
            else:
                checks['c3_ok' if ST.is_principal(CT.scale(vP, 3), piv, k)
                       else 'c3_bad'] += 1
            if ST.is_principal(vP, piv, k):
                cen['pp'] += 1
        else:
            cen['unplaced'] += 1
        for (kk, n) in CT.powers(q):
            bi = CT.bin_of(n)
            if bi is None:
                continue
            cell = cells.setdefault(bi, new_rcell())
            w = 1.0 / kk
            cell['walked'] += w
            if not placed:
                cell['unplaced'] += w
                continue
            if kk % fL:
                continue
            w /= inert_order
            cell['cN'] += w
            cell['src'][typ] += w
            kP = CT.scale(vP, kk)
            if typ == 'p2q':
                kQ = CT.scale(vQ, kk)
                in_e = (ST.is_principal(kP, piv, k)
                        and ST.is_principal(kQ, piv, k))
                in_D = ST.same_class(kP, kQ, piv, k)
            else:
                in_e = ST.is_principal(kP, piv, k)
                in_D = True
            if in_e:
                cell['c3'] += w
            if in_D:
                cell['cE'] += w
    return cells


# ------------------------------------------------------------ the reader
def read_population(recs, base_cap=None):
    """The parent's read_population with the ramified walk beside the
    unramified one. Returns (un, ram, nfields, census, base_un,
    base_ram, checks); un/ram are {(h, reg): {bin: cell}}."""
    un, ram, nfields = {}, {}, {}
    census = {}
    base_un = {} if base_cap else None
    base_ram = {} if base_cap else None
    checks = dict(c3_ok=0, c3_bad=0, c4_agree=0, c4_disagree=0,
                  c4map_disagree=0, c5_tame=0, c5_bad=0, bad_sum=0)
    t0 = time.time()
    for rec in recs:
        (d, cx, a, b, c, O, h, kind, gp, rel) = rec
        if h is None or h == 1 or not cx:
            continue
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        if H is None or H == 1:
            continue
        two = CT.place_over_two(rec)
        cells, nb, _small = CT.walk_field(rec, per_prime, piv, k, two)
        checks['bad_sum'] += nb
        ns = sum(x['ns'] for x in cells.values())
        neq = sum(x['neq'] for x in cells.values())
        reg = 'A'
        if H % 3 == 0:
            exact = CT.diagonal_3part(per_prime, piv, k, H)
            if H == 3:
                reg = ('X' if ns < MIN_SPLIT
                       else 'D' if float(neq) / ns >= HIGH_FRAC else 'M')
            else:
                reg = 'X' if ns < MIN_SPLIT else 'D' if exact else 'M'
        key = (H, reg)
        nfields[key] = nfields.get(key, 0) + 1
        rcells = walk_ramified(rec, piv, k,
                               census.setdefault(key, new_census()),
                               checks)
        tables = [(un, ram)]
        if base_un is not None and abs(d) <= base_cap:
            tables.append((base_un, base_ram))
        for (tu, tr) in tables:
            su = tu.setdefault(key, {})
            for bi, cell in cells.items():
                CT.merge(su.setdefault(bi, CT.new_cell()), cell)
            sr = tr.setdefault(key, {})
            for bi, cell in rcells.items():
                merge_r(sr.setdefault(bi, new_rcell()), cell)
    print("  mapped complex population walked in %.1f s, %d strata"
          % (time.time() - t0, len(un)))
    return un, ram, nfields, census, base_un, base_ram, checks


def pooled_r(st, bins=None):
    out = new_rcell()
    for bi, cell in st.items():
        if bins is None or bi in bins:
            merge_r(out, cell)
    return out


def level(count, corr, total, share):
    return CT.level(count, corr, total, share)


# ------------------------------------------------------------ the reads
SHADOW_CUTS = (100, 250, 500, 1000)


def shadow_field(rec, cap):
    """One field's S_3 shadow below cap: (raw split, unramified N-weight
    k >= 2, unramified G-weight k >= 2, primes counted, ramified
    N-weight, ramified G-weight, type census)."""
    (d, cx, a, b, c, O, h, kind, gp, rel) = rec
    pdisc = CFS.poly_disc3(a, b, c)
    dF = fundamental(d)
    raw = tot = cN = cG = rN = rG = 0.0
    kinds = dict(p2q=0, p3s=0, p3i=0, p3w=0)
    for q in ODD_PRIMES:
        if q >= cap:
            break
        if d % q == 0:
            pl = CFS.maximal_places(O, q)
            es = sorted(e for (_P, e, _f) in pl)
            if es == [1, 2]:
                typ, io, fL = 'p2q', 2, 1
            else:
                kr = kronecker(dF, q)
                typ, io, fL = (('p3w', 6, 1) if kr == 0 else
                               ('p3s', 3, 1) if kr == 1 else
                               ('p3i', 3, 2))
            kinds[typ] += 1
            kk, n = 1, q
            while n < cap:
                rG += 1.0 / kk
                if kk % fL == 0:
                    rN += 1.0 / (kk * io)
                kk += 1
                n *= q
            continue
        _pl, kd = ECP.deg1_places(O, a, b, c, pdisc, q)
        tot += 1
        if kd == 'split':
            raw += 1
        kk, n = 2, q * q
        while n < cap:
            cG += 1.0 / kk
            if (kd == 'split' or (kd == 'partial' and kk % 2 == 0)
                    or (kd == 'inert' and kk % 3 == 0)):
                cN += 1.0 / kk
            kk += 1
            n *= q
    return raw, cN, cG, tot, rN, rG, kinds


def regress(xs, ys):
    """(beta, se_beta, alpha, se_alpha) of y = alpha + beta x."""
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    beta = sxy / sxx
    alpha = my - beta * mx
    s2 = sum((y - alpha - beta * x) ** 2 for x, y in zip(xs, ys)) / (n - 2)
    return (beta, math.sqrt(s2 / sxx), alpha,
            math.sqrt(s2 * (1.0 / n + mx * mx / sxx)))


def s_shadow(recs):
    section("C2  THE S_3 SHADOW over every field -- the event N with the "
            "ramified primes at 1/|I| [f_L | k]")
    t0 = time.time()
    share = 1.0 / 6
    print("  per field, residual = (count on N) - (count on G)/6 with the"
          " unramified powers in; x = the law's own ramified contribution"
          " rN - rG/6; the law says residual = alpha - x, so the slope"
          " beta reads -1 and alpha is whatever remainder is NOT the"
          " ramified term")
    print("  %-5s %-7s %-8s %-8s | %-18s %-18s | %s"
          % ("cut", "fields", "split", "on G", "beta (law -1)",
             "alpha per field", "share raw -> un -> in, z field"))
    betas = {}
    for cap in SHADOW_CUTS:
        rows = [shadow_field(rec, cap) for rec in recs]
        nf = len(rows)
        xs = [r[4] - r[5] * share for r in rows]
        ys = [r[0] + r[1] - (r[3] + r[2]) * share for r in rows]
        beta, seb, alpha, sea = regress(xs, ys)
        betas[cap] = (beta, seb)
        reads = []
        for fN, fG in ((lambda r: r[0], lambda r: r[3]),
                       (lambda r: r[0] + r[1], lambda r: r[3] + r[2]),
                       (lambda r: r[0] + r[1] + r[4],
                        lambda r: r[3] + r[2] + r[5])):
            N = sum(fN(r) for r in rows)
            G = sum(fG(r) for r in rows)
            res = [fN(r) - fG(r) * share for r in rows]
            m = sum(res) / nf
            sd = math.sqrt(sum((v - m) ** 2 for v in res) / (nf - 1))
            reads.append((N / G, m / (sd / math.sqrt(nf))))
        print("  %-5d %-7d %-8d %-8.1f | %+.3f +- %.3f     | %+.3f +- %.3f"
              "     | %.4f (%+.1f) -> %.4f (%+.1f) -> %.4f (%+.1f)"
              % (cap, nf, int(sum(r[0] for r in rows)),
                 sum(r[3] + r[2] + r[5] for r in rows), beta, seb, alpha,
                 sea, reads[0][0], reads[0][1], reads[1][0], reads[1][1],
                 reads[2][0], reads[2][1]))
        if cap == PRIME_CAP:
            kinds = dict(p2q=0, p3s=0, p3i=0, p3w=0)
            for r in rows:
                for t in kinds:
                    kinds[t] += r[6][t]
            print("  ramified odd primes below %d by type P^2Q / P^3 split"
                  " / inert / S_3: %d / %d / %d / %d"
                  % (cap, kinds['p2q'], kinds['p3s'], kinds['p3i'],
                     kinds['p3w']))
            ok(reads[0][1] <= -5,
               "raw totally split share not short at 5 sigma")
    print("  (%.1f s)" % (time.time() - t0))
    return betas


def s_reproduce(un, ram, nfields, ref, label):
    section("C1  REPRODUCTION -- the unramified levels against the "
            "parent's F1 (%s), and the bound" % label)
    for key in sorted(un):
        h, reg = key
        c = CT.pooled(un[key])
        r = pooled_r(ram[key]) if key in ram else new_rcell()
        share = CT.share_of(h, reg)
        lv, z, exp = level(c['n3'], c['c3'], c['ns'] + c['cN'], share)
        want = ref.get(key)
        print("  h = %d %s  %3d fields  unramified level %s  z %s  "
              "bound %.1f  walked %.1f  unplaced %.1f%s"
              % (h, reg, nfields[key],
                 "%.3f" % lv if lv is not None else "--",
                 "%+.2f" % z if z is not None else "--",
                 c['unalloc'], r['walked'], r['unplaced'],
                 "   F1 %.3f" % want if want else ""))
        if want is not None:
            ok(abs(lv - want) < 0.0005 + 1e-9,
               "h = %d %s unramified level %.3f, F1 %.3f"
               % (h, reg, lv, want))
        ok(abs(c['unalloc'] - r['walked']) < 1e-6,
           "h = %d %s bound %.3f, walked %.3f"
           % (h, reg, c['unalloc'], r['walked']))


def s_census(census, nfields):
    section("S2  THE RAMIFIED CENSUS by stratum -- pairs (field, q) by "
            "type; principal shares of P and Q")
    print("  %-9s %-6s | %-28s %-16s %-16s %-16s"
          % ("stratum", "fields", "P^2Q  n / P princ / Q princ",
             "P^3 split n/pp", "P^3 inert n/pp", "S_3 n/pp"))
    rho = {}
    for key in sorted(census):
        h, reg = key
        cn = census[key]
        a = cn['p2q']
        rho[key] = a['pp'] / float(a['n'] - a['unplaced'] or 1)
        print("  h = %d %-3s %-6d | %4d  %4d (%.3f)  %4d (%.3f)"
              "  %-16s %-16s %-16s   unplaced %d, at 2: %d/%d/%d/%d"
              % (h, reg, nfields[key], a['n'], a['pp'], rho[key],
                 a['qp'], a['qp'] / float(a['n'] - a['unplaced'] or 1),
                 "%d / %d" % (cn['p3s']['n'], cn['p3s']['pp']),
                 "%d / %d" % (cn['p3i']['n'], cn['p3i']['pp']),
                 "%d / %d" % (cn['p3w']['n'], cn['p3w']['pp']),
                 sum(cn[t]['unplaced'] for t in TYPES),
                 a['two'], cn['p3s']['two'], cn['p3i']['two'],
                 cn['p3w']['two']))
    return rho


def s_levels(un, ram, nfields, base_un=None, base_ram=None):
    section("S3  THE ALL-PRINCIPAL EVENT with the ramified term -- P1-P4")
    print("  level = (count + unramified + ramified) / (corrected total "
          "x share); sigma Poisson on the expectation")
    out = {}
    for key in sorted(un):
        h, reg = key
        c = CT.pooled(un[key])
        r = pooled_r(ram[key]) if key in ram else new_rcell()
        share = CT.share_of(h, reg)
        lu, zu, eu = level(c['n3'], c['c3'], c['ns'] + c['cN'], share)
        lr, zr, er = level(c['n3'], c['c3'] + r['c3'],
                           c['ns'] + c['cN'] + r['cN'], share)
        tag = "  readable" if er >= MIN_READ and reg != 'D' else ""
        out[key] = (lu, zu, lr, zr, er)
        print("  h = %d %s  %3d fields  all-p %4d  | unramified level %s "
              "z %s  | ramified +%.1f on e, +%.1f on N (%s)  -> exp %.1f "
              "level %s  z %s%s"
              % (h, reg, nfields[key], c['n3'],
                 "%.3f" % lu if lu is not None else "--",
                 "%+.2f" % zu if zu is not None else "--",
                 r['c3'], r['cN'],
                 ", ".join("%s %.1f" % (t, r['src'][t]) for t in TYPES),
                 er,
                 "%.3f" % lr if lr is not None else "--",
                 "%+.2f" % zr if zr is not None else "--", tag))
        if base_un is not None:
            cb = CT.pooled(base_un[key]) if key in base_un else CT.new_cell()
            rb = pooled_r(base_ram[key]) if key in base_ram else new_rcell()
            ci = CT.diff_cell(c, cb)
            ri = new_rcell()
            for kk in ('cN', 'c3', 'cE', 'walked', 'unplaced'):
                ri[kk] = r[kk] - rb[kk]
            for name, cc, rr in (("parents' box", cb, rb),
                                 ("increment", ci, ri)):
                l1, z1, e1 = level(cc['n3'], cc['c3'],
                                   cc['ns'] + cc['cN'], share)
                l2, z2, e2 = level(cc['n3'], cc['c3'] + rr['c3'],
                                   cc['ns'] + cc['cN'] + rr['cN'], share)
                print("     %-13s all-p %4d  unramified %s z %s  | "
                      "ramified +%.1f/+%.1f  level %s  z %s"
                      % (name, cc['n3'],
                         "%.3f" % l1 if l1 is not None else "--",
                         "%+.2f" % z1 if z1 is not None else "--",
                         rr['c3'], rr['cN'],
                         "%.3f" % l2 if l2 is not None else "--",
                         "%+.2f" % z2 if z2 is not None else "--"))
        print("     by bin (q^k in bin): unramified level | ramified in")
        for bi in range(len(BIN_EDGES) - 1):
            if bi not in un[key]:
                continue
            cb = un[key][bi]
            rb = ram[key].get(bi, new_rcell()) if key in ram else new_rcell()
            l1, z1, _ = level(cb['n3'], cb['c3'], cb['ns'] + cb['cN'],
                              share)
            l2, z2, _ = level(cb['n3'], cb['c3'] + rb['c3'],
                              cb['ns'] + cb['cN'] + rb['cN'], share)
            print("       [%4d,%5d)  all-p %4d  %s z %s  | +%.2f/+%.2f  "
                  "%s z %s"
                  % (BIN_EDGES[bi], BIN_EDGES[bi + 1], cb['n3'],
                     "%.3f" % l1 if l1 is not None else "--",
                     "%+.2f" % z1 if z1 is not None else "--",
                     rb['c3'], rb['cN'],
                     "%.3f" % l2 if l2 is not None else "--",
                     "%+.2f" % z2 if z2 is not None else "--"))
    return out


def s_equal(un, ram, nfields):
    section("S4  THE ALL-EQUAL EVENT at h = 3 M, ramified in")
    key = (3, 'M')
    if key not in un:
        print("  no h = 3 M stratum")
        return
    c = CT.pooled(un[key])
    r = pooled_r(ram[key]) if key in ram else new_rcell()
    share = 1.0 / 3
    l1, z1, _ = level(c['neq'], c['cE'], c['ns'] + c['cN'], share)
    l2, z2, e2 = level(c['neq'], c['cE'] + r['cE'],
                       c['ns'] + c['cN'] + r['cN'], share)
    print("  equal %d of %d  unramified level %.3f z %+.2f  | ramified "
          "+%.1f on D, +%.1f on N  -> exp %.1f  level %.3f  z %+.2f"
          % (c['neq'], c['ns'], l1, z1, r['cE'], r['cN'], e2, l2, z2))
    l3, z3, e3 = level(c['neq'] - c['n3'], c['cE'] - c['c3']
                       + r['cE'] - r['c3'], c['ns'] + c['cN'] + r['cN'],
                       2.0 / 9)
    print("  the non-principal equal triples, model 2/9: level %.3f  "
          "z %+.2f" % (l3, z3))


FAMILY_PRIMES = (3, 5, 7, 11, 13, 31, 101, 307, 997)
FAMILY_BOXES = ((0, 3000), (3000, 6000), (6000, 12000), (12000, 24000))


def s_family(recs):
    """The raw split share with NO class map, read as a FAMILY quantity:
    at a fixed prime across the fields of a discriminant box, and pooled
    over a band of primes per box. A per-field explicit formula predicts
    nothing about the first and a box-independent deficit for the
    second; a term in the count of cubic fields by discriminant moves
    with the box."""
    section("S6  THE FAMILY READ -- the raw split share by discriminant "
            "box, no class map")
    boxes = [(lo, hi) for (lo, hi) in FAMILY_BOXES
             if any(lo < abs(r[0]) <= hi for r in recs)]
    print("  the share of fields in the box, p unramified, where p is "
          "totally split (Chebotarev's share 1/6):")
    print("  %-5s" % "p" + "".join("  %-21s" % ("(%d, %d]" % b)
                                    for b in boxes))
    for p in FAMILY_PRIMES:
        line = "  %-5d" % p
        for (lo, hi) in boxes:
            n = s = 0
            for (d, cx, a, b, c, O, h, kind, gp, rel) in recs:
                if not (lo < abs(d) <= hi) or d % p == 0:
                    continue
                _pl, kd = ECP.deg1_places(O, a, b, c,
                                          CFS.poly_disc3(a, b, c), p)
                n += 1
                s += (kd == 'split')
            sh = s / float(n)
            line += "  %.4f +- %.4f n%4d" % (sh, math.sqrt(sh * (1 - sh)
                                                            / n), n)
        print(line)
    print("  the raw split share among the odd unramified primes of a "
          "band, per box:")
    for (lo, hi) in boxes:
        sub = [r for r in recs if lo < abs(r[0]) <= hi]
        line = "  (%5d, %5d] %4d fields" % (lo, hi, len(sub))
        for bi in range(len(BIN_EDGES) - 1):
            n = s = 0
            for (d, cx, a, b, c, O, h, kind, gp, rel) in sub:
                pdisc = CFS.poly_disc3(a, b, c)
                for q in ODD_PRIMES:
                    if (q < BIN_EDGES[bi] or q >= BIN_EDGES[bi + 1]
                            or d % q == 0):
                        continue
                    _pl, kd = ECP.deg1_places(O, a, b, c, pdisc, q)
                    n += 1
                    s += (kd == 'split')
            sh = s / float(n)
            line += "  [%d, %d) %.4f +- %.4f" % (
                BIN_EDGES[bi], BIN_EDGES[bi + 1], sh,
                math.sqrt(sh * (1 - sh) / n))
        print(line)


def s_verdict(out, rho):
    section("S5  THE SLATE READ")
    for key, lab in (((2, 'A'), "P2 h = 2"), ((3, 'M'), "P3 h = 3 M")):
        if key not in out:
            continue
        lu, zu, lr, zr, er = out[key]
        print("  [%s] level %.3f -> %.3f (%+.3f), z %+.2f -> %+.2f: %s"
              % (lab, lu, lr, lr - lu, zu, zr,
                 "RISES" if lr > lu else "FALLS"))
        if key == (3, 'M'):
            print("       principal share of the P^2 Q place %.3f"
                  % rho.get(key, float('nan')))
    both = all(key in out and abs(out[key][3]) <= 2
               for key in ((2, 'A'), (3, 'M')))
    print("  [P1] h = 2 and h = 3 M both within 2 sigma with the "
          "ramified term in: %s" % ("YES -- the front closes"
                                    if both else
                                    "NO -- the front rewrites"))
    hi = [(k, v) for k, v in out.items() if k[0] >= 4 and k[1] != 'D'
          and v[4] >= MIN_READ]
    falls = [k for k, v in hi if v[2] < v[0]]
    print("  [P4] h >= 4 readable strata: %d, of which %d fall: %s"
          % (len(hi), len(falls), ", ".join("h = %d %s" % k
                                            for k in falls) or "none"))


def main():
    t0 = time.time()
    wide = "--wide" in sys.argv[1:]
    if wide:
        import explore_ceiling_topband as TB
        section("S1  THE WIDE POPULATION -- explore_ceiling_topband.py's "
                "reading to |d| <= %d" % TB.WIDE_CAP)
        recs = TB.wide_class_reading()
    else:
        recs = ZT.s1_population()
    run(recs, wide, t0)


def run(recs, wide, t0=None):
    t0 = time.time() if t0 is None else t0
    s_shadow(recs)
    section("THE READER -- the unramified walk and the ramified walk")
    (un, ram, nfields, census, base_un, base_ram,
     checks) = read_population(recs, ECP.DISC_CAP if wide else None)
    print("  [C3] lift relations: %d hold, %d fail; map vectors "
          "disagreeing at a ramified place: %d"
          % (checks['c3_ok'], checks['c3_bad'], checks['c4map_disagree']))
    ok(checks['c3_bad'] == 0, "%d lift relations fail" % checks['c3_bad'])
    ok(checks['c4map_disagree'] == 0,
       "%d map disagreements" % checks['c4map_disagree'])
    print("  [C4] type against v_q(d) at odd q: %d agree, %d disagree"
          % (checks['c4_agree'], checks['c4_disagree']))
    ok(checks['c4_disagree'] == 0, "type disagrees with the valuation")
    print("  [P5] tame P^3 primes %d, with q == 2 mod 3 and F split: %d"
          % (checks['c5_tame'], checks['c5_bad']))
    ok(checks['c5_bad'] == 0, "a tame P^3 prime == 2 mod 3 splits in F")
    ok(checks['bad_sum'] == 0, "%d power triples off zero-sum"
       % checks['bad_sum'])
    if wide:
        s_reproduce(base_un, base_ram, nfields, F1_BASE,
                    "parents' box inside the wide population")
        s_reproduce(un, ram, nfields, F1_WIDE, "wide")
    else:
        s_reproduce(un, ram, nfields, F1_BASE, "base")
    rho = s_census(census, nfields)
    out = s_levels(un, ram, nfields, base_un, base_ram)
    s_equal(un, ram, nfields)
    s_family(recs)
    s_verdict(out, rho)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall%s"
          % (CHECKS, time.time() - t0, "  (--wide)" if wide else ""))


if __name__ == "__main__":
    main()
