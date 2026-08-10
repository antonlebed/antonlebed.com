"""explore_mode_staircase.py — the genesis MODE on breathing fields.

THE QUESTION. At Q's depth column the genesis MODE — the deep
suffix {a : Z_a(beta) < 1} of the wall-priced normalizer sequence — is
the order parameter of the irreducibility transition: its occupation
jumps 0 -> 1 at beta_col and its onset depth diverges logarithmically,
while the intensive route-entropy rate stays analytic
(explore_irreducibility_order.py; there e = 1, the column never
breathes). Does that story transfer to BREATHING columns (e >= 2),
where the cofactor oscillates among e accumulation values and
explore_clock_factorization.py measured a strict bracket pair
(max-headroom clock < deep clock)? Two clocks = one transition or two?
And is the MODE phase-sensitive where the VALUE is provably
defect-blind?

THE MECHANISM. Z_a(beta) = zeta_K(beta) -
cof_fin(E, a, beta) is order.py's normalizer transported by
explore_clock_factorization.py's machinery (T_a = cof - 1). Past the
entrant thresholds (exact convergence, established there) a state of
headroom class h has cof == V_h =
C_lim * sum_{delta<=h} p^(-beta delta) exactly, so each class carries
an asymptotic normalizer Z^(h) = zeta_K - V_h with its own CLASS CLOCK
beta^(h) (root of Z^(h) = 1). V_h strictly increasing in h forces
  beta^(e-1) < ... < beta^(1) < beta^(0),
the earlier bracket pair being the outermost members; post-transient the
classes are residue stripes mod e (tick period exactly e) of
density 1/e each. The candidate laws: the mode occupation is a
STAIRCASE with e steps; the stripes' residues read the tick phase
(torsion/chain) while the step temperatures read the menu alone; the
Cesaro rate r_e = (1/e) sum_h h2(1/(1+Z^(h))) is analytic through
every step and strictly below ln 2 for e >= 2; each step's onset
depth is bounded iff the transparent family is finite, diverging as
a* ~ e * ln(1/dbeta)/(beta^(h) ln p) through an infinite family.

THE PREDICTIONS (fixed and hand-attacked before this file existed):

MS1  THE STAIRCASE: per column the e class clocks are strictly
     ordered; the outermost pair matches explore_clock_factorization.py's
     printed deep/bracket clocks to 2e-3 (deep: sqrt-5 1.70395, sqrt-2
     1.63177, Q 1.60449, i 1.49669, sqrt2 1.48614, sqrt3 1.44746,
     zeta8 1.40019, zeta3 1.33357; bracket: sqrt-5 1.52998, sqrt2
     1.35701, sqrt-2 1.46224, i 1.35445, zeta8 1.22953, sqrt3 1.36555,
     zeta3 1.26810). On the usable range (past thresholds AND
     transient) the struck set at a sample beta in EVERY regime is
     exactly the union of classes with beta^(h) < beta: occupation
     0, 1/e, ..., 1. Showpiece zeta8: 0, 1/4, 1/2, 3/4, 1 across its
     five regimes.
MS2  THE STRIPES READ THE CHAIN: at mid-window beta the struck set is
     exactly the hr = 1 residue class (e = 2 columns); parities fixed
     from explore_clock_factorization.py's phase finding — sqrt3
     stripe EVEN (pre-ticks odd), zeta3 stripe
     ODD (pre-ticks even), the twins complementary; the sqrt3
     zeta3-splice TRANSPLANT flips its stripe parity to ODD while
     every step temperature moves < 1e-9. zeta8's window residues
     measured, not frozen (start-class race).
MS3  THE STEPS ARE MENU-ONLY: for every spliced column and every h,
     the roots through the TRUE chain's class-h cofactor, the NAIVE/
     transplant chain's, and the limit Z^(h) agree pairwise <= 1e-9
     (the CF3 argument per class: caps path-free, headroom = the
     class label itself).
MS4  THE RATE: r_e continuous through every step (|dr| shrinks with
     delta); Q (e = 1) peaks at ln 2 +- 1e-3 at its clock (order.py S1
     reproduced through the K machinery); every e >= 2 column peaks
     STRICTLY below: peak <= ln2 - 5e-4 (hand estimate of the
     tightest, zeta3: tax ~ 1.4e-3).
MS5  THE FINITE LENGTH: sqrt3 (menu PROVABLY finite, the CF8
     exclusions): class-0 and class-1 stripe onsets CONSTANT along
     beta^(h) + {1e-2 ... 1e-6}. Same boundedness in range at the
     2-adic columns (family = the Fermat primes; bounded iff that set
     is finite — conditional, stated not asserted) and at Q's
     2-column itself.
MS6  THE DIVERGENT LENGTH (zeta3, both classes): stage clocks at
     class-h states form a plateau staircase falling to beta^(h);
     plateau gap governed by the next family prime: ln(gap) vs
     ln(q_next) slope = -beta^(h) within 10%, R^2 > 0.99 over the
     resolvable plateaus (family 7, 19, 163, 487, 1459, 39367); the
     onset a*_h along a falling Delta ladder is non-decreasing,
     strictly larger at the end, and log-linear (R^2 > 0.97); the
     hand slope e/(beta^(h) ln 3) = 1.365 (class 0) / 1.436 (class 1)
     printed against the fit (staircase bias expected LOW, the
     order.py precedent 0.535 vs 0.609 — direction-only assert).

THE DESIGN. Everything downstream of explore_clock_factorization.py's
engine, imported: the
census + pump-continued TRUE chains (extend_chain, guard included),
the menus, cof_fin, zeta_K. Naive counterfactuals per column by
chain_from_law (sqrt3: the zeta3-splice transplant), thresholds
computed PER CHAIN (A10). Class clocks by bisection on
zeta_K - V_h - 1; struck tests by Z_a < 1 at explicit betas; the rate
on a 1.02..2.40 grid (asymptotic class values — the Cesaro tail
object) plus step-straddling deltas; onsets as min struck class-h
state (headroom read off the chain, transient included by
construction). Run: `python prime/code/explore_mode_staircase.py`.

FINDINGS (entered post-run, copied from printed output).

1. THE MODE STAIRCASE (MS1 hit; rule given the census-tier lambda
   inputs — the ordering is proved by V_h strict monotonicity, the
   struck sets verified in range): the breathing transition QUANTIZES
   into e geometric steps. Per column the e class clocks are strictly
   ordered with the earlier bracket pair as the outermost members, and
   the struck set at every sampled regime is exactly the union of
   classes with beta^(h) < beta — occupation 0, 1/e, ..., 1. The
   showpiece zeta8 (e = 4): clocks 1.22953 < 1.24259 < 1.27749 <
   1.40019, densities 0.00, 0.26, 0.52, 0.78, 1.00 (23 usable states,
   classes of 5-6). ANSWER to "two clocks = one transition or two":
   e transitions — the deep clock is where the mode COMPLETES (the
   pre-tick stripe strikes last), the bracket clock where it BEGINS.

2. THE STRIPES READ THE CHAIN, THE STEPS DON'T (MS2 + MS3 hit) — the
   hunched contrast lands. Mid-window the struck set is exactly the
   hr = 1 stripe at every e = 2 column; the twins are COMPLEMENTARY
   (sqrt3 stripe EVEN vs zeta3 ODD — opposite to their pre-tick
   parities); the sqrt3 zeta3-splice transplant FLIPS the stripe to
   ODD while all step temperatures hold to 1e-9 — per-class blindness
   verified at every class step of all eight columns (true/naive/
   limit roots pairwise 1e-9). The mode's GEOGRAPHY (which depths are
   struck) is chain/torsion-sensitive exactly where the VALUE and
   every step temperature are provably defect-blind. Unfrozen finds:
   stripe parity varies across the zoo (sqrt2/sqrt-2/i EVEN, sqrt-5
   ODD — each chain's own tick phase); zeta8's windows strike in
   headroom order, residues [3], [0,3], [0,1,3] mod 4 (start-class
   race, measured).

3. THE BREATHING TAX (MS4 hit; observation). r_e is the class-coin
   functional: its route-entropy READING is the solvable genesis's
   (a rule at Q's censused column, read from the process's inside view),
   carried to
   K columns by the crossfield clock convention — the numbers below
   are exact for the functional either way. The rate is
   continuous through every step — all e mode transitions are
   thermodynamically invisible (order.py's S3 split, now at every
   step of every column) — and its peak is STRICTLY below ln 2 at
   every e >= 2 column: tax 3.26e-3 (sqrt3), 3.78e-3 (zeta3),
   5.02e-3 (sqrt2), 7.10e-3 (sqrt-5), 7.33e-3 (i), 7.45e-3 (sqrt-2),
   9.78e-3 (zeta8); Q (e = 1) reproduces peak 0.693147 = ln 2 at
   1.605 through the K machinery (the order.py S1 regression).
   Perfect per-move irreducibility is exclusive to breathless
   columns: at most one stripe's coin can sit at 1/2 at any
   temperature, because the class clocks are distinct.

4. THE LENGTH READS THE TRANSPARENT FAMILY (MS5 partial miss +
   MS6 instrument miss, both adjudicated by asserts; the corrected
   claims verified exactly). sqrt3 (menu PROVABLY finite, thresholds
   done at a = 1): onsets CONSTANT (a* = 1 and 2) — an
   unconditionally bounded correlation length, the first-order-like
   jump. The Fermat columns' onset is NOT constant (the MS5 miss —
   the failed assert was the finding): it WALKS the Fermat entry
   thresholds and saturates at the full-menu state — Q 4, 6, 10, 18;
   sqrt2 9, 17, 33; i 11, 19, 35; zeta8 18, 34, 66 — so its
   boundedness past 65537 IS the Fermat finiteness question. zeta3
   walks its family 2*3^i + 1 EXACTLY: threshold law a = e*i + c_h
   (c_0 = 2, c_1 = 1; exact at i = 1, 2, 4, 5, 6, 9), the mechanism
   assert a*(Delta) = first plateau with gap < Delta exact at all 15
   ladder rungs per class, gap law ln(gap) vs ln(q_next) slope
   -1.3490 / -1.2860 vs -beta^(h) = -1.3336 / -1.2681 (R^2 0.99918 /
   0.99902) => the derived divergence a* = e*ln(1/Delta)/(beta^(h)
   ln 3) + O(1) along family members (the blind Delta-ladder fits
   1.117 / 1.098 vs hand 1.365 / 1.436 are staircase-biased as at
   order.py; the frozen R^2 > 0.97 linear-fit assert REFUSED at
   0.8526 — wrong instrument, the staircase is chunky exactly by the
   family's prime gaps i = 3, 7, 8 missing; replaced by the exact
   mechanism assert. The right instrument closed it: riser fits
   reach the law sub-percent at both classes,
   explore_astar_slope.py). THE OPEN-PROBLEM SYMMETRY (unresolved):
   a column's transition ORDER is pinned to its transparent
   family's finiteness — PROVED bounded at sqrt3 (the CF8 exclusions
   settle its family), OPEN exactly where the family's infinitude is
   open: Q's 2-adic seat is first-order-like iff the Fermat set is
   finite (heuristic: sum 2^-j converges, expect finite), zeta3's P3
   is second-order-like iff 2*3^i + 1 is infinite (heuristic: sum
   1/(i ln 3) diverges, expect infinite) — the correlation length
   reads the prime-counting HEURISTIC of the transparent family, and
   the two conjectured orders differ.

RUN RECORD. Engine ~15 s, 216 checks, all sections pass. Three
pre-green failures: (1) harness — S1's expected densities were
written ascending while the window samples descended (zeta8 printed
0.78/0.52/0.26 = the true staircase hottest-first; samples
reordered); (2) the MS5 miss above (Fermat onsets climb; corrected
assert: non-decreasing, >= 2 distinct values, saturated at the
full-menu state by Delta = 1e-9); (3) the MS6 miss above (linear-fit
R^2 replaced by the mechanism + threshold-law asserts). Every later
rerun green.
"""

