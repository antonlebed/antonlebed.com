r"""ARE THE TWO MECHANISMS THE TRIPLE CORPUS NAMES ONE MECHANISM? -- the
all-equal triple count is short of the uniform model and the shortfall
DEEPENS with the class number, the principal share is short too, and a
coincidence suppression and a principality shortfall are both said to be
present and to pull opposite ways on the share, with neither one sized.

THE FINDING THIS ANSWERS, stated twice in the same file.
explore_cubic_split_triple.py F3: the all-equal triple count over complex
cubic fields, weighed against its own event count, reads 498 against 580.0
at h = 2, 12 against 27.5 at h = 4, 6 against 19.2 at h = 5, 8 against 11.6
at h = 6 and 1 against 3.0 at h = 7 -- three of the five carrying a reading
and running 0.86, 0.44, 0.31, a shortfall that GROWS with h. Its own text
names two mechanisms that would push that direction, refuses both, and
leaves it "as measured and open". The same confound stands at h = 3,
where that file's own regime split leaves 45 non-degenerate fields pooling
245 equal triples against 377.0 at z = -6.8, while the principal share
explore_cubic_class_map.py F2 measures over every degree-1-carrying prime
reads 0.432 against its nominal 4/9. Those two cannot both be one
mechanism: suppressing all-equal triples REMOVES two of the three
class-triples carrying no principal place and so RAISES the share, which is
the opposite direction. The missing measurement is named there and not
taken: the split primes carrying a principal place, and the all-principal
triples, separately from the all-equal ones.

WHAT THIS FILE DOES INSTEAD OF THAT COUNTER, AND WHY. The bare counter
prints three numbers and still compares them to a model that has no dial in
it -- uniformity on M is a hypothesis with no free parameter, so every
departure from it reads as one undifferentiated excess. This file makes the
two mechanisms NESTED instead: it gives the uniform model exactly one dial,
the tilt lambda below, whose entire content is HOW OFTEN A PLACE IS
PRINCIPAL, and fits that dial to the measured per-place share rather than
to the statistic under test. What the dial cannot then reach is the
coincidence mechanism, and the residual after the fit is that mechanism's
SIZE -- printed rather than argued. The counter asked for falls out
of the same read and is printed beside it.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The two
mechanisms are written in different units and that is half the confusion.
"Principality shortfall" is a statement about a PLACE -- one degree-1
place, is its class trivial -- and it is the unit the share deficit of
explore_cubic_class_map.py F2 was measured in. "Coincidence suppression" is
a statement about a TRIPLE and has no reading at a single place at all.
This file holds both in the triple's units by making the place-level claim
a parameter OF the triple distribution, which is what the tilt is; and it
carries an independent place-level reading in the place's own units, which
is what the partial primes below are for.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_cubic_split_triple.py: the enumeration, the maximal
    order, the place engines, the class reading, the relation harvest, the
    per-place vector reader (read_field), the principality and
    same-class tests and field_stats are IMPORTED from that file and its
    two parents, not re-implemented. Every control those files run on the
    map rides in unexamined with them, including the fingerprint
    assumption and the inherited index-exactly-p control on a degree-1
    place. The population, the discriminant cap, the prime cap and the
    bin edges are theirs.

 T2 FROM THE F3 READING: the SHAPE under test -- a shortfall deepening
    with h -- is that file's measurement, and the population, the complex
    restriction and the stratification by H are copied so the reproduction
    control below can be exact rather than approximate. What is NOT
    imported is its refusal: F3 rejects the share-deficit explanation on
    the ground that it "would give roughly that factor at every h, not a
    deepening", and that ground is an ARGUMENT about a model nobody wrote
    down. Writing it down is this file's job, and the argument is under
    test rather than assumed.

 T3 FROM THE MODEL SIDE, and it is the one transplant that could void the
    whole read: the tilt is a one-parameter family chosen for being the
    smallest deformation of uniformity that moves the per-place share, NOT
    derived from any arithmetic. It is a NULL with a dial, never a theory
    of the fields. A tilt that reproduces the counts says the counts need
    no mechanism beyond a depressed share; it does not say the share is
    depressed for the tilt's reason, and no such claim is made below.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE TRIPLE AND ITS MODEL. For p odd, unramified and totally split in
      the cubic field K, (p) = P_1 P_2 P_3 with each P_i of residue
      degree 1 and

          [P_1] + [P_2] + [P_3] = 0 in Cl(K),

      so the triple lies in M = {(c_1,c_2,c_3) in Cl^3 : sum = 0}, of order
      h^2, and the uniform model on M is what every reading above is
      against (explore_cubic_split_triple.py derivation (1)).

  (2) THE ZERO COUNT TAKES THREE VALUES AND NOT FOUR. Write z for the
      number of principal places in the triple. If two coordinates vanish
      the third does too, by the sum, so z is 0, 1 or 3 -- never 2. On M
      the three classes are

          z = 3 : one triple, (0,0,0)                      n3 = 1
          z = 1 : a position (3) and a c =/= 0 with the
                  remaining pair (c,-c)                    n1 = 3(h-1)
          z = 0 : the rest                       n0 = (h-1)(h-2)

      and n0 + n1 + n3 = h^2 as it must. The uniform model's
      q_split = P(z >= 1) = (3h-2)/h^2, which is 7/9 at h = 3.

  (3) THE TILT, AND WHY IT IS THE RIGHT ONE DIAL. Weight a triple by
      lambda^z and normalise:

          Z(lambda) = n0 + n1*lambda + lambda^3

      -- the whole family is a single exponential tilt in the statistic
      "how many places here are principal", so lambda is the only thing it
      can say and a depressed principal share is the only departure it can
      express. At lambda = 1 it IS the uniform model: Z(1) = h^2. The three
      quantities this file reads off it are

          per-place share   rho(lambda) = ((h-1)lambda + lambda^3) / Z
          all-principal     P3(lambda)  = lambda^3 / Z
          all-equal         PE(lambda)  = (lambda^3 + t - 1) / Z

      where t = |Cl[3]|: the equal triples are (c,c,c) with 3c = 0, so
      there are t of them, exactly one of which -- c = 0 -- is the
      all-principal one, and the other t - 1 sit at z = 0 where the tilt
      cannot touch them. At lambda = 1 these read 1/h, 1/h^2 and t/h^2,
      which are the three model values the corpus already uses. AND THE
      LAST LINE IS THE WHOLE POINT: at h coprime to 3 we have t = 1, so
      all-equal and all-principal are THE SAME EVENT and F3's coprime
      strata were measuring the all-principal count under another name.

  (4) THE FIT IS WELL POSED, AND THE ATTACK ON ITS ALGEBRA. rho is fitted
      by bisection, so it must be monotone. With a = h - 1 and n0 = a(a-1),

          rho' has the sign of  N'D - ND'
            = (a + 3L^2)(a(a-1) + 3aL + L^3)
              - (aL + L^3)(3a + 3L^2)
            = a^2(a-1) + 3a(a-1)L^2 + 4aL^3,

      every term nonnegative for a >= 1 and the last strictly positive for
      L > 0, so rho is strictly increasing on (0, inf) at every h >= 2.
      Its LIMITS are where the algebra can blow up and they differ by
      stratum: as lambda -> inf, rho -> 1 everywhere; as lambda -> 0+,
      rho -> 0 when n0 > 0, but at h = 2 we have n0 = (1)(0) = 0 and the
      leading terms cancel to rho -> a*lambda / (3a*lambda) = 1/3. SO AT
      h = 2 THE TILT CANNOT REACH A SHARE BELOW 1/3 AT ALL -- every triple
      already carries a principal place there, and no reweighting of them
      changes that. A measured share outside (rho(0+), 1) is not a fitting
      failure to be clipped; it is a finding, and the rig prints it as one
      rather than returning a boundary lambda.

  (5) THE PARTIAL PRIMES ARE THE PLACE-LEVEL CONTROL, AND THEY CARRY NO
      TRIPLE. A prime with splitting shape (1,2) has one degree-1 place P
      and one of residue degree 2, with [P] + [P'] = 0 -- one constraint on
      two classes, so [P] is unconstrained and uniform on Cl under the
      model. Its principal probability is 1/h with no coincidence structure
      in it whatever: there is no second degree-1 place for it to coincide
      with. So the partial share is a reading of the SAME per-place
      quantity the tilt is fitted to, taken where the triple mechanism
      cannot reach, and comparing the two decides whether a depressed share
      is a property of a PLACE or of a TRIPLE. (What is new here is
      measuring the quantity. The uniformity itself was a NOMINAL when
      this file ran and is now derived --
      explore_cubic_transposition.py settles the transposition
      Frobenius and finds the class uniform on the whole group, so the
      comparison below rests on a proved reference rather than an
      assumed one.)

  (6) h = 3 IS TWO POPULATIONS AND THE TILT BELONGS TO ONE OF THEM. The
      uniform model on M is not the null at every h = 3 field:
      explore_cubic_split_triple.py F1 finds the realized triples confined
      to the diagonal D at 38 of the 83 complex fields, where the
      equal-class fraction is 1.000 by arithmetic and not by chance. A
      tilt of the uniform model has nothing to say there -- lambda moves
      the share, and in that regime the share is what the subgroup fixes.
      So every reading below runs on the R = M half, classified exactly as
      the parent classifies it (at least MIN_SPLIT split primes, fraction
      below HIGH_FRAC), which is also the pool the 245 against 377.0
      above is read over. h = 6, the one other stratum where D
      is nontrivial, holds no degenerate field (F3) and is read whole.
      The whole stratum, the two halves and their sum are all printed, so
      the split is auditable rather than asserted.

  (8) WHAT THE SUPPRESSION ALONE PREDICTS FOR q_split, derived here so
      the comparison in F1 rests on this file's own arithmetic. At h = 3
      the three cells of derivation (2) line up with the equal/unequal
      split exactly: n0 = (h-1)(h-2) = 2 and the equal-but-nonzero triples
      number t - 1 = 2, and they are the SAME two -- (1,1,1) and (2,2,2)
      carry no principal place. So at h = 3 the equal class is
      {(0,0,0)} u {the two z = 0 triples} and every unequal triple is
      z = 1. Suppress the equal class to its measured rate e, leave its
      internal 1 : 2 split at the model and leave the unequal triples
      uniform. Then every unequal triple carries and one third of the
      equal mass does:

          q_split = (1 - e) + e/3,

      which at the measured e = 245/1131 = 0.21663 gives 0.8556 against
      the uniform model's 7/9 = 0.7778. That number is what F1 compares
      the measurement to, and it is a prediction of the suppression with
      NO principality shortfall in it at all.

  (7) WHERE THE SHARE DEFICIT ALREADY LIVES, AND WHY EVERY READ IS BINNED.
      explore_cubic_class_map.py F2 locates the principal-share deficit AT
      SMALL p -- short in the bottom bin at every class number and back at
      nominal by the top. A single pooled lambda per stratum would fit that
      p-dependence into one number and then predict a rare joint event with
      it, which is precisely the Jensen error: the all-principal
      probability is convex in the share, so a pooled fit and a binned fit
      do not agree, and the pooled one biases the prediction DOWNWARD --
      toward the measured shortfall, which is the direction that would
      manufacture the answer. The fit is therefore per bin, on the bin
      edges the census already froze, and the predicted counts are summed
      across bins. Bins too thin to fit fall back to the stratum-pooled
      lambda and the rig prints how many events that fallback covers.

THE PREDICTIONS, frozen before any engine code, and the kills stated as
things the rig PRINTS.

  P1  ONE MECHANISM AT h = 2. The binned tilt fitted to the measured
      per-place share reproduces the all-principal count at h = 2 -- the
      one stratum whose event count carries a reading on its own.
      KILLED IF the printed |observed - predicted| / sqrt(predicted)
      exceeds 2 at h = 2.

  P2  THE SHORTFALL IS A PLACE PROPERTY. The measured principal share on
      PARTIAL primes agrees with the measured per-place share on SPLIT
      primes, bin by bin.
      KILLED IF any bin holding at least 100 partial primes and 100 split
      places prints |z| > 2 on the difference of the two shares.

  P3  THE DEEPENING IS THE SHARE DEFICIT SEEN AT A RARER EVENT. The
      predicted all-equal ratios FALL across h = 2, 4, 5 in the same
      direction the measured 0.86, 0.44, 0.31 fall.
      KILLED IF the predicted ratios span less than 0.10 across those
      three strata while the measured ones span more than 0.4 -- which is
      F3's own argument ("roughly that factor at every h, not a
      deepening") holding after the model is written down.

  P4  is not a prediction but the counter the corpus asks for, printed at
      h = 3 where t = 3 makes the two events distinct: the all-principal
      count, the equal-NONZERO count and q_split, each against the uniform
      model and against the fitted tilt. A decomposition cannot be killed;
      it is read after P1 to P3 are weighed.

THE CONTROLS.

  C1. THE POSITIVE CONTROL, RUN BEFORE ANY VERDICT IS READ. The rig
      reproduces F3's five coprime-and-h=6 rows exactly -- split-prime
      counts, equal counts and expectations -- and the 245 equal triples
      against 377.0 over h = 3's R = M half. An
      instrument that cannot restate the measurement it is decomposing has
      no standing to decompose it, and this is checked before P1 to P4
      print. The h = 3 half is checked from BOTH sides: the R = M pool
      against section II, and the R = D pool at an equal-class fraction of
      exactly 1.000, which is what makes the regime classification here
      the parent's and not a near-copy of it.

  C2. THE INHERITED h = 1 PIN, RE-RUN rather than cited, on the same
      stride the parent uses: at a constructively certified h = 1 field
      every place is principal, so every split prime must read z = 3.
      This is the identity where the answer is known in advance and it is
      the control the per-place read rests on.

  C3. THE ZERO COUNT NEVER READS 2, at any split prime of any mapped
      field -- derivation (2) forbids it, and a violation would mean the
      relation lattice is unsaturated in a way that breaks the sum
      identity itself.

  C4. A PARTIAL PRIME CARRIES EXACTLY ONE DEGREE-1 PLACE, asserted rather
      than assumed, since the partial share is a per-place statistic whose
      denominator is that count.

  C5. THE FIT INVERTS. For each fitted cell the rig feeds lambda back
      through rho and checks the result returns the measured share to
      1e-9, and asserts the monotonicity derivation (4) claims by
      evaluating rho at the bracket ends.

  C6. THE TWO SHARES PASS FILTERS OF DIFFERENT STRICTNESS, and this was
      added after the first run printed the gap F3 below reports. A split
      prime enters only when all THREE of its places map; a partial one
      when its single place does. If an unresolved place correlated with
      non-principality the split share would be enriched by the filter
      alone. The rig counts the drops on both sides.

  C7. q_split = 1 AT h = 2 BY ARITHMETIC. Derivation (2) gives
      n0 = (h-1)(h-2) = 0 there, so no triple in M carries zero principal
      places. An identity the population must satisfy exactly, and the
      cheapest available check on the zero count everything here is built
      out of.

FINDINGS.

  F1. THE CONFOUND DISSOLVES ONTO TWO DIFFERENT SPLITTING TYPES, AND NEITHER
      MECHANISM IS WHERE THE POOLED NUMBER PUT IT (observation; h = 3's R = M
      half, 1131 totally split primes). The two mechanisms the corpus could not
      size are not two effects competing on one population. Read separately:
      totally split primes carry a principal place  973 of 1131 = 0.8603,
      against the uniform model's 7/9 = 0.7778  -- ABOVE the model by a factor
      1.106, and derivation (8) says where it should land if the all-equal
      suppression were acting ALONE and nothing else were: 0.8556. Measured
      0.8603, which is 0.45 of the binomial spread at that rate (0.0105) and
      lies on the FAR side of it, not short. So a principality shortfall among
      totally split primes is not merely unmeasured, it is BOUNDED: anything
      above about 0.010 in q_split -- one part in eighty -- would have shown,
      and the sign is wrong for one. The per-place share says the same in the
      second unit, reading 0.3380 where the suppression-only model gives
      exactly 1/3, since scaling the equal class while keeping its internal 1 :
      2 split leaves E[z] = 1. Against that, the partial primes' bottom bin is
      short by two fifths, so the two populations are not close to sharing a
      departure. The shortfall the pooled 0.432 against 4/9 reports is
      therefore the PARTIAL primes', whose single degree-1 place carries no
      triple at all: their share runs 0.1911, 0.2594, 0.2455, 0.3311 across the
      four bins against a model 1/3, short at the bottom and at the model by
      the top -- which is the shape explore_cubic_class_map.py F2 located at
      small p, now located on a splitting TYPE as well. The pooled share was a
      mixture of a population at its model and a population short of it, and a
      mixture is what no single reweighting of the triple distribution could
      produce.

  F2. THE FITTED TILT FAILS WHEREVER IT HAS THE FREEDOM TO, AND THE
      RESIDUAL IS THE COINCIDENCE MECHANISM'S SIZE (observation; P1
      killed at every stratum carrying its criterion, P3 killed). Fitted
      per bin to the measured per-place share, the tilt predicts the
      all-equal and all-principal counts

          h = 3   245 against 377.5   z = -6.8    87 against 131.2  -3.9
          h = 4    12 against  25.9   z = -2.7    12 against  25.9  -2.7
          h = 5     6 against  17.1   z = -2.7     6 against  17.1  -2.7

      -- so a depressed per-place share does not reach these counts, and
      what it leaves is a factor of 0.649, 0.463 and 0.351 at h = 3, 4
      and 5 on the all-equal count. THE DEEPENING IS READ ON ONE
      STATISTIC AND NOT TWO: at h coprime to 3 all-equal and
      all-principal are the same event (t = 1) while at h = 3 they are
      not, so the series that compares like with like is the
      ALL-PRINCIPAL residual -- 0.663, 0.463, 0.351 at h = 3, 4 and 5.
      That residual IS the coincidence mechanism, printed rather than
      argued, and it still DEEPENS with the class number: the deepening
      was never the share deficit's. P3 reads the same fact
      from the other side -- the tilt's predicted ratios span 0.084
      across h = 2, 4, 5 while the measurement spans 0.547 -- which
      vindicates explore_cubic_split_triple.py F3's refusal ("roughly
      that factor at every h, not a deepening") now that the model it
      was arguing about is written down. At h = 6 and 7 the expectations
      are 2.1 and 3.7 and nothing is read.

  F3. A DEGREE-1 PLACE IS MORE OFTEN PRINCIPAL OVER A TOTALLY SPLIT PRIME THAN
      OVER A PARTIAL ONE, AT EQUAL NORM (observation; P2 KILLED). Both
      statistics read places of norm exactly p and both are binned by p, so the
      comparison is norm-matched and needs no model -- it is two measured
      shares differenced, and at h = 3 both are read over the SAME 45 fields,
      so the comparison is matched in the field set as well as in the norm and
      the bin. The worst read cell is h = 3's 100-300 bin at split 0.3473
      against partial 0.2455, z = +4.38, and at h = 3 the split share sits
      within noise of its model at every bin (0.3229, 0.3173, 0.3473, 0.3393
      against 0.3333, the furthest 0.6 of its own spread away) while the
      partial share climbs 0.1911 to 0.3311. THAT CLEANLINESS IS h = 3's AND
      NOT THE RULE: at h = 2, 4 and 5 the split share is short at small p as
      well, just less so than the partial one, so what generalises across the
      strata is the ORDERING of the two and not the split side's innocence. C6
      kills the one artifact that could manufacture this: 0 of 5596 split and 0
      of 18689 partial primes were dropped for an unresolved place, so the two
      filters admitted everything and neither is selecting. The second
      candidate -- the map's saturation gap, which can call a truly principal
      place non-principal -- cannot make a gap either, and for a stronger
      reason than a count: the lattice is echeloned ONCE PER FIELD after every
      prime has contributed, so both shares are read against the SAME span, and
      an unsaturated lattice moves them together. WHAT THE h = 2 ROW CANNOT
      CARRY, and derivation (4) called it before the run: that stratum's
      biggest gap (+4.25, bottom bin) sits ON THE FLOOR -- the split share
      reads 0.3571 against a hard arithmetic floor of 1/3, so it is constrained
      rather than free and the cell is not evidence of anything. The reading
      rests on h = 3, where the floor is 0.

  F4. P1's FROZEN CRITERION NAMED THE ONE STRATUM WHERE IT CANNOT FIRE
      (property, proved; the slate's own defect). P1 chose h = 2 for
      having the only event count that carries a reading alone, and h = 2
      is exactly where n0 = (h-1)(h-2) vanishes, leaving the tilt a
      two-cell support and ZERO residual freedom. There the fit is an
      identity: rho = (ns + 2 n3)/(3 ns) inverts to n3/ns exactly, so the
      printed 498.0 against 498 at z = 0.00 is algebra and not a
      confirmation. A perfect agreement was the tell. The rig prints the
      degrees of freedom per stratum so the saturation is visible, and
      P1's criterion is read at the df = 1 strata instead, where it dies
      at all three. The lesson generalises past this file: a kill
      criterion frozen at the stratum with the most DATA can land on the
      stratum with the least MODEL, and the two are chosen by opposite
      things.

RUN RECORD. `python prime/code/memwatch.py python
prime/code/explore_cubic_zero_tilt.py`. One process, CPython, no BLAS.
54 checks, 221.6 s wall, peak working set 76.7 MB against memwatch's
512 MB ceiling. Enumeration 15370 polynomials -> 1103 fields in 8.0 s;
class reading 1103 fields, 0 unresolved, in ~165 s; the inherited h = 1
pin 62 fields and 1500 split primes in ~22 s; the reader over the mapped
complex population in ~25 s. THE FIRST RUN IS NOT QUOTED ABOVE AND ITS
FAILURE IS THE REASON C1 EXISTS IN THE SHAPE IT DOES: it reproduced
F3's five rows exactly and missed section II's h = 3 pool, because that
pool is the R = M half and the rig was reading the whole stratum. The
decomposition 2023 = 1131 + 892 split and 1137 = 245 + 892 equal, with
the second half at a fraction of exactly 1.000, is what identified the
convention rather than a guess at it, and it is now checked from both
sides.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_principal as ECP
import explore_cubic_class_map as CCM
import explore_cubic_split_triple as ST

CHECKS = 0

BIN_EDGES = ECP.BIN_EDGES
MIN_STRATUM = ST.MIN_STRATUM
MIN_FIT = 30            # split primes a bin needs before it fits its own
MIN_CMP = 100           # events a bin needs before P2 reads it
MIN_SPLIT = ST.MIN_SPLIT        # the parent's per-field reading floor
HIGH_FRAC = ST.HIGH_FRAC        # the parent's R = D threshold
STRATA = (2, 3, 4, 5, 6, 7)

# Derivation (6): every stratum but h = 3 is read whole; h = 3 is read on
# its R = M half, which is the pool section II quotes.
def regime_read(h):
    return 'M' if h == 3 else 'A'

# C1's targets, quoted from the two documents this file decomposes.
F3_ROWS = {2: (498, 580.0), 4: (12, 27.5), 5: (6, 19.2),
           6: (8, 11.6), 7: (1, 3.0)}
SEC_II = (245, 377.0)


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg


def section(t):
    print("\n" + "=" * 68)
    print(t)
    print("=" * 68)


def bin_of(p):
    for i in range(len(BIN_EDGES) - 1):
        if BIN_EDGES[i] <= p < BIN_EDGES[i + 1]:
            return i
    return None


# ------------------------------------------------------- the tilt
def counts(h):
    """(n0, n1, n3, t) of derivation (2) and (3)."""
    return (h - 1) * (h - 2), 3 * (h - 1), 1, (3 if h % 3 == 0 else 1)


def rho(h, lam):
    n0, n1, _, _ = counts(h)
    return ((h - 1) * lam + lam ** 3) / (n0 + n1 * lam + lam ** 3)


def p_all(h, lam):
    """(all-principal, all-equal) under the tilt."""
    n0, n1, _, t = counts(h)
    z = n0 + n1 * lam + lam ** 3
    return lam ** 3 / z, (lam ** 3 + t - 1) / z


def rho_floor(h):
    """rho(0+) of derivation (4): 1/3 where n0 vanishes, else 0."""
    return 1.0 / 3.0 if (h - 1) * (h - 2) == 0 else 0.0


def fit_lambda(h, target):
    """Bisect rho(h, .) = target. Returns None when the target sits
    outside the family's reachable range (derivation (4))."""
    if not (rho_floor(h) < target < 1.0):
        return None
    lo, hi = 1e-12, 1.0
    while rho(h, hi) < target:
        hi *= 2.0
        if hi > 1e12:
            return None
    ok(rho(h, lo) < target < rho(h, hi) + 1e-15,
       "bracket does not straddle at h = %d, target %.6f" % (h, target))
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if rho(h, mid) < target:
            lo = mid
        else:
            hi = mid
    lam = 0.5 * (lo + hi)
    ok(abs(rho(h, lam) - target) < 1e-9,
       "fit does not invert at h = %d: %.12f vs %.12f"
       % (h, rho(h, lam), target))
    return lam


