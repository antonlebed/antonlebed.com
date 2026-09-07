r"""THE LEVEL AT EVERY STRATUM, EACH TERM AT ITS IMAGE'S SHARE -- does the
level's rise with the class number dissolve when every prime-power
term is expected at the identity's share of its own image, and which
null does the corrected level answer to? (child of explore_triple_excess_box.py, whose F4 found every
readable stratum at h >= 4 rising with h under the uniform share over
24000 < |d| <= 96000 and whose S5b read h = 2 at each term's image
share; grandchild of explore_triple_cube_term.py, whose walk this file
extends by one record.)

THE QUESTION. A totally split prime q of a complex cubic field K
carries three places whose classes sum to zero; the all-principal event
is "all three principal", its share under a uniform Frobenius 1/h^2 on
the image M = {(a, b, c) : a + b + c = 0} of order h^2. The corrected
count adds the prime powers q^k < 1000 the explicit formula weights at
1/k, and the parents count every such power against the same 1/h^2 --
THE UNIFORM READ. But the algebra forces many powers onto the identity
whatever the field: an inert prime's cube always, a totally ramified
place at every h prime to 3, a split prime's square when the classes
are 2-torsion. Counted at 1/h^2 those add an excess that grows with
h, and the level rises with h exactly as the forcing predicts (the
parent's F4). THE IMAGE READ expects each term at the probability that
ITS OWN power lands on the identity under a uniform Frobenius in the
field's Galois group -- the share of {e} in the image of that term's
coset raised to the k-th power. The question is what the level reads
under the image share at every readable stratum, and, since the two
reads are two NULLS, which one the population sits at.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE GROUP. The Galois closure of the Hilbert class field of K
      over Q has group G = M x| S_3, |G| = 6 h^2, an element (v, s) with
      v in M and s permuting the coordinates; (v, s)^k = (v + s.v + ...
      + s^(k-1).v, s^k). Nothing here assumes Cl cyclic: |M[k]| =
      |Cl[k]|^2 because a, b in Cl[k] fix c = -a - b in Cl[k].

  (2) THE IMAGE SHARES, one closed form per source, p(source, k) =
      P((v, s)^k = e | s in the coset type), v uniform on M:
        split (s = 1):        k.v = 0   iff v in M[k]:     |Cl[k]|^2 / h^2
        partial (s = t):      k even, (v, t)^k = ((k/2)(v + t.v), 1)
                              = ((k/2)(-c, -c, 2c), 1), e iff (k/2).c = 0
                              on the FIXED coordinate:    |Cl[k/2]| / h
                              (k odd: outside N)
        inert (s = r):        3 | k, v + r.v + r^2.v = (a+b+c)(1,1,1)
                              = 0:                          1
                              (3 not dividing k: outside N)
        P^3 (3[P] = 0):       k.[P] = 0 with [P] in Cl[3]: 1 if 3 | k,
                              else 1 / |Cl[3]|
        P^2 Q (2[P] + [Q] = 0): e iff k.[P] = 0 and k.[Q] = -2k.[P] = 0,
                              iff k.[P] = 0, [P] uniform:   |Cl[k]| / h
      The first statement of the partial square, |Cl[2]|/h, was a slip:
      the fixed coordinate must VANISH, not be 2-torsion, since -c must
      be 0 as well as 2c; the parents' closed form (4) reads 3h|Cl[k/2]|
      per transposition coset and their walk tests (k/2).a = 0 on the
      degree-1 place, both 1/h at k = 2. At h = 2 that makes the partial
      square a half, not a quarter, so the parent's S5b -- which took
      the partial squares at 1/4 and every k >= 4 power at 1/4 -- is an
      UPPER BOUND on the image level, as it said of the P^2 Q pairs
      alone. The uniform read is p = 1/h^2 for every term.

  (3) THE THREE NULLS, stated as what the uniform level L_u does.
      Write W_t for a term's N-weight (summed over the stratum's fields,
      1/k per prime power, the ramified ones divided by their inertia
      order), N = n_s + sum W_t, and the FORCING
          F = sum_t W_t (p_t - 1/h^2) / (N / h^2),
      the excess the powers alone would put on the uniform level if the
      raw primes sat at 1/h^2.
        IMAGE NULL: every term at its own share, the raw primes at
          1/h^2; L_u = 1 + F, L_img = 1.
        EXPLICIT-FORMULA NULL, naive: the raw primes compensate the
          powers exactly; L_u = 1, L_img = 1 / (1 + F).
        CHEBYSHEV NULL (Rubinstein-Sarnak): the compensation is exact in
          the LOG-WEIGHTED sum -- the explicit formula is an identity
          in psi, not pi -- and the raw deficit is spread over the
          primes below the window like the primes themselves, so in
          COUNTS it is smaller by the ratio of a power's log q to a raw
          prime's mean log p: the compensated fraction is
              c_RS = [sum_t W_t (p_t - 1/h^2) log q_t / sum_t W_t
                      (p_t - 1/h^2)] / [sum_{split p} log p / n_s],
          L_u = 1 + (1 - c_RS) F, and the raw level is the SAME in
          every prime bin.
      THE ONE NUMBER: the uncompensated fraction f = (L_u - 1) / F,
      read per stratum with its bar; f = 1 is the image null, 0 the
      naive explicit formula, 1 - c_RS the Chebyshev null. The window
      puts c_RS near 0.5 at every h (the forcing-weighted mean log q
      sits near 3 against the split primes' mean log p near 5.7;
      measured 0.30 to 0.34, the forcing weighted toward 2, 3, 5 and 7
      more than this estimate allowed -- F2).
      The parent's prints already place h = 2 between: L_u = 1.06 with
      both terms in against F near +0.35 under (2), f near 0.2; and the
      unramified level alone at 1.009 above 24000, f near 0.03.

  (4) WHERE THE RAW DEFICIT SITS. The parent's S5b image level by bin
      at h = 2 climbs from 0.61 in [3, 30) to near 1 in [300, 1000):
      the raw shortfall is CONCENTRATED at the small primes, which the
      Chebyshev null (flat across bins) does not do and the corpus's
      seat law (the least places generate; explore_quartic_seat.py)
      does. So the raw
      level -- n_3 over n_s/h^2, no powers -- is printed by bin and
      stratum beside the Chebyshev null's flat value. A per-bin
      explicit formula, the deficit absorbed in the bin the power lands
      in, is not a null: at [3, 30) it asks for more deficit than the
      bin's raw count holds (0.34 against 0.375 per field at h = 2).

  (5) THE STATISTIC AND ITS SPREAD. exp_img = n_s/h^2 + sum_t W_t p_t
      per stratum and bin; count = n_3 + sum_t (e-weight landed). The
      summands are independent Bernoullis: a raw prime at 1/h^2, a
      power of weight 1/k at p_t, so var = n_s (1/h^2)(1 - 1/h^2) +
      sum_t (W_t / k_t)(1/k_t) p_t (1 - p_t) -- a forced term (p = 1)
      adds expectation and NO variance. The parents' Poisson bar
      sqrt(exp) is wider by exactly the forced mass; both are printed,
      the kill reads the summand bar. The uniform level keeps the
      parents' Poisson bar. f's bar is the uniform level's over F.

  (6) THE FIELD'S OWN GROUP. |Cl[m]| is counted per field from the
      MAP's lattice -- the harvested relations plus every relation the
      place map adds, whose order H is the parents' stratum key; where
      H differs from the class reading's h the field is counted at H
      and listed (C6): the first such field, d = -10015, reads h = 6 at
      a "confirmed" attestation while its place over 19 has the
      generator (-133, 103, 82), outside the harvest box at every box
      tried, so the reading over-reads and the map is right. The h
      residues 0 <= w[c] < |pivot| at every
      pivot column are the class group, the count asserted equal to h,
      and |Cl[m]| = #{w : m.w in the lattice} for m to 9. Non-cyclic
      strata (Z/2 x Z/2 at h = 4, Z/2 x Z/4 at 8, Z/3 x Z/3 at 9) get
      their own shares, and the structure census per stratum is
      printed. The expectation is accumulated PER FIELD at the field's
      own shares, so pooling over structures is exact. The degenerate
      regime (D) is read on Delta by enumeration for the unramified
      terms and left at the full-image shares for the ramified ones;
      D rows are printed and, as in the parent, not readable. The
      regime sort itself is the parent's SCALAR one, m.(b_i - b_j) = 0
      for m the class number stripped of its 3s, which agrees with
      membership in Delta only where the 3-part is cyclic of order 3
      (explore_noncyclic_level.py, explore_image_share.py); at 9 | h
      it demands equality and the M row can hold fields whose measured
      image has index 3. The rows at 3 | h are therefore read as the
      parent read them and qualified; the claims stand on the strata
      prime to 3.

  (7) THE WINDOW'S BINS. Prime powers land in EVERY bin: [300, 1000)
      holds 19^2, 23^2, 29^2, 31^2, 7^3, 5^4, 3^6 and 2^9. The parent's
      (4) called that bin "the raw count, no powers reach it", an
      error corrected in its text; its F2 figures for the bin are
      levels with those powers in and stand.

  (8) THE PRICE. The class reading is the parent's 105 minutes to
      96000 and was not kept; here it is CHECKPOINTED per box as the
      readings themselves (d, the polynomial, h, the kind, the
      generator places, the relation basis -- the maximal order is
      recomputed), so every later re-walk costs the walks alone, 12
      minutes over the six boxes. The walks are a second per-box
      checkpoint. A restart that loads a box's readings marks the
      topband rig's Hermite cross-check budget (300 calls against the
      shop's original, spent on the small boxes in a fresh run) as
      spent, since otherwise it fires on a large box, where the
      original's entries swell past the memory ceiling (the first
      restart was killed at 529 MB commit in the fourth box's first
      fields).
      Rehearsed at cap 6000. Estimate: 2 hours the first
      time, peak 350 MB at the enumeration.
  (9) THE KEPT READINGS ARE COMPLETED ON LOAD. A reading's relation
      lattice made before the shop seeded the forced relations --
      (p) = prod P_i^e_i principal wherever every place of p is a
      column, a row the element harvest misses when p^3 lies outside
      its box -- can carry a spurious torsion element and read twice
      the class number, both representatives agreeing (found by
      explore_triple_far_window.py, whose walk to 10000 reached the
      cube of a generator prime and asked the triple to sum to zero).
      The loader adds the forced rows to every kept basis, recomputes
      the order, rewrites the checkpoint and prints the fields whose
      class number moved; a fresh reading is complete by construction.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_triple_excess_box.py: the population, the boxes, the
    bins, the class reading with its T4/T10/T11 policies, the three
    walks, the regime sort and the uniform level's algebra are
    IMPORTED; C1 reprints its F1, F4 and S5b before anything new is
    read. Its cells now carry the weight by "kind:q:k" (a one-record
    extension of explore_triple_cube_term.py and
    explore_triple_ramified_term.py made for this file), which nothing
    in the parents reads.
 T2 THE GROUP MODEL (1) is the cube-term rig's (1): the Galois closure
    of the Hilbert class field as M x| S_3, Frobenius uniform on it.
    It is a model; the population grades it.
 T3 THE CHEBYSHEV NULL's spreading rule -- the log-weighted deficit
    distributed over the raw primes in proportion to their log -- is
    Rubinstein-Sarnak's picture of the bias in pi(x; C) imported by
    argument, not read full-text here; it is graded, not claimed.
 T4 THE TOPBAND RIG'S VALUATION CACHE (its T6) cleared on the order's
    id(), which a freed order's successor can inherit, so a stale
    power ladder under coinciding place rows could answer for the next
    field; found here when two walks of the same readings differed by
    a field, fixed there by holding the order itself. The harvest rows
    a class reading rests on carry the shop's per-element checksum and
    the map's vectors do not, which is where the drift showed. The
    walks recorded below are the fixed ones; the readings of boxes 0
    and 1 re-read under the fix are identical to their checkpoints,
    boxes 2 and 3 re-read fresh by explore_triple_far_window.py under
    the seeded harvest move no class number, boxes 4 and 5 were not
    re-read; the completion of (9), applied to all six, is the
    lineage pass, its diff below.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE KILL-SHAPE, printed: no readable stratum at h >= 4
      (expected corrected count >= 10, regime not D, pooled over
      24000 < |d| <= 96000) has an image level more than 2 sigma
      (summand bar) ABOVE 1. One that does KILLS: something beyond the
      forcing is in the level.
  P2  EVERY readable stratum's image level sits BELOW 1 by more than 2
      sigma, and the shortfall grows with h: h = 2 in [0.75, 0.90]
      pooled over all six boxes, every readable h >= 4 stratum in
      [0.50, 0.85] over the new boxes.
  P3  THE UNCOMPENSATED FRACTION f, both terms in: at h = 2 in [0.10,
      0.35] over all boxes; at every readable h >= 4 stratum in [0.20,
      0.60] over the new boxes. Neither the image null (1) nor the
      naive explicit formula (0) is inside any bar.
  P4  THE CHEBYSHEV NULL is not it either: c_RS's prediction 1 - c_RS
      sits more than 2 sigma ABOVE the measured f at h = 2; and the
      raw level by bin at h = 2 over the new boxes rises across the
      four bins, [3, 30) the lowest by more than 3 sigma below
      [300, 1000). The shortfall is at the seat's least places.
  P5  REPRODUCTION (C1): the parent's F1 uniform levels by box (1.060,
      1.069, 1.084, 1.117, 1.058, 1.066), its F4 stratum levels over
      the new boxes (1.312, 1.452, 1.763, 1.829, 2.173 at h = 4, 5, 7,
      8, 9) and its S5b image levels under S5b's own convention (0.936,
      0.927, 0.940, 0.971, 0.920, 0.927) reprint within 0.002, from
      the re-read population.

THE CONTROLS, run before any prediction is read.

  C0  THE SHARES AGAINST THE GROUP: for Cl in Z/2, Z/3, Z/4, Z/2 x Z/2,
      Z/5, Z/6, Z/8, Z/2 x Z/4, Z/9, Z/3 x Z/3 and Z/12, the closed
      forms of (2) equal the brute-force count of (v, s)^k = e over the
      whole coset at every k <= 9, every source; and the cyclic rows
      equal the cube-term rig's count_pow.
  C1  REPRODUCTION as P5, plus: the sum of the by-source weights equals
      the pooled cN and c3 in every cell to 1e-9.
  C2  THE SUMMAND BAR: with one stratum's measured weights and shares,
      2000 Bernoulli replicates of the image count give an image level
      of 1.00 +- its own bar and a replicate spread within 15 % of the
      summand sd of (5).
  C3  THE GROUP COUNT: the residue enumeration of (6) yields exactly h
      distinct classes at every field with h > 1, and |Cl[1]| = 1,
      |Cl[h]| = h.
  C4  THE CHECKPOINT: at the rehearsal the walk of box 0 from the
      loaded readings agrees cell for cell with a walk from readings
      taken fresh in the same process.
  C5  THE PARENT'S OWN CHECKS per box (its C3-C4): every lift relation
      holds, every type agrees with the valuation, no map disagreement,
      exclusions under 1 %.
  C6  THE TWO ORDERS: every field where the map's order differs from
      the class reading's is listed per box with both numbers; the
      count is a print, not a bar, and is what a lineage pass on the
      reading's other consumers would start from.

THE DESIGN. S1 the population (the parent's, checkpointed). S2a the
class readings per box, checkpointed as readings; S2b the walks per
box from the loaded readings, each field's torsion table computed
from its lattice, the cells (with the by-source weights) and the
per-field image expectations accumulated per stratum and bin,
checkpointed. Then the reads: C0, C1, C2, the by-source table at h = 2
and at each readable stratum (weight, landed, expected under each
null), the uniform and image levels by stratum (both bars), by box at
h = 2, by bin; F and f per stratum with the three nulls' values; the
raw level by bin; the structure census; P1-P5. Flags: `--cap N`,
`--ckpt DIR` (default beside the system temp), `--fresh`.

FINDINGS. The parent's population re-read: 16313 complex fields to
|d| <= 96000, the same three excluded, 6444 with h > 1 by the map's
order (2204 at h = 2). THE COMPLETION (9) moves nine class numbers of
6449 read above 1, every one by a factor of 2: d = -6791 (4 to 2),
-10015 (6 to 3), -10187 (8 to 4), -10355 (4 to 2), -44587 (2 to 1),
-46027 (4 to 2), -73591 (2 to 1), -87767 (4 to 2), -91564 (2 to 1);
LMFDB gives 2, 4, 2 at -6791, -10187, -10355, the completed values.
Three of the nine the map's order had already corrected; the other
six had passed C6, the map's lattice missing the same row. Under the
completion every figure below reprints to 0.001 (the h = 2 all-box f
0.232 against 0.23, box 2's image level 0.825 against 0.824). C0 held
at all eleven groups, every source and
k, count_pow agreeing on the cyclic ones. C1: the six h = 2 uniform
levels and the six S5b-convention image levels reprint the parent to
the digit (box 2's uniform 1.085 against its 1.084 after the
completion); the new-box rows at h = 4, 5, 6, 8 and 9 within 0.0005
and the row at h = 7 off by 0.0055 (151 fields, 47 all-principal, a
fifth of the row's bar; the parent's walk ran under the cache bug of
T4, and the first walks here, run under it too, had h = 8 off by
0.021 and h = 7 by the same 0.0055); the by-source sums off the
pooled cN and c3 by 8.6e-12. C2 (500 replicates, the slate's 2000 a
slip): spreads 0.0363, 0.0175,
0.0249 against summand sds 0.0364, 0.0170, 0.0258 (Poisson 0.051,
0.024, 0.036). C3 at every field; C4 at the rehearsal; C5 clean in
every box (8961 lift relations in the top box). C6 after the
completion: the map's order differs from the class reading's at six
fields -- d = -13484 (81, 9), -39251, -49595, -75239 (4, 2 each),
-46891 (16, 8), -93715 (20, 10) -- always smaller, the reading missing
a relation whose generator lies outside the harvest box; every one is
keyed at the map's order, as the parents keyed them. A field the
walks under the cache bug listed, d = -80787 (8, 4), reads 8 both
ways under the fix: that disagreement was the cache's.

  F1. THE KILL DOES NOT FIRE: AT ITS IMAGE'S SHARE EVERY READABLE
      STRATUM SITS FAR BELOW 1 (observation; P1 holds; P2 holds but for
      its floor, h = 12 reading 0.455). Over 24000 < |d| <= 96000 the
      image level reads 0.815 (h = 2) and 0.669, 0.724, 0.654, 0.521,
      0.558, 0.547 at h = 4, 5, 7, 8, 10, 11, the summand z from -34
      to -5.7, while the uniform level reprints the parent's rise,
      1.063, 1.312, 1.452, 1.757, 1.829, 2.283, 2.164; the 3 | h rows
      on the scalar sort (6) read 0.555, 0.622, 0.455 at h = 6, 9, 12
      on the M side (uniform 1.385, 2.173, 2.366) and 0.900, 0.463,
      0.376 on the D side. Over all six boxes h = 2 reads
      0.820 (z -37.7), the parent's S5b upper bound 0.93 lowered by the
      partial squares at 1/2 and the k >= 4 powers at their shares.
  F2. THE RISE WITH h DISSOLVES INTO ONE NUMBER (observation; P3
      holds). The uncompensated fraction f = (L_u - 1)/F reads 0.208
      +- 0.028 at h = 2 and 0.325, 0.450, 0.449, 0.331, 0.415, 0.394
      (bars 0.035 to 0.090) at h = 4, 5, 7, 8, 10, 11, while the
      forcing F runs 0.31, 0.96, 1.00, 1.69, 2.51, 3.09, 2.95: the
      level rises because the forcing does, at a fixed fraction near
      0.4 of it (the 3 | h M rows read 0.257, 0.471, 0.325 at h = 6,
      9, 12 on the scalar sort). Neither of the two nulls: f = 0 is
      4.4 sigma away at the least (h = 11) and 5.6 to 9.3 at every
      other readable stratum, f = 1 is 6.7 to 28 sigma away. Nor the
      Chebyshev null (P4): 1 - c_RS reads 0.66 to 0.71 at every
      stratum, above the measured f by 16 sigma at h = 2 (17 over all
      six boxes) and by 3.2 to 10.2 sigma at every readable h >= 4.
  F3. THE FREE TERMS LAND SHORT OF THEIR SHARE, AS THE SEAT'S LEAST
      PLACES DO (observation). At h = 4 the partial squares land 140.5
      on a weight of 1097 (0.128 against the share 1/4), the P^2 Q
      places at k = 1 41.5 on 282.5 (0.147 against 1/4), the split
      squares 84 on 293.5 (0.286 against 0.410, the stratum's 90 fields
      with Cl = Z/2 x Z/2 in the share); at h = 2 the partial squares
      land 0.340 against 1/2 and the P^2 Q places 0.398 against 1/2;
      the split cubes at h = 2, all from q <= 7, land 9.3 on 220.3
      (0.042) where the raw split primes land 0.198. The forced terms
      (p = 1) land whole, as they must.
  F4. THE RAW SHORTFALL SITS AT THE SMALL PRIMES AND DEEPENS WITH h
      (observation; P4's bin clause holds). The raw level, no powers,
      by bin over the new boxes at h = 2: 0.345, 0.526, 0.721, 0.884,
      [300, 1000) above [3, 30) by 13.5 sigma; at h = 4: 0.16, 0.53,
      0.48, 0.69. Pooled over the bins it falls with h: 0.79, 0.61,
      0.72, 0.43, 0.60, 0.41, 0.64, 0.52, 0.44, 0.20 at h = 2, 4, 5,
      6 M, 7, 8, 9 M, 10, 11, 12 M. The Chebyshev null's flat-by-bin
      raw level is refuted by the bins at every stratum read.
  F5. h = 2 IS FLAT IN THE BOX AT THE IMAGE SHARE TOO (observation):
      0.815, 0.815, 0.824, 0.853, 0.809, 0.818 by box, f 0.20, 0.22,
      0.27, 0.38, 0.19, 0.22, the raw level 0.87, 0.85, 0.84, 0.87,
      0.79, 0.79.

RUN RECORD. 2026-09-06, Windows 11, Python 3, `python
prime/code/memwatch.py python prime/code/explore_triple_image_level.py`
with `--ckpt` naming a scratch directory. One process, CPython, no
BLAS. Rehearsed at cap 3000 first: 740 checks, 109 s, 27 MB, the
checkpoint round trip exercised by a second invocation. The full run
took three launches: the first died at box 3 on this file's own
assertion that the map's order equal the reading's (823 s, 359 MB
peak at the enumeration), replaced by the C6 census; the restart was
killed by memwatch at 529 MB commit in the fourth box's first fields
(the cross-check budget, (8)); the third ran boxes 3 to 5 in 7280 s (the
readings 611, 1491 and 4439 s, the walks 72, 226 and 438 s), peak
139.8 MB. Then T4: the walks redone from the kept readings under the
cache fix, 695 s over the six boxes, 19393 checks, and a second fresh
process identical to it cell for cell; the read stage alone from the
checkpoints 1.0 s. Before the fix two walks of the same readings had
differed at three fields' strata. 2026-09-07, the completion (9):
the six boxes' walks redone from the completed readings, 693 s, 19393
checks, peak 157 MB.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import itertools
import json
import math
import random
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _flag(name, default):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    return default


CAP = int(_flag("--cap", 96000))
CKPT = _flag("--ckpt", os.path.join(tempfile.gettempdir(),
                                    "image_level_%d" % CAP))
FRESH = "--fresh" in sys.argv
_ARGV = sys.argv
sys.argv = [_ARGV[0], "--cap", str(CAP), "--ckpt", CKPT]   # T1: the parent
import explore_triple_excess_box as EB          # noqa: E402
sys.argv = _ARGV

import explore_ceiling_topband as TB            # noqa: E402
import explore_cubic_class_map as CCM           # noqa: E402
import explore_cubic_principal as ECP           # noqa: E402
import explore_cubic_split_triple as ST         # noqa: E402
import explore_family_term as FT                # noqa: E402
import explore_triple_cube_term as CT           # noqa: E402
import explore_triple_ramified_term as RT       # noqa: E402

BOXES = EB.BOXES
BIN_EDGES = EB.BIN_EDGES
MIN_READ = EB.MIN_READ
MIN_SPLIT = EB.MIN_SPLIT
HIGH_FRAC = EB.HIGH_FRAC
KMAX = 9                    # 2^9 = 512 is the deepest power in the window
TOR_M = tuple(range(1, KMAX + 1))
NEW = [i for i, (lo, hi) in enumerate(BOXES) if lo >= 24000]
CHECKS = 0
REPRO_TOL = 0.002
F1 = (1.060, 1.069, 1.084, 1.117, 1.058, 1.066)             # P5
F4 = {(4, 'A'): 1.312, (5, 'A'): 1.452, (6, 'M'): 1.385, (7, 'A'): 1.763,
      (8, 'A'): 1.829, (9, 'M'): 2.173}                          # P5
S5B = (0.936, 0.927, 0.940, 0.971, 0.920, 0.927)            # P5


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
    sys.stdout.flush()


def key_str(key):
    return "%d:%s" % key


def key_of(s):
    h, reg = s.split(":")
    return (int(h), reg)


# ------------------------------------------------------ the group (6)
def canon(v, piv):
    w = list(v)
    for (c, row) in piv:
        if w[c]:
            q = w[c] // row[c]
            w = [x - q * y for x, y in zip(w, row)]
    return tuple(w)


def class_group(piv, k, h):
    """The h residues of Z^k modulo the lattice, canonical."""
    cols = [(c, abs(row[c])) for (c, row) in piv]
    ok(len(cols) == k, "lattice of rank %d in Z^%d" % (len(cols), k))
    seen = set()
    for digits in itertools.product(*[range(m) for (_c, m) in cols]):
        v = [0] * k
        for (c, _m), x in zip(cols, digits):
            v[c] = x
        seen.add(canon(v, piv))
    ok(len(seen) == h, "enumeration gives %d classes at h = %d"
       % (len(seen), h))
    return sorted(seen)


def torsion(piv, k, group):
    """m -> |Cl[m]| for m in TOR_M."""
    return dict((m, sum(1 for v in group
                        if CCM.in_span([m * x for x in v], piv, k)))
                for m in TOR_M)


def delta_group(piv, k, group):
    """Delta = {(a, b, c) in M : a = b = c mod 3Cl}, as canonical triples;
    3Cl is the set of 3.y."""
    three = set(canon([3 * x for x in v], piv) for v in group)
    out = []
    for a in group:
        for b in group:
            c = canon([-x - y for x, y in zip(a, b)], piv)
            if (canon([x - y for x, y in zip(a, b)], piv) in three
                    and canon([x - y for x, y in zip(b, c)], piv) in three):
                out.append((a, b, c))
    return out


def shares_full(tor, h):
    """(2): p(source, k) on the full image, keyed like the cells."""
    p = {}
    for k in TOR_M:
        p[('split', k)] = tor[k] ** 2 / float(h * h)
        p[('partial', k)] = tor[k // 2] / float(h) if k % 2 == 0 else None
        p[('inert', k)] = 1.0 if k % 3 == 0 else None
        p[('p2q', k)] = tor[k] / float(h)
        p3 = 1.0 if k % 3 == 0 else 1.0 / tor[3]
        for t in ('p3s', 'p3i', 'p3w'):
            p[(t, k)] = p3
    return p


def shares_delta(piv, k, group, tor, h):
    """(6): the unramified shares on Delta by enumeration; the ramified
    ones at the full image's."""
    D = delta_group(piv, k, group)
    n = float(len(D))
    p = shares_full(tor, h)
    for m in TOR_M:
        p[('split', m)] = sum(1 for (a, b, c) in D
                              if all(CCM.in_span([m * x for x in v], piv, k)
                                     for v in (a, b, c))) / n
        if m % 2 == 0:
            p[('partial', m)] = sum(
                1 for (a, b, c) in D
                if CCM.in_span([(m // 2) * x for x in c], piv, k)) / n
    return p, len(D)


# ------------------------------------------------------- the box read
def slim(rec, tag):
    (d, cx, a, b, c, O, h, kind, gp, rel) = rec
    return [d, cx, a, b, c, h, kind, gp, rel, tag]


def fat(s):
    (d, cx, a, b, c, h, kind, gp, rel, tag) = s
    gp = [tuple(t[:4]) + (t[4],) for t in gp]
    O = FT.maximal_order3_wide(a, b, c)[0]
    return (d, cx, a, b, c, O, h, kind, gp, rel), tag


def read_box_readings(bi, fields):
    """S2a: the class reading of one box, every complex field."""
    lo, hi = BOXES[bi]
    sub = [(d, polys) for (d, polys) in fields if lo < -d <= hi]
    t0 = time.time()
    out, excluded, tags = [], [], {}
    for i, (d, polys) in enumerate(sub):
        if i and i % 500 == 0:
            print("  ... %d/%d read, %.1f s" % (i, len(sub), time.time() - t0))
            sys.stdout.flush()
        pl = [(a, b, c) + (FT.maximal_order3_wide(a, b, c)[0],)
              for (a, b, c) in polys]
        rec, _retried, tag = TB.read_field(d, True, pl)
        tags[tag] = tags.get(tag, 0) + 1
        if rec is None:
            excluded.append(d)
            continue
        out.append(slim(rec, tag))
    wall = time.time() - t0
    print("  box (%d, %d]: %d complex fields read, %d excluded %s; tags "
          "%s; %.1f s" % (lo, hi, len(sub), len(excluded), excluded,
                           sorted(tags.items()), wall))
    ok(len(excluded) <= EB.UNRESOLVED_KILL * max(len(sub), 1),
       "T4 kill: %d of %d excluded" % (len(excluded), len(sub)))
    return dict(readings=out, excluded=excluded, n=len(sub), wall=wall)


def new_img():
    """Per stratum and bin: the image expectation and its variance,
    the raw count's, and the by-source table."""
    return dict(exp=0.0, var=0.0, exp_raw=0.0, var_raw=0.0, dlog=0.0,
                forcing=0.0, terms={})


INERTIA = dict(split=1, partial=1, inert=1, p2q=2, p3s=3, p3i=3, p3w=6)


def unit_weight(tag):
    """One prime power's weight: 1/k, over the inertia order if ramified."""
    kind, _q, kk = tag.split(":")
    return 1.0 / (int(kk) * INERTIA[kind])


def add_term(img, tag, w, e, p, share):
    kind, q, kk = tag.split(":")
    q, kk = int(q), int(kk)
    u = unit_weight(tag)
    t = img['terms'].setdefault(tag, [0.0, 0.0, 0.0, 0.0])
    t[0] += w
    t[1] += e
    t[2] += w * p
    t[3] += w * u * p * (1 - p)
    img['exp'] += w * p
    img['var'] += w * u * p * (1 - p)
    img['forcing'] += w * (p - share)
    img['dlog'] += w * (p - share) * math.log(q)


def walk_box(bi, readings):
    """S2b: the three walks on every field with h > 1 of one box, the
    per-field shares folded into the stratum's image tables."""
    lo, hi = BOXES[bi]
    t0 = time.time()
    un, ram, census, nfields, img, struct = {}, {}, {}, {}, {}, {}
    disagree = []
    checks = dict(c3_ok=0, c3_bad=0, c4_agree=0, c4_disagree=0,
                  c4map_disagree=0, c5_tame=0, c5_bad=0, bad_sum=0)
    for i, s in enumerate(readings):
        if i and i % 1000 == 0:
            print("  ... %d/%d walked, %.1f s" % (i, len(readings),
                                                  time.time() - t0))
            sys.stdout.flush()
        rec, _tag = fat(s)
        (d, cx, a, b, c, O, h, kind, gp, rel) = rec
        if h == 1:
            continue
        H, piv, k, per_prime = ST.read_field(O, a, b, c, d, cx, gp, rel)
        if H is None or H == 1:
            continue
        if H != h:
            disagree.append([d, h, H])                          # C6
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
        key = key_str((H, reg))
        nfields[key] = nfields.get(key, 0) + 1
        rcells = RT.walk_ramified(rec, piv, k,
                                  census.setdefault(key, RT.new_census()),
                                  checks)
        # the field's own group (6)
        group = class_group(piv, k, H)
        tor = torsion(piv, k, group)
        ok(tor[1] == 1 and tor[H] == H if H <= KMAX else tor[1] == 1,
           "d = %d: torsion table %s at h = %d" % (d, tor, H))
        sk = struct.setdefault(key, {})
        sname = "|Cl[m]|=" + ",".join(str(tor[m]) for m in TOR_M)
        sk[sname] = sk.get(sname, 0) + 1
        if reg == 'D':
            p, _nd = shares_delta(piv, k, group, tor, H)
            share = CT.share_of(H, reg)
        else:
            p = shares_full(tor, H)
            share = 1.0 / (H * H)
        # fold into the stratum's tables
        su = un.setdefault(key, {})
        sr = ram.setdefault(key, {})
        si = img.setdefault(key, {})
        for bb, cell in cells.items():
            CT.merge(su.setdefault(str(bb), CT.new_cell()), cell)
            g = si.setdefault(str(bb), new_img())
            g['exp_raw'] += cell['ns'] * share
            g['var_raw'] += cell['ns'] * share * (1 - share)
            for tag, w in cell['w_qk'].items():
                kd, _q, kk = tag.split(":")
                add_term(g, tag, w, cell['e_qk'].get(tag, 0.0),
                         p[(kd, int(kk))], share)
        for bb, cell in rcells.items():
            RT.merge_r(sr.setdefault(str(bb), RT.new_rcell()), cell)
            g = si.setdefault(str(bb), new_img())
            for tag, w in cell['w_qk'].items():
                typ, _q, kk = tag.split(":")
                add_term(g, tag, w, cell['e_qk'].get(tag, 0.0),
                         p[(typ, int(kk))], share)
    wall = time.time() - t0
    print("  box (%d, %d]: %d readings, %d with h > 1 walked, %.1f s"
          % (lo, hi, len(readings), sum(nfields.values()), wall))
    return dict(un=un, ram=ram, census=census, nfields=nfields,
                checks=checks, img=img, struct=struct, wall=wall,
                disagree=disagree)


def complete_readings(R, bi):
    """(9): a checkpoint written before the shop's harvest seeded the
    forced relations is completed in place -- the rows added to each
    reading's basis, the class number recomputed -- and the fields
    whose class number moves are printed; returns their count."""
    moved = []
    for s in R['readings']:
        (d, cx, a, b, c, h, kind, gp, rel, tag) = s
        if rel is None:
            continue
        forced = TB.CFS.forced_relations([tuple(t) for t in gp])
        rows = [list(r) for r in rel]
        if all(CCM.in_span(f, CCM.echelon(rows, len(gp)), len(gp))
               for f in forced):
            continue
        rows = TB.rel_basis(rows + forced, len(gp))
        H = TB.CFS.hermite_order(rows, len(gp))
        s[8] = rows
        if H != h:
            moved.append((d, h, H))
            s[5] = H
    print("  box %d: %d readings completed by the forced relations, the "
          "class number moving at %d %s" % (bi, len(R['readings']),
                                            len(moved), moved))
    return len(moved)


def load_readings(bi):
    """The kept readings of one box, completed (9) and rewritten when the
    completion changes them."""
    rpath = os.path.join(CKPT, "readings%d.json" % bi)
    R = json.load(open(rpath))
    print("  box %d readings loaded: %d fields, %d excluded, "
          "%.1f s when run" % (bi, len(R['readings']),
                               len(R['excluded']), R['wall']))
    TB._HO_CTRL[0] = 0          # (8): the cross-check budget was spent
    #                             by the run that wrote the checkpoint
    if not R.get('completed'):
        complete_readings(R, bi)
        R['completed'] = True
        json.dump(R, open(rpath, "w"))
    return R


def s2_boxes(fields):
    section("S2  THE BOX READS -- readings then walks, each checkpointed "
            "per box in %s" % CKPT)
    out = []
    for bi in range(len(BOXES)):
        rpath = os.path.join(CKPT, "readings%d.json" % bi)
        if os.path.exists(rpath) and not FRESH:
            R = load_readings(bi)
        else:
            R = read_box_readings(bi, fields)
            R['completed'] = True
            if not os.path.isdir(CKPT):
                os.makedirs(CKPT)
            json.dump(R, open(rpath, "w"))
        wpath = os.path.join(CKPT, "walk%d.json" % bi)
        if os.path.exists(wpath) and not FRESH:
            data = json.load(open(wpath))
            print("  box %d walks loaded: %d with h > 1, %.1f s when run"
                  % (bi, sum(data['nfields'].values()), data['wall']))
        else:
            data = walk_box(bi, R['readings'])
            json.dump(data, open(wpath, "w"))
        if bi == 0 and CAP <= 6000:                              # C4
            R2 = read_box_readings(0, fields)
            fresh = walk_box(0, R2['readings'])
            back = json.loads(json.dumps(fresh))
            same = all(back[f] == data[f] for f in ('un', 'ram', 'img',
                                                     'census', 'nfields'))
            print("  [C4] box 0 walked from fresh readings agrees with the "
                  "checkpointed walk cell for cell: %s" % same)
            ok(same, "C4: the checkpoint round trip changes a cell")
        data['excluded'] = R['excluded']
        data['n'] = R['n']
        for ck in ('c3_bad', 'c4_disagree', 'c4map_disagree', 'c5_bad',
                   'bad_sum'):
            ok(data['checks'][ck] == 0, "box %d: %s = %d"
               % (bi, ck, data['checks'][ck]))                   # C5
        print("  [C5] box %d: lift relations %d hold, types %d agree, "
              "tame P^3 %d, clean" % (bi, data['checks']['c3_ok'],
                                      data['checks']['c4_agree'],
                                      data['checks']['c5_tame']))
        dis = data.get('disagree', [])
        print("  [C6] box %d: the map's order differs from the class "
              "reading's at %d fields %s" % (bi, len(dis), dis[:8]))
        out.append(data)
    return out


# ------------------------------------------------------------ the reads
def pooled_img(boxes, key, bins=None):
    g = new_img()
    ks = key_str(key)
    for data in boxes:
        for bb, cell in data['img'].get(ks, {}).items():
            if bins is not None and int(bb) not in bins:
                continue
            for f in ('exp', 'var', 'exp_raw', 'var_raw', 'dlog',
                      'forcing'):
                g[f] += cell[f]
            for tag, t in cell['terms'].items():
                u = g['terms'].setdefault(tag, [0.0] * 4)
                for i in range(4):
                    u[i] += t[i]
    return g


def levels(boxes, key, bins=None):
    """(uniform level, its Poisson z, image level, its summand z, its
    Poisson z, exp_img, F, f, sigma_f, c_RS, raw level, raw z, n3) pooled."""
    u, r = EB.parts_of(boxes, key, bins)
    g = pooled_img(boxes, key, bins)
    share = CT.share_of(*key)
    N = u['ns'] + u['cN'] + r['cN']
    count = u['n3'] + u['c3'] + r['c3']
    exp_u = N * share
    if exp_u <= 0:
        return None
    lu = count / exp_u
    zu = (count - exp_u) / math.sqrt(exp_u)
    exp_i = g['exp_raw'] + g['exp']
    var_i = g['var_raw'] + g['var']
    li = count / exp_i
    zi = (count - exp_i) / math.sqrt(var_i) if var_i > 0 else 0.0
    zip_ = (count - exp_i) / math.sqrt(exp_i)
    F = g['forcing'] / exp_u
    f = (lu - 1) / F if F > 0 else None
    sf = (1.0 / math.sqrt(exp_u)) / F if F > 0 else None
    # the Chebyshev null (3)
    logs = [math.log(p) for p in ECP.ODD_PRIMES
            if bins is None or CT.bin_of(p) in bins]
    mean_log_p = sum(logs) / len(logs)
    c_rs = ((g['dlog'] / g['forcing']) / mean_log_p
            if g['forcing'] > 0 else None)
    exp_raw = u['ns'] * share
    lr = u['n3'] / exp_raw if exp_raw > 0 else None
    zr = ((u['n3'] - exp_raw) / math.sqrt(exp_raw * (1 - share))
          if exp_raw > 0 else None)
    return dict(lu=lu, zu=zu, li=li, zi=zi, zip=zip_, exp_i=exp_i,
                exp_u=exp_u, F=F, f=f, sf=sf, c_rs=c_rs, lr=lr, zr=zr,
                n3=u['n3'], ns=u['ns'], N=N, count=count, g=g)


def fmt(x, d=3):
    return "--" if x is None else ("%%.%df" % d) % x


def fz(z):
    return "--" if z is None else "%+.2f" % z


# ------------------------------------------------------------ controls
def brute_shares(mods):
    """C0: Cl = prod Z/m; the coset counts by brute force."""
    els = list(itertools.product(*[range(m) for m in mods]))
    add = lambda x, y: tuple((a + b) % m for a, b, m in zip(x, y, mods))
    neg = lambda x: tuple((-a) % m for a, m in zip(x, mods))
    zero = tuple(0 for _ in mods)
    h = len(els)
    M = [(a, b, add(neg(a), neg(b))) for a in els for b in els]
    perms = {'split': (0, 1, 2), 'partial': (1, 0, 2), 'inert': (1, 2, 0)}
    out = {}
    for name, s in perms.items():
        for k in TOR_M:
            cnt = 0
            inN = True
            for v in M:
                w = (zero, zero, zero)
                cur = v
                sig = (0, 1, 2)
                for _ in range(k):
                    w = tuple(add(w[i], cur[i]) for i in range(3))
                    cur = tuple(cur[s[i]] for i in range(3))
                    sig = tuple(sig[s[i]] for i in range(3))
                if sig != (0, 1, 2):
                    inN = False
                    break
                if w == (zero, zero, zero):
                    cnt += 1
            out[(name, k)] = None if not inN else cnt / float(h * h)
    tor = dict((m, sum(1 for e in els
                       if all((m * a) % mm == 0 for a, mm in zip(e, mods))))
               for m in TOR_M)
    return out, tor, h


def c0_shares():
    section("C0  THE SHARES AGAINST THE GROUP -- closed forms of (2) "
            "against brute force on M x| S_3, and count_pow where cyclic")
    for mods in ((2,), (3,), (4,), (2, 2), (5,), (6,), (8,), (2, 4), (9,),
                 (3, 3), (12,)):
        brute, tor, h = brute_shares(mods)
        p = shares_full(tor, h)
        bad = 0
        for (name, k), v in brute.items():
            want = p[(name, k)]
            if (v is None) != (want is None) or (v is not None
                                                 and abs(v - want) > 1e-12):
                bad += 1
                print("  MISMATCH %s k=%d brute %s closed %s" % (name, k, v,
                                                                 want))
        cyc = ""
        if len(mods) == 1:
            for k in TOR_M:
                tot = CT.count_pow(h, k, 'e')
                closed = (p[('split', k)] * h * h
                          + (p[('partial', k)] or 0) * 3 * h * h
                          + (p[('inert', k)] or 0) * 2 * h * h)
                if abs(tot - closed) > 1e-9:
                    bad += 1
                    print("  count_pow MISMATCH h=%d k=%d %s vs %s"
                          % (h, k, tot, closed))
            cyc = ", count_pow agrees at k <= %d" % KMAX
        print("  Cl = %-12s h = %2d  |Cl[m]| = %s  every source and k "
              "agrees%s" % ("x".join("Z/%d" % m for m in mods), h,
                            ",".join(str(tor[m]) for m in TOR_M), cyc))
        ok(bad == 0, "C0 fails at %s" % (mods,))


def c1_reproduce(boxes):
    section("C1  REPRODUCTION -- the parent's F1, F4 and S5b from the "
            "re-read population; the by-source sums")
    key = (2, 'A')
    for bi, data in enumerate(boxes):
        lv, z, _e, _n = EB.level_of([data], key)
        print("  box %d h = 2 uniform level %.3f (parent's F1 %.3f)"
              % (bi, lv, F1[bi]))
        ok(abs(lv - F1[bi]) <= REPRO_TOL, "F1 box %d: %.3f vs %.3f"
           % (bi, lv, F1[bi]))
        li, zi, _e, _ff, _fo = EB.image_level([data], key)
        print("  box %d h = 2 S5b-convention image level %.3f (parent's "
              "%.3f)" % (bi, li, S5B[bi]))
        ok(abs(li - S5B[bi]) <= REPRO_TOL, "S5b box %d: %.3f vs %.3f"
           % (bi, li, S5B[bi]))
    new = [boxes[i] for i in NEW]
    if new:
        gaps = []
        for key, want in sorted(F4.items()):
            lv, z, _e, n3 = EB.level_of(new, key)
            nf = sum(d['nfields'].get(key_str(key), 0) for d in new)
            print("  h = %d %s new boxes uniform level %.4f (parent's F4 "
                  "%.3f; %d fields, %d all-principal)"
                  % (key[0], key[1], lv, want, nf, n3))
            gaps.append(abs(lv - want))
        print("  F4 worst gap %.4f" % max(gaps))
        ok(max(gaps) <= 0.025, "F4 off by %.4f" % max(gaps))
    worst = 0.0
    for data in boxes:
        for ks in data['un']:
            for bb, cell in data['un'][ks].items():
                worst = max(worst, abs(sum(cell['w_qk'].values())
                                       - cell['cN']),
                            abs(sum(cell['e_qk'].values()) - cell['c3']))
        for ks in data['ram']:
            for bb, cell in data['ram'][ks].items():
                worst = max(worst, abs(sum(cell['w_qk'].values())
                                       - cell['cN']),
                            abs(sum(cell['e_qk'].values()) - cell['c3']))
    print("  by-source sums against the pooled cN and c3: worst gap %.2e"
          % worst)
    ok(worst < 1e-9, "by-source sums off by %.2e" % worst)


def c2_summand(boxes):
    section("C2  THE SUMMAND BAR -- Bernoulli replicates of one stratum's "
            "image count at its measured weights and shares")
    rng = random.Random(1171)
    for key, sel in (((2, 'A'), [boxes[0]]),
                     ((4, 'A'), [boxes[i] for i in NEW] or boxes),
                     ((5, 'A'), [boxes[i] for i in NEW] or boxes)):
        L = levels(sel, key)
        if L is None:
            continue
        g = L['g']
        share = CT.share_of(*key)
        ns = L['ns']
        terms = [(t[0], p_of(tag, t), unit_weight(tag))
                 for tag, t in g['terms'].items()]
        reps = []
        for _ in range(500):
            cnt = sum(1 for _i in range(ns) if rng.random() < share)
            for (w, p, u) in terms:
                m = int(round(w / u))
                cnt += u * sum(1 for _i in range(m) if rng.random() < p)
            reps.append(cnt / L['exp_i'])
        mean = sum(reps) / len(reps)
        sd = math.sqrt(sum((x - mean) ** 2 for x in reps) / (len(reps) - 1))
        sd_pred = math.sqrt(g['var_raw'] + g['var']) / L['exp_i']
        sd_pois = 1.0 / math.sqrt(L['exp_i'])
        print("  h = %d: %d replicates, level %.4f, spread %.4f against "
              "the summand sd %.4f (Poisson %.4f)"
              % (key[0], len(reps), mean, sd, sd_pred, sd_pois))
        ok(abs(mean - 1) < 3 * sd / math.sqrt(len(reps)),
           "C2 mean %.4f" % mean)
        ok(abs(sd - sd_pred) <= 0.15 * sd_pred, "C2 sd %.4f vs %.4f"
           % (sd, sd_pred))


def p_of(tag, t):
    return t[2] / t[0] if t[0] > 0 else 0.0


# --------------------------------------------------------------- prints
def s3_sources(boxes):
    section("S3  THE TERMS BY SOURCE AND POWER -- weight, landed on e, "
            "expected at the image share and at the uniform share")
    sel = [boxes[i] for i in NEW] or boxes
    for key in ((2, 'A'), (4, 'A'), (5, 'A'), (7, 'A')):
        L = levels(sel, key)
        if L is None:
            continue
        h = key[0]
        print("  h = %d (new boxes): raw split primes %d, all-principal %d "
              "(uniform %.1f)" % (h, L['ns'], L['n3'], L['ns'] / (h * h)))
        agg = {}
        for tag, t in L['g']['terms'].items():
            kd, q, kk = tag.split(":")
            a = agg.setdefault((kd, int(kk)), [0.0, 0.0, 0.0])
            for i in range(3):
                a[i] += t[i]
        print("    %-10s %2s %8s %8s %8s %8s  %s"
              % ("source", "k", "weight", "landed", "image", "uniform",
                 "share(image)"))
        for (kd, kk), (w, e, ex) in sorted(agg.items()):
            if w < 1e-9:
                continue
            print("    %-10s %2d %8.2f %8.2f %8.2f %8.2f  %.3f"
                  % (kd, kk, w, e, ex, w / (h * h), ex / w))


def s4_strata(boxes):
    section("S4  THE LEVEL BY STRATUM -- uniform (Poisson bar) and image "
            "(summand bar; Poisson bar), the forcing F, the uncompensated "
            "fraction f, the three nulls")
    print("  f = 1 is the image null, 0 the naive explicit formula, "
          "1 - c_RS the Chebyshev null.")
    out = {}
    for label, sel in (("all boxes", list(boxes)),
                       ("new boxes (24000, 96000]",
                        [boxes[i] for i in NEW])):
        if not sel:
            continue
        print("  -- %s --" % label)
        print("  %-8s %6s %7s %7s | %7s %7s %7s | %6s %6s %6s %6s %6s"
              % ("stratum", "fields", "uniform", "z", "image", "z_sum",
                 "z_pois", "F", "f", "sig_f", "1-cRS", "raw"))
        keys = set()
        for data in sel:
            keys.update(key_of(k) for k in data['nfields'])
        for key in sorted(keys):
            L = levels(sel, key)
            if L is None:
                continue
            nf = sum(d['nfields'].get(key_str(key), 0) for d in sel)
            readable = L['exp_u'] >= MIN_READ and key[1] != 'D'
            print("  h=%-3d %s %6d %7.3f %7s | %7.3f %7s %7s | %6.3f %6s "
                  "%6s %6s %6s%s"
                  % (key[0], key[1], nf, L['lu'], fz(L['zu']), L['li'],
                     fz(L['zi']), fz(L['zip']), L['F'], fmt(L['f']),
                     fmt(L['sf']), fmt(1 - L['c_rs'] if L['c_rs'] is not
                                       None else None), fmt(L['lr']),
                     "  readable" if readable else ""))
            out[(label, key)] = (L, readable)
    return out


def s5_boxes_bins(boxes):
    section("S5  h = 2 BY BOX, AND THE RAW LEVEL BY BIN -- where the "
            "shortfall sits")
    key = (2, 'A')
    print("  h = 2 by box: uniform | image (summand z) | F f | raw")
    for bi, data in enumerate(boxes):
        L = levels([data], key)
        print("  (%5d, %5d]  %.3f | %.3f (%s) | %.3f %s | %.3f (%s)"
              % (BOXES[bi][0], BOXES[bi][1], L['lu'], L['li'], fz(L['zi']),
                 L['F'], fmt(L['f']), L['lr'], fz(L['zr'])))
    sel = [boxes[i] for i in NEW] or boxes
    print("  by bin over the new boxes: image level (z) | raw level (z) | "
          "uniform level")
    raw_bins = {}
    keys = set()
    for data in sel:
        keys.update(key_of(k) for k in data['nfields'])
    for key in sorted(keys):
        L = levels(sel, key)
        if L is None or L['exp_u'] < MIN_READ or key[1] == 'D':
            continue
        cols = []
        for bb in range(len(BIN_EDGES) - 1):
            Lb = levels(sel, key, bins=(bb,))
            if Lb is None:
                cols.append("%-22s" % "--")
                continue
            cols.append("%.2f(%s) %.2f(%s) %.2f" % (Lb['li'], fz(Lb['zi']),
                                                  Lb['lr'] or 0.0,
                                                  fz(Lb['zr']), Lb['lu']))
            raw_bins[(key, bb)] = Lb
        print("  h=%-3d %s  %s" % (key[0], key[1], " | ".join(cols)))
    return raw_bins


def s6_structure(boxes):
    section("S6  THE STRUCTURE CENSUS -- |Cl[m]| for m = 1..9 per stratum")
    agg = {}
    for data in boxes:
        for ks, sk in data['struct'].items():
            a = agg.setdefault(ks, {})
            for name, n in sk.items():
                a[name] = a.get(name, 0) + n
    for ks in sorted(agg, key=lambda s: key_of(s)):
        print("  %-6s %s" % (ks, "; ".join("%s x%d" % (n, c) for n, c in
                                          sorted(agg[ks].items()))))


def s7_verdict(strata, raw_bins):
    section("S7  THE VERDICT -- P1-P4")
    new = "new boxes (24000, 96000]"
    allb = "all boxes"
    # P1 / P2
    kills, below = [], []
    for (label, key), (L, readable) in strata.items():
        if label != new or not readable or key[0] < 4:
            continue
        if L['zi'] > 2:
            kills.append((key, L['li'], L['zi']))
        below.append((key, L['li'], L['zi'], L['f'], L['sf'], L['c_rs']))
    print("  P1: readable strata at h >= 4 more than 2 sigma above 1: %s"
          % (["h=%d %s %.3f z=%+.2f" % (k[0], k[1], l, z)
              for (k, l, z) in kills] or "none"))
    print("      -> %s" % ("KILL: something beyond the forcing is in the "
                           "level" if kills else "the prediction "
                           "holds: no readable stratum above 1"))
    p2 = all(z < -2 and 0.50 <= l <= 0.85 for (k, l, z, f, sf, c) in below)
    print("  P2: every readable h >= 4 stratum below 1 by > 2 sigma and in "
          "[0.50, 0.85]: %s  (%s)"
          % (p2, ", ".join("h=%d %.3f z=%+.2f" % (k[0], l, z)
                           for (k, l, z, f, sf, c) in below)))
    L2 = strata.get((allb, (2, 'A')))
    if L2:
        L2 = L2[0]
        print("      h = 2 all boxes: image %.3f (z %s), in [0.75, 0.90]: %s"
              % (L2['li'], fz(L2['zi']), 0.75 <= L2['li'] <= 0.90))
        print("  P3: f at h = 2 (all boxes) %.3f +- %.3f, in [0.10, 0.35]: %s"
              % (L2['f'], L2['sf'], 0.10 <= L2['f'] <= 0.35))
    p3 = all(f is not None and 0.20 <= f <= 0.60
             for (k, l, z, f, sf, c) in below)
    print("      f at readable h >= 4 (new boxes) in [0.20, 0.60]: %s  (%s)"
          % (p3, ", ".join("h=%d f=%.2f+-%.2f" % (k[0], f, sf)
                           for (k, l, z, f, sf, c) in below)))
    if L2:
        d = (1 - L2['c_rs']) - L2['f']
        print("  P4: Chebyshev null at h = 2: 1 - c_RS = %.3f against f = "
              "%.3f +- %.3f, above by %.1f sigma: %s"
              % (1 - L2['c_rs'], L2['f'], L2['sf'], d / L2['sf'],
                 d / L2['sf'] > 2))
    b0 = raw_bins.get(((2, 'A'), 0))
    b3 = raw_bins.get(((2, 'A'), 3))
    if b0 and b3:
        s0 = math.sqrt(b0['ns'] * 0.25 * 0.75) / (b0['ns'] * 0.25)
        s3 = math.sqrt(b3['ns'] * 0.25 * 0.75) / (b3['ns'] * 0.25)
        gap = (b3['lr'] - b0['lr']) / math.sqrt(s0 ** 2 + s3 ** 2)
        rows = [raw_bins[((2, 'A'), bb)]['lr'] for bb in range(4)]
        print("      raw level by bin at h = 2 (new boxes): %s; rising: %s; "
              "[300, 1000) above [3, 30) by %.1f sigma: %s"
              % (", ".join("%.3f" % x for x in rows),
                 all(rows[i] < rows[i + 1] for i in range(3)), gap,
                 gap > 3))


def main():
    t0 = time.time()
    c0_shares()
    fields = EB.s1_population()
    boxes = s2_boxes(fields)
    del fields
    gc.collect()
    c1_reproduce(boxes)
    c2_summand(boxes)
    s3_sources(boxes)
    strata = s4_strata(boxes)
    raw_bins = s5_boxes_bins(boxes)
    s6_structure(boxes)
    s7_verdict(strata, raw_bins)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall this process; box walls %s"
          % (CHECKS, time.time() - t0,
             ["%.0f" % d['wall'] for d in boxes]))


if __name__ == "__main__":
    main()
