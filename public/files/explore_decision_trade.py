"""THE DECISION TRADE: can a preference alone buy late gain with
early loss?

THE QUESTION
------------
The reader-descent corpus's stall census leaves one species open
(explore_stall_unresourced.py): unresourced, every off-spine stall
must sit behind an available preference decision — necessary, not
sufficient — and the whole open edge is whether a preference
decision ALONE, with no conserved budget behind it, can buy a late
gain with an early loss. The budgeted burst trap runs on exactly
that trade, financed by a conserved quantity: spending early
removes capacity late. Unresourced, nothing is conserved; the only
cross-step channel is the ratchet's POSITION. This rig hunts the
trade itself, directly, rather than the stalls it would assemble
into.

THE OBSERVABLE (the species in one shape)
-----------------------------------------
A TRADE is an unordered pair of policies adjacent in the cure
graph, both finite-loss, whose counted length profiles differ,
where the policy STRICTLY WORSE at the FIRST differing counted
step has the STRICTLY BETTER total lex deficit. That is "early
loss, late gain" verbatim: the divergence's opening move goes one
way and the product ends the other. The budgeted burst trap's own
dissected anatomy (explore_stall_tie.py, spike1@10/dbl, horizon
16, (B, W) = (2, 0)) IS this shape — the stall class is worse at
counted step 9 (cross-multiplication 1786 vs 1785) and better in
total by 0.0517 ln against its chain-patience-down neighbor — so
the detector has a known positive instance under a budget, and the
species question is whether it can EVER fire with the budget
removed.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves and quotient are the
parents' (explore_scale_clock.py, explore_stall_tie.py): the
mediant-straddle cover of the CF window, policies
(s_t, s_s, pt, pc, delta) over the patience axis {0,1,2,3,INF},
the exact lexicographic deficit over counted steps (N0 = 8), the
cure move set (single coordinate steps plus the route diagonal).
UNRESOURCED throughout the open leg: delta inert, 100 policies,
64 of them finite-patience; pairs with an infinite-loss endpoint
are excluded (the refuser is the signal cure's customer, not this
species').

HAND-ATTACK (fixed before the engine; the proofs are the design)
----------------------------------------------------------------
L1 (WHY A DECISION IS THE ONLY POSSIBLE SOURCE — imported). Along
   a patience-down edge whose two runs are decision-free
   throughout, committed cells NEST (the decision lemma,
   explore_stall_unresourced.py), and nesting plus finite loss is
   pointwise domination: the finer trace is weakly better at
   every counted step, so the first differing step's winner and
   the total's winner coincide — no trade. A route-flip edge
   whose consulted bit never met a decision has IDENTICAL traces
   — no divergence at all. So every trade, if one exists, sits
   across an available decision, and the species' name is honest.
L2 (THE EQUALIZER — what the unresourced loop does to a
   divergence). Unresourced, the commit loop runs to exhaustion
   at every step: the committed cell is a function of the ratchet
   cell and the current references, stuck exactly where every
   available subdivision point straddles its reference. So both
   branches of a decision are dragged to reference scale at every
   later step, and a divergence persists only through the GRID:
   the two ratchet positions subdivide at different points, and
   the stopping configurations differ by a geometry factor step
   by step. On a ROUTE edge the two runs hold the same references
   at every step — the cleanest arena: any trade there is pure
   position, no reference asymmetry at all.
L3 (THE CANDIDATE MECHANISM — transient misalignment). Permanent
   foreclosure is impossible: a reference straddles a fixed
   subdivision point forever only if the stream's limit IS that
   rational point, and the batteries' limits are irrational. What
   remains available is TRANSIENT misalignment: the early-better
   branch commits a small cell whose own subdivision point sits
   inside the shrinking references for a run of steps — its
   counted lengths freeze while the early-worse branch's grid
   subdivides on through. Nothing conserved is needed; the
   ratchet's position carries the coupling. This is the shape the
   forge hunts, and the reason the desert of the stall census
   does not decide the species: a trade is one edge, a stall
   needs a whole neighborhood, and the prior rigs counted only
   stalls and value ties.
L4 (WHAT EITHER ANSWER CLOSES). A printed trade answers the
   species YES — a preference decision alone can buy late gain
   with early loss, and the burst trap's mechanism does not need
   its budget. An empty forge at this scope is the FIRST-STEP
   LAW: along every cure edge, the first differing counted step
   decides the total — the per-step-lex order and the product
   order agree edgewise — which is the exact statement an
   impossibility proof must supply, with the near-miss margin
   census saying how much room it has.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls, gate]
   (i)  UNIT: the detector classifies five planted synthetic
        profiles correctly — dominated, trade, exact total tie,
        identical, interleaved-without-trade.
   (ii) INTEGRATION: on the budgeted landscape spike1@10/dbl,
        horizon 16, (B, W) = (2, 0), banking reader, the detector
        fires at least one trade with first differing counted
        step 9 and comeback gap within 1e-3 of 0.0517 ln — the
        parent's dissected anatomy, rediscovered by the new
        instrument.
C2 [THE FORGE — the open observable] The unresourced sweep: the
   parent battery (maps id, dbl; horizons 16, 120), the aimed
   double-burst battery (maps id, dbl, sq; horizons 16, 48), and
   the FULL density pool — every periodic stream of period <= 3
   over digits 1..4, heads () and (2,) (maps id, dbl, sq;
   horizons 16, 48), not the top-24 slice. Per landscape, every
   cure edge between finite-loss policies is classified. GUESS,
   marked as such: divergent edges are common, interleaved pairs
   (each side strictly better somewhere) exist, and at least one
   strict trade fires — predicted locus a route edge at mixed
   patience in a high-variety world. The desert of the stall
   census is evidence the other way; the guess weighs L3's
   mechanism over it. No anatomy is frozen.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 Any C1 check fails: the rig is dead, no verdicts.
K2 A trade prints unresourced: the species settles YES; the full
   anatomy prints (world, edge, divergence step, per-step
   lengths, totals), capped at five.
K3 Zero trades at full scope: the FIRST-STEP LAW holds at scope
   (rule by exhaustion over the edges tested); the smallest
   comeback gap and the interleave census print beside it — the
   impossibility proof's target and its measured room.

ENGINE
------
E1 controls: the synthetic unit battery (C1(i)); the budgeted
   specimen rediscovery (C1(ii)).
E2 the unresourced forge (C2): per battery, landscapes, edges
   tested, divergent edges, dominated vs interleaved, exact total
   ties across divergent profiles, trades; global minimum comeback
   gap with its specimen; full anatomy of every trade found,
   capped in print at five.
Exact big-integer arithmetic throughout (imported comparators);
floats only in printed logs. Sequential, one landscape at a time;
estimated run one to four minutes, memory trivial (no BLAS
import); positive controls gate all verdicts; exit nonzero on any
check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, ~15 s,
peak 76.5 MB)
----------------------------------------------------------------
F1 Controls exact. The five planted profiles classify correctly;
   on the budgeted burst-trap landscape (244 edges, 184
   divergent, 21 trades) the detector rediscovers the dissected
   anatomy: patience-pc edge (0,1)-(0,2) at sigma = (1,0),
   divergence step 9, comeback gap 0.0517 ln.

F2 THE SPECIES ANSWERS YES, AND THE TRADE IS UBIQUITOUS — K2, at
   a scale the guess did not dare. Unresourced, over 276,376
   finite-finite cure edges in 1,102 landscape runs (112 parent,
   192 aimed, 798 full-pool; the batteries overlap in worlds):
   128,584 divergent edges (101,033 dominated, 27,551
   interleaved), ZERO exact total ties, and 10,174 TRADES in
   1,080 of the 1,102 landscapes — pairs whose first differing
   counted step and total deficit point OPPOSITE ways. By edge
   kind: 5,700 patience-pc, 1,930 route-diagonal, 1,600 route-
   s_t, 584 route-s_s, 360 patience-pt. 4,114 are PURE-PREFERENCE
   witnesses — equal patience on both ends, so the two runs read
   IDENTICAL references at every step and the entire divergence
   is the route bits: preference alone, nothing else different.
   C2's guess was right on existence, too narrow on locus: trades
   are not a route-edge specialty but routine on divergent edges
   of every kind, about 1 in 13.

F3 THE FLAGSHIP WITNESS, hand-verified. World head (2,) period
   (1,4,4) under sq, horizon 16, route diagonal (0,1)-(1,0) at
   equal patience (3,0). The (1,0) side wins the divergence step
   8 by 3.244 ln (cell 15/38009 against 5/494) and then FREEZES
   for three steps (17/48825 three times) while the (0,1) side's
   grid subdivides through (149/261348916 three times, 6.415 ln
   finer per step); the profiles re-merge at step 12 and stay
   identical to the horizon. Net comeback 15.9995 ln as printed
   (3 * 6.415 - 3.244). Early loss, late gain, no conserved quantity
   anywhere — the mechanism is L3's transient misalignment
   verbatim: the early winner's own subdivision point sits inside
   the shrinking references and its counted lengths freeze. A
   second specimen hand-summed from the printed profiles
   (ht1/dbl, horizon 16, route s_s at patience (2,0)): ln totals
   -55.87 against -60.28, the first-step loser better by 4.42 ln.

F4 WHAT THE ANSWER CLOSES AND WHAT IT OPENS. (a) The
   impossibility route to an unresourced stall-free theorem is
   DEAD: the argument the stall census said a proof must supply —
   that a decision cannot buy a late gain with an early loss —
   does not exist. (b) The budgeted burst trap's trade shape
   never needed its budget: what a conserved budget manufactures
   is not the trade but its ASSEMBLY into a full local minimum.
   (c) The sharpened open is exactly that assembly: these
   landscapes carry thousands of trades and, by the prior census
   at overlapping scope (zero stalls, zero adjacent value ties,
   explore_stall_unresourced.py), not one stall — every trade's
   first-step winner still has SOME other strictly improving
   move. Why trades never close into a cycle of the cure graph's
   neighborhoods is the assembly question, and it is a different
   species from the one this rig closes.

THE VERDICT. A preference decision alone, with no conserved
budget behind it, CAN buy a late gain with an early loss: rule —
existence by exact-arithmetic witness, re-derived by hand (F3),
with 10,174 instances at the stated scope. The abundance figures
and the edge-kind census are observations at that scope. The
unresourced cell's stall question stays open and is now the
assembly question (F4c).

Run record. The first run exited 0 in ~15 s with all controls
green and 10,174 trades. Post-run edits, no prediction band
touched: the per-edge-kind tally, the pure-preference count and
the specimen display order were added to the prints, and the
display picked the biggest comebacks rather than the smallest.
Final run ~15 s, peak 76.5 MB under memwatch.
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
# the detector
# ----------------------------------------------------------------- #

def classify_pair(clA, clB, lossA, lossB):
    """Classify one finite-loss pair of counted length profiles.
    Returns None if the profiles are identical, else a dict:
      i0    first differing counted index (step = N0 + i0)
      fw    first-step winner: 'A' or 'B' (strictly smaller cell)
      tw    total winner under the lex deficit: 'A'/'B'/'TIE'
      inter True iff the first-step winner is strictly worse at
            some later counted step
      trade True iff tw is the first-step LOSER
      gap   ln(first-step loser total) - ln(first-step winner
            total): negative exactly on a trade, 0 on a tie
    """
    assert len(clA) == len(clB)
    assert all(z is not None for z in clA + clB)
    i0 = None
    for i in range(len(clA)):
        if ST.frac_cmp(clA[i], clB[i]) != 0:
            i0 = i
            break
    if i0 is None:
        return None
    c0 = ST.frac_cmp(clA[i0], clB[i0])
    fw = "A" if c0 < 0 else "B"
    ct = SC.cmp_lex(lossA, lossB)
    tw = "A" if ct < 0 else ("B" if ct > 0 else "TIE")
    sgn = 1 if fw == "A" else -1
    inter = any(sgn * ST.frac_cmp(clA[i], clB[i]) > 0
                for i in range(i0 + 1, len(clA)))
    trade = tw != "TIE" and tw != fw
    lnA = SC.ln_frac(lossA[0], lossA[1])
    lnB = SC.ln_frac(lossB[0], lossB[1])
    gap = (lnB - lnA) if fw == "A" else (lnA - lnB)
    return {"i0": i0, "fw": fw, "tw": tw, "inter": inter,
            "trade": trade, "gap": gap}

def cure_edges(space, daxis):
    """Unordered cure-graph edges over a policy space."""
    sset = set(space)
    seen = set()
    out = []
    for p in space:
        for q in SC.neighbors_cure(p, SC.AX_BASE, daxis):
            if q not in sset:
                continue
            key = tuple(sorted((SC.pol_key(p), SC.pol_key(q))))
            if key in seen:
                continue
            seen.add(key)
            out.append((p, q))
    return out

def edge_kind(p, q):
    """Which cure move joins p and q."""
    d = [i for i in range(5) if p[i] != q[i]]
    if d == [0]:
        return "route s_t"
    if d == [1]:
        return "route s_s"
    if d == [0, 1]:
        return "route diagonal"
    if d == [2]:
        return "patience pt"
    if d == [3]:
        return "patience pc"
    return "delta"

# ----------------------------------------------------------------- #
# E1: controls
# ----------------------------------------------------------------- #

def _mk_loss(cl):
    num, den = 1, 1
    for a, b in cl:
        num *= a
        den *= b
    return (num, den, False)

def e1_unit():
    print("\nE1a UNIT CONTROL: five planted profiles")
    A1 = [(1, 2), (1, 3), (1, 4)]
    B1 = [(1, 2), (1, 2), (1, 4)]
    r = classify_pair(A1, B1, _mk_loss(A1), _mk_loss(B1))
    check("dominated: A wins step and total, no interleave, no "
          "trade", r["fw"] == "A" and r["tw"] == "A"
          and not r["inter"] and not r["trade"] and r["i0"] == 1)
    A2 = [(1, 2), (1, 2), (1, 9)]
    B2 = [(1, 3), (1, 2), (1, 2)]
    r = classify_pair(A2, B2, _mk_loss(A2), _mk_loss(B2))
    check("trade: B wins first step, A wins total",
          r["fw"] == "B" and r["tw"] == "A" and r["trade"]
          and r["inter"] and r["gap"] < 0)
    A3 = [(1, 2), (1, 3)]
    B3 = [(1, 3), (1, 2)]
    r = classify_pair(A3, B3, _mk_loss(A3), _mk_loss(B3))
    check("exact total tie across divergent profiles",
          r["tw"] == "TIE" and not r["trade"] and abs(r["gap"]) < 1e-12)
    r = classify_pair(A3, A3, _mk_loss(A3), _mk_loss(A3))
    check("identical profiles return None", r is None)
    A5 = [(1, 2), (1, 4)]
    B5 = [(1, 3), (1, 3)]
    r = classify_pair(A5, B5, _mk_loss(A5), _mk_loss(B5))
    check("interleaved without trade, positive gap",
          r["fw"] == "B" and r["tw"] == "B" and r["inter"]
          and not r["trade"] and r["gap"] > 0)

def landscape_tables(J, horizon, B, W):
    daxis = SC.d_axis(W) if B is not None else [SC.INF_D]
    space = SC.policy_space5(SC.AX_BASE, daxis)
    lossd, clensd = {}, {}
    for p in space:
        t, sg, cl = ST.run_pol(J, p, B, W, horizon)
        lossd[p], clensd[p] = t, cl
    return space, daxis, lossd, clensd

def scan_edges(space, daxis, lossd, clensd):
    """Classify every finite-finite cure edge. Returns (stats,
    trades, min-gap specimen)."""
    stats = {"edges": 0, "div": 0, "dom": 0, "inter": 0,
             "ties": 0, "trades": 0, "kinds": {}}
    trades = []
    best = None
    for p, q in cure_edges(space, daxis):
        if lossd[p][2] or lossd[q][2]:
            continue
        stats["edges"] += 1
        r = classify_pair(clensd[p], clensd[q], lossd[p], lossd[q])
        if r is None:
            continue
        stats["div"] += 1
        if r["inter"]:
            stats["inter"] += 1
        else:
            stats["dom"] += 1
        if r["tw"] == "TIE":
            stats["ties"] += 1
        if r["trade"]:
            stats["trades"] += 1
            stats["kinds"][edge_kind(p, q)] = \
                stats["kinds"].get(edge_kind(p, q), 0) + 1
            trades.append((p, q, r))
        elif r["tw"] != "TIE":
            if best is None or r["gap"] < best[2]["gap"]:
                best = (p, q, r)
    return stats, trades, best

def e1_specimen():
    print("\nE1b INTEGRATION CONTROL: the budgeted burst trap's "
          "trade, rediscovered")
    digs = [1] * 16
    digs[10] = 8
    J = SC.images(SC.cylinders(digs), "dbl")
    space, daxis, lossd, clensd = landscape_tables(J, 16, 2, 0)
    stats, trades, _ = scan_edges(space, daxis, lossd, clensd)
    print("  spike1@10/dbl h=16 (B,W)=(2,0): %d edges, %d "
          "divergent, %d trades"
          % (stats["edges"], stats["div"], stats["trades"]))
    hit = [t for t in trades
           if t[2]["i0"] + SC.N0 == 9 and abs(-t[2]["gap"] - 0.0517)
           < 1e-3]
    check("a trade with divergence step 9 and comeback gap "
          "0.0517 ln exists", len(hit) >= 1)
    if hit:
        p, q, r = hit[0]
        print("  specimen: %s <-> %s (%s), step %d, gap %.4f ln"
              % (SC.fmt_pol5(p), SC.fmt_pol5(q), edge_kind(p, q),
                 r["i0"] + SC.N0, -r["gap"]))

# ----------------------------------------------------------------- #
# E2: the unresourced forge
# ----------------------------------------------------------------- #

def battery_landscapes():
    """(battery name, world name, map, horizon, J) for the three
    unresourced batteries."""
    out = []
    for wname, digs in ST.battery_worlds():
        cyls = SC.cylinders(digs)
        for mp in ("id", "dbl"):
            J_full = SC.images(cyls, mp)
            for horizon in (16, SC.N_MAIN):
                out.append(("parent", wname, mp, horizon,
                            J_full[:horizon]))
    for horizon in SU.AIMED_HORIZONS:
        for wname, digs in SU.aimed_worlds(horizon):
            cyls = SC.cylinders(digs)
            for mp in SU.AIMED_MAPS:
                out.append(("aimed", wname, mp, horizon,
                            SC.images(cyls, mp)[:horizon]))
    for horizon in SU.AIMED_HORIZONS:
        for wname, digs in SU.density_pool(horizon):
            cyls = SC.cylinders(digs)
            for mp in SU.AIMED_MAPS:
                out.append(("pool", wname, mp, horizon,
                            SC.images(cyls, mp)[:horizon]))
    return out

def e2_forge():
    print("\nE2  THE UNRESOURCED FORGE: trade hunt along every "
          "cure edge")
    lands = battery_landscapes()
    per = {}
    kinds = {}
    n_trade_lands = 0
    all_trades = []
    best = None
    for bat, wname, mp, horizon, J in lands:
        space, daxis, lossd, clensd = landscape_tables(
            J, horizon, None, 0)
        stats, trades, b = scan_edges(space, daxis, lossd, clensd)
        t = per.setdefault(bat, {"lands": 0, "edges": 0, "div": 0,
                                 "dom": 0, "inter": 0, "ties": 0,
                                 "trades": 0})
        t["lands"] += 1
        for k in ("edges", "div", "dom", "inter", "ties", "trades"):
            t[k] += stats[k]
        for k, v in stats["kinds"].items():
            kinds[k] = kinds.get(k, 0) + v
        if trades:
            n_trade_lands += 1
        for p, q, r in trades:
            all_trades.append((bat, wname, mp, horizon, p, q, r,
                               clensd[p], clensd[q]))
        if b is not None and (best is None
                              or b[2]["gap"] < best[6]["gap"]):
            best = (bat, wname, mp, horizon, b[0], b[1], b[2])
    for bat in ("parent", "aimed", "pool"):
        t = per[bat]
        print("  %-6s: %4d landscapes | %6d edges | %6d divergent "
              "(%d dominated, %d interleaved) | %d total ties | "
              "%d trades"
              % (bat, t["lands"], t["edges"], t["div"], t["dom"],
                 t["inter"], t["ties"], t["trades"]))
    if all_trades:
        print("  TRADES FOUND: %d in %d landscapes — the species "
              "answers YES" % (len(all_trades), n_trade_lands))
        print("  by edge kind: %s"
              % " | ".join("%s %d" % (k, kinds[k])
                           for k in sorted(kinds)))
        eqpat = [t for t in all_trades
                 if t[4][2] == t[5][2] and t[4][3] == t[5][3]]
        print("  pure-preference witnesses (equal patience, same "
              "references): %d" % len(eqpat))
        show = []
        if eqpat:
            show.append(min(eqpat,
                            key=lambda t: (t[3], t[6]["gap"])))
        by_gap = sorted(all_trades, key=lambda t: t[6]["gap"])
        show += [t for t in by_gap if t not in show]
        for bat, wname, mp, horizon, p, q, r, clp, clq in show[:4]:
            print("\n  TRADE %s/%s h=%d (%s):" % (wname, mp,
                                                  horizon, bat))
            print("    %s  vs  %s  (%s)"
                  % (SC.fmt_pol5(p), SC.fmt_pol5(q),
                     edge_kind(p, q)))
            print("    divergence at counted step %d; first-step "
                  "winner %s, total winner %s, comeback gap "
                  "%.4f ln" % (r["i0"] + SC.N0, r["fw"], r["tw"],
                               -r["gap"]))
            for tag, cl in (("A", clp), ("B", clq)):
                cells = " ".join("%d/%d" % z for z in cl)
                print("    %s counted lengths: %s" % (tag, cells))
        if len(all_trades) > 5:
            print("  ... and %d more" % (len(all_trades) - 5))
    else:
        print("  ZERO TRADES — the FIRST-STEP LAW holds at this "
              "scope: along every cure edge tested, the first "
              "differing counted step decides the total.")
        if best is not None:
            bat, wname, mp, horizon, p, q, r = best
            print("  closest comeback: gap %.6f ln at %s/%s h=%d "
                  "(%s), %s <-> %s, divergence step %d"
                  % (r["gap"], wname, mp, horizon, bat,
                     SC.fmt_pol5(p), SC.fmt_pol5(q),
                     r["i0"] + SC.N0))
    return all_trades

# ----------------------------------------------------------------- #

def main():
    print("THE DECISION TRADE: early loss, late gain, no budget?")
    print("=" * 70)
    e1_unit()
    e1_specimen()
    if FAILURES:
        print("\nCONTROLS FAILED — no verdicts.")
        sys.exit(1)
    e2_forge()
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % FAILURES))
    sys.exit(1 if FAILURES else 0)

if __name__ == "__main__":
    main()