import os
import sys
from math import log

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_clock_factorization import (                # noqa: E402
    Column, COLUMNS, run_census, fill_ram_lams, extend_chain,
    pre_ticks, headroom, CEN)
from explore_local_clock import chain_from_law           # noqa: E402
from explore_irreducibility_crossfield import bisect_root  # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


LN2 = log(2.0)

DEEP = {'sqrt-5': 1.70395, 'sqrt-2': 1.63177, 'Q': 1.60449, 'i': 1.49669,
        'sqrt2': 1.48614, 'sqrt3': 1.44746, 'zeta8': 1.40019,
        'zeta3': 1.33357}
BRACKET = {'sqrt-5': 1.52998, 'sqrt2': 1.35701, 'sqrt-2': 1.46224,
           'i': 1.35445, 'zeta8': 1.22953, 'sqrt3': 1.36555,
           'zeta3': 1.26810}


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log(p) - (1.0 - p) * log(1.0 - p)


def V_h(col, h, beta):
    own = sum(col.normP ** (-beta * d) for d in range(h + 1))
    return col.C_lim(beta) * own


def class_clock(col, h):
    return bisect_root(lambda b: col.zk(b) - V_h(col, h, b) - 1.0,
                       1.0001, 2.5)


def Z_fin(col, E, a, beta):
    return col.zk(beta) - col.cof_fin(E, a, beta)


