r"""DOES THE TOP-BAND ASYMMETRY SURVIVE A QUADRUPLED CUBIC POPULATION?
-- the curve comparison (explore_ceiling_curve.py F5) left one place
where the two generator ceilings part company on their own baselines: in
the band 630 <= p < 1000, degree 2 reads 1.043 +- 0.010 -- above 1 by
four sigma -- while degree 3 reads 0.963 +- 0.040, consistent with 1, as
if the cubic surplus exhausts inside the shared range while degree 2's
persists past it. The joint difference is +1.93 sigma and decides
nothing, and the degree-3 bar is set by population: the two readable
curve strata hold 24 fields at the parents' discriminant cap of 6000.
This file widens ONLY the discriminant cap and reads the same band with
the same frozen machinery.

WHAT RIDES ON THE ANSWER. If the two levels separate at 3 sigma, the
"one shared decay" verdict fractures exactly where it was recorded as
weakest, and the ceiling is not one law of the class group across
degrees: degree 2 would keep a surplus at primes where degree 3 has
none. If the enlarged degree-3 point rises to degree 2's and the bar
halves, the asymmetry was the 24-field population's noise and the
one-curve reading strengthens. Both outcomes are worth the run.

THE CAP IS CHOSEN BY POPULATION ARITHMETIC, NOT BY THE PHENOMENON. A
scratch enumeration at cap 12000 counted the increment 6000 < |d| <=
12000: 960 new complex cubic fields, of which 26 land at h = 4, 13 at
h = 6, 5 at h = 8 before the cyclic-profile and admissibility filters --
roughly one more 24-field stratum population per 6000 of cap, with the
high-h share rising. Quadrupling the strata therefore asks for
WIDE_CAP = 24000, and quadrupling the band's expected generator count
halves the bar: at an unchanged separation of 0.080 the joint error
0.010 (+) 0.020 puts the difference near 3.6 of its sigma, so the design
can decide, in either direction, what the parent could only record. The
class reading measured 0.12 s a field on the increment with 3 of 960
unresolved, which prices the run and fixes the unresolved policy below
before any wide field is read.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 EVERYTHING RIDES IN. The enumeration, maximal order, class reading,
    relation harvest, the h = 1 pin, the order profiles and the
    per-place reader are explore_cubic_transposition.py's chain
    (explore_cubic_principal.py, explore_cubic_class_map.py,
    explore_cubic_split_triple.py); the population build, admissibility,
    frozen-strata rule, stratum cells, curve and excess estimators, the
    dispersion scale, the band read, the synthetic controls and the
    degree-2 side are explore_ceiling_curve.py's, imported as functions
    and not re-implemented. The parents' own checks run wherever their
    sections run.

 T2 THE PRIME CAP DOES NOT MOVE. Only the DISCRIMINANT cap widens; every
    place still lives at p < 1000 on the degree-3 side, so the band
    edges, the cut ladder and the degree-2 population are byte-identical
    to the parent's. A wider prime cap would move the question; a wider
    discriminant cap only re-asks it louder.

 T3 THE FROZEN-STRATA RULE IS THE LAW, NOT THE STRATUM SET. At the wide
    population more strata may clear MIN_CELL (h = 8 was priced out at
    the base cap; h = 9 enters the enumeration in the increment). The
    primary read applies the parent's rule to the wide population and
    takes whatever strata it admits; the like-for-like read restricted
    to the base strata h = 4, 6 is printed BESIDE it, so a shift caused
    by new strata is separable from a shift caused by new fields.

 T5 ONE ENGINE LINE IS SWAPPED, AND THE SWAP IS THE PARENT'S OWN MOVE
    REPEATED. The parent widened the shop's index-prime sieve (300 to
    1000) because its Hunter box outgrew the shop's discriminant guard;
    the box at cap 24000 outgrows the parent's in turn -- its largest
    polynomial discriminant is 1,849,700 against the parent's 10^6
    guard, measured over the whole box before this file ran. This file
    installs the same routine with the sieve at 2000 and the guard at
    4 * 10^6 (p^2 dividing a discriminant under that needs p <= 2000),
    which is byte-identical in behaviour below 10^6: the sieve loop
    breaks at p^2 > |d0| long before either bound differs.

 T6 ONE SHOP ROUTINE IS REPLACED, SAME LATTICES BY CONSTRUCTION, AND
    SELF-CHECKED. The shop's place_valuation builds the ideal-power
    ladder P, P^2, ... by repeated ideal multiplication whose HNF
    reduction lets pivot entries grow multiplicatively: at one wide
    field (d = -13924) a single box element of norm 2^19 walked that
    ladder to depth 19 and spent 503 s inside xgcd on integers of some
    10^5 digits -- profiled, not guessed. The installed version does
    two things. It memoizes each (order, ideal) ladder so it is built
    once per field rather than per element; and it builds each rung
    with entries pre-reduced mod D = det(A) * det(B) after adjoining
    the generators D*e_i, which lie in the product lattice because D is
    its index (N(AB) = N(A)N(B) in the maximal order), so the reduction
    changes no lattice while capping every xgcd operand at D. The
    installed version re-runs the shop's original on its first 20,000
    calls, asserting equality call by call, and every harvest row is
    further checked by the shop's own per-element checksum, which
    requires the place valuations to sum against v_p(N) exactly.

 T7 THE SECOND BLOWUP, ONE LEVEL UP, SAME DISEASE, SAME CURE. With T6
    in place a second wide field (one of the two at d = -14703) still
    spent over 20 minutes in its class reading -- profiled to
    hermite_order, whose batch elimination over a 400-row relation
    matrix lets the not-yet-processed columns swell exactly as the
    ideal ladder did. The installed version builds the triangular
    basis by ROW INSERTION: each incoming row is folded in by
    unimodular two-row gcd steps (the 2x2 block [[x, y], [-w, u]] with
    xu + yw = 1, so the row lattice never changes), and every insertion
    is followed by a full off-diagonal reduction, which keeps every
    entry bounded near the current determinant -- the class number's
    size, not its exponential. Same lattice, same order, None on the
    same rank deficiency; cross-checked against the shop's original on
    its first 300 calls.

 T8 THE PIN'S HARVEST IS COMPLETED, NOT TRUSTED. The h = 1 positive
    control reads each sampled certified field through a relation
    lattice the shop harvests at its first rung only -- and that rung
    can return a lattice of FULL RANK but PROPER INDEX, which the
    shop's escalation never catches because it fires on rank
    deficiency alone. One base-population field (d = -771, outside the
    parents' own thinner pin sample) does exactly that: its rung-one
    lattice reads H = 2 against a proved h = 1, and one partial place
    then reads non-principal -- the pin fired on the wide sample and
    this is what it caught. Since a certified field's lattice must
    read 1, this file pre-harvests each SAMPLED certified field with
    the escalation keyed on the ORDER rather than the rank, stores the
    completed lattice where the reader will find it, and kills if any
    certified field's lattice still reads above 1 at the deepest rung.
    Certified fields' lattices feed nothing but this control, so the
    sample is the whole exposure.

 T9 THE MEMORY DIET, both moves lattice-preserving. A harvested
    relation set is stored as its REDUCED BASIS (the T7 insertion's own
    k x k triangle) rather than as hundreds of raw rows -- the same
    lattice, which is the only thing any reader consumes -- and the T6
    ladder cache is scoped to the field being read, since no ladder is
    ever consulted across fields. Without either, 4868 fields' raw
    rows plus every field's dead ladders crossed memwatch's 512 MB
    line mid-run (killed at 514 MB commit, the run record's first
    attempt); with them the peak drops by the raw rows' whole volume.

 T10 THE READING MUST NOT DEPEND ON THE REPRESENTATIVE POLYNOMIAL, AND
    THE WIDE BOX PROVED IT CAN. The wider Hunter box visits (s2, s3) in
    a different order, so 665 of the 1103 base records surface a
    DIFFERENT representative polynomial -- and through five of those
    (all with |c| = 121-class coefficients) the first harvest rung
    returned a lattice of full rank but index 2 short, reading h
    DOUBLED: 2 as 4, 4 as 8. The shop's escalation fires on rank
    deficiency alone and can never see this. Two moves close it.
    First, the base population is enumerated from the parents' own
    cap-6000 box, so its representatives and readings ride in
    byte-identical (Hunter's bound puts every base field in that box).
    Second, every non-certified field's order must AGREE ACROSS TWO
    CONSECUTIVE HARVEST RUNGS -- a shy lattice at one rung must
    reproduce its shyness at a strictly larger box to be believed, and
    the five specimens all heal at the second rung and hold at the
    third. A field with no two agreeing rungs on any representative
    is excluded under the T4 kill accounting. The certification path
    (exhibited generators under the Minkowski bound) is copied from
    the class map verbatim. A doubly-shy lattice, short by the same
    index at two boxes, slips through the rung agreement alone, and
    the base subset -- where the truth is the parent's -- is the
    measured control on that residual; T11 is its cure.

 T11 A LADDER READING IS ATTESTED THROUGH THE FIELD'S OTHER
    REPRESENTATIVES, AND A FLIP RESOLVES BY DIVISIBILITY -- the cure
    explore_ceiling_fourthcell.py runs, carried back here, adopted
    after explore_rank2_hunt.py measured the T10 residual firing in a
    wider box: on that box's representatives the two-rung rule
    inflated 11 of 4825 ladders and refused 11 more, and that reader
    counted two of this file's excluded fields (|d| = 7699, 7771) as
    readable -- off a single settled rung, which F5 below refuses on
    every representative. The rung agreement is
    a property of the PRESENTATION while the class number is the
    field's, and the algebra is one-sided: a settled Hermite order is
    the index of a sublattice of the full relation lattice, hence a
    MULTIPLE of the true class number, so the truth divides every
    settled reading and a gcd across representatives is exact where a
    minimum is only monotone. Three moves, all at the reading. The
    read walks the field's representatives in turn and excludes only
    when every one fails. Every non-certified reading above 1 is then
    put to up to four further representatives, stopping at the first
    agreement -- every reading above 1 and not only the
    composite ones the sibling attests, since an uncertified h = 1
    field can read a prime. On disagreement the gcd of the settled
    readings is adopted when some representative settled at exactly
    it, that representative's whole read (order, generators, lattice)
    riding forward since everything downstream is computed against
    the adopted lattice; the field is excluded and printed when none
    did. A reading with no settled sibling is counted as unconfirmed
    and never silently trusted. Readings of exactly 1 are exact floors
    and are not attested. The counts print: fields read through a
    later representative, sibling-confirmed, without a settled
    sibling, flips resolved, unattested and excluded.

 T4 THE EXCLUSION POLICY, fixed before any wide field is read. A field
    is EXCLUDED, its discriminant printed, when the three-rung ladder
    (boxes 10, 16, 22; caps 400, 1500, 4000) ends with no two
    consecutive readings agreeing on any of its representatives (T10)
    -- rank-deficient throughout included -- or when its
    representatives' settled readings disagree and none settles at
    their gcd (T11). The exclusion is a population edit, so it carries
    a kill: more than 1% of the complex population excluded kills the
    run, the excluded fields' class numbers being unknown exactly
    where the population is being weighed.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE BAR'S ALGEBRA. The band level is a pooled ratio obs/exp over
      the readable strata, bar = scale * sqrt((1-q)/exp) per stratum,
      inverse-variance combined; exp grows linearly in the admitted
      field count at fixed splitting density, so the bar falls as
      1/sqrt(N) and 4x the population halves it. Nothing else in the
      statistic moves with the cap: q = phi(h)/h is per-stratum, the
      dispersion scale is measured per view, and the degree-2 side is
      untouched, so the joint z moves only through the degree-3 bar
      and point.

  (2) THE FREEZE PORTS UNCHANGED. Admissibility (>= MIN_TOT = 10
      partial places below 250, cyclic profile) is priced at the
      SMALLEST cut, so it cannot move with the band; the stratum set is
      frozen at the smallest cut and required in every band, exactly
      the parent's derivation (1). The wide population is frozen by the
      same two sentences with more fields in them.

  (3) THE BASE SUBSET IS A DERIVED CONTROL. The chain is deterministic,
      so re-running it on the |d| <= 6000 subset must REPRINT the
      parent's frozen figures -- cumulative 1.246, 1.201, 1.163, 1.096,
      top band 0.963 +- 0.040, 227 admissible fields, band strata
      {4, 6} -- to print precision. A base subset that fails to reprint
      means the riding-in changed something, and no wide figure is
      readable over it.

  (4) THE INCREMENT IS AN INDEPENDENT SAMPLE. Fields with 6000 < |d| <=
      24000 share no field with the parent's population, so their own
      curve is an out-of-sample replication of the decay, not a
      re-read: its four cumulative points and its top band print under
      their own freeze. The wide read and the increment read answer
      different questions -- precision and replication -- and both are
      kept.

  (5) INDEX CONVENTION, re-derived from the engine. Places are (p, key)
      pairs sorted by p; stratum_cells(fields, lo, hi) reads
      lo <= p < hi, so the top band [630, 1000) is half-open and
      matches the parent's cut ladder ending at 1000 with PRIME_CAP
      excluding 1000 itself.

THE PREDICTIONS, frozen before the engine ran. Every kill is a PRINT.

 P1 THE BASE REPRINTS: the |d| <= 6000 subset prints 227 admissible
    fields, band strata [4, 6], the four cumulative levels within
    0.0015 of 1.246, 1.201, 1.163, 1.096 and the top band within
    0.0015 of 0.963 with se within 0.0015 of 0.040.

 P2 THE POPULATION ARITHMETIC LANDS: the wide top-band expected
    generator count over the primary strata is at least 3x the base's.

 P3 THE VERDICT PRINT: the wide degree-3 top-band level and se, the
    degree-2 top band (unchanged), and the joint z -- plus the same
    z restricted to the base strata h = 4, 6 (T3). The meaning is
    weighed after the run; the print is the deliverable.

 P4 THE INCREMENT REPLICATES OR REFUSES: its own four cumulative
    levels, printed with bars, and whether each successive level is
    lower; its own top-band level beside them.

 P5 THE CONTROLS HOLD AT THE WIDE POPULATION: the uniform synthetic
    reads within 0.08 of 1 at both end cuts with no decay wider than
    0.08; the planted control reads its 1.30 plant within 0.06 at the
    smallest cut, non-increasing along the ladder, and within 0.06 of
    1.00 in the top band.

 P6 NEITHER THE FLOOR NOR THE ESTIMATOR CARRIES THE VERDICT: the
    MIN_TOT = 20 re-read moves the top-band z by less than 1 sigma of
    the primary read, and the per-field mean sits within 0.02 of the
    pooled level at the top band.

THE FINDINGS.

 F1 THE TWO CEILINGS SEPARATE IN THE TOP SHARED BAND (observation).
    Over 630 <= p < 1000 the degree-2 generator level reads
    1.0426 +- 0.0101 and the wide degree-3 level 0.9780 +- 0.0123 --
    a joint z of +4.05, over six readable strata h = 4, 6, 8, 9, 10,
    12 and 1274 admissible fields. Restricted to the base strata
    h = 4, 6 the z is +3.29, so the separation is not the new
    strata's; at MIN_TOT = 20 it is +3.96, so not the floor's; and
    the per-field mean sits within 0.005 of the pooled level, so not
    the estimator's. The parent's recorded +1.93 was this separation
    read through a 24-field blur.

 F2 THE DEGREE-3 SURPLUS EXHAUSTS WITHIN THE SHARED RANGE, THE
    DEGREE-2 SURPLUS DOES NOT (observation). The wide degree-3 top
    band sits 1.8 of its sigma below 1 -- consistent with no surplus
    at all -- while degree 2's sits four of its own above. The two
    curves agree along the lower cuts and part company exactly where
    the primes outgrow this degree's surplus, so the two ceilings are
    not one curve: what survives the separation is consistency of the
    decay along the lower cuts, and nothing here establishes a shared
    shape beyond that consistency.

 F3 THE SEPARATION HOLDS ON THE DISJOINT SAMPLE ALONE (observation).
    The increment population -- 1047 admissible fields, none shared
    with the parent's -- prints its own monotone decay 1.132, 1.102,
    1.072, 1.041 over the shared cuts, replicating the curve out of
    sample, and its own top band 0.9773 +- 0.0130, which against the
    degree-2 band is +3.97 with no nesting anywhere.

 F4 THE FIRST NON-CYCLIC CUBIC CLASS GROUPS IN THIS CORPUS
    (observation). The wide population surfaces 5 fields at h = 4
    with order profile {1:1, 2:3} (Z/2 x Z/2) and 4 at h = 8 with
    {1:1, 2:3, 4:4} (Z/2 x Z/4); the admissibility rule prices them
    out of every curve, as frozen, and the profile control reads them
    as valid groups.

 F5 THE CENSUS STANDS UNDER ATTESTATION (observation; the T11 port,
    run after the four findings above were frozen). With every reading
    above 1 put to the field's other representatives, the box reprints
    4865 fields kept, 1367 with h > 1 and the same three excluded:
    1042 readings sibling-confirmed, 325 with no sibling settling --
    which stand on the two-rung rule alone, the T10 residual still
    open at exactly those, though explore_rank2_hunt.py S3b re-read
    this sub-box through a wider box's representatives (a different
    first polynomial at most fields) and changed no class number -- 0
    flips, 0 excluded on a disagreement no representative attests, 0
    fields read through a later representative, and the three excluded
    fields read through NO representative in this box. Every frozen
    figure above reprints to the printed digit. The sibling reader that
    counted this census
    short by two fields (explore_rank2_hunt.py F7) believes a single
    settled rung -- a multiple of the truth -- where this rule wants
    two; its two "returning" fields are refused here on every
    representative, so the census was never short.

THE PREDICTIONS, WEIGHED.

 P1 PASSES EXACTLY: the base subset reprints 1.2457, 1.2012, 1.1625,
    1.0959 cumulative and 0.9631 +- 0.0399 in the top band, 227
    admissible, strata [4, 6].
 P2 PASSES at 9.52x the base's top-band expectation (needed 3x); the
    bar fell 0.040 to 0.012.
 P3 THE PRINT: z = +4.05 primary, +3.29 like-for-like -- the frozen
    3-sigma line is crossed in both readings, and the meaning weighed
    here is F1/F2.
 P4 PASSES: the increment's four cumulative levels are strictly
    decreasing.
 P5 PASSES: uniform reads 1.0006 to 1.0031 everywhere read; the plant
    reads 1.2599, 1.2763, 1.2321, 1.1681 along the ladder --
    non-increasing within the frozen 0.02 slack, the second point
    rising 0.016 above the first -- and 1.0337 in the top band.
 P6 PASSES: the floor moves the z by 0.09; the estimator gap is
    0.0048.

RUN RECORD. 2026-08-25, Windows 11, Python 3, `python
prime/code/memwatch.py python prime/code/explore_ceiling_topband.py`,
the T11 port in place. One process, CPython, no BLAS. 188 checks here
and 8 in the imported degree-3 chain, 1149.2 s wall (960 s of it the
attested class reading; the 2026-08-18 run without attestation took
876.6 s in all), peak working set 205.7 MB against memwatch's 512 MB
ceiling. 4865 of 4868 fields kept; 3 excluded under T4 (discriminants
-7699, -7771, -23928 -- the kill asserted the share under 1% and the
run passed); 1283 mapped complex fields with H > 1; the pin 167 fields
and 13635 partial places with 0 failures, 9 sample lattices needing a
deeper rung (T8). F1-F4 and the weighed predictions are the 2026-08-18
run's prints and this run reprinted every one of them. The port was
REHEARSED first under TB_REHEARSE (the base box alone, 174 s, 52 MB:
P1 reprinting exactly with attestation on, 176 confirmed and 60 lone),
and the first full run with it crashed AFTER the science print on a
name the rehearsal's early exit never reached -- a rehearsal that
returns before a stage cannot exercise it; the file was swept for
undefined names statically before the rerun. EARLIER ATTEMPTS, all
before any science print: one killed by memwatch at 514 MB commit
(T9's cause), one stopped by the pin reading 1 of 13635 places
non-principal (T8's catch), one stopped by the base subset reading 225
of 227 (T10's catch), and two runs abandoned to profiling when single
fields ran minutes to hours (T6's and T7's causes, the 503-second
element and the 20-minute relation matrix). Every failure became a
flag above."""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from collections import defaultdict
from math import gcd

