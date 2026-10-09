"""stop.py -- where a bounded ladder stops a greedy walk, and whether the
two numbers a place hands a walk, the sup and the tail, decide it.

QUESTION. limit.py proves that a walk on a ladder with bounded gaps stops
widening its support when only finitely many openings are cheap, and
one with unbounded gaps, at a price unbounded in the door, does not. It
does not say WHERE the support stops. Read before at the corner price with the
clock-first tie-break, the horizon sat at the runaway's degree times the
ladder's largest gap, on every ladder read, headed or not, under one notch
for every item and under one notch per item. clock.py proves what a
place's ladder is: the orbit of psi(i) = min(p i, i + e) from 1 with one
overshoot w at the bend, so its gaps are the ramp's, each below e, then
e + w once, then e forever; the SUP is e + w and the TAIL is e. Does the
stop location follow from those two numbers by argument, over every
branch of the walk and under both kinds of clock?

THE SCHEDULE is limit.py's, imported: items of positive degree d, a
supply of finitely many per degree, a ladder S of members x_1 = 1, x_2,
... in order, with next_S(a) its least member at or above a, a born set,
nu openings covering a degree, a price kappa(d, r) in the degree and the
door. An OPENING has door 1 and lands at 1. Under the GLOBAL clock,
limit.py's, a clock move on an item at exponent a has door T + 1 - a,
lands at T + 1 and moves the one notch T to next_S(T + 1). Under a
PER-ITEM clock every item carries its own notch, which is next_S of its
own exponent (every landing is one past a member, so the notch an item
last set is next_S of where it stands): a clock move on an item at
exponent a has door next_S(a) + 1 - a and lands at next_S(a) + 1, and an
unseated item of a covered degree pays door next_S(0) + 1 = 2. The
HORIZON is the least supplied degree left uncovered. The HIGH-WATER
PRICE H of a walk is the largest price it pays. An item's ENTRY DOOR r0
is the door of its first move.

THE ARGUMENT (written before the engine).
  (1) THE HIGH-WATER LEMMA. Any clock, any price, the default covering.
      At the step that pays H every move the state offers costs at least
      H, so every degree with kappa(d, 1) < H has no opening left: it is
      covered or its supply is all seated. No move above H is ever
      paid. So the openings made are every one priced below H, some
      priced at H and none above: the horizon's opening is priced at
      least H. At the corner, every degree supplied and the born set
      {1}, the horizon is H or H + 1, H exactly when degree H is never
      opened, and never below 2.
      The stop location is therefore the high-water price, whatever
      sets it.
  (2) THE PATH OF A CLOCKED ITEM. An item entering by an opening pays
      door 1, lands at 1 = next_S(1), then pays door 1 again and lands
      at 2. Entering through a covered degree at notch 1 it pays door 2
      and lands at 2. From x_j + 1, one past a member x_j, a re-clock
      with no other clock move between pays
      next_S(x_j + 1) + 1 - (x_j + 1) = x_(j+1) - x_j, x_(j+1) the member
      after x_j, and lands at x_(j+1) + 1. So a clocked item pays
      its entry door, a second door 1 if it opened, and then the
      ladder's consecutive gaps in order:
      under a per-item clock always, under the global clock exactly
      while no other item holds a clock move. By clock.py the largest of
      those gaps at a place is the sup and the eventual one the tail.
  (3) PER-ITEM: H IS THE RUNAWAY'S LARGEST PRICE. Let X be clocked
      infinitely often. Its doors read no other item, so the price of
      its pending move is at every step at most one it pays later: before its
      entry kappa(d_X, 1) while its degree is uncovered and kappa(d_X, 2) once
      it is covered, which never reverts, so the pending price only
      rises to the entry actually paid; after its entry, the next gap
      on its path. Greed never pays above any move the state offers, so
      H <= H_X, the largest price X pays, and H >= H_X. With kappa
      increasing in the door, H = kappa(d_X, max(r0, sup)), and r0 = 2
      exceeds the sup only on the exact ladder, sup 1, entered through a
      covered degree:
      a floor at gap 1. Every item clocked infinitely often has the same
      kappa(d, max(r0, sup)). After the bend every re-clock costs kappa(d_X,
      tail): the sup is a barrier paid once, the tail the recurrent
      price. If kappa(d, 1) tends to infinity in d and the gaps are bounded, a
      seated item at depth >= 1 bids at most kappa(d, max(2, sup)) forever,
      so finitely many items are ever moved, the walk clocks forever
      (limit.py) on finitely many items, and one of them is clocked
      infinitely often: the walk stops, at the horizon (1) reads off
      H = kappa(d_X, max(r0, sup)). If the gaps are unbounded, kappa is
      unbounded in the door and kappa(d, 1) tends to infinity, the prices
      paid are unbounded either way and every opening is made.
  (4) GLOBAL: THE SUP IS A FLOOR THAT THE CHAIN CAN RAISE. The notch
      walks S member by member, one clock move per member, and every
      exponent is at most x_j + 1 while the notch stands at the member
      x_(j+1), so the move leaving x_(j+1) has door at least
      x_(j+1) - x_j. Its
      holder's degree is at least the runaway's, by limit.py's chain.
      So every gap is paid at a price of at least kappa(d_X, gap), and H >=
      kappa(d_X, sup). On a branch where the runaway is the only holder, (2)
      and (3) give H = kappa(d_X, max(r0, sup)) exactly. On a branch with a
      strand the new holder enters at door T + 1, or T from exponent 1,
      which no gap bounds. HAND-RUN at the corner, two items per degree,
      S = 1, 1 + c, 1 + 2c, ..., c >= 2. The void menu ties kappa(1, 2) = 2
      = kappa(2, 1). Open degree 2 first; its clock at notch 1 (door 1, price
      2) ties the rational unseated item's (door 2, price 2); take the
      degree-2 item. It lands at 2 and the notch goes to 1 + c. Now it
      bids 2c and a rational unseated item bids c + 2 <= 2c; the
      openings of degrees 3 to c + 1 are cheaper and made first, then
      the rational item takes the clock at c + 2 (a tie at c = 2,
      broken to the lower degree), lands at c + 2 with the notch at
      1 + 2c, and re-clocks at door c forever. Runaway degree 1, sup c,
      one strand, and H = c + 2: the horizon on the clock-first
      continuation is c + 2, not c. So the old reading is the per-item
      clock's theorem and the single-holder branches' under the global
      clock, and a floor on the others, raised by the chain's
      transient.

PREDICTIONS, frozen before the engine, each naming what the run PRINTS.
Ladders: the constant ladders of gap 1, 2, 3, 5; nine place ladders
built from (p, e, w) by clock.py's theorem, headed (2, 1, 1), (2, 2, 1),
(2, 2, 2), (2, 2, 3), (3, 2, 1), (2, 4, 2), (5, 4, 1), (2, 8, 4) and
headless (2, 3, 0); the doubling and square ladders for the fate.
Prices: d r (the corner), d^2 r, d + r. Two items per degree to 400,
born {1}, nu = 1. Every tie branched over the first moves [ruled: 9], each
branch then walked clock-first.
  PR1 THE HIGH-WATER LEMMA. Printed per cell: walks read, and the count
     where a non-born supplied degree with kappa(d, 1) < H is uncovered with
     an item unseated, or a degree with kappa(d, 1) > H was opened, or the
     horizon's opening is priced below H. KILL: one.
  PR2 THE PATH. Printed per ladder: the per-item runaway's first twelve doors
     [ruled: the run reads the first clocked item, F1] on the canonical branch
     against its entry door and the ladder's consecutive gaps. KILL: one
     mismatch.
  PR3 PER-ITEM. Printed per cell: branches, and those where H differs
     from kappa(d, max(r0, sup)) for an item clocked in the last quarter, or
     where such an item's last-quarter doors are not all the tail.
     KILL: one.
  PR4 GLOBAL. Printed per cell: branches, those with a holder change,
     those with H below kappa(d_X, sup), and those with no holder change
     and H differing from kappa(d_X, max(r0, sup)). KILL: either of the last
     two nonzero.
  PR5 THE EXCESS. Printed at the corner on the gap-2, 3, 5 ladders, the
     branch opening degree 2 and clocking it: H, the runaway's degree,
     the strands [ruled: a strand is a holder left behind at a change], the
     horizon. KILL: H = c at any of the three, which
     would put the old reading on that branch and the hand-run wrong.
     Printed without a prediction: per global cell, how many branches
     carry H above kappa(d_X, sup).
  PR6 THE FATE UNDER A PER-ITEM CLOCK. Printed per ladder at the corner:
     openings in the last half of the canonical walk. KILL: one at a
     bounded ladder, or none at the doubling or square ladder.

CONTROLS, run first: this engine's global walk reproduces limit.py's
canonical log move for move on limit.py's own ladders; the lemma
checker fires on a planted walk that pays a dearer move over a cheaper
opening; the path checker fires on a ladder with a gap planted into it.
[Ruled on audit: the lemma checker's plant is a walk's final state with
an opening planted above H and one below it removed, as F0 says.]

FINDINGS (entered after the run, from its printed output).
  F0 CONTROLS. The global walk matches limit.py's clock-first log at
     its 7 ladders, 1680 moves; the lemma checker fires on a planted
     opening above H and a planted skipped one below it; the path
     checker fires on the (2,2,3) walk read against the (2,2,2) gaps.
  F1 THE PATH (PR2 hit). At all 13 ladders the first clocked item, a
     rational one entering through the born degree at door 2, pays 2
     and then the consecutive gaps: (2,2,3) reads 2, 1, 5, 2, 2, ...;
     (2,8,4) reads 2, 1, 2, 4, 12, 8, 8, ...; the exact ladder 2, 1,
     1, ..., the one row where the entry door exceeds the sup.
  F2 THE LEMMA AND THE PER-ITEM CLOCK (PR1, PR3 hit). 149 per-item and
     117 global branches over 13 ladders and three prices: 0 lemma
     faults; at every per-item branch every item clocked in the last
     quarter has H = kappa(d, max(r0, sup)) and pays only the tail there.
  F3 THE GLOBAL CLOCK (PR4 hit, PR5 hit). 0 branches below kappa(d_X, sup), 0
     single-holder branches off kappa(d_X, max(r0, sup)). 20 branches carry a
     holder change, all at the corner price, and all 20 sit ABOVE the floor;
     the 5 other branches above it change no holder and enter above the sup,
     the exact ladder's. At d^2 r and d + r no branch changed holder: d^2 r has
     no void tie, and at d + r the degree-2 holder bids 2 + c against the
     rational item's c + 3 and keeps the clock (read after the run, not
     predicted). The forced branch reads H 4, 5, 7 at gaps 2, 3, 5, runaway
     degree 1, one strand, horizon c + 2, as the hand-run said.
  F4 THE FATE (PR6 hit). No opening in the last half at the 13
     bounded ladders under a per-item clock; 20 and 19 at the doubling
     and square ladders.

RUN RECORD. One process, CPython, no numpy: 76309 checks, 0.4 s, peak
commit 10.1 MB under a memory guard.
"""

