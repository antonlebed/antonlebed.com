"""
explore_three_seats.py -- three conjectures, each decided by the cheapest
print that can end it: whether one number about the rest of a cell
re-keys the abandoned atom's dead predicate class, whether the landing
word's discrepancy exponent is a function of the supply's exponent, and
whether the least split place of a quadratic field is a non-square more
often than a coin says.

THE THREE QUESTIONS.

  Q1. THE UNDER-KEYED AUDIT. On the set-valued ruler (the exact-truth
      instrument for prediction sets) an atom's fate under the min-cost
      covering optimum is no function of its own numbers: keyed by (own
      mass, own sorted posterior row, the operative level), 67 of 444
      keys carry a forced-abandoned atom in one cell and a forced-served
      atom in another (explore_ruler_dual.py D3), so every per-subgroup
      predicate of that form is dead. The conjecture: what decides an
      atom is what the REST of the cell leaves owed, and the one number
      that summarizes it is the certificate's ROOM, D/t* -- the
      threshold certificate's overshoot over the target divided by the
      level (explore_ruler_surplus.py's identity cert - L = D/t*). The
      question: does adding the room to the key remove every collision?

  Q2. THE ORBIT SIEVE. On a fractional-power supply m(g) = ceil g^(1/c),
      1 < c < 2, the growing-window rider lands at passes t_n whose
      normalized offset in its gap window is the Weyl word
      1 - frac((t_n + 2)^(1/c)) along the orbit t -> t + ceil(t^(1/c))
      (explore_three_prints.py F1). Its star discrepancy over the decade
      10^5..10^6 landings fell as N^-0.58 at c = 3/2 and N^-0.37 at
      c = 7/4. The conjecture reads the exponent as a function of c
      alone, so that the coverage theorem the open super-critical cell
      needs is an exponential-sum bound along a polynomial-growth orbit.
      The question: what do c = 4/3 and c = 5/3 print?

  Q3. THE RANK-SEATED BIAS. Over cubic fields of 2-rank 1 the least
      partial place is a non-square (outside 2Cl) about 85 times in 100
      at rank 1, decaying to 0.62 from rank 4, a function of the place's
      RANK in its field's norm order and not of the prime
      (explore_quartic_seat.py). The conjecture: a bias law indexed by
      order statistics, beside Chebyshev's, general to class groups. The
      question: does the least odd split prime of a QUADRATIC field with
      a cyclic even class group land in a non-square class at a share
      above the coin, and above the share that generation alone forces?

WHOSE VOCABULARY. Q1 is written in the knapsack's terms (cost, level,
overshoot, forced fate) as explore_ruler_dual.py has them; Q2 in the
supply rig's (landing, gap window, offset, star discrepancy); Q3 in the
class-group census's (the narrow class of a split prime's form, the
order of its class, a square being a class whose order divides h/2 in a
cyclic group of even order h).

TRANSPLANTS, MARKED.
  Q1 imports from the LP dual the belief that a scalar summary of the
     cell's slack can order the corrections; the parent measured the
     reduced cost failing to beat the atom's weight, so the belief is
     already weak on this sweep.
  Q2 imports from c = 3/2 and 7/4 an exponent law across c; two points
     fit any law, which is why the cheapest print is two more points.
  Q3 imports the cubic seat to degree 2 across the one thing that
     differs -- the cubic count is CLOSED at the field's least places
     while a quadratic field's residual runs outward
     (explore_principal_share.py) --
     and across the S4 dictionary that has no degree-2 analogue.

THE HAND ATTACK, before any engine code.

  Q1. Any per-CELL scalar added to a per-atom key separates atoms of
      different cells, so a room that removed every collision by making
      every key a cell identifier would prove nothing. The honest read
      therefore carries the key's REUSE beside its collision count: the
      share of room-keyed keys whose forced atoms come from two or more
      distinct cells, against the same share for the parent key. A kill
      needs zero collisions AT a reuse that is not near zero. Second,
      the room is exact in Fraction and the level is one of the cell's
      own posterior values, so the key is exact and two keys are equal
      or not with no tolerance. Third, the equal-weight arms are the
      positive control: the condition is PROVED there, so both keys
      must print zero collisions, and the parent key on the unequal
      arms must reprint 67 of 444 before the room key is read.

  Q2. The kill as first written -- 5/3 outside [-0.58, -0.37], or 4/3
      below 3/2's -- cannot tell settling from flat: the two random
      seeds printed -0.53 and -0.52 inside that band, so a word that is
      random-rate at EVERY c would pass it. It is refrozen here on the
      shape the conjecture needs: an exponent that is a function of c
      alone and passes through -0.58 at 3/2 and -0.37 at 7/4 is
      monotone across 4/3 < 3/2 < 5/3 < 7/4. The exponent over one
      decade is itself noisy at about 0.1 (the two random seeds are
      one calibration; a third is added), so a monotone read needs the
      spread across c to exceed that noise. The landings are computed
      exactly in integers; the offset word is exact rationals read into
      floats; the closed-form check in floats is kept to the first
      20,000 landings where t + 2 is exact in a double.

  Q3. Generation is the confound the cubic reading priced at a third of
      the level shift and could bound only from above. Here it can be
      computed EXACTLY per field. The class group is generated by the
      prime ideals of norm below Minkowski's bound B (sqrt(D)/2 real,
      2 sqrt(|D|)/pi imaginary), so at least one class below B is a
      non-square. The classes of the ramified primes below B are fixed
      numbers of the field, read off their forms; under the coin-flip
      null each split prime below B is a non-square with probability
      1/2 independently. If a ramified prime below B is already a
      non-square the constraint is vacuous and the null at rank 1 is
      1/2; else with m unknown split primes below B (2 included when it
      splits) the null at rank 1 is (1/2)/(1 - 2^-m) when the least odd
      split prime is one of the m, and 1/2 when it sits above B. The
      per-field null is averaged over the population and the share is
      read against it. The population is fields with a CYCLIC class
      group of even order (2-rank 1, the cubic cell), the real fields
      restricted to N(eps) = -1 where the narrow and wide groups agree,
      so one census serves both views and no coset is rebuilt. The
      sweep skips p = 2, so RANK is the rank among ODD split primes, as
      the cubic fiber was built on odd primes. The share's own noise at
      a few hundred fields is 0.02-0.03; a 0.10 excess is read at 3
      sigma or more or not at all.

PREDICTIONS, frozen before the run.
  P1. The room key leaves collisions: at least 10 of the 67 parent
      collisions survive it, and the room key's reuse share is above
      0.3 (the room is a coarse rational on a small grid).
  P2. The four exponents are not monotone in c: 4/3 and 5/3 both print
      within 0.12 of -0.5, where the random seeds print, and the spread
      of the four is carried by 7/4 alone.
  P3. The real arm's rank-1 non-square share is above 1/2 by 0.05 to
      0.15 and MOST of it is the generation null; the excess over the
      conditioned null is under 0.05 in both arms.

KILL CRITERIA, as observables.
  Q1 KILLED (the class was under-keyed) iff the room key prints ZERO
     collisions on the unequal arms AND its reuse share is at least 0.1;
     SURVIVES iff it prints 5 or more collisions. Between, refrozen on
     the print.
  Q2 KILLED (no one-parameter law) iff the four exponents, in c order,
     are not monotone, or their total spread is under 0.15; SURVIVES
     iff monotone with spread at least 0.25.
  Q3 KILLED as generation bookkeeping iff in BOTH arms the rank-1 share
     minus the conditioned null is under two of its standard errors;
     KILLED as an S4 accident iff in both arms the raw share is within
     two standard errors of 1/2; SURVIVES iff in both arms the excess
     over the conditioned null is at least 0.10 at two standard errors.
     Otherwise refrozen on the print.

CONTROLS, run before any verdict is read.
  C1 (Q1) Equal-weight arms: zero collisions under both keys.
  C2 (Q1) Parent key on the unequal arms: 444 distinct keys, 67
     colliding, as explore_ruler_dual.py printed.
  C3 (Q2) c = 3/2 and 7/4 reprint -0.58 and -0.37 within 0.02.
  C4 (Q2) The closed form holds: mean deviation under 0.001 over
     landings 100..20000 at every c.
  C5 (Q3) Every field's class count equals its class number, cyclicity
     is certified by an element of order h, and the generation
     constraint is SATISFIED by the actual classes (some prime ideal of
     norm below B is a non-square) at every field read; a field where
     it is not is a bug in the bound or the classes and is fatal.
  C6 (Q3) The pooled non-square share over ALL odd split primes below
     10^4 is 1/2 within two standard errors in both arms (Chebotarev).

THE SECOND RUN'S ADDENDUM, frozen after the first run's prints and
before the second. The first run decided Q1 (SURVIVES, 138 room-keyed
collisions at reuse 0.998) and Q2 (KILLED, exponents -0.41, -0.58,
-0.64, -0.37 in c order, not monotone). Q3 printed two failed controls
and could not be read; what failed and what is added:
  C5 failed at 2 real and 21 imaginary fields because the generation
     check skipped the prime 2: a ramified 2 was never read and a split
     2 is absent from the sweep's hit list. Fixed: the class of the
     prime above 2 is read exactly off its form whenever 2 is not
     inert, for the actual check; the null keeps a split 2 as a coin.
  C6 failed in both arms, the pool over every odd split prime below
     10^4 printing 0.511 at a standard error of 0.001. That excess is
     the classical one -- the square classes are short at small primes
     by the explicit formula's prime-power term, the principal share's
     shortfall explore_principal_share.py records -- and C6 was frozen where that
     term still lives. C6 stands as written and FAILED; C6b is added,
     the same pool over 1000 <= p < 10^4 where the term has decayed,
     read at three standard errors.
  Q3b. The table the first run printed carries the contrast the cubic
     rig read and this file's kill never asked: at a FIXED prime the
     rank-1 and rank->=2 shares, and at a fixed rank the share against
     the prime. Added, per arm: the pooled rank-1 minus rank->=2
     difference D at fixed p over every p with at least 15 fields in
     both cells (inverse-variance weights), and the rank->=2 share at
     p <= 7 against 11 <= p <= 23. Prediction P3b: D under 0.05 in
     both arms, the near-band share above the far-band by 0.05 or more
     in both. REFROZEN KILL: Q3 KILLED as norm-seated iff D is under
     0.05 at two standard errors in both arms AND the near-band share
     exceeds the far-band by 0.05 at two standard errors in both arms
     -- the degree-2 excess then being the prime-power term with the
     rank a shadow of the norm, the one thing the cubic seat is not.
     SURVIVES iff D is 0.10 or more at two standard errors in both.

FINDINGS (the second run's prints, which include the first's).

  F1. THE ROOM DOES NOT RE-KEY THE CLASS. Both equal-weight arms print
      zero collisions under both keys (26 and 58 keys). On the unequal
      arms the parent key reprints 444 distinct keys and 67 colliding,
      every one reused across cells. The room key splits them into 5,158
      keys, 5,147 of them (0.998) reused across cells, and 138 of them
      collide: the room separates 20 of the 67 parent collisions cleanly
      and the other 47 not at all. The room takes 103 distinct values
      from 0 to 53/60 across the forced atoms. Witness: mass 1/20, row
      (3/5, 1/5, 1/5), level 3/10, room 7/30 -- abandoned in every
      optimum at 6 cells and served in every optimum at 48. P1 held.
      Q1 SURVIVES: fate is not a function of the atom's numbers plus
      the certificate's room; the two-number reading is dead with the
      one-number one.

  F2. THE EXPONENT IS NOT A FUNCTION OF c. The closed form holds at all
      four supplies (mean deviation 0.00044, 0.00025, 0.00020, 0.00017
      at c = 4/3, 3/2, 5/3, 7/4). The star discrepancy's slope over
      10^5..10^6 landings prints -0.41, -0.58, -0.64, -0.37 in c order
      (3/2 and 7/4 reprinted to 0.00); the three random seeds print
      -0.53, -0.52, -0.58. Not monotone, spread 0.27, and the 4/3 and
      5/3 values straddle the random band on opposite sides from their
      neighbours. P2 half held (not monotone; the spread is not 7/4's
      alone). Q2 KILLED: no one-parameter law in c, so the exponent is
      not the object a coverage theorem over the orbit would bound, and
      the open cell owes its theorem to something other than the
      offset word's discrepancy.

  F3. THE DEGREE-2 SEAT IS REAL, IS NOT GENERATION, AND ITS AXIS IS
      UNDECIDED AT THIS POPULATION. Real fields with N(eps) = -1 and a
      cyclic even class group, D <= 16000: 485; imaginary, |D| <= 8000:
      1,096. C5 passes at every field once the prime 2 is read. The
      least odd split prime is a non-square 0.771 +- 0.019 of the time
      (374 of 485) and 0.685 +- 0.014 (751 of 1,096); the shares fall
      over rank, 0.680, 0.598, 0.608, 0.534 and 0.614, 0.619, 0.540,
      0.589 at ranks 2 to 5, and sit near 0.55-0.60 to rank 8. The
      exact Minkowski-conditioned null at rank 1 averages 0.508 and
      0.517 -- the bound admits so many split primes that generation
      forces almost nothing, and 316 of 485 and 521 of 1,096 fields
      carry a ramified non-square below it -- so the excess over the
      conditioned null is +0.263 (se 0.019) and +0.168 (se 0.014).
      P3 failed: generation is not most of it, nor any of it. Q3b: at
      fixed p the rank-1 minus rank->=2 difference pools to +0.027
      (se 0.036) real and +0.045 (se 0.025) imaginary; the rank->=2
      share drops from p <= 7 to 11 <= p <= 23 by +0.068 (se 0.035)
      and +0.016 (se 0.024). Neither the norm-seated kill (D under 0.05
      at two se in both arms AND a drop of 0.05 at two se in both) nor
      the survival bar (D of 0.10 at two se in both) is met. Q3 BETWEEN.
      What the table shows without deciding: the share at p = 3 is 0.80
      and 0.71 whatever the rank (3 is always rank 1), at p = 5 it is
      0.82 against 0.78 and 0.74 against 0.59 by rank, and the
      rank->=2 column falls from 0.78 to 0.55 across p = 5..23 in the
      real arm -- a norm-shaped profile the imaginary arm does not
      reproduce (0.59..0.66, flat). REFROZEN KILL on the print: the same
      two numbers over the imaginary fields to |D| <= 32000, where D's
      standard error reaches 0.012 and the 0.05 line is resolved; D
      under 0.05 at two se there kills it as norm-seated, D at 0.10 or
      more carries it.

  CONTROLS. 499 run, 4 failed: C6 and C6b in both arms, as the addendum
  anticipated for C6 and did not for C6b. The pool over every odd split
  prime below 10^4 is 0.5109 +- 0.0009 (293,835 places) and 0.5107 +-
  0.0006 (668,433); over 1000 <= p < 10^4 it is 0.5064 +- 0.0010 and
  0.5067 +- 0.0007. Both are the square classes short by the explicit
  formula's prime-power term -- the prime squares q^2 in a band land in
  square classes, and their count against the band's primes per class
  is of the order of the printed excess (fourteen prime squares between
  1000 and 10^4 against some five hundred split primes per field) --
  and both thresholds were frozen below the term's size. The Q3 reading
  does not rest on either: the rank-1 excess is thirty times the pool's.
  Every other control passed: C1, C2 (444 / 67), C3 (-0.58, -0.37),
  C4 (under 0.001 at every c), C5 (0 fails).

RUN RECORD. Two runs. The first ran the landing walk on the parent's
float-seeded integer root and did not finish in ten minutes at
c = 4/3, where the passes reach 10^24 and a double's root is 10^8 units
off, each corrected one step at a time; the exact Newton root above
replaced it and the walk to 10^6 landings takes 5 to 9 s per c. Second
run: wall 56.8 s, peak working set 282.6 MB (the imaginary census's
class tables) against the 512 MB default, under memwatch.

RESOURCE NOTE. Q1 is the dual rig's sweep once more (16 s, 15 MB) with
one certificate per cell added. Q2 is four exact landing walks to 10^6
plus three random words of 10^6; the landings are streamed and only the
float word kept, about 24 MB per word, one at a time. Q3 is the class
census over real D <= 16000 and imaginary |D| <= 8000 (the real half
ran in 17 s in explore_ceiling_realquad.py). Estimate three minutes,
under 100 MB.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import math                                          # noqa: E402
import random                                        # noqa: E402
import sys                                           # noqa: E402
import time                                          # noqa: E402
from collections import defaultdict                  # noqa: E402
from fractions import Fraction                       # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_abandon import (                  # noqa: E402
    ALPHA, MENU_A, MENU_B, ROWS, WEIGHTS, EQUAL, make_cell, check_truth,
    all_optima,
)
from explore_ruler_barecell import (                 # noqa: E402
    operative_level, certified_optimum,
)
from explore_three_prints import star_discrepancy   # noqa: E402
import explore_class_order as CO                     # noqa: E402
from explore_class_share import classes_real         # noqa: E402
from explore_principal_share import (                # noqa: E402
    primes_upto, kronecker, reduce_form, reduce_definite, class_data_real,
)

F = Fraction
CHECKS = [0, 0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        CHECKS[1] += 1
        print("  CONTROL FAILED: %s" % msg)
    return cond


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


# =============================================================== Q1

def room_of(cell, level):
    """The certificate's overshoot over the target, divided by the level."""
    _lo, _up, _ex, cov = certified_optimum(cell, ALPHA, level)
    return (cov - (1 - ALPHA)) / level