# ------------------------------------------------------- the reader
def read_cells(recs):
    """Walk the mapped population once, keeping the per-place zero count.

    Returns (cells, z2, partial_bad), where cells maps
    (H, regime, bin) -> dict of the counters S3 to S6 read. The regime
    of derivation (6) is 'A' everywhere but h = 3, where a field lands in
    'M', 'D' or 'X' (below the parent's reading floor) by its own
    equal-class fraction -- which is known only once the field is read,
    so a field's bins are accumulated privately and merged after."""
    cells = {}
    z2 = partial_bad = 0
    drop = {'split': 0, 'partial': 0}
    keep = {'split': 0, 'partial': 0}
    t0 = time.time()
    for (d, cx, a, b, c, O, h, kind, gp, rel) in recs:
        if h is None or h == 1 or not cx:
            continue
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        if H is None or H == 1:
            continue
        mine = {}
        for (p, kd, vecs) in per_prime:
            if bin_of(p) is None:
                continue
            if any(v is None for v in vecs):
                if kd in drop:
                    drop[kd] += 1
                continue
            if kd in keep:
                keep[kd] += 1
            b_i = bin_of(p)
            cell = mine.setdefault(b_i, dict(
                ns=0, zsum=0, neq=0, n3=0, neqnz=0, nq=0,
                npart=0, npart_p=0))
            if kd == 'split':
                if len(vecs) != 3:
                    continue
                z = sum(1 for v in vecs if ST.is_principal(v, piv, k))
                if z == 2:
                    z2 += 1
                eq = (ST.same_class(vecs[0], vecs[1], piv, k)
                      and ST.same_class(vecs[0], vecs[2], piv, k))
                cell['ns'] += 1
                cell['zsum'] += z
                cell['nq'] += 1 if z >= 1 else 0
                if eq:
                    cell['neq'] += 1
                if z == 3:
                    cell['n3'] += 1
                elif eq:
                    cell['neqnz'] += 1
            elif kd == 'partial':
                if len(vecs) != 1:
                    partial_bad += 1
                    continue
                cell['npart'] += 1
                cell['npart_p'] += (
                    1 if ST.is_principal(vecs[0], piv, k) else 0)

        # derivation (6): classify the FIELD, then merge its bins
        reg = 'A'
        if H == 3:
            ns = sum(x['ns'] for x in mine.values())
            neq = sum(x['neq'] for x in mine.values())
            if ns < MIN_SPLIT:
                reg = 'X'
            else:
                reg = 'D' if float(neq) / ns >= HIGH_FRAC else 'M'
        for b_i, x in mine.items():
            cell = cells.setdefault((H, reg, b_i), dict(
                ns=0, zsum=0, neq=0, n3=0, neqnz=0, nq=0,
                npart=0, npart_p=0))
            for key in cell:
                cell[key] += x[key]
    print("  the mapped complex population walked in %.1f s, %d cells"
          % (time.time() - t0, len(cells)))
    return cells, z2, partial_bad, drop, keep


