"""The q = 2 climb/degree-1 tie, reached -- the engineered supply the
filtration seam's one counter-direction asks for.

THE QUESTION. explore_filtration_price.py F1: over one residue base q
the multiplicative price is strictly MORE separating than the additive
one -- every cross-degree additive opening tie breaks -- with exactly
ONE new tie of its own, at q = 2 in the climb/degree-1 form (a climb
one log-rung under a degree-1 opening: 2^a = 2^(a+1) - 2^a, the only
way a difference of two q-powers is a q-power). No canonical walk run
there ever REACHED that tie; the open clause is that a supply
engineered to reach it would branch multiplicatively where the
additive walk does not -- the seam's one counter-direction. This rig
builds that supply and runs both prices through it.

THE HAND-TRACE, on paper before the engine. Supply: TWO items of
degree 1, nothing else. Schedule: the corner (alpha = 1, b = 2,
m = 1, born = empty), base q = 2. Step 0 is forced: nothing is
seated, degree 1 is uncovered, so the one move is the fresh open at
door 1 (multiplicative price 2^1 - 2^0 = 1) -- it seats the item at
exponent 1, tickless, and covers degree 1. At step 1 the menu holds
exactly two candidates: the climb on the seated item, width
r = T + 1 - e = 1, price 2^1 both ways; and the covered opening of
the second item, door T + 1 = 2, additive price 2^2, multiplicative
2^2 - 2^1 = 2^1. So the multiplicative menu is the H3 tie and the
additive menu is a singleton climb. The tie needs an item at
exponent 1, which only a fresh seat produces and only the first move
did: it fires once and never again.

PREDICTIONS (fixed before the run; each names what the rig prints):
  P1 (positive control): the six standard supplies' multiplicative
     branched stretches at q = 2 (explore_filtration_price.py's
     branches_raw) each carry exactly ONE branch -- the parent's
     recorded singleton counts, and with them "no canonical walk
     reached the tie", re-verified.
  P2: the engineered supply's multiplicative menu at step 1 is the
     two-key tie {(1,1,move): 1, (1,2,open): 1}; the additive menu at
     the same state is the singleton {(1,1,move): 1}. The
     multiplicative branch count over the branched stretch is 2, the
     additive count is 1.
  P3 (permanence): the two multiplicative branches share no state key
     over 40 further canonical moves -- the open branch carries two
     seated slots forever, the climb branch one (its opening at price
     2^T never undercuts its climb at 2^(T/2)).
  P4: the tie fires ONCE: over a 120-move canonical multiplicative
     walk of the engineered supply, exactly one state's menu has more
     than one key, and it is step 1's.
  P5 (base control): the same supply at q = 3 multiplicative has zero
     multi-key menus over 120 moves -- the order lemma has no
     equality at q >= 3.

KILL-SHAPES, as observables. K1: a multi-key menu inside P1's control
(the instrument contradicts the parent record; nothing downstream
readable). K2: step 1's menu differs from P2's dictionary (the hand
trace is wrong). K3: the branches re-share a key (permanence dies --
an informative miss, not a dead rig).

FINDINGS (entered by a separate post-run edit; printed output copied
from the run):

F1 THE TIE IS REACHED AND IT BRANCHES THE MULTIPLICATIVE WALK ONLY
   (observation, the engineered two-item supply). Step 1's
   multiplicative menu is the predicted two-key tie
   {(1,1,move), (1,2,open)} at price 2^2 - 2^1 = 2^1; the additive
   menu at the same state is the singleton climb. Branched stretch: 2
   multiplicative branches against 1 additive -- the counter-direction
   of the seam's headline sign (everywhere else the swap REMOVES
   ties; here, once, it makes one), exactly where the order lemma's
   q = 2 equality says it must. All six standard supplies' branched
   stretches stay singleton (P1 control green): no walk run there
   reaches the tie; the engineered supply is what reaches it.

F2 THE BRANCH IS PERMANENT AND THE TIE FIRES ONCE (observation). The
   two branches share no state key over 40 further canonical moves --
   seated support two slots against one from the branch point on.
   Over 120 canonical moves the engineered walk's menu is multi-key
   exactly once, at step 1: the tie needs an item at exponent 1, only
   the first fresh seat makes one, and the walk never returns. At
   q = 3 the same supply has zero multi-key menus (P5 green) -- the
   equality is base-2's alone, as derived.

RUN RECORD (this file, ~4 s, well under 512 MB, no numpy; 14 checks
green on the first run, every prediction hit; findings entered by
this post-run edit).

Related scripts: explore_filtration_price.py (the seam, the order
lemma, the price objects -- imported, never reimplemented),
explore_price_schedule.py (the walker beneath it).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import explore_filtration_price as FP
import explore_price_schedule as PS


def ok(cond, msg):
    print(("  [ok] " if cond else "  [FAIL] ") + msg)
    assert cond, msg


def section(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


def npl_of(pairs, dcap=PS.DEG_CAP):
    npl = [0] * (dcap + 1)
    for d, n in pairs:
        npl[d] = n
    return npl


def canonical_tie_census(sch, npl, tag, nmoves):
    """Run the canonical walk (least tie key at every state), recording
    every state whose menu holds more than one key."""
    s = FP.FWalk(npl, sch, tag)
    multi = []
    for step in range(nmoves):
        _, ties = s.menu()
        if len(ties) > 1:
            multi.append((step, dict(ties)))
        s.apply(sorted(ties)[0])
    return multi


# ------------------------------------------------- P1: the six-supply control
section("P1 CONTROL: canonical mult walks at q = 2, six standard supplies")

supplies, _ = FP.supplies_build()
for name in FP.SWEEP:
    sch = FP.FSched("mult-" + name, 2, "mult")
    census = {}
    branches = FP.branches_raw(supplies[name], sch, "mult-" + name, census)
    print(f"  {name:>8}: {len(branches)} branch(es)")
    ok(len(branches) == 1, f"P1: {name} multiplicative stretch is singleton")

# --------------------------------------- P2: the engineered supply, both prices
section("P2: the engineered two-item supply, step-1 menus and branches")

ENG = npl_of([(1, 2)])

sch_m = FP.FSched("eng-mult", 2, "mult", born=())
sch_a = FP.FSched("eng-add", 2, "add", born=())

for sch, label in ((sch_m, "mult"), (sch_a, "add")):
    s = FP.FWalk(ENG, sch, "eng-" + label)
    _, t0 = s.menu()
    print(f"  {label}: step-0 menu {sorted(t0.items())}")
    s.apply(sorted(t0)[0])
    _, t1 = s.menu()
    print(f"  {label}: step-1 menu {sorted(t1.items())}")
    if label == "mult":
        ok(t1 == {(1, 1, "move"): 1, (1, 2, "open"): 1},
           "P2: mult step-1 menu is the climb/degree-1 opening tie")
    else:
        ok(t1 == {(1, 1, "move"): 1},
           "P2: add step-1 menu is the singleton climb")

census_m, census_a = {}, {}
br_m = FP.branches_raw(ENG, sch_m, "eng-mult", census_m)
br_a = FP.branches_raw(ENG, sch_a, "eng-add", census_a)
print(f"  branched stretch: mult {len(br_m)} branches, add {len(br_a)}")
ok(len(br_m) == 2, "P2: multiplicative walk branches (2)")
ok(len(br_a) == 1, "P2: additive walk does not (1)")

# --------------------------------------------------- P3: permanence
section("P3: the two multiplicative branches, 40 further canonical moves")

keys_seen = [set(), set()]
for i, b in enumerate(br_m):
    s = b
    for _ in range(40):
        keys_seen[i].add(PS.key_of(s))
        _, ties = s.menu()
        s.apply(sorted(ties)[0])
    keys_seen[i].add(PS.key_of(s))
slots = [sum(len(v) for v in b.seat.values()) for b in br_m]
print(f"  seated slots per branch after the stretch: {sorted(slots)}")
ok(not (keys_seen[0] & keys_seen[1]),
   "P3: no shared state key over 40 further moves")
ok(sorted(slots) == [1, 2],
   "P3: one branch carries one seated slot, the other two")

# ------------------------------------------- P4, P5: uniqueness + base control
section("P4/P5: tie census over 120 canonical moves, q = 2 and q = 3")

multi2 = canonical_tie_census(FP.FSched("eng-mult2", 2, "mult", born=()),
                              ENG, "eng-mult2", 120)
print(f"  q = 2: multi-key menus at steps {[m[0] for m in multi2]}")
ok(len(multi2) == 1 and multi2[0][0] == 1,
   "P4: the tie fires exactly once, at step 1")

multi3 = canonical_tie_census(FP.FSched("eng-mult3", 3, "mult", born=()),
                              ENG, "eng-mult3", 120)
print(f"  q = 3: multi-key menus at steps {[m[0] for m in multi3]}")
ok(len(multi3) == 0, "P5: zero ties at q = 3 (the equality is base-2's)")

print("\n  done: every section asserted.")
