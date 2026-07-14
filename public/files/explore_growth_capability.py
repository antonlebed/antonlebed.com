"""
explore_growth_capability.py — capability-directed growth, sibling of
explore_growth_laws.py.

THE QUESTION. explore_growth_laws.py's growth laws demand STRUCTURE
(independence, new dynamics, transparency) and trichotomize into the
three fates. This script points the demand at genesis-ladder ROWS
instead: a growth law that wants a CAPABILITY (an order-m element, the
ECC substrate, cyclic units, sqrt(-1)). Design-by-choice picks the
cheapest modulus with the capability outright: OPT(C) = least N such
that Z/N has C. What does design-by-GROWTH pay for the same capability
— and does it ever beat choice?

LAWS. State = modulus N; a move multiplies N by some m' >= 2.
  LAW-JUMP  (patient acquisition): one move, the least m' such that
            Z/(N*m') has the capability.
  LAW-STEP  (impatient acquisition): every move must make strict
            PROGRESS — for the order-m capability, the set of covered
            parts (prime powers q^a || m with q^a | lambda) must
            strictly grow at every step.
  LAW-KEEP  (preservation): grow forever, every move keeping a
            FORALL-shaped capability alive (variants below add
            independence or one-step lookahead).

FINDINGS (tiers stated inline; run record below; all sections assert).

1. THE JUMP IDENTITY (rule, definitional; asserted m <= 200). From
   seed 1, LAW-JUMP's one move IS design-by-choice: the least m' with
   m | lambda(m') is by definition the least N with the capability.
   Patient growth and choice are the same object.

2. THE MYOPIA GAP (single-part rule proved; sweep m <= 200 measured).
   All 60 single-part m (prime powers) tie exactly in one step (rule,
   proved: with one part, the first progress step IS the jump = OPT).
   Multi-part m gap 126/139, with 13 ties. The gap mechanism:
   design-by-choice can buy several parts with ONE move — a combo
   prime (p == 1 mod q1*q2, the Linnik composites of the birthday
   formula) or the right prime power — but the greedy
   takes the cheapest move that makes ANY progress, and once a cheap
   single-part step exists the combo is never picked. Specimens
   (picks -> GRW vs OPT):
     m=15   7,11     -> 77   vs 31  (ratio 2.48; 31 == 1 mod 15)
     m=105  7,7,11   -> 539  vs 211 (ratio 2.55; 211 == 1 mod 105)
     m=190  3,11,191 -> 6303 vs 191 (ratio 33.0, in-range worst: 191
            covers ALL of parts {2,5,19} — 190 = 191-1 — but the
            greedy has already bought parts 2 and 5 cheaply and pays
            for 191 anyway)
   Ratio stats over the 126 gapped m: mean 4.17, max 33.0; the gap
   grows with part count (2 parts: 95 m, mean 3.59; 3 parts: 31 m,
   mean 5.95; no m <= 200 has 4 parts — 210 is the first). THE
   FACTORED-OPTIMUM TIE (observation): the 13 ties are trajectories
   whose cheap steps multiply out to the optimum itself — deepening
   a prime power (5 of 13; m=20: pick 5 covering part 4, then
   deepen 5 -> 25 = OPT) or buying the optimal prime pair one part
   at a time (8 of 13; m=80: 11 then 17, and 187 = 11*17 is OPT).
   Impatience has a measured price, and the price is the combined
   moves forgone.

3. THE GREEDY-OPTIMAL CLASS (rule, proved + verified). Channel-COUNT
   capabilities are where growth ties choice: the ECC substrate
   (omega(N) >= 4 independent channels, the d=4 split's carrier) has
   OPT = 210 = 2*3*5*7 (verified by full sweep N < 600000), and
   progress-greedy growth from seed 1 reaches exactly 210 (the
   least-new lemma, echoing explore_growth_laws.py: each progress step
   is the next prime). Same at every k: omega >= 7 (the rate > 1/2
   substrate)
   gives OPT = 510510 = greedy. Proof of the class: a modulus with k
   independent channels has k distinct prime-power factors, and a
   product of k distinct prime powers is >= the product of its k
   distinct prime bases >= p_k# — the primorial prefix is the global
   minimum, and greedy walks it. "Grow the cheapest ECC-bearing
   tower" picks 210: design-by-growth = design-by-choice on exactly
   the demands that explore_growth_laws.py's structural laws already
   grow.

4. MYOPIA MORTALITY — THE CYCLIC TRAP (rule, proved + verified).
   LAW-KEEP on "U(N) is cyclic" (classification N in {1,2,4} u {p^e}
   u {2 p^e}, textbook; re-verified two ways in range, S4a/S4b):
   the strict greedy from seed 1 walks 1 -> 2 -> 4 and DIES — no
   m' >= 2 keeps U(4 m') cyclic (verified to 10^4; proved: 4m' with
   an odd prime factor has two even-order components C2 x U(p^e);
   4m' a pure 2-power >= 8 has U = C2 x C2^(a-2)). The capability is
   NOT mortal: the column 2*3^e is cyclic at every depth (verified
   e <= 12) — the greedy chose the one door that locks. One step of
   lookahead (pick the least move that keeps the capability AND a
   successor move) escapes forever: 1 -> 2 -> 6 -> 18 -> ... = the
   2*3^e column, 12/12 steps verified — and lands in the DEPTH fate:
   preserving cyclicity forces a p-adic column (breadth kills
   cyclicity at once). Impatience is not only costly (finding 2); it
   can be FATAL, and one move of patience is the full cure here.

5. THE EMERGENT DESIGNED TOWER (rule, proved + verified). LAW-KEEP on
   "sqrt(-1) exists" (solvability of x^2 = -1: v2(N) <= 1 and every
   odd prime channel == 1 mod 4; criterion re-verified by brute
   force N <= 3000) with independence moves (gcd(m', N) = 1): from
   every capability-bearing seed tested (1, 2, 5, 10, 13, 65) the
   picks are
   EXACTLY the missing admissible primes — 2 and the primes == 1 mod
   4 — in increasing order (15 steps per seed; from seed 1:
   2, 5, 13, 17, 29, 37, 41, ...). THE CONSTRAINED LEAST-NEW LEMMA
   (proved): the least coprime capability-keeping m' is a PRIME from
   the admissible set — 2 (when absent) or p == 1 mod 4 — because
   any admissible composite is a product of >= 2 new admissible
   primes counted with multiplicity, each >= the least new
   admissible prime q, so the composite is >= q^2 > q. Constrained
   healing follows by the
   same induction as explore_growth_laws.py's healing rule. The
   punchline: the designed-tower knob ("skip 3 and sqrt(-1) lives")
   is an OUTPUT of capability-directed growth — the
   Gaussian tower 2*5*13*17*29*... grows itself from the demand
   alone. Design-by-growth DISCOVERS designed towers.

THE SYNTHESIS. Does design-by-growth ever beat design-by-choice? On
size-cost, NEVER — growth's terminal modulus is a feasible point of
the minimization choice solves (definitional; asserted GRW >= OPT
throughout). The real content is the trichotomy of the difference:
growth TIES choice exactly on the indivisible demands (single-part
capabilities, channel-count capabilities — the same demands
explore_growth_laws.py's structural fates grow) and by luck on the 13
factored-optimum ties; it OVERPAYS the myopia gap on 126/139 separable
capabilities (the combined moves are invisible to progress reward);
it DIES in preservation traps choice never enters (the cyclic trap
at 4). What growth buys instead is procedure: each move
is a bounded local scan, where choice searches an unbounded space it
must already understand. Read as reward design (observation-tier
commentary): LAW-JUMP is sparse reward,
LAW-STEP is shaped reward, and the shaping provably costs a factor
that grows with how decomposable the goal is — in the smallest
algebra playground that can state it. Honest limit inherited from
explore_growth_laws.py: every law still prices candidates by SIZE
("least m'") — the deleted archimedean place remains the cost axis of
growth (dissected in explore_size_crystallization.py — the
crystallization split; the archimedean axis).

RUN RECORD (python explore_growth_capability.py, ~0.5 s, trivial
memory):
  S1 jump identity: 199/199 m (LAW-JUMP pick == OPT(m))
  S2 myopia sweep m = 2..200: 60 single-part m all tie (GRW == OPT,
     one step); 139 multi-part m: 126 gap, 13 tie (20, 54, 55, 80,
     92, 123, 144, 145, 147, 159, 164, 171, 184 — tie table printed
     with picks and OPT); GRW >= OPT 199/199; specimen table + ratio
     stats above reproduced
  S3 greedy-optimal class: omega sweep N < 600000 (OPT(omega>=k) =
     p_k# for k = 4..7); greedy picks = 2,3,5,7,11,13,17
  S4 cyclic trap: lambda==phi test vs brute group structure N <= 300
     (S4a), classification vs lambda==phi N <= 10000 (S4b); no move
     from 4 (scan to 10^4); 2*3^e cyclic e = 1..12; strict greedy
     halts at 4; lookahead-1 survives 12/12 steps on the 2*3^e column
  S5 emergent designed tower: criterion vs brute N <= 3000; 6 seeds
     x 15 steps, picks == missing admissible primes in order
  TOTAL 14,089 checks, exit 0.

ADJUDICATION vs the predictions fixed before the run (git history):
PR1, PR3, PR5, PR6 landed as stated. PR4 landed with one imprecision:
it predicted lookahead-1 "picking 3 each time"; the measured picks
are [2, 3, 3, ...] — the first pick is 2 (the prediction's own
1 -> 2 -> 6 -> ... trajectory implies it; the "each time" clause
holds from step 2). PR2 landed on its number
(predicted >= 90% of multi-part m gapped; measured 126/139 = 90.6%)
but MISSED the tie mechanism: the prediction allowed ties only where
one cheap prime covers everything; the actual 13 ties are
factored-optimum coincidences — deepening or pair shaped (finding
2), a
mechanism the hand analysis did not foresee — the hand-derived
specimens m=6 (claimed 21) and m=105 (claimed 2233) were WRONG for
the same reason (measured: 9 via the 3 -> 9 deepening; 539 via
7 -> 49): the greedy exploits prime-power deepening the hand
derivation ignored.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from math import gcd

CHECKS = 0


def check(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ---------------------------------------------------------------- tools

def spf_sieve(n):
    spf = list(range(n + 1))
    i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


SPF_CAP = 60000
SPF = spf_sieve(SPF_CAP)


def factor_small(n):
    """Factor n <= SPF_CAP via the sieve."""
    f = {}
    while n > 1:
        p = SPF[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        f[p] = e
    return f


def lam_pp(p, e):
    if p == 2:
        return 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
    return p ** (e - 1) * (p - 1)


def lcm(a, b):
    return a // gcd(a, b) * b


def lam_fac(fac):
    L = 1
    for p, e in fac.items():
        L = lcm(L, lam_pp(p, e))
    return L


def phi_fac(fac):
    F = 1
    for p, e in fac.items():
        F *= p ** (e - 1) * (p - 1)
    return F


def merge(fa, fb):
    f = dict(fa)
    for p, e in fb.items():
        f[p] = f.get(p, 0) + e
    return f


def parts_of(m):
    """Prime powers q^a || m."""
    return {q ** a for q, a in factor_small(m).items()}


# Lambda for every N up to a search cap (design-by-choice's table).
OPT_CAP = 60000
LAM = [0, 1] + [lam_fac(factor_small(n)) for n in range(2, OPT_CAP + 1)]


def opt_order(m):
    """Design-by-choice: least N with an order-m element (m | lambda)."""
    for n in range(2, OPT_CAP + 1):
        if LAM[n] % m == 0:
            return n
    raise AssertionError(f"OPT({m}) beyond cap")


# ------------------------------------------------- S1 + S2: acquisition

def grw_order(m, scan_cap=10000):
    """LAW-STEP: progress-greedy acquisition of an order-m element."""
    parts = parts_of(m)
    fac, val, covered, picks = {}, 1, set(), []
    while covered != parts:
        for mp in range(2, scan_cap + 1):
            f2 = merge(fac, factor_small(mp))
            L2 = lam_fac(f2)
            cov2 = {q for q in parts if L2 % q == 0}
            if covered < cov2:
                fac, val, covered = f2, val * mp, cov2
                picks.append(mp)
                break
        else:
            raise AssertionError(f"GRW({m}): no progress step found")
    return val, picks


def s1_s2():
    print("S1/S2: acquisition -- jump identity + the myopia sweep, m <= 200")
    single_ties, multi = 0, []
    for m in range(2, 201):
        opt = opt_order(m)
        # S1 jump identity: LAW-JUMP from seed 1 IS the OPT search.
        jump = next(n for n in range(2, OPT_CAP + 1) if LAM[n] % m == 0)
        check(jump == opt, f"jump != opt at m={m}")
        grw, picks = grw_order(m)
        check(grw >= opt, f"GRW < OPT at m={m}")  # PR6 feasibility
        if len(parts_of(m)) == 1:
            check(len(picks) == 1 and grw == opt,
                  f"single-part m={m} not a one-step tie")
            single_ties += 1
        else:
            multi.append((m, grw, opt, grw / opt, picks))
    gapped = [t for t in multi if t[1] > t[2]]
    ties = [t for t in multi if t[1] == t[2]]
    print(f"  single-part m: {single_ties} -- all one-step ties (GRW == OPT)")
    print(f"  multi-part m:  {len(multi)} -- gapped {len(gapped)}, "
          f"ties {len(ties)}")
    for m, grw, opt, _, picks in ties:
        print(f"    tie m={m}: picks {picks} -> {grw} == OPT")
    ratios = [t[3] for t in gapped]
    worst = max(gapped, key=lambda t: t[3])
    print(f"  ratio GRW/OPT: mean {sum(ratios)/len(ratios):.2f}, "
          f"max {worst[3]:.2f} at m={worst[0]} "
          f"(GRW {worst[1]} picks {worst[4]} vs OPT {worst[2]})")
    by_parts = {}
    for m, grw, opt, r, _ in gapped:
        by_parts.setdefault(len(parts_of(m)), []).append(r)
    for k in sorted(by_parts):
        rs = by_parts[k]
        print(f"    {k} parts: {len(rs)} m, mean ratio {sum(rs)/len(rs):.2f}")
    for m in (6, 15, 105):
        t = next(t for t in multi if t[0] == m)
        print(f"  specimen m={m}: picks {t[4]} -> {t[1]} vs OPT {t[2]} "
              f"(ratio {t[3]:.2f})")
    return len(gapped), len(ties)


# ------------------------------------------- S3: the greedy-optimal class

def s3():
    print("S3: channel-count capabilities -- the greedy-optimal class")
    cap = 600000
    # omega sieve (count distinct prime divisors)
    omega = bytearray(cap + 1)
    is_comp = bytearray(cap + 1)
    for p in range(2, cap + 1):
        if not is_comp[p]:
            for mult in range(p, cap + 1, p):
                omega[mult] += 1
                if mult > p:
                    is_comp[mult] = 1
    primorial = {4: 210, 5: 2310, 6: 30030, 7: 510510}
    for k, pk in primorial.items():
        first = next(n for n in range(2, cap + 1) if omega[n] >= k)
        check(first == pk, f"OPT(omega>={k}) != p_{k}#")
        print(f"  OPT(omega >= {k}) = {first} = p_{k}#  (full sweep)")
    # progress greedy on channel count from seed 1
    fac, val, picks = {}, 1, []
    while len(fac) < 7:
        for mp in range(2, 100):
            f2 = merge(fac, factor_small(mp))
            if len(f2) > len(fac):
                fac, val = f2, val * mp
                picks.append(mp)
                break
    check(picks == [2, 3, 5, 7, 11, 13, 17], "greedy channel picks")
    check(val == 510510, "greedy terminal")
    print(f"  greedy picks {picks}: 210 at k=4, 510510 at k=7 == OPT "
          f"(growth = choice on this class)")


# ------------------------------------------------- S4: the cyclic trap

def unit_orders(n):
    us = [x for x in range(1, n) if gcd(x, n) == 1]
    orders = []
    for x in us:
        y, o = x % n, 1
        while y != 1:
            y = y * x % n
            o += 1
        orders.append(o)
    return orders


def cyclic(fac):
    return lam_fac(fac) == phi_fac(fac)


def classified_cyclic(fac):
    ps = sorted(fac)
    if not ps:
        return True  # N = 1
    if ps == [2]:
        return fac[2] <= 2  # 2, 4
    odd = [p for p in ps if p != 2]
    return len(odd) == 1 and (2 not in fac or fac[2] == 1)  # p^e, 2p^e


def s4():
    print("S4: LAW-KEEP cyclic -- the trap at 4")
    # S4a: the lambda==phi test against brute-force group structure
    for n in range(1, 301):
        fac = factor_small(n)
        if n <= 2:
            check(cyclic(fac), "tiny cyclic")
            continue
        orders = unit_orders(n)
        exponent = 1
        for o in orders:
            exponent = lcm(exponent, o)
        check(exponent == lam_fac(fac), f"exponent != lambda at {n}")
        check((max(orders) == phi_fac(fac)) == cyclic(fac),
              f"cyclicity test at {n}")
    print("  lambda==phi test == brute cyclicity, N <= 300")
    # S4b: classification in range
    for n in range(1, 10001):
        fac = factor_small(n)
        check(cyclic(fac) == classified_cyclic(fac),
              f"classification at {n}")
    print("  classification {1,2,4,p^e,2p^e} exact, N <= 10000")
    # the strict greedy walks 1 -> 2 -> 4 and dies
    fac, val, picks = {}, 1, []
    dead = False
    while not dead:
        for mp in range(2, 10001):
            f2 = merge(fac, factor_small(mp))
            if cyclic(f2):
                fac, val = f2, val * mp
                picks.append(mp)
                break
        else:
            dead = True
        if len(picks) > 10:
            break
    check(picks == [2, 2] and val == 4 and dead,
          "strict greedy should die at 4")
    print(f"  strict greedy: picks {picks} -> N=4, then NO move to 10^4 "
          f"(proved: 4m' always non-cyclic) -- MYOPIA MORTALITY")
    # the capability itself is immortal: the 2*3^e column
    for e in range(1, 13):
        check(cyclic({2: 1, 3: e}), f"2*3^{e} not cyclic")
    print("  2*3^e cyclic for e = 1..12 -- the greedy chose the locking door")
    # lookahead-1 escapes
    fac, val, picks = {}, 1, []
    for _ in range(12):
        for mp in range(2, 10001):
            f2 = merge(fac, factor_small(mp))
            if not cyclic(f2):
                continue
            has_succ = any(cyclic(merge(f2, factor_small(m2)))
                           for m2 in range(2, 200))
            if has_succ:
                fac, val = f2, val * mp
                picks.append(mp)
                break
        else:
            raise AssertionError("lookahead-1 stuck")
    check(picks == [2] + [3] * 11, "lookahead-1 column")
    check(cyclic(fac), "lookahead-1 terminal cyclic")
    print(f"  lookahead-1: picks {picks[:4]}... 12/12 alive on the 2*3^e "
          f"column -- one step of patience is the cure (the DEPTH fate)")


# --------------------------------------- S5: the emergent designed tower

def sqrt_m1_brute(n):
    return any(x * x % n == n - 1 for x in range(n)) or n == 1


def sqrt_m1_crit(fac):
    if fac.get(2, 0) > 1:
        return False
    return all(p % 4 == 1 for p in fac if p != 2)


def s5():
    print("S5: LAW-KEEP sqrt(-1) + independence -- the emergent designed tower")
    for n in range(1, 3001):
        check(sqrt_m1_brute(n) == sqrt_m1_crit(factor_small(n)),
              f"criterion at {n}")
    print("  solvability criterion (v2 <= 1, odd p == 1 mod 4) exact, "
          "N <= 3000")
    admissible = [2] + [p for p in range(5, 3000)
                        if SPF[p] == p and p % 4 == 1]
    for seed in (1, 2, 5, 10, 13, 65):
        fac, picks = factor_small(seed), []
        check(sqrt_m1_crit(fac), f"seed {seed} lacks the capability")
        for _ in range(15):
            for mp in range(2, SPF_CAP):
                if any(mp % p == 0 for p in fac):
                    continue  # independence: gcd(m', N) = 1
                f2 = merge(fac, factor_small(mp))
                if sqrt_m1_crit(f2):
                    fac = f2
                    picks.append(mp)
                    break
        missing = [p for p in admissible if p not in factor_small(seed)
                   and seed % p != 0][:15]
        check(picks == missing, f"seed {seed}: picks != missing admissible")
    print("  6 seeds x 15 steps: picks == the missing admissible primes "
          "(2 and p == 1 mod 4) in increasing order -- constrained healing;"
          "\n  the Gaussian designed tower grows itself.")


if __name__ == "__main__":
    s1_s2()
    s3()
    s4()
    s5()
    print(f"\nALL SECTIONS PASS -- {CHECKS} checks, exit 0")