def key_parent(cell, r, level, room):
    return (cell.atom_prob(r),
            tuple(sorted(cell.posterior(r), reverse=True)), level)


def key_room(cell, r, level, room):
    return key_parent(cell, r, level, room) + (room,)


def sweep_keys(menu, tag, rows_list, weights, keyfns, indexes):
    cells = 0
    for rows in rows_list:
        for wts in weights:
            cell = make_cell(menu, tag, rows, wts)
            if not check_truth(cell):
                continue
            level, _m, _c, _s = operative_level(cell, ALPHA)
            best, arg = all_optima(cell, ALPHA)
            if best is None:
                continue
            cells += 1
            room = room_of(cell, level)
            cid = (tag, rows, wts)
            for r in range(cell.M):
                if all(s[r] == 0 for s in arg):
                    fate = "ab"
                elif all(s[r] > 0 for s in arg):
                    fate = "sv"
                else:
                    continue
                for kf, idx in zip(keyfns, indexes):
                    slot = idx.setdefault(kf(cell, r, level, room),
                                          {"ab": set(), "sv": set()})
                    slot[fate].add(cid)
    return cells


def read_index(idx):
    coll = [k for k, s in idx.items() if s["ab"] and s["sv"]]
    reuse = sum(1 for s in idx.values() if len(s["ab"] | s["sv"]) >= 2)
    return len(idx), len(coll), reuse, coll


