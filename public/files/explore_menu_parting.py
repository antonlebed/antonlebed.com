"""explore_menu_parting.py -- which walks never part, and why.

THE QUESTION. Pricing a greedy ideal walk by each place's OWN invariant
instead of the whole state's names a different chosen place at most steps
of most walks, but not all: over twelve walks in five rings the two menus
part at 409 of 720 steps, in seven walks across three rings, while five
walks -- Z[w]'s two, the -23 cubic's two, and Z[sqrt-5]'s void -- agree
throughout (explore_wild_ring.py F6). That record says plainly that WHY
those five agree is not settled, and rules out the first guess it could
think of: the -23 cubic's planted walk carries a gap-2 strand from its
seed and its menus still agree, so "every column gap 1" is not the
condition. The two pricings are two SELECTION RULES over the same
dynamics, so a condition separating them names what the populated
invariant sees that the lone one cannot.

This is a classification over walks that already ran. No new ring, no new
engine: the walker, the universes and the door are imported from
explore_wild_ring.py and the engines under it, so their asserts fire
beneath these readings and the 409 is reproduced rather than resembled.

THE SLATE, fixed before any engine code here.

WHAT A DOOR IS AT AN UNSEATED PLACE, hand-derived first because the whole
classification turns on it. An unseated place Q sits at exponent 0 with
lam(Q^0) = 1. Its LONE door is the least r whose climb outruns its own
column from 0, which is the least r with lam(Q^r) > 1; since
lam(Q^1) = N(Q) - 1, that is r = 1 at every place of norm at least 3, and
at least 2 at a place of NORM 2, whose first rung is trivial. So the lone
menu restricted to the norm->=3 unseated places is exactly "cheapest by
norm", and the norm-2 places are the one family where it is not -- which
is worth saying out loud because three of the five rings here have a
place of norm 2 and the first draft of this slate had them all covered by
one sentence that was false at every one of them.

Q's POPULATED door is the least r with lam(Q^r) not dividing L. At an
unseated place of norm at least 3 that exceeds the lone door exactly when
(N(Q) - 1) | L. Call such a place a COVERED opening: the state has
already paid for its first rung, so the populated rule charges it for a
deeper one while the lone rule still sells it the first. At a SEATED
place P at exponent e the same comparison holds with lam(P^e) in place of
1, and since lam(P^e) | L at a seated place the populated door is never
smaller. So, across the whole universe:

    populated cost >= lone cost, at every place and every state,

which makes the two menus differ ONLY where the lone menu's own winner is
strictly widened. That is an implication and not a measurement, and the
rig prints it as a control.

PREDICTIONS.

P1 (control, derived above; a violation is a bug in this rig and not a
   finding). At every place at every step, populated cost >= lone cost.
   0 violations.

P2 (control). At every step where the two menus name different places,
   the LONE menu's winner is strictly widened -- its populated door
   exceeds its lone door. 0 exceptions.

P3 (control on the import). The parting count reproduces the filed
   reading exactly: 409 of 720 steps, 7 of 12 walks, 3 of 5 rings, and
   the five agreeing walks are the ones named above.

P4 (the candidate condition, and what this rig is for). Every parting
   step is driven by a COVERED OPENING: the lone winner is an unseated
   place whose N - 1 already divides L. The five agreeing walks are then
   the walks whose lone winner is never covered. KILLED by either
   observable: a parting step whose lone winner is a SEATED place, or an
   agreeing walk carrying a step whose lone winner is widened at all.

   [P4 AS FROZEN, AND IT CARRIES A DEFECT THE HAND-ATTACK ABOVE HAD
   ALREADY FOUND: the derivation states that the (N - 1) | L reading
   holds at norm at least 3 and not at norm 2, and then this prediction
   was written over the whole universe anyway. It is left verbatim
   because that is what the slate said and rewriting it after the run
   would hide the one thing worth learning here -- a hand-attack is only
   worth its cost if the predictions are then read BACK against it. What
   the rig measures is the split; F2 carries it.]

P5 (the fallback the item named for itself). If P4 dies, the split is
   read against the coarsest thing left -- whether the walk's ring has a
   place of norm 2, whether the seed is void or planted, and the norm of
   the cheapest place in the universe -- and if no column of that table
   agrees with the agree/part answer at every one of the twelve rows, the
   finding is "the seeds differ and nothing finer" and the open clause
   retires.

WHAT IS PRINTED, so a kill is read off an observable and not off a
reading of one: per walk, the parting count, the count of steps whose
lone winner is widened, and that count split by whether the winner was
SEATED or an UNSEATED covered opening; then the twelve-row table P5 asks
for, with the agree/part column beside it.

TIER. A condition holding across twelve walks over five rings is an
OBSERVATION. It is a PATTERN only if it holds at every seed these
engines admit, and a RULE only when derived from the two invariants --
and the derivation above already carries the "only where widened" half,
so what is measured here is which widening mechanism actually fires.

SCALE. Twelve walks of 60 moves over universes already built at import;
one process, no BLAS, well under the 512 MB ceiling.

--------------------------------------------------------------------------
FINDINGS

F1 THE CONTROLS. P1 holds at 0 of the readings taken -- no place's
   populated cost ever undercut its lone cost, which is the derivation
   above printing rather than being trusted. P2 holds at 0 of 409 --
   every parting step had a strictly widened lone winner. P3 reproduces
   the filed reading exactly: 409 of 720 steps, 7 of 12 walks, 3 of 5
   rings, and the five agreeing walks are Z[sqrt-5]'s void, Z[w]'s two
   and the -23 cubic's two, name for name.

F2 EVERY WIDENED LONE WINNER IS AN UNSEATED PLACE, AT 410 OF 410 (rule in
   range over these twelve walks). The seated mechanism never fires as
   the LONE MENU'S WINNER at any step of any walk here: the count is 0,
   not small. So of the two mechanisms the filed record names, only one
   selects. The re-pricing of a seated STRAND is real and is what the
   door excess measures, but a strand is by construction not what either
   menu is about to buy -- which is the load-bearing half of this
   finding, and it is exact.

   THE COVERING IS THEN SPLIT BY NORM, AND THE SPLIT IS MEASURED RATHER
   THAN INFERRED, because the derivation in the slate above covers norm
   >= 3 only. At 293 of the 410 the winner is a genuine COVERED OPENING:
   norm at least 3, and (N - 1) | L at every one of them, 0 off -- the
   state has already paid for its first rung, so the lone rule still
   sells it and the populated rule charges a deeper one. The remaining
   117 are places of NORM 2, whose first rung is trivial for every state
   and where the divisibility holds for a reason that is not the state's:
   the lone door there is already 2, and the widening comes from the
   SECOND rung being covered instead of the first. Both are coverings and
   only the first is a statement about the state's residue cardinalities,
   which is why the count is reported split. An earlier reading of this
   file put all 410 in the first class on the strength of the derivation;
   the derivation does not reach the norm-2 places and the rig now
   measures the divisibility instead of assuming it.

F3 P4 IS KILLED, AND BY THE MARGIN THAT NAMES THE CONDITION: 410 steps
   carry a widened lone winner and 409 of them part. The exception is
   Z[w] (-23) planted at its ramified place, step 1, where the lone menu
   names the split place over 3 at a lone door of 1 and a populated door
   of 2 -- widened, and still the cheapest place under populated pricing,
   so the true menu names it too. A WIDENING is therefore NECESSARY for
   a parting and not sufficient -- the widening and not the covering,
   since 117 of the 410 are the norm-2 places F2 holds apart: what parts
   a menu is not
   the widening but the widening LOSING THE ARGMIN, a comparison between
   two prices the state sets and neither rule owns. That exception is a
   norm-3 place, so it sits inside the 293 F2 measures and not among the
   norm-2 readings F2 holds apart.

F4 SO THE CONDITION IS NOT A COARSE INVARIANT, WHICH IS WEAKER THAN "NOT A
   PROPERTY OF THE RING OR THE SEED" AND IS WHAT IS MEASURED. The stronger
   sentence is not available and should not be written: the (ring, seed)
   pair DETERMINES the whole walk, so "this walk parts" is trivially a
   property of the seed, and the question was only ever which invariant
   of it. Every coarse column P5 asks for disagrees with the verdict at
   some pair: the cheapest norm is 2 at four of the five rings and those
   four split three parting to one agreeing; a norm-2 place is present at
   ten of the twelve walks and present at agreeing ones; and void against
   planted cuts the wrong way twice, Z[sqrt-5] agreeing from the void and
   parting from both plants while Z[i] parts from both. The five agreeing
   walks agree for TWO different reasons and not one: four never carry a
   covered lone winner at any step, and the fifth carries exactly one and
   survives it. That is the answer to the open clause and it is not "the
   seeds differ and nothing finer" -- the selecting mechanism is named
   and exclusive (F2), and the parting test is a comparison between two
   prices at a single STATE, so the natural place to look for a condition
   is a step and not a walk.

F5 A CORRECTION TO THE FILED RECORD, found by reproducing it. Three
   specimens are printed in explore_wild_ring.py F6 and one of them reads
   its own tuple backwards: the print there is (step, TRUE winner, LONE
   winner) and the prose for Z[sqrt-5] planted over 5 says the lone menu
   names the strand, where the tuple has the lone menu naming the split
   place over 3 and the TRUE menu naming the strand. The other two
   specimens -- X at Z[2^(1/3)] and the split place over 5 at Z[i] -- are
   the right way round. The measurement is untouched and the sentence is
   corrected there. F2 above is why the error was reachable at all: a
   seated strand cannot be a lone winner, so the claim was refutable from
   the slate before any of this ran.

WHAT IS LEFT OPEN. (i) Whether a covered opening can lose the argmin at a
   ring with no place of small norm is unmeasured -- the -23 cubic, the
   one ring here whose cheapest norm is 5, never carries a covered lone
   winner at all, so it tests nothing. (ii) The exception is a single
   step in a single walk, which is enough to kill a sufficiency claim and
   not enough to characterize when a widening survives; the derivation
   the characterization would need compares two door exponents against
   two norms and is not attempted here. (iii) Element moves are outside
   this reading, as they are outside the sweep it reproduces.

RUN RECORD. `python memwatch.py explore_menu_parting.py`. One process,
CPython, no BLAS. 8 checks, 1.0 s wall, peak working set 22.0 MB against
the 512 MB ceiling. 12 walks x 60 moves = 720 steps, each priced under
both rules with the full universe scanned for P1. Engines imported, not
re-implemented: explore_wild_ring.py (the lone menu, this ring),
explore_cubic_ring.py (the forcer, the -23 engine, the quadratics).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_wild_ring as W
import explore_cubic_ring as C3

CHECKS = 0
MOVES = W.WALK_MOVES


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def rings():
    """The five engines and their ramified places -- explore_wild_ring.py
    S5's own list, so the seeds are the filed ones."""
    rams_of = {
        "Z[sqrt-5]": [('ram', 2), ('ram', 5)],
        "Z[w] (-23)": [('ram', 23)],
        "Z[i]": [('ram', 2)],
    }
    out = [(n, M, rams_of[n]) for n, M in C3._load_quadratics()]
    out.append(("-23 cubic", C3, [p for p in C3.UNIVERSE if p[1] > 1]))
    out.append(("Z[2^(1/3)]", W, [p for p in W.UNIVERSE if p[1] > 1]))
    return out


