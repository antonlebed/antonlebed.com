"""explore_image_domain.py -- the per-item image's domain measured by a
sufficient test: branch the continuation, read the widest head, and derive
why a constant gap never settles its ties.

THE QUESTION. explore_headed_image.py F3 files the domain claim -- a head is
what makes a per-item limit determined -- on a NECESSARY condition: a state
is called determined when the first-tie and last-tie continuations return one
reading. Its own F7 names the three holes this leaves. (i) Every determined
count is an UPPER bound -- two extremes agreeing says nothing about the
continuations between them -- so the headed cells' 100% and the constant
controls' few percent are both ceilings. (ii) The mechanism -- a ramp breaks
a symmetry a constant gap preserves -- is a shape, not a derivation. (iii)
The widest head, (p 2, e 8, w 4) at sup 12, locks nowhere inside the 24-move
budget and reads ZERO at both supplies, so the claim is untested exactly
where the head is largest. This rig answers all three: the continuation is
BRANCHED over every minimal-cost tie under stated caps, the widest ladder is
walked to twice the budget, and the tie's survival at a constant gap is
derived from the door law and the derivation's consequence checked at every
determined state.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. "Determined" is
this family's own word and keeps its meaning: a state is determined when
every minimal-cost continuation reaches one reading. The branching test
grades it in three verdicts and the words are fixed here: DETERMINED (every
branch enumerated, every one locks, one reading), UNDETERMINED (two branches
lock on different readings -- definitive, since both are genuine least-cost
continuations), UNRESOLVED (a cap fired, or a branch failed to lock at the
horizon -- no verdict, never counted as determined). The old two-extremes
verdict is called EXTREMES-DETERMINED throughout.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The lock horizon is IMPORTED: 2 x 24 continuation moves, judged on the
    second half against the last quarter, exactly explore_headed_image.py's.
    A fork or a lock that first appears past the horizon is invisible to
    both instruments, so every verdict here is "at the horizon" and the
    comparison with the imported figures is like against like.
 T2 The lifted budgets 30..48 for the widest ladder are a NEW parameter
    value. No figure at any budget past 24 exists in the corpus and none is
    inherited: the constant-gap columns printed beside the headed one at
    those budgets are new too.
 T3 The branch enumerator prunes slot-symmetric ties -- two moves of one
    degree and price advancing items with EQUAL exponent and tick. The
    prune is DERIVED (below), not measured, so S1b audits it against the
    unpruned enumerator wherever the unpruned one terminates under the cap.

THE HAND-ATTACK, on paper before any engine code.

 A. THE DOOR LAW MAKES DEPTH FREE OF DISCOUNT AT A CONSTANT GAP. The walker
    prices a move at degree x door and the door reads the CLOCK, not the
    exponent: door = tick + 1 - e. On a constant-gap-g ladder an item that
    has landed once sits at e = tick_old + 1 with tick = tick_old + g, so
    tick - e = g - 1 and the next landing preserves it: every landed item's
    door is g FOREVER, at every depth. Two landed items of one degree are
    therefore priced identically at every step of every continuation --
    depth never buys either of them a discount.

 B. THE TIE IS A FORK, AND THE FORK'S TWO READINGS DIFFER EXACTLY WHERE THE
    KEPT EXPONENTS DO. Take a least-cost continuation from state w that runs
    item A away, and let B be a landed sibling -- same degree d, exponent
    e_B distinct from e_A, with the same door future. EXCHANGING A's and
    B's advances throughout is again least-cost at every step: the swapped
    state differs from the original only by exchanging two items of one
    degree, and menu prices read items only through (degree, exponent,
    tick). The original continuation's reading forgets A and keeps B at
    e_B plus whatever B gained; the mirror forgets B and keeps A at e_A
    plus the same gain. The two readings differ if and only if e_A and e_B
    differ in w. So a state whose forgotten degree carries a landed,
    distinct-exponent, equal-door-future sibling is GENUINELY undetermined
    -- the extremes test was measuring the object, not missing it -- and
    this is a derivation, not a shape. On a constant-gap ladder EVERY pair
    of landed siblings qualifies by A, which is why the tie survives there.

 C. A HEAD BREAKS THE SYMMETRY BY PRICING POSITION -- BUT ONLY OFF THE
    TAIL. On a headed ladder the door depends on where the item stands: at
    the splice it is the sup, past it the tail. An item past the splice
    holds a door future no item behind the splice can match, so the mirror
    argument fails between them and the fork closes. But two siblings BOTH
    past the splice see constant tail doors and are swappable again by B.
    The headed cells' 100% must therefore rest on the walk never LANDING
    two siblings of one degree past the splice inside the budget -- the
    ramp staggers arrivals, the sibling left behind faces the sup door --
    and the swap census below prints whether that is so rather than
    assuming it.

DISTRUST THE MARGIN. The derived halves are A and B -- bookkeeping on the
door law. The vibes are (1) that the branch enumeration terminates under its
caps at the cells that matter, and (2) PR4's "by budget 48": the widest
ladder's stop sits at d_deep x sup and d_deep is not measured here before
the run. Both name printed columns and the caps are printed when they fire,
never silent.

PREDICTIONS, fixed before any engine code, each naming what the rig PRINTS.
What they mean is weighed after the run.

PR1 THE CHAIN INSTRUMENT IS THE IMPORTED ONE. Restricted to a single
    first-tie (or last-tie) chain, the branch enumerator's reading equals
    explore_headed_image.py's reading_locked at every per-item final state
    of every cell. What the rig PRINTS: the agreement count, asserted.
    KILL: any mismatch -- the branch instrument would be a different
    instrument and nothing downstream could be compared.

PR2 THE HEADED 100% SURVIVES BRANCHING. At the twelve headed cells whose
    every final state is extremes-determined, every final state is
    branch-DETERMINED: full enumeration, one reading. What the rig PRINTS:
    per headed cell, determined / undetermined / unresolved counts beside
    the extremes figure. KILL: any headed final state UNDETERMINED or
    UNRESOLVED.

PR3 THE CONSTANT CONTROLS FALL TO THEIR SYMMETRIC STATES. Hand-attack B
    both ways: (a) no branch-DETERMINED state anywhere carries a swappable
    pair -- a landed, distinct-exponent, equal-door-future sibling pair
    with exactly one of the two forgotten by its reading; (b) among the
    extremes-determined control states that fall under branching, the
    fallen carry swappable pairs. What the rig PRINTS: per cell, the
    branch verdicts beside the extremes figure, and the swap census over
    determined and fallen states. KILL for (a), the derivation's own: a
    DETERMINED state carrying a swappable pair.

PR4 THE WIDEST HEAD READS NONZERO AND FULL PAST ITS STOP. At budgets
    30..48 the (p 2, e 8, w 4) ladder's walk locks and every locked final
    state is branch-DETERMINED at both supplies -- the domain claim
    extending to the widest head. What the rig PRINTS: live counts, locked
    counts and branch verdicts at each lifted budget, the constant
    controls beside. KILL: zero determined states at budget 48 at either
    supply.

PR5 THE GLOBAL CLOCK IS UNTOUCHED. Branching moves nothing at a global
    clock: every global live state is branch-DETERMINED. The filed
    tie-independence there is two-extremes evidence, so this is a new
    check of an old figure. What the rig PRINTS: the global state count
    and its determined count. KILL: any global UNDETERMINED state.

THE POSITIVE CONTROL (S1, run before any verdict is read).
  S1a PR1 as a control: both single-chain policies against the imported
      reading at every per-item final state, asserted state by state.
  S1b THE PRUNE AUDITED. The slot-symmetry prune is derived, so the
      unpruned enumerator is run beside it at a printed sample of states
      -- the sorted roster's first 60, not a spread across cells -- and
      the verdicts must agree wherever the unpruned one terminates under
      the cap.
  S1c THE DOOR LAW PRINTED, hand-attack A's premise: at every constant-gap
      final state, every item whose own tick exceeds 1 has door exactly
      the gap. Asserted per state.

THE INSTRUMENTS. The walker, the enumeration, the repaired reading, the
lock test, the ladders, both supplies and the schedule are all
explore_headed_image.py's, imported: live_at, reading_locked, determined,
ladder_row, supplies, sched, and the psi generator underneath them from
explore_headed_ladder.py. This rig adds the branch enumerator and the door
and swap censuses; the caps are its own and printed.

FINDINGS (tiers below; run record at the bottom).

F1 THE CONSTANT CONTROLS' DETERMINED STATES WERE ALL TIES -- THE PER-ITEM
   IMAGE OVER A CONSTANT-GAP LADDER OF GAP 2 OR WIDER HAS AN EMPTY DOMAIN
   (rule in range; every extremes-determined state of every such control
   cell fully enumerated, no caps fired). The 2491 extremes-determined
   states across the 26 control cells of gap >= 2 -- the 2.9% to 13%
   explore_headed_image.py F3 filed as an upper bound -- go UNDETERMINED to
   the last state: two genuine least-cost continuations lock on different
   readings at every one. The upper bound did not shrink; it collapsed.
   What that empties is the domain and not the instrument: the extremes
   image sizes this rig prints at those cells (14 readings at the widest
   F_2[x] sup control, 570 at an h5 cell) are counts of artifacts, and the
   honest per-item image of a constant-gap ladder in this range holds NO
   reading at all.

F2 AND THE HEADED 100% IS REAL (rule in range; PR2 confirmed at full
   enumeration). All twelve headed cells whose every final state passed the
   extremes test keep every state DETERMINED under the branch enumeration
   -- 142 states, no caps, one reading per state. With F1 this sharpens the
   domain claim of explore_headed_image.py F3 from an upper bound to an
   exact statement in range: the head does not enlarge the per-item image's
   domain, it CREATES it.

F3 WHY, NOW DERIVED AND NOT A SHAPE (rule; the derivation's premise and
   consequence both checked in range). The door reads the clock, not the
   exponent: door = tick + 1 - e. On a constant-gap-g ladder every landed
   item therefore holds door g forever (33293 final states, no exception),
   so two landed siblings of one degree are priced identically at every
   step of every continuation, and any continuation that runs one away has
   an equal-cost mirror running the other -- readings that differ exactly
   where the siblings' kept exponents do. The consequence holds both ways
   in range: ZERO of the branch-determined states anywhere carry a
   swappable pair (a landed, distinct-exponent, equal-door-future sibling
   pair split by the reading), and at the h5 cells of gap 2 through 8 the
   fallen states carry the witness almost to the last -- 120 of 121 up to
   458 of 462 per cell. THE RESIDUAL, at observation: 47 fallen states
   carry NO such pair -- all 30 F_2[x] falls, the h5 gap-12 cell's 2, and
   one to four per remaining h5 cell -- so a second fork kind parts
   readings there: the census condition is sufficient, not necessary, and
   the other fork is not named here.

F4 THE ONE CONSTANT SURVIVOR IS GAP 1 (observation; 25 states). The exact
   ladder keeps its extremes-determined states: 24 of 24 over F_2[x] and
   1 of 1 over h5 branch-DETERMINED, none carrying a swappable pair --
   consistent with F3, since a determined state there must simply hold no
   landed distinct-exponent pair at a forgotten degree, and these hold
   none. So F1's empty-domain statement is for gap >= 2, and the per-item
   domain dichotomy in range reads: a constant gap of 2 or wider hands the
   image nothing, the exact ladder and every head hand it their locked
   states.

F5 THE WIDEST HEAD LOCKS PAST THE OLD CAP, AND ITS DOMAIN IS FULL WHERE IT
   RESOLVES (rule in range; PR4's kill FIRED at its named budget and the
   lifted probe answered the question the kill was probing). At budget 48
   nothing is locked at either supply -- the frozen kill -- and the lock
   arrives between 60 and 84, none at 60 at either supply: over h5 all 320
   live states are locked already at 72 (and 10168 of 10168 at 84), over
   F_2[x] 90 of 134 at 72 and 5712 of 5712 at 84. At
   budget 84 the full enumeration reads 4432 DETERMINED / 0 UNDETERMINED /
   1280 UNRESOLVED over F_2[x] (331 readings) and 9202 / 0 / 966 over h5
   (188 readings): ZERO ties at the widest head -- every state the caps
   and horizon resolve is determined, and the unresolved band is the
   rig's own budget, not a tie found. The economics print shows the stop
   arrived: at a final state the recurrent degree-1 item's door price is
   8 and the cheapest move is 8 -- the runaway's own advance has reached
   the menu floor. The enumeration
   outruns its 20000-state cap at budgets 87-89, so nothing past 84 is
   read.

F6 NO TIE APPEARS AT A GLOBAL CLOCK UNDER BRANCHING (rule in range; PR5).
   Over 747 deduplicated global-clock states: 516 DETERMINED, 0
   UNDETERMINED, 231 with a branch unlocked at the horizon, 0 at a cap.
   Probed against the imported instrument, the 231 split: 102 carry no
   extremes reading either, and 129 PASS the extremes test while holding
   a least-cost branch that does not lock in 48 moves -- so the filed
   global tie-independence is CONFIRMED at 516 states, UNCERTIFIED rather
   than refuted at 129, and no state anywhere read two readings.

F7 WHAT IS LEFT OPEN. (i) Every verdict is at the imported 2 x 24-move
   horizon (T1): a fork first appearing past it is invisible, so DETERMINED
   means determined-at-horizon everywhere. (ii) F3's residual: the fork
   that parts the F_2[x] fallen states without a swappable pair is unnamed.
   (iii) The widest head's unresolved band (1280 and 966 states) and its
   budgets past 84 are unread, and its reading set at 84 (404 by the
   extremes count, 331 among branch-determined states) is not settled.
   (iv) The image over a MIXED universe is still unrun --
   explore_tick_pump.py F8 (ii) asks for both and neither file answers the
   second half.

TIERS. F1, F2, F5, F6: rule in the stated ranges -- exhaustive enumeration
under printed caps, nothing sampled. F3: the derivation is algebra on the
door law and the mirror argument; its premise and consequence are checked
exhaustively in range, and its residual is at observation. F4: observation
at 25 states.

RUN RECORD. One process, CPython, no BLAS, under memwatch.py's 512 MB
ceiling. The first full run was KILLED at that ceiling inside S4 (the
bracketed design addition above); the final run: wall 361.5 s, peak
working set 451.6 MB. 4 aggregated asserts over 33443 chain-agreement
states (S1a, 0 mismatches), 60 unpruned prune audits (S1b, 60 agree), and
33293 door-law states (S1c, 0 violations), plus 3 forced-failure checks;
the census tables are printed, not asserted, and every cap that fired is
in the prints. S3's unresolved split (102 against 129) entered by a
post-run audit: the section gained the split print and was re-run alone,
the other figures untouched.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_headed_image as HI
import explore_headed_ladder as HL
import explore_tick_pump as TP

CHECKS = 0

H = HI.LOCK_STEPS               # half the continuation, imported (T1)
CAP_MENUS = 4096                # continuation states scanned per verdict
CAP_CHAINS = 256                # full chains per verdict
P2_BUDGETS = (24, 30, 36, 42, 48)   # the lifted grid; 24 is the old cap
LIVE_CAP = 20000                # live states per budget before a stated stop
PRUNE_SAMPLE = 60               # states audited unpruned in S1b
WIDE = "Z[2^1/8] w4"            # the sup-12 ladder, F7 (iii)'s empty cells


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ---------------------------------------------------- the branch enumerator
def read_of(w, half):
    """The reading of w with the slots in `half` forgotten -- the same
    construction as explore_headed_image.py's reading_locked, taken from a
    recurrent set computed along one branch rather than one policy."""
    out = {}
    for dd, row in w.seat.items():
        if not row:
            continue
        out[dd] = sorted(-1 if (dd, i) in half else e
                         for i, e in enumerate(row))
    return tuple(sorted((dd, tuple(v)) for dd, v in out.items()))


def lock_of(w, marks, sizes):
    """The recurrent set of one 2H-move chain, or None where the chain has
    not locked -- the three lock clauses exactly as the imported instrument
    states them: second half agrees with last quarter, the support froze,
    every recurrent item already seated in w."""
    tail = marks[H:]
    half = set().union(*tail) if tail else set()
    qtr = set().union(*marks[H + H // 2:])
    if not half or half != qtr:
        return None
    if sizes[-1] != sizes[H - 1]:
        return None
    if any(len(w.seat.get(d, ())) <= i for d, i in half):
        return None
    return half


def branch(w, policy=None, prune=True,
           cap_menus=CAP_MENUS, cap_chains=CAP_CHAINS):
    """Every minimal-cost continuation of w to the horizon, or one of them.
    policy None branches on every tie; "first"/"last" replay the imported
    extremes. Returns (verdict, readings, one recurrent set per locked
    chain, counters). Verdicts: DET / UNDET / UNRES as the docstring fixes
    them. The prune drops a tie advancing an item of the same degree,
    price, exponent AND tick as one already taken -- slot-symmetric moves
    whose subtrees differ only by relabelling two interchangeable items,
    which a slot-free reading cannot see (audited in S1b, never assumed)."""
    st = {"menus": 0, "chains": 0, "capped": False, "unlocked": False}
    readings, halves = set(), []

    def go(s, marks, sizes):
        if st["capped"] or st["unlocked"] or len(readings) > 1:
            return
        if len(marks) == 2 * H:
            st["chains"] += 1
            half = lock_of(w, marks, sizes)
            if half is None:
                st["unlocked"] = True
                return
            r = read_of(w, half)
            if r not in readings:
                readings.add(r)
                halves.append(half)
            return
        if st["chains"] >= cap_chains or st["menus"] >= cap_menus:
            st["capped"] = True
            return
        st["menus"] += 1
        _, ties = s.menu()
        if policy == "first":
            picks = [ties[0]]
        elif policy == "last":
            picks = [ties[-1]]
        elif prune:
            seen, picks = set(), []
            for mv in ties:
                _, d, slot, r, kind = mv
                if kind == "move":
                    k = (d, r, kind, s.seat[d][slot], s.tick((d, slot)))
                else:
                    k = (d, r, kind)
                if k in seen:
                    continue
                seen.add(k)
                picks.append(mv)
        else:
            picks = ties
        for mv in picks:
            s2 = s.copy()
            b = len(s2.clocks)
            s2.apply(mv)
            go(s2, marks + [set((c[1], c[2]) for c in s2.clocks[b:])],
               sizes + [sum(len(r) for r in s2.seat.values())])

    go(w, [], [])
    if len(readings) > 1:
        v = "UNDET"
    elif st["unlocked"] or st["capped"]:
        v = "UNRES"
    elif readings:
        v = "DET"
    else:
        v = "UNRES"
    return v, readings, halves, st


def chain_read(w, last=False):
    """The single-policy chain's reading, or None unlocked -- the branch
    machinery on the imported instrument's own path."""
    _, readings, _, _ = branch(w, policy="last" if last else "first")
    return next(iter(readings)) if readings else None


