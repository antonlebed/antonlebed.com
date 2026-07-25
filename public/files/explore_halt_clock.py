"""explore_halt_clock.py — the halt clock c*(D) (explore_function_field_melt.py's remainder).

THE QUESTION (explore_function_field_melt.py finding 5's open
edge). Bounded-alphabet thermal D-DYN over F_2[x] (moves of degree <= D)
is MORTAL, and at D = 10 every run died at the SAME clock reading c* = 5,
temperature-independent (observation). WHY 5, what is c*(D), and
what exactly is beta-independent about it?

PREDICTIONS HC1-HC6 (fixed before the run), hand-attacked BEFORE this
engine was written. Findings are written from
the green run's output only.

  HC1 (criterion): menu membership == the two-channel criterion (clock:
      some place's new depth > 2^c_global; odd: some fresh place g with
      2^deg(g) - 1 not dividing the odd part of lambda), every monic
      deg <= 9, on a battery of constructed + MC-reached states.
  HC2 (fresh law): the odd channel's divisibility is the Mersenne
      lattice: 2^d - 1 | lcm_{d' in S}(2^{d'} - 1) iff some d' in S is
      a multiple of d — UNIFORMLY for d >= 2, including the Zsygmondy
      exception d = 6 (3^2 is the honorary primitive: ord_9(2) = 6).
      Exhaustive over S subset of {1..12}, d = 2..14.
  HC3 (mode law): modal halt reading = floor(log2 D) + 2 at
      D in {2, 3, 4, 5, 6, 8, 12}, beta = 2 (N = 100; D = 12: N = 60).
      At D in {2, 8}: ALL runs at the mode (D = 2: tail impossible;
      D = 8: dyadic-phase cost 8, rate ~1e-5).
  HC4 (tail law): at D = 6 (dyadic-phase cost 2^{J+1} - D = 2) the
      exceedance rate at beta = 2, N = 400 is in (0, 0.4); rates
      ordered rate(1.25) > rate(3) strictly and weakly monotone
      across 1.25 / 2 / 3. At D = 2 exceedance is EXACTLY 0.
  HC5 (support): DP c_max(D) == hand values 3, 5, 5, 7 at
      D = 2, 4, 5, 10; every DP witness chain replays admissibly
      through thermal_menu and achieves the DP reading; the budget
      bound 2^{c-1} + 1 <= 2 + D(c-1) + (D-1)(D-2)/2 holds at every
      D and is NOT tight at D = 5; no MC run exceeds DP.
  HC6 (halt time): T_halt <= (D - 1) + (c_final - c_0) on EVERY run
      (each move raises the clock or collects a new Mersenne degree);
      median T at D = 6 weakly decreasing as beta drops 3 -> 2 -> 1.25.

A pre-run FINDINGS draft was fabricated inside this file's creating
Write and expunged before the run — a recurring species of the
fabrication reflex, fired again here, minutes after planning the guard.
Adjudication of its
banked inventions: every non-code-derivable
specific was FALSE — all three tail rates (invented 32.5/8.75/1.0%,
true 18.75/12.5/3.25%), the median story (invented "8/8/8 equality",
true 7/8/8 with a strict drop), the budget-tightness set (invented
{5,8,11,12}, true {5,8,12}), the check count. Not for the first time:
the reflex's inventions anti-correlate with truth.

FINDINGS (naming tiers below; run record at bottom; all sections
assert; predictions HC1-HC6 all confirmed, no misses).

1. THE ADMISSIBILITY CRITERION HAS TWO CHANNELS (criterion, proved;
   asserted exhaustively: 20 states x all 1022 monics deg <= 9).
   m is admissible iff it fires the CLOCK channel — some place, old
   or new, reaches depth > 2^c, where c = v2(lambda) =
   max_g ceil_log2(depth_g) is the GLOBAL clock (deepening a trailing
   column below the global frontier is INADMISSIBLE) — or the ODD
   channel: some fresh place g with 2^deg(g) - 1 not dividing
   lambda's odd part. Nothing else grows lambda: 1-units are 2-groups
   in char 2, Mersennes are odd. Proof: lambda = lcm_g (2^{d_g} - 1)
   * 2^{ceil_log2(e_g)}; the 2-part is the max, the odd part a lattice
   join. The two channels are the module law's rank split
   (explore_module_law.py) read as a menu partition.

2. THE FRESH LAW IS THE MERSENNE LATTICE (criterion, proved via
   Zsygmondy/Bang; asserted exhaustively: all 4096 subsets S of
   {1..12} x d = 2..14). The degree-d fresh door is open iff NO open
   degree is a multiple of d: 2^d - 1 | lcm_{d' in S}(2^{d'} - 1) iff
   d | d' for some d' in S. (<=) direct; (=>) the primitive prime of
   2^d - 1 (Zsygmondy), UNIFORM even at the exception d = 6, where
   63 = 3^2 * 7 has no primitive prime but ord_9(2) = 6 makes 3^2 the
   honorary primitive. Corollaries: the odd channel fires at most
   once per degree — one fresh 2^d - 1 ever (same-degree places can
   still open later as rider passengers or clock-jumpers);
   opening d' CLOSES every unopened door d | d'; degree-1 places
   never fire the odd channel (2^1 - 1 = 1 — the root of the cold
   x+1 starvation, explore_function_field_lock.py); RIDERS g * x^r (deg <= D) creep a column
   below the frontier for free, total creep budget
   R(D) = (D-1)(D-2)/2.

3. THE MODE LAW: c*(D) = floor(log2 D) + 2 (rule for the mechanism;
   MC-confirmed at D = 2, 3, 4, 5, 6, 8, 12, beta = 2, N = 100 each,
   D = 12: N = 60 — modal reading 3, 3, 4, 4, 4, 5, 5 as frozen, all
   660 runs halting). SCOPE: stated for the melt's light seed x^2
   (c_0 = 1); a seed already reading past c*(D) changes the law
   (its final reading depends on the seed's own dyadic phase —
   untested). Mechanism: thermal picks are minimal-degree-
   biased, so crossings land at frontier + small; from a minimal
   landing 2^j + 1 the next frontier is 2^j away — affordable iff
   2^j <= D; the last affordable frontier is 2^{floor(log2 D) + 1}.
   An earlier measurement's c* = 5 at D = 10 is the instance floor(log2 10) + 2. The
   death reading is the BIT-LENGTH OF THE ALPHABET BOUND plus one:
   the mortality clock reads the dyadic size of the world's alphabet.

4. THE TAIL BREATHES WITH THE DYADIC PHASE OF D (rule for the cost;
   MC for the rates). Exceeding the mode needs creep + overshoot >=
   2^{J+1} - D (J = floor(log2 D)) — the distance from D to the next
   power of 2 — at thermal price ~2^{-beta * cost}. Exceedance at
   beta = 2 follows the cost: cost 1 (D = 3) 29/100, cost 2 (D = 6)
   14/100, cost 3 (D = 5) 2/100, cost 4 (D = 12) 1/60, cost 4 with
   rider starvation (D = 4, R = 3) 0/100, cost 8 (D = 8) 0/100,
   R = 0 (D = 2) IMPOSSIBLE (proved: no riders, gap unbridgeable).
   Temperature moves the tail, not the mode (D = 6, N = 400/beta):
   exceedance 18.75% / 12.50% / 3.25% at beta = 1.25 / 2 / 3,
   strictly monotone; modal reading 4 at all three betas. The earlier
   "temperature-independent c*" claim is PRECISED: the MODE is
   beta-independent; the DISTRIBUTION is not — the tail is a
   thermometer, and the dyadic phase of D sets its price. UNFROZEN
   find: the hot tail spreads BOTH ways — one beta = 1.25 run died
   BELOW the mode (reading 3, 1/400): the clock stranded on an
   EXPENSIVE leader (diagnosed state: deg-2 place at depth 5 is the
   clock, crossing 8 there costs 2r = 8 > 6, the deg-1 columns sit
   at depth 2 needing r = 7 > 6, every door spent — menu empty).
   Cold dynamics rides the cheapest column; heat can strand the
   clock on a column whose crossings the alphabet cannot pay.

5. THE SUPPORT LAW: witness = DP at every D (budget bound: rule;
   DP: exhaustive within the single-leader class; witnesses
   replayed). Ceiling c_max(D) for D = 2..12: 3, 4, 5, 5, 6, 6, 6,
   7, 7, 7, 7 — support jumps at D = 3, 4, 6, 9 where the mode jumps
   at powers of 2: TWO different staircases. Upper bounds: total
   leader depth <= seed + D * (#clock-raising moves) + R(D),
   #raises <= c - c_0 (every admissible move raises the clock or
   spends a door — finding 1's dichotomy), giving 2^{c-1} + 1 <=
   2 + D(c-1) + R(D) (rule, any trajectory, multi-column included) —
   tight except D in {5, 8, 12}; the exact single-leader optimum is
   a small DP over (depth, clock, creep spent), and an explicit
   chain achieving the DP value was replayed move-by-move through
   the real menu at every D (asserted admissible). EXACTNESS SCOPE:
   where budget = DP the ceiling is unconditional; at D = 5 a
   counting argument closes it (a foreign column's crossing gives
   the leader a rider <= D - 1, one less than an own crossing, and
   the budget slack is zero); at D in {8, 12} a multi-column
   strategy exceeding the DP by the one reading the budget still
   allows is not excluded (open — hand attempts at D = 8 fell short). Support ~
   2 log2 D vs mode ~ log2 D: thermal typicality reaches HALF the
   designed log-ceiling, the gap paid in riders. THE LATTICE TAX
   (scheduler fact, surfaced by a crash): creep delivery is a
   precedence-constrained assignment — opening a door closes its
   unopened divisor doors (finding 2), so a step's doors must respect
   divisor-before-multiple order and cover its need; naive ascending
   chunking FAILS (first run crashed at D = 9), while a lattice-legal
   allocation existed for every D <= 12 (no value gap here; whether
   the tax ever lowers c_max at larger D is open).

6. THE HALT-TIME LEDGER: T <= (D - 1) + (c_final - c_0) (rule, from
   finding 1's dichotomy: every move raises the clock — at most
   c_final - c_0 raises — or spends one of the D - 1 doors; asserted
   on all 1960 MC runs). An earlier run's median T = 13 at D = 10, beta = 2 is
   the equality instance (9 doors + 4 raises). Medians at D = 6 are
   7 / 8 / 8 at beta = 1.25 / 2 / 3 — weakly decreasing with
   temperature, as frozen, the strict drop at the hottest beta; the
   candidate mechanisms (door loss — a multiple opening first closes
   divisor doors — and multi-door combos, both favored by heavier
   picks) were not separately counted.

RUN RECORD (from the green run, 2026-07-10, 8390 checks, ~6 s, well
under 512 MB; a first run crashed in SE's replay chunker — the
lattice tax, finding 5 — with SA/SB already green; SA-SD numbers
identical on the fixed rerun).
  SA 20 states (8 constructed + 12 MC-reached at beta 2, D = 8) x
     all 1022 monics deg <= 9: menu == criterion, per-state assert.
  SB 4096 subsets x d = 2..14 vs the open-multiple law; the d = 6
     rescue asserted on S = {3} (door 6 open) and S = {12} (closed).
  SC beta = 2, T = 60: histograms 3:100 | 3:71,4:29 | 4:100 |
     4:98,5:2 | 4:86,5:14 | 5:100 | 5:59,6:1 at D = 2,3,4,5,6,8,12;
     mode majority + all-at-mode at D in {2, 8} + per-run halt-time
     bound + reading <= DP asserted.
  SD D = 6, N = 400 per beta: exceedance 75/50/13 of 400 at
     beta = 1.25/2/3; below-mode run diagnosed separately (seed
     27925 + 169); D = 2: 100/100 at reading 3.
  SE DP + budget + witness replay for D = 2..12 (table in finding 5);
     hand values 3, 5, 5, 7 at D = 2, 4, 5, 10 matched.

Related scripts: explore_function_field_melt.py (the melt; this
script is its finding 5's closure), explore_module_law.py
(the rank dichotomy; the two channels are its thermal menu form),
explore_function_field_lock.py (the cold sprawl).
"""

