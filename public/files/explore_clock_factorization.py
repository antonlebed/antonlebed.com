"""explore_clock_factorization.py — the beta_col re-read over the defect zoo.

THE QUESTION. The deep clock — the tick-state accumulation normalizer's
interior root beta_col — was conjectured DEFECT-BLIND (argument, unverified
numerically: a splice shifts tick phase, not the asymptotic gap structure
the accumulation values read). explore_local_clock.py's census supplies the
controlled pairs: seven spliced fields with measured seat defects, the Q_3
parity twins (same (p,e,f), opposite tick parities), and Q_2(zeta_8) (e = 4,
the largest arrival extra). Verify or refute; if verified, pin what each
layer of the clock DOES read.

THE MECHANISM (read off the crossfield analysis (explore_irreducibility_crossfield.py)
and the census). Column at place P over p in global field K (all columns here
f = 1), state P^a, wall lambda(O/P^a) = lcm(p-1, E(a)) with E the census
1-unit chain. Transparency of a move m: lambda(state*m) = lambda(state) —
by CRT componentwise caps (the state lemma), so the finite cofactor is

  cof(a, beta) = prod_{external entrants} [sum_{j<=cap_h(a)} N_h^(-beta j)]
                 * sum_{delta=0}^{hr(a)} p^(-beta delta)

where cap_h(a) is the entrant's exponent cap under the CURRENT wall and
hr(a) = max{b : E(b) = E(a)} - a is the own-column headroom (0 exactly at
pre-tick states — crossfield's a = 2^s convention). THE DEEP CLOCK := the
pre-tick-state limit's root (this is crossfield SYN's drop_own convention).

WHY BLINDNESS IS EXPECTED (theorem-shaped): caps are
divisibility-monotone in E(a) and E is non-decreasing, so the limit caps
are PATH-FREE (any chain with E -> inf passes every finite threshold); and
hr = 0 at pre-tick states by definition. The deep clock is then a function
of the LIMIT MENU alone — proved given the state lemma + the local lambda
inputs (census tier). This engine verifies the premises numerically
(chains, menus, exact finite-a convergence) and the regressions, and
measures what is left in each layer.

THE PREDICTIONS (fixed and hand-attacked before this file existed;
later amendments included):

CF1  EXACT CONVERGENCE (sharpened by the hand attack from "asymptotic
     < 1e-7" — every entrant threshold is FINITE): at pre-tick states past
     the last threshold, cof == C_lim exactly (<= 1e-12 relative); the
     pre-tick sequence is a non-decreasing staircase before that. Worked
     instance frozen: sqrt-5 P2 at beta = 1.5, a = 10: cof = C_lim =
     (1+3^-1.5)^2 (1+5^-1.5) = 1.54912.
CF2  THE ACCUMULATION SET is {C_lim * sum_{delta<=h} p^(-beta delta) :
     h = 0..e-1}: e distinct values, cof(a) == V_{hr(a)} at every a past
     the thresholds; post-transient hr cycles 0..e-1 with period e (e = 1
     degenerate: a single value, no breathing).
CF3  THE BLINDNESS: per spliced field the naive counterfactual chain
     (chain_from_law, no splice) reaches the SAME C_lim and the same deep
     clock (roots through the true-chain and naive-chain finite cofactors
     agree <= 1e-9 with the limit root), while the finite-a cofactors
     DIFFER in the transient (the defect is finite-time-visible).
     Instances: Q (N7), sqrt-5 (N8), sqrt2 (N9), sqrt-2 (N10), i (N11),
     zeta_3 (N12), zeta_8 (N13).
CF4  THE PHASE reads the splice/torsion (conventions pinned by hand: the
     census docstring's "ticks" = my pre-tick + 1): post-transient
     pre-tick parities — sqrt3 ODD vs zeta_3 EVEN (the twins, opposite);
     at sqrt2/sqrt-2/i the splice flips the naive EVEN pre-ticks to ODD.
     zeta_8's phase measured, not hand-frozen (a start-class race).
CF5  THE TWINS' DEEP CLOCKS DIFFER ONLY BY MENU: {sqrt3 menu, zeta3 menu}
     x {naive-shaped chain, spliced chain} — same clock within a menu
     (1e-9), across menus a gap >= 0.05 (direction not frozen; hand
     estimates, not asserts: sqrt3 ~ 1.45, zeta3 ~ 1.36).
CF6  REGRESSIONS through the TRUE spliced chains: Q's 2-column deep clock
     = 1.6045 +- 2e-3 (explore_irreducibility_places.py print — computed
     there at the lambda-limit, never having seen the chain); Q(sqrt-5) P2
     = 1.70395 +- 1e-3 (crossfield SYN print).
CF7  THE BRACKET READS e: the max-headroom clock beta'_col < beta_col at
     every e >= 2 column; equal at e = 1. (The e -> inf limit of the
     mixed-char bracket factor is 1/(1 - p^-beta) = crossfield F3's
     equal-char post-tick factor — cited, not re-asserted.)
CF8  MENU EXACTNESS: the hand menus (below, THE MENUS) verified by an
     independent brute entrant scan; sqrt3's menu is exactly {(2, cap 2)}
     (no split entrant ever: 2*3^i + 1 == 7 mod 12 vs split == +-1 mod 12;
     no inert entrant ever: 8 | h^2 - 1 for odd h vs 2-part 2 of
     2*3^inf); zeta_8's exactly {17,257,65537 x4, 9 x2}.

THE MENUS (hand-derived, adversarially re-derived;
entrant = (norm, copies, limit cap)):
  Q 2-col:       (3,1,1) (5,1,1) (17,1,1) (257,1,1) (65537,1,1)  [Fermat]
  sqrt-5 P2:     (3,2,1) (5,1,1)                    [chi_-20 gate; SYN menu]
  sqrt2 P2:      (17,2,1) (257,2,1) (65537,2,1) (9,1,1)   [5 inert: OUT —
                 the Fermat gate splits the sqrt2/i pair]
  sqrt-2 P2:     (3,2,1) (17,2,1) (257,2,1) (65537,2,1)
  i P2:          (5,2,1) (17,2,1) (257,2,1) (65537,2,1) (9,1,1)
  zeta8 P2:      (17,4,1) (257,4,1) (65537,4,1) (9,2,1)
  sqrt3 P3:      (2,1,2)                            [the poorest menu]
  zeta3 P3:      (4,1,2) + (h,2,1) for h = 2*3^i+1 prime, 1 <= i <= 14
Local identities used: Q_2(sqrt3) = Q_2(sqrt-5) (-15 == 1 mod 8, a 2-adic
square), so Z[sqrt3]/P2^j reads the N8 chain; odd-p unramified E(j) =
p^(j-1) (v(u^p - 1) = v(u-1) + 1); 2-adic unramified quadratic = the
censused "Q2-unram-F4" chain; ramified-5 entrant at sqrt-5 = the censused
Q5(sqrt-5) chain.

THE DESIGN. Chains: the census re-run in-process (explore_local_clock.LF,
importable) for the eight column fields + the two entrant fields; TRUE
chains extended past amax by per-orbit pump continuation (every recorded
value above the seat marches +e: cancellation is seat-confined — the
two-gear rule's scope; for zeta_8 this closes an earlier run's "period-4
continuation unverified" vacuum CONDITIONALLY on that rule), with the
seat-blind guard (an orbit truncated at the valuation cap BEFORE clearing
the seat could be seat-redirected: no continuation, asserted unable to
overtake the winner). NAIVE counterfactuals: chain_from_law
without splice; the sqrt3 counterfactual is the zeta_3-splice TRANSPLANT
(1 -> 4). Menus built from one constructor (splitting law + ramified
lambda tables + the family d*p^i+1, i <= 14) and verified by scan.
zeta_K via Dirichlet L products (characters mod 3, 4, 8, 12, 20; L tails
<= period * N^-beta < 1e-5 at LN = 30000). Roots by bisection, interior
asserts against beta*_K (root of zeta_K = 2). Everything asserts against
the slate; run `python prime/code/explore_clock_factorization.py`.

FINDINGS (entered post-run, copied from printed output).

1. THE DEEP CLOCK IS DEFECT-BLIND — the open question CLOSED (rule: proved
   given the state lemma + the census-tier lambda inputs, verified in range,
   4440 checks): at ALL EIGHT columns the deep clock computed through the
   TRUE spliced chain's finite cofactor, through the NAIVE counterfactual
   chain's, and at the limit menu agree to 1e-9 (CF3 hit everywhere). The
   proof is two lines once operationalized: entrant caps are
   divisibility-monotone in the wall and E is non-decreasing, so the limit
   menu is PATH-FREE; and the own-column headroom is zero at pre-tick
   states by definition. The earlier "argument, unverified numerically"
   status upgrades to rule.

2. THE CLOCK FACTORIZATION (the four layers; CF1-CF4 all hit): the deep
   VALUE reads the LIMIT MENU alone (= the field's splitting law + ramified
   lambda tables); the accumulation SET reads e — exactly e values
   {C_lim * sum_{delta<=h} p^(-beta delta), h = 0..e-1} (four at zeta_8,
   one at e = 1: Q's 2-column breathes not at all, like Q's tame odd);
   the PHASE reads torsion (sqrt3 pre-ticks ODD vs zeta_3 EVEN; the splice
   flips naive EVEN to ODD at sqrt2/sqrt-2/i; zeta_8's phase 2 mod 4,
   carried by the level-1 splice landing 14); the finite-time TRANSIENT
   reads the full arrival-graded defect — visible in the cofactor in range
   at every spliced field, NOWHERE at the limit. Convergence is EXACT at
   finite a (CF1 sharpened by the hand attack): past the last entrant
   threshold (a = 18/6/33/33/35/66/1/20 across the eight columns) the
   pre-tick cofactor EQUALS C_lim to 1e-12, a staircase before that.

3. THE TWINS SPLIT BY MENU ALONE (CF5 hit): sqrt3-column 1.44746 vs
   zeta3-column 1.33357 (gap 0.1139) — same (p, e, f) = (3, 2, 1),
   opposite tick parities, and the chain TRANSPLANT moves neither root
   (1e-9). What the deep clock reads of "the field beyond (p, e, f)" is
   its SPLITTING LAW (reciprocity), not its local torsion: sqrt3's menu is
   the poorest in the thread — exactly {(2, cap 2)}, both exclusion proofs
   in the docstring header — vs zeta_3's long split family. The
   CONTRAPOSITIVE pair (unfrozen find): Q(sqrt2) and Q(sqrt-2) share the
   SAME census chain (landing 5) yet their clocks split 1.48614 vs 1.63177
   — the Fermat gate: 5 splits mod 8 in neither, 3 splits in Q(sqrt-2)
   only. Same chain, different clock; same menu, same clock.

4. THE SPECTRUM (deep clocks through the true chains) + REGRESSIONS (CF6
   hit): sqrt-5 P2 1.70395 > sqrt-2 1.63177 > Q 2-col 1.60449 > i 1.49669
   > sqrt2 1.48614 > sqrt3 P3 1.44746 > zeta8 1.40019 > zeta3 P3 1.33357,
   every root interior in (1, beta*_K). Q's 2-column 1.60449 reproduces
   places.py's 1.6045 and sqrt-5's P2 reproduces crossfield's 1.70395 —
   both original numbers were computed at the lambda-limit and never saw
   the chains; here they are re-derived THROUGH the true spliced chains.

5. THE BRACKET READS e (CF7 hit): the max-headroom clock sits strictly
   below the deep clock at every e >= 2 (sqrt-5 1.52998, sqrt2 1.35701,
   sqrt-2 1.46224, i 1.35445, zeta8 1.22953, sqrt3 1.36555, zeta3 1.26810)
   and equals it at e = 1; the e -> inf limit of the bracket factor is the
   equal-char post-tick factor (crossfield F3).

6. SCOPE. The chain extension past the census range is the two-gear rule
   applied where cancellation cannot occur (every continued value clears
   the seat) — for zeta_8 this closes an earlier run's "period-4 continuation
   unverified" vacuum CONDITIONALLY on that rule; orbits truncated by the
   valuation cap before clearing the seat get no continuation and are
   guard-asserted unable to overtake the winner. The blindness proof
   inherits the state lemma's tier and the census lambda inputs.

RUN RECORD. Engine ~7 s, 4440 checks, all sections pass. Three pre-green
failures, each its own lesson: (1) the first extension treated EVERY
CAP-sentinel orbit as unknown — at Q2(sqrt2) every post-transient orbit
value is odd, so every long orbit ends in the sentinel and the guard
caught its own extension undercounting E (fix: continuation is law-exact
whenever the last exact value clears the seat; only seat-blind orbits stay
guarded); (2) the p = 2 candidate family ran i <= 14 and missed 65537
(Fermat reach i <= 16); (3) CF3's "first E-differing state" assert — the
cofactor reads the chain only through (caps, headroom), and at sqrt-5's
first differing state both tie; made existential (itself a finding-shaped
fact: even the transient is only (caps, headroom)-visible). Three
pre-green failures total; every later rerun green.
"""

