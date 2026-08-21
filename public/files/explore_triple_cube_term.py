r"""THE CUBE TERM -- is the all-equal triple's shortfall, the one that
DEEPENS with the class number, the prime-power term of the explicit
formula read at the TRIPLE EVENT rather than at the place? (sibling of
explore_ceiling_squares.py, which put the term back per PLACE class and
flattened the generator ceiling; of explore_cubic_split_triple.py, whose
F3 measured the deepening and left it open; and of
explore_cubic_zero_tilt.py, whose F2 isolated it as a residual no
per-place share reaches -- 0.663, 0.463, 0.351 on the all-principal
count at h = 3, 4, 5 -- and named it "the coincidence mechanism".)

THE QUESTION. Over the complex cubic fields to |d| <= 6000 and the odd
primes below 1000, the count of totally split primes whose three places
are all principal is short of the uniform model's 1/h^2 share, and the
shortfall GROWS with h: 0.86 of the model at h = 2, 0.66 at 3, 0.46 at 4,
0.35 at 5. The corpus has already read the principal SHARE's shortfall
as the explicit formula's prime-power term, per place. This file asks
whether the TRIPLE event's shortfall, deepening and all, is the same term
read at the identity element of a larger group -- and whether the
deepening is the inert primes' cube.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE GROUP. K a non-Galois cubic field, L its S_3 closure, H its
      Hilbert class field, M the Galois closure of H over Q. Gal(M/L)
      embeds in Cl(K)^3 by the Artin symbols of the three conjugate
      Hilbert class fields, and the image lies in the sum-zero subgroup
          N = {(a, b, c) in Cl^3 : a + b + c = 0}, |N| = h^2,
      because a totally split rational prime's three places multiply
      to (p). Write G = Gal(M/Q), |G| = 6 |Gal(M/L)|, and assume the
      image is all of N (the uniform model's hypothesis). At prime h
      it is: N is an irreducible S_3-module away from 3, so the image
      is N or trivial, and trivial means h = 1. At h = 3 the image is
      N or the diagonal {(c, c, c)} -- the degenerate fields, which
      the parents' regime read sets apart. At composite h proper
      S_3-stable subgroups exist (at h = 4 the squares' sum-zero
      triples, of order 4) and nothing here checks them; the measured
      corrections need no such assumption, the model share 1/h^2 does.
      Elements of G are (v, s) with v in N and s in S_3, and
      the Frobenius of a totally split prime is (v, e) with v its
      triple of place classes; of a partial prime, (v, t) with t a
      transposition; of an inert prime, (v, r) with r a 3-cycle.

  (2) THE EVENTS ARE CONJUGACY-STABLE SUBSETS OF G. All-principal is
      the identity {e}. All-equal is D = {(c, c, c) : 3c = 0}, of size
      t = |Cl[3]|. Totally split is N itself. Each is a union of
      conjugacy classes, so Chebotarev and its explicit formula apply
      to each: the count of primes with Frobenius in X is short of
      (|X|/|G|) Li(x) by 1/k per prime q with q^k <= x and
      Frob_q^k in X, for every k >= 2.

  (3) THE POWERS, BY SPLITTING TYPE, which is where the deepening
      comes from.
        split q, (v, e)^k = (k.v, e):
            in {e} iff k.b_i = 0 for all three places,
            in D   iff the three k.b_i share one class,
            in N   always.
        partial q, (v, t)^k: odd k lands outside N; even k lands on
            (k/2).(v + t.v) = (k/2).(2a, -a, -a) with a the class of
            the degree-1 place (explore_ceiling_squares.py (4)), so
            in {e} iff (k/2).a = 0,
            in D   iff (3k/2).a = 0,
            in N   for every even k.
        inert q, (v, r)^k: k not a multiple of 3 lands outside N;
            (v, r)^3 = (v + r.v + r^2.v, e) = (s, s, s) with s the SUM
            of v's coordinates, which is 0 because v lies in N. So
            every inert prime's cube is the IDENTITY -- in {e}, in D
            and in N, at every multiple of 3 -- and that is the norm
            relation a + b + c = 0 doing the work.
      Every inert prime below x^(1/3) therefore lands 1/3 on the
      all-principal event, whose main-term share is 1/(6h^2), while a
      split or partial prime's square lands there only when its
      classes are 2-torsion or trivial.

  (4) THE GROUP COUNTS, closed form under (1) with Cl cyclic:
        #{g : g^k = e}  = |Cl[k]|^2 + [k even] 3h |Cl[k/2]|
                          + [3 | k] 2h^2
        #{g : g^k in D} = |Cl[3k]| |Cl[k]| + [k even] 3h |Cl[3k/2]|
                          + [3 | k] 2h^2
        #{g : g^k in N} = h^2 (1 + [k even] 3 + [3 | k] 2)
      (the transposition count: (v,t)^k = e needs (k/2).c = 0 on the
      fixed coordinate with the other two free subject to the sum,
      h |Cl[k/2]| per transposition; in D the fixed coordinate's
      condition is (3k/2).c = 0). The expected correction to a count
      over a window W is
        E[c_X] = sum over k >= 2 of (1/k) (#{g^k in X} / 6h^2)
                 #{q : q^k in W},   (every prime, 2 included since (A))
      and the relative deficit of the all-principal FRACTION is
        [ (3h + |Cl[2]|^2)/2 - 2 ] pi(sqrt x)/pi(x)
        + [ (2h^2 + |Cl[3]|^2)/3 - 1 ] pi(cbrt x)/pi(x) + ...
      The square coefficient grows like 3h/2 and the cube coefficient
      like 2h^2/3: at cut 1000 (pi(31.6) = 11, pi(10) = 4, pi(1000) =
      168) the two terms read 0.20 + 0.05 at h = 2, 0.20 + 0.19 at
      h = 3, 0.39 + 0.24 at h = 4, 0.39 + 0.38 at h = 5 -- a deficit
      deepening with h at first order, against the measured 0.14,
      0.34, 0.54, 0.65. The first-order figure overshoots at small x
      (Li against pi, and the window's own primes), which is why the
      test below puts the term back PER FIELD AND PER PRIME rather
      than reading the asymptotic coefficient.

  (5) THE STATISTIC'S ALGEBRA. The corrected count of an event is the
      counted primes plus the weights of the prime powers landing in
      it; the corrected total is the counted totally split primes plus
      the weights landing in N; the level is corrected count over
      (corrected total x model share), the model share being 1/h^2 for
      all-principal and t/h^2 for all-equal. The spread is Poisson on
      the expected corrected count, the parents' convention. The
      denominator's correction is about 15 % of the count at cut 1000
      and never nears zero. A cell's corrected count can exceed its
      expectation by the correction alone only if the raw count is
      already at the model, which is the case the question excludes.

  (6) WHAT IS NOT CONTROLLED. (a) The prime 2 and the ramified primes
      are walked by no class map here (the parents' maps walk odd
      unramified primes); their powers' weights are printed as an
      UNALLOCATED BOUND per window, never added. (b) The oscillatory
      remainder: one field's is as large as the shift and a population
      average is what removes it -- the strata here are 94, 45, 18 and
      18 fields, so the small strata read at a spread the field count
      sets and not the prime count. (c) Below the discriminant the
      remainder carries geometry the average does not remove; the
      per-bin table shows where the correction is the whole story and
      where it is not, and the pooled read is the prediction's.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_cubic_zero_tilt.py and its parents: the population,
    the class reading, the per-place vector reader, the regime
    classification at h = 3 and the F3 rows are IMPORTED, not
    re-implemented; every control those files run rides in with them.
 T2 FROM explore_ceiling_squares.py: the partial prime's square
    (2a, -a, -a) and the inert cube on (0, 0, 0) are that file's
    derivation (4), re-derived above and used at the triple event
    that file never read.
 T3 THE CYCLIC ASSUMPTION in (4)'s closed forms: |Cl[k]| = gcd(k, h)
    is read off h alone. At h = 2, 3, 5 the group is cyclic by order;
    at h = 4 the closed form is printed under the assumption and P3
    is read at the prime strata. The measured corrections carry no
    such assumption -- they are computed from the classes themselves.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE ALL-PRINCIPAL LEVEL CORRECTS TO 1. At every readable
      stratum -- h = 2, h = 3 (the M regime), h = 4, h = 5, readable
      meaning an expected corrected count of at least 10 -- the
      corrected all-principal level pooled over q^k < 1000 lies within
      2 sigma of 1, where the raw reads 0.86, 0.66, 0.46, 0.35.
  P2  THE DEEPENING IS THE CUBE TERM'S. The inert cubes' share of the
      all-principal correction, measured, is larger at h = 5 than at
      h = 2; and the closed form of (4) reproduces the measured
      all-principal correction within 20 % at h = 2, 3 and 5.
  P3  THE EQUAL EVENT CORRECTS TOO. At the h = 3 M pool the corrected
      all-equal level lies within 2 sigma of 1 (raw 0.65); and the D
      regime's all-principal count, read against ITS model 1/3 (the
      image is the diagonal, of order 3), corrects to within 2 sigma
      of 1.
  KILL, as observables: the corrected all-principal level more than
      3 sigma from 1 at two or more readable strata, or moving AWAY
      from 1 at any of them, prints the term as not the mechanism.

THE CONTROLS, run before any prediction is read.

  C1  REPRODUCTION. The raw strata reprint explore_cubic_split_triple.py
      F3 exactly -- 498 equal at h = 2, 12 at 4, 6 at 5, 8 at 6, 1 at 7
      against 580.0, 27.5, 19.2, 11.6, 3.0 expected -- and the h = 3 M
      pool reprints explore_cubic_zero_tilt.py's 1131 split, 245 equal,
      87 all-principal.
  C2  THE TOTALLY SPLIT COUNT ITSELF, the event N, which needs no class
      map and exercises the cube landing in N: over EVERY field of the
      population (1103, h = 1 included) the raw share of totally split
      primes among the odd unramified primes below 1000 sits below 1/6
      by at least 5 sigma, and the corrected share within 2 sigma of
      1/6.
  C3  THE WEIGHTS SUM TO ZERO: every split prime's k-th power triple
      sums to zero in the class group (as (3) requires), checked at
      every power used.

THE DESIGN. The parents' enumeration and class reading over the
complex fields; one walk per mapped field over its split and partial
primes with their class vectors, the inert primes read off the
discriminant, the window q^k < 1000 for every k >= 1; raw counts at
k = 1, correction weights at k >= 2, both by the parents' bins on the
value q^k and pooled; the expected corrections from (4) beside the
measured; the C2 control over every field from the splitting types
alone.

THE WIDE RUN (`--wide`, frozen before it ran). The population swaps for
explore_ceiling_topband.py's wide_class_reading() -- the parents' box
to |d| <= 6000 read by the parents' own policy plus the increment to
|d| <= 24000, the same record shape, the sibling's T4 exclusion
asserted by the sibling -- exactly as explore_ceiling_squares.py's
deg3_records(wide=True) does. The strata loops take every h the
population carries; C1 reads the parents' box alone, walked in the
same pass, and must reprint the rows above; C2 and C3 run over the
whole. Predictions: P1 holds again on the four strata of F1 (within 2
sigma of 1, none moving away) and on every stratum the wider count
makes readable; P2a's rise of the inert cube's share holds over every
h present; P3's M half reads the h = 3 all-equal level, which is the
one open figure -- if it corrects to within 2 sigma of 1 the residual
of F3 was the 45-field average's, and if it stands at F3's size it is
a third thing, to be recorded as measured. Estimate: the base run's
199 s with 158 s in the class reading and the squares rig's wide run
at 3.4 x its base run put this near 11 minutes.

THE SECOND FREEZE -- three extensions fixed after the first wide run
printed (its figures are W0 in the findings) and before the rerun,
each answering something that run showed.
  (A) THE PRIME 2, walked. Its type is read as any odd prime's (the
      algebra O/2O where 2 divides the index, the roots mod 2 where it
      does not -- and 2 is totally split only in the former case, the
      common-index-divisor case, which the first draft of this freeze
      wrongly excluded and the rehearsal caught), and each degree-1
      place above it is put through the parents' map
      (explore_cubic_class_map.py map_place) like any odd place; the
      powers then land by (3) exactly as an odd prime's. A probe over
      the complex fields to |d| <= 1500 placed 13 of 13 partial-2
      places, the map's several vectors agreeing modulo the lattice 26
      of 26 times, and every one of them NON-principal of full order.
      The ramified 2 and a 2 with an unplaced place stay in the bound.
  (B) THE REGIME AT EVERY h DIVISIBLE BY 3. The degenerate image of
      derivation (1) is the 3-part of N collapsed to the diagonal, and
      it is read EXACTLY per field: with m = h stripped of its 3s, a
      field is in regime D iff every fully mapped split prime has
      m.(b_i - b_j) = 0 for all pairs (its 3-parts pairwise equal) and
      at least MIN_SPLIT split primes, else M. The D image is N_m +
      diag_3, of order 3 m^2, so its all-principal share is 1/(3 m^2):
      1/3 at h = 3, 1/12 at h = 6. At h = 3 the parents' own rule (the
      equal fraction against HIGH_FRAC) stays the stratum definition
      (T1) and the exact test's agreement with it is printed; at h =
      9 other intermediate images exist and an M there means only
      "not the diagonal".
  (C) THE BOX, wide only: every stratum's pooled level read for the
      parents' box |d| <= 6000 and the increment separately -- (6c)'s
      geometry is the remainder below the discriminant, and the wide
      population widens the discriminant while the prime window
      stands.
  P4  At h = 6 the exact test sorts the fields into M and D, and each
      regime's corrected all-principal level against ITS share lies
      within 2 sigma of 1 wherever the regime is readable; at h = 3
      the exact test agrees with the parents' regime on every field.
  P5  The prime 2 moves the pooled all-principal level UP by 0.01 to
      0.02 at h = 2 and by 0.03 to 0.05 at h = 3 M (hand: per field
      about 0.26 on {e} and 0.56 on N at h = 2, 0.17 and 0.56 at h =
      3, with the partial place of full order), and the h = 3 M level
      stays outside 2 sigma of 1.
  P6  At h = 2 the parents' box reprints the base run's bins (top bin
      1.020) and the increment's top bin carries the overshoot; the
      corrected level rises with |d| at a fixed window.
  C4  The map's several vectors for the place above 2 agree modulo
      the lattice at every placed field.

FINDINGS. Two populations: the parents' box (|d| <= 6000, 1103
fields, the base run) and the wide one (|d| <= 24000, 4865 fields,
1367 with h > 1, the `--wide` run); the wide figures are the claim's
and the base ones are quoted where the box is the point. W0 marks the
first wide run, before the second freeze: it read h = 2 at 1.027 +-
0.017, h = 3 M at 0.840 +- 0.033, h = 6 UNSORTED at 1.494 (z = +3.5,
its raw count at 0.959 of the full-image model) and the h = 3 M
all-equal event at 0.915 +- 0.019.

  F1. THE DEEPENING IS THE CUBE TERM'S: THE CORRECTED LEVEL IS FLAT IN
      h ACROSS EIGHT READABLE STRATA (the cube's landing on the identity
      a property, by (3); the flatness a pattern across the strata; P2a
      SURVIVES on both populations, P4 SURVIVES, C1-C4 pass). The
      weights of (3), the prime 2 included, put back per field and per
      prime over q^k < 1000 on the wide population:

          h = 2     484 fields  2601 of 12098  raw 0.860  level 1.058 +- 0.017
          h = 3 M   283 fields   485 of  7232  raw 0.604  level 0.877 +- 0.033
          h = 4     106 fields    94 of  2622  raw 0.574  level 1.061 +- 0.072
          h = 5      92 fields    44 of  2295  raw 0.479  level 1.068 +- 0.096
          h = 6 M    50 fields    15 of  1230  raw 0.439  level 1.117 +- 0.158
          h = 7      37 fields     6 of   875  raw 0.336  level 1.114 +- 0.219
          h = 8      23 fields     1 of   551  raw 0.116  level 1.294 +- 0.313
          h = 9 M    30 fields     4 of   711  raw 0.456  level 1.200 +- 0.313

      The raw shortfall runs from 0.86 to 0.12 across the strata and
      the corrected level does not move with h; the inert cube's
      share of the all-principal correction reads 0.170, 0.247, 0.334,
      0.450, 0.401, 0.638, 0.518, 0.689 at h = 2 to 9 (base: 0.187,
      0.298, 0.486, 0.472 at h = 2 to 5). The regimes of (B): the
      exact 3-part test agrees with the parents' equal-fraction rule
      on all 413 h = 3 fields (83 of 83 in the box), and at h = 6 it
      sorts 15 degenerate fields (image of order 12) from 50 full
      ones -- W0's 1.494 splits into 1.117 +- 0.158 against 1/36 and
      1.097 +- 0.171 against 1/12 (z = +0.74, +0.56). The h = 3
      degenerate regime reads 0.968 +- 0.029 against 1/3 (994 of 3086,
      raw 0.966). C2 over all 4865 fields and 804,769 odd unramified
      primes: raw 0.14953 against 1/6 at z = -41.3, corrected 0.16740
      at z = +1.77, the correction 3.55 per field. The prime 2 (A):
      every degree-1 place above it placed (no field unplaced), the
      map's vectors agreeing modulo the lattice at every field (C4);
      it is ramified in 161, inert in 140, partial in 151 and totally
      split in 32 of the h = 2 fields, 52 of its places principal
      there, 21 at h = 3 M (1 in the degenerate regime), 3 at h = 4, 1 at
      h = 5, none above. The
      base population, for the record: 1.030 +- 0.038, 0.909 +- 0.083,
      0.812, 0.872 at h = 2, 3 M, 4, 5 (four of four within 2 sigma;
      1.002, 0.891, 0.731, 0.843 before the prime 2 was walked).

  F2. THE WHOLE SHORTFALL IS NOT THE TERM ALONE: THE FROZEN KILL FIRES
      ON THE WIDE POPULATION, WITH OPPOSITE SIGNS AT THE TWO STRATA
      (observation; P1 KILLED as frozen -- two readable strata beyond
      3 sigma -- P3's M half KILLED again, P5 half right, P6 half
      right). h = 2 sits OVER at 1.058 +- 0.017 (z = +3.46): by bin
      1.044, 0.818, 1.002, 1.114 (z = +0.7, -3.2, +0.1, +5.3), the top
      bin [300, 1000) carrying the excess with its raw count already
      at 0.982 of the model; by box 1.030 +- 0.038 in the parents' box
      and 1.064 +- 0.019 in the increment (z = +0.8, +3.5). h = 3 M
      sits UNDER at 0.877 +- 0.033 (z = -3.74), the box 0.909 +- 0.083
      and the increment 0.871 +- 0.036 agreeing; by bin 1.146, 0.565,
      0.818, 0.917 (z = +1.2, -4.1, -2.7, -2.0). Its all-equal event
      reads 0.934 +- 0.019 (z = -3.5, W0 0.915, base 0.869 +- 0.048
      with the prime 2, 0.850 without) and its non-principal classes
      (c, c, c) 0.963 +- 0.023 (z = -1.6): the equal event's residual
      is the all-principal one's. The h >= 4 strata all sit above 1
      (1.06 to 1.29), pooled 413.4 against 382.3 expected (z = +1.6).
      What the two signs say: the spread is Poisson on the expectation,
      which the field-to-field remainder of (6b) widens without changing
      a sign; and BOTH residuals sit inside the ramified primes'
      unallocated bound (F4), since a weight landing on the identity
      raises a level and one landing in N and missing the identity
      lowers it -- the h = 3 M deficit (114 on 928; 2 is ramified in 178
      of the 283 fields) is the first kind's size and the h = 2 excess
      (+207 on 3571, against 1135 of N-weight in the bound) the
      second's. The prime 2 moved h = 2 by +0.031 and h = 3 M by +0.037
      (P5 froze +0.01 to +0.02 and +0.03 to +0.05, the h = 2 band
      missed), and the level rises with |d| at h = 2, 4, 5, 6 and falls
      at both h = 3 regimes (P6's "rises" half wrong). Whether the
      residuals are the ramified primes' powers, the remainder below the
      discriminant (the window q^k < 1000 sits under |d| at every field
      of the increment), or a third thing is left open here: the
      instrument that decides first is the ramified primes' powers read
      by their inertia cosets (a map extension: the inertia group's
      image in N x| S3 per ramified prime), and the window scaled to |d|
      is the second, a different population read.

  F3. THE CLOSED FORM OF (4) OVERSHOOTS THE MEASURED CORRECTION BY A
      THIRD TO A HALF, FOR A REASON THE RIG PRINTS (observation; P2b
      KILLED at its frozen 20 %). Wide: 1177 measured against 1786 at
      h = 2 (34 %), 329 against 636 at h = 3 (48 %), 71 against 127 at
      h = 5 (44 %); on N, 2187 against 2612, 1116 against 1527, 398
      against 496. The closed form takes every base q <= 31 at its
      asymptotic share and they are nowhere near it: totally split
      0.146, 0.152, 0.132, 0.134 against 1/6 at h = 2 to 5, a partial
      prime's degree-1 place principal 0.290 against 0.500 at h = 2,
      0.235 against 0.333 at h = 3, 0.133 against 0.250 at h = 4,
      0.126 against 0.200 at h = 5, and the prime 2 taken at the
      uniform kinds when it is ramified in a third of the fields --
      the small-prime deficit the corpus located at the bottom bin,
      now located on the bases of the prime powers. The term is
      therefore read per prime and never by its leading coefficient,
      and (4)'s first-order deficits (0.24, 0.39, 0.63, 0.77, 1.21,
      1.35 at h = 2 to 7) are the asymptotic shape of the deepening,
      not its size at cut 1000.

  F4. WHAT THE UNALLOCATED BOUND SAYS (property of the rig). With the
      prime 2 walked, the bound is the ramified primes' powers alone:
      1135 on the h = 2 stratum against a correction of 1177 and 1096
      at h = 3 M against 329 -- a bound and not an estimate, since a
      ramified prime's powers land by the inertia coset and no map
      here reads them. The bound covers either residual of F2, by the
      identity's share of it or by N's.

RUN RECORD. 2026-08-21, Windows 11, Python 3, `python
prime/code/memwatch.py python prime/code/explore_triple_cube_term.py`
and the same with `--wide`. One process, CPython, no BLAS. Base: 15
checks, 199.2 s wall, peak working set 77.0 MB against memwatch's 512
MB ceiling; enumeration 15370 polynomials -> 1103 fields, class reading
0 unresolved. Wide: 15 checks, 777.4 s wall, peak working set 125.7 MB;
15370 + 85050 polynomials -> 1103 base + 3765 increment fields in 52 s,
class reading 4865 fields kept and 3 excluded unresolved (-7699, -7771,
-23928, the sibling's own T4 policy) in 578 s, C2 over every field in
37 s, the walk over the 19 strata in 102 s. The wide run ran three
times on the day: W0 with the first freeze alone; then with the second
freeze, whose first draft of (A) said 2 never splits and whose base
rehearsal raised KeyError 'split' at the first common-index-divisor
field -- the claim was wrong and the draft is recorded in (A); then
with (4)'s closed form summing over the prime 2 as well, which changed
F3's column and nothing else. The base run ran after each edit and
reprinted C1 each time.
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

CHECKS = 0
PRIME_CAP = ECP.PRIME_CAP
ODD_PRIMES = ECP.ODD_PRIMES
BIN_EDGES = ECP.BIN_EDGES
MIN_SPLIT = ST.MIN_SPLIT
HIGH_FRAC = ST.HIGH_FRAC
MIN_READ = 10.0         # expected corrected count a stratum needs
F3_ROWS = ZT.F3_ROWS    # (equal, expected) by h, the parents' F3
SEC_II = (1131, 245, 87)  # h = 3 M pool: split, equal, all-principal


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


def bin_of(n):
    for i in range(len(BIN_EDGES) - 1):
        if BIN_EDGES[i] <= n < BIN_EDGES[i + 1]:
            return i
    return None


def powers(q):
    """(k, q^k) for k >= 1 with q^k below the cap."""
    out, k, n = [], 1, q
    while n < PRIME_CAP:
        out.append((k, n))
        k += 1
        n *= q
    return out


def scale(v, m):
    return [m * x for x in v]


def gcd(a, b):
    return math.gcd(a, b)


# ------------------------------------------------------- the closed form
def count_pow(h, k, event):
    """#{g in G : g^k in event} under (4), Cl cyclic of order h."""
    ev = 1 if k % 2 == 0 else 0
    th = 1 if k % 3 == 0 else 0
    if event == 'e':
        return (gcd(k, h) ** 2 + ev * 3 * h * gcd(k // 2, h)
                + th * 2 * h * h)
    if event == 'D':
        return (gcd(3 * k, h) * gcd(k, h)
                + ev * 3 * h * gcd(3 * k // 2, h) + th * 2 * h * h)
    return h * h * (1 + ev * 3 + th * 2)


def expected_corr(h, event, nfields, lo, hi):
    """E[c_event] over nfields fields for q^k in [lo, hi), k >= 2."""
    tot = 0.0
    for q in [2] + list(ODD_PRIMES):     # the prime 2 walked since (A)
        for (k, n) in powers(q):
            if k < 2 or not (lo <= n < hi):
                continue
            tot += (1.0 / k) * count_pow(h, k, event) / (6.0 * h * h)
    return tot * nfields


# --------------------------------------------------------------- the walk
def new_cell():
    return dict(ns=0, n3=0, neq=0, cN=0.0, c3=0.0, cE=0.0,
                c3_src=dict(ssq=0.0, psq=0.0, icb=0.0, scb=0.0, hi=0.0),
                unalloc=0.0)


SMALL = {}          # (h, reg) -> kinds and shares over the bases q^2 < cap
TWO = {'disagree': 0}   # (h, reg) -> the prime 2's kinds; C4's count
REGIME = dict(agree=0, disagree=0)   # h = 3: the exact test vs HIGH_FRAC


def land(cell, w, in_N, in_e, in_D, src):
    if in_N:
        cell['cN'] += w
    if in_e:
        cell['c3'] += w
        cell['c3_src'][src] += w
    if in_D:
        cell['cE'] += w


def place_over_two(rec):
    """(kind, per-place map output) for the prime 2: its type, and for
    each degree-1 place above it the parents' map's vectors (several
    per place, checked against each other by C4), None where the map
    placed nothing. The list is empty for an inert or a ramified 2."""
    (d, cx, a, b, c, O, h, kind, gp, rel) = rec
    if d % 2 == 0:
        return 'ramified', []
    pdisc = CFS.poly_disc3(a, b, c)
    places, kd = ECP.deg1_places(O, a, b, c, pdisc, 2)
    if kd in ('inert', 'ramified'):
        return kd, []
    rows = ECP.t2_rows(O, a, b, c)
    k = len(gp)
    gbp = {}
    for col, (q, e, f, name, Q) in enumerate(gp):
        gbp.setdefault(q, []).append((col, f, Q))
    out = []
    for P in places:
        got, _saw = CCM.map_place(O, P, 2, rows, cx, gp, gbp, sorted(gbp),
                                  k)
        out.append(got if got else None)
    return kd, out


def walk_field(rec, per_prime, piv, k, two):
    """One field: per-bin raw counts and corrections. Returns
    ({bin: cell}, n_bad_sum, small) with small the field's census of
    kinds over the bases q with q^2 below the cap; two = (kind,
    vectors) for the prime 2 from place_over_two."""
    (d, cx, a, b, c, O, h, kind, gp, rel) = rec
    pdisc = CFS.poly_disc3(a, b, c)
    seen = {}
    for (p, kd, vecs) in per_prime:
        seen[p] = (kd, vecs)
    cells = {}
    bad = 0
    small = dict(split=0, partial=0, inert=0, pp=0)
    for q in ODD_PRIMES:
        if q in seen:
            kd, vecs = seen[q]
            if any(v is None for v in vecs):
                continue
        elif d % q == 0:
            kd, vecs = 'ramified', None
        else:
            if q * q >= PRIME_CAP:
                continue            # its powers are out of the window
            _pl, kd = ECP.deg1_places(O, a, b, c, pdisc, q)
            vecs = None
            if kd not in ('inert', 'ramified'):
                raise AssertionError("unmapped %s prime %d at d = %d"
                                     % (kd, q, d))
        if q * q < PRIME_CAP and kd != 'ramified':
            small[kd] += 1
            if kd == 'partial' and len(vecs) == 1:
                small['pp'] += 1 if ST.is_principal(vecs[0], piv, k) else 0
        for (kk, n) in powers(q):
            bi = bin_of(n)
            if bi is None:
                continue
            cell = cells.setdefault(bi, new_cell())
            w = 1.0 / kk
            if kd == 'ramified':
                cell['unalloc'] += w
                continue
            if kk == 1:
                if kd == 'split' and len(vecs) == 3:
                    cell['ns'] += 1
                    z = sum(1 for v in vecs if ST.is_principal(v, piv, k))
                    eq = (ST.same_class(vecs[0], vecs[1], piv, k)
                          and ST.same_class(vecs[0], vecs[2], piv, k))
                    if z == 3:
                        cell['n3'] += 1
                    if eq:
                        cell['neq'] += 1
                continue
            # k >= 2: where does Frob^k land?
            if kd == 'split':
                if len(vecs) != 3:
                    continue
                kv = [scale(v, kk) for v in vecs]
                if not ST.sums_to_zero(kv, piv, k):
                    bad += 1
                in_N = True
                in_e = all(ST.is_principal(v, piv, k) for v in kv)
                in_D = (ST.same_class(kv[0], kv[1], piv, k)
                        and ST.same_class(kv[0], kv[2], piv, k))
                src = 'ssq' if kk == 2 else 'scb' if kk == 3 else 'hi'
            elif kd == 'partial':
                if kk % 2 or len(vecs) != 1:
                    continue
                a1 = vecs[0]
                in_N = True
                in_e = ST.is_principal(scale(a1, kk // 2), piv, k)
                in_D = ST.is_principal(scale(a1, 3 * kk // 2), piv, k)
                src = 'psq' if kk == 2 else 'hi'
            else:                   # inert
                if kk % 3:
                    continue
                in_N = in_e = in_D = True
                src = 'icb' if kk == 3 else 'hi'
            land(cell, w, in_N, in_e, in_D, src)
    # the prime 2's powers (A), by (3) like any prime; a ramified 2 or
    # one with an unplaced place stays in the bound. Its k = 1 is no
    # count: the raw counts are the odd primes' by construction.
    kd2, per2 = two
    placed = [g[0] for g in per2] if per2 and all(per2) else None
    for (kk, n) in powers(2):
        bi = bin_of(n)
        if bi is None or kk < 2:
            continue
        cell = cells.setdefault(bi, new_cell())
        w = 1.0 / kk
        if kd2 == 'inert':
            if kk % 3 == 0:
                land(cell, w, True, True, True,
                     'icb' if kk == 3 else 'hi')
        elif kd2 == 'partial' and placed:
            a2 = placed[0]
            if kk % 2 == 0:
                land(cell, w, True,
                     ST.is_principal(scale(a2, kk // 2), piv, k),
                     ST.is_principal(scale(a2, 3 * kk // 2), piv, k),
                     'psq' if kk == 2 else 'hi')
        elif kd2 == 'split' and placed and len(placed) == 3:
            kv = [scale(v, kk) for v in placed]
            if not ST.sums_to_zero(kv, piv, k):
                bad += 1
            land(cell, w, True,
                 all(ST.is_principal(v, piv, k) for v in kv),
                 (ST.same_class(kv[0], kv[1], piv, k)
                  and ST.same_class(kv[0], kv[2], piv, k)),
                 'ssq' if kk == 2 else 'scb' if kk == 3 else 'hi')
        else:
            cell['unalloc'] += w
    return cells, bad, small


def merge(into, cell):
    for key in ('ns', 'n3', 'neq', 'cN', 'c3', 'cE', 'unalloc'):
        into[key] += cell[key]
    for key in into['c3_src']:
        into['c3_src'][key] += cell['c3_src'][key]


def read_population(recs, base_cap=None):
    """Walk the mapped complex population. Returns
    (strata, nfields, bad, base) with strata[(h, reg)] = {bin: cell};
    base is the same table over the fields with |d| <= base_cap alone
    (the parents' box inside a wider population), None when no cap."""
    strata, nfields = {}, {}
    base = {} if base_cap else None
    bad = 0
    t0 = time.time()
    for rec in recs:
        (d, cx, a, b, c, O, h, kind, gp, rel) = rec
        if h is None or h == 1 or not cx:
            continue
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        if H is None or H == 1:
            continue
        two = place_over_two(rec)
        kd2, per2 = two
        for got in per2:
            for v in (got or [])[1:]:
                if not ST.same_class(got[0], v, piv, k):
                    TWO['disagree'] += 1
        cells, nb, small = walk_field(rec, per_prime, piv, k, two)
        bad += nb
        ns = sum(x['ns'] for x in cells.values())
        neq = sum(x['neq'] for x in cells.values())
        reg = 'A'
        if H % 3 == 0:
            exact = diagonal_3part(per_prime, piv, k, H)
            if H == 3:
                reg = ('X' if ns < MIN_SPLIT
                       else 'D' if float(neq) / ns >= HIGH_FRAC else 'M')
                if reg != 'X':
                    REGIME['agree' if (reg == 'D') == exact
                           else 'disagree'] += 1
            else:
                reg = 'X' if ns < MIN_SPLIT else 'D' if exact else 'M'
        key = (H, reg)
        nfields[key] = nfields.get(key, 0) + 1
        sm = SMALL.setdefault(key, dict(split=0, partial=0, inert=0, pp=0))
        for kk in sm:
            sm[kk] += small[kk]
        tw = TWO.setdefault(key, dict(ramified=0, inert=0, partial=0,
                                      split=0, unplaced=0, pp=0))
        tw[kd2] += 1
        if per2:
            if all(per2):
                tw['pp'] += sum(1 for got in per2
                                if ST.is_principal(got[0], piv, k))
            else:
                tw['unplaced'] += 1
        tables = [strata]
        if base is not None and abs(d) <= base_cap:
            tables.append(base)
        for table in tables:
            st = table.setdefault(key, {})
            for bi, cell in cells.items():
                merge(st.setdefault(bi, new_cell()), cell)
    print("  mapped complex population walked in %.1f s, %d strata"
          % (time.time() - t0, len(strata)))
    return strata, nfields, bad, base


def three_free(h):
    """h with its factors of 3 stripped: m of (B)."""
    while h % 3 == 0:
        h //= 3
    return h


def diagonal_3part(per_prime, piv, k, h):
    """(B): every fully mapped split prime has its three classes'
    3-parts pairwise equal, i.e. m.(b_i - b_j) = 0 with m = h without
    its 3s."""
    m = three_free(h)
    for (p, kd, vecs) in per_prime:
        if kd != 'split' or len(vecs) != 3 or any(v is None for v in vecs):
            continue
        u = [scale(v, m) for v in vecs]
        if not (ST.same_class(u[0], u[1], piv, k)
                and ST.same_class(u[0], u[2], piv, k)):
            return False
    return True


def share_of(h, reg):
    """The model's all-principal share: 1/h^2 on the full image,
    1/(3 m^2) on the degenerate one (B)."""
    if reg == 'D':
        m = three_free(h)
        return 1.0 / (3 * m * m)
    return 1.0 / (h * h)


def diff_cell(whole, part):
    out = new_cell()
    for key in ('ns', 'n3', 'neq', 'cN', 'c3', 'cE', 'unalloc'):
        out[key] = whole[key] - part[key]
    for key in out['c3_src']:
        out['c3_src'][key] = whole['c3_src'][key] - part['c3_src'][key]
    return out


def class_numbers(strata):
    """The h values the population carries, in order."""
    return tuple(sorted(set(h for (h, reg) in strata)))


def pooled(st, bins=None):
    out = new_cell()
    for bi, cell in st.items():
        if bins is None or bi in bins:
            merge(out, cell)
    return out


# ------------------------------------------------------------ the reads
def level(count, corr, total, share):
    exp = total * share
    if exp <= 0:
        return None, None, exp
    lv = (count + corr) / exp
    z = (count + corr - exp) / math.sqrt(exp)
    return lv, z, exp


def s_reproduce(strata):
    section("C1  REPRODUCTION -- the raw strata against the parents")
    print("  %-4s %-5s %-7s %-7s %-7s %-9s %s"
          % ("h", "reg", "split", "equal", "all-p", "model", "parents"))
    for h in class_numbers(strata):
        regs = ('M', 'D', 'X') if h == 3 else ('all',)
        for reg in regs:
            if reg == 'all':
                c = new_cell()
                for r in ('A', 'M', 'D', 'X'):
                    if (h, r) in strata:
                        merge(c, pooled(strata[(h, r)]))
            elif (h, reg) in strata:
                c = pooled(strata[(h, reg)])
            else:
                continue
            t3 = 3 if h % 3 == 0 else 1
            model = c['ns'] * t3 / float(h * h)
            ref = ""
            if h != 3 and h in F3_ROWS:
                eq, exp = F3_ROWS[h]
                ref = "F3 %d / %.1f" % (eq, exp)
                ok(c['neq'] == eq, "h = %d equal %d, F3 %d"
                   % (h, c['neq'], eq))
                ok(abs(model - exp) < 0.06, "h = %d model %.2f, F3 %.1f"
                   % (h, model, exp))
            if (h, reg) == (3, 'M'):
                ref = "zero_tilt %d / %d / %d" % SEC_II
                ok((c['ns'], c['neq'], c['n3']) == SEC_II,
                   "h = 3 M pool %s" % str((c['ns'], c['neq'], c['n3'])))
            print("  %-4d %-5s %-7d %-7d %-7d %-9.1f %s"
                  % (h, reg, c['ns'], c['neq'], c['n3'], model, ref))


def s_split_control(recs):
    section("C2  THE TOTALLY SPLIT COUNT over every field -- the event N")
    t0 = time.time()
    raw = tot = corr = 0.0
    nf = 0
    for (d, cx, a, b, c, O, h, kind, gp, rel) in recs:
        nf += 1
        pdisc = CFS.poly_disc3(a, b, c)
        for q in ODD_PRIMES:
            if d % q == 0:
                continue
            _pl, kd = ECP.deg1_places(O, a, b, c, pdisc, q)
            if kd == 'ramified':
                continue
            tot += 1
            if kd == 'split':
                raw += 1
            for (kk, n) in powers(q):
                if kk < 2:
                    continue
                if (kd == 'split' or (kd == 'partial' and kk % 2 == 0)
                        or (kd == 'inert' and kk % 3 == 0)):
                    corr += 1.0 / kk
    share = 1.0 / 6
    se = math.sqrt(share * (1 - share) / tot)
    z_raw = (raw / tot - share) / se
    z_cor = ((raw + corr) / (tot + corr) - share) / se
    print("  %d fields, %d odd unramified primes, %d totally split"
          % (nf, int(tot), int(raw)))
    print("  raw share       %.5f   z = %+.2f against 1/6"
          % (raw / tot, z_raw))
    print("  correction      %.1f on N over %d fields (%.2f per field)"
          % (corr, nf, corr / nf))
    print("  corrected share %.5f   z = %+.2f    (%.1f s)"
          % ((raw + corr) / (tot + corr), z_cor, time.time() - t0))
    ok(z_raw <= -5, "raw totally split share not short at 5 sigma")
    ok(abs(z_cor) <= 2, "corrected share off 1/6 at z = %.2f" % z_cor)


def s_levels(strata, nfields, base=None):
    section("S3  THE ALL-PRINCIPAL EVENT, corrected -- P1")
    print("  level = (count + correction) / (corrected total x share);"
          " share 1/h^2, or 1/(3 m^2) in regime D; sigma Poisson on the"
          " expectation")
    readable = []
    for h in class_numbers(strata):
        for reg in ('A', 'M', 'D'):
            key = (h, reg)
            if key not in strata:
                continue
            c = pooled(strata[key])
            share = share_of(h, reg)
            lv_raw, z_raw, exp_raw = level(c['n3'], 0.0, c['ns'], share)
            lv, z, exp = level(c['n3'], c['c3'], c['ns'] + c['cN'], share)
            tag = ""
            if exp >= MIN_READ and reg != 'D':
                readable.append((h, reg, lv, z))
                tag = "  readable"
            print("  h = %d %s  %3d fields  split %5d  all-p %4d  "
                  "raw %.3f  | corr +%.1f on %d, +%.1f on N  "
                  "-> exp %.1f  level %.3f  z %+.2f  unalloc <= %.1f%s"
                  % (h, reg, nfields[key], c['ns'], c['n3'], lv_raw,
                     c['c3'], c['n3'], c['cN'], exp, lv, z,
                     c['unalloc'], tag))
            if base is not None:
                cb_ = pooled(base[key]) if key in base else new_cell()
                ci_ = diff_cell(c, cb_)
                for name, cc in (("parents' box", cb_), ("increment", ci_)):
                    lb, zb, eb = level(cc['n3'], cc['c3'],
                                       cc['ns'] + cc['cN'], share)
                    print("     %-13s split %5d  all-p %4d  corr +%.1f/+%.1f"
                          "  exp %.1f  level %s  z %s"
                          % (name, cc['ns'], cc['n3'], cc['c3'], cc['cN'],
                             eb, "%.3f" % lb if lb is not None else "--",
                             "%+.2f" % zb if zb is not None else "--"))
            print("     by bin (q^k in bin):")
            for bi in range(len(BIN_EDGES) - 1):
                if bi not in strata[key]:
                    continue
                cb = strata[key][bi]
                lr, zr, er = level(cb['n3'], 0.0, cb['ns'], share)
                lc, zc, ec = level(cb['n3'], cb['c3'],
                                   cb['ns'] + cb['cN'], share)
                print("       [%4d,%5d)  split %5d  all-p %4d  raw %s"
                      "  corr +%.2f/+%.2f  level %s  z %s"
                      % (BIN_EDGES[bi], BIN_EDGES[bi + 1], cb['ns'],
                         cb['n3'],
                         "%.3f" % lr if lr is not None else "--",
                         cb['c3'], cb['cN'],
                         "%.3f" % lc if lc is not None else "--",
                         "%+.2f" % zc if zc is not None else "--"))
    print("  P1 reads %d readable strata:" % len(readable))
    far = [r for r in readable if abs(r[3]) > 3]
    for (h, reg, lv, z) in readable:
        print("     h = %d %s  corrected level %.3f  z = %+.2f  %s"
              % (h, reg, lv, z, "within 2 sigma" if abs(z) <= 2
                 else "OUTSIDE 2 sigma"))
    print("  [P1] %d of %d within 2 sigma; %d beyond 3 sigma (kill at 2)"
          % (sum(1 for r in readable if abs(r[3]) <= 2), len(readable),
             len(far)))
    return readable


def s_cube(strata, nfields):
    section("S4  THE DEEPENING -- the inert cube's share, and the closed "
            "form of (4) -- P2")
    print("  %-9s %-8s %-8s %-8s %-8s %-8s | %-9s %-9s %s"
          % ("stratum", "ssq", "psq", "icb", "scb", "hi",
             "c3 meas", "c3 (4)", "icb share"))
    shares = {}
    agree = {}
    for h in class_numbers(strata):
        for reg in ('A', 'M'):
            key = (h, reg)
            if key not in strata:
                continue
            c = pooled(strata[key])
            s = c['c3_src']
            exp3 = expected_corr(h, 'e', nfields[key], 3, PRIME_CAP)
            expN = expected_corr(h, 'N', nfields[key], 3, PRIME_CAP)
            sh = s['icb'] / c['c3'] if c['c3'] else 0.0
            shares[h] = sh
            agree[h] = abs(c['c3'] - exp3) / exp3 if exp3 else None
            print("  h = %d %-3s %-8.2f %-8.2f %-8.2f %-8.2f %-8.2f | "
                  "%-9.2f %-9.2f %.3f     (N: %.1f measured, %.1f (4))"
                  % (h, reg, s['ssq'], s['psq'], s['icb'], s['scb'],
                     s['hi'], c['c3'], exp3, sh, c['cN'], expN))
    print("  inert cube share: h = 2 %.3f, h = 5 %.3f"
          % (shares.get(2, 0), shares.get(5, 0)))
    print("  [P2a] %s" % ("rises" if shares.get(5, 0) > shares.get(2, 0)
                         else "DOES NOT RISE"))
    for h in (2, 3, 5):
        if h in agree:
            print("  [P2b] h = %d: measured against (4) differ by %.1f %%%s"
                  % (h, 100 * agree[h],
                     "" if agree[h] <= 0.20 else "   (beyond 20 %)"))
    # what (4) assumes and the small primes do not give: the kinds and
    # the shares over the bases q with q^2 below the cap
    print("  the bases q <= %d, measured against (4)'s uniform input:"
          % int(PRIME_CAP ** 0.5))
    print("  %-9s %-22s %-22s %-22s %s"
          % ("stratum", "split (1/6)", "partial (1/2)",
             "inert (1/3)", "partial place principal (1/h)"))
    for h in class_numbers(strata):
        for reg in ('A', 'M'):
            key = (h, reg)
            if key not in strata:
                continue
            kc = SMALL[key]
            tot = float(kc['split'] + kc['partial'] + kc['inert'])
            if not tot:
                continue
            print("  h = %d %-3s %-22s %-22s %-22s %s"
                  % (h, reg,
                     "%d  %.3f" % (kc['split'], kc['split'] / tot),
                     "%d  %.3f" % (kc['partial'], kc['partial'] / tot),
                     "%d  %.3f" % (kc['inert'], kc['inert'] / tot),
                     "%d of %d  %.3f against %.3f"
                     % (kc['pp'], kc['partial'],
                        kc['pp'] / float(kc['partial'] or 1), 1.0 / h)))
    # the prime 2 (A): kinds, placements, and the partial place's class
    print("  the prime 2 by stratum: ramified / inert / partial / split"
          " fields; fields with an unplaced place; principal places")
    for h in class_numbers(strata):
        for reg in ('A', 'M', 'D'):
            key = (h, reg)
            if key not in TWO:
                continue
            t = TWO[key]
            print("  h = %d %-3s %3d / %3d / %3d / %3d   unplaced %d"
                  "   principal places %d"
                  % (h, reg, t['ramified'], t['inert'], t['partial'],
                     t['split'], t['unplaced'], t['pp']))
    # the first-order coefficients, for the record
    print("  first-order relative deficit of the all-principal fraction,"
          " (4) at cut %d:" % PRIME_CAP)
    pi_x = len(ODD_PRIMES) + 1
    pi_sq = sum(1 for q in ODD_PRIMES if q * q < PRIME_CAP) + 1
    pi_cb = sum(1 for q in ODD_PRIMES if q ** 3 < PRIME_CAP) + 1
    for h in (2, 3, 4, 5, 6, 7):
        cl2 = gcd(2, h)
        cl3 = gcd(3, h)
        sq = ((3 * h + cl2 * cl2) / 2.0 - 2) * pi_sq / float(pi_x)
        cb = ((2 * h * h + cl3 * cl3) / 3.0 - 1) * pi_cb / float(pi_x)
        print("     h = %d  square %.2f + cube %.2f = %.2f" % (h, sq, cb,
                                                              sq + cb))


def s_equal(strata, nfields):
    section("S5  THE ALL-EQUAL EVENT at h = 3, and the D regime -- P3")
    out = {}
    for reg in ('M', 'D'):
        key = (3, reg)
        if key not in strata:
            continue
        c = pooled(strata[key])
        share = 1.0 / 3            # t/h^2 = 3/9 in M; in D the image
        #                            is share_of(3, 'D') = 1/3 as well
        #                            is the diagonal and every triple
        #                            is equal: share 1 for equal,
        #                            1/3 for all-principal
        if reg == 'M':
            lr, zr, _ = level(c['neq'], 0.0, c['ns'], share)
            lc, zc, exp = level(c['neq'], c['cE'], c['ns'] + c['cN'],
                                share)
            print("  h = 3 M  %d fields  equal %d of %d  raw %.3f  "
                  "corr +%.1f / +%.1f  exp %.1f  level %.3f  z %+.2f"
                  % (nfields[key], c['neq'], c['ns'], lr, c['cE'],
                     c['cN'], exp, lc, zc))
            out['M'] = zc
            ln, zn, en = level(c['neq'] - c['n3'], c['cE'] - c['c3'],
                               c['ns'] + c['cN'], 2.0 / 9)
            print("     the non-principal equal triples (c, c, c), "
                  "c of order 3, model 2/9: %d raw, corr +%.1f, exp %.1f,"
                  " level %.3f, z %+.2f"
                  % (c['neq'] - c['n3'], c['cE'] - c['c3'], en, ln, zn))
            print("     by bin (q^k in bin): equal | non-principal equal")
            for bi in range(len(BIN_EDGES) - 1):
                if bi not in strata[key]:
                    continue
                cb = strata[key][bi]
                lr, zr, _ = level(cb['neq'], 0.0, cb['ns'], share)
                lc, zc2, ec = level(cb['neq'], cb['cE'],
                                    cb['ns'] + cb['cN'], share)
                ln, zn, en = level(cb['neq'] - cb['n3'],
                                   cb['cE'] - cb['c3'],
                                   cb['ns'] + cb['cN'], 2.0 / 9)
                print("       [%4d,%5d)  split %5d  equal %4d  raw %s"
                      "  corr +%.2f  level %s  z %s | %d raw, corr "
                      "+%.2f, level %s, z %s"
                      % (BIN_EDGES[bi], BIN_EDGES[bi + 1], cb['ns'],
                         cb['neq'],
                         "%.3f" % lr if lr is not None else "--",
                         cb['cE'],
                         "%.3f" % lc if lc is not None else "--",
                         "%+.2f" % zc2 if zc2 is not None else "--",
                         cb['neq'] - cb['n3'], cb['cE'] - cb['c3'],
                         "%.3f" % ln if ln is not None else "--",
                         "%+.2f" % zn if zn is not None else "--"))
        else:
            lr, zr, _ = level(c['n3'], 0.0, c['ns'], share)
            lc, zc, exp = level(c['n3'], c['c3'], c['ns'] + c['cN'],
                                share)
            print("  h = 3 D  %d fields  all-p %d of %d  raw %.3f  "
                  "corr +%.1f / +%.1f  exp %.1f  level %.3f  z %+.2f"
                  "   (model 1/3: the image is the diagonal)"
                  % (nfields[key], c['n3'], c['ns'], lr, c['c3'],
                     c['cN'], exp, lc, zc))
            out['D'] = zc
    for reg, z in out.items():
        print("  [P3] %s regime: %s" % (reg, "within 2 sigma"
                                         if abs(z) <= 2
                                         else "OUTSIDE 2 sigma"))


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
    s_split_control(recs)
    section("THE READER -- one walk over the mapped complex population")
    strata, nfields, bad, base = read_population(
        recs, ECP.DISC_CAP if wide else None)
    print("  [C3] split-prime power triples off zero-sum: %d" % bad)
    ok(bad == 0, "%d power triples do not sum to zero" % bad)
    print("  [C4] the place above 2: the map's vectors disagreeing modulo"
          " the lattice: %d" % TWO['disagree'])
    ok(TWO['disagree'] == 0, "%d disagreements at the place above 2"
       % TWO['disagree'])
    print("  [P4] h = 3: the exact 3-part test against the parents'"
          " regime: %d agree, %d disagree"
          % (REGIME['agree'], REGIME['disagree']))
    if wide:
        print("  C1 below reads the parents' box |d| <= %d inside the wide"
              " population; the strata after it read the whole of it"
              % ECP.DISC_CAP)
    s_reproduce(base if wide else strata)
    s_levels(strata, nfields, base)
    s_cube(strata, nfields)
    s_equal(strata, nfields)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall%s"
          % (CHECKS, time.time() - t0, "  (--wide)" if wide else ""))


if __name__ == "__main__":
    main()