def struck(col, E, a, beta):
    return Z_fin(col, E, a, beta) < 1.0


def threshold_a(col, E):
    return next(a for a in range(1, len(E) + 1)
                if col.caps_fin(E, a) == col.limit_caps)


def transient_end(col, E):
    pts = pre_ticks(E)
    i = len(pts) - 1
    while i > 0 and pts[i] - pts[i - 1] == col.e:
        i -= 1
    return pts[i]


def usable(col, E):
    lo = max(threshold_a(col, E), transient_end(col, E))
    hi = len(E) - col.e - 1
    return [a for a in range(lo, hi + 1) if headroom(E, a) is not None]


def class_states(col, E, h, rng):
    return [a for a in rng if headroom(E, a) == h]


def root_fin_class(col, E, h):
    a = next(a for a in reversed(usable(col, E)) if headroom(E, a) == h)
    return bisect_root(lambda b: col.zk(b) - col.cof_fin(E, a, b) - 1.0,
                       1.0001, 2.5)


def onset(col, E, h, beta, need=True):
    for a in range(1, len(E) - col.e):
        if headroom(E, a) == h and struck(col, E, a, beta):
            return a
    ok(not need, col.label + ": no struck class-%d state in range" % h)
    return None


def linfit(xs, ys):
    n = float(len(xs))
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    slope = sxy / sxx
    ss_res = sum((y - my - slope * (x - mx)) ** 2
                 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys)
    return slope, 1.0 - ss_res / ss_tot