# ------------------------------------------------------------- the censuses
def door_seq(pump, e, t, n=2 * H):
    """The doors an item faces over its next n solo advances, from exponent
    e and tick t: door = t + 1 - e, land at t + 1, tick to the next ladder
    member. Stops where the ladder runs out; two items stopping at one tick
    share their whole future anyway."""
    out = []
    for _ in range(n):
        r = max(1, t + 1 - e)
        out.append(r)
        e = e + r
        try:
            t = pump.next_at(max(t, e))
        except AssertionError:
            break
    return tuple(out)


def swap_pair(w, half, pump):
    """Hand-attack B's witness: a degree carrying a FORGOTTEN slot and a
    KEPT slot, both landed (own tick above 1), exponents distinct, door
    futures pointwise equal. Returns one such (d, i, j) or None."""
    for d, i in sorted(half):
        row = w.seat.get(d, [])
        if len(w.seat.get(d, ())) <= i:
            continue
        ti = w.tick((d, i))
        if ti <= 1:
            continue
        fi = door_seq(pump, row[i], ti)
        for j, ej in enumerate(row):
            if (d, j) in half or j == i:
                continue
            tj = w.tick((d, j))
            if tj <= 1 or ej == row[i]:
                continue
            if door_seq(pump, ej, tj) == fi:
                return (d, i, j)
    return None