import random
import statistics
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_function_field_melt as melt
from explore_function_field_melt import (
    pdeg, pmul, ceil_log2, lam_pp, lcm, lam_of_fac, lam_after,
    thermal_menu, run_thermal, v2,
)

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


SEED_FAC = {2: 2}  # x^2 — the melt's seed (c_0 = 1)
C0 = 1


# ---------------------------------------------------- the two-channel criterion
def clock_of(fac):
    return max((ceil_log2(e) for e in fac.values()), default=0)


def odd_part(n):
    return n >> v2(n)


def criterion(fac, m):
    """Admissible iff the clock channel or the odd channel fires."""
    c = clock_of(fac)
    oddL = odd_part(lam_of_fac(fac))
    for g, e in melt._FAC[m].items():
        if fac.get(g, 0) + e > (1 << c):          # clock: beat the GLOBAL frontier
            return True
        if g not in fac and oddL % ((1 << pdeg(g)) - 1) != 0:  # odd: new Mersenne
            return True
    return False


def sa_criterion():
    print("== SA THE TWO-CHANNEL ADMISSIBILITY CRITERION ==")
    g6 = melt._IRR_BY_DEG[6][0]
    g4 = melt._IRR_BY_DEG[4][0]
    g3 = melt._IRR_BY_DEG[3][0]
    g2 = melt._IRR_BY_DEG[2][0]  # x^2+x+1 = 7
    states = [
        dict(SEED_FAC),
        {2: 2, 3: 16},
        {2: 1, 7: 1},
        {g6: 1, 2: 4},
        {g2: 1, g4: 1},
        {g3: 1, g6: 1},
        {2: 2, 3: 3, 7: 2, g3: 1},
        {2: 33, 7: 1},
    ]
    rng = random.Random(178)
    for s in range(4):
        fac = dict(SEED_FAC)
        for cut in (3, 3, 3):  # capture after moves 3, 6, 9
            fac2, picks, halted = run_thermal(fac, 2.0, 8, cut, "DYN", rng)
            fac = fac2
            states.append(dict(fac))
            if halted:
                break
    D = 9
    n_monic = 0
    for fac in states:
        menu, _, _, _ = thermal_menu(fac, 2.0, D, "DYN")
        menu = set(menu)
        agree = True
        n_monic = 0
        for m in range(2, 2 << D):
            if pdeg(m) < 1 or m >> pdeg(m) != 1:
                continue
            n_monic += 1
            if (m in menu) != criterion(fac, m):
                agree = False
                break
        ok(agree, f"SA criterion == menu on state {fac}")
    print(f"   {len(states)} states x {n_monic} monics: criterion == menu")