def s1_staircase(cols, chains, clocks):
    print("S1 the staircase (MS1)")
    for col in cols:
        cl = clocks[col.key]
        for h in range(col.e - 1):
            ok(cl[h + 1] < cl[h] - 1e-6,
               col.label + ": class clocks not strictly ordered")
        ok(abs(cl[0] - DEEP[col.key]) < 2e-3,
           col.label + ": deep anchor off: %.5f" % cl[0])
        if col.e > 1:
            ok(abs(cl[col.e - 1] - BRACKET[col.key]) < 2e-3,
               col.label + ": bracket anchor off: %.5f" % cl[col.e - 1])
        E = chains[col.census_name]
        rng = usable(col, E)
        ok(all(len(class_states(col, E, h, rng)) >= 3
               for h in range(col.e)),
           col.label + ": usable range too thin")
        samples = [max(1.02, cl[col.e - 1] - 0.03)]
        samples += [(cl[h] + cl[h - 1]) / 2.0
                    for h in range(col.e - 1, 0, -1)]
        samples += [cl[0] + 0.05]
        dens = []
        for beta in samples:
            n_struck = 0
            for h in range(col.e):
                want = beta > cl[h]
                sts = class_states(col, E, h, rng)
                ok(all(struck(col, E, a, beta) == want for a in sts),
                   col.label + ": class %d not uniform at beta=%.4f"
                   % (h, beta))
                n_struck += len(sts) if want else 0
            dens.append(n_struck / float(len(rng)))
        want_d = [k / float(col.e) for k in range(col.e + 1)]
        ok(all(abs(d - w) < 0.20 for d, w in zip(dens, want_d)),
           col.label + ": density ladder off: %s" % dens)
        print("  %-18s clocks %s   densities %s" % (
            col.label, " ".join("%.5f" % b for b in cl),
            " ".join("%.2f" % d for d in dens)))