def door_law(w, g):
    """Hand-attack A's premise at one state: every item whose own tick
    exceeds 1 has door exactly g. Returns the violations."""
    out = []
    for d, row in w.seat.items():
        for i, e in enumerate(row):
            t = w.tick((d, i))
            if t > 1 and t + 1 - e != g:
                out.append((d, i, e, t))
    return out


# ----------------------------------------------------- S0 the forced failures
def s0_forced():
    section("S0  THE HARNESS FORCED TO FAIL")
    print("  Every check the run leans on, made to fail once.")
    npl = HI.supplies()["F_2[x]"]
    root = TP.PWalk(npl, HI.sched(), TP.p_step(2), TP.PERITEM, HI.DCAP)
    bad = 0
    try:
        v, _, _, _ = branch(root, cap_menus=0)
        ok(v == "DET", "forced: a capped verdict read as determined")
    except AssertionError:
        bad += 1
    try:
        a = door_seq(TP.p_step(2), 1, 1)
        b = door_seq(TP.p_step(2), 2, 3)
        ok(a == b, "forced: an unlanded and a landed door future read equal")
    except AssertionError:
        bad += 1
    try:
        r = lock_of(root, [set() for _ in range(2 * H)], [0] * (2 * H))
        ok(r is not None, "forced: an empty chain read as locked")
    except AssertionError:
        bad += 1
    ok(bad == 3, "only %d of the 3 forced checks fired" % bad)
    print("  3 of 3 forced checks fired.")


