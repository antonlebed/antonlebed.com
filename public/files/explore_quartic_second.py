r"""THE NON-SQUARE SEAT ON A SECOND POPULATION -- the complex cubic fields
with 24000 < |d| <= 48000, read with the first population's machinery
and never pooled with it (sibling of explore_quartic_seat.py, whose
filter, quartic certificate and table statistics it imports; the class
reading is explore_ceiling_topband.py's chain on a wider box).

THE QUESTION. On the 686 complex cubic fields of 2-rank 1 with |d| <=
24000 the least partial place of a field is a NON-SQUARE in the class
group -- its Frobenius in the S4 quartic field a 4-cycle rather than a
transposition -- 84 times in 100, at h = 2, 4 and 6 alike, graded by the
place's rank and flat in its prime (explore_quartic_seat.py F2-F3).
That is one population's print, and the same file read the rank-1 share
falling with the discriminant at -0.039 +- 0.019 per unit of log|d| -- a
2-sigma slope that, continued, would bring the seat down to the
Chebotarev 1/2 at a finite discriminant and make it a small-field fact
rather than a law. This file reads a DISJOINT second population: every
complex cubic field of 2-rank 1 in the increment 24000 < |d| <= 48000,
which the density of cubic fields prices at about the first population's
size again. Two things are asked of it: does the seat stand at all on
fields the first reading never saw, and does the slope continue, flatten
or reverse with the lever doubled.

THE HAND-ATTACK (pre-engine, on paper).

  (1) THE POPULATION IS DISJOINT BY CONSTRUCTION. The Hunter box at cap
      48000 is enumerated whole, the fields with |d| <= 24000 are
      dropped, and the remainder is read by the first population's
      read_one verbatim -- the certification path at h = 1, the rung
      ladder with the two-consecutive-rungs rule, the 1% unresolved
      kill on the complex fields of the increment. Nothing of the first
      population is re-read: its mapped records come from the cache of
      the first run (QSEAT_CACHE) and enter only as a REPRINT control
      and as the other half of the slope fit, never as part of any
      second-population statistic. The pin sample's lattice completion
      (the topband file's T8) is skipped: it serves the h = 1 certified
      fields, which this reading discards before the filter. One of
      the topband file's two swap controls is retired here: its bounded
      Hermite order is cross-checked against the shop's original on the
      first 300 calls, which the first run spent on base-box fields;
      on the increment the original's entry swell IS the pathology the
      bounded routine replaced -- the field d = -25035 reads in 0.29 s
      bounded and past 50 s inside the control, found by a stack dump
      at the rehearsal -- so the 300-call identity the first run
      certified stands and the counter is zeroed. The valuation-ladder
      control (20000 calls) is cheap on the increment and stays.

  (2) THE ENGINE'S ONE MOVED GUARD. The maximal-order routine sieves
      index primes to 2000 under a 4 x 10^6 guard on the polynomial
      discriminant, sized for the cap-24000 box (its largest 1,849,700).
      The polynomial discriminant of a reduced cubic grows with the
      field discriminant times the index squared, so the cap-48000 box
      may cross 4 x 10^6; the routine is re-installed with the sieve at
      4000 and the guard at 1.6 x 10^7 (p^2 dividing a number below
      that needs p <= 4000), byte-identical below 4 x 10^6 because the
      sieve loop breaks at p^2 > |d0|. The largest polynomial
      discriminant met is printed, so the guard is read and not trusted.

  (3) WHAT THE SLOPE CAN AND CANNOT SAY. The first population's slope is
      a least-squares line through 686 points spread over log|d| from
      about 7.9 to 10.1; the increment adds about as many points over
      10.1 to 10.8. A fall of 0.039 per unit continued over the gap
      between the two populations' mean log|d| -- about 0.9 -- predicts
      the increment's rank-1 share near 0.80 against the first
      population's 0.838 +- 0.014, a difference of one bar, so the
      TWO-SAMPLE contrast alone cannot decide the slope; the UNION fit
      over both populations' rows can, its lever doubled and its bar
      roughly halved. Both are printed; the frozen verdict reads the
      union slope. A share near 1/2 on the increment is a different
      thing from a slope: it is the seat's kill, and it is frozen
      separately.

  (4) EVERY CONTROL OF THE FIRST READING RUNS AGAIN ON THE NEW FIELDS,
      the quartic certificate included: the S4 quartic built from the
      order alone -- a generator of an order-2 ideal's square, a unit,
      the sign of the norm and a congruence mod 4 -- read against the
      records' prediction at every prime to 1000. On the increment the
      ideals are larger and the generator search's float LLL meets its
      norm cap more often, so fewer fields may build; the built share is
      printed and the 80% floor stands. The first full run built 585 of
      840 (70%) and stopped at that floor, 0 disagreements over 96,360
      primes, the misses all box-search misses -- 144 fields with no
      non-square unit in the box of 3, 111 with no generator of I^2
      through box 12; larger fields carry larger units. The box ladders
      are therefore widened HERE ONLY -- units to a box of 8 when 3
      finds no non-square, generators one rung on to 16 -- as arguments
      the sibling's builder takes with its own ladders as defaults, so
      the sibling's record is untouched; the floor is not moved. The
      widening recovered 17 fields (602 of 840, 72%), and a diagnosis
      on five of the unit misses found NO unit at all in boxes to 14 in
      four of them and one with coordinates near 1.6 x 10^6 in the
      fifth: the regulators have outgrown a box search, and a unit
      finder that reads the relation harvest's kernel is a build, not a
      rung. So the floor is made NON-FATAL in this file only, after the
      run and recorded as such: it prints its verdict, the
      disagreement check stays fatal, and P1-P3 -- statistics of the
      class records, not of the quartic -- are read on all 840 fields
      while the certificate covers the 602 built.

THE DESIGN. Enumerate the Hunter box to CAP = 48000; keep |d| > 24000;
class-read each field (read_one); map the complex fields with h > 1
(s3_profiles); filter to 2-rank 1 over the place floor (records_from).
Per field: the non-square indicator of the partial place at ranks 1 to
10, the (p, rank) table, the |d| bands (24000, 36000) and (36000,
48000). The first population's rows are rebuilt from the cache for the
reprint and the union slope. The increment's mapped records are
checkpointed to QSECOND_CACHE after the class reading so that a kill in
the probe never buys the reading again; QSECOND_CAP overrides the cap
for the rehearsal.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE SEAT STANDS ON THE SECOND POPULATION (the promotion event the
      shelf names). Pooled over every 2-rank-1 stratum of the increment
      the non-square excess at rank 1 is at least 0.20 at 3 sigma, and
      the h = 2 stratum's rank-1 excess lies within 2 sigma (bars summed
      in quadrature) of the h = 4 stratum's. An excess under 0.20, or
      one short of 3 sigma, is the KILL: the seat is a small-field fact.
  P2  THE SLOPE. Frozen on the union fit of the rank-1 non-square share
      on log|d| over both populations' rows: FALLING if the slope is at
      least 2 sigma below zero, FLAT if within 2 sigma of zero, RISING
      otherwise. This file's guess, stated as a guess: FALLING at a
      size between 0.02 and 0.05 per unit of log|d|, with P1 standing --
      a finite-discriminant component riding on a seat that does not
      reach 1/2 in any box this machinery can read. The two-sample
      contrast (increment's rank-1 share minus the first population's
      0.838 +- 0.014, frozen) is printed beside it and does not vote.
  P3  THE RANK GRADING REPRODUCES. On the increment's (p, rank) table D
      (rank 1 minus rank >= 2 at fixed p, pooled) is at least 0.05 at 2
      sigma and S (the slope of the rank-1 share on p) is within 2 sigma
      of zero; the ranks 1-3, 4-6 and 7-10 pooled excesses each lie
      within 2 sigma (joint) of the first population's +0.246 +- 0.009,
      +0.136 +- 0.010 and +0.109 +- 0.009. A norm-seated read (|z_D| < 2
      with z_S <= -2) kills the rank reading.

THE CONTROLS, run before any prediction is read.

  C1  THE TRIPLE PARITY on the increment: every split prime's triple has
      1 or 3 classes in 2Cl.
  C2-C4  THE QUARTIC CERTIFICATE on the increment (the sibling's certify):
      every built g irreducible with disc(g) = d_K times a square; one
      real-positive Selmer candidate a square mod 4 in every built field;
      0 disagreements between g mod p and the records; at least 80% of
      the fields built.
  C5  THE REPRINT. The first population's rows, rebuilt from the cache
      through the same imported filter, read rank 1 pooled +0.338 within
      0.003 of the first file's print on 686 fields, and h = 2 +0.341
      within 0.003 on 484.
  C6  THE NULL on the increment: one seeded uniform re-sort of every
      partial place's class; D and S within 3 sigma of zero.
  C7  THE PLANTED SEATS on the increment: the rank plant reads D at 3
      sigma with |z_S| < 2, the norm plant S at -3 sigma with |z_D| < 2.
  C8  THE ENGINE. The 1% unresolved kill on the increment's complex
      fields; no field of the increment carries |d| <= 24000; the
      largest polynomial discriminant met is below the moved guard.

THE FINDINGS (the post-run record; every number is a print of the run).

  THE POPULATION. 200,214 polynomials, 10,141 fields to 48000, 5273 in
  the increment; the largest polynomial discriminant 5,117,339 -- past
  the first box's 4 x 10^6 guard, under the moved one. Class reading
  5266 fields kept, 7 unresolved (d = -29004, -35331, -41860, -41999,
  -45075, -45131, -46700, under the 1% kill), 0.201 s a field; 1692
  mapped complex fields with H > 1, 0 profile, order, span or order-1
  failures over 269,077 places; 866 of even class number, 840 of 2-rank 1
  and all 840 over the place floor: h = 2 (529), 4 (118), 6 (117), 8
  (30), 10 (19), 12 (16), 14 (4), 16 (4), 18 (2), 20 (1), every one
  cyclic. The 2-rank filter dropped the increment's non-cyclic groups:
  Z/2 x Z/2 at h = 4 (17 fields), Z/2 x Z/4 at h = 8 (5), Z/2 x Z/6 at h
  = 12 (2), Z/2 x Z/8 at h = 16 (2); Z/3 x Z/3 at h = 9 (2) is odd.

  CONTROLS. C1: 21,424 split primes, every triple with 1 or 3 classes in
  2Cl. C2-C4: 602 of 840 built (72%, COVERAGE SHORT, hand-attack (4)) --
  105 with no generator of I^2 through box 16, 133 with no non-square
  unit through box 8; the extension generated by the unit alone in 215,
  by u alpha in 198, by alpha in 189; every g irreducible with disc(g) =
  d_K times a square, the pairing identity to 9.7e-15 on three fields;
  exactly one real-positive Selmer candidate a square mod 4 in every
  built field; 99,146 readings of g mod p against the records -- 34,143
  3-cycles, 26,722 4-cycles, 22,893 transpositions, 12,317 double
  transpositions, 3071 identities -- and 0 disagreements, 560 index
  primes skipped. C5: the first population reprints +0.338 +- 0.014 and
  +0.341 +- 0.017 through the imported filter. C6: the null reads D
  +0.020 +- 0.029, S -0.005 +- 0.005. C7: the rank plant D +0.251 +-
  0.029 (8.6 sigma) with S -0.003 +- 0.005, the norm plant S -0.029 +-
  0.005 (-6.1 sigma) with D -0.047 +- 0.029.

  F1  P1 PASSES: THE SEAT STANDS ON THE SECOND POPULATION (observation,
      840 fields none of which the first reading saw). The non-square
      share of the least partial place minus 1/2: pooled +0.300 +- 0.014
      at rank 1 (21.7 sigma); h = 2 +0.307 +- 0.017 (529 fields), h = 4
      +0.322 +- 0.035 (118), 0.4 sigma apart; h = 6 +0.295 +- 0.037, h =
      8 +0.267 +- 0.079; ranks 2 to 6 +0.167, +0.133, +0.120, +0.113,
      +0.090 and rank 10 +0.079 +- 0.017 (4.6 sigma); pooled +0.200 +-
      0.008 over ranks 1-3, +0.108 +- 0.009 over 4-6, +0.094 +- 0.008
      over 7-10. The least partial place is a non-square 80 times in 100.
      The certificate covers 602 of these fields; the 2-part of the other
      238 fields' labels rests on the relation lattice alone.

  F2  P2 READS FALLING, AS GUESSED, AND THE FALL IS LEVEL INSIDE THE
      INCREMENT (observation). The union slope of the rank-1 share on
      log|d| over 1526 fields is -0.034 +- 0.013 per unit (-2.7 sigma; h
      = 2 alone -0.032 +- 0.015, h = 4 -0.031 +- 0.035). Inside the
      increment the slope is -0.009 +- 0.071 and the two bands read
      0.798 +- 0.025 (24000 to 36000) and 0.802 +- 0.024 (36000 to
      48000); the two-sample contrast is 0.800 +- 0.017 (the null's bar)
      against 0.838 +- 0.014, -0.038 +- 0.022, the populations' mean
      log|d| 10.48 and 9.32 -- a gap of 1.16, where the hand-attack
      priced 0.9. With the first population's bands the five
      points run 0.89, 0.86, 0.82, 0.80, 0.80: whatever falls has fallen
      by |d| = 24000 and is level across the next doubling, and the
      fitted line would reach 1/2 only near |d| = 10^8, far outside any
      box this chain reads. A small-field component is real at 2.7 sigma;
      nothing in the data continues it.

  F3  P3 FAILS BY ITS LETTER, AND WHAT FAILS IS THE PROFILE'S LEVEL, NOT
      ITS GRADING (observation). On the increment's (p, rank) table D =
      +0.159 +- 0.029 (5.5 sigma) and S = -0.003 +- 0.005 per unit of p:
      RANK-SEATED by the sibling's frozen letter outright, where the
      first population reached only MIXED (D +0.088 +- 0.034). The rank-1
      share is 0.796, 0.798, 0.873, 0.775, 0.714, 0.758 at p = 3 through
      17; rank 2 0.583 to 0.742; rank >= 4 0.597 +- 0.011 over 29-50
      (2242 places), 0.597 +- 0.010 over 50-100, 0.611 +- 0.027 over
      100-250. But every rank pool sits under the first population's:
      +0.200 against +0.246 (-3.9 sigma), +0.108 against +0.136 (-2.1),
      +0.094 against +0.109 (-1.2) -- 0.046, 0.028 and 0.015 by pooled
      band, the same sign at every rank, which is F2's fall seen across
      the whole profile. So the |d| component is a LEVEL of the profile and the
      grading by rank -- 0.80, 0.67, 0.63, 0.62, 0.61, 0.59 -- is the
      first population's shape one step lower. A totally split prime
      below the least place lowers its share by 0.10 +- 0.10 at p = 5,
      0.06 +- 0.11 at p = 7 and 0.10 +- 0.11 at p = 11, the same hint as
      before and still not a read.

WHAT IS NOT CONTROLLED. The mechanism, as in the sibling. The 238
unbuilt fields carry no certificate and are not excluded. Whether the
level shift is |d| itself or something the increment carries with it --
the Minkowski bound, the number of places below the cut -- is not
separated here; the sibling's generation-conditioned null priced that
confound at a tenth of the excess on the first population and has not
been run on the second.

RUN RECORD. 2026-08-20, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_quartic_second.py`
with QSECOND_CACHE and QSEAT_CACHE set. One process, CPython, no BLAS.
Rehearsed at cap 26000 (432 fields, 67 of 2-rank 1, 141 s), which found
the retired control's stall by a stack dump. The first full run: 1350.2
s wall, peak working set 219.6 MB against the 512 MB ceiling, the class
reading 1060 s and the profiles 134 s of it, stopped at the coverage
floor with 585 of 840 built; the widened boxes (602 built, 100 s) and
then the non-fatal floor were added after it, each run from the
checkpoint. Every number above is the third run's: 1215 checks passed,
101.7 s wall, peak 309.0 MB -- except that the certificate's reading
count stood at the first run's 96,360 (585 fields' worth) until a fourth
run from the checkpoint (101.1 s, peak 309.0 MB, every other statistic
reprinting to the digit) replaced it with the 602 fields' 99,146; the
readings are deterministic under the hash seed, 165 a field.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import pickle
import random
import sys
import time
from collections import defaultdict
from math import log, sqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_field_shop as CFS             # noqa: E402
import explore_cubic_principal as ECP              # noqa: E402
import explore_cubic_transposition as XT           # noqa: E402
import explore_ceiling_topband as TB               # noqa: E402
import explore_ceiling_constant as EC              # noqa: E402
import explore_quartic_seat as QS                  # noqa: E402

CHECKS = 0
SEED = 20886
FIRST_CAP = 24000                      # the first population's box
CAP = int(os.environ.get("QSECOND_CAP", "48000"))
REHEARSAL = CAP < 48000                # a smaller cap: C7 not asserted
BANDS_D = ((FIRST_CAP, 36000), (36000, 48000))
FIRST_RANK1 = (0.838, 0.014)           # the first population, frozen
FIRST_POOLS = {(1, 3): (0.246, 0.009), (4, 6): (0.136, 0.010),
               (7, 10): (0.109, 0.009)}
REPRINT = {'rank1': (0.338, 0.003), 'h2': (0.341, 0.003)}
GUARD = 16 * 10 ** 6                   # the moved polynomial-disc guard
GEN_BOXES = (3, 5, 8, 12, 16)          # the sibling's ladder, one rung on
UNIT_BOXES = (3, 8)                    # the sibling's box, then a wider one
SIEVE = ECP.CR._sieve(4000)
MAXD0 = [0]


def maximal_order3_wider(a, b, c):
    """The topband file's routine with the sieve at 4000 and the guard at
    1.6 x 10^7; identical below 4 x 10^6, where the loop breaks first."""
    R = (-c, -b, -a)
    trvec = (3, -a, a * a - 2 * b)
    O = CFS.Order(R, trvec, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    d0 = O.trace_form_disc()
    assert abs(d0) < GUARD, "polynomial discriminant %d past the guard" % d0
    if abs(d0) > MAXD0[0]:
        MAXD0[0] = abs(d0)
    for p in SIEVE:
        if p * p > abs(d0):
            break
        if d0 % (p * p) == 0:
            O = CFS.p_maximalize(O, p)
    return O, O.trace_form_disc()


ECP.maximal_order3 = maximal_order3_wider      # the declared swap
TB._HO_CTRL[0] = 0        # the retired control (hand-attack (1))


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


section = QS.section
fmt = QS.fmt
mean_se = QS.mean_se
cell_se = QS.cell_se


# ----------------------------------------------------------- the reading
def increment_reading():
    """The topband file's S1 loop on the fields of (FIRST_CAP, CAP]."""
    t0 = time.time()
    fields, b = ECP.enumerate_fields(CAP)
    inc = [f for f in fields if abs(f[1]) > FIRST_CAP]
    print("  %d polynomials -> %d fields to %d, %d in the increment;"
          " largest polynomial discriminant %d; %.1f s"
          % (b[0], len(fields), CAP, len(inc), MAXD0[0], time.time() - t0))
    ok(MAXD0[0] < GUARD, "C8: the moved guard was reached")
    ok(all(abs(f[1]) > FIRST_CAP for f in inc),
       "C8: a first-population field in the increment")
    t0 = time.time()
    recs, excluded = [], []
    n_cx = n_cx_ex = n_kept = 0
    for i, (ad, d, cx, polys) in enumerate(inc):
        if i and i % 500 == 0:
            print("  ... %d/%d fields, %.1f s" % (i, len(inc),
                                                  time.time() - t0))
        a, b_, c, O = polys[0]
        if cx:
            n_cx += 1
        got = TB.read_one(d, cx, a, b_, c, O)
        if got is None:
            excluded.append(d)
            if cx:
                n_cx_ex += 1
            continue
        h, kind, gp, rel = got
        n_kept += 1
        if h > 1 and cx:          # all the profiles read; the rest is weight
            recs.append((d, cx, a, b_, c, O, h, kind, gp,
                         TB.rel_basis(rel, len(gp))))
    dt = time.time() - t0
    print("  class reading: %d fields kept, %d complex with H > 1, %d"
          " excluded unresolved %s, %.1f s (%.3f s a field)"
          % (n_kept, len(recs), len(excluded), excluded, dt,
             dt / max(len(inc), 1)))
    ok(n_cx_ex <= TB.UNRESOLVED_KILL * max(n_cx, 1),
       "C8: %d of %d complex fields unresolved" % (n_cx_ex, n_cx))
    return recs