def s2_stripes(cols, chains, clocks, naive):
    print("S2 the stripes read the chain (MS2)")
    par = {}
    for col in cols:
        if col.e != 2:
            continue
        cl = clocks[col.key]
        mid = (cl[1] + cl[0]) / 2.0
        E = chains[col.census_name]
        rng = usable(col, E)
        hit = [a for a in rng if struck(col, E, a, mid)]
        ok(hit == class_states(col, E, 1, rng),
           col.label + ": struck set != the hr=1 stripe")
        ps = {a % 2 for a in hit}
        ok(len(ps) == 1, col.label + ": stripe not a single parity")
        par[col.key] = ps.pop()
        print("  %-18s mid-window %.5f   stripe = hr-1 class, parity %s"
              % (col.label, mid, "EVEN" if par[col.key] == 0 else "ODD"))
    ok(par['sqrt3'] == 0, "sqrt3 stripe not EVEN")
    ok(par['zeta3'] == 1, "zeta3 stripe not ODD")
    ok(par['sqrt3'] != par['zeta3'], "the twins' stripes not complementary")
    c3 = next(c for c in cols if c.key == 'sqrt3')
    En = naive['sqrt3']
    cl = clocks['sqrt3']
    mid = (cl[1] + cl[0]) / 2.0
    rngn = usable(c3, En)
    hitn = [a for a in rngn if struck(c3, En, a, mid)]
    ok(hitn == class_states(c3, En, 1, rngn),
       "sqrt3 transplant: struck set != the hr=1 stripe")
    psn = {a % 2 for a in hitn}
    ok(psn == {1}, "sqrt3 transplant stripe not ODD: %s" % psn)
    print("  sqrt3 TRANSPLANT (zeta3-splice): stripe parity flips to ODD;"
          " step temperatures held (S3)")
    c8 = next(c for c in cols if c.key == 'zeta8')
    E8 = chains[c8.census_name]
    cl8 = clocks['zeta8']
    rng8 = usable(c8, E8)
    for k in range(1, 4):
        mid = (cl8[k] + cl8[k - 1]) / 2.0
        hit = [a for a in rng8 if struck(c8, E8, a, mid)]
        want = sorted(a for h in range(k, 4)
                      for a in class_states(c8, E8, h, rng8))
        ok(hit == want,
           "zeta8: window %d struck set != classes >= %d" % (k, k))
        res = sorted({a % 4 for a in hit})
        print("  zeta8 window %d: struck classes h >= %d, residues %s"
              " mod 4" % (k, k, res))


def s3_blindness(cols, chains, clocks, naive):
    print("S3 the steps are menu-only (MS3)")
    for col in cols:
        E, En = chains[col.census_name], naive[col.key]
        cl = clocks[col.key]
        for h in range(col.e):
            bt = root_fin_class(col, E, h)
            bn = root_fin_class(col, En, h)
            ok(abs(bt - cl[h]) < 1e-9 and abs(bn - cl[h]) < 1e-9,
               col.label + ": class %d step not menu-only"
               " (%.12f / %.12f / %.12f)" % (h, bt, bn, cl[h]))
        print("  %-18s all %d class steps: true/naive/limit agree 1e-9"
              % (col.label, col.e))