# --------------------------------------------------- the cells, walked once
def build_cells():
    """Every per-item cell's final states with the imported extremes verdict
    beside this rig's two single-policy chains -- S1a runs inside the build,
    before any branch verdict exists to read."""
    sups = HI.supplies()
    sch = HI.sched()
    rows = [HI.ladder_row(lab, p, e, w) for lab, p, e, w in HL.HEADED]
    cells = {}
    mismatch = 0
    for name in ("F_2[x]", "h5"):
        for label, pump, sup, tail, csup, ctail in rows:
            for tag, pm, g in (("head", pump, None),
                               ("sup", csup, sup), ("tail", ctail, tail)):
                per = HI.live_at(sups[name], sch, pm, TP.PERITEM,
                                 max(HI.P_BUDGETS))
                fin = list(per[-1].values())
                ext = []
                for w in fin:
                    r1, r2 = chain_read(w), chain_read(w, True)
                    if (r1 != HI.reading_locked(w)
                            or r2 != HI.reading_locked(w, True)):
                        mismatch += 1
                    ext.append(r1 is not None and r1 == r2)
                cells[(name, label, tag)] = (pm, g, fin, ext)
    return sups, sch, rows, cells, mismatch


def s1_controls(cells, mismatch):
    section("S1  THE CONTROLS")
    n = sum(len(c[2]) for c in cells.values())
    print("  S1a  both single-policy chains against the imported reading at")
    print("       every per-item final state: %d states, %d mismatches."
          % (n, mismatch))
    ok(mismatch == 0,
       "S1a: the chain instrument parted from the imported reading at %d "
       "states" % mismatch)

    print("  S1b  the prune audited against the unpruned enumerator:")
    done = agree = skipped = 0
    for (name, label, tag), (pm, g, fin, ext) in sorted(cells.items()):
        for w in fin:
            if done + skipped >= PRUNE_SAMPLE:
                break
            vp, rp, _, _ = branch(w)
            vu, ru, _, stu = branch(w, prune=False)
            if stu["capped"]:
                skipped += 1
                continue
            done += 1
            if vp == vu and rp == ru:
                agree += 1
            else:
                print("       DISAGREE %s/%s/%s: pruned %s, unpruned %s"
                      % (name, label, tag, vp, vu))
    print("       %d audited, %d agree, %d skipped at the unpruned cap."
          % (done, agree, skipped))
    ok(agree == done,
       "S1b: the prune changed a verdict at %d states" % (done - agree))

    viol = states = 0
    for (name, label, tag), (pm, g, fin, ext) in cells.items():
        if g is None:
            continue
        for w in fin:
            states += 1
            v = door_law(w, g)
            if v:
                viol += 1
    print("  S1c  the door law at every constant-gap final state: %d states,"
          % states)
    print("       %d with a landed item off door = gap." % viol)
    ok(viol == 0, "S1c: hand-attack A's premise failed at %d states" % viol)