def stratum(cells, h, reg=None):
    """The per-bin rows of one stratum-and-regime, plus its totals.
    reg=None pools every regime, which is how the whole h = 3 stratum is
    printed beside its halves."""
    rows = []
    tot = dict(ns=0, zsum=0, neq=0, n3=0, neqnz=0, nq=0,
               npart=0, npart_p=0)
    for b_i in range(len(BIN_EDGES) - 1):
        merged = None
        for (hh, rr, bb), cell in cells.items():
            if hh != h or bb != b_i or (reg is not None and rr != reg):
                continue
            if merged is None:
                merged = dict((key, 0) for key in cell)
            for key in cell:
                merged[key] += cell[key]
        if merged is None:
            continue
        rows.append((b_i, merged))
        for key in tot:
            tot[key] += merged[key]
    return rows, tot


# ------------------------------------------------------- the sections
def s1_population():
    section("S1  THE ENGINE -- enumeration and the class reading (T1)")
    t0 = time.time()
    fields, buckets = ECP.enumerate_fields(ECP.DISC_CAP)
    print("  %d polynomials -> %d fields, %.1f s"
          % (buckets[0], len(fields), time.time() - t0))
    recs = []
    t0 = time.time()
    for (ad, d, cx, polys) in fields:
        a, b, c, O = polys[0]
        rows = ECP.t2_rows(O, a, b, c)
        h, kind, gen_places, rel = CCM.class_and_relations(O, d, cx, rows)
        recs.append((d, cx, a, b, c, O, h, kind, gen_places, rel))
    n_un = sum(1 for r in recs if r[6] is None)
    print("  class reading: %d fields, %d unresolved, %.1f s"
          % (len(recs), n_un, time.time() - t0))
    ok(n_un == 0, "%d fields unresolved" % n_un)
    return recs


