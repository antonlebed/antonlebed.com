"""The ramified consumer's door, derived: why one residue class runs longest.

THE QUESTION. A place over 2 of a ramified quadratic field, seated at depth
1, is handed a state whose exponent already carries 2^2 (the norm-5 carrier
supplies exactly that much). The cheapest deepening of that place -- its
DOOR -- is the least r whose lambda no longer divides what the state has.
Swept over the 28 ramified quadratic fields Q(sqrt d), d squarefree,
|d| <= 60, the corpus reports that door taking exactly three values sorted
with no exceptions by d mod 8: 5 at d = 2 and 6, 6 at d = 3, 7 at d = 7
(explore_norm5_carrier.py, S5). Two things about that reading are recorded
as unexplained. First, WHY d = 7 runs longest is filed open. Second, d mod 8
is strictly COARSER than the completion Q_2(sqrt d) -- those 28 fields
realize all six ramified quadratic extensions of Q_2 against four residues,
so the door is constant across completions the residue merges -- and the
same reading also attributes the door's size to "how long the flat stretch
runs", which is completion data. Both cannot be the owner.

THE REDUCTION, DERIVED ON PAPER BEFORE ANY ENGINE CODE. The place is
ramified with residue field F_2, so |(O/P^n)^*| = 2^(n-1) and lambda(P^n) is
a pure 2-power 2^(c_n); the state's exponent has 2-part exactly 2^2; so
lambda(P^n) fails to divide it exactly when c_n >= 3, i.e. exactly when some
unit's fourth power is not 1 mod P^n. Hence

    door(d) = min over units u, u^4 != 1, of v_P(u^4 - 1).

For a ramified place e = 2 and f = 1 give v_P(x) = v_2(N(x)), and the norm
of the fourth-power defect FACTORS through the trace and norm of u alone:

    N(u^4 - 1) = (N - T + 1) * (N + T + 1) * ((N-1)^2 + T^2),

N = N(u), T = Tr(u), from N(u-1), N(u+1) and N(u^2+1) = (N-1)^2 + T^2. The
third factor is A SUM OF TWO SQUARES, which is where the 2-adic content
sits: an odd square is 1 mod 8, so two odd squares sum to exactly 2 mod 8
and contribute one factor of 2, while an odd and an even sum to something
odd and contribute none. That single parity is the whole candidate mechanism
and it reads d only mod 8.

THE HAND DERIVATION (to be confirmed or killed by the rig below). Write
u = p + q*sqrt(d), j = v_P(u - 1). For j >= 3 the three factors have
valuations j, 2, 2, so v_P(u^4 - 1) = j + 4 >= 7. For j = 2, u = 1 + 2w with
w a unit, and v_P(u+1) = 2 + v_P(w+1) >= 3 since every unit is 1 mod P, so
again >= 7. So the minimum, whenever it is below 7, is attained at j = 1,
and door <= 7 for EVERY ramified quadratic. At j = 1 the two outer factors
contribute 1 each and the sum of squares decides:

  d = 2 mod 4 (so d = 2, 6 mod 8), d = 2m with m odd. A unit needs p odd.
  With q odd the outer factors are (p-1)^2 - 2mq^2 and (p+1)^2 - 2mq^2, each
  of valuation exactly 1; N - 1 = (p^2 - 1) - 2mq^2 has valuation exactly 1
  since 8 | p^2 - 1; so the sum of squares is 4*((N-1)/2)^2 + 4p^2 with both
  halves ODD, valuation exactly 3. Total exactly 5. With q even the outer
  factors already cost 5 and the total is >= 7. So door = 5, and the
  derivation never consults m mod 4 -- which is why d = 2 and d = 6 mod 8
  agree rather than merely happening to.

  d = 3 mod 4 (so d = 3, 7 mod 8), d odd. A unit needs p + q odd; p odd with
  q even is the j >= 2 case, so take p even, q odd. Both outer factors are
  odd^2 - d*odd^2 = 1 - d mod 8, valuation exactly 1. Writing p = 2p' and
  N - 1 = 4p'^2 - (d q^2 + 1), the sum of squares is (N-1)^2 + 16p'^2, and
  d q^2 + 1 = d + 1 mod 8 splits the two classes:
    d = 3 mod 8: d q^2 + 1 = 4 mod 8. At p = 0 this gives v_2(N-1) = 2 with
      (N-1)/4 odd and p' = 0 even, so the two squares are odd and even, the
      sum has valuation 4 exactly, and the total is 6.
    d = 7 mod 8: d q^2 + 1 = 0 mod 8. Then p' even forces v_2(N-1) >= 3 and
      the total >= 8; p' ODD forces v_2(N-1) = 2 with BOTH (N-1)/4 and p'
      odd, so the sum of squares picks up the extra factor of 2 -- valuation
      5 -- and the total is 7. There is no third option, so door = 7.
  Equivalently, for d = 3 mod 4 the whole answer is
      door(d) = 6 + v_2(s^2 + 1),  s = (d - 3)/4,
  which is 6 for s even (d = 3 mod 8) and 7 for s odd (d = 7 mod 8).

SO THE ANSWER TO THE OPEN CLAUSE, IF THE RIG CONFIRMS IT, is that the
longest-running class is the one where a parity forces two ODD squares into
the sum, and the reason the door is coarser than the completion is that
nothing in the derivation reads d beyond mod 8. The flat stretch's length is
then not completion data at all -- it is a function of d mod 8, and the
attribution to the completion is the wrong owner.

TRANSPLANTS AND WHAT IS NOT CARRIED.
 T1 The door's DEFINITION is transplanted from explore_norm5_carrier.py:
    least r >= 1 with lambda(P^(a+r)) not dividing the state's exponent, at
    a = 1. The hypothesis that the seated state's 2-part is exactly 2^2 is
    that script's finding (v_2(N(Q) - 1) = 2 at every norm-5 carrier) and is
    carried as a HYPOTHESIS, named in P3's control rather than re-derived.
 T2 The corpus's three door values (5, 6, 7 by residue) and Q(i)'s column
    (v_2 = 0,1,2,2,2,2,2,3,3) are QUOTED as the numbers to reproduce. They
    are re-bruted here from scratch -- no import of the carrier scripts --
    so a disagreement is a real disagreement and not a shared routine
    compared with itself.
 T3 No class group, no walk, no ideal menu. The object here is one place of
    one field and its unit group; the walk that spends the door is somebody
    else's rig.
 T4 v_P(x) = v_2(N(x)) is used throughout and is a PROPERTY of a ramified
    place (e = 2, f = 1), re-checked in S1 rather than assumed.

REPRESENTATIVE STABILITY, the one numerical trap. Units are enumerated as
(p, q) mod 2^K. Changing p or q by 2^K moves u^4 - 1 by an amount of
valuation at least 2K, so any valuation strictly below 2K read off a
representative is the true 2-adic valuation. Every value this rig reports is
compared against 2K and a value at or above it is reported as CENSORED
rather than as a number.

PREDICTIONS, FIXED BEFORE THE RUN.
 P1 POSITIVE CONTROL, run and read before any verdict. v_P = v_2 o N holds
    at every sampled element of every sampled ramified field; and the
    independently bruted lambda column of Q(i)'s place over 2 is
    v_2 = 0,1,2,2,2,2,2,3,3 at n = 1..9, the corpus's own printed column. If
    either fails the rig is wrong and no door reading below is worth
    reading.
 P2 The norm identity N(u^4 - 1) = (N-T+1)(N+T+1)((N-1)^2 + T^2) holds
    EXACTLY, as integers, at every sampled (p, q, d).
 P3 THE REDUCTION. min over units of v_P(u^4 - 1) equals the door computed
    the corpus's way -- straight off the bruted lambda column, as the least
    r with lambda(P^(1+r)) not dividing 4 -- at all 28 fields. A mismatch
    kills the reduction and with it everything after it.
 P4 THE CLOSED FORM. Over every squarefree d with 2 ramified and
    |d| <= 2000, the bruted door is 5 at d = 2, 6 mod 8; 6 at d = 3 mod 8;
    7 at d = 7 mod 8. No exceptions.
 P5 THE MINIMUM'S SEAT. Restricted to units with v_P(u - 1) >= 2 the
    minimum is >= 7 at every field, so the door is attained at j = 1
    wherever it is below 7 -- and the door never exceeds 7 anywhere.

KILL-SHAPES, as observables this rig PRINTS.
 K1 S1 prints a v_P != v_2 o N sample, or a Q(i) column differing from
    0,1,2,2,2,2,2,3,3. Either kills the rig, not the claim.
 K2 S2 prints a nonzero identity-mismatch count. Kills the factorization
    the whole derivation runs through.
 K3 S3 prints a nonzero count of fields where the min-over-units door and
    the column door disagree. Kills the reduction.
 K4 S4 prints any ramified d whose door is outside {5, 6, 7}, or any d
    whose door disagrees with its residue class. Kills the closed form --
    and a door outside {5,6,7} kills the j >= 2 lower bound with it.
 K5 S5 prints a field where the j >= 2 minimum is below 7. Kills P5 and
    means the hand case analysis missed a seat.

WHAT A SURVIVING RUN WOULD AND WOULD NOT BUY. It would turn an open clause
into a rule verified over a stated range with a hand proof beside it, and
move the door's ownership from the completion to d mod 8. It would NOT say
anything about the walks that spend the door, about the carrier's ablation,
or about the limit -- those are measured elsewhere and are not touched here.

FINDINGS (run 2026-06-09; peak 11.6 MB, wall 2.8s; every prediction held).

F1 THE CONTROL PASSED FIRST. v_P(2) = 2 with v_P additive over 26 fields, 0
   violations; and the lambda column of Q(i)'s place over 2, bruted here
   from the unit group with nothing imported, is c_n = 0,1,2,2,2,2,2,3,3 at
   n = 1..9 -- the corpus's own printed column, character for character. The
   norm identity held exactly at 5915 integer samples, 0 mismatches.

F2 THE REDUCTION HOLDS (P3). min over units of v_P(u^4 - 1) equals the door
   read off the bruted column at all 49 ramified fields with |d| <= 60, 0
   disagreements. Note the SCOPE difference from the carrier sweep: that one
   reads 28 fields, being the ramified arm of the 41 fields where 5 also has
   a degree-1 place, since a norm-5 carrier is what supplies the state its
   2-part there. The door law needs only THAT the seated state's 2-part is
   exactly 2^2 and never that a norm-5 place is what supplied it, so it is
   stated here over every ramified quadratic and the carrier's 28 are a
   sub-family of the 49.

F3 THE DOOR LAW (theorem; verified at 1619 fields, |d| <= 2000, 0
   off-residue and 0 censored). For every squarefree d with 2 ramified, the
   depth-1 door of the place over 2 against a state of 2-part exactly 2^2 is

       door(d) = 5  at d = 2 and 6 mod 8      (404 and 404 fields)
                 6  at d = 3 mod 8            (405 fields)
                 7  at d = 7 mod 8            (406 fields)

   and NEVER anything else -- the three values the carrier sweep measured
   are the three that exist. The proof is the case analysis in the slate
   above and is complete for all such d: j = v_P(u-1) >= 3 gives j + 4 >= 7,
   j = 2 gives >= 7 because a unit's 1 + w is always even, and j = 1 -- which
   for odd d means p even with q odd, and for d = 2 mod 4 means q odd -- puts
   1 on each outer factor and leaves the sum of two squares to decide. Hence
   also door <= 7 at every ramified quadratic, with no computation in it.

F4 WHY 7 RUNS LONGEST: TWO ODD SQUARES. For d = 3 mod 4 the whole law is
   door(d) = 6 + v_2(s^2 + 1) with s = (d-3)/4 -- 0 misses over every such d
   to 2000. s is even exactly at d = 3 mod 8, where s^2 + 1 is odd and buys
   nothing; s is odd exactly at d = 7 mod 8, where s^2 + 1 = 2 mod 8 because
   an odd square is 1 mod 8, and that single factor of 2 is the extra rung.
   The open clause's answer is therefore a parity, not a depth: the longest
   class is the one whose sum of two squares has both summands odd.

F5 WHY 2 AND 6 MOD 8 AGREE (P4's other half). Write d = 2c with c odd -- c,
   NOT d, is the quantity whose parity is at issue here, and conflating the
   two is easy enough that it is worth naming: d is EVEN throughout this
   case. The j = 1 computation reads c only through "c is odd". The two
   outer factors are valuation 1 for either parity class of c, and the sum
   of squares is 4(((N-1)/2)^2 + p^2) with both summands odd whatever c is.
   So the door is 5 with no c-dependence at all, which is why the two
   residues coincide rather than coinciding by accident. Printed at nine
   fields spanning both residues and both signs: door 5 at every one.

F6 THE MINIMUM'S SEAT (P5). Restricted to units with v_P(u-1) >= 2, the
   minimum is >= 7 at every one of the 49 fields, 0 exceptions -- so the
   door is attained at j = 1 wherever it is below 7, as the hand analysis
   requires. This is what makes F3's case analysis exhaustive rather than
   suggestive.

F7 SO THE OWNER WAS WRONG, AND THIS IS THE CORRECTION. The corpus reads the
   door's size off "how long the column's flat stretch runs", and files that
   length as COMPLETION data -- while separately reporting the door constant
   on d mod 8, which is strictly coarser than the completion. Both cannot
   own it, and F3 settles which: every step of the derivation reads d only
   mod 8 (through 1 - d mod 8, d q^2 + 1 mod 8, and "m is odd"), so the flat
   stretch's LENGTH is a function of d mod 8 and the door is constant across
   completions the residue merges BECAUSE nothing finer than the residue
   ever enters. The completion still owns plenty here -- it owns which
   quadratic extension of Q_2 the place sits in, six of them over these
   residues' four classes -- but it does not own the door, and the earlier
   reading credited it with a quantity the derivation never consults it for.

WHAT THIS DOES NOT TOUCH, restated after the run because the temptation is
strongest now. Nothing here measures a walk, an ablation or a limit; the
door is a price and this rig says only what the price IS. Whether any walk
pays it, and what it buys when paid, is explore_norm5_carrier.py's reading
and is unchanged by this.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from math import gcd

# ---------------------------------------------------------------- parameters

K_UNITS = 5           # units enumerated as (p, q) mod 2^K_UNITS
K_SPECIMEN = 6        # the wider box used on the 28 specimen fields
CENSOR = 2 * K_UNITS  # valuations at or above this are not trusted
COLUMN_DEPTH = 9      # rungs of the lambda column the control reproduces
SPECIMEN_BOUND = 60   # the corpus's own sweep box
WIDE_BOUND = 2000     # the closed form's range

QI_COLUMN = (0, 1, 2, 2, 2, 2, 2, 3, 3)   # quoted, explore_norm5_carrier.py
STATE_TWO_PART = 4                        # the seated carrier's 2-part, 2^2

DOOR_BY_RESIDUE = {2: 5, 6: 5, 3: 6, 7: 7}


# ------------------------------------------------------------------ 2-adics

def v2(n):
    """2-adic valuation of a nonzero integer."""
    assert n != 0, "v2(0) is undefined -- caller must screen exact zeros"
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def squarefree(n):
    m = abs(n)
    if m < 2:
        return m == 1
    i = 2
    while i * i <= m:
        if m % (i * i) == 0:
            return False
        i += 1
    return True


def ramified_ds(bound):
    """Squarefree d, |d| <= bound, d != 1, with 2 RAMIFIED in Q(sqrt d):
    exactly d = 2, 3 mod 4 (which is also when O_K = Z[sqrt d])."""
    out = []
    for d in range(-bound, bound + 1):
        if d in (0, 1) or not squarefree(d):
            continue
        if d % 4 in (2, 3):
            out.append(d)
    return out


# --------------------------------------------------- arithmetic in Z[sqrt d]

def mul(a, b, d):
    (p, q), (r, s) = a, b
    return (p * r + q * s * d, p * s + q * r)


def norm(a, d):
    p, q = a
    return p * p - d * q * q


def powq(a, e, d):
    out, base = (1, 0), a
    while e:
        if e & 1:
            out = mul(out, base, d)
        base = mul(base, base, d)
        e >>= 1
    return out


def vP(a, d):
    """v_P at the ramified place over 2. For e = 2, f = 1 the norm's 2-adic
    valuation IS v_P: v_P(N(x)) = 2 v_P(x) and v_P(2) = 2. Returns None for
    the exact zero, which has no valuation and is screened by the caller."""
    n = norm(a, d)
    if n == 0:
        return None
    return v2(n)


def sub1(a):
    return (a[0] - 1, a[1])


_UNIT_CACHE = {}


def units_mod(d, k):
    """Unit representatives (p, q) mod 2^k: N(u) odd. Every unit of the local
    ring is congruent to one of these mod 2^k. Membership depends on d only
    through d mod 2, so the list is cached on (d mod 2, k)."""
    key = (d % 2, k)
    if key not in _UNIT_CACHE:
        M = 1 << k
        _UNIT_CACHE[key] = [(p, q) for p in range(M) for q in range(M)
                            if norm((p, q), d) % 2 != 0]
    return _UNIT_CACHE[key]


# --------------------------------------------- S1  the positive control

def s1_control():
    print("S1  POSITIVE CONTROL -- the valuation identity and Q(i)'s column")

    # v_P cannot be checked against "the largest n with x inside P^n" when
    # P^n is itself read off the norm -- that is the same routine compared
    # with itself. So check instead the two properties that PIN a ramified
    # v_P and that a wrong normalization would break: v_P(2) = 2 (e = 2),
    # and additivity on products. The external anchor is the column below.
    bad = 0
    for d in ramified_ds(30):
        if vP((2, 0), d) != 2:
            bad += 1
            print("    v_P(2) != 2 at d = %d" % d)
        for a in [(1, 1), (3, 2), (2, 1), (5, 4), (1, 2)]:
            for b in [(1, 1), (7, 3), (2, 3)]:
                va, vb = vP(a, d), vP(b, d)
                vab = vP(mul(a, b, d), d)
                if va is None or vb is None or vab is None:
                    continue
                if vab != va + vb:
                    bad += 1
                    print("    v_P not additive at d = %d: %s %s" % (d, a, b))
    print("    v_P(2) = 2 and additivity: %d violations over %d fields"
          % (bad, len(ramified_ds(30))))

    # The lambda column of the ramified place over 2 in Q(i), bruted from
    # the unit group with no carrier machinery imported. c_n = log2 of the
    # exponent of (O/P^n)^*: the max over units of the least e with
    # u^(2^e) = 1 mod P^n.
    col = column(-1, K_SPECIMEN)
    print("    Q(i) column c_n, n = 1..%d: %s" % (COLUMN_DEPTH, col))
    print("    corpus's printed column:           %s" % (list(QI_COLUMN),))
    print("    MATCH" if tuple(col) == QI_COLUMN else "    MISMATCH -- K1")
    return bad, tuple(col) == QI_COLUMN


def column(d, k):
    """c_n for n = 1..COLUMN_DEPTH: log2 of the exponent of (O/P^n)^*."""
    us = units_mod(d, k)
    col = []
    for n in range(1, COLUMN_DEPTH + 1):
        worst = 0
        for u in us:
            e, x = 0, u
            while True:
                v = vP(sub1(x), d)
                if v is None or v >= n:
                    break
                x = mul(x, x, d)
                e += 1
                assert e < 20, "order search runaway"
            worst = max(worst, e)
        col.append(worst)
    return col


# --------------------------------------------- S2  the norm factorization

def s2_identity():
    print("S2  THE NORM IDENTITY  N(u^4-1) = (N-T+1)(N+T+1)((N-1)^2+T^2)")
    bad = samples = 0
    for d in ramified_ds(40):
        for p in range(-6, 7):
            for q in range(-6, 7):
                u = (p, q)
                N, T = norm(u, d), 2 * p
                lhs = norm(sub1(powq(u, 4, d)), d)
                rhs = (N - T + 1) * (N + T + 1) * ((N - 1) ** 2 + T * T)
                samples += 1
                if lhs != rhs:
                    bad += 1
                    if bad <= 3:
                        print("    mismatch d=%d p=%d q=%d" % (d, p, q))
    print("    %d samples, %d mismatches" % (samples, bad))
    return bad


# --------------------------------------------- S3  the reduction

def door_from_units(d, k, jmin=1):
    """min over units u with v_P(u-1) >= jmin, u^4 != 1, of v_P(u^4 - 1)."""
    best = None
    for u in units_mod(d, k):
        t = sub1(u)
        vt = vP(t, d)
        if vt is None:                      # u = 1 exactly: u^4 = 1
            continue
        if vt < jmin:
            continue
        v = vP(sub1(powq(u, 4, d)), d)
        if v is None:                       # a genuine 4th root of unity
            continue
        if best is None or v < best:
            best = v
    return best


def door_from_column(d, k):
    """The door the corpus's way: least r >= 1 with lambda(P^(1+r)) not
    dividing the seated state's 2-part."""
    col = column(d, k)          # col[i] = c_(i+1)
    r = 1
    while r < len(col) and STATE_TWO_PART % (1 << col[r]) == 0:
        r += 1
    assert r < len(col), "column too short to close the door -- raise depth"
    return r


