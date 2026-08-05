"""THE ASSEMBLY QUESTION: can a world deny a trade's late winner
every improving move?

THE QUESTION
------------
The decision-trade census (explore_decision_trade.py) proved the
ingredient abundant: unresourced, about one divergent cure edge in
thirteen is a TRADE — the first differing counted step and the
total deficit point opposite ways — yet the stall census at
overlapping scope (explore_stall_unresourced.py) found ZERO stalls
in 348 distinct worlds: every trade's late winner off the bottom
still has a strictly improving move elsewhere in its neighborhood.
The open edge is the ASSEMBLY: can a world be DESIGNED that stacks
trades until one policy class beats its whole neighborhood — an
unresourced off-bottom stall — or is the exit forced? This rig
attacks the design route: an adversarial stream search aimed
directly at the stall margin, seeded by a near-stall census of the
existing batteries.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves and quotient are the
parents' (explore_scale_clock.py, explore_stall_tie.py,
explore_stall_unresourced.py): the mediant-straddle cover of the
CF window, policies (s_t, s_s, pt, pc, delta) over the patience
axis {0,1,2,3,INF}, the exact lexicographic deficit over counted
steps (N0 = 8), cure moves (single coordinate steps plus the route
diagonal), the behavioral quotient by counted trace. UNRESOURCED
throughout the open leg: delta inert, 100 policies. A STALL is the
parents' object verbatim: an off-bottom quotient class none of
whose cure neighbors ranks strictly lower; STRICT when every
neighbor is strictly worse. The STALL MARGIN of a finite-loss
off-bottom class is min over cure neighbors of
ln(neighbor total) - ln(class total): positive exactly on a strict
stall, and its distance below zero is how far the class sits from
stalling.

HAND-ATTACK (fixed before the engine; the proofs are the design)
----------------------------------------------------------------
L1 (BOTTOM-ADJACENCY EXCLUSION, proved). No class containing a
   policy at patience (0,1) or (1,0) can stall. Such a class has
   the bottom class as a cure neighbor (one patience-down step),
   and POINTWISE GLOBAL OPTIMALITY (the bottom lemma's corollary,
   explore_bootstrap_cures.py) makes the bottom's committed cell
   the inclusion-minimum cover cell containing the current image —
   weakly shorter than any policy's cell at every counted step, so
   the bottom's total is weakly better by the product. If the
   class's total strictly exceeds the bottom's, the bottom is a
   strictly improving neighbor; if it ties, the class has rank 0
   and is not a stall by definition. Either way: every member of a
   stall class sits at pt + pc >= 2, so the assembly must hold at
   patience depth two or beyond, where the neighborhood has up to
   nine classes to beat.
L2 (THE HORIZON CUT — why the desert does not decide). A trade's
   late win is a TRANSIENT WINDOW: divergence, freeze, re-merge
   (the trade rig's L3 mechanism), and on generic streams the
   profiles re-merge well inside the horizon, so the measured
   totals sample the window's settled aftermath. But a stall needs
   the class to be ahead on EVERY cure edge at the SAME cut, and
   each edge is a SEPARATE pairwise inequality against the common
   class trace — nothing conserved couples the edges, which is
   exactly what the trade rig proved (no budget behind the trade).
   The design freedom the prior batteries never aimed: stagger
   each neighbor's divergence window so the horizon cuts inside
   all of them at once, or after re-merges that each net in the
   class's favor. The zero of the prior census is a desert
   reading over generic streams, not a law over designed ones.
L3 (WHAT THE FORGE CAN AND CANNOT CLOSE). Adversarial local
   search is complete for nothing: a WITNESS closes the question
   (a world can deny the exit), an empty forge at scope is an
   observation — the margin ceiling it reached prints, and the
   question stays open with its adversarial room measured. The
   asymmetry is the design's point: the census route already
   returned its zero, so only the witness direction has a cheap
   close, and the search is aimed there.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls, gate]
   (i)  UNIT: on the parent designed-world battery (both maps,
        horizon 16), the margin detector's stall list computed
        directly from the quotient losses equals the parents'
        qstalls output on every landscape, and both are empty.
   (ii) INTEGRATION: on the budgeted burst-trap landscape
        (spike1@10/dbl, horizon 16, (B, W) = (2, 0)), the detector
        reproduces the parents' known strict stall — a class with
        member sigma = (1, 0), patience (0, 2) — with every
        per-neighbor margin strictly positive.
C2 [THE NEAR-STALL CENSUS — the seeds] Unresourced, horizons 12
   and 16, maps id/dbl/sq, over the full density pool, the aimed
   double-burst battery and the parent battery: per landscape,
   every finite-loss off-bottom class's stall margin and
   improving-neighbor count. GUESS, marked as such: some class
   somewhere hangs by ONE improving neighbor, and the best margin
   lands within 1 ln of zero. (Horizon 12 is NEW scope: the prior
   censuses scanned 16 and up, and a shorter counted window can
   only make holding a lead easier — if the plain census already
   stalls there, that is a finding before any forge runs.)
C3 [THE ADVERSARIAL FORGE — the open observable] From the top
   near-stall seeds per (horizon, map) cell, first-improvement
   hill-climbing on the best stall margin, one digit mutation at a
   time (positions 0..h-1, digits 1..6), stopping at a local
   maximum, a printed stall, or the evaluation budget. GUESS,
   marked as such: a stall prints — the assembly is achievable by
   design, predicted locus a mixed-patience class at pt + pc >= 2
   with the horizon cutting inside staggered divergence windows.
   The 348-world desert weighs the other way; the guess weighs
   L2's horizon-cut freedom over it.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 Any C1 check fails: the rig is dead, no verdicts.
K2 A stall prints unresourced (census or forge): the assembly
   question settles YES — a world CAN deny every improving move —
   and the full anatomy prints (digits, map, horizon, class
   members, per-neighbor margins with first differing counted
   steps, counted length profiles), capped at three specimens.
K3 The forge exhausts at scope with zero stalls: the best margin
   reached prints with its world and class, beside the
   improving-neighbor minimum — the adversarial room measured, the
   question open.

ENGINE
------
E1 controls: the parent-battery equivalence sweep (C1(i)); the
   budgeted burst-trap rediscovery (C1(ii)).
E2 the near-stall census (C2): per battery and cell, margins and
   improving counts; the top seeds per cell carried to E3.
E3 the forge (C3): first-improvement climbs from the seeds under
   one global evaluation budget (20,000 landscapes, logged if
   hit); every specimen's anatomy printed and one hand-verified.
Exact big-integer arithmetic for every verdict (the parents'
comparators); ln only in printed logs. Sequential, one landscape
at a time; estimated run two to six minutes, memory trivial (no
BLAS import); positive controls gate all verdicts; exit nonzero on
any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, ~21 s,
memory trivial)
----------------------------------------------------------------
F1 Controls exact. The 56-landscape parent slice reproduces zero
   stalls with the two stall computations agreeing on every
   landscape (the agreement is asserted inside the evaluator, so
   it held on every landscape this rig ran); the budgeted burst
   trap is rediscovered strict at margin +0.0517 ln.

F2 K2 FIRED IN THE CENSUS, BEFORE THE FORGE RAN: the unresourced
   cell is NOT stall-free as a class. 2 of 1,014 unresourced
   census landscapes carry a strict off-bottom stall — both plain
   short-period worlds under the sq map at horizon 12: digits
   231313131313 and 321212121212, stall class in each the single
   policy sigma = (1, 0), patience (3, 0). The prior censuses'
   zero over 348 worlds was a property of their scanned horizons
   (16 and up), not of the cell.

F3 THE FLAGSHIP, hand-verified (321212121212 / sq / horizon 12).
   The stall loses the first counted step to every finite
   neighbor and wins every total: margins +0.4775 ln against the
   patience-(2,0) class, +4.7307 against (3,0), +4.7601 against
   (3,1), +INF against the refuser. Hand-summed from the printed
   profiles: stall ln total ln(7/12 * 1/228 * (5/63954)^2)
   = -24.88 against the nearest neighbor's -24.40, difference
   +0.48 ln = the printed margin. Every finite edge is a TRADE
   with the stall at the late-winner end, and the assembly needed
   no stagger: ONE deep window — pay at step 8, collect at steps
   9 through 11 — holds against the whole neighborhood at once.

F4 THE HORIZON WINDOW — the cut mechanism confirmed. Both census
   stall worlds stall at horizons 11 and 12 ONLY: best margins
   negative at horizons 9 and 10 (-0.25 to -0.59), positive
   inside the window (+0.18 to +0.48), and negative from 13 on,
   collapsing to -3.87 and -1.21 by horizon 16. The stall exists
   exactly while the horizon cuts inside the trade window; a
   longer count lets the neighbors' re-merge repay the divergence
   and the stall dissolves.

F5 THE DESIGNED STALL AT THE SCANNED SCOPE. At horizon 16 under
   sq — where this rig's own 177-world census is stall-free — the
   climb from the all-1 seed (head 3) reaches a strict stall on
   the scan after four accepted mutations: digits
   3116131111111116, three bursts staggered against an all-1
   base (6 at step 3, 3 at step 5, 6 at step 15 — the last inside
   the counted window at the cut), stall class the single policy
   sigma = (0, 1), patience (2, 0), margins +0.2839 to +12.5761
   over five finite neighbor classes (hand-check: stall ln total
   -82.87 against the nearest neighbor's -82.58). Exactly one of
   its five edges is a trade — the patience-down class wins the
   first counted step by 1/114 against 1/106 and loses the total —
   and the stall wins the other four at their first differing
   step (cross-multiplied from the printed profiles), so the
   designed stall holds one late win and beats the rest outright,
   where the horizon-12 flagship holds every finite edge as a
   trade. So
   stall-freeness at ANY horizon is a battery property, not a
   cell property. The id and dbl cells' climbs all end at
   negative local maxima (best -0.7388 ln at horizon 12, -1.0997
   at 16): at this scope only the sq map's squared shrink rate
   amplifies a late collection deep enough to hold a whole
   neighborhood — an observation, not a wall.

F6 THE CURE SURVIVES. Every specimen — both census stalls and the
   designed one — has escape radius exactly 2 through the cure
   quotient graph, extending the corpus's radius-2 reading to the
   new species: two-move lookahead cures every finite-loss stall
   found to date, this rig's included.

THE VERDICT. The assembly question closes YES — a world CAN deny
a trade's late winner every improving move: rule (existence by
exact-arithmetic witnesses, one hand-verified at each horizon).
Unresourced strict off-bottom stalls exist in the named class
with no budget anywhere in the mechanism: in plain period-2
worlds under sq at horizons 11-12, and at the previously scanned
horizon 16 by three designed bursts. What survives of the desert:
stall-freeness is a property of the battery (generic streams,
long counts, slow maps), the escape radius stays 2, and the
mechanism is the horizon cut over the decision trade's transient
window.

Run record. The first run (E1-E3) exited 0 in ~15 s: the census
found the two horizon-12 stalls and the forge stopped at its
specimen cap without reaching the horizon-16 cells. Three
post-run engine extensions, no prediction band touched: E4
(horizon persistence) added because the census had already fired;
the forge changed to move to the next cell on a stall so the
horizon-16 cells ran (finding the designed stall); E5 (escape
radius) added once specimens existed. Final run ~21 s, 5,922 of
20,000 forge evaluations spent, ALL CHECKS PASS, exit 0.
"""