def mapped_increment():
    cache = os.environ.get("QSECOND_CACHE")
    if cache and os.path.exists(cache):
        with open(cache, "rb") as fh:
            mapped = pickle.load(fh)
        print("  increment's mapped records read from %s" % cache)
        return mapped
    mapped = XT.s3_profiles(increment_reading())
    if cache:
        with open(cache, "wb") as fh:
            pickle.dump(mapped, fh)
        print("  increment's mapped records checkpointed to %s" % cache)
    return mapped


def first_rows():
    cache = os.environ.get("QSEAT_CACHE")
    if not (cache and os.path.exists(cache)):
        print("  no QSEAT_CACHE: the first population is not rebuilt;"
              " C5 and the union slope are not read")
        return None
    with open(cache, "rb") as fh:
        mapped = pickle.load(fh)
    recs = QS.records_from(mapped)
    return QS.field_rows(recs)


def z_of(pair):
    """A statistic's z, or None where the table could not read it."""
    return None if pair[0] is None else pair[0] / pair[1]


def rank1_share(rows):
    vals = [r['ns'][0] + 0.5 for r in rows if r['ns']]
    return cell_se(vals) + (len(vals),)


def slope_line(label, rows):
    pts = [(log(abs(r['d'])), r['ns'][0] + 0.5) for r in rows if r['ns']]
    b, se, a = EC.slope_fit(pts)
    print("    %-9s slope %+.4f +- %.4f per unit of log|d| (%d fields,"
          " mean log|d| %.2f)" % (label, b, se, len(pts),
                                  sum(x for x, y in pts) / len(pts)))
    return b, se


