"""door.py -- the door identity: a number ring's place reads the state
through one p-adic valuation, so its block clock ticks in COUNTS, and
what that does to the chain inside a block.

QUESTION. dial.py proves the block clock: items share one notch per
block, a clock move lands one above it and moves it to the next member
of the MOVER's ladder, and inside a block the holders' degrees fall, so
a block clocked forever has one runaway. A number ring's places over one
rational prime share a notch because each reads the state through v_p(L)
alone. Is the ring's door the block clock's T + 1 - a in one unit, so
that the chain holds inside a ring's block? And the excess over a lone
door, which other places' residue fields set and nothing bounds: does it
break the chain, or only move the door by an amount the place cannot
see?

THE OBJECTS. A place P over p, residue field of N = p^f elements,
ramification e, width w (clock.py), carries its ladder (the orbit
from 1 of psi(i) = min(p i, i + e), save the step leaving the bend,
which overshoots by w) with members x_1 = 1 < x_2 < ...
(stop.py place_ladder). Its COLUMN at depth
b is c(b) = #{j : x_j < b}, so that lambda(P^b) = (N - 1) p^c(b), and
m(j) = x_j + 1 is the least depth whose column reaches j, m(0) = 1. A
state seats places at exponents a >= 1; L is the lcm of the seated
lambda's; the block over p is its places, and its COUNT is V =
v_p(L). A move on P raises its exponent from a (0 if unseated) by the
DOOR r, the least r >= 1 with lambda(P^(a + r)) not dividing L, at
price N^r.

THE ARGUMENT (written before the engine).
  (1) THE DOOR IDENTITY. The prime-to-p part of lambda(P^b) is N - 1 at
      every b >= 1, so if P is seated, or N - 1 already divides L, then
      lambda(P^(a + r)) divides L iff c(a + r) <= V. The door is
      m(V + 1) - a = T + 1 - a with T = x_(V+1), the notch read through
      P's own ladder; otherwise P is unseated, N - 1 does not divide L,
      and the door is 1. A clock move lands at m(V + 1), where the
      column is V + 1 exactly (U_b/U_(b+1) has exponent p, so the
      column rises at most one per depth), so V rises by ONE and, N - 1
      already dividing L, no other coordinate of L moves.
  (2) ONE UNIT IFF ONE LADDER. The ring's notch is a COUNT, the number of
      ticks the block has made, and each place translates it through its
      own ladder; dial.py's notch is a DEPTH, moved along the mover's
      ladder and read raw by every item. If every item of a block
      carries one ladder, the depth after the j-th tick is x_(j+1) in
      both, so the two engines are the same walk move for move. If a
      block carries two ladders they part: a count names a different
      depth on each.
  (3) THE CHAIN IN COUNTS. Let R move the notch from V_R - 1 to V_R and
      the block's next clock move be Y's, Y != R, at count V. Y's
      column count is at most V_R - 1, so its depth is at most
      x_(V_R) = m_Y(V_R) - 1 on its own ladder, and
          door_Y >= m_Y(V + 1) - m_Y(V_R) + 1;
      where Y last landed by a move (at m_Y of its count, 1 if only
      opened, 0 if unseated) it is at least m_Y(V + 1) - m_Y(V_R - 1),
      the bound the walks check, but a seed can sit deeper in its
      count [ruled on audit: the walks check the first, proved bound;
      the second holds by the same argument where Y landed by a move].
      R pends m_R(V + 1) - m_R(V_R). With one ladder, Y's door
      exceeds R's pending door at every V >= V_R, so the degree falls:
      dial.py's chain, and it survives any rise of V between the two
      moves. With two ladders Y can pend at or below R's door at equal
      or higher degree, and the chain in degrees fails.
  (4) THE TAIL. Past both bends every gap is the tail gap, so with V =
      V_R (nothing moved the count between) door_Y >= g_Y + 1 against
      R's g_R, and greed taking Y means kappa(d_Y, g_Y + 1) <= kappa(d_R, g_R);
      by strict monotonicity in the door the RECURRENT price kappa(d_Y, g_Y)
      is strictly below kappa(d_R, g_R). So at bounded gaps, past the last
      opening, every change of holder inside a block lowers the
      recurrent price, only finitely many can happen, and a block
      clocked forever keeps ONE runaway for any price strictly
      increasing in the door, whatever ladders it holds. In a ring the
      recurrent price is N^e = p^(ef), the local degree's power.
  (5) THE RESIDUE ROUTE. Only an opening moves another block's count:
      seating G over l adds N(G) - 1, and v_p(N(G) - 1) above V raises
      V at a stroke. That is a JUMP of the count, not of any door: every
      place of the block reads the new count through its own ladder. At
      bounded gaps the openings are finitely many, so the jumps end, and
      (3) and (4) hold through them. With the chain in counts, dial.py's
      bounded law (one recurrent price per clocked block) holds in a
      ring, and two blocks' recurrent prices p^(ef), q^(e'f') never tie:
      a number ring keeps ONE runaway place.

HAND-ATTACK.
  (a) Schedule family, one block, slot 0 on gap 3 (1, 4, 7, ...) and
      slot 1 on the exact ladder, price d r, lowest exponent first. The
      degree-1 items are born covered and tie at door 2; the lower slot,
      the wide one, lands at 2 and the count is 1. The wide item pends
      m(2) - 2 = 5 - 2 = 3, the narrow one enters at m(2) = 3: price 3
      each, degree 1 each; the tie rule takes the lower exponent, the
      narrow entry. So the block changes holder at EQUAL degree. In
      dial.py the notch went to 4 along the wide ladder, the narrow
      entry costs 5 and the wide item keeps the clock: the engines part.
  (b) Z[i]. Void: the ramified place over 2, (2, 2, 3), ladder 1, 2, 7,
      9, ..., has N - 1 = 1, so it enters at door 2 (price 4), then
      pays 1 (price 2), then faces 5 (price 32). The inert place over 3,
      N - 1 = 8, opens at 9 and lifts v_2(L) from 2 to 3: a jump, and
      the ramified place's door at depth 3 becomes m(4) - 3 = 7, price
      128.
  (c) The cubic ring of x^3 + 2x + 1 (discriminant -59, squarefree, so
      Z[alpha] is maximal and Dedekind's factorization holds at every
      p). Over 2 it has a place of degree 1, Z_2's ladder (2, 1, 1),
      and one of degree 2, ladder (2, 1, 0): two ladders in one block.
      Over 59 one unramified and one ramified place of degree 1: ladders
      (59, 1, 0) and (59, 2, 0). The ring x^3 - x - 1 (discriminant -23)
      has 2 inert and 23 split as P Q^2.

PREDICTIONS, frozen before the engine, each naming what the run PRINTS.
Schedule family: stop.py's 13 bounded ladders and dial.py's 2 climbing
ones, dial.py's five partitions and three prices, dial.py's supply (two
items a degree to 400), 240 moves (480 climbing), lowest exponent
first. Rings: Z[i], Z[sqrt(-5)], Z[sqrt(2)] and the two cubics, places
of norm up to 4000, walked 300 moves from the void with ties branched
over the first 8 moves, and from a seed belt (each of the six cheapest
places seated alone at exponent 1, 2 or 3), each seed walked lowest
exponent first and highest exponent first.
  PR1 THE DOOR IDENTITY. At every state a ring walk reaches, every place
      on the menu read: the door by lcm against the full integer L
      against the count form of (1). KILL: one mismatch. Also printed:
      clock moves that moved any coordinate of L but their own
      prime's, or moved their own by other than one. KILL: one.
      [Ruled on audit: given the formula, (1) makes the lcm door equal
      to the count form and moves L on its own coordinate by one, so
      both kills' counts are printed, a property of the model, not held.]
  PR2 ONE UNIT. The count walker against dial.run move for move (kind,
      degree, door, price, block, item). At every cell whose blocks each
      carry one ladder -- a common ladder under every partition, and a
      two-ladder supply under SLOT and ITEM -- KILL: one parting. At the
      two-ladder supplies under ONE, MOD2, MOD3, printed: cells parting.
      KILL: none part (the unit question would be empty).
  PR3 THE CHAIN IN COUNTS. At every change of holder inside a block, in
      the count walker and in the ring walks: the bound of (3) on Y's
      door. KILL: one violation. Changes whose two items carry one
      ladder and whose degree does not fall. KILL: one. Printed: changes
      not falling at two-ladder blocks, and cell (a)'s first change in
      block 0 with both doors. KILL: cell (a)'s first change is not
      (1, 0) -> (1, 1) at door 3 against 3.
  PR4 THE TAIL. Every change of holder with both items past their bends
      and no count move between: the new holder's recurrent price below
      the old one's. KILL: one not below. At bounded ladders and in every
      ring walk: a block with two items clocked in the last quarter.
      KILL: one. In a ring walk: two blocks clocked in the last quarter.
      KILL: one.
  PR5 THE JUMP, printed: per ring, openings that raised the count of a
      block already holding a seated place, and cell (b)'s first jump.
      Predicted present at Z[i].

CONTROLS, run first: the count walker on a common ladder under ONE
matches stop.py's global walk; the ring walker's lambda(P^b) matches a
brute exponent of (Z/p^b)^x at Z's places for b <= 12 [ruled on
audit: over 2, 3, 5, 7 to p^b <= 5000, so b <= 12 at 2 only] and the
Gaussian-integer column of Z[i] against brute (Z[i]/P^b)^x for the
ramified place and the inert place over 3 to norm 3^8; the chain
checker fires on a planted change rising in degree at one ladder; the
bound checker fires on a planted door below it.

FINDINGS (entered after the run, from its printed output).
  F0 CONTROLS. The count walker under ONE matches stop.py's global walk
     move for move at 7 ladders, 1680 moves; lambda(P^b) = (N - 1)
     p^c(b) matches the brute exponent at 28 (p, b) over Z, at Z[i]'s
     ramified place for b = 1..10 and at its inert place over 3 for b =
     1..4; both planted checkers fire.
  F1 THE DOOR IDENTITY (PR1 hit, as a property of the model). 201,456
     door readings over every expansion of the ring walks, 0 where the
     lcm door and the count form differ; 56,556 clock moves, 0 moving L
     off their own coordinate or by other than one. Given lambda(P^b)
     = (N - 1) p^c(b), (1) makes the two doors equal, so these print
     the engine's bookkeeping; the formula's ring content
     is F0's brute controls and clock.py's ladder theorem.
  F2 ONE UNIT (PR2 hit, both sides). 225 common-ladder cells and 252
     two-ladder cells under SLOT and ITEM: 0 parting. 378 two-ladder
     cells under ONE, MOD2 and MOD3: 52 parting. Cell (a) parts at move
     3: the count walker enters the narrow item at door 3, dial.py clocks the
     wide one at door 3. The one-ladder agreement is (2)'s construction,
     one walk by design: it guards the code, not (2).
  F3 THE CHAIN IN COUNTS (PR3 hit). 54 changes of holder inside a block,
     0 below the bound of (3); all 54 at two-ladder blocks and all 54
     not falling in degree; cell (a)'s first change is (1, 0) -> (1, 1)
     at door 3 against 3. On these unbranched walks no
     one-ladder cell changed holder at all, and there the engine is
     dial.py's move for move (F2).
  F4 THE TAIL (PR4 hit, its first clause VACUOUS). 0 tail changes in
     any walk, so argument (4)'s inequality stands on its proof alone.
     The reason is in (3): a holder that loses the clock is left a whole
     count behind and pays two of its gaps to return, so a tail change
     needs the old holder retaken on the new one's ramp, a gap the
     shared count closes within a few ticks. 0 bounded blocks with two
     items clocked in the last quarter; in the rings, 0 blocks with two
     items and 0 walks with two blocks clocked there.
  F5 THE JUMP (PR5 hit). Openings raising the count of a block holding
     a seated place: 7 at Z[i], 0, 2, 0 and 4 at Z[sqrt(-5)], Z[sqrt(2)]
     and the two cubics. Cell (b) is Z[i]'s first: the inert place over
     3 opens at move 3 and lifts v_2(L) from 2 to 3, moving the
     ramified place's door at depth 3 from 5 to 7.
  F6 THE RING'S BLOCKS (S3, added after the run, no prediction). The
     void and seed-belt walks made 0 changes of holder inside any ring
     block, H between 7 and 13. Seating two places over one prime at
     every pair of depths 1..4 among the 30 cheapest places: 1856
     walks, 252 of them clocking the seeded block, 0 clocking both
     seeded places, 0 changes of holder, 0 late blocks with two
     items: of two places seated over one
     prime, at most one is ever clocked, in every walk read.

RUN RECORD. One process, CPython, no numpy: 551306 checks, 81.8 s,
peak commit 13.4 MB under a memory guard.
"""