import sys

import explore_scale_clock as SC
import explore_stall_tie as ST
import explore_stall_unresourced as SU

FAILURES = []

def check(name, ok):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, name))
    if not ok:
        FAILURES.append(name)

# ----------------------------------------------------------------- #
# the margin detector
# ----------------------------------------------------------------- #

INF_LN = float("inf")

def stalls_direct(mem, nbrs, qloss):
    """The parents' stall object recomputed straight from the
    quotient losses (no rank map): off-bottom (some class anywhere
    is strictly better) with no strictly better cure neighbor."""
    out = []
    for s in mem:
        if not any(SC.cmp_comp(qloss[u], qloss[s]) < 0 for u in mem):
            continue
        if any(SC.cmp_comp(qloss[t], qloss[s]) < 0 for t in nbrs[s]):
            continue
        out.append(s)
    return set(out)

def margin_table(mem, nbrs, qloss, qranks):
    """Per finite-loss off-bottom class s:
      (margin_ln, improving, strict)
    margin_ln  min over cure neighbors t of lnL(t) - lnL(s)
               (an infinite-loss neighbor contributes +inf)
    improving  count of strictly better neighbors
    strict     True iff every neighbor is strictly worse."""
    out = {}
    for s in mem:
        if qranks[s] == 0 or qloss[s][1][2]:
            continue
        ls = SC.ln_loss(qloss[s][1])
        m, imp, strict = None, 0, True
        for t in nbrs[s]:
            c = SC.cmp_lex(qloss[t][1], qloss[s][1])
            if c < 0:
                imp += 1
            if c <= 0:
                strict = False
            d = INF_LN if qloss[t][1][2] \
                else SC.ln_loss(qloss[t][1]) - ls
            m = d if m is None else min(m, d)
        out[s] = (m, imp, strict)
    return out