def s2_pin(recs):
    section("S2  C2 THE INHERITED h = 1 PIN, RE-RUN -- every split prime "
            "of a certified field must read z = 3")
    sample = [r for i, r in enumerate([x for x in recs if x[7] == 'cert'])
              if i % CCM.PIN_STRIDE == 0]
    bad = n = 0
    t0 = time.time()
    for (d, cx, a, b, c, O, h, kind, gp, rel) in sample:
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        for (p, kd, vecs) in per_prime:
            if kd != 'split' or len(vecs) != 3 or any(v is None
                                                      for v in vecs):
                continue
            n += 1
            if sum(1 for v in vecs
                   if ST.is_principal(v, piv, k)) != 3:
                bad += 1
    print("  [C2] %d certified fields, %d split primes, %d not at z = 3, "
          "%.1f s" % (len(sample), n, bad, time.time() - t0))
    ok(n > 0, "the pin walked no split prime")
    ok(bad == 0, "%d split primes below z = 3 at h = 1" % bad)


def s3_reproduce(cells, z2, partial_bad, drop, keep):
    section("S3  C1 THE POSITIVE CONTROL -- the measurements this file "
            "decomposes, restated before anything is read")
    print("  [C3] split primes whose zero count reads 2, which "
          "derivation (2) forbids: %d" % z2)
    ok(z2 == 0, "%d split primes at z = 2" % z2)
    print("  [C4] partial primes not carrying exactly one degree-1 "
          "place: %d" % partial_bad)
    ok(partial_bad == 0, "%d partial primes with a bad place count"
       % partial_bad)
    # C6, added after the first run printed the split/partial gap: a SPLIT
    # prime is kept only when all THREE of its places map and a PARTIAL one
    # when its single place does, so the two shares pass filters of
    # different strictness. If an unresolved place correlated with
    # non-principality the split share would be enriched by the filter
    # alone, which is the one artifact that could manufacture P2's gap.
    print("  [C6] the inclusion filters the two shares pass: split "
          "%d kept, %d dropped for an unresolved place (%.4f); partial "
          "%d kept, %d dropped (%.4f)"
          % (keep['split'], drop['split'],
             drop['split'] / float(keep['split'] + drop['split'])
             if keep['split'] + drop['split'] else 0.0,
             keep['partial'], drop['partial'],
             drop['partial'] / float(keep['partial'] + drop['partial'])
             if keep['partial'] + drop['partial'] else 0.0))
    print("  %-3s %-6s %-8s %-8s %-10s %-11s %s"
          % ("h", "pool", "split", "equal", "expected", "target",
             "source"))
    bad = 0
    for h in STRATA:
        pools = ([(None, "all"), ('M', "R = M"), ('D', "R = D"),
                  ('X', "thin")] if h == 3 else [(None, "all")])
        for (reg, label) in pools:
            _, tot = stratum(cells, h, reg)
            if not tot['ns']:
                continue
            _, _, _, t = counts(h)
            exp = tot['ns'] * float(t) / (h * h)
            tgt = SEC_II if (h == 3 and reg == 'M') else (
                F3_ROWS.get(h) if h != 3 else None)
            mark = ""
            if tgt is not None:
                if tot['neq'] != tgt[0] or abs(exp - tgt[1]) > 0.05:
                    bad += 1
                    mark = "  MISMATCH"
            print("  %-3d %-6s %-8d %-8d %-10.1f %-11s %s%s"
                  % (h, label, tot['ns'], tot['neq'], exp,
                     ("%d / %.1f" % tgt) if tgt else "--",
                     "sec II pool" if tgt is SEC_II
                     else ("F3" if tgt else "printed"), mark))
    ok(bad == 0, "%d strata fail to reproduce the published reading" % bad)
    # the other side of the same split: R = D is degenerate by arithmetic
    _, dtot = stratum(cells, 3, 'D')
    print("  [C1] the R = D half's equal-class fraction: %d of %d = %.4f "
          "(F1's degenerate regime, 1.0000 by arithmetic)"
          % (dtot['neq'], dtot['ns'],
             float(dtot['neq']) / dtot['ns'] if dtot['ns'] else 0.0))
    ok(dtot['ns'] > 0 and dtot['neq'] == dtot['ns'],
       "R = D half reads %d of %d equal" % (dtot['neq'], dtot['ns']))