def sb_fresh_law():
    print("== SB THE FRESH LAW (the Mersenne lattice) ==")
    for S_bits in range(1 << 12):
        S = [d + 1 for d in range(12) if S_bits >> d & 1]
        L = 1
        for d in S:
            L = lcm(L, (1 << d) - 1)
        good = all(
            (L % ((1 << d) - 1) == 0) == any(d2 % d == 0 for d2 in S)
            for d in range(2, 15)
        )
        ok(good, f"SB fresh law on S = {S}")
    # the d = 6 rescue, named: no multiple of 6 open => 63 does not divide
    L3 = (1 << 3) - 1   # degree 3 open: brings 7 but not 9
    ok(lcm(L3, 1) % 63 != 0, "SB d=6: a multiple of 3 alone leaves door 6 open")
    L12 = (1 << 12) - 1  # 4095 = 63 * 65: multiple of 6 closes door 6
    ok(L12 % 63 == 0, "SB d=6: a multiple of 6 closes door 6 (the 3^2 rescue)")
    print("   4096 subsets x d = 2..14: divisibility == open-multiple")


# ------------------------------------------------------------------ support DP
def dp_support(D, seed_a=2, seed_c=1):
    """Exact single-leader max reading: BFS over (depth, clock, creep spent).

    Transitions: creep to position p <= 2^c (spending p - a of the door
    budget R(D)), then cross to any landing L in (2^c, p + D]. Returns
    (c_max, witness) — witness = [(creep, r, landing), ...]."""
    R = (D - 1) * (D - 2) // 2
    start = (seed_a, seed_c, 0)
    frontier_states = {start: None}  # state -> parent (state, creep, r)
    seen = {start}
    best = seed_c
    best_state = start
    queue = [start]
    while queue:
        a, c, spent = queue.pop()
        lo_p = max(a, (1 << c) - D + 1)
        hi_p = min(1 << c, a + (R - spent))
        for p in range(lo_p, hi_p + 1):
            for L in range((1 << c) + 1, p + D + 1):
                st = (L, ceil_log2(L), spent + (p - a))
                if st in seen:
                    continue
                seen.add(st)
                frontier_states[st] = ((a, c, spent), p - a, L - p)
                queue.append(st)
                if st[1] > best:
                    best = st[1]
                    best_state = st
    chain = []
    st = best_state
    while frontier_states[st] is not None:
        parent, creep, r = frontier_states[st]
        chain.append((creep, r, st[0]))
        st = parent
    chain.reverse()
    return best, chain