# ----------------------------------------------------------------- #
# one landscape, one evaluation
# ----------------------------------------------------------------- #

def evaluate(digs, mp, horizon):
    """Full unresourced quotient landscape of one designed stream.
    Returns a dict with the census tuple, the margin table, the
    parents' stalls (both computations), and the best margin."""
    J = SC.images(SC.cylinders(list(digs)), mp)[:horizon]
    mem, nbrs, qloss, qranks, stalls, ties, cbs = \
        SU.landscape(J, horizon)
    direct = stalls_direct(mem, nbrs, qloss)
    assert direct == set(stalls), "stall detectors disagree"
    marg = margin_table(mem, nbrs, qloss, qranks)
    best = None
    for s, (m, imp, strict) in marg.items():
        if best is None or m > marg[best][0]:
            best = s
    return {"J": J, "mem": mem, "nbrs": nbrs, "qloss": qloss,
            "qranks": qranks, "stalls": stalls, "ties": ties,
            "marg": marg, "best": best,
            "best_m": marg[best][0] if best is not None else None}

def anatomy(tag, digs, mp, horizon, ev, cap_nbrs=12):
    """Print a stall specimen fully enough to hand-verify."""
    print("  %s: digits %s  map %s  horizon %d"
          % (tag, "".join(str(d) for d in digs), mp, horizon))
    for s in ev["stalls"]:
        mem, nbrs, qloss = ev["mem"], ev["nbrs"], ev["qloss"]
        reps = sorted(mem[s], key=SC.pol_key)
        print("    stall class %s" % SC.summarize_class(mem[s]))
        ls = None if qloss[s][1][2] else SC.ln_loss(qloss[s][1])
        rows = [("STALL", s, reps[0], 0.0)]
        for t in sorted(nbrs[s], key=lambda t: ev["qranks"][t]):
            d = INF_LN if qloss[t][1][2] \
                else SC.ln_loss(qloss[t][1]) - ls
            rows.append(("nbr", t, sorted(mem[t], key=SC.pol_key)[0],
                         d))
        for tag2, sig, p, d in rows[:cap_nbrs + 1]:
            tr = SC.run_reader(ev["J"], p[:4], horizon)[3]
            cl = []
            for n in range(SC.N0, horizon):
                lo, hi = tr[n][2]
                num = hi[0] * lo[1] - lo[0] * hi[1]
                den = lo[1] * hi[1]
                cl.append("%d/%d" % (num, den))
            print("      %-5s %s  margin %s"
                  % (tag2, SC.fmt_pol5(p),
                     "+INF" if d == INF_LN else "%+.4f" % d))
            print("        counted lengths: %s" % " ".join(cl))

