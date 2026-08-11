r"""explore_even_winner.py -- THE OVER-2 CELL OF THE WINNER-KIND DICHOTOMY.
When the void's first winner is an unramified place OVER 2, what does the
walk seat, and what does the menu minimum do?

THE QUESTION. The clock corpus proves: a void walk whose first winner is
split or inert of ODD norm seats exactly one place ever, and the menu
minimum is a constant n0 from step 1 (the strict-climb induction,
explore_late_seating.py hand-attack B). The over-2 cell is left open there:
norm 2's column holds a flat step (lambda(Z/8) = 2), so the induction's
hypothesis fails, and no walked ring hands an unramified place over 2 the
void. This file mints six rings that do -- three where the winner is the
SPLIT place of norm 2, three where it is the INERT place of norm 4 -- and
asks whether monogamy (one seating ever) survives, and what replaces the
constant-minimum signature.

WHOSE VOCABULARY. Engine observables throughout, re-derived from
explore_late_seating.py and its hosts rather than memory: lam_P(pl, a) is
the exponent of (O/P^a)^*; L = lam_state(st) = lcm of the seated columns;
door_r(pl, e, L) = the least r >= 1 with lam_P(pl, e+r) not dividing L; a
move at pl costs norm(pl)^r and raises the exponent by r; greedy takes the
menu minimum, first tie member by place_key. The one factory correction
this file carries: explore_late_seating's QRing states the split column as
(p-1)*p^(a-1), which is FALSE at p = 2 (the true column is 1, 2, then
2^(a-2) -- explore_module_law's SPLIT2_TABLE, the flat step at depth 3);
never exercised there (both minted rings ramify 2), load-bearing here.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The falling-paid hand walk below models the norm-2 column on the
    classical lambda of Z/2^a. The brute-forcer on the actual residue
    rings (explore_gaussian_runaway.unit_exponent) is the authority; S2
    asserts every cell in range.
 T2 The odd-norm induction's frame (strict climb -> constant minimum) is
    the NEIGHBOURING cell's vocabulary. At residue degree 1 over 2 that
    frame fails at the flat step, and the monogamy argument below is
    re-derived from the falling minimum, not inherited from the frame.
 T3 "Seats exactly one place" is the VOID sentence. Seeded walks answer a
    different one (can a fuller invariant hand a rival the menu?) and are
    reported apart (S5), never as kills.

THE HAND-ATTACK, on paper before any engine code.

 A. THE SPLIT CASE (norm-2 winner; d = -7, -31, -55). If 2 splits and the
    ring has no place of norm 3 and no ramified place under 4, the void
    menu reads: each norm-2 conjugate at door 2 (lam(P,1) = 1 divides
    L = 1, lam(P,2) = 2 does not), cost 4 -- an AUTOMATIC void tie at 4,
    the conjugate pair -- and everything else at >= 5. Tie-break seats one
    conjugate at exponent 2; L = lam(P,2) = 2. Step 2: the flat step
    (lam(P,3) = 2 divides 2) widens the winner's own door to 2, cost 4,
    exponent to 4; the CONJUGATE jumps to door 4, cost 16 (its column is
    the winner's, every rung dividing L). Step 3 on: lam climbs one
    doubling per depth, door 1, cost 2 forever. Paid: 4, 4, 2, 2, 2, ...
    -- the menu minimum FALLS, the opposite of the ramified transient's
    climb and off the odd-norm proof's constant. Monogamy re-derived: the
    only cost-4 void rivals are the conjugates (a second norm-2 place;
    inert 2 cannot coexist with split 2, and no ramified place prices 4);
    the losing conjugate jumps to 16 at step 2 and widens with L; every
    other rival lost the void at >= 5, is nondecreasing (Lemma B), and
    the paid sequence never exceeds 4: no rival ever undercuts. One
    seating ever, with the tie caveat now STRUCTURAL (the conjugate,
    symmetric, either member telling the same story).
 B. THE INERT CASE (norm-4 winner; d = -19, -43, -115). If 2 is inert and
    the ring has no norm-3 place and no ramified place under 4, the void
    menu reads: the inert place at door 1 (lam(P,1) = 3 does not divide
    1), cost 4, alone at its price (2 inert leaves no second norm-4
    place). Its column is 3 * 2^(a-1) -- STRICT climb, no flat step -- so
    the odd-norm induction's mechanism re-enters even though its licence
    hypothesis (e < p - 1) is unmeetable at p = 2: door 1 forever,
    constant paid 4, one seating ever, no tie at all.
 C. WHY THE FLAT STEP LIVES AT RESIDUE DEGREE 1 AND NOWHERE UNRAMIFIED.
    (1 + 2u)^2 = 1 + 4(u + u^2) and u + u^2 mod 2 is the Artin-Schreier
    map of the residue field. Over F_2 it vanishes identically (x^2 = x),
    so every square of 1 + P is 1 mod P^3 and the column pauses: the flat
    step. Over F_4 it does not vanish (a generator has u + u^2 = 1), so
    depth 3 holds an order-4 unit and the column doubles strictly from
    depth 2 on: E(a) = 2^(a-1), lam = 3 * 2^(a-1). The over-2 cell is
    therefore TWO cells, split by residue degree, and only degree 1
    carries the anomaly.
 D. THE STALLED-RAM PROBE. d = -55 (ram 5, 11) and d = -115 (ram 5, 23)
    put a cheap stalled ramified door beside the even winner: R5 prices 5
    at the void (lam(R5,1) = 4 does not divide 1), loses to 4, and the
    paid sequence never rises past it (A falls to 2, B holds 4). The
    catching mechanism that seats Z[sqrt(-30)]'s R5 -- a CLIMBING
    transient -- has nothing to climb with here, so an even unramified
    winner should be MORE monogamous than an odd one, not less: the one
    winner kind whose menu minimum can never rise at all.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 FACTORY CONTROL. The corrected factory at (T, N0) = (1, -6) against
    the K23 host engine (disc -23, the one walked ring with a split 2):
    every shared place's lambda table agrees on the brute window, the
    norm-2 cells to depth 12 included, and doors sampled at
    L in {1, 2, 6, 12, 60}, e in {0, 1, 2} agree. The PARENT factory's
    uncorrected split formula disagrees with the host at (norm 2, a = 3)
    -- the correction is live, not vacuous. KILL: any corrected-factory
    cell off the host; or the parent agreeing at the flat step.
PR2 THE COLUMNS, BRUTE-FORCED. On the actual residue rings, the norm-2
    column at d = -7 prints 1, 2, 2, 4, ..., 2^(a-2) to depth 17 and the
    norm-4 column at d = -19 prints 3 * 2^(a-1) to depth 8; the closed
    forms match every brute cell. KILL: one cell, which kills hand-attack
    C's Artin-Schreier reading and not just a prediction.
PR3 SUB-CELL A. At d = -7, -31, -55 the void menu minimum is 4 at a
    two-member tie (the conjugate pair, both at door 2); the walk seats
    the tie-broken conjugate at exponent 2; paid prints 4 4 2 2 2 ... (2
    from step 3 on, never rising); exactly ONE fresh seating in 40 moves;
    the losing conjugate's cost prints 16 at step 2. KILL: a second
    seating, a paid entry above 4, or a paid tail off the constant 2.
PR4 SUB-CELL B. At d = -19, -43, -115 the void minimum is 4 with a
    one-member tie (no twin); paid prints the constant 4; exactly one
    fresh seating in 40 moves; the winner's column climbs strictly at
    every depth to 20. KILL: a second seating, any paid off 4, or a flat
    cell in the column.
PR5 STALLED RAMS STAY STALLED. At d = -55 and d = -115, R5 prints cost 5
    at the void and is never seated in 40 moves; the per-step least
    unseated-ramified margin prints alongside. KILL: any ramified seating
    at these two rings.
PR6 MONOTONE. Across every trajectory recorded in this file, an unseated
    place's cost never falls while it stays unseated (Lemma B in situ).
    PRINTS: pairs checked, violations. KILL: one violation.
PR7 THE SEEDED SWEEPS (observation, flag T3 -- a different sentence, no
    kill fixed). Ram-free generator-product seeds (norm <= 40) at all six
    rings, every unplanted-ramified seating printed with its step and
    cost.

FINDINGS, entered after the run from printed output. All seven predictions
landed; both controls clean.

F1 THE OVER-2 CELL CLOSES: MONOGAMY IS EVERY UNRAMIFIED WINNER'S (rule,
   proved at the quadratic shape; premises machine-checked). All six void
   walks seat exactly one place ever in 40 moves. The inert sub-cell is
   the odd-norm story re-entered: the norm-4 column 3 * 2^(a-1) climbs
   strictly (brute to depth 8 at one ring -- the completion at an inert 2
   is the same unramified quadratic extension of Q_2 at all three --
   checked to 21), so door 1 and the constant
   paid 4 -- the strict-climb conclusion holds even though the licence
   hypothesis e < p - 1 that DERIVED it at odd norm is unmeetable at
   p = 2; what replaces the licence is hand-attack C's Artin-Schreier
   fact, brute-confirmed. The split sub-cell is where the frame fails
   (the flat step) and monogamy is re-derived from the falling minimum:
   paid prints 4 4 2 2 2 ... at all three rings, and every rival lost the
   void at >= 4 and never falls (PR6: 153,051 pairs, 0 violations).

F2 THE PAID DIRECTION READS THE WINNER'S KIND, NOW THREE WAYS (rule at
   the walked rings). The menu minimum FALLS to the floor 2 and STAYS
   exactly when the winner has norm 2 (the flat step widens the winner's
   own door once, then one doubling per depth prices its recurrent move
   at 2); it is CONSTANT at every other unramified winner; it RISES
   through a ramified winner's transient -- which may touch the floor on
   the way (Z[i] pays 2 twice) but climbs off it. A norm-2 winner is the
   one kind that locks on itself BELOW its opening price, at the
   family's least possible recurrent price.

F3 THE VOID TIE IS STRUCTURAL AT NORM 2. A norm-2 winner never arrives
   alone: its conjugate ties at exactly 4 (both door 2, the printed
   two-member tie at all three A-rings), so the dichotomy's "up to a void
   tie" caveat is FORCED there rather than exceptional -- and benign: the
   tie is symmetric, and the losing conjugate jumps to 16 at step 2 (its
   column is the winner's own, every rung dividing L) and widens with the
   invariant. The inert sub-cell prints a one-member tie: 2 inert leaves
   no second norm-4 place, and in a quadratic ring nothing else can price
   4 at the void.

F4 STALLED RAMS STAY STALLED: THE EVEN WINNER IS THE MOST MONOGAMOUS
   KIND. R5 prices 5 at the void beside both even winners (d = -55,
   -115), margin +1, and is never seated: the catching mechanism that
   seats Z[sqrt(-30)]'s R5 is a CLIMBING minimum, and an even unramified
   winner's minimum never rises at all -- it falls or holds.

F5 SEEDED (observation sweep, flag T3 -- a different sentence). Ram-free
   seeds hand unplanted ramified places the menu at 16 of 39 D7 walks
   (R7 at 7), 16 of 52 D55 (R5 at 5, R11 at 11), 6 of 16 D115 (R5 at 5),
   0 at D31, D19, D43 -- the odd-part-of-L mechanism of the filed seeded
   lever, indifferent to the void winner's kind.

RUN RECORD. One process, CPython, no BLAS; the factory, walker and seed
builder imported from explore_late_seating.py / explore_lock_budget.py,
the brute-forcer from explore_gaussian_runaway.py run on the minted
rings' actual residue rings. 321 checks green. Under memwatch: peak
working set 25.2 MB, peak commit 19.1 MB against the 512 MB ceiling,
wall 3.3 s. (Universe truncation checked harmless in review: primes
enumerated to 61 only, and the max menu minimum over every recorded walk
-- void and seeded, all six rings -- is 23, below the norm of any absent
place, so no truncated place could ever have undercut a menu.)
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_gaussian_runaway as ZI      # the brute-forcer
import explore_late_seating as LS          # the QRing factory + seed builder
import explore_lock_budget as LB           # the imported walker
import explore_module_law as K23           # Z[w], w^2 = w - 6: the split-2 host

CHECKS = 0

NMOVES = 40           # moves per recorded walk
DEPTH_CHECK = 20      # winner-column depths checked
SPLIT2_BRUTE = 17     # norm-2 brute depths (2^17 under the factory's cap)
INERT2_BRUTE = 8      # norm-4 brute depths (4^8 under the factory's cap)


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------ the corrected quadratic ring
def split2_lam(a):
    """The norm-2 split column: exponent of (Z/2^a)^*."""
    if a <= 2:
        return (1, 1, 2)[a]
    return 2 ** (a - 2)


class EQRing(LS.QRing):
    """explore_late_seating's factory with the split column corrected at
    p = 2 (the flat step) and the inert-2 closed form kept but, like the
    ramified columns, asserted against the brute residue ring before first
    deep use (S2 runs the assertion for the record)."""

    def lam_P(self, pl, a):
        if a == 0:
            return 1
        if pl[0] == 'split' and pl[1] == 2:
            return split2_lam(a)
        return LS.QRing.lam_P(self, pl, a)


# the six minted rings: Z[t], t^2 = t + N0, disc = 1 + 4*N0
D7 = EQRing("Q(sqrt-7)", 1, -2)       # 2 split, 3 inert, ram 7
D31 = EQRing("Q(sqrt-31)", 1, -8)     # 2 split, 3 inert, ram 31
D55 = EQRing("Q(sqrt-55)", 1, -14)    # 2 split, 3 inert, ram 5 and 11
D19 = EQRing("Q(sqrt-19)", 1, -5)     # 2 inert, 3 inert, ram 19
D43 = EQRing("Q(sqrt-43)", 1, -11)    # 2 inert, 3 inert, ram 43
D115 = EQRing("Q(sqrt-115)", 1, -29)  # 2 inert, 3 inert, ram 5 and 23

A_RINGS = [("D7", D7), ("D31", D31), ("D55", D55)]
B_RINGS = [("D19", D19), ("D43", D43), ("D115", D115)]
RINGS = A_RINGS + B_RINGS


# --------------------------------------------------- S1 the split-2 host control
def s1_host_control():
    section("S1  FACTORY CONTROL -- the corrected factory against the K23 "
            "host, the one walked ring with a split 2 (PR1)")
    F = EQRing("ctl-K23", 1, -6)
    P = LS.QRing("ctl-K23-parent", 1, -6)
    host = {}
    for pl in K23.UNIVERSE:
        host[(pl[0], pl[1]) if pl[0] != 'split' else pl] = pl
    shared = n2cells = 0
    for pl in F.UNIVERSE:
        key = (pl[0], pl[1]) if pl[0] != 'split' else pl
        if key not in host:
            continue
        hpl = host[key]
        ok(F.place_norm(pl) == K23.place_norm(hpl),
           "norm mismatch at %s" % (pl,))
        amax = 12 if F.place_norm(pl) == 2 else 1
        while F.place_norm(pl) ** (amax + 1) <= 200_000 and amax < 12:
            amax += 1
        for a in range(1, amax + 1):
            got, want = F.lam_P(pl, a), K23.lam_P(hpl, a)
            ok(got == want, "lam(%s,%d): factory %d vs host %d"
               % (pl, a, got, want))
            if F.place_norm(pl) == 2:
                n2cells += 1
        shared += 1
    print("  corrected factory vs host: %d shared places agree on the brute"
          " window, %d norm-2 cells to depth 12 included" % (shared, n2cells))
    p2 = next(pl for pl in F.UNIVERSE
              if pl[0] == 'split' and pl[1] == 2)
    hp2 = host[p2]
    ok(P.lam_P(p2, 3) != K23.lam_P(hp2, 3),
       "PR1: the parent's split formula must miss the flat step")
    print("  the correction is live: parent lam(P2,3) = %d, host %d,"
          " corrected %d" % (P.lam_P(p2, 3), K23.lam_P(hp2, 3),
                             F.lam_P(p2, 3)))
    for L in (1, 2, 6, 12, 60):
        for pl in F.UNIVERSE[:6]:
            key = (pl[0], pl[1]) if pl[0] != 'split' else pl
            if key not in host:
                continue
            for e in (0, 1, 2):
                ok(F.door_r(pl, e, L) == K23.door_r(host[key], e, L),
                   "door mismatch %s e=%d L=%d" % (pl, e, L))
    print("  doors sampled at L in {1, 2, 6, 12, 60}, e in {0, 1, 2}: agree")


# ----------------------------------------------------- S2 the columns, brute
def s2_columns():
    section("S2  THE TWO OVER-2 COLUMNS, BRUTE-FORCED FROM THE RESIDUE "
            "RINGS (PR2)")
    p2 = next(pl for pl in D7.UNIVERSE if pl[0] == 'split' and pl[1] == 2)
    col = []
    for a in range(1, SPLIT2_BRUTE + 1):
        v = ZI.unit_exponent(p2, a, D7.T, D7.N0)
        ok(v == split2_lam(a),
           "norm-2 column at depth %d: brute %d vs closed %d"
           % (a, v, split2_lam(a)))
        col.append(v)
    print("  d=-7 norm-2 column to depth %d: %s"
          % (SPLIT2_BRUTE, " ".join(str(v) for v in col)))
    print("    the flat step at depth 3, then one doubling per depth"
          " (2^(a-2))")
    q2 = next(pl for pl in D19.UNIVERSE if pl[0] == 'inert' and pl[1] == 2)
    col = []
    for a in range(1, INERT2_BRUTE + 1):
        v = ZI.unit_exponent(q2, a, D19.T, D19.N0)
        ok(v == 3 * 2 ** (a - 1),
           "norm-4 column at depth %d: brute %d vs closed %d"
           % (a, v, 3 * 2 ** (a - 1)))
        col.append(v)
    print("  d=-19 norm-4 column to depth %d: %s"
          % (INERT2_BRUTE, " ".join(str(v) for v in col)))
    print("    no flat step anywhere: 3 * 2^(a-1), strict from depth 1")


# ------------------------------------------------------- S3 the six void walks
VOID_RECS = {}


def s3_void_walks():
    section("S3  THE SIX VOID WALKS (PR3, PR4, PR5)")
    for name, M in RINGS:
        rec = LS.walk_record(M, {}, NMOVES)
        VOID_RECS[name] = rec
        seat = LS.fresh_seatings(rec)
        marg = LS.ram_margins(M, rec)
        st0, L0 = {}, 1
        vcost, vties = M.ideal_menu(st0, L0)
        print("\n  %s (%s, disc %d)" % (name, M.name, M.disc))
        print("    void menu min %d, tie members %d: %s"
              % (vcost, len(vties),
                 "; ".join("%s door %d" % (LB.show_place(M, pl), r)
                           for pl, r in vties)))
        print("    paid:     %s" % " ".join(
            "%d" % c for _, _, c, _, _ in rec[:14]))
        print("    seatings: %s" % "; ".join(
            "step %d: %s cost %d" % (s, LB.show_place(M, pl), c)
            for s, pl, c in seat))
        if any(m[1] is not None for m in marg):
            tight = min((m[1] - m[0], i + 1) for i, m in enumerate(marg)
                        if m[1] is not None)
            print("    tightest unseated-ram margin: %+d at step %d" % tight)
    for name, M in A_RINGS:
        rec = VOID_RECS[name]
        seat = LS.fresh_seatings(rec)
        paid = [c for _, _, c, _, _ in rec]
        vcost, vties = M.ideal_menu({}, 1)
        ok(vcost == 4 and len(vties) == 2
           and all(pl[0] == 'split' and pl[1] == 2 and r == 2
                   for pl, r in vties),
           "PR3: %s void: min 4 at the conjugate-pair tie, both door 2"
           % name)
        ok(len(seat) == 1 and seat[0][1][0] == 'split'
           and seat[0][1][1] == 2,
           "PR3: %s seats exactly one place, the norm-2 winner" % name)
        ok(paid[0] == 4 and paid[1] == 4
           and all(c == 2 for c in paid[2:]),
           "PR3: %s paid is 4 4 then the constant 2" % name)
        winner = seat[0][1]
        loser = next(pl for pl, r in vties if pl != winner)
        st1, L1 = rec[1][0], rec[1][1]
        lcost = M.place_norm(loser) ** M.door_r(loser, 0, L1)
        ok(lcost == 16,
           "PR3: %s losing conjugate prices 16 at step 2" % name)
        print("  PR3 %-4s: one seating, paid 4 4 2..., conjugate jumps"
              " 4 -> %d" % (name, lcost))
    for name, M in B_RINGS:
        rec = VOID_RECS[name]
        seat = LS.fresh_seatings(rec)
        paid = [c for _, _, c, _, _ in rec]
        vcost, vties = M.ideal_menu({}, 1)
        ok(vcost == 4 and len(vties) == 1 and vties[0][0][0] == 'inert'
           and vties[0][0][1] == 2 and vties[0][1] == 1,
           "PR4: %s void: min 4, the inert-2 place alone at door 1" % name)
        ok(len(seat) == 1 and seat[0][1][0] == 'inert',
           "PR4: %s seats exactly one place, the norm-4 winner" % name)
        ok(all(c == 4 for c in paid),
           "PR4: %s paid is the constant 4" % name)
        P0 = seat[0][1]
        for a in range(1, DEPTH_CHECK + 1):
            ok(M.lam_P(P0, a + 1) % M.lam_P(P0, a) == 0
               and M.lam_P(P0, a + 1) > M.lam_P(P0, a),
               "PR4: %s winner column climbs at depth %d" % (name, a))
        print("  PR4 %-4s: one seating, constant paid 4, column climbs to"
              " depth %d" % (name, DEPTH_CHECK + 1))
    for name in ("D55", "D115"):
        M = dict(RINGS)[name]
        rec = VOID_RECS[name]
        r5 = next(pl for pl in M.UNIVERSE if pl[0] == 'ram' and pl[1] == 5)
        ok(M.place_norm(r5) ** M.door_r(r5, 0, 1) == 5,
           "PR5: %s R5 prices 5 at the void" % name)
        ok(all(pl != r5 for _, pl, _ in LS.fresh_seatings(rec)),
           "PR5: %s never seats R5" % name)
        print("  PR5 %-4s: R5 at 5 stalled and never seated" % name)


# ------------------------------------------------------- S4 the monotone check
def s4_monotone(all_recs):
    section("S4  UNSEATED COSTS ARE NONDECREASING, IN SITU (PR6)")
    pairs = viol = 0
    for M, rec in all_recs:
        last = {}
        for st, L, cost, pl, r in rec:
            for q in M.UNIVERSE:
                if st.get(q, 0):
                    last.pop(q, None)
                    continue
                c = M.place_norm(q) ** M.door_r(q, 0, L)
                if q in last:
                    pairs += 1
                    if c < last[q]:
                        viol += 1
                        print("    VIOLATION: %s falls %d -> %d"
                              % (q, last[q], c))
                last[q] = c
    print("  %d consecutive unseated-cost pairs checked, %d violations"
          % (pairs, viol))
    ok(viol == 0, "PR6: no unseated cost ever falls")


# --------------------------------------------------------- S5 the seeded sweep
def s5_seeded(all_recs):
    section("S5  THE SEEDED SWEEPS -- ram-free seeds, every unplanted "
            "ramified seating (PR7, observation)")
    for name, M in RINGS:
        seeds = LS.ram_free_seeds(M)
        events = []
        for seed in seeds:
            rec = LS.walk_record(M, seed, NMOVES)
            all_recs.append((M, rec))
            for s, pl, c in LS.fresh_seatings(rec):
                if pl[0] == 'ram':
                    events.append((seed, s, pl, c))
        hit = len(set(tuple(sorted((str(k), v) for k, v in e[0].items()))
                      for e in events))
        print("\n  %-4s %d ram-free seeds (norm <= %d): %d walks seat an"
              " unplanted ramified place"
              % (name, len(seeds), LS.SEED_NORM_CAP, hit))
        for seed, s, pl, c in events[:6]:
            print("      seed %-22s step %2d  %-6s cost %d"
                  % (LB.show_state(M, seed), s, LB.show_place(M, pl), c))
        if len(events) > 6:
            print("      ... %d more" % (len(events) - 6))


def main():
    s1_host_control()
    s2_columns()
    s3_void_walks()
    all_recs = [(dict(RINGS)[n], VOID_RECS[n]) for n, _ in RINGS]
    s5_seeded(all_recs)
    s4_monotone(all_recs)
    print("\n%d checks green." % CHECKS)


if __name__ == "__main__":
    main()