def budget_bound(D, seed_a=2, seed_c=1):
    R = (D - 1) * (D - 2) // 2
    c = seed_c
    while (1 << c) + 1 <= seed_a + D * (c + 1 - seed_c) + R:
        c += 1
    return c


def greedy_chain(D, seed_a=2, seed_c=1):
    """Cross with full r = D as soon as affordable, creeping the minimum
    needed each time — the depth-maximizing single-leader strategy."""
    R = (D - 1) * (D - 2) // 2
    spent, a, c = 0, seed_a, seed_c
    chain = []
    while True:
        creep = max(0, (1 << c) + 1 - D - a)
        if creep > R - spent:
            break
        p = a + creep
        chain.append((creep, D, p + D))
        spent += creep
        a, c = p + D, ceil_log2(p + D)
    return chain


def allocate_creep(needs, D):
    """Assign doors (degree d, room D - d) to creep steps: each step's
    assigned rooms must sum >= its need (riders shave freely, unopened
    doors don't close anything); a door's assigned DIVISORS must sit in
    earlier-or-equal steps (opening d' closes unopened doors d | d' —
    the fresh law). Returns {step: [doors]} or None."""
    doors = [d for d in range(2, D + 1) if D - d > 0]
    k = len(needs)
    found = {}
    nodes = [0]

    def rec(i, rem, assign):
        nodes[0] += 1
        if nodes[0] > 300000:
            return False
        if not any(rem):
            found.update(assign)
            return True
        if i == len(doors):
            return False
        if sum(D - d for d in doors[i:]) < sum(rem):
            return False
        d = doors[i]
        for j in range(k):
            if rem[j] == 0:
                continue
            if any(d % dd == 0 and assign.get(dd, j) > j
                   for dd in doors[:i]):
                continue
            assign[d] = j
            rem2 = list(rem)
            rem2[j] = max(0, rem2[j] - (D - d))
            if rec(i + 1, rem2, assign):
                return True
            del assign[d]
        return rec(i + 1, rem, assign)  # skip this door

    if rec(0, list(needs), {}):
        out = {}
        for d, j in found.items():
            out.setdefault(j, []).append(d)
        return out
    return None