# ----------------------------------------------------------------- #
# E1: controls
# ----------------------------------------------------------------- #

def e1_controls():
    print("\nE1  CONTROLS")
    n_land = n_stall = 0
    agree = True
    for wname, digs in ST.battery_worlds():
        for mp in ("id", "dbl"):
            ev = evaluate(digs[:16], mp, 16)
            n_land += 1
            n_stall += len(ev["stalls"])
    check("C1(i) parent battery h=16: %d landscapes, detector "
          "agreement on every one, zero stalls" % n_land,
          agree and n_stall == 0)

    digs = [1] * 16
    digs[10] = 8
    J = SC.images(SC.cylinders(digs), "dbl")[:16]
    B, W = 2, 0
    daxis = SC.d_axis(W)
    space = SC.policy_space5(SC.AX_BASE, daxis)
    sigd, lossd, clensd = {}, {}, {}
    for p in space:
        t, sg, cl = ST.run_pol(J, p, B, W, 16)
        sigd[p], lossd[p], clensd[p] = sg, t, cl
    mem, nbrs, qloss, qranks, stalls, ties, cbs = \
        ST.census(space, sigd, lossd, clensd, daxis)
    direct = stalls_direct(mem, nbrs, qloss)
    marg = margin_table(mem, nbrs, qloss, qranks)
    hit = None
    for s in stalls:
        if any(p[:4] == (1, 0, 0, 2) for p in mem[s]):
            hit = s
    ok = (direct == set(stalls) and hit is not None
          and hit in marg and marg[hit][2] and marg[hit][0] > 0)
    if hit is not None and hit in marg:
        print("  burst-trap stall rediscovered: margin %+.4f ln, "
              "%d improving neighbors, strict %s"
              % (marg[hit][0], marg[hit][1], marg[hit][2]))
    check("C1(ii) budgeted burst trap: known strict stall at "
          "sigma=(1,0) patience (0,2), all margins positive", ok)