# ------------------------------------- S2 the branching census (PR2, PR3)
def s2_census(rows, cells):
    section("S2  THE BRANCHING CENSUS, PER-ITEM FINAL STATES (PR2, PR3)")
    print("  Extremes-determined states get the full enumeration; a state")
    print("  the extremes already fail cannot be determined by inclusion")
    print("  (both extremes are branches) and is not re-run. `swap` counts")
    print("  determined states with a swappable pair -- hand-attack B says")
    print("  zero.")
    out = {}
    for name in ("F_2[x]", "h5"):
        print("\n  supply %s" % name)
        print("  %-14s %-5s %-4s %-9s %-9s %-7s %-7s %-7s %-6s %s"
              % ("ladder", "cell", "n", "extremes", "branchDET", "fellUN",
                 "fellUR", "capped", "swap", "fallen have pair"))
        for label, pump, sup, tail, csup, ctail in rows:
            for tag in ("head", "sup", "tail"):
                pm, g, fin, ext = cells[(name, label, tag)]
                ne = sum(ext)
                det = undet = unres = capped = swaps = 0
                fell_with = fell = 0
                for w, e in zip(fin, ext):
                    if not e:
                        continue
                    v, readings, halves, st = branch(w)
                    if st["capped"]:
                        capped += 1
                    if v == "DET":
                        det += 1
                        if swap_pair(w, halves[0], pm):
                            swaps += 1
                    elif v == "UNDET":
                        undet += 1
                    else:
                        unres += 1
                    if v != "DET":
                        fell += 1
                        if halves and swap_pair(w, halves[0], pm):
                            fell_with += 1
                print("  %-14s %-5s %-4d %-9d %-9d %-7d %-7d %-7d %-6d %s"
                      % (label, tag, len(fin), ne, det, undet, unres,
                         capped, swaps,
                         "%d of %d" % (fell_with, fell) if fell else "-"))
                out[(name, label, tag)] = (len(fin), ne, det, undet, unres,
                                           swaps)
    hd = [(k, v) for k, v in out.items() if k[2] == "head"]
    full = [(k, v) for k, v in hd if v[0] and v[1] == v[0]]
    kept = sum(1 for k, v in full if v[2] == v[0])
    print("\n  PR2: of %d headed cells extremes-determined at every state, %d"
          % (len(full), kept))
    print("       stayed determined at every state under branching.")
    sw = sum(v[5] for v in out.values())
    print("  PR3 (a): %d determined states carry a swappable pair." % sw)
    return out