sys.stdout.reconfigure(line_buffering=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_principal as ECP
import explore_cubic_class_map as CCM
import explore_cubic_field_shop as CFS
import explore_cubic_transposition as XT
import explore_ceiling_curve as EC
import explore_class_order as CO
from explore_principal_share import primes_upto

CHECKS = 0

WIDE_CAP = 24000                  # chosen by the probe arithmetic above
BASE_CAP = ECP.DISC_CAP           # the parents' 6000, the control subset
CUTS = EC.CUTS
BANDS = EC.BANDS
TOP = BANDS[-1]                   # (630, 1000)
MIN_TOT = EC.MIN_TOT
MIN_TOT_HARD = EC.MIN_TOT_HARD
MIN_CELL = EC.MIN_CELL
UNRESOLVED_KILL = 0.01            # T4: excluded share that kills the run
ATTEST_MAX = 4                    # T11: further representatives read
REHEARSE = bool(os.environ.get("TB_REHEARSE"))   # base box, P1 only
if REHEARSE:
    WIDE_CAP = BASE_CAP

BASE_CUM = (1.246, 1.201, 1.163, 1.096)   # the parent's frozen prints
BASE_TOP = (0.963, 0.040)
REPRINT_TOL = 0.0015

WIDE_SIEVE = ECP.CR._sieve(2000)  # T5: index primes for the wide box


def maximal_order3_wide(a, b, c):
    """T5: the parent's routine with the sieve widened to the wide box's
    measured discriminant range (max 1,849,700 over the cap-24000 box);
    identical below 10^6, where the loop breaks before the bounds part."""
    R = (-c, -b, -a)
    trvec = (3, -a, a * a - 2 * b)
    O = CFS.Order(R, trvec, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    d0 = O.trace_form_disc()
    assert abs(d0) < 4 * 10 ** 6, "discriminant out of the widened range"
    for p in WIDE_SIEVE:
        if p * p > abs(d0):
            break
        if d0 % (p * p) == 0:
            O = CFS.p_maximalize(O, p)
    return O, O.trace_form_disc()


ECP.maximal_order3 = maximal_order3_wide  # T5: the declared swap

_PV_ORIG = CFS.place_valuation
_PV_CACHE = {}
_PV_CTRL = [20000]        # T6: calls still cross-checked vs the original


def _ideal_mul_mod(O, A, B):
    """T6: ideal_mul_hnf with every generator entry reduced mod
    D = det(A) * det(B), after adjoining D*e_i -- in the product lattice
    since D is its index -- so the lattice is unchanged and no HNF
    operand outgrows D."""
    n = O.n
    D = 1
    for i in range(n):
        D *= A[i][i] * B[i][i]
    D = abs(D)
    gens = [tuple(x % D for x in O.mul(tuple(A[i]), tuple(B[j])))
            for i in range(n) for j in range(n)]
    gens += [tuple(D if j == i else 0 for j in range(n))
             for i in range(n)]
    return CFS.hnf_red(gens, n)


_PV_OWNER = [None]


def place_valuation_cached(O, v, P, cap):
    """T6: the shop's place_valuation with the power ladder memoized per
    (order, ideal) and built by the mod-det multiplication; the same
    lattices, self-checked against the original for its first calls.
    T9: the cache holds one field at a time -- no ladder is consulted
    across fields, so anything else is dead weight."""
    if _PV_OWNER[0] != id(O):
        _PV_CACHE.clear()
        _PV_OWNER[0] = id(O)
    key = tuple(tuple(r) for r in P)
    lad = _PV_CACHE.get(key)
    if lad is None:
        lad = [P]
        _PV_CACHE[key] = lad
    k = 0
    while k < cap:
        if len(lad) <= k:
            lad.append(_ideal_mul_mod(O, lad[-1], P))
        if CFS.in_lattice(v, lad[k], O.n):
            k += 1
        else:
            break
    if _PV_CTRL[0] > 0:
        _PV_CTRL[0] -= 1
        assert _PV_ORIG(O, v, P, cap) == k, "T6: cached valuation differs"
    return k


CFS.place_valuation = place_valuation_cached  # T6: the declared swap

_HO_ORIG = CFS.hermite_order
_HO_CTRL = [300]          # T7: calls still cross-checked vs the original
_xgcd = ECP.CR.xgcd


def hermite_basis_bounded(rows, k):
    """T7/T9: the bounded insertion's triangular basis itself -- the
    same lattice as the rows, in k rows; None where rank-deficient."""
    basis = [None] * k
    for r0 in rows:
        r = list(r0)
        while True:
            lead = None
            for j in range(k):
                if r[j]:
                    lead = j
                    break
            if lead is None:
                break
            b = basis[lead]
            if b is None:
                basis[lead] = [-t for t in r] if r[lead] < 0 else r
                break
            g, x, y = _xgcd(b[lead], r[lead])
            u, w = b[lead] // g, r[lead] // g
            nb = [x * bi + y * ri for bi, ri in zip(b, r)]
            nr = [u * ri - w * bi for bi, ri in zip(b, r)]
            basis[lead] = [-t for t in nb] if nb[lead] < 0 else nb
            r = nr
        for i in range(k - 1, -1, -1):
            if basis[i] is None:
                continue
            for j in range(i):
                bj = basis[j]
                if bj is not None and bj[i]:
                    q = bj[i] // basis[i][i]
                    if q:
                        basis[j] = [a - q * t
                                    for a, t in zip(bj, basis[i])]
    return basis


def hermite_order_bounded(rows, k):
    """T7: the shop's hermite_order by row insertion with off-diagonal
    reduction after every step -- the same row lattice via unimodular
    2x2 blocks, entries kept near the determinant instead of swelling."""
    if not rows:
        return None if k else 1
    basis = hermite_basis_bounded(rows, k)
    if any(b is None for b in basis):
        out = None
    else:
        out = 1
        for j in range(k):
            out *= abs(basis[j][j])
    if _HO_CTRL[0] > 0:
        _HO_CTRL[0] -= 1
        assert _HO_ORIG(rows, k) == out, "T7: bounded order differs"
    return out


CFS.hermite_order = hermite_order_bounded  # T7: the declared swap


def rel_basis(rows, k):
    """T9: a harvested relation set stored as its reduced basis -- the
    same lattice in k rows; falls back to the raw rows if any column
    lacks a pivot (a rank-deficient set is the caller's signal)."""
    if rows is None:
        return None
    basis = hermite_basis_bounded(rows, k)
    if any(b is None for b in basis):
        return [list(r) for r in rows]
    return [list(b) for b in basis]


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def section(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


RUNGS = ((CFS.REL_BOX, 400), (CFS.REL_BOX + 6, 1500),
         (CFS.REL_BOX + 12, 4000))


def read_one(d, cx, a, b, c, O):
    """(h, kind, gp, rel_or_None) or None when excluded -- the class
    map's certification path verbatim (T10), then the rung ladder with
    the two-consecutive-rungs agreement rule."""
    rows = ECP.t2_rows(O, a, b, c)
    gp = CFS.relation_generators(O)
    mb = CFS.minkowski_bound(d, O.n, cx)
    small = [t for t in CFS.all_places_upto_prime(O, mb)
             if t[0] ** t[2] <= mb]
    if all(ECP.find_gen(O, P, rows, p ** f, cx) is not None
           for (p, e, f, name, P) in small):
        return 1, 'cert', gp, None
    prevH = None
    for (box, cap) in RUNGS:
        rows2 = CFS.harvest_relations(O, gp, box=box, cap=cap)
        H = CFS.hermite_order(rows2, len(gp))
        if H is not None and H == prevH:
            return H, ('relH1' if H == 1 else 'H'), gp, rows2
        prevH = H
    return None


def read_field(d, cx, polys):
    """T10 + T11: one field's reading through its representatives --
    the retry walk, then the attestation of any reading above 1, a
    disagreement resolved by the gcd. Returns (rec, retried, tag): rec
    the record or None when excluded; retried whether a later
    representative than the first supplied it; tag the T11 outcome --
    'excluded' (no representative reads), 'cert' / 'relH1' (exact,
    not attested), 'confirmed', 'lone', 'flip', or 'unattested'
    (settled readings disagree and none settles at their gcd)."""
    got = None
    first = 0
    for first, (a, b, c, O) in enumerate(polys):
        got = read_one(d, cx, a, b, c, O)
        if got is not None:
            break
    if got is None:
        return None, False, 'excluded'
    h, kind, gp, rel = got
    tag = kind
    used = first                                   # the record's source
    if h > 1:
        reads = [(first, (a, b, c, O), got)]
        others = [(j, t) for j, t in enumerate(polys) if j != first]
        for (j, (a2, b2, c2, O2)) in others[:ATTEST_MAX]:
            got2 = read_one(d, cx, a2, b2, c2, O2)
            if got2 is None:
                continue
            reads.append((j, (a2, b2, c2, O2), got2))
            if len(set(r[2][0] for r in reads)) == 1:
                break                              # a sibling agrees
        hs = [r[2][0] for r in reads]
        if len(reads) == 1:
            tag = 'lone'
        elif len(set(hs)) == 1:
            tag = 'confirmed'
        else:
            g = hs[0]
            for x in hs[1:]:
                g = gcd(g, x)
            print("  T11: d=%d settled readings %s, gcd %d" % (d, hs, g))
            if g not in hs:
                return None, first > 0, 'unattested'
            tag = 'flip'
            used, (a, b, c, O), got = next(r for r in reads
                                           if r[2][0] == g)
            h, kind, gp, rel = got
    rec = (d, cx, a, b, c, O, h, kind, gp, rel_basis(rel, len(gp)))
    return rec, used > 0, tag


def wide_class_reading():
    """The parent's S1 loop: the base population from the parents' own
    box (T10), the increment from the wide one, T4 + T10 + T11 policies
    on."""
    t0 = time.time()
    fields6, b6 = ECP.enumerate_fields(BASE_CAP)
    fieldsW, bW = ECP.enumerate_fields(WIDE_CAP)
    fields = fields6 + [f for f in fieldsW if abs(f[1]) > BASE_CAP]
    print("  %d + %d polynomials -> %d base + %d increment fields, "
          "%.1f s" % (b6[0], bW[0], len(fields6),
                      len(fields) - len(fields6), time.time() - t0))
    t0 = time.time()
    recs = []
    excluded = []
    n_cx = n_cx_ex = 0
    n_retry = 0
    tags = defaultdict(int)
    for i, (ad, d, cx, polys) in enumerate(fields):
        if i and i % 500 == 0:
            print("  ... %d/%d fields, %.1f s" % (i, len(fields),
                                                  time.time() - t0))
        if cx:
            n_cx += 1
        rec, retried, tag = read_field(d, cx, polys)
        n_retry += retried
        tags[tag] += 1
        if rec is None:
            excluded.append(d)
            if cx:
                n_cx_ex += 1
            continue
        recs.append(rec)
    n_hi = sum(1 for r in recs if r[6] > 1)
    print("  class reading: %d fields kept (%d through a later "
          "representative), %d with H > 1, %d excluded %s, %.1f s"
          % (len(recs), n_retry, n_hi, len(excluded), excluded,
             time.time() - t0))
    print("  T11: readings above 1 -- %d sibling-confirmed, %d without a "
          "settled sibling, %d flips resolved by the gcd, %d unattested "
          "and excluded; %d fields read through no representative"
          % (tags['confirmed'], tags['lone'], tags['flip'],
             tags['unattested'], tags['excluded']))
    ok(n_cx_ex <= UNRESOLVED_KILL * max(n_cx, 1),
       "T4 kill: %d of %d complex fields unresolved"
       % (n_cx_ex, n_cx))

    # T8: complete the pin sample's lattices, escalating on the ORDER
    pool = [r for r in recs if r[7] == 'cert' and r[1]]
    sample_ids = set(id(r) for r in pool[::XT.PIN_STRIDE])
    t0 = time.time()
    n_deep = 0
    out = []
    for r in recs:
        if id(r) not in sample_ids:
            out.append(r)
            continue
        (d, cx, a, b, c, O, h, kind, gp, rel) = r
        for box, cap in ((CFS.REL_BOX, 400), (CFS.REL_BOX + 6, 1500),
                         (CFS.REL_BOX + 12, 4000)):
            rows2 = CFS.harvest_relations(O, gp, box=box, cap=cap)
            H = CFS.hermite_order(rows2, len(gp))
            if H == 1:
                break
            n_deep += 1
        ok(H == 1, "T8 kill: certified field d=%d reads H=%s at the "
           "deepest rung" % (d, H))
        out.append((d, cx, a, b, c, O, h, kind, gp,
                    rel_basis(rows2, len(gp))))
    print("  T8: %d pin-sample lattices completed, %d needed a deeper "
          "rung, %.1f s" % (len(sample_ids), n_deep, time.time() - t0))
    return out


def split_pop(mapped):
    """(base, increment) populations, built by the parent's builder."""
    base = EC.build_pop3([m for m in mapped if abs(m[0]) <= BASE_CAP])
    inc = EC.build_pop3([m for m in mapped if abs(m[0]) > BASE_CAP])
    full = EC.build_pop3(mapped)
    return base, inc, full


def freeze(pop, floor):
    f = EC.admissible(pop, CUTS[0], floor)
    keep, keepb = EC.frozen_strata(f, CUTS, BANDS)
    return f, keep, keepb


def band_point(fields, keep, lo, hi):
    strata = EC.stratum_cells(fields, lo, hi)
    scale, nsc = EC.within_scale(strata, keep)
    mu, se, pts = EC.curve_point(strata, keep, scale)
    return mu, se, pts, strata


def print_band(tag, mu, se, pts):
    cells = "  ".join("h=%d %.3f+-%.3f" % t for t in pts)
    print("  %s band %d-%d  raw %.4f +- %.4f   %s"
          % (tag, TOP[0], TOP[1], mu, se, cells))


def reprint_base(f_base, kb, kbb):
    """P1: the base subset against the parent's frozen figures."""
    ok(len(f_base) == 227, "base admissible %d != 227" % len(f_base))
    ok(kbb == [4, 6], "base band strata %s != [4, 6]" % kbb)
    cb = EC.read_curve(f_base, kb, CUTS, "base", bands=None)
    for cut, want in zip(CUTS, BASE_CUM):
        ok(abs(cb[cut][0] - want) < REPRINT_TOL,
           "base cut %d reads %.4f against the parent's %.3f"
           % (cut, cb[cut][0], want))
    mu, se, pts, _ = band_point(f_base, kbb, *TOP)
    print_band("base", mu, se, pts)
    ok(abs(mu - BASE_TOP[0]) < REPRINT_TOL and
       abs(se - BASE_TOP[1]) < REPRINT_TOL,
       "base top band %.4f +- %.4f against the parent's %.3f +- %.3f"
       % (mu, se, BASE_TOP[0], BASE_TOP[1]))
    print("  P1: the base subset reprints the parent's frozen figures")
    return cb


def main():
    t0 = time.time()

    section("S1  THE WIDE POPULATION (T1, T4) -- cap %d" % WIDE_CAP)
    recs = wide_class_reading()
    XT.s2_pin(recs)
    mapped = XT.s3_profiles(recs)
    del recs                                 # T9
    pop_base, pop_inc, pop_full = split_pop(mapped)
    del mapped                               # T9
    ok(all(p < 1000 for (h, c, pl) in pop_full for (p, k) in pl),
       "a degree-3 place at or past 1000 (T2)")

    if REHEARSE:
        section("REHEARSAL -- the base box alone, frozen and reprinted")
        f_base, kb, kbb = freeze(pop_base, MIN_TOT)
        print("  base      %4d admissible, cum %s, bands %s"
              % (len(f_base), kb, kbb))
        reprint_base(f_base, kb, kbb)
        print()
        print("%d checks passed here, %.1f s wall" % (CHECKS,
                                                       time.time() - t0))
        return

    section("S2  THE THREE FREEZES (derivations (2), (4))")
    f_base, kb, kbb = freeze(pop_base, MIN_TOT)
    f_inc, ki, kib = freeze(pop_inc, MIN_TOT)
    f_full, kf, kfb = freeze(pop_full, MIN_TOT)
    print("  base      %4d admissible, cum %s, bands %s"
          % (len(f_base), kb, kbb))
    print("  increment %4d admissible, cum %s, bands %s"
          % (len(f_inc), ki, kib))
    print("  wide      %4d admissible, cum %s, bands %s"
          % (len(f_full), kf, kfb))

    section("S3  P1 -- THE BASE SUBSET REPRINTS THE PARENT")
    cb = reprint_base(f_base, kb, kbb)

    section("S4  THE DEGREE-2 SIDE (imported whole, unchanged)")
    plist = primes_upto(CO.PCAP)
    rows, bad, id_bad, c2_bad, c4_bad, law_bad = CO.sweep(-1, plist)
    ok(bad[2] == 0 and bad[3] == 0, "the order walk failed")
    pop2 = EC.build_pop2(rows)
    f2 = EC.admissible(pop2, CUTS[0], CO.MIN_SPLIT)
    cnt2 = defaultdict(int)
    for (h, c, pl) in f2:
        cnt2[h] += 1
    f2 = [(h, c, pl) for (h, c, pl) in f2 if cnt2[h] >= EC.MINSTRAT]
    k2, k2b = EC.frozen_strata(f2, CUTS, BANDS)
    k2 = [h for h in k2 if EC.is_composite(h)]
    k2b = [h for h in k2b if EC.is_composite(h)]
    print("  %d fields after the stratum floor, cum %s, bands %s"
          % (len(f2), k2, k2b))
    mu2, se2, pts2, _ = band_point(f2, k2b, *TOP)
    print_band("deg2", mu2, se2, pts2)

    section("S5  P2 P3 -- THE VERDICT PRINT")
    sb = EC.stratum_cells(f_base, *TOP)
    sw = EC.stratum_cells(f_full, *TOP)
    eb = sum(sb[h]['exp'][h] for h in kbb if h in sb)
    ew = sum(sw[h]['exp'][h] for h in kfb if h in sw)
    print("  top-band expected generator count: base %.1f, wide %.1f "
          "(x%.2f)" % (eb, ew, ew / eb))
    ok(ew >= 3.0 * eb, "P2: the wide expectation is only %.2fx" % (ew / eb))
    muw, sew, ptsw, _ = band_point(f_full, kfb, *TOP)
    print_band("wide", muw, sew, ptsw)
    z = EC.zdiff((mu2, se2), (muw, sew))
    print("  P3 primary: deg2 %.4f +- %.4f vs wide deg3 %.4f +- %.4f, "
          "z = %+.2f" % (mu2, se2, muw, sew, z))
    print("  wide deg3 distance from 1: %+.4f (%.1f of its sigma)"
          % (muw - 1.0, abs(muw - 1.0) / sew))
    mul, sel, ptsl, _ = band_point(f_full, [4, 6], *TOP)
    zl = EC.zdiff((mu2, se2), (mul, sel))
    print_band("wide[4,6]", mul, sel, ptsl)
    print("  P3 like-for-like (base strata): z = %+.2f" % zl)

    section("S6  P4 -- THE INCREMENT ALONE (derivation (4))")
    ok(len(ki) >= 1 and len(kib) >= 1,
       "the increment population has no readable stratum")
    ci = EC.read_curve(f_inc, ki, CUTS, "inc", bands=None)
    lv = [ci[cut][0] for cut in CUTS]
    print("  increment monotone non-increasing: %s"
          % all(lv[i] >= lv[i + 1] for i in range(len(lv) - 1)))
    mui, sei, ptsi, _ = band_point(f_inc, kib, *TOP)
    print_band("inc", mui, sei, ptsi)

    section("S7  THE WIDE CURVE, CUMULATIVE (the decay re-read)")
    cw = EC.read_curve(f_full, kf, CUTS, "wide", bands=None)
    for cut in CUTS:
        print("    cut %4d  wide - base = %+.4f (nested, no z claimed)"
              % (cut, cw[cut][0] - cb[cut][0]))

    section("C4  POSITIVE CONTROL, UNIFORM (wide population)")
    u = EC.synth_uniform(f_full)
    pts_u = {}
    for cut in (CUTS[0], CUTS[-1]):
        strata = EC.stratum_cells(u, 0, cut)
        mu, se, _ = EC.curve_point(strata, kf, 1.0)
        pts_u[cut] = mu
        print("  uniform cut %4d: %.4f" % (cut, mu))
        ok(abs(mu - 1.0) < 0.08, "uniform reads %.4f at %d" % (mu, cut))
    ok(abs(pts_u[CUTS[0]] - pts_u[CUTS[-1]]) < 0.08,
       "uniform curve decays by %.4f"
       % (pts_u[CUTS[0]] - pts_u[CUTS[-1]]))
    strata = EC.stratum_cells(u, *TOP)
    mu, se, _ = EC.curve_point(strata, kf, 1.0)
    print("  uniform top band: %.4f" % mu)
    ok(abs(mu - 1.0) < 0.08, "uniform top band reads %.4f" % mu)

    section("C5  POSITIVE CONTROL, PLANTED DECAY (wide population)")
    pl = EC.synth_planted(f_full)
    vals = []
    for cut in CUTS:
        strata = EC.stratum_cells(pl, 0, cut)
        mu, se, _ = EC.curve_point(strata, kf, 1.0)
        vals.append(mu)
        print("  planted cut %4d: %.4f" % (cut, mu))
    strata = EC.stratum_cells(pl, *TOP)
    mu, se, _ = EC.curve_point(strata, kf, 1.0)
    print("  planted top band: %.4f" % mu)
    ok(abs(vals[0] - EC.PLANT) < 0.06,
       "the plant reads %.4f at the smallest cut" % vals[0])
    ok(all(vals[i] >= vals[i + 1] - 0.02 for i in range(len(vals) - 1)),
       "the planted curve is not non-increasing: %s" % vals)
    ok(abs(mu - 1.0) < 0.06, "the planted top band reads %.4f" % mu)

    section("P6  NEITHER THE FLOOR NOR THE ESTIMATOR")
    f_hard, kh, khb = freeze(pop_full, MIN_TOT_HARD)
    muh, seh, ptsh, sh = band_point(f_hard, khb, *TOP)
    print_band("wide'", muh, seh, ptsh)
    zh = EC.zdiff((mu2, se2), (muh, seh))
    print("  MIN_TOT %d -> %d: %d fields, z = %+.2f (primary %+.2f)"
          % (MIN_TOT, MIN_TOT_HARD, len(f_hard), zh, z))
    ok(abs(zh - z) < 1.0, "P6: the floor moves the z by %.2f" % (zh - z))
    worst = 0.0
    for h in kfb:
        s = sw.get(h)
        if s is None or not s['gpf']:
            continue
        pf = sum(s['gpf']) / len(s['gpf'])
        worst = max(worst, abs(pf - EC.pooled_level(s, h)))
    print("  per-field vs pooled at the top band: largest gap %.4f"
          % worst)
    ok(worst < 0.02, "P6: the estimator gap is %.4f" % worst)

    section("SUMMARY")
    print("  %d checks passed here, %d in the imported degree-3 chain, "
          "%.1f s wall" % (CHECKS, XT.CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