# ----------------------------------------------------------------- #
# E2: the near-stall census
# ----------------------------------------------------------------- #

CENSUS_HORIZONS = (12, 16)
CENSUS_MAPS = ("id", "dbl", "sq")
SEED_K = 4

def census_pool(horizon):
    pool = []
    seen = set()
    for wname, digs in (SU.density_pool(horizon)
                        + SU.aimed_worlds(horizon)
                        + ST.battery_worlds()):
        key = tuple(digs[:horizon])
        if key in seen or len(digs) < horizon:
            continue
        seen.add(key)
        pool.append((wname, list(key)))
    return pool

def e2_census():
    print("\nE2  THE NEAR-STALL CENSUS (unresourced)")
    seeds = {}
    n_land = 0
    stall_hits = []
    global_best = None
    imp_min = None
    for horizon in CENSUS_HORIZONS:
        pool = census_pool(horizon)
        for mp in CENSUS_MAPS:
            cell = []
            for wname, digs in pool:
                ev = evaluate(digs, mp, horizon)
                n_land += 1
                if ev["stalls"]:
                    stall_hits.append((wname, digs, mp, horizon, ev))
                if ev["best_m"] is not None:
                    cell.append((ev["best_m"], wname, digs))
                    if (global_best is None
                            or ev["best_m"] > global_best[0]):
                        cls = ev["best"]
                        global_best = (ev["best_m"], wname, mp,
                                       horizon,
                                       SC.summarize_class(
                                           ev["mem"][cls]))
                    for s, (m, imp, st) in ev["marg"].items():
                        if imp_min is None or imp < imp_min[0]:
                            imp_min = (imp, wname, mp, horizon,
                                       SC.summarize_class(
                                           ev["mem"][s]))
            cell.sort(key=lambda z: (-z[0], z[1]))
            seeds[(horizon, mp)] = [(w, d) for _m, w, d
                                    in cell[:SEED_K]]
            print("  h=%d %-3s: %d worlds, best margin %+.4f ln "
                  "(%s), seed band %+.4f..%+.4f"
                  % (horizon, mp, len(cell),
                     cell[0][0], cell[0][1],
                     cell[SEED_K - 1][0], cell[0][0]))
    print("  landscapes %d | census stalls %d" %
          (n_land, len(stall_hits)))
    if global_best is not None:
        print("  nearest to stalling anywhere: margin %+.4f ln at "
              "%s/%s h=%d, class %s" % global_best)
    if imp_min is not None:
        print("  fewest improving neighbors anywhere: %d at "
              "%s/%s h=%d, class %s" % imp_min)
    return seeds, stall_hits