def replay_witness(D, chain):
    """Drive a chain through the REAL menu: creep = riders on allocated
    doors (ascending within each step), crossings = x^r. Every move is
    asserted against thermal_menu. Returns the achieved reading, or
    None if the creep schedule has no lattice-legal allocation."""
    alloc = allocate_creep([c for c, _, _ in chain], D)
    if alloc is None:
        return None
    fac = dict(SEED_FAC)
    for i, (creep, r, landing) in enumerate(chain):
        s = creep
        for d in sorted(alloc.get(i, [])):
            if s == 0:
                break
            rid = min(D - d, s)
            g = melt._IRR_BY_DEG[d][0]
            m = pmul(g, 1 << rid)  # g * x^rid
            menu, _, _, _ = thermal_menu(fac, 2.0, D, "DYN")
            ok(m in menu, f"SE replay D={D}: door {d} + rider {rid} admissible")
            for gg, ee in melt._FAC[m].items():
                fac[gg] = fac.get(gg, 0) + ee
            s -= rid
        ok(s == 0, f"SE replay D={D}: creep {creep} delivered at step {i}")
        m = 1 << r  # x^r
        menu, _, _, _ = thermal_menu(fac, 2.0, D, "DYN")
        ok(m in menu, f"SE replay D={D}: crossing x^{r} admissible")
        for gg, ee in melt._FAC[m].items():
            fac[gg] = fac.get(gg, 0) + ee
        ok(fac[2] == landing, f"SE replay D={D}: landing {landing}")
    return v2(lam_of_fac(fac))


DP_CACHE = {}


def se_support():
    print("== SE THE SUPPORT LAW (budget >= DP >= replayed witness) ==")
    hand = {2: 3, 4: 5, 5: 5, 10: 7}
    print("   D   witness  DP  budget")
    for D in range(2, 13):
        cmax, dp_chain = dp_support(D)
        DP_CACHE[D] = cmax
        bb = budget_bound(D)
        ok(cmax <= bb, f"SE DP <= budget at D={D}")
        wit = None
        for chain in (dp_chain, greedy_chain(D)):
            got = replay_witness(D, chain)
            if got is not None:
                wit = got if wit is None else max(wit, got)
        ok(wit is not None, f"SE some witness chain replays at D={D}")
        ok(wit <= cmax, f"SE witness <= DP at D={D}")
        if D in hand:
            ok(cmax == hand[D], f"SE DP hand value at D={D}: {cmax} == {hand[D]}")
            ok(wit == hand[D], f"SE witness hand value at D={D}: {wit} == {hand[D]}")
        print(f"  {D:2d}   {wit:7d}  {cmax:2d}  {bb:6d}"
              f"   {'EXACT' if wit == cmax else 'BRACKET (lattice tax)'}")
    ok(DP_CACHE[5] < budget_bound(5), "SE budget NOT tight at D=5")