# ------------------------------------------- S3 the global clock (PR5)
def s3_global(sups, sch, rows):
    section("S3  THE GLOBAL CLOCK UNDER BRANCHING (PR5)")
    print("  Every live global-clock state of every headed cell and its sup")
    print("  control, all budgets, deduplicated by state key.")
    seen = {}
    for name in ("F_2[x]", "h5"):
        for label, pump, sup, tail, csup, ctail in rows:
            for pm in (pump, csup):
                per = HI.live_at(sups[name], sch, pm, TP.GLOBAL,
                                 max(HI.G_BUDGETS))
                for st_ in per:
                    for k, w in st_.items():
                        seen.setdefault((name, pm.tag, k), w)
    det = undet = capped = 0
    un_both = un_ext = 0
    for w in seen.values():
        v, _, _, st = branch(w)
        if v == "DET":
            det += 1
        elif v == "UNDET":
            undet += 1
        elif st["capped"]:
            capped += 1
        elif HI.determined(w) is None:
            un_both += 1
        else:
            un_ext += 1
    print("  %d states: %d determined, %d undetermined, %d unresolved"
          % (len(seen), det, undet, capped + un_both + un_ext))
    print("  (%d at a cap; %d with no extremes reading either; %d passing"
          % (capped, un_both, un_ext))
    print("  the extremes test with a least-cost branch unlocked at the")
    print("  horizon -- uncertified there, not refuted).")