def cheapest_norm(mod):
    return min(mod.place_norm(pl) for pl in mod.UNIVERSE)


def classify_walk(mod, seed):
    """One greedy walk, every step read twice. Returns the counts the
    slate asks for plus the first specimen of each mechanism."""
    st = dict(seed)
    L = mod.lam_state(st)
    parted = widened = cov = seat = 0
    cov3 = cov2 = cov_bad = 0
    p1_bad = p2_bad = 0
    spec = {}
    for step in range(1, MOVES + 1):
        _, ties = mod.ideal_menu(st, L)
        true_pl, r = ties[0]
        _, lties = W.lone_menu(mod, st)
        lone_pl = lties[0][0]

        # P1: the inequality, over the whole universe at this state.
        for q in mod.UNIVERSE:
            e = st.get(q, 0)
            lr = mod.door_r(q, e, mod.lam_P(q, e))
            pr = mod.door_r(q, e, L)
            n = mod.place_norm(q)
            if n ** pr < n ** lr:
                p1_bad += 1

        e_l = st.get(lone_pl, 0)
        wl = mod.door_r(lone_pl, e_l, mod.lam_P(lone_pl, e_l))
        wp = mod.door_r(lone_pl, e_l, L)
        is_wide = wp > wl
        if is_wide:
            widened += 1
            if e_l >= 1:
                seat += 1
                spec.setdefault('seated', (step, lone_pl, e_l, wl, wp))
            else:
                cov += 1
                # The derivation says an unseated place of norm >= 3 is
                # widened exactly when (N - 1) | L. MEASURE it rather than
                # infer it -- and hold the NORM-2 places apart, where the
                # first rung is trivial for every state and the divisibility
                # is true for a reason that has nothing to do with the state.
                n_l = mod.place_norm(lone_pl)
                if n_l == 2:
                    cov2 += 1
                    spec.setdefault('norm2', (step, lone_pl, n_l, wl, wp))
                else:
                    if L % (n_l - 1) == 0:
                        cov3 += 1
                        spec.setdefault('covered',
                                        (step, lone_pl, n_l, wl, wp))
                    else:
                        cov_bad += 1
                        spec.setdefault('uncovered',
                                        (step, lone_pl, n_l, wl, wp, L))
        if lone_pl != true_pl:
            parted += 1
            if not is_wide:
                p2_bad += 1
            spec.setdefault('part', (step, true_pl, lone_pl, is_wide))

        st[true_pl] = st.get(true_pl, 0) + r
        L = mod.lam_state(st)
    return dict(parted=parted, widened=widened, covered=cov, seated=seat,
                cov3=cov3, cov2=cov2, cov_bad=cov_bad,
                p1_bad=p1_bad, p2_bad=p2_bad, spec=spec)


