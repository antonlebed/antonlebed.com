"""
explore_interactive_observer.py -- THE INTERACTIVE OBSERVER (sibling
of explore_growth_laws.py and explore_class_gap.py).

THE QUESTION. Earlier studies (the route-amnesia and thermometer
work) ran PASSIVE inference: an observer handed the state (the
isomorphism class) and nothing else. This study gives the inhabitant
a WATCH (it sees the moves as they happen), a PROBE (it may query
whether a move is admissible), and a HAND (it may inject moves of
its own), and asks what each buys, per fate, against predictions
fixed before the run (PR1-PR9) and a paper attack on the mechanism.

FINDINGS (tier labels below; run record follows; all sections assert).

1. THE WITNESS FAMILY (rule, proved; verified S0). Every thermal
   greedy law is an EXPONENTIAL FAMILY in beta: P_x(m) =
   m^(-beta)/Z_x, natural parameter beta, sufficient statistic
   -log m. So watching is sampling: the per-pick Fisher information
   is I_step(x) = Var_x(log m), scores are martingale increments,
   and a watched segment carries I = sum of per-state Var(log m).
   Closed forms: breadth via F(beta) = zeta(beta) prod_{p|N}
   (1 - p^(-beta)) and its two derivatives; depth (D-DYN at 3^t) via
   the full zeta sums minus the wall cofactor's divisors (the
   wall-priced normalizer, from that earlier study). Verified
   against brute coprime sums with rigorous tail brackets (N = 30,
   210; beta 1.5/2/3).

2. THE WITNESS THERMOMETER (rule in range; limit = PNT heuristic,
   observation; verified S1). An earlier finite thermometer --
   total snapshot information <= an order-1 cap, forever -- is a
   COMPRESSION ARTIFACT, not a law of the world. Along the breadth
   trajectory the PER-MOVE information never dies: I_step(p_k#,
   beta = 2) = 0.9134 (k = 3), dips to 0.8129 (k = 50), then climbs
   monotonically -- 0.8668 (k = 5000), 0.8907 (k = 100000) -- toward
   the heuristic limit 1/(beta-1)^2 (the pick m = q e^u has
   u ~ Exp(beta-1) by PNT density; = 1 at beta 2). Positive floor
   certified in range without PNT: disjoint log-buckets [q, 2q) vs
   [4q, 8q) both carry computable mass, giving Var >= 0.0134/0.0141
   at k = 50/5000 (rule in range). So WATCHED information grows
   LINEARLY in moves while the state's total is capped: an eternal
   inhabitant that merely watches its world grow accumulates
   unbounded temperature information (the Cramer-Rao floor falls as
   1/sqrt(moves)); one that only reads the state never beats sd ~ 1.
   The cap itself recomputed here with a Chebyshev prime tail
   (Rosser-Schoenfeld pi(x) < 1.26 x/log x): I_state-total in
   [0.88447, 0.88450] at beta 2 (inside the earlier bracket of
   [0.8844, 0.8859]), [3.82677, 3.88007] at 1.5, 0.17228 at 3.
   THE CROSSOVER (predicted vs. measured): the prediction was a
   monotone approach and one-move > whole-state by k = 5000 at
   beta 2; measured, the approach is NON-MONOTONE (the
   dip: small-rung menus are variance-rich -- at k = 3 the menu
   holds comparable-mass moves across octaves, 7 vs 49) and the
   crossover sits at k* in (33000, 100000): I_step passes the whole
   infinite state's cap between q = 389173 and 1299721 (I at
   k = 40000 grazes the cap's lower edge within 3e-5 -- the fine
   location is limited by the cap bracket itself). At beta = 3
   ONE move beats the state's eternity at EVERY tested rung
   (0.2135..0.2310 > 0.17228, k <= 5000); at beta = 1.5 the state
   wins at every tested k >= 10 (k = 3 lands inside the cap
   bracket, unresolved). THE POLE DUEL (observation, three betas):
   the cap is BELOW the one-move limit 1/(beta-1)^2 at 1.5, 2, and
   3 -- at leading order both scale as 1/(beta-1)^2 at the pole,
   and in the tested range the second order always favors the move:
   the whole infinite state is worth less than one late watched
   move. Float wall (honest scope): at beta = 3, k > ~1e4 the
   closed form's F - 1 cancels below float64 and values are not
   reported; beta 1.5/2 are safe throughout (S ~ q^(1-beta) >> eps).

3. THE WITNESS GAP (rule, proved -- law of total variance; verified
   S2 exactly). I_path = I_state + E[I_route posterior]: the
   information watching buys OVER the aged snapshot (state + move
   count) is EXACTLY the Fisher information of the route posterior
   -- the same normalizer sequence that earlier work proved carries
   all route information. Verified on the truncated world (menu
   <= 12, 4 moves, 648 paths, all three quantities computed
   independently and analytically): 0.649817 = 0.446763 + 0.203054,
   identity to 1.2e-15. The amnesia mechanism now has a name: the
   route-weight cancellation makes the state a LOSSY CODE for its
   own history, and what it loses is precisely the route posterior's
   information. Memory is not in the world; it is in the witnessing.

4. THE DEMAND CHAIN + THE COLD BLINDNESS (rule, proved; verified
   S3). Introduce D-SEMI (the semisimplicity demand: Z/Nm stays
   squarefree = all channels fields). Then A_SEMI < A_IND < A_MEM
   strictly (separating moves q^2 and 2q) yet ALL THREE greedy picks
   coincide at the least prime not dividing N -- verified
   IND == MEM at 99999/99999 states N <= 1e5, SEMI == IND at all
   1823 squarefree N <= 3000, and 25-step T = 0 trajectories
   identical from seeds 1, 30, 105. So at ZERO temperature the law
   is INVISIBLE TO ANY ETERNAL WATCHER -- three different demands
   write one world forever -- while ONE admissibility probe (propose
   q^2: SEMI refuses; propose 2q: only MEM accepts) separates them
   in a single step. The observation/intervention gap of causal
   inference materializes in arithmetic growth, and it is infinite
   at T = 0. Heat closes it at a computable rate: THE DISCRIMINATION
   CLOCKS (rule) -- for nested demands KL(P_narrow || P_wide) =
   log(Z_wide/Z_narrow) exactly, decaying with slope log(m*/q) where
   m* is the cheapest differing move (at N = 30: slope -> log 2 for
   IND vs MEM, measured 0.7047; log 7 for SEMI vs IND, measured
   1.9355). Temperature is a free experimenter -- and identification
   is ASYMMETRIC: under the wider truth one witnessed off-support
   move identifies SURELY (geometric time); under the narrower truth
   only at the KL rate. THE EXISTENTIAL PROBE: one gcd-push
   (30 -> 60) separates by LIFE VS DEATH -- D-SEMI's admissible set
   empties forever (Nm never squarefree: a new mortality specimen,
   the chain crosses the fate chart), D-IND heals on (picks 7, 11,
   13, ...) carrying the scar.

5. THE SCAR LEDGER (rule, proved + measured; verified S4). In the
   breadth fate the hand cannot change the destination (healing
   absorbs every push) but every scar is PERMANENT (multiplication
   never removes -- the healing rule's dark half; 200/200 thermal
   continuations keep the injected 2-scar). So in the amnesiac fate
   THE ONLY FOSSILS ARE ARTIFACTS -- and they FORGE: a crystal state
   dressed with geometric scars is state-indistinguishable from
   thermal genesis BY CONSTRUCTION (300 forged worlds fed to the
   earlier MLE harness: 0.587 read crystal vs the thermal law
   1/zeta(2) = 0.608, conditional mean beta-hat 1.638 vs that
   earlier study's measured 1.635), and a SINGLE 2-scar moves the
   crystal's reading from infinity to beta-hat = 1.878. False
   memories are implantable.
   THE DENIABILITY SPLIT: a gcd-scar (push 2 at state 30) has
   probability 0 under thermal D-IND -- SIGNED, certainly artificial
   to any watcher -- yet the resulting state is thermally reachable
   (route 1 -3-> 3 -5-> 15 -4-> 60), so it is DENIABLE in the state;
   a coprime scar (move 4 at state 15) is a positive-probability
   thermal event, deniable even to the watcher. States can always be
   forged; only watched paths can be signed, and only gcd-scars sign.

6. THE UNIVERSAL RUDDER (relock-at-2: rule, proved; general targets:
   rule in range, construction + Dirichlet argued; verified S5). The
   depth fate is ONE-PUSH CONTROLLABLE. To 2: pushing 2^r to depth
   e = max(3, v_2(lambda(N)) + 2) establishes the 2-lock recurrence
   invariant (v_2(lambda) = e - 2), pricing 2's door at 2 forever --
   and 2 is the least possible move, so no rival door can undercut:
   200/200 states (random <= 1e6 + deep columns 3^15, 17^6, 5^10,
   primorials, walls; 21 already there) re-lock at 2, 30/30 post-push
   picks each. ANY world is one push from the 2-adic column,
   including a 17-column six deep (17^6 ~ 2.4e7). To a general prime
   q: one composite push raising q's depth to v_q(lambda) + 2, times
   P, with P == 1 mod B (B raises
   every rival door above q: incumbent columns need v_s(lambda') >=
   e_s + t_s - 2 -- an earlier blocker-enrichment result read as a
   CONTROL LAW), P !== 1 mod q; Dirichlet supplies P, Miller-Rabin
   finds it fast (specimens: P = 191 steers 30 to the 7-column;
   P = 15496819561 steers the 3^15 column to 13). 16/16 (state,
   target) pairs locked. An earlier study's basin geography was
   decidable; interactively it is PROGRAMMABLE.

7. THE PHOENIX (protocol canonical; DNA law + spectrum law: rules,
   proved; infinitude: criterion, exact; verified S6). Give
   mortality MINIMAL LIFE SUPPORT: run greedy D-TRA; at each death
   (the state IS the wall W(lambda), explore_selection_frame.py)
   inject the least possible move m = 2. Then: (i) THE RUDDER-PRIMED
   WALL (rule, proved): the wall formula's 2-part 2^(v_2(L)+2) is
   exactly the 2-lock invariant, so the minimal push coincides with
   the D-DYN greedy pick at every wall (asserted at every death, 6
   seeds) --
   the phoenix is D-TRA composed with D-DYN's own move, no free
   choice anywhere. (ii) THE FROZEN DNA LAW (rule, proved): pushes
   bump only lambda's 2-part and fills are transparent, so D :=
   odd(lambda) is INVARIANT along the whole trajectory -- the seed's
   odd lambda-part is the phoenix's genome, fixed at birth.
   (iii) THE SPECTRUM LAW (rule, proved + verified at 6 seeds):
   the windows ever opened are exactly {p : (p-1) | 2^t * D} -- each
   odd window at frozen depth v_p(D) + 1, the 2-column deepening
   forever; limit object 2^inf * prod p^(v_p(D)+1), a DESIGNED
   supernatural number programmed by the seed. (iv) SEED 1 (D = 1):
   the windows are THE FERMAT PRIMES exactly -- 3, 5, 17, 257,
   65537 opened at v_2(lambda) = 1, 2, 4, 8, 16 (their own Fermat
   exponents), no sixth window through lambda = 2^40 (F_5 composite
   caught by Miller-Rabin), every fill after 65537 EMPTY: from the
   fifth window on, the world is dead-on-arrival at every wall and
   lives one push per epoch. THE FERMAT CRITERION (exact): the
   seed-1 phoenix opens infinitely many windows IFF there are
   infinitely many Fermat primes. Seed 7 (D = 3): the Pierpont-type
   family {3, 5, 7, 13, 17, 97, 193, 257, 769, 12289, ...}
   (2^a 3^b + 1, b <= 1), window 3 at depth 2 = v_3(D) + 1. THE
   CHEAPEST ESCAPE FROM DEATH GROWS THE FERMAT PRIMES -- mortality
   plus one bit per epoch is a designed-tower factory, and its
   design language is the seed's odd lambda-part. (Non-minimal
   pushes can program D upward mid-flight -- the general phoenix as
   a designed-growth instrument is an open lead.)

8. SYNTHESIS -- THE THREE GIFTS OF THE HAND. Watching: memory lives
   in witnessing, not in states -- per-move information is bounded
   below in BOTH fates (the depth watcher gets 1.2430/move at
   beta 2, even richer than breadth's ~0.87: its co-finite menu is
   fatter), so the amnesiac/mnemonic split (established earlier) is
   a property of STATES only; every fate's witness remembers
   linearly, and the gap between watching and reading is exactly
   the route posterior
   (finding 3). Probing: at T = 0 observationally-identical demands
   are everywhere (the chain), and one query -- or one push, read
   existentially -- names the law no eternity of watching could.
   Acting: the hand's power is fate-graded in the OPPOSITE direction
   to memory: breadth sells INSCRIPTION (unsteerable destination,
   permanent forgeable scars), depth sells DESTINATION (one push,
   any column), mortality sells TIME -- and the minimal price of
   time is the Fermat primes.

HONEST SCOPE. The witness thermometer's 1/(beta-1)^2 limit is a PNT
heuristic (the in-range floors are bucket-certified); the pole duel
is a three-beta observation, not a theorem. The rudder's general-q
construction relies on Dirichlet for P (instantiated 16/16 at
q <= 13); targets and states beyond the census are argued, not
swept. The phoenix protocol is the MINIMAL one (least push,
unconditionally 2); richer intervention policies (programming D
mid-flight, non-2 pushes) are unexplored. All watch results assume
the observer knows the law family and reads exact states; the
beta = 3 large-k float wall is stated in finding 2.

RUN RECORD (this file, ~2.2 s, 209,339 checks, all sections assert).
S0 W-formula brute-verified L <= 12; lambda 10 knowns; closed-form
I_step inside rigorous brute brackets (N = 30, 210 x beta 1.5/2/3).
S1 caps [3.82677, 3.88007] / [0.88447, 0.88450] / 0.17228 vs
one-move limits 4/1/0.25; I_step table k = 3..100000; dip + climb
asserted; crossover bracket (33000, 100000) at beta 2; bucket floors
0.0134/0.0141; depth I_step(3^t) = 1.2430 (t = 10..30, converged).
S2 648 paths, 26 end states: 0.649817 = 0.446763 + 0.203054
(1.2e-15). S3 chain specimens 14/49; picks 99999/99999 + 1823;
3 x 25-step identical trajectories; KL table beta 2..10, slopes
0.7047/1.9355; SEMI death scan 10^4 + IND healing picks 7-19.
S4 200/200 scar persistence; forgery 0.587 crystal / cond-mean
1.638; single-scar beta-hat 1.878; route 1-3-15-60 admissible.
S5 relock 200/200 (21 trivial); rudder 16/16, P specimens 7, 191,
2251, 42967, 258280327, 15496819561. S6 seed-1 windows/thresholds
exact Fermat; 40 pushes, late fills all 0; seed-7 spectrum; DNA
frozen at 6 seeds; spectrum law got == want at 6 seeds. Predictions
PR1-PR9: PR2-PR9 confirmed; PR1 bands held but its two shape
sub-predictions MISSED and were upgraded (the dip; the located
crossover) plus the pole-duel bonus. One harness off-by-one (the
terminal wall left unfilled) was caught by the spectrum-law assert,
not by eye.
"""

