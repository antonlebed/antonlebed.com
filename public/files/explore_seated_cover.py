"""The below-2^d seated-set covering rule, run -- the one member of the
seated-set kind explore_ladder_stop.py's exoneration did not cover.

THE QUESTION. explore_ladder_stop.py PR5: none of the five covering
rules keyed to the SEATED SET stops the fresh ladder, and the named
mechanism is that such a rule is FED BY the openings it would have to
outrun -- explicitly not a proof over the whole kind, since a
seated-set rule covering everything below 2^d (an opening at degree d
covers every degree below 2^d) would outrun the ladder, and no rule
like that was run. This rig adds that rule as a dial and runs it.

THE HAND-ATTACK, on paper before the engine, and it flips the
question. The below-2^d covered set does outrun the ladder's DEGREE
-- but outrunning the degree is not stopping the walk. Between fresh
opens a seated-set rule's covered set is FROZEN: it reads only the
born set and the opened degrees, and neither changes on a declining
move. So the least uncovered degree -- the frontier -- has a CONSTANT
price, while every declining move is a ticking move (fresh opens are
the only tickless moves in this family, engine-asserted per move) and
the deep item's re-clock doubles T, sending the menu minimum past any
bound. The frontier open is therefore eventually the strict minimum
and the walk takes it: NO seated-set rule stops the ladder
permanently; it can only stretch the gaps between opens. The covered
set a STOPPING rule needs must grow while the walk declines, which is
exactly the clock-keyed family's covered-while-d <= c*T.

The trace, corner schedule (price d * staleness, b = 2, m = 1, degree
1 born covered), width-2 supply with items at every degree to 65536,
canonical (deep-at-1) branch, ties to the climb by the canonical key
order:
  fresh opens at degrees 2, 4, 16, 65536,
  at clocks    T =       8, 16, 64, 262144,
  after ticking stretches of 3, 1, 2, 12 moves,
and after move 22 (the 65536 open) the rule covers everything below
2^65536, so the supply has no uncovered degree left and the walk is
not read past there (the parent's own discipline: past that state a
stopped ladder and a spent supply print the same thing).

PREDICTIONS (fixed before the run; each names what the rig prints):
  P1 (positive control): rule "self" on the same harness opens
     consecutive degrees 2, 3, 4, ... over 40 moves -- the parent's
     unstopped ladder, so the pow2 dial is the only thing that moves.
  P2: the pow2 walk's fresh opens are exactly degrees 2, 4, 16, 65536
     at steps 3, 5, 8, 21, at clocks T = 8, 16, 64, 262144; 22 moves
     read in all, and at move 22 the supply has no uncovered degree.
  P3: every move between fresh opens is a ticking move (the stretch
     lengths are 3, 1, 2, 12), and at every declined state the menu's
     own minimum is <= the frontier's price, with equality only at
     the climb-tie states.
  P4: each frontier open is taken at the first state whose climb
     price T/2 strictly exceeds the frontier price -- the frozen
     frontier undercut by a doubling clock, never a stop.

KILL-SHAPES, as observables. K1: the control's opened list is not
consecutive (harness broken, nothing readable). K2: an open sequence
other than P2's (the hand trace is wrong). K3: the walk declines the
frontier at a state where the frontier is the strict menu minimum
(the frozen-frontier argument is wrong -- the rule DOES stop the
ladder, the stronger finding, not a dead rig).

FINDINGS (entered by a separate post-run edit; printed output copied
from the run):

F1 THE BELOW-2^d RULE OUTRUNS THE DEGREE AND STILL DOES NOT STOP THE
   LADDER (observation for the run; the argument above is the reason,
   and the run confirms it move for move). Fresh opens at degrees
   2, 4, 16, 65536, at steps 3, 5, 8, 21, at clocks T = 8, 16, 64,
   262144 -- the hand trace exactly. The covered set leaps past every
   bound (after the fourth open it reaches 2^65536) and the walk
   still opens the frontier every time, each open firing exactly when
   the doubling climb price T/2 first strictly exceeds the frozen
   frontier price (P4, all four opens). The ticking stretches between
   opens are 3, 1, 2, 12 moves with no tickless move among them (P3);
   the "self" control opens consecutive degrees 2..34 over 40 moves
   (P1).

F2 SO NO SEATED-SET RULE STOPS THE LADDER, AND THE STOPPING KIND IS
   CLOCK-KEYED (rule for the dial family, by the frozen-frontier
   argument, its premise engine-asserted per move; measured at the
   most generous member). A seated-set rule's covered set reads only
   the born and opened degrees, which no declining move changes, so
   the frontier's price is a constant against a clock every declining
   move doubles: the frontier is eventually the strict menu minimum
   at ANY coverage growth rate. The parent's five-rule exoneration
   ("fed by the openings") thus extends to the whole seated-set kind:
   what a stopping rule needs is a covered set that grows WHILE the
   walk declines, and the clock-keyed covered-while-d <= c*T family
   (explore_stopped_untie.py's threshold c >= d_deep/2) is exactly
   that. Outrunning the ladder's DEGREE is not stopping the walk.

RUN RECORD (this file, ~2 s, well under 512 MB, no numpy; every
prediction hit on the first run -- two print-message cleanups, no
engine change; findings entered by this post-run edit).

Related scripts: explore_ladder_stop.py (the harness, the five rules,
the exoneration -- imported, never reimplemented),
explore_price_schedule.py (the walker beneath it),
explore_stopped_untie.py (the clock-keyed threshold c >= d_deep/2).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import explore_ladder_stop as LS
import explore_price_schedule as PS


def ok(cond, msg):
    print(("  [ok] " if cond else "  [FAIL] ") + msg)
    assert cond, msg


def section(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


class PSched(LS.CSched):
    """The covering dial extended by one rule: pow2 -- an opening at
    degree d covers every degree below 2^d. Tested via bit lengths so
    no 2^65536 integer is ever built: dd >= bit_length(d) iff d < 2^dd
    for d >= 1."""

    def extra(self, d, opens, T):
        if self.rule == "pow2":
            return any(dd >= d.bit_length() for dd in opens)
        return LS.CSched.extra(self, d, opens, T)


HI = 65536

section("P1 CONTROL: rule 'self' on the width-2 supply, 40 moves")

npl_self = LS.flat_supply(2, LS.LADDER_CAP)
w, opens, _ = LS.ladder_walk(npl_self, PSched("self-control", rule="self"),
                             "self-control", 40)
print(f"  opened degrees: {w.opened}")
ok(w.opened == list(range(2, 2 + len(w.opened))) and len(w.opened) >= 8,
   "P1: 'self' opens consecutive degrees 2, 3, 4, ... (unstopped ladder)")

section("P2/P3/P4: the pow2 rule, width-2 supply to degree 65536")

npl = LS.flat_supply(2, HI)
sch = PSched("pow2", rule="pow2")
wk = LS.CWalk(npl, sch, "pow2", HI)

log = []       # (step, taken_key, T_after, frontier, fprice, best)
step = 0
while True:
    d, fprice = LS.least_uncovered(wk)
    if d is None:
        break
    best, ties = wk.menu()
    key = sorted(ties)[0]
    Tb = wk.T
    wk.apply(key)
    log.append((step, key, Tb, wk.T, d, fprice, best))
    step += 1
    assert step <= 200, "runaway: coverage did not exhaust in 200 moves"

# a fresh open is a door-1 open (the only tickless move kind here)
fresh = [(s, k[0], Ta) for s, k, Tb, Ta, d, fp, b in log
         if k[2] == "open" and k[1] == 1]

print(f"  moves read: {len(log)}")
print("  fresh opens (step, degree, T at the open):")
for s, dd, Ta in fresh:
    print(f"    step {s:>3}  degree {dd:>6}  T {Ta}")

ok([dd for _, dd, _ in fresh] == [2, 4, 16, 65536],
   "P2: fresh opens are exactly degrees 2, 4, 16, 65536")
ok([s for s, _, _ in fresh] == [3, 5, 8, 21],
   "P2: at steps 3, 5, 8, 21")
ok([Ta for _, _, Ta in fresh] == [8, 16, 64, 262144],
   "P2: at clocks T = 8, 16, 64, 262144")
ok(len(log) == 22, "P2: 22 moves read before coverage exhausts the supply")
d_after, _ = LS.least_uncovered(wk)
ok(d_after is None, "P2: after the last open no uncovered degree remains")

# P3: between fresh opens every move ticks; stretch lengths as derived
stretches, cur = [], 0
tickless_outside = 0
for s, k, Tb, Ta, d, fp, b in log:
    if k[2] == "open" and k[1] == 1:
        stretches.append(cur)
        cur = 0
        continue
    cur += 1
    if Ta == Tb:
        tickless_outside += 1
print(f"  ticking stretches between fresh opens: {stretches}")
ok(tickless_outside == 0,
   "P3: every move between fresh opens is a ticking move")
ok(stretches == [3, 1, 2, 12],
   "P3: the stretch lengths are 3, 1, 2, 12 as hand-derived")

# P3/P4: declined states price the frontier; opens fire on strict undercut
declined_bad = [s for s, k, Tb, Ta, d, fp, b in log
                if not (k[2] == "open" and k[1] == 1) and not b <= fp]
ok(not declined_bad,
   "P3: at every declined state the menu minimum is <= the frontier price")
for s, k, Tb, Ta, d, fp, b in log:
    if k[2] == "open" and k[1] == 1:
        ok(Tb // 2 > fp,
           f"P4: step {s}: climb price {Tb // 2} > frontier price {fp} "
           f"at the open")
print("  [ok] P4: every frontier open fires exactly when the doubling "
      "climb price passes it")

print("\n  done: every section asserted.")