def rate(col, beta):
    return sum(h2(1.0 / (1.0 + col.zk(beta) - V_h(col, h, beta)))
               for h in range(col.e)) / float(col.e)


def s4_rate(cols, clocks):
    print("S4 the rate: analytic, and the breathing tax (MS4)")
    grid = [1.02 + 0.005 * i for i in range(277)]
    for col in cols:
        cl = clocks[col.key]
        vals = [rate(col, b) for b in grid]
        peak = max(vals)
        b_peak = grid[vals.index(peak)]
        for h in range(col.e):
            d1 = abs(rate(col, cl[h] + 1e-3)
                     - rate(col, cl[h] - 1e-3))
            d2 = abs(rate(col, cl[h] + 1e-4)
                     - rate(col, cl[h] - 1e-4))
            ok(d2 < 2e-3 and d2 <= d1 + 1e-12,
               col.label + ": rate jumps at step %d (%.2e / %.2e)"
               % (h, d1, d2))
        if col.e == 1:
            ok(abs(peak - LN2) < 1e-3,
               col.label + ": e=1 peak != ln2: %.6f" % peak)
            ok(abs(b_peak - cl[0]) < 0.02,
               col.label + ": e=1 peak not at the clock")
            print("  %-18s peak %.6f = ln2 at %.3f (the order.py S1"
                  " regression)" % (col.label, peak, b_peak))
        else:
            ok(peak <= LN2 - 5e-4,
               col.label + ": no breathing tax: peak %.6f" % peak)
            print("  %-18s peak %.6f at %.3f   tax %.2e" % (
                col.label, peak, b_peak, LN2 - peak))


def s5_finite_length(cols, chains, clocks):
    print("S5 the finite length (MS5; the Fermat-ladder amendment)")
    for key in ('sqrt3', 'Q', 'sqrt2', 'i', 'zeta8'):
        col = next(c for c in cols if c.key == key)
        E = chains[col.census_name]
        cl = clocks[key]
        if key == 'sqrt3':
            # thresholds complete at a = 1: the frozen CONSTANT claim
            ladder = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
            for h in range(col.e):
                a_s = [onset(col, E, h, cl[h] + d) for d in ladder]
                ok(len(set(a_s)) == 1,
                   col.label + ": class %d onset not constant: %s"
                   % (h, a_s))
                print("  %-18s class %d onset a* = %d at every Delta in"
                      " [1e-2, 1e-6]" % (col.label, h, a_s[0]))
            continue
        # Fermat columns: the onset climbs the entry thresholds and
        # SATURATES at the full-menu state (bounded iff the menu is)
        ladder = [10.0 ** -k for k in range(2, 11)]
        a_s = [onset(col, E, 0, cl[0] + d) for d in ladder]
        ok(all(b >= a for a, b in zip(a_s, a_s[1:])),
           col.label + ": onset not non-decreasing: %s" % a_s)
        ok(len(set(a_s)) >= 2,
           col.label + ": onset never climbs in range: %s" % a_s)
        a_full = next(a for a in range(1, len(E) - col.e)
                      if headroom(E, a) == 0
                      and col.caps_fin(E, a) == col.limit_caps)
        ok(a_s[-1] == a_full and a_s[-2] == a_full,
           col.label + ": onset not saturated at the full-menu state"
           " %d: %s" % (a_full, a_s))
        print("  %-18s class 0 onsets %s -> saturates at a* = %d"
              " (the full-menu state)" % (col.label, a_s, a_full))


FAMILY_I = (1, 2, 4, 5, 6, 9)          # 2*3^i+1 prime, i <= 14