def s3_reduction():
    print("S3  THE REDUCTION -- min over units against the column door")
    ds = ramified_ds(SPECIMEN_BOUND)
    bad = 0
    for d in ds:
        a = door_from_units(d, K_SPECIMEN)
        b = door_from_column(d, K_SPECIMEN)
        flag = "" if a == b else "   DISAGREE -- K3"
        if a != b:
            bad += 1
        if a != b or d in (-1, -6, 2, 3, 7, 15):
            print("    d = %4d  min-over-units %s  column door %s%s"
                  % (d, a, b, flag))
    print("    %d ramified fields to |d| <= %d, %d disagreements"
          % (len(ds), SPECIMEN_BOUND, bad))
    return bad


# --------------------------------------------- S4  the closed form

def s4_closed_form():
    print("S4  THE CLOSED FORM over every ramified d, |d| <= %d" % WIDE_BOUND)
    ds = ramified_ds(WIDE_BOUND)
    tally, offres, censored, outside = {}, [], 0, []
    for d in ds:
        v = door_from_units(d, K_UNITS)
        if v is None or v >= CENSOR:
            censored += 1
            continue
        res = d % 8
        tally.setdefault((res, v), 0)
        tally[(res, v)] += 1
        if v != DOOR_BY_RESIDUE[res]:
            offres.append((d, res, v))
        if v not in (5, 6, 7):
            outside.append((d, v))
    for key in sorted(tally):
        print("    d = %d mod 8, door %d: %5d fields" % (key[0], key[1],
                                                         tally[key]))
    print("    %d fields, %d censored at the 2^%d box, %d off-residue, "
          "%d outside {5,6,7}" % (len(ds), censored, K_UNITS, len(offres),
                                  len(outside)))
    for d, res, v in offres[:5]:
        print("    OFF-RESIDUE d = %d (%d mod 8) door %d -- K4" % (d, res, v))
    for d, v in outside[:5]:
        print("    OUTSIDE d = %d door %d -- K4" % (d, v))
    return len(offres), len(outside)