# ------------------------------- S4 the widest head, lifted budgets (PR4)
# [Design addition after the first full run: that run was KILLED at the
# memory ceiling here, because this section held every budget's whole state
# dict on the way to 48. The enumeration now keeps only the snapshots it
# will read, the S2 cache is freed before this section runs, and the head
# alone is probed further -- to budget 96 -- with the menu economics of a
# final state printed, so a walk that still does not lock says WHY.]
PROBE_BUDGETS = (24, 36, 48, 60, 72, 84, 96)


def live_capped(npl, sch, pump, budget, keep, cap=LIVE_CAP):
    """The imported enumeration keeping only the budgets in `keep`, with a
    stated stop: if a budget's live set passes the cap the run stops THERE
    and says so, rather than truncating silently."""
    root = TP.PWalk(npl, sch, pump, TP.PERITEM, HI.DCAP)
    live = {root.key(): root}
    out = {}
    for b in range(1, budget + 1):
        nxt = {}
        for s in live.values():
            _, ties = s.menu()
            for mv in ties:
                s2 = s.copy()
                s2.apply(mv)
                nxt.setdefault(s2.key(), s2)
        if len(nxt) > cap:
            return out, (b, len(nxt))
        live = nxt
        if b in keep:
            out[b] = dict(live)
    return out, None


