"""THE SEED EXCLUSION: instrumenting the divergence seed at the
identity map's patience-down pairs.

THE QUESTION
------------
The shift telescope (explore_shift_telescope.py) left the
distance-one domination law measured, not derived: under the
identity map every off-bottom finite-loss class has SOME member
whose tree-patience-down move lands nested pointwise with smaller
loss (9,401 of 9,401 classes), while the pairwise form fails in
3,225 of 44,040 finite pairs — the member choice is load-bearing.
The paper analysis of the parallel commit loops names exactly one
divergence shape that can break nesting: THE SEED (below). This
rig instruments it: per pair, does the seed fire, when, and at
which style bits; per class, do the nesting witnesses coincide
with the seed-free members? If seeds never fire at witness
members, the remaining derivation is a selection argument — name
the member choice that avoids the seed — rather than a healing
argument.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves, quotient, the stall
object and the landscape evaluator are the parents'
(explore_scale_clock.py, explore_stall_assembly.py,
explore_stall_maprate.py, explore_shift_telescope.py).
UNRESOURCED throughout: delta inert, 100 policies, N0 = 8 counted
start, quotient by counted trace, cure neighbors, lexicographic
deficit. Identity map except the sq contrast leg.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
LEMMA D (THE DIVERGENCE TRICHOTOMY — any map, any stream). Fix
(st, ss, pc) and compare X = (st, ss, pt, pc) with its
tree-patience-down Y = (st, ss, pt', pc), pt' < pt. Y's tree
reference at step n is J[n - pt'], a subset of X's J[n - pt]
whenever both exist, and Y's exists whenever X's does (images
strictly nest). At any commit-loop micro-step where the two runs
sit at the SAME cell:
  (i)  the chain candidates are IDENTICAL — same chain reference,
       same cell, same chain_kmax;
  (ii) any tree door X holds, Y holds, and it is the SAME door: a
       child strictly containing X's reference strictly contains
       Y's, and at most one child contains a given interval (the
       left child needs the interval strictly below the two
       children's shared endpoint, the right strictly above —
       exclusive).
So Y's menu is X's plus at most one FRESHER-ONLY DOOR (present
exactly when X's reference straddles the cell's mediant or X's
reference does not yet exist, while Y's fits one side), and the
first differing choice has exactly two shapes:
  (a) NESTED DESCENT — X halts on an empty menu and commits; Y
      takes the fresher-only door and descends properly inside
      X's committed cell.
  (b) THE SEED — the cell prefers tree (st = 0 at a tree cell,
      ss = 1 at a straddle cell), X is doorless with a LIVE chain
      candidate and takes it, Y takes the fresher-only door: X
      commits into the straddle chain at the very mediant Y's
      door just stepped past, and the two committed cells can
      overlap without nesting.
Every other combination keeps the choices equal: if X holds a
door, Y holds the same door and the shared preference bit picks
the same slot; if neither holds a door the menus coincide. PROOF
mechanical from (i)-(ii) and the loop's selection rule (chain is
taken iff a chain candidate exists and (no door or the cell
prefers chain)).
WHAT THE TRICHOTOMY DOES NOT GOVERN: steps that START from
unequal cells. After (a) the pair is nested and the two loops run
from different cells; whether non-nesting can arise from a NESTED
start without any seed — NESTED DRIFT — is a question the
instrumentation must answer, not the paper.
TOOL (the tree-cell invariant, proved on paper beside the shift
telescope): every tree-type cell a run commits strictly contains
the then-current tree reference, hence all later ones; a tree
cell refusing both children means the tree reference straddles
its mediant. Used to read anatomies; not load-bearing for the
tallies.

PREDICTIONS, fixed before the engine ran
----------------------------------------
S1 [gate] The lockstep walk replicates the engine: over the three
   anchor worlds x id/dbl/sq x all four style pairs x pt in
   {1,2,3,INF} x pc axis, both runs' per-step committed cells
   equal explore_scale_clock.run_reader's, and every first
   divergence from an equal-cell step classifies as (a) or (b) —
   zero UNEXPECTED. A single miss kills the rig (K1).
S2 [gate, the frozen controls] At the id census scope (pools at
   horizons 9/10/12/16): finite pt-down pairs total 44,040 with
   3,225 counted-nesting failures; from-INF pairs total 14,680
   with 0 counted and 508 all-steps failures — the telescope's
   frozen record reproduced from this rig's own walk (K2).
S3 [the entry guess] GUESS, marked as such: a step that ENTERS
   non-nesting (state OVERLAP or INVERTED from a previously
   equal-or-nested state) always starts EQUAL and carries a seed
   event — NESTED DRIFT never occurs at scope. Any drift entry
   prints with its anatomy; it is a finding, not a gate.
S4 [the witness guess — the aimed question] GUESS: seeds never
   fire at witness members. Per off-bottom finite-loss id class,
   every member whose pt-down pair witnesses class-level nesting
   (distinct class, finite smaller loss, counted nesting holds)
   shows ZERO seed events, so each of the 9,147 finite-witness
   classes holds a seed-free finite witness, and the class
   witness sets coincide with the seed-free sets up to in-class
   and loss-tie members. Counterweight: a seed could fire
   pre-window and heal by the counted start, in which case the
   witness read splits AVOIDED from HEALED — both are tallied.
S5 [the bit anatomy] Entailed by Lemma D and read as consistency:
   every seed sits at a tree cell with st = 0 or a straddle cell
   with ss = 1. The informative GUESS: members with
   (st, ss) = (1, 0) — chain-preferring at both cell kinds —
   never fire a seed and never fail counted nesting.
S6 [the healing read] The 508 from-INF all-steps failures all sit
   strictly before the counted window (the frozen record's
   claim): print the last-bad-step histogram and confirm every
   one heals to nested-or-equal by step 8.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 Any S1 miss — a cell mismatch against run_reader or an
   UNEXPECTED divergence class: the walk misreads the engine, the
   rig is dead, no verdicts.
K2 An S2 control total misses the frozen record: the scope or the
   criterion drifted — rig dead.
K3 S1 and S2 hold: every other tally prints as a finding. If S3
   and S4 print clean, the distance-one derivation's remaining
   owes are NAMED: prove nested persistence (drift measured
   absent) and prove the seed-free member exists in every class
   (the selection argument). If S4 breaks, the healed witnesses'
   anatomies are the finding and the derivation is a healing
   argument.

E5 FOLLOW-UP SLATE (frozen after the first full run and before E5
ran; the E2/E3 prints showed (1,0)-bit members fire zero seeds
and zero counted failures, so the selection coverage became the
sharp question)
----------------------------------------------------------------
E5a GUESS: chain-preferring pairs never enter a bad state at ANY
    step — all-steps failures zero for (1,0)-bit pairs, finite
    and from-INF tallied apart.
E5b THE COVERAGE TALLY: per class, the style-bit patterns of the
    members whose pt-down witnesses (out-of-class, finite smaller
    loss, counted nesting). GUESS: most but not all of the 9,401
    classes hold a (1,0)-bit witness; the residue prints with its
    witness-bit anatomies — the named gap any chain-preferring
    selection argument must cover another way.

ENGINE
------
E1 the lockstep battery (S1): anchor worlds, three maps, all
   pairs; per-step cells checked against run_reader for both
   policies.
E2 the pair census (S2, S3, S5, S6): id, census pools at horizons
   9/10/12/16, every policy with pt in {1,2,3,INF}; per pair the
   lockstep walk records seed events (cell kind, step,
   pre-window/counted), state per step (EQUAL/NESTED/INVERTED/
   OVERLAP against closed containment), non-nesting entries with
   their start state and event, first counted failure.
E3 the class read (S4): same loop, landscape evaluated per world
   (explore_stall_assembly.evaluate, id); per off-bottom
   finite-loss class the witness set, the seed-free set, and the
   class category — seed-free finite witness / healed-only
   finite witness / INF-only witness — with anatomies for any
   class lacking a seed-free witness.
E4 the sq contrast: the three stall specimens' stall-class
   members' pt-down pairs, seed events and states printed — the
   map where the law breaks, read by the same instrument.
E5 the selection coverage (E5a-b): the census loop again, per
   class the witness set's style-bit patterns and the (1,0)
   all-steps tally.
Exact big-integer arithmetic for every verdict; ln never enters.
Sequential; estimated run twenty-five to thirty-five minutes (the
two census passes and the per-world evaluate are the drivers);
memory trivial (no BLAS import); exit nonzero on any check
failure.

FINDINGS (F1-F4 entered after the first full run, E1-E4 only;
ALL CHECKS PASS, exit 0, ~17 min)
----------------------------------------------------------------
F1 THE WALK REPLICATES AND THE TRICHOTOMY IS EXHAUSTIVE. 720
   battery pairs (three worlds x three maps): zero cell misses
   against run_reader at every step, zero UNEXPECTED divergence
   classes there and across the full census — every divergence
   from an equal-cell step is a nested descent or a seed, as
   Lemma D states.
F2 THE FROZEN CONTROLS REPRODUCE. Finite pt-down 44,040 pairs
   with 3,225 counted failures (3,696 all-steps); from-INF
   14,680 with 0 counted and 508 all-steps; 9,401 off-bottom
   finite-loss classes; witness kinds 9,147 finite / 254
   INF-only / 0 both / 0 none.
F3 THE SEED IS A PRE-WINDOW PHENOMENON AND NOT THE BREAK
   MECHANISM (S3 falsified). Every seed at census scope fires
   BEFORE the counted window: seed-T 839 + 839 at st = 0,
   seed-S 231 + 231 at ss = 1, zero counted-window seeds under
   id (the bit symmetry — counts equal across the inert other
   bit — says the configurations arise before that bit ever
   acts). Counted failures split 941 with a seed against 2,284
   seedless; 12,623 non-nesting entries carry no seed at entry,
   the printed anatomies all entering from NESTED. NESTED DRIFT
   — ungoverned by the equal-cell trichotomy — is the dominant
   break path, so the distance-one law needs a WINDOW-HEALING
   statement, not a seed-avoidance one.
F4 THE HEALING AND THE SQ CONTRAST. From-INF badness always
   heals by step 5 (last-bad histogram 4: 451, 5: 57), three
   steps before the window opens. S4's guess splits: 8,900
   classes hold a finite witness with zero seed events, 247 hold
   only witnesses that fired a seed — every printed anatomy a
   benign pre-window seed-T whose pair NEVER entered a bad state
   (the seed committed nested, nothing to heal) — and 254 are
   the INF-only classes. Under sq the same instrument shows the
   stall members' badness PERSISTING into the window (both
   census stalls fail at the window's first step; the designed
   stall oscillates, fails at 9, and fires a counted-window seed
   at step 14 — the only one in any printed tally, the id census
   having none anywhere): the id/sq split is the
   window's relation to the bad phase — transient and early
   against recurrent.
F5 THE CHAIN-PREFERRING NESTING LAW, AND ITS PARTIAL COVERAGE
   (E5a confirmed, E5b's residue real and large). (1,0)-bit
   pairs never enter a bad state at ANY step: zero all-steps
   failures across 11,010 finite and 3,670 from-INF pairs — no
   drift, no seed, nesting pointwise everywhere (rule at census
   scope). But the selection it licenses covers 5,774 classes of
   9,401 (5,520 with a finite-pt (1,0) witness, 254 with the
   from-INF one): 3,627 classes hold NO (1,0)-bit witness, their
   witnesses all carrying a prefer-tree bit. The witness
   bit-pattern census: all four bit pairs witness in 3,257
   classes; sole-pattern classes 917 at (0,0), 934 at (0,1),
   1,009 at (1,0), 851 at (1,1); every pattern occurs.

THE VERDICT. The aimed dichotomy dissolves rather than resolves:
under the identity map the divergence seed is REAL BUT BENIGN —
every firing sits before the counted window, none breaks a
witness — and it is NOT the break mechanism, which is nested
drift (F3). What the instrument found instead is a law and a
residue. THE CHAIN-PREFERRING NESTING LAW (rule at scope): a
reader preferring the chain at both cell kinds has its
tree-patience-down run nested pointwise at EVERY step — 14,680
pairs, zero exceptions — and by Lemma D its only equal-cell
divergence is the nested descent, so its paper derivation owes
exactly one statement: nested persistence for chain-preferring
readers (drift measured absent there). (Taken up by
explore_chain_persistence.py: that owe is the IDENTITY MAP'S,
not the commit loop's — the law holds at exhaustive scope under
id and fails abundantly under sq and dbl — and the persistence
argument is now a proved skeleton whose surviving open piece is
the near-side endpoint-equality enumeration.) Selection by that law
settles 5,774 of the 9,401 classes. The residue's 3,627 classes
witness only at bit pairs carrying a tree preference at one or
both cell kinds, where counted nesting holds
because every bad phase (and every seed) sits pre-window: the
distance-one law's remaining owes are therefore NAMED — the
chain-preferring persistence proof, and the pre-window
confinement of the residue witnesses' bad phases.

Run record. TWO runs. The first (E1-E4) exited 0 with no gate
trips; its prints falsified S3 and split S4, the F1-F4 findings
were entered from its output, and the E5 slate was frozen on
those prints before E5 was written. The second run (all legs)
exited 0 with the E1-E4 output byte-identical to the first
(diffed); no E1-E4 prediction, band, or check was touched
between the runs. ~17 min and ~30 min.
"""