# --------------------------------------------- S5  the mechanism

def s5_mechanism():
    print("S5  THE MECHANISM -- the sum of two squares, and where j >= 2 sits")
    print("    d = 3 mod 4: door against 6 + v_2(s^2+1), s = (d-3)/4")
    bad = 0
    for d in ramified_ds(WIDE_BOUND):
        if d % 4 != 3:
            continue
        v = door_from_units(d, K_UNITS)
        s = (d - 3) // 4
        pred = 6 + v2(s * s + 1)
        if v != pred:
            bad += 1
            if bad <= 5:
                print("    formula miss d = %d: door %s predicted %d"
                      % (d, v, pred))
    print("    %d misses of the s-formula" % bad)

    print("    j >= 2 restricted minimum (P5: never below 7)")
    low = 0
    for d in ramified_ds(SPECIMEN_BOUND):
        v = door_from_units(d, K_SPECIMEN, jmin=2)
        if v is not None and v < 7:
            low += 1
            print("    d = %d: j>=2 min %d -- K5" % (d, v))
    print("    %d fields with a j >= 2 minimum below 7" % low)

    print("    d = 2 mod 4: door against c = d/2, which is the odd one (d is")
    print("    even here); independence of c is why 2 and 6 mod 8 agree")
    for d in [2, 6, 10, 14, -2, -6, -10, 22, 26]:
        if d % 4 != 2:
            continue
        print("      d = %4d (%d mod 8, c = %d): door %s"
              % (d, d % 8, d // 2, door_from_units(d, K_UNITS)))
    return bad, low


if __name__ == "__main__":
    print("=" * 70)
    print("THE RAMIFIED CONSUMER'S DOOR -- derived from the unit group")
    print("=" * 70)
    vbad, colok = s1_control()
    print()
    idbad = s2_identity()
    print()
    redbad = s3_reduction()
    print()
    offres, outside = s4_closed_form()
    print()
    sbad, jlow = s5_mechanism()

    # One line naming which kill-shape fired, so a reader of the output
    # alone -- not of this file -- knows whether any verdict above stands.
    print()
    fired = []
    if vbad or not colok:
        fired.append("K1 (control)")
    if idbad:
        fired.append("K2 (identity)")
    if redbad:
        fired.append("K3 (reduction)")
    if offres or outside:
        fired.append("K4 (closed form)")
    if jlow:
        fired.append("K5 (the minimum's seat)")
    if sbad:
        fired.append("the s-formula")
    print("VERDICT: " + ("every prediction held; no kill-shape fired"
                         if not fired else "FIRED -- " + ", ".join(fired)))