# ------------------------------------------------------------- mode + tail MC
def run_battery(D, beta, N, T, seed0):
    """N runs; returns (readings, times) with per-run HC6 bound asserted."""
    readings, times = [], []
    for i in range(N):
        rng = random.Random(seed0 + i)
        fac, picks, halted = run_thermal(dict(SEED_FAC), beta, D, T, "DYN", rng)
        ok(halted, f"SC/SD mortality: run halts (D={D}, beta={beta}, run {i})")
        cf = v2(lam_of_fac(fac))
        ok(len(picks) <= (D - 1) + (cf - C0),
           f"SC/SD halt-time bound (D={D}, beta={beta}, run {i})")
        readings.append(cf)
        times.append(len(picks))
    return readings, times


def sc_mode():
    print("== SC THE MODE LAW c*(D) = floor(log2 D) + 2 ==")
    battery = [(2, 100), (3, 100), (4, 100), (5, 100), (6, 100), (8, 100),
               (12, 60)]
    print("   D   mode  predicted  histogram")
    for D, N in battery:
        readings, _ = run_battery(D, 2.0, N, 60, 17800 + D)
        hist = {}
        for r in readings:
            hist[r] = hist.get(r, 0) + 1
        mode = max(hist, key=lambda r: hist[r])
        pred = D.bit_length() - 1 + 2  # floor(log2 D) + 2
        ok(mode == pred, f"SC modal reading at D={D}: {mode} == {pred}")
        ok(hist[mode] > N // 2, f"SC mode is a majority at D={D}")
        ok(max(readings) <= DP_CACHE[D], f"SC no run exceeds DP support D={D}")
        if D in (2, 8):
            ok(min(readings) == max(readings) == pred,
               f"SC all runs at mode (D={D})")
        print(f"  {D:2d}   {mode:4d}  {pred:9d}  {sorted(hist.items())}")


def sd_tail():
    print("== SD THE TAIL LAW (the dyadic phase of D) ==")
    D, N = 6, 400
    mode = D.bit_length() - 1 + 2
    rates, meds = {}, {}
    for beta in (1.25, 2.0, 3.0):
        readings, times = run_battery(D, beta, N, 60, 27800 + int(beta * 100))
        exceed = sum(1 for r in readings if r > mode)
        rates[beta] = exceed / N
        meds[beta] = statistics.median(times)
        ok(max(readings) <= DP_CACHE[D], f"SD no run exceeds DP (beta={beta})")
        hist = {}
        for r in readings:
            hist[r] = hist.get(r, 0) + 1
        ok(max(hist, key=lambda r: hist[r]) == mode,
           f"SD mode beta-independent at D=6 (beta={beta})")
        print(f"   beta={beta}: exceedance {exceed}/{N} = {rates[beta]:.4f}, "
              f"median T = {meds[beta]}, hist {sorted(hist.items())}")
    ok(0 < rates[2.0] < 0.4, "SD exceedance at beta=2 in (0, 0.4)")
    ok(rates[1.25] > rates[3.0], "SD tail strictly monotone across the span")
    ok(rates[1.25] >= rates[2.0] >= rates[3.0], "SD tail weakly monotone")
    ok(meds[1.25] <= meds[2.0] <= meds[3.0],
       "SD median halt time weakly decreasing with temperature")
    # D = 2: exceedance impossible (R(2) = 0, gap unbridgeable) — proved; MC
    readings, _ = run_battery(2, 2.0, 100, 60, 27999)
    ok(all(r == 3 for r in readings), "SD D=2 exceedance exactly 0")


def main():
    import time
    t0 = time.time()
    melt.build_tables()
    ok(v2(lam_of_fac(SEED_FAC)) == C0, "seed x^2 has c_0 = 1")
    sa_criterion()
    sb_fresh_law()
    se_support()   # DP first: SC/SD assert against it
    sc_mode()
    sd_tail()
    print(f"\nALL SECTIONS GREEN — {CHECKS} checks, {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