import sys
from fractions import Fraction

import explore_scale_clock as SC
import explore_stall_assembly as SA
import explore_stall_maprate as MR

FAILURES = []

def check(name, ok):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, name))
    if not ok:
        FAILURES.append(name)

NEARMISS = (1, 2, 64, 1, 2, 1, 64, 1, 1, 2)
FLAGSHIP = (3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
DESIGNED = (3, 1, 1, 6, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6)

def frac_le(a, b):
    return a[0] * b[1] <= b[0] * a[1]

def state_of(cx, cy):
    """How Y's committed interval sits against X's; closed
    containment at both ends."""
    xlo, xhi = SC.interval(cx)
    ylo, yhi = SC.interval(cy)
    yin = frac_le(xlo, ylo) and frac_le(yhi, xhi)
    xin = frac_le(ylo, xlo) and frac_le(xhi, yhi)
    if yin and xin:
        return "EQUAL"
    if yin:
        return "NESTED"
    if xin:
        return "INVERTED"
    return "OVERLAP"

def commit_step(C, ref_t, ref_c, s_t, s_s):
    """One step's commit loop, the parent's verbatim, each
    micro-decision recorded as (cell, door, chain, took)."""
    records = []
    guard = 0
    while True:
        guard += 1
        if guard > 10 ** 6:
            raise AssertionError("commit loop runaway")
        cand_tree = cand_chain = None
        if C[0] == "T":
            _, l, r, d = C
            v = SC.mediant(l, r)
            if ref_t is not None:
                for ch in (("T", l, v, d + 1), ("T", v, r, d + 1)):
                    if SC.contains(ch, ref_t):
                        cand_tree = ch
                        break
            if ref_c is not None:
                k = SC.chain_kmax(v, l, r, ref_c)
                if k >= 1:
                    cand_chain = ("S", v, l, r, d, k)
            prefer_chain = (s_t == 1)
        else:
            _, v, l, r, d, k = C
            if ref_c is not None:
                k2 = SC.chain_kmax(v, l, r, ref_c)
                if k2 > k:
                    cand_chain = ("S", v, l, r, d, k2)
            if ref_t is not None:
                mL, mR = SC.interval(C)
                for ch in (("T", mL, v, d + k + 1),
                           ("T", v, mR, d + k + 1)):
                    if SC.contains(ch, ref_t):
                        cand_tree = ch
                        break
            prefer_chain = (s_s == 0)
        if cand_tree is None and cand_chain is None:
            records.append((C, None, None, "halt"))
            return C, records
        if cand_chain is not None and (cand_tree is None
                                       or prefer_chain):
            records.append((C, cand_tree, cand_chain, "chain"))
            C = cand_chain
        else:
            records.append((C, cand_tree, cand_chain, "door"))
            C = cand_tree

def classify_divergence(recx, recy, s_t, s_s):
    """First differing micro-action of two equal-start records:
    'descend', 'seed-T', 'seed-S', None (no divergence), or an
    'unexpected*' tag."""
    m = min(len(recx), len(recy))
    for i in range(m):
        cx, dx, chx, tx = recx[i]
        cy, dy, chy, ty = recy[i]
        if cx != cy:
            return "unexpected-cell"
        same = (tx == ty
                and (tx != "door" or dx == dy)
                and (tx != "chain" or chx == chy))
        if same:
            continue
        prefer_tree = (s_t == 0) if cx[0] == "T" else (s_s == 1)
        if tx == "halt" and ty == "door" and dx is None \
                and dy is not None:
            return "descend"
        if tx == "chain" and ty == "door" and dx is None \
                and dy is not None and chx is not None \
                and prefer_tree:
            return "seed-T" if cx[0] == "T" else "seed-S"
        return "unexpected"
    if len(recx) != len(recy):
        return "unexpected-length"
    return None

def run_pair(J_list, pol, horizon):
    """Lockstep run of X = pol and its tree-patience-down Y.
    Returns per-pair instrumentation: events, states, entries,
    failure steps."""
    st, ss, pt, pc = pol
    ptd = 3 if pt is None else pt - 1
    Cx = Cy = SC.ROOT
    events = []      # (step, kind)
    states = []
    ivals = []       # ((xlo, xhi), (ylo, yhi)) per step
    entries = []     # (step, prev_state, event_kind_or_None)
    first_cfail = None
    last_bad = None
    prev = "EQUAL"
    for n in range(horizon):
        rtx = J_list[n - pt] if pt is not None and n - pt >= 0 \
            else None
        rty = J_list[n - ptd] if n - ptd >= 0 else None
        rc = J_list[n - pc] if pc is not None and n - pc >= 0 \
            else None
        equal_start = (Cx == Cy)
        Cx, recx = commit_step(Cx, rtx, rc, st, ss)
        Cy, recy = commit_step(Cy, rty, rc, st, ss)
        ev = None
        if equal_start:
            ev = classify_divergence(recx, recy, st, ss)
            if ev is not None:
                events.append((n, ev))
        s = state_of(Cx, Cy)
        states.append(s)
        ivals.append((SC.interval(Cx), SC.interval(Cy)))
        bad = s in ("INVERTED", "OVERLAP")
        if bad:
            last_bad = n
            if prev not in ("INVERTED", "OVERLAP"):
                entries.append((n, prev, ev))
            if n >= SC.N0 and first_cfail is None:
                first_cfail = n
        prev = s
    return {"events": events, "states": states, "ivals": ivals,
            "entries": entries, "first_cfail": first_cfail,
            "last_bad": last_bad, "Cx": Cx, "Cy": Cy}

def ptdown5(p5):
    st, ss, pt, pc, d = p5
    return (st, ss, 3 if pt is None else pt - 1, pc, d)

# ----------------------------------------------------------------- #
# E1: the lockstep battery
# ----------------------------------------------------------------- #

ANCHORS = (("near-miss", NEARMISS, 10),
            ("flagship", FLAGSHIP, 12),
            ("designed", DESIGNED, 16))

def pair_pols():
    return [p for p in SC.policy_space4(SC.AX_BASE)
            if p[2] is None or p[2] in (1, 2, 3)]

def e1_battery():
    print("\nE1  THE LOCKSTEP BATTERY (walk vs run_reader, "
          "trichotomy)")
    pairs = cell_miss = unexpected = 0
    for wname, digs, horizon in ANCHORS:
        cyls = SC.cylinders(list(digs))
        for mp in ("id", "dbl", "sq"):
            J = SC.images(cyls, mp)[:horizon]
            for pol in pair_pols():
                st, ss, pt, pc = pol
                ptd = 3 if pt is None else pt - 1
                pd = run_pair(J, pol, horizon)
                pairs += 1
                trx = SC.run_reader(J, pol, horizon)[3]
                trd = SC.run_reader(J, (st, ss, ptd, pc),
                                    horizon)[3]
                # the walk's committed intervals must match the
                # engine's at every step, both policies
                if any(pd["ivals"][n] != (trx[n][2], trd[n][2])
                       for n in range(horizon)):
                    cell_miss += 1
                    print("  CELL MISS %s %s %s"
                          % (wname, mp, str(pol)))
                for _n, k in pd["events"]:
                    if k.startswith("unexpected"):
                        unexpected += 1
                        print("  UNEXPECTED %s %s %s step %d: %s"
                              % (wname, mp, str(pol), _n, k))
    check("battery: %d pairs, zero cell misses" % pairs,
          cell_miss == 0)
    check("battery: zero UNEXPECTED divergence classes",
          unexpected == 0)

# ----------------------------------------------------------------- #
# E2 + E3: the pair census and the class read (id)
# ----------------------------------------------------------------- #

CENSUS_HORIZONS = (9, 10, 12, 16)

def e2_e3_census():
    print("\nE2/E3  THE PAIR CENSUS AND THE CLASS READ (id, "
          "horizons %s)"
          % ",".join(str(h) for h in CENSUS_HORIZONS))
    tal = {"fin": [0, 0, 0], "inf": [0, 0, 0]}
    seed_hist = {}
    drift_entries = []
    seedless_entries = []
    cfail_with_seed = cfail_seedless = 0
    inf_heal = {}
    inf_heal_late = []
    bits10_seed = bits10_cfail = 0
    cats = {"seedfree-fin": 0, "healed-fin": 0, "inf-only": 0,
            "none": 0, "both-kinds": 0}
    wit_fin_only = wit_inf_only = wit_both = wit_none = 0
    healed_anatomies = []
    nclasses = 0
    unexpected = 0
    for horizon in CENSUS_HORIZONS:
        pool = MR.census_pool(horizon)
        for wname, digs in pool:
            J = SC.images(SC.cylinders(list(digs)), "id")[:horizon]
            pairdata = {}
            for pol in pair_pols():
                pd = run_pair(J, pol, horizon)
                pairdata[pol] = pd
                key = "inf" if pol[2] is None else "fin"
                t = tal[key]
                t[0] += 1
                cfail = pd["first_cfail"] is not None
                afail = pd["last_bad"] is not None
                t[1] += cfail
                t[2] += afail
                nseed = 0
                for n, k in pd["events"]:
                    if k.startswith("unexpected"):
                        unexpected += 1
                        continue
                    if k.startswith("seed"):
                        nseed += 1
                        hk = (k, pol[0], pol[1],
                              "pre" if n < SC.N0 else "counted")
                        seed_hist[hk] = seed_hist.get(hk, 0) + 1
                for n, prevs, ev in pd["entries"]:
                    if prevs == "NESTED" or (
                            prevs == "EQUAL"
                            and (ev is None
                                 or not ev.startswith("seed"))):
                        if len(drift_entries) < 8:
                            drift_entries.append(
                                (wname, horizon, pol, n, prevs,
                                 ev))
                        seedless_entries.append(1)
                if cfail:
                    if nseed:
                        cfail_with_seed += 1
                    else:
                        cfail_seedless += 1
                if pol[:2] == (1, 0):
                    bits10_seed += (nseed > 0)
                    bits10_cfail += cfail
                if key == "inf" and afail and not cfail:
                    lb = pd["last_bad"]
                    inf_heal[lb] = inf_heal.get(lb, 0) + 1
                    if lb >= SC.N0:
                        inf_heal_late.append((wname, horizon,
                                              pol, lb))
                pd["nseed"] = nseed
            ev = SA.evaluate(list(digs), "id", horizon)
            sig_of = {p: s for s, ps in ev["mem"].items()
                      for p in ps}
            qloss = ev["qloss"]
            for s in ev["marg"]:
                nclasses += 1
                Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
                fin_wit, fin_seedfree_wit, inf_wit = [], [], []
                for m5 in ev["mem"][s]:
                    pol = m5[:4]
                    if pol not in pairdata:
                        continue
                    q5 = ptdown5(m5)
                    t = sig_of[q5]
                    if t == s or qloss[t][1][2]:
                        continue
                    Lt = Fraction(qloss[t][1][0], qloss[t][1][1])
                    pd = pairdata[pol]
                    wit = (Lt < Lx
                           and pd["first_cfail"] is None)
                    if not wit:
                        continue
                    if pol[2] is None:
                        inf_wit.append(m5)
                    else:
                        fin_wit.append(m5)
                        if pd["nseed"] == 0:
                            fin_seedfree_wit.append(m5)
                if fin_wit and inf_wit:
                    wit_both += 1
                elif fin_wit:
                    wit_fin_only += 1
                elif inf_wit:
                    wit_inf_only += 1
                else:
                    wit_none += 1
                if fin_wit:
                    if fin_seedfree_wit:
                        cats["seedfree-fin"] += 1
                    else:
                        cats["healed-fin"] += 1
                        if len(healed_anatomies) < 8:
                            m5 = fin_wit[0]
                            pd = pairdata[m5[:4]]
                            healed_anatomies.append(
                                (wname, horizon, m5,
                                 pd["events"], pd["last_bad"]))
                elif inf_wit:
                    cats["inf-only"] += 1
                else:
                    cats["none"] += 1
        print("  h=%-2d done (classes so far %d)"
              % (horizon, nclasses))
    print("  finite pt-down: %d pairs, counted fails %d, "
          "all-steps fails %d" % tuple(tal["fin"]))
    print("  from-INF pt-down: %d pairs, counted fails %d, "
          "all-steps fails %d" % tuple(tal["inf"]))
    print("  seed histogram ((kind, st, ss, window): count):")
    for hk in sorted(seed_hist):
        print("    %s: %d" % (str(hk), seed_hist[hk]))
    print("  counted failures: %d with a seed, %d seedless"
          % (cfail_with_seed, cfail_seedless))
    print("  non-nesting entries without a seed from EQUAL "
          "(drift or seedless): %d" % len(seedless_entries))
    for w, h, pol, n, prevs, evk in drift_entries:
        print("    ENTRY %s h=%d %s step %d from %s event %s"
              % (w, h, str(pol), n, prevs, evk))
    print("  (1,0)-bit members: %d fired seeds, %d counted fails"
          % (bits10_seed, bits10_cfail))
    print("  from-INF healing (last bad step: count): %s"
          % dict(sorted(inf_heal.items())))
    for w, h, pol, lb in inf_heal_late[:8]:
        print("    LATE HEAL %s h=%d %s last bad %d"
              % (w, h, str(pol), lb))
    print("  class witness kinds: fin-only %d, inf-only %d, "
          "both %d, none %d (of %d)"
          % (wit_fin_only, wit_inf_only, wit_both, wit_none,
             nclasses))
    print("  class categories: %s" % cats)
    for w, h, m5, evs, lb in healed_anatomies:
        print("    HEALED-ONLY %s h=%d %s events %s last bad %s"
              % (w, h, SC.fmt_pol5(m5), evs, lb))
    check("zero UNEXPECTED divergence classes at census scope",
          unexpected == 0)
    check("finite pairs reproduce 44,040 (%d)" % tal["fin"][0],
          tal["fin"][0] == 44040)
    check("finite counted fails reproduce 3,225 (%d)"
          % tal["fin"][1], tal["fin"][1] == 3225)
    check("from-INF pairs reproduce 14,680 (%d)" % tal["inf"][0],
          tal["inf"][0] == 14680)
    check("from-INF counted fails reproduce 0 (%d)"
          % tal["inf"][1], tal["inf"][1] == 0)
    check("from-INF all-steps fails reproduce 508 (%d)"
          % tal["inf"][2], tal["inf"][2] == 508)
    check("class total reproduces 9,401 (%d)" % nclasses,
          nclasses == 9401)
    check("witness kinds reproduce 9,147 fin / 254 inf-only / "
          "0 both / 0 none (%d/%d/%d/%d)"
          % (wit_fin_only, wit_inf_only, wit_both, wit_none),
          (wit_fin_only, wit_inf_only, wit_both, wit_none)
          == (9147, 254, 0, 0))

# ----------------------------------------------------------------- #
# E4: the sq contrast
# ----------------------------------------------------------------- #

SQ_SPECIMENS = (
    ("census-2313..", (2, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3), 12),
    ("census-3212..", FLAGSHIP, 12),
    ("designed-16", DESIGNED, 16),
)

def e4_sq():
    print("\nE4  THE SQ CONTRAST (stall-class members' pt-down "
          "pairs)")
    for tag, digs, horizon in SQ_SPECIMENS:
        ev = SA.evaluate(list(digs), "sq", horizon)
        check("%s reproduces as a stall" % tag,
              bool(ev["stalls"]))
        J = ev["J"]
        for s in ev["stalls"]:
            for m5 in ev["mem"][s]:
                pol = m5[:4]
                if not (pol[2] is None or pol[2] in (1, 2, 3)):
                    continue
                pd = run_pair(J, pol, horizon)
                print("  %s stall member %s: events %s, first "
                      "counted fail %s, states %s"
                      % (tag, SC.fmt_pol5(m5), pd["events"],
                         pd["first_cfail"],
                         " ".join(x[0] for x in pd["states"])))

# ----------------------------------------------------------------- #
# E5: the selection coverage (id)
# ----------------------------------------------------------------- #

def e5_selection():
    print("\nE5  THE SELECTION COVERAGE (witness bits per class, "
          "id)")
    bad10 = {"fin": [0, 0], "inf": [0, 0]}   # pairs, all-steps bad
    patt = {}
    has10 = {"fin": 0, "inf": 0, "none": 0}
    residue = []
    nclasses = 0
    for horizon in CENSUS_HORIZONS:
        pool = MR.census_pool(horizon)
        for wname, digs in pool:
            J = SC.images(SC.cylinders(list(digs)), "id")[:horizon]
            pairdata = {}
            for pol in pair_pols():
                pd = run_pair(J, pol, horizon)
                pairdata[pol] = pd
                if pol[:2] == (1, 0):
                    key = "inf" if pol[2] is None else "fin"
                    bad10[key][0] += 1
                    bad10[key][1] += pd["last_bad"] is not None
            ev = SA.evaluate(list(digs), "id", horizon)
            sig_of = {p: s for s, ps in ev["mem"].items()
                      for p in ps}
            qloss = ev["qloss"]
            for s in ev["marg"]:
                nclasses += 1
                Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
                bits = set()
                fin10 = inf10 = False
                for m5 in ev["mem"][s]:
                    pol = m5[:4]
                    if pol not in pairdata:
                        continue
                    q5 = ptdown5(m5)
                    t = sig_of[q5]
                    if t == s or qloss[t][1][2]:
                        continue
                    Lt = Fraction(qloss[t][1][0], qloss[t][1][1])
                    if Lt < Lx and \
                            pairdata[pol]["first_cfail"] is None:
                        bits.add(pol[:2])
                        if pol[:2] == (1, 0):
                            if pol[2] is None:
                                inf10 = True
                            else:
                                fin10 = True
                bk = tuple(sorted(bits))
                patt[bk] = patt.get(bk, 0) + 1
                if fin10:
                    has10["fin"] += 1
                elif inf10:
                    has10["inf"] += 1
                else:
                    has10["none"] += 1
                    if len(residue) < 12:
                        residue.append(
                            (wname, horizon,
                             SC.summarize_class(ev["mem"][s]),
                             bk))
        print("  h=%-2d done (classes so far %d)"
              % (horizon, nclasses))
    print("  (1,0) finite pairs: %d, all-steps bad %d"
          % tuple(bad10["fin"]))
    print("  (1,0) from-INF pairs: %d, all-steps bad %d"
          % tuple(bad10["inf"]))
    print("  witness bit-pattern census (sorted bit set: "
          "classes):")
    for bk in sorted(patt):
        print("    %s: %d" % (str(bk), patt[bk]))
    print("  (1,0) witness coverage: finite %d, from-INF-only "
          "%d, none %d (of %d)"
          % (has10["fin"], has10["inf"], has10["none"], nclasses))
    for w, h, cls, bk in residue:
        print("    RESIDUE %s h=%d %s witness bits %s"
              % (w, h, cls, str(bk)))
    check("E5 class total reproduces 9,401 (%d)" % nclasses,
          nclasses == 9401)

# ----------------------------------------------------------------- #

def main():
    print("THE SEED EXCLUSION (id, unresourced, exact "
          "arithmetic)")
    e1_battery()
    if FAILURES:
        print("\nRIG DEAD AT E1 (K1): %s" % FAILURES)
        return 1
    e2_e3_census()
    e4_sq()
    e5_selection()
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % FAILURES))
    return 1 if FAILURES else 0

if __name__ == "__main__":
    sys.exit(main())