def q1():
    section("Q1  THE UNDER-KEYED AUDIT -- the room added to the key")
    t0 = time.time()
    eq = [{}, {}]
    un = [{}, {}]
    kf = (key_parent, key_room)
    n_eq = sweep_keys(MENU_A, "A-EQ", ROWS, [EQUAL], kf, eq)
    n_eq += sweep_keys(MENU_B, "B-EQ", ROWS, [EQUAL], kf, eq)
    n_un = sweep_keys(MENU_A, "A-UN", ROWS, WEIGHTS, kf, un)
    n_un += sweep_keys(MENU_B, "B-UN", ROWS, WEIGHTS, kf, un)
    print("  cells: %d equal-weight, %d unequal (%.1fs)"
          % (n_eq, n_un, time.time() - t0))
    for name, idx in (("parent key", eq[0]), ("room key", eq[1])):
        n, c, _r, _ = read_index(idx)
        print("  C1 equal weights, %-10s: %d keys, %d collisions"
              % (name, n, c))
        ok(c == 0, "equal-weight collisions under the %s" % name)
    np_, cp, rp, coll_p = read_index(un[0])
    nr, cr, rr, coll_r = read_index(un[1])
    print("  C2 unequal, parent key: %d distinct keys, %d colliding, "
          "%d keys reused across cells (%.3f)" % (np_, cp, rp, rp / np_))
    ok(np_ == 444 and cp == 67, "parent key reprints 444 / 67")
    print("  unequal, ROOM key:      %d distinct keys, %d colliding, "
          "%d keys reused across cells (%.3f)" % (nr, cr, rr, rr / nr))
    rooms = sorted({k[3] for k in un[1]})
    print("  distinct room values across the forced atoms: %d "
          "(min %s, max %s)" % (len(rooms), rooms[0], rooms[-1]))
    # how a parent collision splits under the room: does the room
    # separate the abandoned side from the served side?
    split_clean = 0
    for k in coll_p:
        ab_rooms = {kk[3] for kk in un[1] if kk[:3] == k and un[1][kk]["ab"]}
        sv_rooms = {kk[3] for kk in un[1] if kk[:3] == k and un[1][kk]["sv"]}
        if not (ab_rooms & sv_rooms):
            split_clean += 1
    print("  parent collisions the room separates cleanly: %d of %d"
          % (split_clean, cp))
    for k in coll_r[:3]:
        s = un[1][k]
        print("  surviving collision: mass %s row (%s) level %s room %s "
              "-- abandoned in %d cell(s), served in %d"
              % (k[0], ",".join(str(v) for v in k[1]), k[2], k[3],
                 len(s["ab"]), len(s["sv"])))
    if cr == 0 and rr / nr >= 0.1:
        verdict = "KILLED -- under-keyed"
    elif cr >= 5:
        verdict = "SURVIVES"
    else:
        verdict = "BETWEEN"
    print("  Q1 verdict: %s (room-key collisions %d, reuse %.3f)"
          % (verdict, cr, rr / nr))
    return verdict, cr, rr / nr, split_clean