import math
import random
from functools import lru_cache

CHECKS = 0


def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)


# ----------------------------------------------------------------------
# S0 MACHINERY
# ----------------------------------------------------------------------

def sieve_primes(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i:: i] = bytearray(len(s[i * i:: i]))
    return [i for i in range(n + 1) if s[i]]


def sieve_spf(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


PRIMES_200K = sieve_primes(1300000)
SPF_LIM = 200001
SPF = sieve_spf(SPF_LIM - 1)


def is_prime(n):
    """Deterministic Miller-Rabin for n < 3.3e24."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


@lru_cache(maxsize=None)
def factor(n):
    """Factor dict of n (trial division + Miller-Rabin remainder)."""
    if n == 1:
        return ()
    fd = {}
    m = n
    if m < SPF_LIM:
        while m > 1:
            p = SPF[m]
            fd[p] = fd.get(p, 0) + 1
            m //= p
        return tuple(sorted(fd.items()))
    d = 2
    while d * d <= m and d < 100000:
        while m % d == 0:
            fd[d] = fd.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        if not is_prime(m):
            raise ValueError(f"factor({n}): rough remainder {m} composite")
        fd[m] = fd.get(m, 0) + 1
    return tuple(sorted(fd.items()))


def fd_of(n):
    return dict(factor(n))


def fd_int(fd):
    v = 1
    for p, e in fd.items():
        v *= p ** e
    return v


def fd_mul(a, b):
    c = dict(a)
    for p, e in b.items():
        c[p] = c.get(p, 0) + e
    return c


def fd_lcm(a, b):
    c = dict(a)
    for p, e in b.items():
        if c.get(p, 0) < e:
            c[p] = e
    return c


def fd_divides(a, b):
    """a | b for factor dicts."""
    return all(b.get(p, 0) >= e for p, e in a.items())


def lam_fd(state_fd):
    """Carmichael lambda of the ring given by a factor dict, as fd."""
    lam = {}
    for p, e in state_fd.items():
        if p == 2:
            if e == 1:
                contrib = {}
            elif e == 2:
                contrib = {2: 1}
            else:
                contrib = {2: e - 2}
        else:
            contrib = fd_of(p - 1)
            if e > 1:
                contrib = fd_mul(contrib, {p: e - 1})
        lam = fd_lcm(lam, contrib)
    return lam


def W_of(lam):
    """The transparency wall W(L) as a factor dict (formula from that
    earlier study: 2-part 2^(v2+2) for L even else 2; odd p with
    (p-1)|L at v_p(L)+1)."""
    v2 = lam.get(2, 0)
    W = {2: v2 + 2} if v2 >= 1 else {2: 1}
    # enumerate divisors d of L, test p = d+1 odd prime
    items = sorted(lam.items())
    divs = [1]
    for p, e in items:
        divs = [d * p ** k for d in divs for k in range(e + 1)]
    for d in divs:
        p = d + 1
        if p > 2 and is_prime(p):
            W[p] = lam.get(p, 0) + 1
    return W


def lam_grows(state_fd, m):
    lam0 = lam_fd(state_fd)
    lam1 = lam_fd(fd_mul(state_fd, fd_of(m)))
    return lam1 != lam0  # lam0 | lam1 always (divisibility monotone)


def pick_dyn(state_fd, mmax=100000):
    """Greedy D-DYN pick: least m >= 2 with lambda growth."""
    for m in range(2, mmax):
        if lam_grows(state_fd, m):
            return m
    raise RuntimeError("no dynamic move found")


# --- zeta and log-weighted zeta sums via Euler-Maclaurin ---------------

def zsum(beta, j, M=100000):
    """sum_{m>=2} m^-beta log^j m, Euler-Maclaurin tail at M."""
    s = 0.0
    for m in range(2, M + 1):
        lm = math.log(m)
        s += m ** (-beta) * lm ** j
    b1 = beta - 1.0
    L = math.log(M)
    if j == 0:
        tail = M ** (-b1) / b1
    elif j == 1:
        tail = M ** (-b1) * (L / b1 + 1 / b1 ** 2)
    else:
        tail = M ** (-b1) * (L * L / b1 + 2 * L / b1 ** 2 + 2 / b1 ** 3)
    f = M ** (-beta) * L ** j
    fp = M ** (-beta - 1) * (j * L ** (j - 1) - beta * L ** j) if j else \
        -beta * M ** (-beta - 1)
    # Euler-Maclaurin: sum_{m=2}^inf = sum_{m=2}^M + int_M^inf
    #                  - f(M)/2 - f'(M)/12 + O(f''')
    return s + tail - f / 2 - fp / 12


@lru_cache(maxsize=None)
def zeta_d(beta, j):
    """zeta^(j)(beta) up to sign: returns sum_{m>=1} m^-beta log^j m."""
    return (1.0 if j == 0 else 0.0) + zsum(beta, j)


def istep_ind(prime_list, beta):
    """Per-pick Fisher info Var(log m) of thermal D-IND at a squarefree
    state with the given prime support. Closed form via
    F = zeta * prod(1-p^-beta)."""
    z0, z1, z2 = zeta_d(beta, 0), zeta_d(beta, 1), zeta_d(beta, 2)
    logF = math.log(z0) + math.fsum(
        math.log1p(-p ** (-beta)) for p in prime_list)
    Gp = -z1 / z0 + math.fsum(
        math.log(p) * p ** (-beta) / (1 - p ** (-beta))
        for p in prime_list)
    Gpp = z2 / z0 - (z1 / z0) ** 2 - math.fsum(
        math.log(p) ** 2 * p ** (-beta) / (1 - p ** (-beta)) ** 2
        for p in prime_list)
    F = math.exp(logF)
    Fp = F * Gp          # = -sum m^-b log m over coprime m
    Fpp = F * (Gpp + Gp * Gp)
    S = F - 1.0
    E1 = -Fp / S
    E2 = Fpp / S
    return E2 - E1 * E1, S, E1


def istep_dyn_3t(t, beta):
    """Per-pick Fisher info of thermal D-DYN at state 3^t: admissible =
    all m>=2 minus divisors of W(lambda)/3^t (the wall discount)."""
    state = {3: t}
    lam = lam_fd(state)
    W = W_of(lam)
    cof = {p: e - state.get(p, 0) for p, e in W.items()
           if e - state.get(p, 0) > 0}
    check(fd_divides(state, W), f"S1 3^{t}: state does not divide wall")
    items = sorted(cof.items())
    divs = [1]
    for p, e in items:
        divs = [d * p ** k for d in divs for k in range(e + 1)]
    S = zsum(beta, 0)
    S1 = zsum(beta, 1)
    S2 = zsum(beta, 2)
    for d in divs:
        if d >= 2:
            ld = math.log(d)
            S -= d ** (-beta)
            S1 -= d ** (-beta) * ld
            S2 -= d ** (-beta) * ld * ld
    E1 = S1 / S
    return S2 / S - E1 * E1


# ----------------------------------------------------------------------
print("=" * 72)
print("S0  MACHINERY + EXPONENTIAL-FAMILY SANITY")
print("=" * 72)

# W formula brute check for small L (max n with lambda(n) | L)
for L, Wexp in [(1, 2), (2, 24), (4, 240), (6, 504), (8, 480),
                (10, 264), (12, 65520)]:
    Wf = fd_int(W_of(fd_of(L) if L > 1 else {}))
    check(Wf == Wexp, f"S0 W({L}) = {Wf} != {Wexp}")
    # brute: every n <= Wexp with lambda | L divides W; none bigger in 4W
    for n in range(1, min(4 * Wexp, 3000)):
        lamn = fd_int(lam_fd(fd_of(n) if n > 1 else {}))
        if L % lamn == 0:
            check(Wexp % n == 0, f"S0 brute W({L}): n={n} escapes")
print("  W(L) formula verified against brute for L <= 12")

# lambda sanity vs known values
for n, ln in [(8, 2), (16, 4), (30, 4), (510510, 240), (240, 4),
              (504, 6), (2, 1), (4, 2), (9, 6), (27, 18)]:
    check(fd_int(lam_fd(fd_of(n))) == ln, f"S0 lambda({n}) != {ln}")
print("  lambda on factor dicts verified (10 knowns)")

# exponential-family closed form vs brute at N = 30, 210
for N in (30, 210):
    pl = [p for p, _ in factor(N)]
    for beta in (1.5, 2.0, 3.0):
        var_cf, S_cf, E1_cf = istep_ind(pl, beta)
        M = 200000
        s = s1 = s2 = 0.0
        for m in range(2, M + 1):
            if math.gcd(m, N) == 1:
                w = m ** (-beta)
                lm = math.log(m)
                s += w
                s1 += w * lm
                s2 += w * lm * lm
        # rigorous brackets: the coprime tail beyond M lies in
        # [0, full tail] for each moment
        b1 = beta - 1
        L = math.log(M)
        T0 = M ** (-b1) / b1
        T1 = M ** (-b1) * (L / b1 + 1 / b1 ** 2)
        T2 = M ** (-b1) * (L * L / b1 + 2 * L / b1 ** 2 + 2 / b1 ** 3)
        check(s - 1e-9 <= S_cf <= s + T0 + 1e-9,
              f"S0 S bracket N={N} b={beta}: {S_cf} vs [{s}, {s + T0}]")
        e1_lo, e1_hi = s1 / (s + T0), (s1 + T1) / s
        e2_lo, e2_hi = s2 / (s + T0), (s2 + T2) / s
        v_lo, v_hi = e2_lo - e1_hi ** 2, e2_hi - e1_lo ** 2
        check(v_lo - 1e-9 <= var_cf <= v_hi + 1e-9,
              f"S0 Var bracket N={N} b={beta}: {var_cf} vs "
              f"[{v_lo}, {v_hi}]")
print("  closed-form I_step matches brute coprime sums (N=30, 210; "
      "3 betas)")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("S1  THE WITNESS THERMOMETER")
print("=" * 72)

ALLP = PRIMES_200K

# the snapshot cap, computed independently: I_total(beta) =
# sum_p (log p)^2 p^-beta / (1-p^-beta)^2 over ALL primes. Prime tail
# beyond the sieve by Abel summation + pi(t) < 1.26 t/log t
# (Rosser-Schoenfeld): sum_{p>X} f(p) <= 1.26 beta int_X (log t) t^-beta
# dt * (1-X^-beta)^-2, dropping the negative boundary term.
SNAP_TOTAL = {}
X = ALLP[-1]
for beta in (1.5, 2.0, 3.0):
    s = sum((math.log(p)) ** 2 * p ** (-beta) / (1 - p ** (-beta)) ** 2
            for p in ALLP)
    b1 = beta - 1.0
    L = math.log(X)
    tail = (1.26 * beta * X ** (-b1) * (L / b1 + 1 / b1 ** 2)
            / (1 - X ** (-beta)) ** 2)
    SNAP_TOTAL[beta] = (s, s + tail)
check(0.8844 <= SNAP_TOTAL[2.0][0] and SNAP_TOTAL[2.0][1] <= 0.8859,
      "S1 snapshot cap disagrees with the earlier bracket")
print("  SNAPSHOT caps (whole infinite state, recomputed with a "
      "Chebyshev prime tail; inside the earlier bracket at beta 2):")
for beta in (1.5, 2.0, 3.0):
    lo, hi = SNAP_TOTAL[beta]
    lim = 1 / (beta - 1) ** 2
    print(f"    beta={beta}: cap in [{lo:.5f}, {hi:.5f}]; one-move "
          f"limit 1/(beta-1)^2 = {lim:.5f}")
    # THE POLE DUEL: the whole infinite state is worth less than one
    # asymptotic watched move, at every tested temperature (leading
    # orders match at the pole; second order decides for the move)
    check(hi < lim, f"S1 pole duel: cap !< one-move limit at {beta}")
print("  THE POLE DUEL: cap < 1/(beta-1)^2 at all three betas -- the "
      "infinite state loses to one late move everywhere (tested "
      "range)")

KLIST = [3, 10, 50, 300, 1000, 5000, 20000, 33000, 40000, 100000]
K3MAX = 5000  # beta = 3: S = F - 1 ~ q^-2 underflows float64 rel
#               precision beyond k ~ 1e4 (the float wall); values
#               there would be cancellation garbage and are not shown
ivals = {}
print(f"  {'k':>6} {'q=p_k+1':>8} | " +
      " | ".join(f"I_step(b={b})" for b in (1.5, 2.0, 3.0)))
for k in KLIST:
    pl = ALLP[:k]
    row = []
    for beta in (1.5, 2.0, 3.0):
        if beta == 3.0 and k > K3MAX:
            row.append(None)
            continue
        v, _, _ = istep_ind(pl, beta)
        ivals[(k, beta)] = v
        row.append(v)
    print(f"  {k:>6} {ALLP[k]:>8} | " +
          " | ".join("     (float wall)"[:11] if v is None else
                     f"{v:>11.4f}" for v in row))
print(f"  heuristic limits 1/(beta-1)^2: 4.0 / 1.0 / 0.25 "
      f"(beta = 3 shown only for k <= {K3MAX}: beyond, F - 1 "
      f"underflows float64)")

# PR1 bands (fixed before the run)
check(0.65 <= ivals[(5000, 2.0)] <= 1.35, "PR1 I(5000, 2) band")
check(0.15 <= ivals[(5000, 3.0)] <= 0.35, "PR1 I(5000, 3) band")
check(2.8 <= ivals[(5000, 1.5)] <= 5.2, "PR1 I(5000, 1.5) band")
# The approach is NON-MONOTONE -- a dip near k ~ 50 (small-rung menus
# are variance-rich), then a slow climb. The prediction
# |I(5000)-1| < |I(3)-1| does not hold; the measured shape is:
check(ivals[(50, 2.0)] < ivals[(3, 2.0)], "S1 the dip exists")
for k1, k2 in zip(KLIST[2:-1], KLIST[3:]):
    check(ivals[(k1, 2.0)] < ivals[(k2, 2.0)],
          f"S1 climb {k1} -> {k2} at beta 2")
# The beta = 2 crossover sits at k* in (33000, 100000) against the
# recomputed cap (tighter than the earlier bracket), not <= 5000.
# I(40000) = 0.88444 grazes the cap's lower edge within 3e-5, so the
# fine location is limited by the cap bracket itself; the
# conservative bracket is asserted:
check(ivals[(33000, 2.0)] < SNAP_TOTAL[2.0][0],
      "S1 crossover bracket: below cap at k = 33000")
check(ivals[(100000, 2.0)] > SNAP_TOTAL[2.0][1],
      "PR1 HEADLINE (located): one watched move > whole-state total "
      "by k = 1e5 (beta 2)")
for k in KLIST:
    if k <= K3MAX:
        check(ivals[(k, 3.0)] > SNAP_TOTAL[3.0][1],
              f"PR1 one move > state total at beta 3, k={k}")
    if k >= 10:  # k = 3 sits inside the cap bracket: unresolved
        check(ivals[(k, 1.5)] < SNAP_TOTAL[1.5][0],
              f"PR1 near the pole the state wins, k={k}")
check(SNAP_TOTAL[1.5][0] <= ivals[(3, 1.5)] <= SNAP_TOTAL[1.5][1] + 0.1,
      "S1 beta=1.5 k=3 sits near the cap (bracket-unresolved)")
print("  PR1 bands PASS; prediction misses 1-2 adjudicated: the dip + the "
      "located crossover (k* in (33000, 100000) at beta 2; every "
      "tested rung at beta 3; at beta 1.5 the state wins at every "
      "tested k >= 10 while the k = 3 duel is inside the cap "
      "bracket). The watched total grows LINEARLY; the snapshot is "
      "capped.")

# bucket-certified positive floor at k = 50 and k = 5000 (beta = 2)
for k in (50, 5000):
    q = ALLP[k]
    beta = 2.0
    B1 = sum(p ** (-beta) for p in ALLP if q <= p < 2 * q)
    B3 = sum(p ** (-beta) for p in ALLP if 4 * q <= p < 8 * q)
    _, S, _ = istep_ind(ALLP[:k], beta)
    floor = min(B1, B3) / S * (math.log(math.sqrt(2))) ** 2
    check(floor > 0.01, f"S1 bucket floor k={k}: {floor}")
    check(ivals[(k, beta)] > floor, f"S1 floor consistency k={k}")
    print(f"  bucket-certified floor at k={k}: Var >= {floor:.4f} "
          f"(buckets [q,2q) mass {B1:.3e}, [4q,8q) mass {B3:.3e})")

# PR9 depth twin: I_step at 3^t
d_ivals = {}
for t in (5, 10, 20, 25, 30):
    d_ivals[t] = istep_dyn_3t(t, 2.0)
print("  depth world I_step(3^t, beta=2): " +
      ", ".join(f"t={t}: {d_ivals[t]:.4f}" for t in d_ivals))
check(0.7 <= d_ivals[30] <= 1.3, "PR9 depth I_step band")
check(abs(d_ivals[30] - d_ivals[25]) < 0.02, "PR9 depth convergence")
print("  PR9 PASS: the depth watcher also gains per-move info bounded "
      "below -- WITNESSING EQUALIZES THE FATES")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("S2  THE WITNESS GAP (Louis identity on the truncated world)")
print("=" * 72)

MENU_MAX = 12
NMOVES = 4
BETA0 = 2.0


def menu(state):
    return [m for m in range(2, MENU_MAX + 1) if math.gcd(m, state) == 1]


def zq(state, beta):
    ms = menu(state)
    Z = sum(m ** (-beta) for m in ms)
    Zp = -sum(m ** (-beta) * math.log(m) for m in ms)
    return Z, Zp


paths = [(1, 1.0, 0.0, [])]  # (state, prob, score, statelist)
istep_by_t = [0.0] * NMOVES
for t in range(NMOVES):
    new = []
    for state, pr, sc, sl in paths:
        ms = menu(state)
        Z, Zp = zq(state, BETA0)
        # per-state Fisher info (analytic)
        e1 = sum(m ** (-BETA0) * math.log(m) for m in ms) / Z
        e2 = sum(m ** (-BETA0) * math.log(m) ** 2 for m in ms) / Z
        istep_by_t[t] += pr * (e2 - e1 * e1)
        for m in ms:
            pm = m ** (-BETA0) / Z
            dsc = -math.log(m) - Zp / Z
            new.append((state * m, pr * pm, sc + dsc, sl + [state]))
    paths = new

I_path = sum(istep_by_t)
byN = {}
for state, pr, sc, sl in paths:
    byN.setdefault(state, []).append((pr, sc))
I_state = 0.0
I_miss = 0.0
mean_score = 0.0
for N, lst in byN.items():
    PN = sum(pr for pr, _ in lst)
    sobs = sum(pr * sc for pr, sc in lst) / PN
    I_state += PN * sobs * sobs
    I_miss += PN * (sum(pr * sc * sc for pr, sc in lst) / PN - sobs ** 2)
    mean_score += PN * sobs
print(f"  truncated world: menu <= {MENU_MAX}, {NMOVES} moves, "
      f"{len(paths)} paths, {len(byN)} end states, beta0 = {BETA0}")
print(f"  I_path  = {I_path:.9f}")
print(f"  I_state = {I_state:.9f}   (the aged snapshot)")
print(f"  I_route = {I_miss:.9f}   (the route posterior)")
print(f"  I_state + I_route - I_path = {I_state + I_miss - I_path:.2e}")
check(abs(mean_score) < 1e-9, "S2 mean score != 0")
check(abs(I_state + I_miss - I_path) < 1e-9 * max(1.0, I_path),
      "PR2 Louis identity")
check(I_miss > 1e-3, "PR2 the gap is real")
check(I_state < I_path, "S2 snapshot strictly lossy")
print("  PR2 PASS: what watching buys over the snapshot is EXACTLY the "
      "Fisher information of the route posterior")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("S3  THE DEMAND CHAIN: cold blindness, clocks, existential probe")
print("=" * 72)


def sqfree(m):
    return all(e == 1 for _, e in factor(m))


def adm_ind(N, m):
    return math.gcd(N, m) == 1


def adm_mem(N, m):
    return any(N % p != 0 for p, _ in factor(m))


def adm_semi(N, m):
    return math.gcd(N, m) == 1 and sqfree(m) and sqfree(N)


def pick_of(N, adm, mmax=1000):
    for m in range(2, mmax):
        if adm(N, m):
            return m
    return None


# chain strictness specimens at N = 30
check(adm_mem(30, 14) and not adm_ind(30, 14), "S3 14 separates MEM/IND")
check(adm_ind(30, 49) and not adm_semi(30, 49), "S3 49 separates IND/SEMI")
check(adm_semi(30, 7), "S3 7 in all three")

# PR3 pick equality sweep
lim = 100000
spf = SPF
agree = 0
for N in range(2, lim + 1):
    # least prime not dividing N
    q = 2
    while N % q == 0:
        q = ALLP[ALLP.index(q) + 1] if q > 2 else 3
    # brute MEM pick: least m carrying a prime not dividing N
    mm = None
    for m in range(2, q + 1):
        x, new = m, False
        while x > 1:
            p = spf[x]
            if N % p != 0:
                new = True
                break
            while x % p == 0:
                x //= p
        if new:
            mm = m
            break
    check(mm == q, f"S3 MEM pick at {N}: {mm} != {q}")
    # IND pick: least coprime
    mi = None
    for m in range(2, q + 1):
        if math.gcd(N, m) == 1:
            mi = m
            break
    check(mi == q, f"S3 IND pick at {N}: {mi} != {q}")
    agree += 1
print(f"  PR3 PASS: IND pick == MEM pick == least new prime, "
      f"{agree}/{lim - 1} states")

nsq = 0
for N in range(2, 3001):
    if sqfree(N):
        ps = pick_of(N, adm_semi)
        pi = pick_of(N, adm_ind)
        check(ps == pi, f"S3 SEMI pick at {N}: {ps} != {pi}")
        nsq += 1
print(f"  SEMI pick == IND pick on all {nsq} squarefree N <= 3000")

# cold blindness: identical T=0 trajectories
for seed in (1, 30, 105):
    Ns = [seed, seed, seed]
    for step in range(25):
        picks = [pick_of(Ns[0], adm_ind), pick_of(Ns[1], adm_mem),
                 pick_of(Ns[2], adm_semi)]
        check(picks[0] == picks[1] == picks[2],
              f"S3 trajectories diverge at seed {seed} step {step}")
        Ns = [n * p for n, p in zip(Ns, picks)]
print("  COLD BLINDNESS: 25-step T=0 trajectories identical for all "
      "three demands (seeds 1, 30, 105) -- the watcher gets ZERO bits")

# discrimination clocks: closed forms + brute check


def Z_closed(N, beta, which):
    pl = [p for p, _ in factor(N)]
    if which == "IND":
        v = zeta_d(beta, 0)
        for p in pl:
            v *= (1 - p ** (-beta))
        return v - 1
    if which == "MEM":
        prod = 1.0
        for p in pl:
            prod *= (1 - p ** (-beta))
        return zeta_d(beta, 0) - 1 / prod
    if which == "SEMI":
        v = zeta_d(beta, 0) / zeta_d(2 * beta, 0)
        for p in pl:
            v /= (1 + p ** (-beta))
        return v - 1
    raise ValueError


for which, adm in (("IND", adm_ind), ("MEM", adm_mem), ("SEMI", adm_semi)):
    zc = Z_closed(30, 2.0, which)
    M = 200000
    zb = sum(m ** (-2.0) for m in range(2, M + 1) if adm(30, m))
    check(abs(zc - zb) < 2.0 / M + 1e-9,
          f"S3 Z_{which}(30) closed {zc} vs brute {zb}")
print("  normalizer closed forms verified against brute (N = 30)")

# the differences are brute-summed directly (closed-form differencing
# cancels catastrophically at high beta); tails negligible relative
kl_im = {}
kl_si = {}
MKL = 200000
for beta in (2.0, 4.0, 6.0, 8.0, 10.0):
    zi = d_im = d_si = 0.0
    for m in range(2, MKL + 1):
        w = m ** (-beta)
        i = adm_ind(30, m)
        if i:
            zi += w
            if not adm_semi(30, m):
                d_si += w
        elif adm_mem(30, m):
            d_im += w
    zs = zi - d_si
    kl_im[beta] = math.log1p(d_im / zi)
    kl_si[beta] = math.log1p(d_si / zs)
    if beta == 2.0:
        check(abs(kl_im[beta] -
                  math.log(Z_closed(30, beta, "MEM") /
                           Z_closed(30, beta, "IND"))) < 1e-3,
              "S3 KL brute vs closed form (IND/MEM)")
        check(abs(kl_si[beta] -
                  math.log(Z_closed(30, beta, "IND") /
                           Z_closed(30, beta, "SEMI"))) < 1e-3,
              "S3 KL brute vs closed form (SEMI/IND)")
print("  KL(IND||MEM) at N=30: " +
      ", ".join(f"b={b}: {kl_im[b]:.3e}" for b in kl_im))
print("  KL(SEMI||IND) at N=30: " +
      ", ".join(f"b={b}: {kl_si[b]:.3e}" for b in kl_si))
check(0.2 <= kl_im[2.0] <= 0.7, "PR4 KL(IND||MEM) beta=2 band")
slope_im = (math.log(kl_im[8.0]) - math.log(kl_im[10.0])) / 2
slope_si = (math.log(kl_si[8.0]) - math.log(kl_si[10.0])) / 2
check(abs(slope_im - math.log(2)) < 0.1 * math.log(2),
      f"PR4 IND/MEM clock: slope {slope_im} != log 2")
check(abs(slope_si - math.log(7)) < 0.1 * math.log(7),
      f"PR4 SEMI/IND clock: slope {slope_si} != log 7")
print(f"  PR4 PASS: discrimination clocks log(m*/q): IND/MEM slope "
      f"{slope_im:.4f} (log 2 = {math.log(2):.4f}), SEMI/IND slope "
      f"{slope_si:.4f} (log 7 = {math.log(7):.4f})")
print("  KL(MEM||IND) = +inf (support): under MEM-truth one witnessed "
      "off-support move identifies SURELY, geometric time")

# the existential probe: scar 30 -> 60
check(all(not adm_semi(60, m) for m in range(2, 10001)),
      "S3 SEMI dead at 60 (scan)")
N = 60
opened = []
for _ in range(20):
    m = pick_of(N, adm_ind)
    opened.append(m)
    N *= m
check(opened[:5] == [7, 11, 13, 17, 19], "S3 IND heals after scar")
check(fd_of(N).get(2, 0) == 2, "S3 the scar persists through healing")
print("  EXISTENTIAL PROBE: one gcd-push (30 -> 60) kills D-SEMI "
      "instantly (admissible empty: Nm never squarefree); D-IND heals "
      "on (picks 7, 11, 13, ...) carrying the scar forever")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("S4  THE SCAR LEDGER: permanence, forgery, deniability")
print("=" * 72)

rng = random.Random(153)

# permanence under thermal continuation (definitional; 200 runs)
for run in range(200):
    N = 60
    for _ in range(30):
        # thermal D-IND pick from truncated menu
        ms = [m for m in range(2, 60) if math.gcd(m, N) == 1]
        ws = [m ** (-2.0) for m in ms]
        tot = sum(ws)
        r = rng.random() * tot
        acc = 0.0
        for m, w in zip(ms, ws):
            acc += w
            if acc >= r:
                break
        N *= m
    check(fd_of(N).get(2, 0) == 2, f"S4 scar erased in run {run}")
print("  200/200 thermal continuations: the 2-scar persists "
      "(multiplication never removes -- the healing rule's dark half)")

# the earlier MLE harness
MLE_PRIMES = [p for p in ALLP if p <= 3000]


def mle_score(profile, beta):
    s = 0.0
    for p, d in profile:
        u = p ** (-beta)
        s += -(d - 1) * math.log(p) + math.log(p) * u / (1 - u)
    return s


def mle(profile, lo=1.05, hi=12.0):
    if mle_score(profile, hi) > 0:
        return None  # crystal reading
    for _ in range(60):
        mid = (lo + hi) / 2
        if mle_score(profile, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def sample_thermal_profile(beta, rnd):
    prof = []
    for p in MLE_PRIMES:
        d = 1
        while rnd.random() < p ** (-beta):
            d += 1
        prof.append((p, d))
    return prof


# forgery: 300 forged worlds (crystal + geometric scars at beta 2)
crys = 0
finites = []
for rep in range(300):
    prof = sample_thermal_profile(2.0, rng)
    est = mle(prof)
    if est is None:
        crys += 1
    else:
        finites.append(est)
frac = crys / 300
condmean = sum(finites) / len(finites)
print(f"  FORGERY: 300 forged states (crystal + sampled scars): "
      f"{frac:.3f} read CRYSTAL (thermal law 1/zeta(2) = 0.608), "
      f"conditional mean beta-hat = {condmean:.3f}")
check(0.55 <= frac <= 0.70, "PR5 forged crystal fraction")
check(1.4 <= condmean <= 1.9, "PR5 forged conditional mean")

# single 2-scar world
prof1 = [(p, 1) for p in MLE_PRIMES]
prof1[0] = (2, 2)
est1 = mle(prof1)
check(est1 is not None and 1.2 <= est1 <= 8.0, "PR5 single-scar MLE")
print(f"  a SINGLE 2-scar on the crystal reads as temperature "
      f"beta-hat = {est1:.3f} (the crystal reading is infinity)")

# deniability split
check(not adm_ind(30, 2), "S4 gcd-push off-support")
# thermal route to 60: 1 -> 3 -> 15 -> 60 via moves 3, 5, 4
route = [(1, 3), (3, 5), (15, 4)]
pr = 1.0
for st, mv in route:
    check(adm_ind(st, mv), f"S4 route move {mv} at {st} inadmissible")
print("  DENIABILITY SPLIT: the push 2 at state 30 has probability 0 "
      "under thermal D-IND (off-support: watcher-SIGNED), yet state 60 "
      "is thermally reachable (route 1 -3-> 3 -5-> 15 -4-> 60: "
      "state-DENIABLE). A coprime scar (move 4 at state 15) is "
      "positive-probability: deniable even to the watcher.")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("S5  THE UNIVERSAL RUDDER")
print("=" * 72)

# relock-at-2: push to e = max(3, v2(lambda)+2)
specials = [fd_of(x) for x in (3 ** 15, 17 ** 6, 5 ** 10, 510510, 24,
                               240, 504, 30030, 2 ** 20, 1)]
states = specials + [fd_of(rng.randrange(2, 10 ** 6)) for _ in range(190)]
relocked = 0
already = 0
for st in states:
    lam = lam_fd(st)
    a = lam.get(2, 0)
    etgt = max(3, a + 2)
    r = etgt - st.get(2, 0)
    cur = dict(st)
    if r > 0:
        cur = fd_mul(cur, {2: r})
    else:
        already += 1
    for step in range(30):
        m = pick_dyn(cur)
        check(m == 2, f"S5 relock miss at {fd_int(st)} step {step}: "
                      f"pick {m}")
        cur = fd_mul(cur, {2: 1})
    relocked += 1
print(f"  PR6 PASS: {relocked}/200 states re-locked at 2 by ONE push "
      f"2^r to depth max(3, v2(lambda)+2) ({already} already there); "
      f"30 post-push picks all = 2")


def door_all(st, q_max=200):
    """All door prices (least lambda-growing power per prime) up to a
    scan bound; returns dict prime -> door cost."""
    lam0 = lam_fd(st)
    doors = {}
    for q in [p for p in ALLP if p <= q_max]:
        for r in range(1, 40):
            cand = q ** r
            if cand > 10 ** 12:
                break
            if lam_fd(fd_mul(st, {q: r})) != lam0:
                doors[q] = cand
                break
    return doors


def build_rudder(st, q):
    """One-push steering of state st to the q-column: q^r * (optional
    Dirichlet prime P). Returns the push as a factor dict."""
    lam = lam_fd(st)
    a = lam.get(q, 0)
    r = a + 2 - st.get(q, 0)
    push = {q: r}
    # provisional post-push doors
    test = fd_mul(st, push)
    doors = door_all(test, q_max=max(50, q + 1))
    bad = {s: c for s, c in doors.items() if s != q and c < q}
    if not bad:
        return push, None
    # need P: build B raising each bad rival's lambda-part
    B = {}
    for s in bad:
        es = test.get(s, 0)
        ts = 1
        while s ** ts <= q:
            ts += 1
        need = max(0, es + ts - 2) if es else max(0, ts - 2)
        if need:
            B[s] = max(B.get(s, 0), need)
        if not es:
            B = fd_lcm(B, fd_of(s - 1) if s > 2 else {})
    Bn = fd_int(B)
    # CRT: P == 1 mod Bn, P == g mod q with g != 1
    g = 2 if q != 2 else 1
    modulus = Bn * q
    # solve x == 1 (Bn), x == g (q)
    inv = pow(Bn, -1, q)
    x0 = (1 + Bn * ((g - 1) * inv % q)) % modulus
    j = 0
    while True:
        P = x0 + j * modulus
        j += 1
        if P > max(3, q) and is_prime(P) and fd_int(st) % P != 0:
            try:
                factor(P - 1)
            except ValueError:
                continue
            return push, P


targets = [3, 5, 7, 13]
bases = [fd_of(30), fd_of(3 ** 15), fd_of(2 ** 20), fd_of(510510)]
steered = 0
for st in bases:
    for q in targets:
        push, P = build_rudder(st, q)
        cur = fd_mul(st, push)
        if P is not None:
            cur = fd_mul(cur, {P: 1})
        for step in range(30):
            m = pick_dyn(cur)
            check(m == q, f"S5 rudder miss: state {fd_int(st)} -> q={q}"
                          f" step {step}: pick {m}")
            cur = fd_mul(cur, {q: 1})
        steered += 1
        ptxt = f" * P={P}" if P else ""
        print(f"    state {fd_int(st):>12} -> column {q}: push "
              f"{q}^{push[q]}{ptxt}: LOCKED (30 steps)")
check(steered == 16, "PR7 rudder census")
print(f"  PR7 PASS: {steered}/16 (state, target) pairs steered by ONE "
      f"push -- the depth fate is one-push controllable to ANY prime")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("S6  THE PHOENIX (mortality + minimal life support)")
print("=" * 72)


def odd_part(fd):
    return {p: e for p, e in fd.items() if p != 2}


def phoenix(seed, v2max):
    """Run D-TRA greedy; at each death push m = 2. Returns (window
    events [(p, v2-of-lambda-at-opening)], DNA history, fills, pushes,
    wall_pick_ok)."""
    st = fd_of(seed) if seed > 1 else {}
    lam = lam_fd(st)
    dna0 = odd_part(lam)
    events = []
    fills = []
    pushes = 0
    wall_pick2 = True
    known = set(st)
    while True:
        W = W_of(lam)
        check(fd_divides(st, W), f"S6 phoenix({seed}): state !| wall")
        cof = {p: e - st.get(p, 0) for p, e in W.items()
               if e - st.get(p, 0) > 0}
        if not cof:
            if lam.get(2, 0) >= v2max:
                break  # the terminal wall is filled before stopping
            # dead: check the D-DYN pick here is 2, then push 2
            if pick_dyn(st) != 2:
                wall_pick2 = False
            st = fd_mul(st, {2: 1})
            pushes += 1
            lam = lam_fd(st)
            check(odd_part(lam) == dna0,
                  f"S6 phoenix({seed}): DNA drifted at push {pushes}")
            fills.append(0)
        else:
            p = min(p for p in cof)
            if p not in known and p != 2:
                events.append((p, lam.get(2, 0)))
                known.add(p)
            st = fd_mul(st, {p: 1})
            if fills:
                fills[-1] += 1
            lam2 = lam_fd(st)
            check(lam2 == lam, f"S6 phoenix({seed}): fill not "
                               f"transparent at {p}")
    return st, events, dna0, fills, pushes, wall_pick2


# seed 1: the Fermat phoenix
st1, ev1, dna1, fills1, pushes1, wp1 = phoenix(1, 40)
check(dna1 == {}, "PR8 seed-1 DNA != 1")
check(wp1, "PR8 the wall's own D-DYN pick is 2 (rudder-primed walls)")
check([e[0] for e in ev1] == [3, 5, 17, 257, 65537],
      f"PR8 seed-1 windows: {[e[0] for e in ev1]}")
check([e[1] for e in ev1] == [1, 2, 4, 8, 16],
      f"PR8 seed-1 thresholds: {[e[1] for e in ev1]}")
print(f"  SEED 1: odd windows {[e[0] for e in ev1]} opened at "
      f"v2(lambda) = {[e[1] for e in ev1]} -- THE FERMAT PRIMES, at "
      f"their Fermat exponents; no sixth window through lambda = 2^40")
# fills1[i] = fill after the push raising v2(lambda) to i+1; 65537
# opens in the fill after push 16, so EVERY later fill (pushes
# 17..40) must be empty -- the claim printed below, asserted in full
late_fills = fills1[16:]
check(len(late_fills) == 24 and all(f == 0 for f in late_fills),
      "PR8 late fills nonempty (should be dead-on-arrival)")
print(f"  {pushes1} pushes total; every fill after 65537 is EMPTY: "
      f"the world is on permanent life support, one push per epoch")

# seed 7: the Pierpont-type phoenix (D = 3)
st7, ev7, dna7, fills7, pushes7, wp7 = phoenix(7, 12)
check(dna7 == {3: 1}, "PR8 seed-7 DNA != 3")
got7 = sorted(p for p, _ in ev7 if p < 3000)
res7 = sorted(set(list(fd_of(7))) | set(p for p, _ in ev7))
want7 = [3, 5, 13, 17, 97, 193, 257, 769]  # opened (7 resident in seed)
check(got7 == want7, f"PR8 seed-7 spectrum: {got7} != {want7}")
check(st7.get(3, 0) == 2, "PR8 seed-7 window 3 at depth v_3(D)+1 = 2")
print(f"  SEED 7 (DNA = 3): windows {sorted(res7)} -- the family "
      f"odd(p-1) | 3 (Pierpont 2^a 3 + 1 and Fermat); window 3 at "
      f"depth 2 = v_3(DNA)+1")

# the criterion assert: opened == predicted, several seeds
for seed, v2m in ((1, 20), (2, 20), (3, 20), (15, 20), (7, 12), (11, 12)):
    stx, evx, dnax, _, _, wpx = phoenix(seed, v2m)
    check(wpx, f"S6 seed {seed}: a wall's D-DYN pick != 2")
    D = fd_int(dnax)
    resident = set(fd_of(seed)) if seed > 1 else set()
    got = set(p for p, _ in evx) | {p for p in resident if p != 2}
    want = set()
    for p in ALLP:
        if p == 2 or p > 10 ** 5:
            continue
        pm = p - 1
        v2p = 0
        while pm % 2 == 0:
            pm //= 2
            v2p += 1
        if D % pm == 0 and v2p <= v2m and (2 ** v2p) * pm <= \
                fd_int(lam_fd(stx)):
            # p-1 | 2^t * D at some reached lambda
            if fd_divides(fd_of(p - 1), lam_fd(stx)):
                want.add(p)
    check(got == want, f"S6 criterion seed {seed}: {sorted(got)} != "
                       f"{sorted(want)}")
print("  THE SPECTRUM LAW verified at 6 seeds: windows ever opened == "
      "{p : (p-1) | 2^t * DNA} exactly (DNA = odd(lambda(seed)), "
      "frozen at birth)")
print("  THE FERMAT CRITERION: phoenix(seed 1) opens infinitely many "
      "windows IFF there are infinitely many Fermat primes")

# ----------------------------------------------------------------------
print()
print("=" * 72)
print("S7  SYNTHESIS")
print("=" * 72)
print("""  WATCH: per-move temperature info is bounded below in BOTH fates
  (linear growth) while the snapshot is zeta-capped in breadth: the
  amnesia is a property of states, not processes -- witnessing
  equalizes the fates, and the watching-vs-snapshot gap is EXACTLY
  the route posterior's information (Louis identity, S2).
  PROBE: at T = 0 the demand chain SEMI < IND < MEM writes one
  trajectory -- the law is invisible to any eternal watcher, one
  admissibility probe separates it; heat separates at the
  discrimination clock log(m*/q).  One push separates existentially
  (SEMI dies, IND heals).
  HAND: breadth sells INSCRIPTION (scars are the only fossils, and
  they forge temperature); depth sells DESTINATION (one push, any
  column); mortality sells TIME -- and the minimal price of time is
  the Fermat primes.""")
print(f"\nALL CHECKS PASS: {CHECKS}")