def s4_place_control(cells):
    section("S4  P2 THE PLACE-LEVEL CONTROL -- the same per-place share "
            "read where no triple exists")
    print("  split share = principal places / 3 x split primes; partial "
          "share = principal / partial primes; both model 1/h.")
    print("  derivation (4)'s floor is printed beside the model because "
          "it BINDS: at h = 2 no triple carries zero principal places, so "
          "the split share cannot read below 1/3 whatever the arithmetic "
          "does, and a cell sitting on that floor is constrained rather "
          "than free.")
    print("  %-3s %-6s %-9s %-9s %-9s %-9s %-7s %s"
          % ("h", "bin", "places", "split", "partial", "model", "floor",
             "z"))
    worst = None
    for h in STRATA:
        rows, tot = stratum(cells, h, regime_read(h))
        if len(rows) == 0 or tot['ns'] == 0:
            continue
        for (b_i, cell) in rows:
            npl = 3 * cell['ns']
            if npl == 0 or cell['npart'] == 0:
                continue
            s_sp = float(cell['zsum']) / npl
            s_pa = float(cell['npart_p']) / cell['npart']
            se = (s_sp * (1 - s_sp) / npl
                  + s_pa * (1 - s_pa) / cell['npart']) ** 0.5
            z = (s_sp - s_pa) / se if se > 0 else 0.0
            read = (cell['npart'] >= MIN_CMP and npl >= MIN_CMP)
            if read and (worst is None or abs(z) > abs(worst[2])):
                worst = (h, b_i, z)
            fl = rho_floor(h)
            near = fl > 0 and s_sp - fl < 0.05
            print("  %-3d %-6s %-9d %-9.4f %-9.4f %-9.4f %-7.4f %s%s%s"
                  % (h, "%d-%d" % (BIN_EDGES[b_i], BIN_EDGES[b_i + 1]),
                     npl, s_sp, s_pa, 1.0 / h, fl, "%+.2f" % z,
                     "  ON THE FLOOR" if near else "",
                     "" if read else "   (not read)"))
    if worst is None:
        print("  no bin carries both counts at the %d-event floor" % MIN_CMP)
    else:
        print("  worst read cell: h = %d, bin %d, z = %+.2f -- P2 %s"
              % (worst[0], worst[1], worst[2],
                 "SURVIVES" if abs(worst[2]) <= 2 else "KILLED"))
    return worst


