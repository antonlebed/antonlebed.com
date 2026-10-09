"""column.py -- the closed form of a place's lambda column, where it holds,
what a number ring's norm does not fix of it, and which index its price is.

QUESTION. A place P of a Dedekind ring, residue field of N = p^f elements,
ramification index e over p, has lambda(P^b) = (N - 1) p^c(b) for b >= 1,
c(b) the number of ladder members below b (door.py; clock.py). The
TAME CLOSED FORM
    lambda(P^b) = (N - 1) p^ceil((b - 1)/e)
is what a place's norm and one gap can express. Three questions.
  (a) At exactly which places does the closed form hold at every depth?
  (b) Does a norm fix a column even inside one ring?
  (c) The price N^r of a move from depth a to a + r is the additive index
      [P^a : P^(a+r)]. When is it the unit group's index, and by how much
      does it part from it?

THE ARGUMENT (written before the engine).
  (1) THE STAIRCASE. c determines the ladder (x_j is the least b with
      c(b + 1) = j), and ceil((b - 1)/e) is the c of the ladder
      1, 1 + e, 1 + 2e, ..., the STAIRCASE. So the closed form holds at
      every depth iff the ladder is the staircase. By the ladder theorem
      (clock.py) the ladder is psi's orbit from 1, psi(i) = min(pi, i + e),
      save one overshoot by the width w where the bend s = e/(p - 1) is a
      power of p.
        e < p - 1: s < 1, so every i >= 1 lies above the bend, psi(i) =
          i + e, s is no power of p, and the ladder is the staircase.
        e = p - 1: s = 1 = p^0, and the ladder is 1, A, A + e, ... with
          A = s + e + w = 1 + e + w: the staircase iff w = 0
          iff there is no head, and by the head criterion that is iff not
          (f = 1 and mu_p in K).
        e > p - 1: s > 1, so 1 lies below the bend and x_2 = psi(1) = p <
          1 + e: the ladder departs at its second member.
      In equal characteristic e is infinite and the ladder is 1, p, p^2,
      ..., never a staircase. So THE CLOSED FORM HOLDS EXACTLY WHERE
      e <= p - 1 AND THE PLACE HAS NO HEAD.
  (2) THE QUADRATIC FIELDS. In Q(sqrt delta) e <= 2, so (1) fails only
      at p = 2 or 3. Over 2: a split place is Z_2, e = p - 1 = 1 with a
      head (u_bar = 1 = -1); an inert one has f = 2, no head, and obeys;
      a ramified one has e = 2 > 1 and departs. Over 3 only a ramified
      place has e = p - 1 = 2, and it has a head iff mu_3 is in
      Q_3(sqrt delta), iff that field is Q_3(sqrt -3), iff -delta/3 is a
      square in Q_3, iff delta/3 = 2 mod 3, iff delta = 6 mod 9. At every
      p >= 5 e = 2 < p - 1. So THE CLOSED FORM FAILS IN Q(sqrt delta)
      EXACTLY AT THE PLACES OVER 2 OF RESIDUE DEGREE 1, AND AT THE PLACE
      OVER 3 WHEN delta = 6 mod 9, and not at delta = 3 mod 9: not at
      every field where 3 ramifies.
  (3) A NORM DOES NOT FIX A COLUMN IN ONE RING. In a quadratic field a
      rational prime is split, inert or ramified and not two at once, so
      the places of one norm share (p, e, f) and one column. The ring of
      x^3 - x - 1 (discriminant -23, squarefree, so the ring is maximal)
      has x^3 - x - 1 = (x - 3)(x - 10)^2 mod 23, so 23 = P Q^2 with P of
      (e, f) = (1, 1) and Q of (2, 1), both of norm 23. Both have
      e <= 22 = p - 1 and no head, so both obey (1) with gaps 1 and 2:
      the columns agree at b = 1, 2 (22, 22 * 23) and part at b = 3,
      22 * 23^2 = 11638 against 22 * 23 = 506.
  (4) THE PRICE'S INDEX. |(O/P^b)^x| = (N - 1) N^(b - 1) for b >= 1, by
      the split (O/P^b)^x = (O/P)^x x U_1/U_b, and |U_1/U_b| = N^(b - 1)
      since each U_i/U_(i+1) is the residue field under addition. So for
      a SEATED place, a >= 1, the unit index |(O/P^(a+r))^x| /
      |(O/P^a)^x| is N^r, the price, and at an OPENING, a = 0, it is
      (N - 1) N^(r - 1), the price times (N - 1)/N. The two readings of
      the price agree on seated places and part at openings only.

TRANSPLANTS. The ladder theorem, the head criterion and the width are
clock.py's and are imported (ladder, criterion); the columns below are
read off the generators (module_law.py's E_gen), controlled against the
whole group (E_full) wherever it has at most 20000 elements, never off
the ladder they are compared with. The 23 places are built
here from the Hensel lift of x^3 - x - 1 over Z_23.

PREDICTIONS, fixed before the run.
  C  CONTROL. E_gen = E_full at every place used, to the depth where the
     group is at most 20000 elements; the Hensel factor of x^3 - x - 1
     over Z_23 is (x - r)(x^2 + s x + t) with r = 3 mod 23, and the
     quadratic shifted by 10 is Eisenstein.
  S  Over clock.py's 32 places plus x^2 - 15, x^2 + 15, x^2 - 21,
     x^2 + 21 at 3 and x^2 - 5, x^2 + 10 at 5 and x^2 - 7 at 7: the
     closed form holds at b = 1..D (D the ladder depth clock.py reads) at
     exactly the places with e <= p - 1 and criterion() false. At p = 3
     and e = 2 the headed places are exactly those with delta = 6 mod 9
     (x^2 - 6, x^2 + 3, x^2 - 15, x^2 + 21 of delta = 6, -3, 15, -21), and
     the others (x^2 - 3, x^2 + 15, x^2 - 21, of delta = 3, -15, 21) obey.
  R  At the ring of x^3 - x - 1: P and Q read columns 22, 506, 11638 and
     22, 506, 506 at b = 1, 2, 3, both equal to the closed form with e = 1
     and 2 to depth 12; and no other rational prime below 2000 has a
     repeated root of x^3 - x - 1.
  I  At every place of clock.py's list with N^3 <= 20000 and b = 1..3,
     the count of units of O/P^b is (N - 1) N^(b - 1), so the ratio at
     a >= 1 is N^r and at a = 0 is (N - 1) N^(r - 1).
KILLS, as printed observables: any C line off (nothing below is read);
an S place on the wrong side of the biconditional, or a p = 3 place off
its delta mod 9; an R column off 11638 / 506 at b = 3 or off the closed
form, or a second ramified prime; an I count off [ruled on audit: I
is printed, its count the enumeration's own shape].

FINDINGS. Every prediction landed, no kill fired: 8/8 checks PASS, I
  printed (its count is the enumeration's own shape).
  C  E_gen = E_full at 414 (place, depth) over the 41 places, 0 off; the
     Hensel root is 3 mod 23, and the shifted quadratic is y^2 - D with
     no linear term and v_23(D) = 1.
  S  Of the 39 places, the closed form holds at the 16 with e <= p - 1
     and no head and departs at the other 23, 0 on the wrong side. It
     departs first at b = p + 1 at every one of the 23: 3 over 2, 4 over
     3, 6 at x^4 + 5, 8 at x^6 + 7. That is forced: where e > p - 1,
     x_2 = p <= e, and where e = p - 1 with a head, x_2 = p + w > p;
     either way the column agrees with the staircase up to b = p and
     not at p + 1. At p = 3, e = 2 the head falls at delta = -3, 6, 15,
     -21, all 6 mod 9, and not at 3, -15, 21, all 3 mod 9.
  R  P reads 22, 506, 11638, 267674 and Q 22, 506, 506, 11638 at b = 1..4,
     both the closed form with e = 1 and 2 to depth 12; 23 is the only
     prime below 2000 with a repeated root.
  I  351 unit counts and index ratios at all 39 places read, each with
     N^3 <= 20000, 0 off: printed, not counted, since the units are
     enumerated as the expansions whose valuation is 0, a nonzero
     constant digit, so the count is (N - 1) N^(b - 1) by construction,
     val the only code it exercises, and the ratios follow.
  Tiers: (1) a theorem, a corollary of the ladder theorem and the head
  criterion, with the first departure at b = p + 1; (2) a theorem by the
  local classification; (3) a property, read at one ring; (4) a property.

RUN RECORD. 8/8, 17.4 s wall, peak commit 6.5 MB under a memory guard,
I printed rather than counted.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from module_law import Local, check, section, CHECKS, vp
from clock import PLACES, criterion, depth

LIMIT = 20000          # the whole group is enumerated up to this size
PREC = 20              # the 23 factor is carried mod 23^PREC
RING_DEPTH = 12

EXTRA = [
    Local(3, [-15, 0, 1], "eis", "x^2 - 15"),
    Local(3, [15, 0, 1], "eis", "x^2 + 15"),
    Local(3, [-21, 0, 1], "eis", "x^2 - 21"),
    Local(3, [21, 0, 1], "eis", "x^2 + 21"),
    Local(5, [-5, 0, 1], "eis", "x^2 - 5"),
    Local(5, [10, 0, 1], "eis", "x^2 + 10 at 5"),
    Local(7, [-7, 0, 1], "eis", "x^2 - 7"),
]
QUAD3 = {"x^2 + 3": -3, "x^2 - 3": 3, "x^2 - 6": 6, "x^2 - 15": 15,
         "x^2 + 15": -15, "x^2 - 21": 21, "x^2 + 21": -21}


def closed(loc, b):
    return (loc.q - 1) * loc.p ** (-(-(b - 1) // loc.e))


def whole_ok(loc):
    """E_gen = E_full wherever U_1/U_b has at most LIMIT elements."""
    off = seen = 0
    b = 1
    while loc.q ** (b - 1) <= LIMIT:
        seen += 1
        off += loc.E_gen(b) != loc.E_full(b)
        b += 1
    return seen, off


# ---------------------------------------------- the ring of x^3 - x - 1 at 23
def hensel_23():
    """(r, D, lin): x^3 - x - 1 = (x - r)(x^2 + r x + r^2 - 1) over Z_23 with
    r = 3 mod 23, and the quadratic, shifted by c = -r/2, is y^2 - D."""
    p, mod = 23, 23 ** PREC
    r = 3
    for _ in range(PREC):
        r = (r - (r ** 3 - r - 1) * pow(3 * r * r - 1, -1, mod)) % mod
    s, t = r, r * r - 1
    c = (-s * pow(2, -1, mod)) % mod
    D = (-(c * c + s * c + t)) % mod
    lin = (2 * c + s) % mod
    return r, D, lin


def section_control(pair):
    section("C. CONTROL: the whole group, and the Hensel factor at 23")
    seen = off = 0
    for loc in PLACES + EXTRA + list(pair):
        s, o = whole_ok(loc)
        seen += s
        off += o
    check("E_gen = E_full at every place used, groups <= 20000", off == 0,
          f"{seen} (place, depth) read, {off} off")
    r, D, lin = hensel_23()
    mod = 23 ** PREC
    print(f"  r = {r % 23} mod 23, (r^3 - r - 1) = 0 mod 23^{PREC}: "
          f"{(r ** 3 - r - 1) % mod == 0}; linear term {lin}, "
          f"v_23(D) = {vp(D, 23)}")
    check("the factor is (x - r)(quadratic), r = 3, and y^2 - D Eisenstein",
          r % 23 == 3 and (r ** 3 - r - 1) % mod == 0
          and vp(D, 23) == 1)


def section_staircase():
    section("S. THE CLOSED FORM HOLDS IFF e <= p - 1 AND NO HEAD")
    wrong = 0
    measured = {}
    for loc in PLACES + EXTRA:
        D = depth(loc)
        holds = all(loc.lam(b) == closed(loc, b) for b in range(1, D + 1))
        measured[loc.name] = holds
        want = loc.e <= loc.p - 1 and not criterion(loc)
        first = next((b for b in range(1, D + 1)
                      if loc.lam(b) != closed(loc, b)), None)
        tag = "holds" if holds else f"departs at b = {first}"
        print(f"  {loc.name:22s} p={loc.p} e={loc.e} f={loc.f} "
              f"head={'y' if criterion(loc) else 'n'}  to {D}: {tag}"
              f"{'' if holds == want else '  OFF'}")
        wrong += holds != want
    late = sum(1 for loc in PLACES + EXTRA
               if any(loc.lam(b) != closed(loc, b)
                      for b in range(1, depth(loc) + 1))
               and next(b for b in range(1, depth(loc) + 1)
                        if loc.lam(b) != closed(loc, b)) != loc.p + 1)
    check("a failing column departs first at b = p + 1", late == 0,
          f"{late} off")
    check("holds exactly where e <= p - 1 and no head", wrong == 0,
          f"{wrong} places on the wrong side of {len(PLACES + EXTRA)}")
    off = 0
    for loc in PLACES + EXTRA:
        if loc.name in QUAD3:
            d = QUAD3[loc.name]
            off += measured[loc.name] != (d % 9 != 6)
            print(f"    delta = {d:4d}, {d % 9} mod 9: "
                  f"{'head' if criterion(loc) else 'no head'}")
    check("at p = 3, e = 2: the column departs exactly at delta = 6 mod 9",
          off == 0)


def section_ring(pair):
    section("R. x^3 - x - 1: 23 = P Q^2, one norm, two columns")
    P, Q = pair
    colP = [P.lam(b) for b in range(1, RING_DEPTH + 1)]
    colQ = [Q.lam(b) for b in range(1, RING_DEPTH + 1)]
    print(f"  P (e=1): {colP[:4]} ...")
    print(f"  Q (e=2): {colQ[:4]} ...")
    check("columns 22, 506, 11638 and 22, 506, 506 at b = 1..3",
          colP[:3] == [22, 506, 11638] and colQ[:3] == [22, 506, 506])
    check("both equal the closed form to depth 12",
          all(colP[b - 1] == closed(P, b) and colQ[b - 1] == closed(Q, b)
              for b in range(1, RING_DEPTH + 1)))
    rep = [ell for ell in range(2, 2000)
           if all(ell % k for k in range(2, int(ell ** 0.5) + 1))
           and any((x ** 3 - x - 1) % ell == 0
                   and (3 * x * x - 1) % ell == 0 for x in range(ell))]
    print(f"  primes below 2000 with a repeated root: {rep}")
    check("23 is the only one", rep == [23])


def section_index():
    section("I. THE PRICE IS THE ADDITIVE INDEX; THE UNIT INDEX PARTS AT 0")
    seen = off = 0
    for loc in PLACES + EXTRA:
        N = loc.q
        if N ** 3 > LIMIT:
            continue
        counts = [1] + [sum(1 for _ in loc.reps(b, True)) for b in (1, 2, 3)]
        for b in (1, 2, 3):
            seen += 1
            off += counts[b] != (N - 1) * N ** (b - 1)
        for a in range(0, 3):
            for r in range(1, 4 - a):
                want = N ** r if a else (N - 1) * N ** (r - 1)
                seen += 1
                off += counts[a + r] != counts[a] * want
    print(f"  |(O/P^b)^x| = (N - 1) N^(b - 1); ratio N^r seated, "
          f"(N - 1) N^(r - 1) at 0: {seen} readings, {off} off (the "
          f"enumeration's own shape)")


def main():
    r, D, _ = hensel_23()
    pair = (Local(23, [0, 1], "unr", "P over 23"),
            Local(23, [-D, 0, 1], "eis", "Q over 23"))
    section_control(pair)
    if not all(CHECKS):
        print("  control failed: run stopped")
        raise SystemExit(1)
    section_staircase()
    section_ring(pair)
    section_index()
    print()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks PASS")
    if not all(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