import os
import sys
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_local_clock import LF, ZOO, FROZEN, chain_from_law, \
    chain_from_orbits                                   # noqa: E402
from explore_irreducibility_crossfield import zeta_hp, lseries, \
    bisect_root, chi20                                  # noqa: E402
from explore_depth_observer import is_prime             # noqa: E402

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def lcm(a, b):
    return a * b // gcd(a, b)


# ------------------------------------------------------------ zeta_K per field

LN = 30000


def chi_m4(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def chi_8(n):
    return 0 if n % 2 == 0 else (1 if n % 8 in (1, 7) else -1)


def chi_m8(n):
    return 0 if n % 2 == 0 else (1 if n % 8 in (1, 3) else -1)


def chi_12(n):
    return 0 if gcd(n, 12) > 1 else (1 if n % 12 in (1, 11) else -1)


def chi_m3(n):
    return 0 if n % 3 == 0 else (1 if n % 3 == 1 else -1)


ZK = {
    'Q':      lambda b: zeta_hp(b),
    'i':      lambda b: zeta_hp(b) * lseries(b, chi_m4, 'm4', LN),
    'sqrt2':  lambda b: zeta_hp(b) * lseries(b, chi_8, 'c8', LN),
    'sqrt-2': lambda b: zeta_hp(b) * lseries(b, chi_m8, 'm8', LN),
    'sqrt3':  lambda b: zeta_hp(b) * lseries(b, chi_12, 'c12', LN),
    'zeta3':  lambda b: zeta_hp(b) * lseries(b, chi_m3, 'm3', LN),
    'zeta8':  lambda b: (zeta_hp(b) * lseries(b, chi_8, 'c8', LN)
                         * lseries(b, chi_m4, 'm4', LN)
                         * lseries(b, chi_m8, 'm8', LN)),
    'sqrt-5': lambda b: zeta_hp(b) * lseries(b, chi20, 'm20', LN),
}

# splitting law: (is_split(h), copies when split); non-split odd h is inert
# (norm h^2, copies 1) except zeta8 where f = 2 gives TWO norm-h^2 primes.
SPLIT = {
    'Q':      (lambda h: True, 1),
    'i':      (lambda h: h % 4 == 1, 2),
    'sqrt2':  (lambda h: h % 8 in (1, 7), 2),
    'sqrt-2': (lambda h: h % 8 in (1, 3), 2),
    'sqrt3':  (lambda h: h % 12 in (1, 11), 2),
    'zeta3':  (lambda h: h % 3 == 1, 2),
    'zeta8':  (lambda h: h % 8 == 1, 4),
    'sqrt-5': (lambda h: chi20(h) == 1, 2),
}
DISC = {'Q': 1, 'i': -4, 'sqrt2': 8, 'sqrt-2': -8, 'zeta8': 256,
        'sqrt3': 12, 'zeta3': -3, 'sqrt-5': -20}

JMAX = 6


# ------------------------------------------------------------------ the census

NEEDED = ["Q2", "Q2(sqrt2)", "Q2(sqrt-2)", "Q2(sqrt-5)  x^2-2x+6",
          "Q2(i)  x^2-2x+2", "Q2(zeta8)", "Q3(sqrt3)", "Q3(zeta3)",
          "Q2-unram-F4", "Q5(sqrt-5)"]
CEN = {}


def run_census():
    for name in NEEDED:
        row = next(z for z in ZOO if z[0] == name)
        lf = LF(*row)
        orbits = [lf.orbit(u) for u in lf.units()]
        chain = chain_from_orbits(lf.p, orbits, lf.amax)
        if name in FROZEN:
            want = FROZEN[name][:lf.amax]
            ok(chain[:len(want)] == want, "census drift at " + name)
        CEN[name] = (lf, orbits, chain)


def extend_chain(name, e, A):
    """TRUE chain to depth A: census orbits + pump continuation (+e above the
    seat, the two-gear rule's scope), with the capped-orbit winner guard."""
    lf, orbits, chain = CEN[name]
    p, amax, capv = lf.p, lf.amax, lf.CAP
    seat = lf.seat if lf.seat is not None else 0
    distinct = set(tuple(o) for o in orbits)
    sets = []
    for o in distinct:
        vals = [v for v in o if v < capv]
        # an orbit whose last EXACT value clears the seat continues +e
        # law-exactly (pump-only; the CAP sentinel just hides values > amax);
        # one capped at/below the seat could be seat-redirected: guard it.
        blind = (len(vals) < len(o)) and (not vals or vals[-1] <= seat)
        if not blind and vals:
            v = vals[-1]
            while v + e <= A + e:
                v += e
                vals.append(v)
        sets.append((sorted(set(vals)), blind))
    best = [0] * A
    for vals, blind in sets:
        idx = 0
        for a in range(1, A + 1):
            while idx < len(vals) and vals[idx] < a:
                idx += 1
            if idx > best[a - 1]:
                best[a - 1] = idx
    E = [p ** m for m in best]
    ok(E[:amax] == chain, name + ": extension disagrees with census in range")
    for vals, blind in sets:
        if not blind:
            continue
        n_exact = len(vals)
        for a in range(amax + 1, A + 1):
            bound = n_exact + max(0, (a - 1 - (amax + 1)) // e + 1)
            ok(p ** bound <= E[a - 1],
               name + ": seat-blind orbit could overtake the winner at a=%d"
               % a)
    return E


def pre_ticks(E):
    return [a for a in range(1, len(E)) if E[a] > E[a - 1]]


def headroom(E, a):
    v, b = E[a - 1], a
    while b < len(E) and E[b] == v:
        b += 1
    return (b - a) if b < len(E) else None


# ----------------------------------------------------------- menus + cofactors


def cap_at(lams, wall):
    cap = 0
    for lam in lams:
        if wall % lam == 0:
            cap += 1
        else:
            break
    return cap


def split_lams(h):
    return [(h - 1) * h ** (j - 1) for j in range(1, JMAX + 1)]


def inert_lams(h):
    return [lcm(h * h - 1, h ** (j - 1)) for j in range(1, JMAX + 1)]


RAM_LAMS = {}          # (field key, h) -> (norm, lams); filled from the census


def fill_ram_lams():
    e_n8 = CEN["Q2(sqrt-5)  x^2-2x+6"][2]
    RAM_LAMS[('sqrt3', 2)] = (2, [e_n8[j - 1] for j in range(1, JMAX + 1)])
    e_n6 = CEN["Q5(sqrt-5)"][2]
    RAM_LAMS[('sqrt-5', 5)] = (5, [lcm(4, e_n6[j - 1])
                                   for j in range(1, JMAX + 1)])


def unram2_lams():
    e_u = CEN["Q2-unram-F4"][2]                 # 2-adic unramified quadratic
    return [lcm(3, e_u[j - 1]) for j in range(1, JMAX + 1)]


def build_menu(key, p):
    q1 = p - 1
    wall_lim = q1 * p ** 64
    ds = [d for d in (1, 2) if q1 % d == 0]
    imax = 16 if p == 2 else 14         # Fermat reach / the crossfield imax
    cands = sorted({d * p ** i + 1 for d in ds for i in range(0, imax + 1)})
    ents = []
    for h in cands:
        if h < 2 or h == p or not is_prime(h):
            continue
        if DISC[key] % h == 0:
            norm, lams = RAM_LAMS[(key, h)]
            copies = 1
        else:
            spl, csp = SPLIT[key]
            if spl(h):
                norm, copies, lams = h, csp, split_lams(h)
            elif h == 2:
                norm, copies, lams = 4, 1, unram2_lams()
            else:
                norm, copies = h * h, (2 if key == 'zeta8' else 1)
                lams = inert_lams(h)
        cap = cap_at(lams, wall_lim)
        if cap:
            ok(cap < JMAX, "cap ran into JMAX at (%s, %d)" % (key, h))
            ents.append((h, norm, copies, cap, lams))
    return ents


def C_from(menu, caps, beta):
    s = 1.0
    for (h, norm, copies, capl, lams), c in zip(menu, caps):
        f = sum(norm ** (-beta * j) for j in range(c + 1))
        s *= f ** copies
    return s


class Column(object):
    def __init__(self, label, key, census_name, p, e, A):
        self.label, self.key, self.census_name = label, key, census_name
        self.p, self.e, self.A = p, e, A
        self.q1, self.normP = p - 1, p
        self.zk = ZK[key]
        self.menu = build_menu(key, p)
        self.limit_caps = [m[3] for m in self.menu]

    def C_lim(self, beta):
        return C_from(self.menu, self.limit_caps, beta)

    def caps_fin(self, E, a):
        wall = lcm(self.q1, E[a - 1])
        return [cap_at(m[4], wall) for m in self.menu]

    def cof_fin(self, E, a, beta):
        hr = headroom(E, a)
        own = sum(self.normP ** (-beta * d) for d in range(hr + 1))
        return C_from(self.menu, self.caps_fin(E, a), beta) * own

    def root_lim(self):
        return bisect_root(lambda b: self.zk(b) - self.C_lim(b) - 1.0,
                           1.0001, 2.5)

    def root_fin(self, E, a):
        ok(headroom(E, a) == 0, self.label + ": root_fin off a pre-tick state")
        return bisect_root(lambda b: self.zk(b) - self.cof_fin(E, a, b) - 1.0,
                           1.0001, 2.5)

    def root_bracket(self):
        def geom(b):
            return sum(self.normP ** (-b * d) for d in range(self.e))
        return bisect_root(
            lambda b: self.zk(b) - self.C_lim(b) * geom(b) - 1.0, 1.0001, 2.5)

    def beta_star(self):
        return bisect_root(lambda b: self.zk(b) - 2.0, 1.0001, 2.5)


COLUMNS = [
    ("Q : 2-column",      'Q',      "Q2",                   2, 1, 30),
    ("Q(sqrt-5) : P2",    'sqrt-5', "Q2(sqrt-5)  x^2-2x+6", 2, 2, 45),
    ("Q(sqrt2) : P2",     'sqrt2',  "Q2(sqrt2)",            2, 2, 45),
    ("Q(sqrt-2) : P2",    'sqrt-2', "Q2(sqrt-2)",           2, 2, 45),
    ("Q(i) : P2",         'i',      "Q2(i)  x^2-2x+2",      2, 2, 45),
    ("Q(zeta8) : P2",     'zeta8',  "Q2(zeta8)",            2, 4, 90),
    ("Q(sqrt3) : P3",     'sqrt3',  "Q3(sqrt3)",            3, 2, 45),
    ("Q(zeta3) : P3",     'zeta3',  "Q3(zeta3)",            3, 2, 45),
]


# ------------------------------------------------------------------- sections


def s1_menus(cols):
    print("S1 the menus (CF8)")
    slate = {
        'Q':      [(3, 1, 1), (5, 1, 1), (17, 1, 1), (257, 1, 1),
                   (65537, 1, 1)],
        'sqrt-5': [(3, 2, 1), (5, 1, 1)],
        'sqrt2':  [(9, 1, 1), (17, 2, 1), (257, 2, 1), (65537, 2, 1)],
        'sqrt-2': [(3, 2, 1), (17, 2, 1), (257, 2, 1), (65537, 2, 1)],
        'i':      [(5, 2, 1), (9, 1, 1), (17, 2, 1), (257, 2, 1),
                   (65537, 2, 1)],
        'zeta8':  [(9, 2, 1), (17, 4, 1), (257, 4, 1), (65537, 4, 1)],
        'sqrt3':  [(2, 1, 2)],
    }
    for col in cols:
        got = sorted((m[1], m[2], m[3]) for m in col.menu)
        if col.key in slate:
            ok(got == sorted(slate[col.key]),
               col.label + ": menu != slate: %s" % got)
        else:                                   # zeta3: the family rule
            fam = sorted([(4, 1, 2)] +
                         [(2 * 3 ** i + 1, 2, 1) for i in range(1, 15)
                          if is_prime(2 * 3 ** i + 1)])
            ok(got == fam, col.label + ": menu != family rule: %s" % got)
        # independent brute completeness scan: every prime h <= 2000 enters
        # iff the constructor said so (first-exponent route check)
        wall_lim = col.q1 * col.p ** 64
        in_menu = {m[0] for m in col.menu}
        for h in range(2, 2001):
            if not is_prime(h) or h == col.p:
                continue
            if DISC[col.key] % h == 0:
                lam1 = RAM_LAMS[(col.key, h)][1][0]
            elif SPLIT[col.key][0](h):
                lam1 = h - 1
            else:
                lam1 = h * h - 1
            ok((wall_lim % lam1 == 0) == (h in in_menu),
               col.label + ": scan disagrees at h=%d" % h)
        print("  %-18s menu %s" % (
            col.label, sorted((m[1], m[2], m[3]) for m in col.menu)))
    # the sqrt3 proofs, in range
    for i in range(1, 15):
        h = 2 * 3 ** i + 1
        ok(h % 12 == 7, "sqrt3: family member not 7 mod 12 at i=%d" % i)
    for h in range(3, 2001, 2):
        if is_prime(h):
            ok((h * h - 1) % 8 == 0, "sqrt3: 8 ndiv h^2-1 at h=%d" % h)
    print("  sqrt3: no split entrant (family == 7 mod 12), no inert entrant"
          " (8 | h^2-1): menu = {(2, cap 2)} exactly")


def s2_convergence(cols, chains):
    print("S2 exact convergence + the accumulation set (CF1, CF2)")
    out = {}
    for col in cols:
        E = chains[col.census_name]
        pts = pre_ticks(E)
        lim = col.limit_caps
        past = next(a for a in pts if col.caps_fin(E, a) == lim)
        b_lim = col.root_lim()
        for beta in (1.5, b_lim):
            clim = col.C_lim(beta)
            prev = 0.0
            for a in pts:
                if a > col.A - col.e - 1:
                    break
                c = col.cof_fin(E, a, beta)
                ok(c >= prev - 1e-12, col.label + ": pre-tick staircase dips")
                prev = c
                if a >= past:
                    ok(abs(c - clim) <= 1e-12 * clim,
                       col.label + ": cof != C_lim at pre-tick a=%d" % a)
            # V_h equality at every state past the thresholds
            vals = set()
            for a in range(past, col.A - col.e - 1):
                hr = headroom(E, a)
                if hr is None:
                    continue
                vh = clim * sum(col.normP ** (-beta * d)
                                for d in range(hr + 1))
                c = col.cof_fin(E, a, beta)
                ok(abs(c - vh) <= 1e-12 * vh,
                   col.label + ": cof != V_hr at a=%d" % a)
                vals.add(round(vh, 12))
            ok(len(vals) == col.e,
               col.label + ": %d accumulation values != e=%d"
               % (len(vals), col.e))
        # post-transient hr cycle
        tail = [b - a for a, b in zip(pts, pts[1:])]
        suffix = 0
        while suffix < len(tail) and tail[len(tail) - 1 - suffix] == col.e:
            suffix += 1
        ok(suffix >= 5, col.label + ": post-transient tick suffix too short")
        out[col.key] = (b_lim, past, pts)
        print("  %-18s C_lim(1.5) = %.6f   %d accumulation values, "
              "thresholds done at a = %d" % (
                  col.label, col.C_lim(1.5), col.e, past))
    return out


def s3_blindness(cols, chains, s2):
    print("S3 the blindness + the phase (CF3, CF4)")
    naive = {}
    for col in cols:
        E = chains[col.census_name]
        if col.key == 'sqrt3':
            En = chain_from_law(col.p, col.e, col.A, splice=(1, 4))
            tag = "zeta3-splice transplant"
        else:
            En = chain_from_law(col.p, col.e, col.A)
            tag = "naive counterfactual"
        naive[col.key] = En
        ok(E != En, col.label + ": counterfactual chain identical")
        a_diff = next(a for a in range(1, col.A + 1)
                      if E[a - 1] != En[a - 1])
        # the cofactor reads the chain only through (caps, headroom): the
        # first E-differing state may tie — assert the transient is visible
        # SOMEWHERE (existential over in-range states)
        a_vis = next((a for a in range(1, CEN[col.census_name][0].amax + 1)
                      if abs(col.cof_fin(E, a, 1.5)
                             - col.cof_fin(En, a, 1.5)) > 1e-9), None)
        ok(a_vis is not None,
           col.label + ": transient invisible in the cofactor")
        b_lim = s2[col.key][0]
        a_t = next(a for a in reversed(pre_ticks(E))
                   if col.caps_fin(E, a) == col.limit_caps)
        a_n = next(a for a in reversed(pre_ticks(En))
                   if col.caps_fin(En, a) == col.limit_caps)
        bt, bn = col.root_fin(E, a_t), col.root_fin(En, a_n)
        ok(abs(bt - b_lim) < 1e-9 and abs(bn - b_lim) < 1e-9,
           col.label + ": deep clock NOT blind (%.12f / %.12f / %.12f)"
           % (bt, bn, b_lim))
        print("  %-18s true/naive/limit roots agree at %.6f   "
              "(E differs first at a = %d: %s)" % (
                  col.label, b_lim, a_diff, tag))
    # CF4 phases (post-transient pre-tick parities)
    for key, lo, parity, want in (('sqrt3', 3, 2, 1), ('zeta3', 4, 2, 0),
                                  ('sqrt2', 5, 2, 1), ('sqrt-2', 5, 2, 1),
                                  ('i', 7, 2, 1)):
        col = next(c for c in cols if c.key == key)
        pts = [a for a in pre_ticks(chains[col.census_name])
               if lo <= a <= col.A - col.e]
        ok(all(a % parity == want for a in pts),
           key + ": pre-tick parity broken: %s" % pts[:6])
    for key in ('sqrt2', 'sqrt-2', 'i'):
        col = next(c for c in cols if c.key == key)
        pts = [a for a in pre_ticks(naive[key]) if 2 <= a <= col.A - col.e]
        ok(all(a % 2 == 0 for a in pts),
           key + ": naive pre-ticks not even: %s" % pts[:6])
    col8 = next(c for c in cols if c.key == 'zeta8')
    pts8 = pre_ticks(chains[col8.census_name])
    tail8 = [a for a in pts8 if a >= 18]
    ok(all(b - a == 4 for a, b in zip(tail8, tail8[1:])),
       "zeta8: extended ticks not period 4")
    print("  phases: sqrt3 pre-ticks ODD vs zeta3 EVEN (the twins);"
          " sqrt2/sqrt-2/i splice flips EVEN -> ODD;")
    print("  zeta8 pre-ticks %s ... phase %d mod 4" % (
        pts8[:6], tail8[0] % 4))
    return naive


def s4_regressions(cols, s2):
    print("S4 regressions + the spectrum (CF6)")
    b_q = s2['Q'][0]
    ok(abs(b_q - 1.6045) < 2e-3,
       "Q 2-column regression: %.5f != 1.6045" % b_q)
    b_k5 = s2['sqrt-5'][0]
    ok(abs(b_k5 - 1.70395) < 1e-3,
       "sqrt-5 P2 regression: %.5f != 1.70395" % b_k5)
    print("  Q 2-column %.5f (places.py 1.6045)   Q(sqrt-5) P2 %.5f "
          "(crossfield 1.70395)" % (b_q, b_k5))
    print("  the spectrum (deep clocks, all through TRUE spliced chains):")
    for col in sorted(cols, key=lambda c: -s2[c.key][0]):
        bs = col.beta_star()
        b = s2[col.key][0]
        ok(1.0 < b < bs, col.label + ": clock not interior (1, beta*)")
        print("    %-18s beta_col = %.5f   (beta* = %.5f)" % (
            col.label, b, bs))


def s5_bracket_twins(cols, s2, chains, naive):
    print("S5 the bracket + the twins (CF7, CF5)")
    for col in cols:
        b, bb = s2[col.key][0], col.root_bracket()
        if col.e == 1:
            ok(abs(bb - b) < 1e-9, col.label + ": e=1 bracket != deep")
        else:
            ok(bb < b - 1e-6, col.label + ": bracket !< deep clock")
        print("  %-18s deep %.5f   bracket %.5f   (e = %d)" % (
            col.label, b, bb, col.e))
    c3 = next(c for c in cols if c.key == 'sqrt3')
    cz = next(c for c in cols if c.key == 'zeta3')
    roots = {}
    for col, other in ((c3, cz), (cz, c3)):
        E, En = chains[col.census_name], naive[col.key]
        a_t = next(a for a in reversed(pre_ticks(E))
                   if col.caps_fin(E, a) == col.limit_caps)
        a_n = next(a for a in reversed(pre_ticks(En))
                   if col.caps_fin(En, a) == col.limit_caps)
        bt, bn = col.root_fin(E, a_t), col.root_fin(En, a_n)
        ok(abs(bt - bn) < 1e-9, col.label + ": twins within-menu split")
        roots[col.key] = bt
    gap = abs(roots['sqrt3'] - roots['zeta3'])
    ok(gap >= 0.05, "twins gap %.4f < 0.05" % gap)
    print("  the twins: sqrt3-col %.5f vs zeta3-col %.5f (gap %.4f) — "
          "opposite tick parities, SAME clock per menu" % (
              roots['sqrt3'], roots['zeta3'], gap))


def main():
    print("THE CLOCK FACTORIZATION — beta_col over the defect zoo")
    print("=" * 64)
    run_census()
    fill_ram_lams()
    cols = [Column(*row) for row in COLUMNS]
    chains = {c.census_name: extend_chain(c.census_name, c.e, c.A)
              for c in cols}
    s1_menus(cols)
    s2 = s2_convergence(cols, chains)
    naive = s3_blindness(cols, chains, s2)
    s4_regressions(cols, s2)
    s5_bracket_twins(cols, s2, chains, naive)
    print("\nALL SECTIONS PASS (%d checks)" % CHECKS)


if __name__ == "__main__":
    main()