def s5_tilt(cells):
    section("S5  P1 AND P3 THE FITTED TILT -- one dial, fitted to the "
            "share, predicting the two joint counts")
    print("  lambda is fitted per bin to that bin's measured per-place "
          "share; predicted counts sum across bins. A bin below %d split "
          "primes falls back to the stratum-pooled lambda." % MIN_FIT)
    print("  df is the tilt's own residual freedom: the family's support "
          "has 3 cells where n0 > 0 and 2 where it vanishes, less one for "
          "normalisation and one for the fitted lambda. AT df = 0 THE FIT "
          "IS AN IDENTITY AND PREDICTS NOTHING.")
    print("  %-3s %-3s %-7s %-8s %-8s %-8s %-8s %-8s %s"
          % ("h", "df", "split", "obs eq", "pred eq", "obs 3", "pred 3",
             "unif eq", "z(eq) z(3)"))
    out = {}
    for h in STRATA:
        rows, tot = stratum(cells, h, regime_read(h))
        if tot['ns'] == 0:
            continue
        pooled = fit_lambda(h, float(tot['zsum']) / (3 * tot['ns']))
        pred_e = pred_3 = 0.0
        fallback = unreach = 0
        for (b_i, cell) in rows:
            if cell['ns'] == 0:
                continue
            lam = None
            if cell['ns'] >= MIN_FIT:
                lam = fit_lambda(h, float(cell['zsum']) / (3 * cell['ns']))
            if lam is None:
                if cell['ns'] >= MIN_FIT:
                    unreach += cell['ns']
                else:
                    fallback += cell['ns']
                lam = pooled
            if lam is None:
                continue
            q3, qe = p_all(h, lam)
            pred_e += qe * cell['ns']
            pred_3 += q3 * cell['ns']
        _, _, _, t = counts(h)
        unif_e = tot['ns'] * float(t) / (h * h)
        ze = ((tot['neq'] - pred_e) / pred_e ** 0.5) if pred_e > 0 else 0.0
        z3 = ((tot['n3'] - pred_3) / pred_3 ** 0.5) if pred_3 > 0 else 0.0
        out[h] = dict(ns=tot['ns'], obs_e=tot['neq'], pred_e=pred_e,
                      obs_3=tot['n3'], pred_3=pred_3, unif_e=unif_e,
                      ze=ze, z3=z3, fallback=fallback, unreach=unreach,
                      pooled=pooled)
        df = 1 if (h - 1) * (h - 2) > 0 else 0
        out[h]['df'] = df
        print("  %-3d %-3d %-7d %-8d %-8.1f %-8d %-8.1f %-8.1f %+.1f  "
              "%+.1f%s"
              % (h, df, tot['ns'], tot['neq'], pred_e, tot['n3'], pred_3,
                 unif_e, ze, z3, "   (saturated)" if df == 0 else ""))
        if fallback or unreach:
            print("      %d split primes on the pooled fallback, %d in "
                  "bins whose share leaves the family's range"
                  % (fallback, unreach))
    if 2 in out:
        print("  P1 at h = 2: |obs - pred| / sqrt(pred) on the "
              "all-principal count = %.2f, at df = %d"
              % (abs(out[2]['z3']), out[2]['df']))
        print("      P1 NAMED THE ONE STRATUM WHERE ITS OWN CRITERION "
              "CANNOT FIRE. At h = 2, n0 = (h-1)(h-2) = 0, so the support "
              "is {z = 1, z = 3} and the per-place share determines the "
              "all-principal fraction outright: rho = (ns + 2 n3)/(3 ns) "
              "inverts to n3/ns exactly. The zero above is that identity "
              "and not a confirmation. THE STRATA THAT CARRY A READING "
              "ARE THOSE AT df = 1.")
    live = [h for h in sorted(out) if out[h]['df'] == 1
            and out[h]['pred_3'] >= 5.0]
    if live:
        print("  P1's criterion read where the tilt has a residual "
              "freedom and the expectation carries one: %s"
              % ", ".join("h = %d at z = %+.1f" % (h, out[h]['z3'])
                          for h in live))
        print("      -- %s" % ("SURVIVES" if all(abs(out[h]['z3']) <= 2
                                                 for h in live)
                               else "KILLED at every such stratum"
                               if all(abs(out[h]['z3']) > 2 for h in live)
                               else "mixed"))
    print("  the residual the fitted tilt leaves, which is the "
          "coincidence mechanism's SIZE (observed / predicted):")
    for h in sorted(out):
        if out[h]['pred_e'] > 0:
            print("      h = %d   all-equal %.3f of the tilt's own "
                  "prediction%s"
                  % (h, out[h]['obs_e'] / out[h]['pred_e'],
                     "   (df = 0, no residual by construction)"
                     if out[h]['df'] == 0 else ""))
    trio = [h for h in (2, 4, 5) if h in out and out[h]['unif_e'] > 0]
    if len(trio) == 3:
        pr = [out[h]['pred_e'] / out[h]['unif_e'] for h in trio]
        ms = [out[h]['obs_e'] / out[h]['unif_e'] for h in trio]
        print("  P3 across h = 2, 4, 5: predicted ratios %s (span %.3f), "
              "measured %s (span %.3f) -- %s"
              % (", ".join("%.3f" % x for x in pr), max(pr) - min(pr),
                 ", ".join("%.3f" % x for x in ms), max(ms) - min(ms),
                 "KILLED" if (max(pr) - min(pr) < 0.10
                              and max(ms) - min(ms) > 0.4)
                 else "SURVIVES"))
    return out