# ------------------------------------------------------------------ main
def main():
    t0 = time.time()
    rng = random.Random(SEED)

    section("THE SECOND POPULATION (%d < |d| <= %d, 2-rank 1, the place"
            " floor)" % (FIRST_CAP, CAP))
    mapped = mapped_increment()
    ok(all(abs(m[0]) > FIRST_CAP for m in mapped),
       "C8: a mapped field with |d| <= %d" % FIRST_CAP)
    recs = QS.records_from(mapped)
    by_h = defaultdict(int)
    for rec in recs:
        by_h[rec['h']] += 1
    print("  by class number: %s" % dict(sorted(by_h.items())))
    print("  non-cyclic among them: %d"
          % sum(1 for rec in recs if not rec['cyclic']))
    print("  %.1f s" % (time.time() - t0))
    ok(REHEARSAL or len(recs) >= 50, "too few fields to read")

    section("C1  THE TRIPLE PARITY")
    n_split = bad = 0
    for rec in recs:
        for p in rec['types']:
            cls = QS.s4_class(rec, p)
            if cls in ('1111', '22'):
                n_split += 1
            elif cls == 'BAD':
                bad += 1
    ok(bad == 0, "C1: %d split triples with 0 or 2 classes in 2Cl" % bad)
    print("  C1 PASSES: %d split primes, every triple with 1 or 3 classes"
          " in 2Cl" % n_split)

    section("C2, C3, C4  THE QUARTIC CERTIFICATE ON THE INCREMENT")
    QS.certify(recs, label="C4 PASSES (the sibling's P1)",
               floor_fatal=False, gen_boxes=GEN_BOXES, unit_boxes=UNIT_BOXES)

    section("C5  THE REPRINT (the first population from the cache)")
    rows1 = first_rows()
    if rows1 is not None:
        t1 = QS.rank_table(rows1, "first population, pooled")
        mu, se = t1[1]
        ok(abs(mu - REPRINT['rank1'][0]) < REPRINT['rank1'][1],
           "C5: first population rank 1 reads %.3f" % mu)
        th2 = QS.rank_table([r for r in rows1 if r['h'] == 2],
                            "first population, h = 2")
        ok(abs(th2[1][0] - REPRINT['h2'][0]) < REPRINT['h2'][1],
           "C5: first population h = 2 reads %.3f" % th2[1][0])
        print("  C5 PASSES: the first population reprints")

    section("C6, C7  THE NULL AND THE TWO PLANTED SEATS (increment)")
    null = QS.field_rows(recs, rng=rng)
    D0, S0, _ = QS.table_read(null, "null")
    zD0, zS0 = z_of(D0), z_of(S0)
    ok(REHEARSAL or (zD0 is not None and zS0 is not None
                     and abs(zD0) < 3.0 and abs(zS0) < 3.0),
       "C6: the null's D or S is off zero or unreadable")
    print("  C6 PASSES: null D and S within 3 sigma of zero")
    pr = QS.field_rows(recs, rng=random.Random(SEED + 1),
                       plant=('rank', QS.PLANT_RANK))
    Dr, Sr, _ = QS.table_read(pr, "rank-planted")
    pn = QS.field_rows(recs, rng=random.Random(SEED + 2),
                       plant=('norm', QS.PLANT_NORM))
    Dn, Sn, _ = QS.table_read(pn, "norm-planted")
    zDr, zSr, zDn, zSn = z_of(Dr), z_of(Sr), z_of(Dn), z_of(Sn)
    ok(REHEARSAL or (None not in (zDr, zSr) and zDr >= 3.0
                     and abs(zSr) < 2.0),
       "C7: the rank plant does not read as rank-seated")
    ok(REHEARSAL or (None not in (zDn, zSn) and zSn <= -3.0
                     and abs(zDn) < 2.0),
       "C7: the norm plant does not read as norm-seated")
    print("  C7 PASSES: the rank plant reads %s, the norm plant %s"
          % (QS.seat_verdict(Dr, Sr), QS.seat_verdict(Dn, Sn)))
    del null, pr, pn
    gc.collect()

    section("P1  THE SEAT ON THE SECOND POPULATION, BY STRATUM AND POOLED")
    rows = QS.field_rows(recs)
    per_h = {}
    for h in sorted(by_h):
        sub = [r for r in rows if r['h'] == h]
        if len(sub) < 10:
            print("  h = %d: %d fields, not read" % (h, len(sub)))
            continue
        per_h[h] = QS.rank_table(sub, "h = %d" % h)
    pooled = QS.rank_table(rows, "pooled over every stratum")
    mu, se = pooled[1]
    p1a = mu >= 0.20 and mu / se >= 3.0
    gap = None
    if 2 in per_h and 4 in per_h:
        m2, s2 = per_h[2][1]
        m4, s4 = per_h[4][1]
        gap = (m2 - m4) / sqrt(s2 * s2 + s4 * s4)
        print("  h = 2 rank 1 %s against h = 4 rank 1 %s: %.1f sigma apart"
              % (fmt(m2, s2), fmt(m4, s4), gap))
    print("  pooled rank-1 excess %s against 0.20 at 3 sigma: %s"
          % (fmt(mu, se), p1a))
    print("  P1 %s" % ("PASSES" if p1a and gap is not None and abs(gap) < 2.0
                        else "FAILS -- the kill"))

    section("P2  THE SLOPE IN |d|")
    m_inc, s_inc, n_inc = rank1_share(rows)
    diff = m_inc - FIRST_RANK1[0]
    sd = sqrt(s_inc ** 2 + FIRST_RANK1[1] ** 2)
    print("  increment rank-1 share %.3f +- %.3f (%d) against the first"
          " population's %.3f +- %.3f: %+.3f +- %.3f (%.1f sigma), printed"
          " and not voting" % (m_inc, s_inc, n_inc, FIRST_RANK1[0],
                               FIRST_RANK1[1], diff, sd, diff / sd))
    for (lo, hi) in BANDS_D:
        vals = [r['ns'][0] + 0.5 for r in rows
                if r['ns'] and lo <= abs(r['d']) < hi]
        if len(vals) >= QS.MIN_CELL:
            m, s = cell_se(vals)
            print("    band %d-%d: %.3f +- %.3f (%d)" % (lo, hi, m, s,
                                                          len(vals)))
        else:
            print("    band %d-%d: --(%d)" % (lo, hi, len(vals)))
    print("  slopes of the rank-1 share on log|d|:")
    slope_line("increment", rows)
    if rows1 is not None:
        slope_line("first", rows1)
        b, sb = slope_line("union", rows1 + rows)
        z = b / sb
        verdict = "FALLING" if z <= -2.0 else ("FLAT" if z < 2.0 else "RISING")
        print("  P2 (guess FALLING, 0.02 to 0.05) reads: %s (union slope"
              " %+.4f +- %.4f, z %+.1f)" % (verdict, b, sb, z))
        for h in (2, 4):
            sub1 = [r for r in rows1 if r['h'] == h]
            sub2 = [r for r in rows if r['h'] == h]
            if len(sub2) >= QS.MIN_CELL:
                slope_line("union h=%d" % h, sub1 + sub2)
    else:
        print("  P2 not read without the first population's rows")

    section("P3  RANK AGAINST NORM ON THE INCREMENT")
    D, S, stats = QS.table_read(rows, "increment")
    zD, zS = z_of(D), z_of(S)
    rank_ok = (None not in (zD, zS) and D[0] >= 0.05 and zD >= 2.0
               and abs(zS) < 2.0)
    print("  frozen: D >= 0.05 at 2 sigma and |z_S| < 2: %s; the sibling's"
          " letter reads %s" % (rank_ok, QS.seat_verdict(D, S)))
    pools_ok = True
    for key, (m1, s1) in sorted(FIRST_POOLS.items()):
        m2, s2 = pooled[key]
        z = (m2 - m1) / sqrt(s1 * s1 + s2 * s2)
        pools_ok = pools_ok and abs(z) < 2.0
        print("  ranks %d-%d pooled: increment %s against first %s,"
              " %+.1f sigma" % (key[0], key[1], fmt(m2, s2), fmt(m1, s1), z))
    print("  P3 %s" % ("PASSES" if rank_ok and pools_ok else "FAILS"))
    QS.split_below_table(rows)

    print("\n%d checks passed (%d here, %d in the imported sibling), %.1f s"
          " wall" % (CHECKS + QS.CHECKS, CHECKS, QS.CHECKS,
                     time.time() - t0))


if __name__ == "__main__":
    main()