# ----------------------------------------------------------------- #
# E3: the adversarial forge
# ----------------------------------------------------------------- #

EVAL_CAP = 20000
MAX_ACCEPTS = 60
FORGE_DIGITS = (1, 2, 3, 4, 5, 6)

def climb(digs0, mp, horizon, budget):
    """First-improvement hill-climb on the best stall margin.
    Returns (best_margin, digs, ev_or_None_specimen, accepts)."""
    cur = list(digs0)
    ev = evaluate(cur, mp, horizon)
    budget[0] -= 1
    if ev["stalls"]:
        return ev["best_m"], cur, ev, 0
    accepts = 0
    while accepts < MAX_ACCEPTS and budget[0] > 0:
        improved = False
        for pos in range(horizon):
            for d in FORGE_DIGITS:
                if d == cur[pos]:
                    continue
                cand = cur[:]
                cand[pos] = d
                ev2 = evaluate(cand, mp, horizon)
                budget[0] -= 1
                if ev2["stalls"]:
                    return ev2["best_m"], cand, ev2, accepts
                if (ev2["best_m"] is not None
                        and (ev["best_m"] is None
                             or ev2["best_m"] > ev["best_m"])):
                    cur, ev = cand, ev2
                    improved = True
                    break
                if budget[0] <= 0:
                    break
            if improved or budget[0] <= 0:
                break
        if not improved:
            break
        accepts += 1
    return ev["best_m"], cur, None, accepts

def e3_forge(seeds):
    print("\nE3  THE ADVERSARIAL FORGE")
    budget = [EVAL_CAP]
    specimens = []
    best_overall = None
    for (horizon, mp), cell in sorted(seeds.items()):
        for wname, digs in cell:
            if budget[0] <= 0:
                break
            m, d, spec, acc = climb(digs, mp, horizon, budget)
            tag = "seed %s/%s h=%d" % (wname, mp, horizon)
            if spec is not None:
                specimens.append((d, mp, horizon, spec))
                print("  %s: STALL after %d accepts" % (tag, acc))
                break  # next cell: this cell's question is answered
            print("  %s: local max margin %+.4f ln after %d accepts"
                  % (tag, m, acc))
            if m is not None and (best_overall is None
                                  or m > best_overall[0]):
                best_overall = (m, d, mp, horizon, wname)
        if budget[0] <= 0:
            break
    if budget[0] <= 0:
        print("  NOTE: evaluation budget (%d) exhausted — climbs "
              "beyond it were dropped" % EVAL_CAP)
    print("  evaluations spent %d of %d" %
          (EVAL_CAP - budget[0], EVAL_CAP))
    return specimens, best_overall

# ----------------------------------------------------------------- #
# E4: horizon persistence (added after the first run, no prediction
# band touched: the census leg itself returned stalls at horizon 12,
# so the horizon dial becomes a measured observable — each distinct
# stall world, extended by its tail period, swept over horizons
# 9..16)
# ----------------------------------------------------------------- #

E4_CAP = 12