def s6_counter(cells, out):
    section("S6  P4 THE COUNTER THE CORPUS ASKS FOR -- h = 3, where the "
            "all-equal and all-principal events come apart")
    rows, tot = stratum(cells, 3, 'M')
    if tot['ns'] == 0:
        print("  no h = 3 stratum in the population")
        return None
    h = 3
    n = tot['ns']
    lam = out.get(3, {}).get('pooled')
    q3u, qeu = p_all(h, 1.0)
    n0, n1, _, t = counts(h)
    qsu = float(n1 + 1) / (h * h)
    print("  the h = 3 complex stratum: %d totally split primes" % n)
    print("  the tilt column here is the STRATUM-POOLED fit, kept for "
          "reading the four events against one dial; derivation (7) is "
          "why the predictions READ in S5 are the per-bin ones instead, "
          "and the two differ (377.1 here against S5's 377.5).")
    print("  %-24s %-9s %-11s %-11s %s"
          % ("event", "observed", "uniform", "tilt (pooled)",
             "obs/uniform"))
    fit = p_all(h, lam) if lam else (None, None)
    qsf = ((n1 * lam + lam ** 3) / (n0 + n1 * lam + lam ** 3)
           if lam else None)
    for (name, obs, mu, mf) in (
            ("all-equal", tot['neq'], qeu * n,
             fit[1] * n if lam else None),
            ("all-principal (0,0,0)", tot['n3'], q3u * n,
             fit[0] * n if lam else None),
            ("equal and nonzero", tot['neqnz'], (t - 1) * n / float(h * h),
             (t - 1) * n / (n0 + n1 * lam + lam ** 3) if lam else None),
            ("carries a principal", tot['nq'], qsu * n,
             qsf * n if lam else None)):
        print("  %-24s %-9d %-11.1f %-11s %.3f"
              % (name, obs, mu, "%.1f" % mf if mf is not None else "--",
                 obs / mu if mu else 0.0))
    print("  per-place principal share %.4f against the model's %.4f"
          % (float(tot['zsum']) / (3 * n), 1.0 / h))
    supp = tot['neq'] / float(n)
    print("  derivation (8): the all-equal suppression acting ALONE, at "
          "the measured equal rate %.5f, carries q_split to %.4f from the "
          "model's 7/9 = %.4f. Measured here: %.4f."
          % (supp, (1.0 - supp) + supp / 3.0, qsu, tot['nq'] / float(n)))
    # C7: derivation (2) at h = 2 gives n0 = 0, so EVERY triple carries a
    # principal place and q_split is 1 by arithmetic. An identity the
    # population must satisfy exactly, and the cheapest check on the
    # zero count the whole file is built out of.
    _, t2 = stratum(cells, 2, 'A')
    print("  [C7] h = 2 has n0 = 0, so q_split = 1 identically: %d of %d "
          "split primes carry a principal place" % (t2['nq'], t2['ns']))
    ok(t2['ns'] > 0 and t2['nq'] == t2['ns'],
       "h = 2 reads %d of %d carrying" % (t2['nq'], t2['ns']))
    return tot


def main():
    t0 = time.time()
    recs = s1_population()
    s2_pin(recs)
    section("THE READER -- one walk over the mapped complex population")
    cells, z2, partial_bad, drop, keep = read_cells(recs)
    s3_reproduce(cells, z2, partial_bad, drop, keep)
    s4_place_control(cells)
    out = s5_tilt(cells)
    s6_counter(cells, out)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