import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import limit as L  # noqa: E402

CHECKS = [0]


def check(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise SystemExit("FAIL: " + msg)


# ---------------------------------------------------------------------------
# ladders

def place_ladder(p, e, w):
    """The orbit of psi(i) = min(p i, i + e) from 1, the step leaving the
    bend e/(p - 1) overshooting by w when the bend is a power of p."""
    bend = e // (p - 1) if e % (p - 1) == 0 else None
    if w:
        q = 1
        while bend is not None and q < bend:
            q *= p
        check(bend is not None and q == bend, f"a width off a p-power bend "
              f"at ({p}, {e})")

    def gen(t):
        return t + e + w if t == bend else min(p * t, t + e)
    return L.Ladder(f"({p},{e},{w})", gen, True)


def gaps(lad, n):
    while len(lad.m) < n + 1:
        lad.m.append(lad.gen(lad.m[-1]))
    return [b - a for a, b in zip(lad.m, lad.m[1:n + 1])]


def sup_tail(lad):
    g = gaps(lad, 60)
    return max(g), g[-1]


def ladders():
    out = [L.ladder_gap(c) for c in (1, 2, 3, 5)]
    for p, e, w in ((2, 1, 1), (2, 2, 1), (2, 2, 2), (2, 2, 3), (3, 2, 1),
                    (2, 4, 2), (5, 4, 1), (2, 8, 4), (2, 3, 0)):
        out.append(place_ladder(p, e, w))
    return out


# ---------------------------------------------------------------------------
# the walker. A seated item is keyed (degree, exponent, entry door); a move
# TYPE is (kind, degree, exponent, entry door), kind c (clock a seated
# item), u (clock an unseated item of a covered degree) or o (open).

class St:
    __slots__ = ("T", "seat", "opens", "nseat")

    def __init__(self):
        self.T, self.seat = 1, Counter()
        self.opens, self.nseat = Counter(), Counter()

    def copy(self):
        s = St()
        s.T, s.seat = self.T, Counter(self.seat)
        s.opens, s.nseat = Counter(self.opens), Counter(self.nseat)
        return s

    def key(self):
        return (self.T, tuple(sorted(self.seat.items())),
                tuple(sorted(self.opens.items())))


def clock_door(S, st, a, glob):
    """(door, landing) of a clock move on an item at exponent a."""
    if glob:
        return st.T + 1 - a, st.T + 1
    t = S.ladder.next(max(a, 1))
    return t + 1 - a, t + 1


def menu(S, st, sup, glob):
    best, types = None, []
    for (d, a, r0), n in st.seat.items():
        k = S.price(d, clock_door(S, st, a, glob)[0], False)
        if best is None or k < best:
            best, types = k, [(("c", d, a, r0), n)]
        elif k == best:
            types.append((("c", d, a, r0), n))
    for d in sup:
        if best is not None and S.price(d, 1, True) > best:
            break
        u = sup[d] - st.nseat[d]
        if u <= 0:
            continue
        if not L.covered(S, st, d):
            t, k = ("o", d, 0, 1), S.price(d, 1, True)
        else:
            r = clock_door(S, st, 0, glob)[0]
            t, k = ("u", d, 0, r), S.price(d, r, True)
        if best is None or k < best:
            best, types = k, [(t, u)]
        elif k == best:
            types.append((t, u))
    return best, types


def apply(S, st, t, glob):
    """(state after, door paid, the moved item's key after)."""
    kind, d, a, r0 = t
    s = st.copy()
    if kind == "o":
        s.seat[(d, 1, 1)] += 1
        s.opens[d] += 1
        s.nseat[d] += 1
        return s, 1, (d, 1, 1)
    r, land = clock_door(S, st, a, glob)
    if kind == "c":
        s.seat[(d, a, r0)] -= 1
        if not s.seat[(d, a, r0)]:
            del s.seat[(d, a, r0)]
    else:
        check(r == r0, "an unseated item's entry door")
        s.nseat[d] += 1
    s.seat[(d, land, r0)] += 1
    if glob:
        s.T = S.ladder.next(st.T + 1)
    return s, r, (d, land, r0)


def canon(types):
    """limit.py's tie-break: a clock before an opening, low degree and low
    exponent first."""
    return min(types, key=lambda tm: (tm[0][0] == "o", tm[0][1],
                                      tm[0][2], tm[0][3]))[0]


def top(st):
    return max(st.seat, key=lambda k: k[1]) if st.seat else None


def step(S, st, t, glob, price, log):
    """Apply t and log (type, door, price, key after, holder changed). A
    change of holder is read as limit.py reads it: the previous holder
    stands alone at the top exponent, one above every other."""
    tp = top(st)
    s, r, landed = apply(S, st, t, glob)
    chg = False
    if t[0] != "o" and glob:
        chg = (tp is not None and tp[1] >= 2
               and (t[0] == "u" or t[2] < tp[1]))
        if chg:
            check(t[1] < tp[0], "the chain: a change of holder not falling")
    check(S.price(t[1], r, t[0] != "c") == price, "the menu's price")
    log.append((t, r, price, landed, chg))
    return s, log


def run(S, sup, glob, n, st=None, log=None, first=()):
    """Walk n moves clock-first; `first` forces the opening moves."""
    st = st if st is not None else St()
    log = [] if log is None else log
    forced = list(first)
    for _ in range(n):
        best, types = menu(S, st, sup, glob)
        if forced:
            t = forced.pop(0)
            check(any(tt == t for tt, _ in types),
                  f"a forced move {t} is not least")
        else:
            t = canon(types)
        st, log = step(S, st, t, glob, best, log)
    return st, log


def branches(S, sup, glob, k, n, cap=6000):
    """Every distinct state any tie choice reaches in k moves, each then
    walked clock-first for n more."""
    front = {St().key(): (St(), [])}
    for _ in range(k):
        nxt = {}
        for st, log in front.values():
            best, types = menu(S, st, sup, glob)
            for t, _m in types:
                s2, lg = step(S, st, t, glob, best, list(log))
                nxt.setdefault(s2.key(), (s2, lg))
        front = nxt
        check(len(front) <= cap, "the branch cap")
    return [run(S, sup, glob, n, st, list(log)) for st, log in front.values()]


def follow(log, start):
    """The doors paid by one item, followed from its move at index start
    through its key."""
    cur = log[start][3]
    doors = [log[start][1]]
    for t, r, _, landed, _ in log[start + 1:]:
        if t[0] == "c" and (t[1], t[2], t[3]) == cur:
            doors.append(r)
            cur = landed
    return doors


def horizon(S, st, sup):
    return min(d for d in sup if sup[d] and not L.covered(S, st, d))


def lemma_faults(S, st, sup, H):
    """The high-water lemma's clauses, counted: a degree priced below H
    left with an opening, one priced above H opened, the horizon priced
    below H."""
    bad = 0
    for d in sup:
        if not sup[d] or d in S.born:
            continue
        p1 = S.price(d, 1, True)
        if p1 < H and not L.covered(S, st, d) and st.nseat[d] < sup[d]:
            bad += 1
        if p1 > H and st.opens[d]:
            bad += 1
    if S.price(horizon(S, st, sup), 1, True) < H:
        bad += 1
    return bad


def late(log):
    """Every (degree, entry door) clocked in the last quarter, with the
    doors paid there."""
    out = {}
    for t, r, _, landed, _ in log[3 * len(log) // 4:]:
        if t[0] != "o":
            out.setdefault((landed[0], landed[2]), []).append(r)
    return out


PRICES = [("d r", L.price_power(1)), ("d^2 r", L.price_power(2)),
          ("d + r", L.price_additive)]
SUP = L.wide(2, 400)
K, N = 9, 240


# ---------------------------------------------------------------------------
# the sections

def section_control():
    print("S0  CONTROLS")
    moves = 0
    for lad in L.LADDERS:
        S = L.Sched(lad.name, lad, L.price_power(1))
        _, ref = L.walk(S, SUP, N)
        _, mine = run(S, SUP, True, N)
        check([x[:3] for x in ref] == [(t[0], t[1], r) for t, r, *_ in mine],
              f"the global engine parts from limit.py at {lad.name}")
        moves += len(ref)
    print(f"  the global walk matches limit.py's clock-first log move for "
          f"move at {len(L.LADDERS)} ladders, {moves} moves")
    S = L.Sched("gap 3", L.ladder_gap(3), L.price_power(1))
    st, log = run(S, SUP, True, N)
    H = max(x[2] for x in log)
    check(lemma_faults(S, st, SUP, H) == 0, "the lemma on a clean walk")
    bad = st.copy()
    bad.opens[H + 1] += 1
    bad.nseat[H + 1] += 1
    f1 = lemma_faults(S, bad, SUP, H)
    bad = st.copy()
    d0 = next(d for d in range(2, H) if st.opens[d])
    bad.opens[d0] -= 1
    bad.nseat[d0] -= 1
    f2 = lemma_faults(S, bad, SUP, H)
    check(f1 > 0 and f2 > 0, "the lemma checker did not fire")
    print(f"  the lemma checker fires on a planted opening above H ({f1}) "
          f"and on a planted skipped one below it ({f2})")
    ok, _, _ = path(place_ladder(2, 2, 3), gaps(place_ladder(2, 2, 2), 14))
    check(not ok, "the path checker did not fire")
    print("  the path checker fires on the (2,2,3) walk read against the "
          "(2,2,2) gaps")


def path(lad, g):
    S = L.Sched(lad.name, lad, L.price_power(1))
    _, log = run(S, SUP, False, 120)
    i = next(i for i, x in enumerate(log) if x[0][0] != "o")
    doors = follow(log, i)
    r0 = log[i][3][2]
    want = ([1] if r0 == 1 else [2]) + g
    return doors[:12] == want[:12], r0, doors[:12]


def section_path():
    print("S1  THE PATH (PR2): the first clocked item's first twelve doors, "
          "per-item clock, corner")
    for lad in ladders():
        ok, r0, doors = path(lad, gaps(lad, 14))
        check(ok, f"the path at {lad.name}")
        s, tl = sup_tail(lad)
        print(f"  {lad.name:9s} sup {s:2d} tail {tl}  entry {r0}  {doors}")


def section_walks():
    """PR1, PR3, PR4: every cell, every branch."""
    print(f"S2  EVERY CELL (PR1, PR3, PR4): 2 items per degree to 400, born "
          f"{{1}}, ties branched over {K} moves, {N} more clock-first")
    print("  price  ladder    sup tail  branches  lemma  per-item off | "
          "changes  below  1-holder off  above")
    tot = Counter()
    for pname, price in PRICES:
        for lad in ladders():
            s, tl = sup_tail(lad)
            S = L.Sched(lad.name, lad, price)
            row = Counter()
            for glob in (False, True):
                for st, log in branches(S, SUP, glob, K, N):
                    H = max(x[2] for x in log)
                    row["lemma"] += lemma_faults(S, st, SUP, H)
                    lt = late(log)
                    check(lt, "no clock move in the last quarter")
                    if not glob:
                        row["pi"] += 1
                        for (d, r0), doors in lt.items():
                            if (H != price(d, max(r0, s), False)
                                    or set(doors) != {tl}):
                                row["pi_off"] += 1
                        continue
                    row["gl"] += 1
                    check(len(lt) == 1, "two items clocked late, global")
                    (dX, _), = lt
                    check(set(lt[(dX, _)]) == {tl}, "the global tail")
                    chg = any(x[4] for x in log)
                    row["chg"] += chg
                    row["below"] += H < price(dX, s, False)
                    row["above"] += H > price(dX, s, False)
                    row["chg_above"] += chg and H > price(dX, s, False)
                    if not chg:
                        r0x = next(x[3][2] for x in log if x[0][0] != "o")
                        row["entry_above"] += (H > price(dX, s, False)
                                               and r0x > s)
                        row["one_off"] += H != price(dX, max(r0x, s), False)
            check(row["lemma"] == 0, f"the lemma at {pname} {lad.name}")
            check(row["pi_off"] == 0, f"per-item at {pname} {lad.name}")
            check(row["below"] == 0 and row["one_off"] == 0,
                  f"global at {pname} {lad.name}")
            tot += row
            print(f"  {pname:6s} {lad.name:9s} {s:3d} {tl:4d} "
                  f"{row['pi']:5d}/{row['gl']:<4d} {row['lemma']:5d} "
                  f"{row['pi_off']:9d}     | {row['chg']:6d} "
                  f"{row['below']:6d} {row['one_off']:12d} "
                  f"{row['above']:6d}")
    print(f"  totals: {tot['pi']} per-item and {tot['gl']} global branches; "
          f"lemma faults {tot['lemma']}, per-item off {tot['pi_off']}; "
          f"global: {tot['chg']} with a holder change, {tot['below']} below "
          f"the floor, {tot['one_off']} single-holder off, {tot['above']} "
          f"above the floor: {tot['chg_above']} with a holder change, "
          f"{tot['entry_above']} without one and the entry door above the "
          f"sup")


def section_excess():
    """PR5."""
    print("S3  THE EXCESS (PR5): corner, global clock, open degree 2 then "
          "clock it, then clock-first")
    for c in (2, 3, 5):
        S = L.Sched(f"gap {c}", L.ladder_gap(c), L.price_power(1))
        st, log = run(S, SUP, True, N, first=[("o", 2, 0, 1),
                                               ("c", 2, 1, 1)])
        H = max(x[2] for x in log)
        (dX, _), = late(log)
        strands = sum(x[4] for x in log)
        u = horizon(S, st, SUP)
        check(H != c, f"the old reading held on the strand branch, c = {c}")
        check(H == c + 2 and dX == 1 and strands == 1 and u == c + 2,
              f"PR5: the hand-run at c = {c}")
        print(f"  gap {c}: H {H}, runaway degree {dX}, strands {strands}, "
              f"horizon {u}, d_X sup {dX * c}")


def section_fate():
    """PR6."""
    print("S4  THE FATE UNDER A PER-ITEM CLOCK (PR6): openings in the last "
          "half, corner, clock-first")
    for lad in ladders() + [L.ladder_b(2), L.Ladder(
            "squares", lambda t: (L.isqrt(t) + 1) ** 2, False)]:
        S = L.Sched(lad.name, lad, L.price_power(1))
        _, log = run(S, SUP, False, N)
        late_opens = sum(1 for x in log[N // 2:] if x[0][0] == "o")
        check((late_opens == 0) == lad.bounded, f"the fate at {lad.name}")
        print(f"  {lad.name:12s} bounded {str(lad.bounded):5s} "
              f"late openings {late_opens}")


def main():
    t0 = time.time()
    section_control()
    section_path()
    section_walks()
    section_excess()
    section_fate()
    print(f"ALL CHECKS PASS: {CHECKS[0]} checks, {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