def e4_persistence(census_stalls):
    print("\nE4  HORIZON PERSISTENCE of the census stalls "
          "(stall count per horizon, best margin in ln)")
    seen = set()
    for wname, digs, mp, horizon, _ev in census_stalls:
        key = (tuple(digs), mp)
        if key in seen:
            continue
        if len(seen) >= E4_CAP:
            print("  NOTE: %d further stall worlds not swept (cap %d)"
                  % (len(census_stalls) - len(seen), E4_CAP))
            break
        seen.add(key)
        row = []
        for h in range(9, 17):
            d = list(digs)
            while len(d) < h:
                d.append(d[len(d) - 2])
            ev = evaluate(d[:h], mp, h)
            row.append("h%d:%d%s" % (h, len(ev["stalls"]),
                       "" if ev["best_m"] is None else
                       "(%+.2f)" % ev["best_m"]))
        print("  %s/%s: %s" % (wname, mp, " ".join(row)))

# ----------------------------------------------------------------- #
# E5: escape radius (added after the run found specimens, no
# prediction band touched: the corpus's standing claim — every
# finite-loss stall found to date has escape radius exactly 2
# through the cure graph — is measured on the new species)
# ----------------------------------------------------------------- #

def escape_radius(s0, nbrs, qloss, cap=4):
    """Minimum number of cure moves through the quotient graph from
    s0 to a class with strictly better loss; None if none within
    cap."""
    seen = {s0}
    front = [s0]
    for d in range(1, cap + 1):
        nxt = []
        for s in front:
            for t in nbrs[s]:
                if t in seen:
                    continue
                if SC.cmp_comp(qloss[t], qloss[s0]) < 0:
                    return d
                seen.add(t)
                nxt.append(t)
        front = nxt
    return None

def e5_radius(census_stalls, specimens):
    print("\nE5  ESCAPE RADIUS of every specimen (cap 4)")
    seen = set()
    pool = [(w, d, mp, h, ev) for w, d, mp, h, ev in census_stalls]
    pool += [("forged", d, mp, h, ev) for d, mp, h, ev in specimens]
    for wname, digs, mp, horizon, ev in pool:
        key = (tuple(digs), mp, horizon)
        if key in seen:
            continue
        seen.add(key)
        for s in ev["stalls"]:
            r = escape_radius(s, ev["nbrs"], ev["qloss"])
            print("  %s/%s h=%d class %s: radius %s"
                  % (wname, mp, horizon,
                     SC.summarize_class(ev["mem"][s]),
                     "NONE<=4" if r is None else str(r)))

# ----------------------------------------------------------------- #

def main():
    print("THE ASSEMBLY QUESTION: can a designed world stall?")
    print("=" * 70)
    e1_controls()
    if FAILURES:
        print("\nCONTROLS FAILED — no verdicts.")
        sys.exit(1)
    seeds, census_stalls = e2_census()
    for wname, digs, mp, horizon, ev in census_stalls[:3]:
        anatomy("CENSUS SPECIMEN (%s)" % wname, digs, mp, horizon, ev)
    e4_persistence(census_stalls)
    specimens, best_overall = e3_forge(seeds)
    e5_radius(census_stalls, specimens)
    print("\nVERDICT OBSERVABLES")
    if census_stalls or specimens:
        print("  K2: an unresourced stall exists — specimens below.")
        if best_overall is not None:
            print("  best margin among stall-free forge cells: "
                  "%+.4f ln at map %s h=%d (from seed %s)"
                  % (best_overall[0], best_overall[2],
                     best_overall[3], best_overall[4]))
        shown = set()
        for digs, mp, horizon, ev in specimens:
            key = (tuple(digs), mp, horizon)
            if key in shown or len(shown) >= 3:
                continue
            shown.add(key)
            anatomy("FORGE SPECIMEN", digs, mp, horizon, ev)
    else:
        print("  K3: zero stalls at scope.")
        if best_overall is not None:
            print("  best forge margin %+.4f ln at digits %s map %s "
                  "h=%d (from seed %s)"
                  % (best_overall[0],
                     "".join(str(x) for x in best_overall[1]),
                     best_overall[2], best_overall[3],
                     best_overall[4]))
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % FAILURES))
    sys.exit(1 if FAILURES else 0)

if __name__ == "__main__":
    main()