def s6_divergent_length(cols, chains, clocks):
    print("S6 the divergent length (MS6, zeta3; the mechanism assert)")
    col = next(c for c in cols if c.key == 'zeta3')
    E = chains[col.census_name]
    cl = clocks['zeta3']
    hi = len(E) - col.e - 1
    fam = [2 * 3 ** i + 1 for i in FAMILY_I]
    ok(sorted(m[1] for m in col.menu) == sorted(fam + [4]),
       "zeta3 menu != the family + the 4-entrant")
    for h in range(col.e):
        sts = [a for a in range(1, hi + 1) if headroom(E, a) == h]
        plateaus, seen = [], set()
        for a in sts:
            caps = tuple(col.caps_fin(E, a))
            if caps in seen:
                continue
            seen.add(caps)
            b_a = bisect_root(
                lambda b: col.zk(b) - col.cof_fin(E, a, b) - 1.0,
                1.0001, 2.5)
            missing = [m[1] for m, c in zip(col.menu, caps) if c < m[3]]
            plateaus.append((a, max(b_a - cl[h], 0.0),
                             min(missing) if missing else None))
        # the threshold law: member i enters at a = e*i + c_h exactly
        entry = {}
        for q, i in zip(fam, FAMILY_I):
            idx = next(j for j, m in enumerate(col.menu) if m[1] == q)
            entry[i] = next(a for a in sts
                            if col.caps_fin(E, a)[idx] > 0)
        c_h = entry[1] - col.e * 1
        ok(all(entry[i] == col.e * i + c_h for i in FAMILY_I),
           "zeta3 class %d: thresholds not e*i + c: %s" % (h, entry))
        # the gap law over the family plateaus
        pts = [(log(q), log(g)) for a, g, q in plateaus
               if q in fam and 5e-8 < g < 0.1]
        ok(len(pts) >= 4, "zeta3 class %d: too few plateaus: %d"
           % (h, len(pts)))
        slope, r2 = linfit([x for x, _ in pts], [y for _, y in pts])
        ok(abs(slope + cl[h]) < 0.10 * cl[h],
           "zeta3 class %d: gap slope %.4f vs -beta^(h) %.4f"
           % (h, slope, -cl[h]))
        ok(r2 > 0.99, "zeta3 class %d: gap fit R^2 %.5f" % (h, r2))
        # the mechanism assert: a*(Delta) = first plateau with gap < Delta
        deltas = [10.0 ** (-k / 3.0) for k in range(4, 19)]
        a_s = [onset(col, E, h, cl[h] + d) for d in deltas]
        for d, a_star in zip(deltas, a_s):
            want = min(a for a, g, q in plateaus if g < d)
            ok(a_star == want,
               "zeta3 class %d: onset %d != mechanism %d at %.2e"
               % (h, a_star, want, d))
        ok(a_s[-1] > a_s[0], "zeta3 class %d: onset not climbing" % h)
        xs = [log(1.0 / d) for d in deltas]
        os_, _ = linfit(xs, [float(a) for a in a_s])
        hand = col.e / (cl[h] * log(3.0))
        print("  class %d: thresholds a = %d*i + %d at i = %s; gap slope"
              " %.4f (law %.4f, R^2 %.5f);" % (
                  h, col.e, c_h, list(FAMILY_I), slope, -cl[h], r2))
        print("    onsets %s exact by the mechanism; fit slope %.3f"
              " (hand law %.3f, staircase-biased)" % (
                  sorted(set(a_s)), os_, hand))


def main():
    print("THE MODE STAIRCASE — the genesis mode on breathing fields")
    print("=" * 64)
    run_census()
    fill_ram_lams()
    cols = [Column(*row) for row in COLUMNS]
    chains = {c.census_name: extend_chain(c.census_name, c.e, c.A)
              for c in cols}
    naive = {}
    for col in cols:
        if col.key == 'sqrt3':
            naive[col.key] = chain_from_law(col.p, col.e, col.A,
                                            splice=(1, 4))
        else:
            naive[col.key] = chain_from_law(col.p, col.e, col.A)
    clocks = {c.key: [class_clock(c, h) for h in range(c.e)]
              for c in cols}
    s1_staircase(cols, chains, clocks)
    s2_stripes(cols, chains, clocks, naive)
    s3_blindness(cols, chains, clocks, naive)
    s4_rate(cols, clocks)
    s5_finite_length(cols, chains, clocks)
    s6_divergent_length(cols, chains, clocks)
    print("\nALL SECTIONS PASS (%d checks)" % CHECKS)


if __name__ == "__main__":
    main()