def economics(w, sch):
    """One state's menu floor beside its deep items' own doors: what the
    cheapest move costs, against what advancing each deep item would."""
    best, _ = w.menu()
    deep = [(d, e, sch.price(d, max(1, w.tick((d, i)) + 1 - e)))
            for d, i, e in w.deep_items()]
    return best, sorted(deep)


def s4_wide(sups, sch, rows):
    section("S4  THE WIDEST HEAD AT LIFTED BUDGETS (PR4)")
    print("  The sup-12 ladder walked to budget %d, its constant controls"
          % max(PROBE_BUDGETS))
    print("  to %d beside it. `locked` is the extremes test at that"
          % max(P2_BUDGETS))
    print("  budget's states; the last kept budget gets the full")
    print("  enumeration, and a final head state's menu economics print.")
    row = next(r for r in rows if r[0] == WIDE)
    label, pump, sup, tail, csup, ctail = row
    for name in ("F_2[x]", "h5"):
        print("\n  supply %s" % name)
        for tag, pm, buds in (("head", pump, PROBE_BUDGETS),
                              ("sup", csup, P2_BUDGETS),
                              ("tail", ctail, P2_BUDGETS)):
            per, blown = live_capped(sups[name], sch, pm, max(buds),
                                     set(buds))
            if blown is not None:
                bb, n = blown
                print("  %-5s STOPPED: %d live states passed the %d cap at "
                      "budget %d; the kept budgets read below"
                      % (tag, n, LIVE_CAP, bb))
            kept = sorted(per)
            lives, locks, sizes = [], [], []
            for b in kept:
                st_ = per[b]
                lives.append(len(st_))
                rd_, lk, un = HI.locked_image(st_)
                locks.append(lk)
                sizes.append(len(rd_))
            if not kept:
                continue
            det = undet = unres = 0
            readings = set()
            fin = per[max(kept)]
            for w in fin.values():
                v, rd, _, _ = branch(w)
                if v == "DET":
                    det += 1
                    readings |= rd
                elif v == "UNDET":
                    undet += 1
                else:
                    unres += 1
            print("  %-5s live at %s: %s" % (tag, ",".join(map(str, kept)),
                                             "  ".join(map(str, lives))))
            print("        locked: %s   image size: %s"
                  % ("  ".join(map(str, locks)),
                     "  ".join(map(str, sizes))))
            print("        at budget %d the full enumeration: DET/UNDET/"
                  "UNRES %d/%d/%d (%d readings)"
                  % (max(kept), det, undet, unres, len(readings)))
            if tag == "head" and fin:
                w = next(iter(fin.values()))
                best, deep = economics(w, sch)
                print("        one final state: cheapest move %d; deep "
                      "items (degree, exponent, own door price): %s"
                      % (best, deep))


# ------------------------------------------------------------------- main
def main():
    s0_forced()
    sups, sch, rows, cells, mismatch = build_cells()
    s1_controls(cells, mismatch)
    s2_census(rows, cells)
    cells.clear()
    s3_global(sups, sch, rows)
    s4_wide(sups, sch, rows)
    section("SUMMARY")
    print("  %d checks, over %d headed ladders and their constant controls"
          % (CHECKS, len(rows)))
    print("  at two supplies, the continuation branched at every tie.")


if __name__ == "__main__":
    main()