def main():
    section("S1  THE TWELVE WALKS, EACH STEP PRICED BOTH WAYS")
    print("  %-12s %-18s %-7s %-8s %-8s %-7s" % (
        "ring", "seed", "parted", "widened", "unseat", "seated"))
    rows = []
    for name, M, rams in rings():
        seeds = [("void", {})]
        for pl in rams:
            seeds.append(("planted %s" % (W.show(pl) if M is W else str(pl)),
                          {pl: 1}))
        for sname, seed in seeds:
            g = classify_walk(M, seed)
            rows.append((name, sname, M, g))
            print("  %-12s %-18s %-7d %-8d %-8d %-7d"
                  % (name, sname, g['parted'], g['widened'],
                     g['covered'], g['seated']))

    total_part = sum(g['parted'] for _, _, _, g in rows)
    steps = MOVES * len(rows)
    parting_walks = [(n, s) for n, s, _, g in rows if g['parted']]
    parting_rings = sorted({n for n, s in parting_walks})
    agreeing = [(n, s) for n, s, _, g in rows if not g['parted']]

    section("S2  THE CONTROLS -- read before any classification")
    bad = sum(g['p1_bad'] for _, _, _, g in rows)
    print("  P1  populated cost < lone cost at %d readings" % bad)
    ok(bad == 0, "P1: a populated cost undercut its lone cost")

    p2_bad = sum(g['p2_bad'] for _, _, _, g in rows)
    print("  P2  parting steps whose lone winner was NOT widened: %d of %d"
          % (p2_bad, total_part))
    ok(p2_bad == 0, "P2: a menu parted with an unwidened lone winner")

    print("  P3  parted at %d of %d steps, %d of %d walks, %d of 5 rings"
          % (total_part, steps, len(parting_walks), len(rows),
             len(parting_rings)))
    print("      agreeing walks: %s" % ", ".join("%s/%s" % a
                                                 for a in agreeing))
    ok(total_part == 409, "P3: the filed parting count did not reproduce")
    ok(steps == 720, "P3: the step count did not reproduce")
    ok(len(parting_walks) == 7, "P3: the parting-walk count did not reproduce")
    ok(len(parting_rings) == 3, "P3: the parting-ring count did not reproduce")

    section("S3  P4 -- IS EVERY PARTING STEP A COVERED OPENING?")
    p4_seated = [(n, s, g['seated']) for n, s, _, g in rows if g['seated']]
    p4_agree_wide = [(n, s, g['widened']) for n, s, _, g in rows
                     if not g['parted'] and g['widened']]
    print("  parting walks whose lone winner was ever SEATED: %s"
          % (p4_seated or "none"))
    print("  agreeing walks carrying a widened lone winner:   %s"
          % (p4_agree_wide or "none"))
    p4 = not p4_seated and not p4_agree_wide
    print("  P4 %s" % ("SURVIVES: every parting step is a covered opening"
                       if p4 else "KILLED by the observables above"))

    t3 = sum(g['cov3'] for _, _, _, g in rows)
    t2 = sum(g['cov2'] for _, _, _, g in rows)
    tb = sum(g['cov_bad'] for _, _, _, g in rows)
    tw = sum(g['widened'] for _, _, _, g in rows)
    print()
    print("  the widened unseated winners split by NORM, measured and not")
    print("  inferred -- the derivation covers norm >= 3 only:")
    print("    norm >= 3 with (N-1) | L (a covered opening): %d" % t3)
    print("    norm >= 3 with (N-1) not dividing L:          %d" % tb)
    print("    norm 2, whose first rung is trivial for any state: %d" % t2)
    print("    total widened: %d" % tw)
    ok(tb == 0, "the norm>=3 widening was not the covering after all")
    ok(t3 + t2 == tw, "the widened winners did not split by norm")
    for n, s, _, g in rows:
        for k in ('covered', 'norm2', 'seated', 'part'):
            if k in g['spec']:
                print("    %-12s %-18s first %-8s %s"
                      % (n, s, k, str(g['spec'][k])))

    section("S4  P5 -- THE COARSE TABLE, AGREE/PART AGAINST THE OBVIOUS")
    print("  %-12s %-18s %-6s %-8s %-9s %s" % (
        "ring", "seed", "min N", "has N=2", "seed", "verdict"))
    cols = []
    for n, s, M, g in rows:
        mn = cheapest_norm(M)
        row = (mn, mn == 2, s == "void", "part" if g['parted'] else "agree")
        cols.append(row)
        print("  %-12s %-18s %-6d %-8s %-9s %s"
              % (n, s, mn, row[1], "void" if row[2] else "planted", row[3]))
    verd = [r[3] for r in cols]
    for j, label in ((0, "min norm"), (1, "has a norm-2 place"),
                     (2, "seed is void")):
        vals = [r[j] for r in cols]
        agrees = all((vals[a] == vals[b]) == (verd[a] == verd[b])
                     for a in range(len(cols)) for b in range(len(cols)))
        print("  column '%s' agrees with the verdict at every pair: %s"
              % (label, agrees))

    section("VERDICT -- the predictions read against what printed")
    print("  P1 control: 0 undercuts, see S2")
    print("  P2 control: see S2")
    print("  P3 control: %d of %d, %d walks, %d rings -- see S2"
          % (total_part, steps, len(parting_walks), len(parting_rings)))
    print("  P4 %s -- see S3" % ("SURVIVES" if p4 else "KILLED"))
    print("  P5 the coarse table: see S4")
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