# =============================================================== Q2

def iroot(a, k):
    """Largest r with r^k <= a, exact: Newton from a power-of-two seed.
    The parent's float-seeded root corrects by unit steps and walks 10^8
    of them once a exceeds 2^53 -- the runaway this file's first run hit."""
    if a < 2:
        return a
    r = 1 << ((a.bit_length() + k - 1) // k)
    while True:
        nr = ((k - 1) * r + a // r ** (k - 1)) // k
        if nr >= r:
            break
        r = nr
    while r ** k > a:
        r -= 1
    while (r + 1) ** k <= a:
        r += 1
    return r


def make_supply(c):
    """c = p/q. m(g) = ceil g^(q/p); M(d) = floor d^(p/q), both exact."""
    p, q = c.numerator, c.denominator

    def m(g):
        if g <= 0:
            return 0
        r = iroot(g ** q, p)
        return r if r ** p >= g ** q else r + 1

    def M(d):
        return iroot(d ** p, q)
    return m, M


def offset_word(c, n_land):
    """The normalized offset at the first n_land landings, streamed."""
    m, M = make_supply(c)
    t, d = 0, 2
    xs = []
    dev, ndev = 0.0, 0
    while len(xs) < n_land:
        while True:
            nd = m(t + d + 2)
            if nd <= d:
                break
            d = nd
        t += d
        top, top1 = M(d) - 2, M(d - 1) - 2
        x = F(top - t, top - top1)
        xs.append(float(x))
        n = len(xs)
        if 100 <= n < 20000:
            y = 1.0 - math.fmod((t + 2) ** (1.0 / float(c)), 1.0)
            dev += abs(float(x) - y)
            ndev += 1
    return xs, dev / ndev


def ladder(xs):
    d4 = star_discrepancy(xs[:10000])
    d5 = star_discrepancy(xs[:100000])
    d6 = star_discrepancy(xs)
    return (math.log(d5 / d4) / math.log(10),
            math.log(d6 / d5) / math.log(10), d6)


def q2():
    section("Q2  THE ORBIT SIEVE -- the exponent at c = 4/3 and 5/3")
    N = 1000000
    cs = [F(4, 3), F(3, 2), F(5, 3), F(7, 4)]
    out = {}
    for c in cs:
        t0 = time.time()
        xs, dev = offset_word(c, N)
        s45, s56, d6 = ladder(xs)
        out[c] = s56
        print("  c = %s: closed-form deviation %.5f over landings "
              "100..20000; D*(10^6) = %.6f; slope 10^4..10^5 %.2f, "
              "slope 10^5..10^6 %.2f  (%.1fs)"
              % (c, dev, d6, s45, s56, time.time() - t0))
        ok(dev < 0.001, "closed form at c = %s" % c)
        del xs
    ok(abs(out[F(3, 2)] - (-0.58)) <= 0.02
       and abs(out[F(7, 4)] - (-0.37)) <= 0.02,
       "C3 reprint of -0.58 and -0.37")
    rnd = []
    for seed in (1, 2, 3):
        rng = random.Random(seed)
        xs = [rng.random() for _ in range(N)]
        s45, s56, d6 = ladder(xs)
        rnd.append(s56)
        print("  random seed %d: slope 10^4..10^5 %.2f, slope "
              "10^5..10^6 %.2f" % (seed, s45, s56))
        del xs
    seq = [out[c] for c in cs]
    mono = all(seq[i] <= seq[i + 1] for i in range(3))
    spread = max(seq) - min(seq)
    print("  exponents in c order (4/3, 3/2, 5/3, 7/4): %s; monotone %s; "
          "spread %.2f; random seeds %s"
          % (", ".join("%.2f" % s for s in seq), mono, spread,
             ", ".join("%.2f" % s for s in rnd)))
    if not mono or spread < 0.15:
        verdict = "KILLED -- no one-parameter law"
    elif spread >= 0.25:
        verdict = "SURVIVES"
    else:
        verdict = "BETWEEN"
    print("  Q2 verdict: %s" % verdict)
    return verdict, seq, rnd


# =============================================================== Q3

def ramified_key(D, p, sign, member, rt):
    """The class of a prime ideal of norm p, p ramified or split (any p
    with a form (p, b, c) of discriminant D, 2 included)."""
    for b in range(0, 2 * p):
        if (b * b - D) % (4 * p) == 0:
            f = (p, b, (b * b - D) // (4 * p))
            if sign < 0:
                return reduce_definite(f, D)
            return member[reduce_form(f, D, rt)]
    return None


def is_square(order, h):
    return (h // 2) % order == 0


def census(sign, dbound, plist):
    old = CO.DBOUND
    CO.DBOUND = dbound
    try:
        rows, bad, id_bad, c2_bad, c4_bad, law_bad = CO.sweep(sign, plist)
    finally:
        CO.DBOUND = old
    fields = []
    for D, hplus, recs, orders, n0, tot0, q, hits in rows:
        h = hplus
        if h % 2 or h < 2:
            continue
        if max(orders.values()) != h:
            continue                                  # not cyclic
        if sign > 0:
            hw, hp2, neps = class_data_real(D, math.isqrt(D))
            if neps != -1:
                continue                              # narrow != wide
            ok(hw == hp2 == h, "D=%d: h, h+ disagree at N(eps) = -1" % D)
        fields.append((D, h, recs, orders, hits))
    return fields


def rank_table(fields, sign, tag, plist):
    print("  %s: %d fields with a cyclic even class group" % (tag, len(fields)))
    if not fields:
        return None
    ranks = defaultdict(lambda: [0, 0])
    null1 = []
    ns_all = tot_all = 0
    pr1 = defaultdict(lambda: [0, 0])
    prk = defaultdict(lambda: [0, 0])
    gen_fail = 0
    far = [0, 0]
    for D, h, recs, orders, hits in fields:
        rt = int(math.isqrt(abs(D)))
        member = None
        if sign > 0:
            _r, member, _t, rt = classes_real(D)
        B = math.sqrt(D) / 2 if sign > 0 else 2 * math.sqrt(-D) / math.pi
        # the fixed part: ramified primes below B, 2 included
        fixed_ns = False
        two_ns = False
        for p in plist:
            if p > B:
                break
            if D % p == 0:
                k = ramified_key(D, p, sign, member, rt)
                if k is not None and not is_square(orders[k], h):
                    fixed_ns = True
            elif p == 2 and kronecker(D, 2) == 1:
                k = ramified_key(D, 2, sign, member, rt)
                two_ns = k is not None and not is_square(orders[k], h)
        # the unknown part: split primes below B (2 included, as a coin)
        m = sum(1 for p in plist if p <= B and D % p and kronecker(D, p) == 1)
        # the actual generation check (C5): some prime ideal below B a
        # non-square, split or ramified, 2 read exactly
        actual = fixed_ns or two_ns or any(
            not is_square(orders[k], h) for p, k in hits if p <= B)
        if not actual:
            gen_fail += 1
        first = hits[0][0]
        if fixed_ns or first > B or m == 0:
            nl = 0.5
        else:
            nl = 0.5 / (1 - 0.5 ** m)
        null1.append(nl)
        for i, (p, k) in enumerate(hits[:8]):
            ns = not is_square(orders[k], h)
            ranks[i + 1][0] += ns
            ranks[i + 1][1] += 1
            if p <= 50:
                (pr1 if i == 0 else prk)[p][0] += ns
                (pr1 if i == 0 else prk)[p][1] += 1
        for p, k in hits:
            ns = not is_square(orders[k], h)
            ns_all += ns
            tot_all += 1
            if p >= 1000:
                far[0] += ns
                far[1] += 1
    ok(gen_fail == 0, "%s: %d fields whose classes below B generate "
       "nothing non-square" % (tag, gen_fail))
    print("  C5 generation satisfied at every field: fails %d" % gen_fail)
    share_all = ns_all / tot_all
    se_all = math.sqrt(0.25 / tot_all)
    print("  C6 pooled non-square share over all odd split primes: %.4f "
          "+- %.4f over %d places" % (share_all, se_all, tot_all))
    ok(abs(share_all - 0.5) <= 2 * se_all, "%s Chebotarev pool" % tag)
    sf, sef = far[0] / far[1], math.sqrt(0.25 / far[1])
    print("  C6b the same pool over 1000 <= p < 10^4: %.4f +- %.4f over %d"
          % (sf, sef, far[1]))
    ok(abs(sf - 0.5) <= 3 * sef, "%s far-band pool" % tag)
    print("  non-square share of the r-th odd split prime:")
    r1 = None
    for r in sorted(ranks):
        n, tot = ranks[r]
        sh = n / tot
        se = math.sqrt(sh * (1 - sh) / tot) if 0 < sh < 1 else 0.0
        print("    rank %d: %.3f +- %.3f  (%d of %d)" % (r, sh, se, n, tot))
        if r == 1:
            r1 = (sh, se)
    nl = sum(null1) / len(null1)
    print("  conditioned null at rank 1 (exact Minkowski generation, "
          "averaged over fields): %.3f; fields with a ramified non-square "
          "below B (null 1/2): %d of %d"
          % (nl, sum(1 for x in null1 if x == 0.5), len(null1)))
    print("  rank-1 excess over 1/2: %+.3f; over the conditioned null: "
          "%+.3f (se %.3f)" % (r1[0] - 0.5, r1[0] - nl, r1[1]))
    print("  (p, rank) table, non-square share at rank 1 / rank >= 2:")
    wsum = dsum = 0.0
    near, farb = [0, 0], [0, 0]
    for p in sorted(set(pr1) | set(prk)):
        a, b = pr1.get(p, [0, 0]), prk.get(p, [0, 0])
        if p <= 23:
            print("    p = %2d: rank 1 %s (%d)   rank >= 2 %s (%d)"
                  % (p, "%.2f" % (a[0] / a[1]) if a[1] else "  -", a[1],
                     "%.2f" % (b[0] / b[1]) if b[1] else "  -", b[1]))
        if a[1] >= 15 and b[1] >= 15:
            s1, sk = a[0] / a[1], b[0] / b[1]
            var = (max(s1 * (1 - s1), 0.01) / a[1]
                   + max(sk * (1 - sk), 0.01) / b[1])
            wsum += 1 / var
            dsum += (s1 - sk) / var
        if b[1] and p <= 23:
            cell = near if p <= 7 else farb
            cell[0] += b[0]
            cell[1] += b[1]
    Dc, Dse = dsum / wsum, 1 / math.sqrt(wsum)
    sn, sfb = near[0] / near[1], farb[0] / farb[1]
    drop_se = math.sqrt(0.25 / near[1] + 0.25 / farb[1])
    print("  Q3b rank against norm: pooled rank-1 minus rank->=2 share at "
          "fixed p, D = %+.3f (se %.3f); rank->=2 share at p <= 7 %.3f (%d) "
          "against 11 <= p <= 23 %.3f (%d), drop %+.3f (se %.3f)"
          % (Dc, Dse, sn, near[1], sfb, farb[1], sn - sfb, drop_se))
    return r1, nl, (Dc, Dse), (sn - sfb, drop_se)


def q3():
    section("Q3  THE RANK-SEATED BIAS -- the least odd split prime of a "
            "quadratic field")
    plist = primes_upto(CO.PCAP)
    t0 = time.time()
    real = census(+1, 16000, plist)
    r_real = rank_table(real, +1, "real, N(eps) = -1, D <= 16000", plist)
    print("  (%.1fs)" % (time.time() - t0))
    t0 = time.time()
    imag = census(-1, 8000, plist)
    r_imag = rank_table(imag, -1, "imaginary, |D| <= 8000", plist)
    print("  (%.1fs)" % (time.time() - t0))
    arms = [x for x in (r_real, r_imag) if x is not None]
    book = all(r1[0] - nl < 2 * r1[1] for r1, nl, _d, _k in arms)
    flat = all(abs(r1[0] - 0.5) < 2 * r1[1] for r1, nl, _d, _k in arms)
    norm = all(d[0] + 2 * d[1] < 0.05 and k[0] - 2 * k[1] >= 0.05
               for _r, _n, d, k in arms)
    surv = all(d[0] - 2 * d[1] >= 0.10 for _r, _n, d, _k in arms)
    if book:
        verdict = "KILLED -- generation bookkeeping"
    elif flat:
        verdict = "KILLED -- an S4 accident"
    elif norm:
        verdict = "KILLED -- norm-seated (the refrozen kill)"
    elif surv:
        verdict = "SURVIVES"
    else:
        verdict = "BETWEEN"
    print("  Q3 verdict: %s" % verdict)
    return verdict, arms


if __name__ == "__main__":
    t0 = time.time()
    v1 = q1()
    v2 = q2()
    v3 = q3()
    print("\nSUMMARY")
    print("  Q1 %s" % v1[0])
    print("  Q2 %s" % v2[0])
    print("  Q3 %s" % v3[0])
    print("  controls: %d run, %d failed" % (CHECKS[0], CHECKS[1]))
    print("  wall %.1fs" % (time.time() - t0))