import os
import sys
import time
from collections import Counter
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import limit as L  # noqa: E402
import stop as SP  # noqa: E402
import dial as D  # noqa: E402

CHECKS = [0]


def check(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise SystemExit("FAIL: " + msg)


# ---------------------------------------------------------------------------
# a ladder read in counts

def member(lad, j):
    """x_j, the j-th member (x_1 = 1)."""
    while len(lad.m) < j:
        lad.m.append(lad.gen(lad.m[-1]))
    return lad.m[j - 1]


def mdepth(lad, j):
    """m(j): the least depth whose column reaches j; m(0) = 1."""
    return 1 if j == 0 else member(lad, j) + 1


def column(lad, b):
    """c(b) = #{j : x_j < b}."""
    j = 0
    while member(lad, j + 1) < b:
        j += 1
    return j


def tail_index(lad):
    """The least j with every gap x_(i+1) - x_i = the tail gap for i >= j,
    and the tail gap; None for a climbing ladder."""
    if not lad.bounded:
        return None, None
    g = SP.gaps(lad, 80)
    t = g[-1]
    j = len(g)
    while j > 0 and g[j - 1] == t:
        j -= 1
    return j + 1, t


# ---------------------------------------------------------------------------
# the schedule family with the notch kept as a count

def col_notch(C, st, it):
    """The depth the block's count names on this item's own ladder."""
    return member(C.ladder(*it), st.T.get(C.block(*it), 0) + 1)


def col_moves(C, st, sup):
    out = []
    for (d, s), (a, r0) in st.seat.items():
        r = col_notch(C, st, (d, s)) + 1 - a
        out.append((C.price(d, r, False), ("c", d, a, r0, s)))
    for d in sup:
        if out and C.price(d, 1, True) > min(out)[0]:
            break
        for s in range(sup[d]):
            if (d, s) in st.seat:
                continue
            if not L.covered(C.S, st, d):
                out.append((C.price(d, 1, True), ("o", d, 0, 1, s)))
            else:
                r = col_notch(C, st, (d, s)) + 1
                out.append((C.price(d, r, True), ("u", d, 0, r, s)))
    return out


def col_apply(C, st, t):
    kind, d, a, r0, s = t
    n = st.copy()
    it = (d, s)
    if kind == "o":
        n.seat[it] = (1, 1)
        n.opens[d] += 1
        n.nseat[d] += 1
        return n, 1, None, it
    b = C.block(d, s)
    T = col_notch(C, st, it)
    r = T + 1 - a
    if kind == "u":
        check(r == r0, "an unseated item's entry door")
        n.nseat[d] += 1
    n.seat[it] = (T + 1, r0 if kind == "c" else r)
    n.T[b] = st.T.get(b, 0) + 1
    n.last[b] = it
    return n, r, b, it


def col_run(C, sup, n, choose=D.canon_low):
    """(state, dial-format log, extended log). An extended entry is
    (block, item, degree, exponent before, count before, count after,
    door) for every clock move."""
    st, log, ext = D.St(), [], []
    for _ in range(n):
        ms = col_moves(C, st, sup)
        best = min(p for p, _ in ms)
        t = choose([t for p, t in ms if p == best])
        s2, r, b, it = col_apply(C, st, t)
        check(C.price(t[1], r, t[0] != "c") == best, "the menu's price")
        prev = st.last.get(b) if b is not None else None
        log.append((t[0], t[1], r, best, b, it, prev))
        if b is not None:
            v = st.T.get(b, 0)
            ext.append((b, it, t[1], t[2], v, v + 1, r))
        st = s2
    return st, log, ext


# ---------------------------------------------------------------------------
# the chain read in counts, shared by both engines. A clock-move record is
# (block, holder, degree, exponent before, count before, count after,
# door); lad(holder) is its ladder, rec(holder, door) its recurrent-price
# comparison key, price(holder, door) its price.

def chain_reading(ext, lad, price, same):
    """Counts over the changes of holder inside a block: (changes, bound
    violations, one-ladder changes not falling, two-ladder changes not
    falling, tail changes, tail changes not lowering the recurrent price,
    the first change of each block)."""
    last = {}
    out = Counter()
    first = {}
    for b, it, d, a, v0, v1, r in ext:
        if b in last and last[b][0] != it:
            z, dz, vz = last[b]
            out["changes"] += 1
            ly, lz = lad(it), lad(z)
            bound = mdepth(ly, v0 + 1) - mdepth(ly, vz) + 1
            out["bound_bad"] += r < bound
            pend = mdepth(lz, v0 + 1) - mdepth(lz, vz)
            first.setdefault(b, (z, it, r, pend))
            if not d < dz:
                out["same_rise" if same(it, z) else "two_rise"] += 1
            ky, gy = tail_index(ly)
            kz, gz = tail_index(lz)
            if (ky is not None and kz is not None and v0 == vz
                    and a >= mdepth(ly, ky) and vz >= ky and vz >= kz):
                out["tail"] += 1
                out["tail_bad"] += not price(it, gy) < price(z, gz)
        last[b] = (it, d, v1)
    return out, first


def late_blocks(log):
    """block -> set of holders over the clock moves of a ring walk's last
    quarter."""
    out = {}
    for kind, i, r, price, b in log[int(len(log) * 0.75):]:
        if b is not None:
            out.setdefault(b, set()).add(i)
    return out


# ---------------------------------------------------------------------------
# number rings: places, and a walk whose door is read by lcm

def primes_to(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


class Place:
    __slots__ = ("p", "f", "e", "w", "N", "lad", "idx", "name")

    def __init__(self, p, f, e, w):
        self.p, self.f, self.e, self.w = p, f, e, w
        self.N = p ** f
        self.lad = SP.place_ladder(p, e, w)

    def lam(self, b):
        return (self.N - 1) * self.p ** column(self.lad, b)


def unram(p, f):
    return Place(p, f, 1, 1 if (p == 2 and f == 1) else 0)


def legendre(a, p):
    return pow(a % p, (p - 1) // 2, p)


def quadratic(m, ram, nmax):
    """Q(sqrt m), ring of integers Z[sqrt m] (m = 2, 3 mod 4), ram: p ->
    (e, f, w) at the ramified primes."""
    out = []
    for p in primes_to(nmax):
        if p in ram:
            e, f, w = ram[p]
            out.append(Place(p, f, e, w))
        elif legendre(m, p) == 1:
            out += [unram(p, 1), unram(p, 1)]
        elif p * p <= nmax:
            out.append(unram(p, 2))
    return out


def cubic(a, b, ramp, nmax):
    """Q(alpha), alpha^3 + a alpha + b = 0, squarefree discriminant with the
    one prime ramp: ramp = P Q^2, both of degree 1."""
    out = []
    for p in primes_to(nmax):
        if p == ramp:
            out += [Place(p, 1, 1, 0), Place(p, 1, 2, 0)]
            continue
        roots = sum((x * x * x + a * x + b) % p == 0 for x in range(p))
        if roots == 3:
            out += [unram(p, 1), unram(p, 1), unram(p, 1)]
        elif roots == 1:
            out.append(unram(p, 1))
            if p * p <= nmax:
                out.append(unram(p, 2))
        elif p ** 3 <= nmax:
            out.append(unram(p, 3))
    return out


NMAX = 4000
RINGS = [
    ("Z[i]", lambda: quadratic(-1, {2: (2, 1, 3)}, NMAX)),
    ("Z[sqrt(-5)]", lambda: quadratic(-5, {2: (2, 1, 2), 5: (2, 1, 0)},
                                      NMAX)),
    ("Z[sqrt(2)]", lambda: quadratic(2, {2: (2, 1, 1)}, NMAX)),
    ("x^3+2x+1", lambda: cubic(2, 1, 59, NMAX)),
    ("x^3-x-1", lambda: cubic(-1, -1, 23, NMAX)),
]


def build(maker):
    pls = sorted(maker(), key=lambda q: (q.N, q.p, q.e))
    for i, q in enumerate(pls):
        q.idx = i
        q.name = f"{q.N}:{q.p},{q.e},{q.f}#{i}"
    return pls


def vp(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


class RSt:
    __slots__ = ("a", "L", "last")

    def __init__(self):
        self.a, self.L, self.last = {}, 1, {}

    def copy(self):
        s = RSt()
        s.a, s.L, s.last = dict(self.a), self.L, dict(self.last)
        return s

    def key(self):
        return tuple(sorted(self.a.items()))


def door_lcm(q, a, Lv):
    r = 1
    while Lv % q.lam(a + r) == 0:
        r += 1
    return r


def door_count(q, a, Lv):
    if a >= 1 or Lv % (q.N - 1) == 0:
        return mdepth(q.lad, vp(Lv, q.p) + 1) - a
    return 1


def rmenu(pls, st, tally):
    """(best price, [move types]); a type is (kind, place, exponent, door).
    Every door read is read both ways into tally."""
    ms = []

    def read(q, a):
        r = door_lcm(q, a, st.L)
        tally["read"] += 1
        tally["mismatch"] += r != door_count(q, a, st.L)
        return r

    for i, a in st.a.items():
        q = pls[i]
        r = read(q, a)
        ms.append((q.N ** r, ("c", i, a, r)))
    best = min(p for p, _ in ms) if ms else None
    for q in pls:
        if best is not None and q.N > best:
            break
        if q.idx in st.a:
            continue
        r = read(q, 0)
        pr = q.N ** r
        ms.append((pr, ("o" if r == 1 and st.L % (q.N - 1) else "u",
                        q.idx, 0, r)))
        if best is None or pr < best:
            best = pr
    check(best is not None and best < pls[-1].N, "the supply ran out")
    return best, [t for p, t in ms if p == best]


def r_low(types):
    return min(types, key=lambda t: (t[0] == "o", t[1], t[2]))


def r_high(types):
    return min(types, key=lambda t: (t[0] == "o", -t[2], t[1]))


def rstep(pls, st, t, price, log, ext, tally):
    kind, i, a, r = t
    q = pls[i]
    n = st.copy()
    n.a[i] = a + r
    n.L = st.L * q.lam(a + r) // gcd(st.L, q.lam(a + r))
    ratio = n.L // st.L
    if kind != "o":
        tally["clock"] += 1
        tally["coord_bad"] += ratio != q.p
        v = vp(st.L, q.p)
        ext.append((q.p, i, q.f, a, v, v + 1, r))
        n.last[q.p] = i
    else:
        seated = {pls[j].p for j in st.a}
        for ell in seated:
            if ell != q.p and ratio % ell == 0:
                tally["jump"] += 1
                if "jump_at" not in tally:
                    tally["jump_at"] = (q.name, ell, vp(st.L, ell),
                                        vp(n.L, ell), len(log) + 1)
    log.append((kind, i, r, price, None if kind == "o" else q.p))
    return n


def rwalk(pls, st, n, choose, log, ext, tally):
    for _ in range(n):
        best, types = rmenu(pls, st, tally)
        st = rstep(pls, st, choose(types), best, log, ext, tally)
    return st


def rbranches(pls, k, n, tally, cap=4000):
    front = {(): (RSt(), [], [])}
    for _ in range(k):
        nxt = {}
        for st, log, ext in front.values():
            best, types = rmenu(pls, st, tally)
            for t in types:
                lg, ex = list(log), list(ext)
                s2 = rstep(pls, st, t, best, lg, ex, tally)
                nxt.setdefault(s2.key(), (s2, lg, ex))
        front = nxt
        check(len(front) <= cap, "the branch cap")
    out = []
    for st, log, ext in front.values():
        st = rwalk(pls, st, n - k, r_low, log, ext, tally)
        out.append((st, log, ext))
    return out


def seeded(pls, q, a):
    st = RSt()
    st.a[q.idx] = a
    st.L = q.lam(a)
    return st


# ---------------------------------------------------------------------------
# brute unit exponents for the controls

def exponent_zmod(p, b):
    m = p ** b
    phi = m // p * (p - 1)
    units = [u for u in range(1, m) if u % p]
    for n in sorted(k for k in range(1, phi + 1) if phi % k == 0):
        if all(pow(u, n, m) == 1 for u in units):
            return n


def gmul(x, y, m):
    return ((x[0] * y[0] - x[1] * y[1]) % m, (x[0] * y[1] + x[1] * y[0]) % m)


def gpow(x, n, m):
    r = (1 % m, 0)
    while n:
        if n & 1:
            r = gmul(r, x, m)
        x = gmul(x, x, m)
        n >>= 1
    return r


def exponent_gauss_ram(b):
    """Exponent of (Z[i]/(1+i)^b)^x, a 2-group: the least 2^j taking every
    unit to 1 mod (1+i)^b, read by the norm's 2-adic valuation."""
    k = (b + 1) // 2
    m = 2 ** k
    units = [(x, y) for x in range(m) for y in range(m) if (x + y) % 2]

    def v(z):
        x, y = (z[0] - 1) % m, z[1] % m
        if x == 0 and y == 0:
            return 2 * k
        return vp(x * x + y * y, 2)
    n = 1
    while not all(v(gpow(u, n, m)) >= b for u in units):
        n *= 2
    return n


def exponent_gauss_inert3(b):
    m = 3 ** b
    order = 9 ** (b - 1) * 8
    units = [(x, y) for x in range(m) for y in range(m)
             if (x % 3, y % 3) != (0, 0)]
    for n in sorted(k for k in range(1, order + 1) if order % k == 0):
        if all(gpow(u, n, m) == (1, 0) for u in units):
            return n


# ---------------------------------------------------------------------------
# the sections

SUP = D.SUP
N_S, N_C = 240, 480
N_R, K_R = 300, 8
N_P = 150


def section_control():
    print("S0  CONTROLS")
    moves_read = 0
    for lad in L.LADDERS:
        S = L.Sched(lad.name, lad, L.price_power(1))
        _, ref = SP.run(S, SUP, True, N_S)
        C = D.Cell(lad.name, L.price_power(1), D.PARTS["ONE"],
                   D.common(lad))
        _, mine, _ = col_run(C, SUP, N_S)
        check([(t[0], t[1], r, p) for t, r, p, *_ in ref]
              == [x[:4] for x in mine],
              f"the count walker parts from stop.py at {lad.name}")
        moves_read += len(ref)
    print(f"  the count walker under ONE matches stop.py's global walk "
          f"move for move at {len(L.LADDERS)} ladders, {moves_read} moves")
    nz = 0
    for p in (2, 3, 5, 7):
        b = 1
        while p ** b <= 5000:
            check(exponent_zmod(p, b) == unram(p, 1).lam(b),
                  f"lambda at Z's place over {p}, depth {b}")
            nz += 1
            b += 1
    ram, ine = Place(2, 1, 2, 3), Place(3, 2, 1, 0)
    for b in range(1, 11):
        check(exponent_gauss_ram(b) == ram.lam(b),
              f"lambda at Z[i]'s ramified place, depth {b}")
    for b in range(1, 5):
        check(exponent_gauss_inert3(b) == ine.lam(b),
              f"lambda at Z[i]'s inert place over 3, depth {b}")
    print(f"  lambda(P^b) = (N - 1) p^c(b) against brute exponents: {nz} "
          f"(p, b) over Z, Z[i]'s ramified place at b = 1..10 and its "
          f"inert place over 3 at b = 1..4")
    g1 = L.ladder_gap(1)
    planted = [(0, (1, 0), 1, 0, 0, 1, 2), (0, (2, 0), 2, 1, 1, 2, 3)]
    out, _ = chain_reading(planted, lambda it: g1,
                           lambda it, g: it[0] * g, lambda x, y: True)
    check(out["same_rise"] == 1, "the chain checker did not fire")
    planted = [(0, (1, 0), 1, 0, 0, 1, 2), (0, (1, 1), 1, 0, 1, 2, 1)]
    out, _ = chain_reading(planted, lambda it: g1,
                           lambda it, g: it[0] * g, lambda x, y: True)
    check(out["bound_bad"] == 1, "the bound checker did not fire")
    print("  the chain checker fires on a planted rise at one ladder; the "
          "bound checker on a planted door below the bound")


def schedule_cell(C, n, tot, bounded=True):
    """Run both engines at one cell: (parted, first changes, count log,
    dial log)."""
    _, dlog = D.run(C, SUP, n)
    st, clog, ext = col_run(C, SUP, n)
    parted = [x[:6] for x in dlog] != [x[:6] for x in clog]
    out, first = chain_reading(
        ext, lambda it: C.ladder(*it),
        lambda it, g: C.price(it[0], g, False),
        lambda x, y: C.ladder(*x) is C.ladder(*y))
    tot.update(out)
    if bounded:
        lt = D.late(clog, 0.25)
        tot["late_two"] += sum(len(v) > 1 for v in lt.values())
    return parted, first, clog, dlog


def section_unit():
    print("S1  ONE UNIT, AND THE CHAIN IN COUNTS (schedule family)")
    tot = Counter()
    pure = pure_parted = 0
    for lad in SP.ladders() + D.climbing_ladders():
        n = N_S if lad.bounded else N_C
        for part in D.PARTS:
            for pname, price in D.PRICES:
                C = D.Cell(lad.name, price, D.PARTS[part], D.common(lad))
                parted, *_ = schedule_cell(C, n, tot, lad.bounded)
                pure += 1
                pure_parted += parted
    b = {x.name: x for x in SP.ladders()}
    mix = [b["exact"], b["gap 2"], b["gap 3"], b["(2,1,1)"], b["(2,2,3)"],
           b["(2,4,2)"], b["(5,4,1)"]]
    mixed = mixed_parted = split = split_parted = 0
    for l0 in mix:
        for l1 in mix:
            if l0 is l1:
                continue
            for part in D.PARTS:
                for pname, price in D.PRICES:
                    C = D.Cell(f"{l0.name}|{l1.name}", price, D.PARTS[part],
                               D.by_slot(l0, l1))
                    parted, *_ = schedule_cell(C, N_S, tot)
                    if part in ("SLOT", "ITEM"):
                        split += 1
                        split_parted += parted
                    else:
                        mixed += 1
                        mixed_parted += parted
    print(f"  one ladder a block: {pure} common-ladder cells, "
          f"{pure_parted} parting; {split} two-ladder cells under SLOT and "
          f"ITEM, {split_parted} parting")
    print(f"  two ladders a block: {mixed} cells under ONE, MOD2, MOD3, "
          f"{mixed_parted} parting")
    print(f"  changes of holder {tot['changes']}: bound violations "
          f"{tot['bound_bad']}; one-ladder changes not falling "
          f"{tot['same_rise']}; two-ladder changes not falling "
          f"{tot['two_rise']}")
    print(f"  tail changes {tot['tail']}, not lowering the recurrent price "
          f"{tot['tail_bad']}; bounded blocks with two items clocked in the "
          f"last quarter {tot['late_two']}")
    C = D.Cell("gap 3|exact", L.price_power(1), D.PARTS["ONE"],
               D.by_slot(b["gap 3"], b["exact"]))
    parted, first, clog, dlog = schedule_cell(C, N_S, Counter())
    z, y, r, pend = first[0]
    at = next(i for i, (u, v) in enumerate(zip(clog, dlog))
              if u[:6] != v[:6])
    print(f"  cell (a), gap 3 | exact, ONE, d r: first change {z} -> {y} "
          f"at door {r} against {pend}; the engines part at move {at + 1}: "
          f"count {clog[at][:4]}, dial {dlog[at][:4]}")
    check(pure_parted == 0 and split_parted == 0,
          "PR2: a one-ladder cell parts")
    check(mixed_parted > 0, "PR2: no two-ladder cell parts")
    check(tot["bound_bad"] == 0, "PR3: the bound")
    check(tot["same_rise"] == 0, "PR3: a one-ladder change not falling")
    check((z, y, r, pend) == ((1, 0), (1, 1), 3, 3), "PR3: cell (a)")
    check(tot["tail_bad"] == 0, "PR4: a tail change")
    check(tot["late_two"] == 0, "PR4: two items late in a bounded block")


def section_rings():
    print("S2  THE RINGS")
    for name, maker in RINGS:
        pls = build(maker)
        tally = Counter()
        walks = rbranches(pls, K_R, N_R, tally)
        nb = len(walks)
        for q in pls[:6]:
            for a in (1, 2, 3):
                for choose in (r_low, r_high):
                    log, ext = [], []
                    st = rwalk(pls, seeded(pls, q, a), N_R, choose, log, ext,
                               tally)
                    walks.append((st, log, ext))
        tot = Counter()
        H = 0
        late_two = late_multi = 0
        runaways = Counter()
        for st, log, ext in walks:
            out, _ = chain_reading(
                ext, lambda i: pls[i].lad, lambda i, g: pls[i].N ** g,
                lambda i, j: ((pls[i].p, pls[i].e, pls[i].w)
                              == (pls[j].p, pls[j].e, pls[j].w)))
            tot.update(out)
            H = max(H, max(x[3] for x in log))
            lb = late_blocks(log)
            late_two += sum(len(v) > 1 for v in lb.values())
            late_multi += len(lb) > 1
            for v in lb.values():
                for i in v:
                    runaways[pls[i].name] += 1
        check(H < NMAX, "the supply's norm bound")
        mixed = sorted({q.p for q in pls for r in pls if q.p == r.p
                        and (q.e, q.w) != (r.e, r.w)})
        print(f"  {name}: {nb} void branches + {len(walks) - nb} seeded "
              f"walks, H {H}; blocks holding two ladders {mixed}")
        print(f"    doors read {tally['read']}, lcm against count "
              f"mismatches {tally['mismatch']}; clock moves "
              f"{tally['clock']}, moving L off their own coordinate or by "
              f"other than one {tally['coord_bad']}")
        print(f"    changes {tot['changes']}: bound violations "
              f"{tot['bound_bad']}, one-ladder not falling "
              f"{tot['same_rise']}, two-ladder not falling "
              f"{tot['two_rise']}; tail changes {tot['tail']}, not lowering "
              f"{tot['tail_bad']}")
        print(f"    late quarter: blocks with two items {late_two}, walks "
              f"with two blocks {late_multi}; runaways {dict(runaways)}")
        print(f"    jumps {tally['jump']}; first {tally.get('jump_at')}")
        if name == "Z[i]":
            ram = next(q for q in pls if q.p == 2)
            print("    the ramified place's door at depth 3 at v_2(L) = 2, 3: "
                  f"{door_count(ram, 3, 4)}, {door_count(ram, 3, 8)}")
            check(tally["jump"] > 0, "PR5: no jump at Z[i]")
        check(tot["bound_bad"] == 0, "PR3: the bound in a ring")
        check(tot["same_rise"] == 0, "PR3: a one-ladder change in a ring")
        check(tot["tail_bad"] == 0, "PR4: a tail change in a ring")
        check(late_two == 0, "PR4: two items late in a ring's block")
        check(late_multi == 0, "PR4: two blocks late in a ring")


def section_pairs():
    """Added after the run, no prediction: two places over one prime
    seated together, the population that tests a ring's block."""
    print("S3  TWO PLACES IN ONE BLOCK (added after the run)")
    for name, maker in RINGS:
        pls = build(maker)
        tally, tot = Counter(), Counter()
        walks = late_two = 0
        head = pls[:30]
        for i, q in enumerate(head):
            for r in head[i + 1:]:
                if r.p != q.p:
                    continue
                for a1 in range(1, 5):
                    for a2 in range(1, 5):
                        for choose in (r_low, r_high):
                            st = RSt()
                            st.a = {q.idx: a1, r.idx: a2}
                            st.L = (q.lam(a1) * r.lam(a2)
                                    // gcd(q.lam(a1), r.lam(a2)))
                            log, ext = [], []
                            rwalk(pls, st, N_P, choose, log, ext, tally)
                            out, _ = chain_reading(
                                ext, lambda k: pls[k].lad,
                                lambda k, g: pls[k].N ** g,
                                lambda k, j: (
                                    (pls[k].p, pls[k].e, pls[k].w)
                                    == (pls[j].p, pls[j].e, pls[j].w)))
                            tot.update(out)
                            walks += 1
                            held = {k for b, k, *_ in ext if b == q.p}
                            tot["clocked"] += bool(held)
                            tot["both"] += {q.idx, r.idx} <= held
                            late_two += sum(len(v) > 1 for v in
                                            late_blocks(log).values())
        print(f"  {name}: {walks} walks, {tot['clocked']} clocking the "
              f"seeded block, {tot['both']} clocking both seeded places; "
              f"doors read {tally['read']}, mismatches {tally['mismatch']}; "
              f"changes of holder {tot['changes']}; late blocks with two "
              f"items {late_two}")


def main():
    t0 = time.time()
    section_control()
    section_unit()
    section_rings()
    section_pairs()
    print(f"\n{CHECKS[0]} checks, {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
