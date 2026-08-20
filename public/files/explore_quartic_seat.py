r"""THE QUARTIC SEAT -- is the generating class's seat at a cubic field's
least places a fact about the S4 quartic field whose cubic resolvent it
is? (sibling of explore_ceiling_early.py, whose wide population and rank
statistic it reads; the class records come from the same chain.)

THE QUESTION. Over the cyclic cubic class groups of the wide box the
least partial place of a field -- the degree-1 place over the smallest
odd prime of splitting type (1, 2) -- lies in a GENERATING class 0.283 +-
0.032 above the uniform share phi(h)/h, the excess decaying over the
rank of the place in its field's own norm order and surviving a
generation-conditioned null at a tenth of its size
(explore_ceiling_early.py F2, C5). Nothing in that reading says WHY.
This file reframes the seat through class field theory and asks two
things of the reframe: whether it is RIGHT, checked against an object
built independently of the class records, and whether it KILLS the
reading the sibling filed -- rank, not norm -- with a contrast the old
frame could not state.

THE HAND-ATTACK (pre-engine, on paper).

  (1) THE DICTIONARY. Let K be a complex cubic field whose class group
      has 2-rank 1 (cyclic of even order, and nothing else in this box
      below Z/2 x Z/4). K has exactly one unramified quadratic extension
      M, the fixed field of 2Cl under the Artin map, and the Galois
      closure N of M over Q has group S4: K is the fixed field of a
      dihedral D4 (the stabiliser of one of the three pairings of four
      letters), M the fixed field of the Klein four-group V inside that
      D4 holding its two disjoint transpositions, and the fixed field of
      a point stabiliser S3 is a QUARTIC field F whose cubic resolvent
      is K -- Heilbronn's correspondence, one F per nontrivial element of
      Cl[2]. An unramified prime p's Frobenius class in S4 reads off K's
      records: a 3-cycle fixes no pairing, so p is INERT in K; a double
      transposition fixes all three, so p SPLITS in K; a transposition
      or a 4-cycle fixes exactly one, so p is PARTIAL in K. Within the
      partial type the degree-1 place P of K corresponds to the fixed
      pairing's D4, and P splits in M exactly when the Frobenius lies in
      that D4's V -- which a transposition does and a 4-cycle does not.
      So for a partial prime: P in 2Cl <-> transposition <-> p of type
      (1, 1, 2) in F; P a non-square <-> 4-cycle <-> p INERT in F. For a
      split prime with classes (c1, c2, c3), c1 + c2 + c3 = 0: the
      identity puts all three in 2Cl (p totally split in F); a double
      transposition (12)(34) lies in the V of the pairing {12|34} and in
      neither other V, so exactly ONE of the three places is in 2Cl (p
      of type (2, 2) in F). Zero or two in 2Cl is impossible, the image
      of the sum in Cl/2Cl being 0. Every cycle type of F is therefore a
      FUNCTION of the records the corpus already holds, and the seat
      reads: the smallest partial prime of K is inert in F far more
      often than the Chebotarev share 1/2 of the partial primes -- a
      bias between two classes of S4 of the same size, neither of which
      is a square in S4 or has a square root there, so no prime-power
      term of any explicit formula separates them.

  (2) THE FRAME MAKES h A NUISANCE PARAMETER. The S4 statement is about
      Cl/2Cl, so it is the same statement at every even h: the least
      partial place is a NON-SQUARE. At h = 4 and h = 8 the non-squares
      ARE the generating classes, and the sibling's generator cell is
      this cell; at h = 6 the non-squares are {1, 3, 5} and the
      generator cell {1, 5} is a subset; at h = 2 a non-square is simply
      a NON-PRINCIPAL place, which the sibling never read, its cell
      needing a class of order h > 2 to differ from the trivial one. The
      non-square indicator has expectation 1/2 at EVERY even h under the
      uniform nominal, so the strata pool without weights, and h = 2 --
      the largest stratum of the box -- enters the read for the first
      time. If the seat is one S4 fact, h = 2 reads the same excess as
      h = 4; if it is a fact about ORDERS within the group, the strata
      part.

  (3) RANK AGAINST NORM, THE CONTRAST THE OLD FRAME COULD NOT STATE. The
      sibling's rank read and its window read are consistent with two
      different seats: an excess e(r) that is a function of the place's
      RANK (the field's least place is a non-square whatever prime it
      sits at), or an excess e(p) that is a function of the place's
      NORM (a partial prime at p = 5 is a non-square with some share
      whether or not 3 was partial). The two agree on every marginal the
      sibling printed, because small ranks sit at small primes. They
      part on the two-way table of (p, rank): under e(r), at a fixed
      prime p the share at rank 1 exceeds the share at rank >= 2 and at
      a fixed rank it does not move with p; under e(p) the reverse.
      Conditioning on p = p_1 IS conditioning on the splitting of every
      prime below it -- none partial -- which is the conditioning set
      the aim names, and it is not the place's own class. The table is
      sparse by construction: 3 is always rank 1; 5 is rank 1 or 2; the
      cell (p, r) needs r - 1 partial primes below p, and the share of
      fields in which the first r - 1 odd primes are all partial is
      2^-(r-1) at the Chebotarev rate, so rank 1 at p = 13 is one field
      in sixteen. Each cell is a Bernoulli mean with standard error
      sqrt(s(1-s)/N) -- read here with the NULL's variance, sqrt(1/4N),
      0.11 at N = 20, because the empirical bar of a unanimous small cell
      is ZERO and an inverse-variance weight on it blows up (the
      rehearsal found exactly that cell); the contrast D between rank 1 and
      rank >= 2 at a fixed p is read pooled over the primes whose two
      cells both hold at least 15 fields, inverse-variance weighted, and
      the slope S of the rank-1 share on p over the cells of at least 15
      fields by weighted least squares. The kill and its converse are
      both frozen on these two observables (P3), and a null and TWO
      planted effects, one of each seat, are run first so that D and S
      are known to SEPARATE the seats before either is read (C6, C7).

  (4) BUILDING F WITHOUT THE CLASS RECORDS. The dictionary is a
      function of the records, so reading it back from the records tests
      nothing; the control builds F from the ORDER alone. Take a partial
      prime p whose degree-1 place P has a class of even order 2m; then
      I = P^m has order 2 and I^2 is principal, generated by some alpha
      with |N(alpha)| = p^(2m) -- a box search in the ideal I^2's reduced
      basis, the parents' generator search. M = K(sqrt x) for some x in
      the Selmer group {x : (x) is a square ideal} / squares, which is
      spanned by alpha, -1 and a fundamental unit: eight classes, of
      which the unramified one is the unique nontrivial class that is
      POSITIVE at the real embedding (the narrow and wide class groups
      coincide at one real place, so M is unramified at infinity too)
      and a SQUARE MODULO 4, the condition for no ramification at the
      places above 2 of an element prime to 2. So the candidates are the
      real-positive members of {+-alpha, +-u alpha, +-u} for a unit u
      that is not a square -- three classes -- and exactly one must pass
      the mod-4 test. TWO passing would exhibit two unramified quadratic
      extensions and refute the 2-rank the relation lattice assigned;
      NONE passing, once u is known not to be a square class, would say
      the lattice's order-2 class is not one. The test is therefore an
      INDEPENDENT check of the 2-part of the class reading, and it is
      the part the seat rides on. The unit comes from the same box
      search at norm 1, and whether it is a square class is read off
      its quadratic residues at the field's degree-1 places (a square
      is a residue everywhere; a non-square is a non-residue at half of
      them), so a unit that reads as +-square at a dozen places is
      discarded for the next one the box holds.

  (5) THE QUARTIC FROM THE KUMMER GENERATOR. With x = alpha chosen, F =
      Q(theta) for theta = (sqrt a1 + sqrt a2 + sqrt a3)/2 over the
      conjugates a_i of alpha, the signs fixed by their product being
      the rational square root of N(alpha). Ferrari's resolvent inverts
      exactly: for a depressed quartic with roots t_i summing to zero
      the three numbers (t1 + t2)^2, (t1 + t3)^2, (t1 + t4)^2 have
      elementary symmetric functions -2p, p^2 - 4r and q^2 in the
      quartic's coefficients x^4 + p x^2 + q x + r (checked by hand on
      x^4 - 1, (x^2 - 1)(x^2 - 4) and (x - 3)(x + 1)^3), so if alpha has
      characteristic polynomial z^3 - s1 z^2 + s2 z - s3 then 2 theta is
      a root of
          g(X) = X^4 - 2 s1 X^2 + 8 sqrt(s3) X + (s1^2 - 4 s2),
      an integer polynomial, the sign of the linear term immaterial (X
      -> -X). Two checks ride on it: g is irreducible over Q (M is not
      the compositum of K with a quadratic field, the closure being S4
      and not S3 x C2), and disc(g) = d_K times a square, the quartic
      field's discriminant being EQUAL to the cubic resolvent's when
      M/K is unramified (Heilbronn). The cycle type of p in F is the
      factorisation pattern of g mod p wherever p does not divide
      disc(g), read as the number of roots of g in F_p and the degree of
      gcd(g, X^(p^2) - X): (1,1,1,1), (1,1,2), (1,3), (2,2) and (4)
      have root counts 4, 2, 1, 0, 0 and the last two gcd degrees 4 and
      0. The primes dividing disc(g) but not d_K are index primes of
      Z[theta] and are skipped, counted.

THE DESIGN. The wide population of explore_ceiling_topband.py (|d| <=
24000, every complex cubic field the class reading resolved), restricted
to class groups of 2-rank 1 and to fields carrying at least MIN_TOT
partial places below 250 (the sibling's floor), which at h = 4, 6, 8 is
exactly the sibling's 185 cyclic fields and adds every other even h.
Per field: the S4 class of every odd unramified prime to 1000 from the
records; the quartic F built as in (4) and (5) and read against them;
the non-square indicator by rank of the partial place (ranks 1 to 10,
pooled 1-3, 4-6, 7-10), per stratum and pooled; the (p, rank) table for
p = 3 to 23 and rank 1, 2, 3, >= 4; at rank 1 and fixed p, the share
split by whether a totally split prime sits below p.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE DICTIONARY HOLDS. In every field where F is built, the cycle
      type read from g mod p agrees with the type the records predict
      at EVERY readable prime -- a control that must pass before any
      statistic is read; one disagreement stops the run.
  P2  ONE S4 FACT. Pooled over every 2-rank-1 stratum the non-square
      excess at rank 1 is at least 0.20 at 3 sigma, and the h = 2
      stratum's rank-1 excess lies within 2 sigma (the two bars summed
      in quadrature) of the h = 4 stratum's.
  P3  THE SEAT IS THE NORM, NOT THE RANK (against the sibling's filed
      reading, stated as this file's guess: the mechanisms a field's
      arithmetic offers -- Euler factors, secondary terms, the size of
      the field -- are functions of p and |d|, not of a place's rank).
      Frozen: D lies within 2 sigma of zero and S is negative at 2
      sigma. The converse, rank-seated: D >= 0.10 at 2 sigma with S
      within 2 sigma of zero. Anything else is MIXED and is reported as
      such.

THE CONTROLS, run before any prediction is read.

  C1  THE TRIPLE PARITY. Over every split prime in the records, the
      number of the three classes lying in 2Cl is 1 or 3, never 0 or 2.
  C2  THE QUARTIC. For every built F: g irreducible over Q; disc(g) a
      square multiple of d_K; on the first three built fields, the four
      complex roots of g summed in pairs, squared, reproduce the roots
      of alpha's characteristic polynomial to 1e-6.
  C3  THE SELMER SELECTION. In every field with a non-square unit in
      hand, exactly ONE real-positive candidate is a square mod 4;
      fields where none is, or where no non-square unit was found in
      the box, are printed with their discriminants and counted, never
      silently dropped. Two passing is a FAIL.
  C4  THE DICTIONARY AGAINST F (P1's mechanism): agreements and
      disagreements per S4 class, and the index primes skipped.
  C5  THE REPRINT. The h = 4 stratum's ranks 1-3 pooled generator
      excess reads +0.190 within 0.003 of the sibling's print on 101
      fields, and the generator cell's rank-1 excess pooled over h = 4,
      6, 8 reads +0.283 within 0.003 on 185.
  C6  THE NULL for D and S: one seeded uniform re-sort of every partial
      place's class, the table rebuilt; D and S within 3 sigma of zero.
  C7  THE PLANTED SEATS: on the re-sorted classes, a rank-planted
      population (the rank-1 place made a non-square with probability
      0.75 whatever its prime) must read D at least 3 sigma above zero
      with S within 2 sigma of zero, and a norm-planted population (a
      partial place at p made a non-square with probability 0.5 +
      0.9/p whatever its rank) must read S at least 3 sigma below zero
      with D within 2 sigma of zero -- the two observables shown to
      separate the seats before the real table is read.

THE FINDINGS (the post-run record; every number is a print of the run).

  THE POPULATION. 1283 mapped complex fields, 695 of even class number,
  686 of 2-rank 1 and all 686 over the place floor: h = 2 (484 fields),
  4 (101), 6 (65), 8 (19), 10 (9), 12 (5), 14 (2), 16 (1); every one
  cyclic.

  CONTROLS. C1: 17051 split primes, every triple with 1 or 3 classes in
  2Cl. C2-C4: 616 of the 686 fields built -- 47 where no generator of
  I^2 was found in boxes to 12, 22 where the box held no non-square unit,
  1 with no order-2 ideal of norm below 10^9, each printed with its
  discriminants; in 198 of the 616 the unramified extension is generated
  by the UNIT alone, in 211 by u alpha and in 207 by alpha. Every g
  irreducible with disc(g) = d_K times a square; the pairing identity
  holds to 1.6e-16 on three fields; exactly one real-positive Selmer
  candidate is a square mod 4 in every built field, never two, never
  none. C4: 101,592 readings of g mod p against the records' prediction
  -- 27096 4-cycles, 35731 3-cycles, 23697 transpositions, 11828 double
  transpositions, 3240 identities -- and 0 disagreements, 499 index
  primes skipped. C5: +0.190 +- 0.023 on 101 fields and +0.283 +- 0.032
  on 185, the sibling's prints exactly. C6: the null reads D +0.030 +-
  0.034 and S +0.010 +- 0.007. C7: the rank plant reads D +0.268 +- 0.034
  (7.8 sigma) with S +0.004 +- 0.007, the norm plant S -0.035 +- 0.007
  (-4.8 sigma) with D +0.020 +- 0.034: the two observables separate the
  seats as designed.

  F1  P1 PASSES: THE DICTIONARY HOLDS (rule, verified across 616 fields
      and 101,592 primes). The class a partial place carries mod 2Cl, and
      the count of a split triple's classes in 2Cl, predict the cycle
      type of the prime in the quartic field built from the order alone,
      at every readable prime of every field, without exception. Since
      the quartic was built without the relation lattice -- from a
      generator, a unit, a sign and a congruence mod 4 -- this is an
      independent certificate of the 2-part of every class label in the
      616 fields built, and of the 2-rank the lattice assigned there: a wrong 2-rank
      would have shown as two passing Selmer candidates or none, and a
      wrong label as a wrong pattern mod p.

  F2  P2 PASSES: THE SEAT IS ONE S4 FACT, AT EVERY EVEN h (observation,
      686 fields). The non-square share of the least partial place minus
      1/2: h = 2 +0.341 +- 0.017, h = 4 +0.322 +- 0.038 (0.5 sigma
      apart), h = 6 +0.392 +- 0.039, h = 8 +0.184 +- 0.110; pooled +0.338
      +- 0.014 at rank 1 (24 sigma), then 0.222, 0.179, 0.125, 0.160,
      0.121 through rank 6 and 0.103 +- 0.019 at rank 10 (5.5 sigma);
      pooled +0.246 +- 0.009 over ranks 1-3, +0.136 +- 0.010 over 4-6,
      +0.109 +- 0.009 over 7-10. At h = 6 the non-square cell, {1, 3, 5},
      reads +0.392 +- 0.039 at rank 1 where the generator cell {1, 5}
      reads +0.251 +- 0.062: the class of order 2 carries the bias too,
      so the cell the seat lives on is Cl/2Cl and not the generators. At
      h = 2 the statement is that a field's least partial place is
      NON-PRINCIPAL 84 times in 100.

  F3  P3 READS MIXED BY THE FROZEN LETTER, AND THE GUESS IS REFUTED: THE
      SEAT IS GRADED BY RANK AND FLAT IN THE NORM (observation). The
      non-square share by (p, rank) -- rank 1: 0.850 (p = 3, 273 fields),
      0.849 (5, 199), 0.795 (7, 117), 0.880 (11, 50), 0.714 (13, 21);
      rank 2: 0.764, 0.753, 0.710, 0.788, 0.726, 0.571, 0.655 at p = 5
      through 23 and 0.452 +- 0.090 over 29-50; rank 3: 0.655, 0.721,
      0.736, 0.672, 0.663, 0.585 at p = 7 through 23, 0.634 over 29-50;
      rank >= 4: 0.630, 0.584, 0.607, 0.655, 0.645 at p = 11 through 23,
      0.628 +- 0.012 over 29-50 (1844 places), 0.616 +- 0.011 over 50-100
      (2048), 0.570 +- 0.033 over 100-250 (235). So D = +0.088 +- 0.034
      (2.6 sigma, under the frozen 0.10) and S = -0.005 +- 0.007: the
      norm-seated reading this file guessed dies on S and on the rank >=
      4 row, flat to within its bars across a twentyfold range of p, and
      the rank-seated reading holds its sign at 2.6 sigma but not its
      frozen size. What stands: a place's share of non-squares is a
      function of its RANK -- about 0.85 at rank 1, 0.75 at rank 2, 0.70
      at rank 3, 0.62 from rank 4 on -- and not of the prime it sits at,
      up to p = 250. Conditioning on the primes below the least place
      (the aim's kill) leaves the rank-1 share at 0.85 at every p from 3
      to 11; a totally split prime below it lowers the share by 0.15 +-
      0.11 at p = 5 and 0.08 +- 0.09 at p = 7, a hint and not a read.

  F4  THE |d| READ (descriptive, added after the slate): the rank-1 share
      falls with the discriminant at -0.039 +- 0.019 per unit of log|d|
      pooled (-0.039 +- 0.022 at h = 2), 0.892 +- 0.046 below |d| = 6000,
      0.855 +- 0.039 to 12000, 0.815 +- 0.025 to 24000 -- a 2-sigma
      slope, a finite-discriminant component at most.

WHAT IS NOT CONTROLLED. The mechanism. The reframe states the seat as
the order statistics of S4's two odd classes in a quartic field -- the
first partial prime is a 4-cycle 85 times in 100, the fourth and later
62 -- independent of the prime's size; no Chebotarev or prime-power term
distinguishes the two classes, and whether a secondary term of the
quartic count, or the conditioning on an even class number, or something
with a name produces it is left open. The 70 unbuilt fields are not read
by the control and not excluded from the statistic.

RUN RECORD. 2026-08-20, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_quartic_seat.py`.
One process, CPython, no BLAS. 1242 checks passed, 769.7 s wall, peak working
set 170.8 MB against the 512 MB ceiling; the class reading is the whole
of the wall and the probe itself 25 s. Rehearsed at 86 fields with the
dictionary read to 200 (4 s), which found a unanimous five-field cell
with an empirical bar of zero blowing up an inverse-variance weight --
the bars became the null's sqrt(1/4N). The first full run overflowed the
parents' float LLL on an ideal of norm p^16, whence NORM_CAP; the second
read ONE field, d = -22612, with no Selmer candidate passing, and the
cause was a float sign: a unit with coordinates near 10^6 has a real
embedding near 10^-12, read with the wrong sign at the real root, and
its negative -- real-positive and a square mod 4 -- was the generator
the field needed. The sign is now the sign of the norm, exact; the same
run had also offered a unit and its negative as two units. Every
statistic of the third run reprints in the fourth, this one, which added
F4 and nothing else.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import pickle
import random
import sys
import time
from collections import defaultdict
from fractions import Fraction
from math import isqrt, log, sqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_squares as SQ               # noqa: E402
import explore_ceiling_curve as CV                 # noqa: E402
import explore_ceiling_constant as EC              # noqa: E402
import explore_cubic_field_shop as CFS             # noqa: E402
import explore_cubic_principal as ECP              # noqa: E402
import explore_cubic_transposition as XT           # noqa: E402
from explore_principal_share import primes_upto    # noqa: E402

CHECKS = 0
SEED = 20885
RANKS = 10
RANK_POOLS = ((1, 3), (4, 6), (7, 10))
TABLE_PRIMES = (3, 5, 7, 11, 13, 17, 19, 23)
TABLE_BANDS = ((29, 50), (50, 100), (100, 250), (250, 1000))   # descriptive
TABLE_RANKS = (1, 2, 3, 4)                 # 4 means rank >= 4
MIN_CELL = 15
READ_CAP = 1000                            # primes the dictionary is read to
SELECT_CAP = 100                           # partial primes offered for alpha
NORM_CAP = 10 ** 9                         # |N(alpha)| the float LLL can hold
RESIDUE_PLACES = 12                        # places a unit's square class reads at
REPRINT_H4 = (0.190, 0.003)
REPRINT_GEN = (0.283, 0.003)
PLANT_RANK = 0.75
PLANT_NORM = 0.9
ONE3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
QUICK = os.environ.get("QSEAT_QUICK") == "1"    # the rehearsal: 80 fields
if QUICK:
    READ_CAP, MIN_CELL = 200, 5


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


mean_se = CV.mean_se
fmt = EC.fmt


# ------------------------------------------------------------- the records
def records():
    """Every resolved complex field of the wide box with a 2-rank-1 class
    group and the sibling's place floor, with its ORDER kept (the
    sibling's records drop it). QSEAT_CACHE may name a pickle of the
    mapped records, for iteration; the default runs the class reading."""
    cache = os.environ.get("QSEAT_CACHE")
    if cache and os.path.exists(cache):
        with open(cache, "rb") as fh:
            mapped = pickle.load(fh)
        print("  mapped records read from %s" % cache)
    else:
        import explore_ceiling_topband as TB
        mapped = XT.s3_profiles(TB.wide_class_reading())
    out = records_from(mapped)
    if QUICK:
        stride = max(1, len(out) // 80)
        out = out[::stride]
        print("  (rehearsal: every %d-th field, %d kept)" % (stride, len(out)))
    return out


def records_from(mapped):
    """The filter alone, on any mapped list (the sibling
    explore_quartic_second.py hands it the increment's)."""
    pop3 = CV.build_pop3(mapped)
    out = []
    n_even = n_r1 = 0
    for (m, f) in zip(mapped, pop3):
        (d, cx, a, b, c, O, H, piv, k, per_prime, prof) = m
        if H % 2:
            continue
        n_even += 1
        G = SQ.group_deg3(piv, k, H)
        two = sum(1 for key in G.keys if G.dbl[key] == G.triv)
        if two != 2:
            continue
        n_r1 += 1
        if sum(1 for (p, key) in f[2] if p < SQ.CUTS[0]) < CV.MIN_TOT:
            continue
        types = {}
        dropped = 0
        for (p, kd, vecs) in per_prime:
            if any(v is None for v in vecs):
                dropped += 1
                types[p] = 'dropped'
                continue
            if kd == 'split':
                types[p] = ('split', tuple(XT.reduce_vec(v, piv)
                                           for v in vecs))
            else:
                types[p] = ('partial', XT.reduce_vec(vecs[0], piv))
        out.append(dict(d=d, a=a, b=b, c=c, O=O, cx=cx, G=G, h=H,
                        types=types, places=list(f[2]), dropped=dropped,
                        cyclic=CV.cyclic_profile(H, f[1])))
    print("  %d mapped fields, %d of even class number, %d of 2-rank 1,"
          " %d over the place floor" % (len(mapped), n_even, n_r1,
                                        len(out)))
    return out


def s4_class(rec, p):
    """The records' prediction of p's cycle type in F, or None."""
    if p == 2 or rec['d'] % p == 0:
        return None
    t = rec['types'].get(p)
    if t is None:
        return '13'
    if t == 'dropped':
        return None
    G = rec['G']
    if t[0] == 'partial':
        return '4' if t[1] not in G.squares else '112'
    n_sq = sum(1 for key in t[1] if key in G.squares)
    if n_sq == 3:
        return '1111'
    if n_sq == 1:
        return '22'
    return 'BAD'


# ------------------------------------------------------------- the order
def theta_vec(O, v):
    return [sum(Fraction(v[i]) * O.basis[i][j] for i in range(3))
            for j in range(3)]


def real_positive(O, v):
    """The sign at the real embedding, EXACTLY: N(v) = v_real |v_cx|^2 in
    a complex cubic field, so the sign of the norm is the sign of the real
    embedding. A float evaluation at the real root cancels to noise on a
    unit with million-sized coordinates, whose real value is ~1e-12 (the
    first full run read one such sign wrong and built nothing there)."""
    return O.norm(v) > 0


def char_poly(O, v):
    """(s1, s2, s3) of the multiplication-by-v matrix."""
    M = [O.mul(v, tuple(1 if j == i else 0 for j in range(3)))
         for i in range(3)]
    s1 = M[0][0] + M[1][1] + M[2][2]
    s2 = (M[0][0] * M[1][1] - M[0][1] * M[1][0]
          + M[0][0] * M[2][2] - M[0][2] * M[2][0]
          + M[1][1] * M[2][2] - M[1][2] * M[2][1])
    s3 = CFS.det3(M)
    return s1, s2, int(s3)


def residue_at(O, v, p, r):
    """v mod the degree-1 place (p, theta - r), as an element of F_p."""
    t = theta_vec(O, v)
    acc = 0
    for j in range(3):
        num, den = t[j].numerator, t[j].denominator
        if den % p == 0:
            return None
        acc = (acc + num * pow(den, -1, p) * pow(r, j, p)) % p
    return acc


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def residue_places(rec):
    """(p, r) over the first partial primes off the polynomial
    discriminant, where the cubic has one root mod p."""
    a, b, c = rec['a'], rec['b'], rec['c']
    pdisc = CFS.poly_disc3(a, b, c)
    out = []
    for p, t in sorted(rec['types'].items()):
        if t == 'dropped' or t[0] != 'partial' or pdisc % p == 0:
            continue
        rts = [r for r in range(p) if (((r + a) * r + b) * r + c) % p == 0]
        if len(rts) == 1:
            out.append((p, rts[0]))
        if len(out) >= RESIDUE_PLACES:
            break
    return out


def square_signature(O, v, rps):
    return tuple(legendre(residue_at(O, v, p, r), p) for (p, r) in rps)


def is_square_mod4(O, v):
    target = tuple(x % 4 for x in v)
    for x in range(4):
        for y in range(4):
            for z in range(4):
                sq = O.mul((x, y, z), (x, y, z))
                if tuple(t % 4 for t in sq) == target:
                    return True
    return False


def find_units(O, rows, cx, want=3, box=ECP.GEN_BOX):
    """Elements of norm +-1 other than +-1, from the parents' weighted
    reduced-basis search over the whole order."""
    found = []
    one = O.one
    neg_one = tuple(-x for x in one)
    for level in ECP.GEN_LEVELS:
        for w in ECP.weight_grid(cx, level):
            wrows = [[w[i] * rows[i][j] for j in range(3)]
                     for i in range(len(rows))]
            red = ECP.reduced_basis(O, ONE3, wrows)
            form = ECP.norm_form(O, red)
            for x in range(-box, box + 1):
                xp = (1, x, x * x, x ** 3)
                for y in range(-box, box + 1):
                    yp = (1, y, y * y, y ** 3)
                    A = [0, 0, 0, 0]
                    for (i, j, k), cf in form.items():
                        A[k] += cf * xp[i] * yp[j]
                    for z in range(-box, box + 1):
                        if x == 0 and y == 0 and z == 0:
                            continue
                        N = ((A[3] * z + A[2]) * z + A[1]) * z + A[0]
                        if N != 1 and N != -1:
                            continue
                        v = tuple(x * red[0][t] + y * red[1][t]
                                  + z * red[2][t] for t in range(3))
                        if v in (one, neg_one) or v in found:
                            continue
                        if tuple(-x for x in v) in found:
                            continue
                        if abs(O.norm(v)) != 1:
                            continue
                        found.append(v)
                        if len(found) >= want:
                            return found
    return found


def place_ideal(rec, p):
    """The HNF of the degree-1 place over a partial prime p."""
    O = rec['O']
    if p <= CFS.REL_PRIME_CAP:
        pl = [P for (P, e, f) in CFS.maximal_places(O, p) if f == 1]
    else:
        pdisc = CFS.poly_disc3(rec['a'], rec['b'], rec['c'])
        pl, kind = ECP.deg1_places(O, rec['a'], rec['b'], rec['c'],
                                   pdisc, p)
    assert pl is not None and len(pl) == 1, "partial prime without one place"
    return pl[0]


def build_quartic(rec, rows, gen_boxes=(ECP.GEN_BOX, 5, 8, 12),
                  unit_boxes=(ECP.GEN_BOX,)):
    """(g, alpha, info) or (None, None, reason). g is the integer
    coefficient list of X^4 + ... from the Kummer generator of the
    unramified quadratic extension, chosen as the hand-attack says. The
    box ladders default to this file's; a sibling may widen them."""
    O, G = rec['O'], rec['G']
    # the cheapest order-2 ideal: P^m with P of class order 2m
    best = None
    for p, t in sorted(rec['types'].items()):
        if p > SELECT_CAP:
            break
        if t == 'dropped' or t[0] != 'partial':
            continue
        o = G.order[t[1]]
        if o % 2:
            continue
        m = o // 2
        if p ** (2 * m) > NORM_CAP:
            continue
        if best is None or p ** (2 * m) < best[0]:
            best = (p ** (2 * m), p, m)
    if best is None:
        return None, None, 'no order-2 ideal of norm below the cap'
    target, p, m = best
    P = place_ideal(rec, p)
    I2 = CFS.ideal_pow_hnf(O, P, 2 * m)
    alpha = None
    for box in gen_boxes:
        try:
            alpha = ECP.find_gen(O, I2, rows, target, rec['cx'], box=box)
        except OverflowError:           # the float LLL on a huge lattice
            alpha = None
            break
        if alpha is not None:
            break
    if alpha is None:
        return None, None, 'no generator of I^2 found (norm %d)' % target
    rps = residue_places(rec)
    triv_sig = tuple(1 for _ in rps)
    neg_sig = tuple(legendre(-1, p) for (p, r) in rps)
    for ubox in unit_boxes:
        units = find_units(O, rows, rec['cx'], box=ubox)
        nonsq = [u for u in units
                 if square_signature(O, u, rps) not in (triv_sig, neg_sig)]
        if nonsq:
            break
    if not nonsq:
        return None, None, ('no non-square unit in the box (%d units seen)'
                            % len(units))
    u = nonsq[0]
    cands = []
    for base, name in ((alpha, 'alpha'), (O.mul(u, alpha), 'u alpha'),
                       (u, 'u')):
        pos = base if real_positive(O, base) else tuple(-x for x in base)
        cands.append((name, pos))
    passing = [(name, v) for (name, v) in cands if is_square_mod4(O, v)]
    if len(passing) != 1:
        return None, None, ('SELMER: %d of 3 real-positive candidates are'
                            ' squares mod 4 (%s)'
                            % (len(passing), [n for n, v in passing]))
    name, x = passing[0]
    s1, s2, s3 = char_poly(O, x)
    q = isqrt(s3)
    assert q * q == s3, "the Kummer generator's norm is not a square"
    g = [1, 0, -2 * s1, 8 * q, s1 * s1 - 4 * s2]
    return g, x, dict(p=p, m=m, kind=name, s=(s1, s2, s3))


# ------------------------------------------------------ polynomials mod p
def pmod(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    return pmod(out, p)


def prem(a, g, p):
    """a mod g, g monic, coefficient lists low to high."""
    a = list(a)
    dg = len(g) - 1
    while len(a) - 1 >= dg and any(a):
        if a[-1] == 0:
            a.pop()
            continue
        cf = a[-1]
        shift = len(a) - 1 - dg
        for i in range(dg + 1):
            a[shift + i] = (a[shift + i] - cf * g[i]) % p
        a.pop()
    return pmod(a, p)


def pgcd(a, b, p):
    a, b = pmod(a, p), pmod(b, p)
    while any(b):
        inv = pow(b[-1], -1, p)
        bm = [(x * inv) % p for x in b]
        a, b = b, prem(a, bm, p)
    return a


def pcompose(h, f, g, p):
    """h(f) mod g by Horner."""
    out = [0]
    for cf in reversed(h):
        out = prem(pmul(out, f, p), g, p)
        out[0] = (out[0] + cf) % p
        out = pmod(out, p)
    return out


def minus_x(a, p):
    """a(X) - X."""
    a = list(a) + [0] * max(0, 2 - len(a))
    a[1] = (a[1] - 1) % p
    return pmod(a, p)


def xpow_mod(e, g, p):
    """X^e mod g."""
    result = [1]
    base = [0, 1]
    while e:
        if e & 1:
            result = prem(pmul(result, base, p), g, p)
        e >>= 1
        if e:
            base = prem(pmul(base, base, p), g, p)
    return result


def cycle_type(gcoef, p):
    """The factorisation pattern of a squarefree quartic mod p."""
    g = pmod(list(reversed(gcoef)), p)          # low to high, monic
    assert len(g) == 5
    xp = xpow_mod(p, g, p)
    n1 = len(pgcd(g, minus_x(xp, p), p)) - 1
    xpp = pcompose(xp, xp, g, p)
    n2 = len(pgcd(g, minus_x(xpp, p), p)) - 1
    if n1 == 4:
        return '1111'
    if n1 == 2:
        return '112'
    if n1 == 1:
        return '13'
    if n1 == 0 and n2 == 4:
        return '22'
    if n1 == 0 and n2 == 0:
        return '4'
    raise AssertionError("pattern (%d, %d) at p = %d" % (n1, n2, p))


def poly_disc(g):
    from sympy import Poly, discriminant, symbols
    X = symbols('X')
    return int(discriminant(Poly(g, X)))


def is_irreducible(g):
    from sympy import Poly, symbols, factor_list
    X = symbols('X')
    fl = factor_list(Poly(g, X).as_expr())[1]
    return len(fl) == 1 and fl[0][1] == 1


def pairing_check(g, s):
    """C2's numeric half: the quartic's roots summed in pairs and
    squared give alpha's conjugates."""
    from sympy import Poly, symbols
    X = symbols('X')
    rts = [complex(z) for z in Poly(g, X).nroots(n=30)]
    rts = [z / 2 for z in rts]                   # theta = X / 2
    pairs = [(rts[0] + rts[1]) ** 2, (rts[0] + rts[2]) ** 2,
             (rts[0] + rts[3]) ** 2]
    s1, s2, s3 = s
    e1 = sum(pairs)
    e2 = pairs[0] * pairs[1] + pairs[0] * pairs[2] + pairs[1] * pairs[2]
    e3 = pairs[0] * pairs[1] * pairs[2]
    scale = 1.0 + abs(s1) + abs(s2) + abs(s3)
    return max(abs(e1 - s1), abs(e2 - s2), abs(e3 - s3)) / scale


# ------------------------------------------------------- the statistics
def field_rows(recs, rng=None, plant=None):
    """Per field: the non-square indicator minus 1/2 by rank, with the
    prime at each rank, and the generator indicator minus phi(h)/h.
    rng re-sorts classes uniformly; plant = ('rank', q) | ('norm', q)
    overrides the indicator after the re-sort."""
    rows = []
    for rec in recs:
        G = rec['G']
        gens = [k for k in G.keys if G.order[k] == G.h]
        gshare = len(gens) / float(G.h)
        places = sorted(rec['places'])
        if rng is not None:
            places = [(p, rng.choice(G.keys)) for (p, key) in places]
        ns, gen, ps = [], [], []
        for i, (p, key) in enumerate(places[:RANKS]):
            odd = key not in G.squares
            if plant is not None:
                kind, q = plant
                if kind == 'rank' and i == 0:
                    odd = rng.random() < q
                elif kind == 'norm':
                    odd = rng.random() < 0.5 + q / p
            ns.append((1.0 if odd else 0.0) - 0.5)
            gen.append((1.0 if key in gens else 0.0) - gshare)
            ps.append(p)
        rows.append(dict(h=G.h, d=rec['d'], ns=ns, gen=gen, ps=ps,
                         cyclic=rec['cyclic'], types=rec['types']))
    return rows


def rank_table(rows, tag, which='ns'):
    print("  %s: %s by rank (%d fields)"
          % (tag, "non-square share minus 1/2" if which == 'ns'
             else "generator share minus phi(h)/h", len(rows)))
    out = {}
    for r in range(1, RANKS + 1):
        vals = [row[which][r - 1] for row in rows if len(row[which]) >= r]
        if len(vals) < 2:
            continue
        mu, se = mean_se(vals)
        out[r] = (mu, se)
        if r <= 6 or r == RANKS:
            print("    rank %2d  %s  z %+.1f  (%d)"
                  % (r, fmt(mu, se), mu / se if se else 0.0, len(vals)))
    for (a, b) in RANK_POOLS:
        vals = []
        for row in rows:
            v = row[which][a - 1:b]
            if len(v) == b - a + 1:
                vals.append(sum(v) / len(v))
        if len(vals) >= 2:
            mu, se = mean_se(vals)
            out[(a, b)] = (mu, se)
            print("    ranks %2d-%2d pooled  %s  z %+.1f  (%d)"
                  % (a, b, fmt(mu, se), mu / se if se else 0.0,
                     len(vals)))
    return out


def cell_se(vals):
    """Mean and the null-variance bar sqrt(1/4N): never zero."""
    n = len(vals)
    return sum(vals) / n, (0.25 / n) ** 0.5


def cells_of(rows):
    """(p, rank) -> list of non-square indicators (0/1)."""
    cells = defaultdict(list)
    for row in rows:
        for i, p in enumerate(row['ps']):
            r = min(i + 1, TABLE_RANKS[-1])
            if p in TABLE_PRIMES:
                cells[(p, r)].append(row['ns'][i] + 0.5)
            else:
                for (lo, hi) in TABLE_BANDS:
                    if lo <= p < hi:
                        cells[((lo, hi), r)].append(row['ns'][i] + 0.5)
    return cells


def table_read(rows, tag, verbose=True):
    """D (rank-1 minus rank>=2 share at fixed p, pooled) and S (slope of
    the rank-1 share on p), each with its standard error."""
    cells = cells_of(rows)
    if verbose:
        print("  %s: non-square share by (p, rank); '--' under %d fields;"
              " the prime bands beyond 23 are descriptive, outside D and S"
              % (tag, MIN_CELL))
        print("    %6s " % "p" + "".join("%18s" % ("rank %d" % r if r < 4
                                                    else "rank >= 4")
                                          for r in TABLE_RANKS))
    stats = {}
    for p in TABLE_PRIMES + TABLE_BANDS:
        line = "    %6s " % (p if isinstance(p, int) else "%d-%d" % p)
        for r in TABLE_RANKS:
            vals = cells.get((p, r), [])
            if len(vals) >= MIN_CELL:
                mu, se = cell_se(vals)
                stats[(p, r)] = (mu, se, len(vals))
                line += "  %.3f+-%.3f(%3d)" % (mu, se, len(vals))
            else:
                line += "  %16s" % ("--(%d)" % len(vals))
        if verbose:
            print(line)
    # D: rank 1 against rank >= 2 at fixed p, inverse-variance pooled
    num = den = 0.0
    used = []
    for p in TABLE_PRIMES:
        if (p, 1) not in stats:
            continue
        hi = [v for r in TABLE_RANKS[1:] for v in cells.get((p, r), [])]
        if len(hi) < MIN_CELL:
            continue
        mu1, se1, n1 = stats[(p, 1)]
        mu2, se2 = cell_se(hi)
        var = se1 ** 2 + se2 ** 2
        if var <= 0:
            continue
        num += (mu1 - mu2) / var
        den += 1.0 / var
        used.append(p)
    D = (num / den, (1.0 / den) ** 0.5) if den else (None, None)
    # S: weighted slope of the rank-1 share on p
    pts = [(p, stats[(p, 1)][0], 1.0 / stats[(p, 1)][1] ** 2)
           for p in TABLE_PRIMES if (p, 1) in stats]
    if len(pts) >= 3:
        W = sum(w for _, _, w in pts)
        mx = sum(w * x for x, _, w in pts) / W
        my = sum(w * y for _, y, w in pts) / W
        sxx = sum(w * (x - mx) ** 2 for x, _, w in pts)
        b = sum(w * (x - mx) * (y - my) for x, y, w in pts) / sxx
        S = (b, (1.0 / sxx) ** 0.5)
    else:
        S = (None, None)
    if verbose:
        print("    D (rank 1 minus rank >= 2 at fixed p, pooled over p in"
              " %s): %s  z %s" % (used, fmt(*D),
                                 "%+.1f" % (D[0] / D[1]) if D[0] is not None
                                 else "--"))
        print("    S (slope of the rank-1 share on p, %d cells): %s per"
              " unit of p  z %s" % (len(pts), fmt(*S),
                                    "%+.1f" % (S[0] / S[1])
                                    if S[0] is not None else "--"))
    return D, S, stats


def seat_verdict(D, S):
    if D[0] is None or S[0] is None:
        return 'UNREADABLE'
    zD, zS = D[0] / D[1], S[0] / S[1]
    if abs(zD) < 2.0 and zS <= -2.0:
        return 'NORM-SEATED'
    if D[0] >= 0.10 and zD >= 2.0 and abs(zS) < 2.0:
        return 'RANK-SEATED'
    return 'MIXED'


def split_below_table(rows):
    """At rank 1 and fixed p: the non-square share split by whether a
    totally split prime sits below p."""
    print("  rank 1 at fixed p, split by a totally split prime below p"
          " (none | at least one)")
    for p in TABLE_PRIMES:
        a, b = [], []
        for row in rows:
            if not row['ps'] or row['ps'][0] != p:
                continue
            has = any(q < p and t != 'dropped' and t[0] == 'split'
                      for q, t in row['types'].items())
            (b if has else a).append(row['ns'][0] + 0.5)
        cells = []
        for vals in (a, b):
            if len(vals) >= MIN_CELL:
                mu, se = cell_se(vals)
                cells.append("%.3f+-%.3f(%3d)" % (mu, se, len(vals)))
            else:
                cells.append("%16s" % ("--(%d)" % len(vals)))
        print("    p = %2d   %s | %s" % (p, cells[0], cells[1]))


def certify(recs, label="P1 PASSES", floor_fatal=True, **boxes):
    """C2, C3, C4 on any record list: the quartic built from the order,
    read against the records at every prime to READ_CAP; the checks
    stop the run on a disagreement, and on the 80% coverage floor unless
    floor_fatal is off, when the floor prints its verdict and the run
    goes on. Returns the count built."""
    t1 = time.time()
    built = 0
    reasons = defaultdict(list)
    agree = defaultdict(int)
    disagree = []
    skipped_index = 0
    n_pair = 0
    kinds = defaultdict(int)
    worst_pair = 0.0
    plist = primes_upto(READ_CAP)
    for i, rec in enumerate(recs):
        rows = ECP.t2_rows(rec['O'], rec['a'], rec['b'], rec['c'])
        g, x, info = build_quartic(rec, rows, **boxes)
        if g is None:
            reasons[info.split('(')[0].strip()].append(rec['d'])
            continue
        ok(is_irreducible(g), "C2: g reducible at d = %d: %s"
           % (rec['d'], g))
        dg = poly_disc(g)
        ok(dg % rec['d'] == 0 and isqrt(dg // rec['d']) ** 2 == dg // rec['d'],
           "C2: disc(g) = %d is not d_K = %d times a square"
           % (dg, rec['d']))
        index = isqrt(dg // rec['d'])
        if n_pair < 3:
            err = pairing_check(g, info['s'])
            worst_pair = max(worst_pair, err)
            n_pair += 1
        built += 1
        kinds[info['kind']] += 1
        for p in plist:
            if p == 2 or dg % p == 0:
                if p != 2 and rec['d'] % p and index % p == 0:
                    skipped_index += 1
                continue
            want = s4_class(rec, p)
            if want is None:
                continue
            got = cycle_type(g, p)
            if got == want:
                agree[want] += 1
            else:
                disagree.append((rec['d'], p, want, got))
        if (i + 1) % 100 == 0:
            print("  ... %d fields, %d built, %.1f s"
                  % (i + 1, built, time.time() - t1))
    print("  %d of %d fields built (%.1f s); Kummer generator: %s"
          % (built, len(recs), time.time() - t1, dict(kinds)))
    for reason, ds in sorted(reasons.items()):
        print("    not built, %s: %d fields %s"
              % (reason, len(ds), ds if len(ds) <= 12 else ds[:12] + ['...']))
    ok(not any(r.startswith('SELMER: 2') for r in reasons),
       "C3: a field with two unramified quadratic extensions")
    ok(worst_pair < 1e-6, "C2: pairing identity off by %.2e" % worst_pair)
    print("  C2 PASSES: every built g irreducible with disc(g) = d_K x"
          " square; pairing identity on %d fields to %.1e"
          % (n_pair, worst_pair))
    print("  C3: exactly one real-positive Selmer candidate is a square"
          " mod 4 in every built field")
    print("  C4: agreements by S4 class %s; %d disagreements; %d index"
          " primes skipped" % (dict(agree), len(disagree), skipped_index))
    for (d, p, want, got) in disagree[:20]:
        print("    d = %d  p = %d  records say %s, F says %s"
              % (d, p, want, got))
    ok(not disagree, "P1/C4: the dictionary disagrees with F")
    if floor_fatal or built >= 0.8 * len(recs):
        ok(built >= 0.8 * len(recs), "fewer than 80%% of fields built")
    else:
        print("  COVERAGE SHORT: %d of %d built (%.0f%%), under the 80%%"
              " floor; the certificate is read on the fields built"
              % (built, len(recs), 100.0 * built / len(recs)))
    print("  %s: the dictionary holds at every readable prime of"
          " every built field" % label)
    gc.collect()
    return built


# ------------------------------------------------------------------ main
def main():
    t0 = time.time()
    rng = random.Random(SEED)

    section("THE POPULATION (the wide box, 2-rank 1, the sibling's floor)")
    recs = records()
    by_h = defaultdict(int)
    for rec in recs:
        by_h[rec['h']] += 1
    print("  by class number: %s" % dict(sorted(by_h.items())))
    print("  non-cyclic among them: %d"
          % sum(1 for rec in recs if not rec['cyclic']))
    print("  %.1f s" % (time.time() - t0))

    section("C1  THE TRIPLE PARITY")
    n_split = bad = 0
    for rec in recs:
        for p in rec['types']:
            cls = s4_class(rec, p)
            if cls in ('1111', '22'):
                n_split += 1
            elif cls == 'BAD':
                bad += 1
    ok(bad == 0, "C1: %d split triples with 0 or 2 classes in 2Cl" % bad)
    print("  C1 PASSES: %d split primes, every triple with 1 or 3 classes"
          " in 2Cl" % n_split)

    section("C2, C3, C4  THE QUARTIC BUILT FROM THE ORDER, READ AGAINST"
            " THE RECORDS")
    certify(recs)

    section("C5  THE REPRINT (the sibling's generator cell)")
    rows = field_rows(recs)
    sib = [r for r in rows if r['h'] in (4, 6, 8)]
    h4 = [r for r in rows if r['h'] == 4]
    vals = [sum(r['gen'][:3]) / 3 for r in h4 if len(r['gen']) >= 3]
    mu, se = mean_se(vals)
    print("  h = 4, ranks 1-3 pooled generator excess %s (%d fields)"
          % (fmt(mu, se), len(vals)))
    ok(QUICK or abs(mu - REPRINT_H4[0]) < REPRINT_H4[1],
       "C5: h = 4 ranks 1-3 reads %.3f" % mu)
    vals = [r['gen'][0] for r in sib if r['gen']]
    mu, se = mean_se(vals)
    print("  h = 4, 6, 8 rank-1 generator excess %s (%d fields)"
          % (fmt(mu, se), len(vals)))
    ok(QUICK or abs(mu - REPRINT_GEN[0]) < REPRINT_GEN[1],
       "C5: rank-1 generator excess reads %.3f" % mu)
    print("  C5 %s" % ("not read in the rehearsal" if QUICK else "PASSES"))

    section("C6, C7  THE NULL AND THE TWO PLANTED SEATS")
    null = field_rows(recs, rng=rng)
    D0, S0, _ = table_read(null, "null")
    ok(abs(D0[0] / D0[1]) < 3.0 and abs(S0[0] / S0[1]) < 3.0,
       "C6: the null's D or S is off zero")
    print("  C6 PASSES: null D and S within 3 sigma of zero")
    pr = field_rows(recs, rng=random.Random(SEED + 1),
                    plant=('rank', PLANT_RANK))
    Dr, Sr, _ = table_read(pr, "rank-planted")
    pn = field_rows(recs, rng=random.Random(SEED + 2),
                    plant=('norm', PLANT_NORM))
    Dn, Sn, _ = table_read(pn, "norm-planted")
    ok(QUICK or (Dr[0] / Dr[1] >= 3.0 and abs(Sr[0] / Sr[1]) < 2.0),
       "C7: the rank plant does not read as rank-seated")
    ok(QUICK or (Sn[0] / Sn[1] <= -3.0 and abs(Dn[0] / Dn[1]) < 2.0),
       "C7: the norm plant does not read as norm-seated")
    print("  C7 PASSES: the rank plant reads %s, the norm plant %s"
          % (seat_verdict(Dr, Sr), seat_verdict(Dn, Sn)))
    del null, pr, pn

    section("P2  THE NON-SQUARE SEAT BY STRATUM AND POOLED")
    per_h = {}
    for h in sorted(by_h):
        sub = [r for r in rows if r['h'] == h]
        if len(sub) < 10:
            print("  h = %d: %d fields, not read" % (h, len(sub)))
            continue
        per_h[h] = rank_table(sub, "h = %d" % h)
    pooled = rank_table(rows, "pooled over every stratum")
    mu, se = pooled[1]
    p2a = mu >= 0.20 and mu / se >= 3.0
    m2, s2 = per_h[2][1]
    m4, s4 = per_h[4][1]
    gap = (m2 - m4) / sqrt(s2 * s2 + s4 * s4)
    print("  pooled rank-1 excess %s against 0.20 at 3 sigma: %s"
          % (fmt(mu, se), p2a))
    print("  h = 2 rank 1 %s against h = 4 rank 1 %s: %.1f sigma apart"
          % (fmt(m2, s2), fmt(m4, s4), gap))
    print("  P2 PASSES iff both: %s" % (p2a and abs(gap) < 2.0))
    sub6 = [r for r in rows if r['h'] == 6]
    rank_table(sub6, "h = 6, the generator cell {1, 5} for comparison",
               which='gen')

    section("P3  RANK AGAINST NORM: THE (p, rank) TABLE")
    D, S, stats = table_read(rows, "measured")
    verdict = seat_verdict(D, S)
    print("  frozen: norm-seated iff |z_D| < 2 and z_S <= -2; rank-seated"
          " iff D >= 0.10 at 2 sigma and |z_S| < 2")
    print("  P3 (this file's guess: NORM-SEATED) reads: %s" % verdict)
    split_below_table(rows)
    for h in (2, 4):
        sub = [r for r in rows if r['h'] == h]
        print("  stratum h = %d alone:" % h)
        table_read(sub, "h = %d" % h)

    section("THE |d| READ (descriptive, added after the slate)")
    print("  rank-1 non-square share on log|d|, and by |d| band")
    for label, sub in (("pooled", rows), ("h = 2", [r for r in rows
                                                   if r['h'] == 2]),
                       ("h = 4", [r for r in rows if r['h'] == 4])):
        pts = [(log(abs(r['d'])), r['ns'][0] + 0.5) for r in sub if r['ns']]
        b, se, a = EC.slope_fit(pts)
        bands = []
        for (lo, hi) in ((0, 6000), (6000, 12000), (12000, 24000)):
            vals = [r['ns'][0] + 0.5 for r in sub
                    if r['ns'] and lo <= abs(r['d']) < hi]
            if len(vals) >= MIN_CELL:
                mu, se2 = cell_se(vals)
                bands.append("%.3f+-%.3f(%d)" % (mu, se2, len(vals)))
            else:
                bands.append("--(%d)" % len(vals))
        print("    %-7s slope %+.3f +- %.3f per unit of log|d| (%d fields);"
              " bands %s" % (label, b, se, len(pts), "  ".join(bands)))

    print("\n%d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
