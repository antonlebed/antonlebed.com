"""explore_shifted_prime_density.py — the lower bound's engine: the density of
shifted primes with a large prime factor, and the two constants it is NOT.

THE QUESTION. A companion to explore_lcm_shifted_primes.py, which proved the
UPPER bound L(x) = log lcm{p-1 : p <= x} << x loglog x/log x (unconditional,
a prime-pair sieve) and left the MATCHING LOWER bound L(x) >> x loglog x/log x
open. This engine charts the object the lower bound rests on and separates two
constants the literature and our own docs risk conflating.

  L(x) = sum_{q <= x} log q * 1[q | some p-1 <= x]  (+ o(sqrt x log x)).

Its log-mass is dominated by the LARGEST prime factors: L_large (q > x/log x)
is the growing bulk. A prime q > x/log x divides some p-1 <= x iff p = mq+1 is
prime for some (even) m < log x, i.e. iff P+(p-1) = q for some p <= x. So the
lower bound reduces to counting primes p <= x with a large largest-prime-factor
P+(p-1), across the range where that count is exactly the sieve's upper bound.

WHY IT IS HARD (the hardness map, from full-text literature contact). Writing
P+(p-1) = x^c, the density of primes with P+(p-1) > x^c is, UNDER the
Elliott-Halberstam conjecture, the Dickman value

    #{p <= x : P+(p-1) > x^c} / pi(x)  ->  -log c        (1/2 < c < 1).

Unconditionally a LOWER bound on this density (a positive proportion of p) is
known only for c bounded well away from 1: c up to ~0.677 (Baker-Harman 1998;
~0.679 with Maynard-type improvements). The unconditional results NEAR c = 1 run
the OTHER way -- UPPER bounds on the density (Ding-Wang arXiv:2510.04026,
lim sup T_c(x)/pi(x) <= (7/2)(-log c) for fixed c > e^{-2/7} ~ 0.751, via a BFI
estimate at level x^{4/7-eps}) -- the wrong direction for a lower bound. The lower
bound on L needs c -> 1 (the range q ~ x/log x = x^{1-o(1)}), where the EH/Dickman
density -log c ~ loglog x/log x supplies exactly the sieve upper bound's order.
That range demands primes in arithmetic progressions to moduli approaching x --
BEYOND Bombieri-Vinogradov (level x^{1/2}) and BFI (x^{4/7}); it is an
Elliott-Halberstam-strength input. So the matching lower bound is EH-HARD, not
merely Bombieri-Vinogradov-adjacent. Under EH it follows (the -log c density at
c -> 1 supplies the order, modulo a distinct-vs-multiplicity step); unconditionally
it is out of reach. The UPPER bound, by contrast, needs only a sieve upper bound and
stays unconditional.

TWO CONSTANTS, NOT ONE. The vanishing rate is alpha(x) = L(x)/log phi(N_x) ~
c_L * loglog x/log x, with c_L the LCM-RATE constant (numerics ~0.76). This is a
DIFFERENT quantity from the SIZE-RESERVE threshold

    rho_c = lim sum_{p<=x} log P+(p-1) / theta(x)   ->   Golomb-Dickman 0.6243

(under EH; the reserve solvency threshold of the size-weighted growth fate). rho_c
measures the PRODUCT-side largest-prime-factor mass sum log P+(p-1) ~ rho_c * x
(a Theta(x) quantity, WITH multiplicity), normalised by theta(x). c_L measures the
LCM-side rate (L is o(x); DISTINCT large primes only). They have different
normalisations and different values (0.76 vs 0.6243); the heuristic (EH, distinct
~ multiplicity in the top range) makes c_L order 1, not Golomb-Dickman. Calling
c_L "the rate's constant = Golomb-Dickman" conflates the two. This engine puts
r(x) = L log x/(x loglog x) [-> c_L] and rho_c(x) = sum log P+/theta [-> GD] on the
SAME primes so the separation is visible.

PREDICTIONS P1-P3 (fixed before the run, from the hand analysis + the EH density
law above; findings enter by a separate post-run edit copying printed output):
  P1 (the EH density law). At x ~ 1e7, D(x,c) = #{p<=x : P+(p-1) > x^c}/pi(x) is
     positive and strictly decreasing over the grid c in {0.55,...,0.85}, and of
     the SAME ORDER as the EH/Dickman value -log c: the ratio D(x,c)/(-log c) lies
     in (0.4, 1.3) at every grid c. Finite-x undershoot GROWS toward c -> 1 (the
     ratio decreases along the grid), because the extreme top range is where the
     sieve scale is only ~half realised at x = 1e7. Confirms our shifted primes
     obey the largest-prime-factor law whose c -> 1 tail is the lower bound's engine.
  P2 (the extreme tail = the census). At c* = 1 - loglog x/log x (the split
     point x/log x), D(x,c*) reproduces the companion script's census fraction
     f ~ 0.09-0.10 (cross-check, agree to ~2 sig figs), and D(x,c*)/(-log c*) is in
     (0.4, 0.7) -- the ~0.5 Dickman-scale undershoot at finite x that keeps the
     proved upper bound's constant out of reach of the numerics.
  P3 (two distinct constants). On the same primes at every milestone (1e5, 1e6,
     1e7): r(x) = L(x) log x/(x loglog x) [-> c_L, ~0.76] and rho_c(x) =
     sum log P+(p-1)/theta(x) [-> Golomb-Dickman 0.6243, in-range ~0.53-0.58] are
     DISTINCT and non-crossing -- r(x) > rho_c(x) with r - rho_c > 0.12 at every
     milestone. The LCM-rate constant is NOT the size-reserve/GD threshold.

DESIGN. Thin, import-free. Sieve primes to X_MAX = 1e7 (bytearray, ~10 MB);
one size-ordered pass factoring each p-1 by trial division over primes <= sqrt
(early break), tracking running max exponents to grow L = log lcm, accumulating
theta(x) = sum_{p<=x} log p and S(x) = sum_{p<=x} log P+(p-1), and storing P+(p-1)
per prime for the density curve. At each milestone snapshot L, theta, S; after the
pass compute D(x,c) over the c-grid and the census at c*. A few seconds, well under
512 MB, no numpy. All sections assert.

HONEST SCOPE. The hardness classification (EH-hard lower bound; unconditional
lower-bound frontier c ~ 0.677, the near-c=1 unconditional results being upper
bounds) is HAND-DERIVED from full-text literature contact
(Baker-Harman; Ding-Wang arXiv:2510.04026 and the BFI level x^{4/7}; the EH
Dickman density; the friable-EH machinery). This engine only CHARTS the density
law our data obeys and the numeric separation of the two constants -- a
consistency check, not a proof of the lower bound (which is EH-conditional). The
asymptotic value of c_L is itself open (EH-conditional); the numerics pin only
that it is ~0.76 in range and distinct from Golomb-Dickman.

FINDINGS (run record at bottom; all sections assert).

1. TWO DISTINCT CONSTANTS (P3, confirmed -- the headline). On the same primes:
   r(x) = L log x/(x loglog x) falls 0.7786 -> 0.7661 -> 0.7637 (x=1e5,1e6,1e7),
   while rho_c(x) = sum log P+(p-1)/theta(x) RISES 0.5791 -> 0.5888 -> 0.5954. They
   are numerically distinct in range and move from OPPOSITE SIDES -- c_L (~0.76, the
   LCM/alpha rate constant) above, Golomb-Dickman 0.6243 (the size-reserve threshold
   rho_c) below -- never crossing: r - rho_c = 0.20, 0.18, 0.17 > 0.12 throughout.
   These are DIFFERENT QUANTITIES: distinct-lcm rate (an o(x) sum, normalised by
   x loglog x/log x) vs product-side P+ mass (a Theta(x) sum, normalised by theta ~ x).
   So "the rate's constant" (c_L) is not identifiable with the size-reserve /
   Golomb-Dickman threshold rho_c; c_L's own limit is open (whether it happens to
   share a numeric value with GD is itself open, but the quantities are not the same).

2. THE EH DENSITY LAW (P1, confirmed). D(x,c) = #{p<=x : P+(p-1) > x^c}/pi(x) at
   x=1e7 falls monotone 0.479 (c=0.55) -> 0.068 (c=0.85), tracking the EH/Dickman
   value -log c at the same order: the ratio D/(-log c) sits in (0.42, 0.80) and
   DECREASES steadily along the grid (0.80 -> 0.42), i.e. the finite-x undershoot
   grows toward c -> 1. So our shifted primes obey the largest-prime-factor law
   whose c -> 1 tail (-log c ~ loglog x/log x) is exactly the lower bound's engine;
   the growing top-range undershoot is why the proved upper bound's constant is not
   yet reached at x = 1e7 (and why the matching lower bound needs the c -> 1 / EH
   regime, not any fixed-c range).

3. THE EXTREME TAIL = THE CENSUS (P2, confirmed). At c* = 0.8275 = 1 - loglog x/log x
   (the companion script's split point x/log x = 620422), D(x,c*) = 0.08968 -- reproducing the
   companion script's census fraction f ~ 0.09 to 2 sig figs -- and D(x,c*)/(-log c*)
   = 0.4737, the ~0.5 Dickman-scale undershoot. The extreme tail of the density
   curve IS the large-q census the o(x) upper bound caps; at finite x it realises
   only ~half the Dickman scale, consistent with the flat r ~ 0.76 sitting below the
   heuristic asymptotic.

RUN RECORD (this file, ~1.9 s, 8 checks, ~10 MB, no numpy; all sections assert, no
misses). Milestones x in {1e5, 1e6, 1e7} (x = first prime >= target); density grid
c in {0.55,...,0.85} at x=1e7; c* = 1 - loglog x/log x. Predictions P1-P3 worked out
by hand from the EH density law + literature contact before the run. All three hit:
P1 (D decreasing, ratio in band + decreasing toward c->1), P2 (census f ~ 0.09,
ratio ~0.47), P3 (r ~ 0.76 and rho_c ~ 0.58-0.60 distinct, non-crossing, opposite-
side convergence). The hardness classification (EH-hard lower bound; unconditional
lower-bound frontier c ~ 0.677 Baker-Harman -- the 0.751/BFI-level-4/7 Ding-Wang
result is an UPPER bound, the other direction) is literature-derived, not
computed here -- this engine charts only the density law and the constant separation.

Companions: explore_lcm_shifted_primes.py (the o(x) UPPER bound),
explore_ledger_threshold.py / explore_reserve_zoo.py (the size-reserve threshold
rho_c -> Golomb-Dickman).
"""

import sys
from math import log


X_MAX = 10 ** 7 + 100000
MILESTONES = [10 ** 5, 10 ** 6, 10 ** 7]
C_GRID = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85]

PASS = 0
FAIL = 0


def ok(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {msg}")


def sieve_primes(n):
    """All primes <= n via a byte sieve."""
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    i = 2
    while i * i <= n:
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
        i += 1
    return [i for i in range(2, n + 1) if s[i]]


def build():
    """One size-ordered pass over primes p <= X_MAX: grow L = log lcm(p-1) via
    running max exponents; accumulate theta = sum log p and S = sum log P+(p-1);
    store P+(p-1) per prime. Snapshot (L, theta, S, pi) at each milestone."""
    primes = sieve_primes(X_MAX)
    small = [q for q in primes if q * q <= X_MAX]
    running = {}
    L = 0.0
    theta = 0.0
    S = 0.0
    pplus = []
    pcount = 0
    ms_idx = 0
    snaps = []
    for p in primes:
        theta += log(p)
        if p == 2:
            pplus.append(1)
            pcount += 1
            if ms_idx < len(MILESTONES) and p >= MILESTONES[ms_idx]:
                snaps.append(dict(x=p, L=L, theta=theta, S=S, pi=pcount))
                ms_idx += 1
            continue
        n = p - 1
        big = 1
        for q in small:
            if q * q > n:
                break
            if n % q == 0:
                e = 0
                while n % q == 0:
                    n //= q
                    e += 1
                big = q
                old = running.get(q, 0)
                if e > old:
                    L += (e - old) * log(q)
                    running[q] = e
        if n > 1:
            q = n
            if q > big:
                big = q
            old = running.get(q, 0)
            if 1 > old:
                L += log(q)
                running[q] = 1
        S += log(big)
        pplus.append(big)
        pcount += 1
        if ms_idx < len(MILESTONES) and p >= MILESTONES[ms_idx]:
            snaps.append(dict(x=p, L=L, theta=theta, S=S, pi=pcount))
            ms_idx += 1
    return snaps, pplus, primes


def density(primes, pplus, x, thr):
    """#{p <= x : P+(p-1) > thr} / pi(x)."""
    cnt = 0
    tot = 0
    for i, p in enumerate(primes):
        if p > x:
            break
        tot += 1
        if pplus[i] > thr:
            cnt += 1
    return cnt, tot


def main():
    snaps, pplus, primes = build()

    # ---- P3: the two constants on the same primes ----
    print("== P3: two distinct constants (r -> c_L ~0.76 vs rho_c -> GD 0.6243) ==")
    print(f"{'x':>9} {'L(x)':>12} {'r=Llogx/(xllx)':>15} "
          f"{'rho_c=S/theta':>13} {'r - rho_c':>10}")
    rows = []
    for s in snaps:
        x = s['x']
        L = s['L']
        llx = log(log(x))
        r = L * log(x) / (x * llx)
        rho_c = s['S'] / s['theta']
        rows.append(dict(x=x, L=L, r=r, rho_c=rho_c, pi=s['pi']))
        print(f"{x:>9} {L:>12.1f} {r:>15.4f} {rho_c:>13.4f} {r - rho_c:>10.4f}")
    ok(all(row['r'] > row['rho_c'] for row in rows),
       "r(x) > rho_c(x) at every milestone (non-crossing)")
    ok(all(row['r'] - row['rho_c'] > 0.12 for row in rows),
       "r - rho_c > 0.12 (the two constants are distinct)")

    # ---- P1: the EH density law D(x,c) vs -log c ----
    top = rows[-1]
    x = top['x']
    print(f"\n== P1: EH density D(x,c)=#{{p<=x:P+(p-1)>x^c}}/pi(x) vs -log c "
          f"(x={x}) ==")
    print(f"{'c':>5} {'x^c':>12} {'D(x,c)':>9} {'-log c':>8} {'ratio':>7}")
    Dvals = []
    ratios = []
    for c in C_GRID:
        thr = x ** c
        cnt, tot = density(primes, pplus, x, thr)
        D = cnt / tot
        dick = -log(c)
        ratio = D / dick
        Dvals.append(D)
        ratios.append(ratio)
        print(f"{c:>5.2f} {thr:>12.0f} {D:>9.5f} {dick:>8.4f} {ratio:>7.4f}")
    ok(all(D > 0 for D in Dvals), "D(x,c) > 0 over the grid")
    ok(all(Dvals[i] > Dvals[i + 1] for i in range(len(Dvals) - 1)),
       "D(x,c) strictly decreasing in c")
    ok(all(0.4 < rr < 1.3 for rr in ratios),
       "D/(-log c) in (0.4, 1.3): same order as the EH/Dickman density")
    ok(all(ratios[i] > ratios[i + 1] for i in range(len(ratios) - 1)),
       "D/(-log c) decreasing along the grid (undershoot grows toward c->1)")

    # ---- P2: the extreme tail c* = 1 - loglog x/log x = the census x/log x ----
    print(f"\n== P2: the extreme tail c* = 1 - loglog x/log x (split x/log x) ==")
    thr_star = x / log(x)
    c_star = log(thr_star) / log(x)          # = 1 - loglog x/log x
    cnt, tot = density(primes, pplus, x, thr_star)
    D_star = cnt / tot
    dick_star = -log(c_star)
    print(f"  c* = {c_star:.4f}  x/log x = {thr_star:.0f}  D(x,c*) = {D_star:.5f}"
          f"  -log c* = {dick_star:.4f}  ratio = {D_star / dick_star:.4f}")
    ok(0.05 < D_star < 0.15, "census fraction D(x,c*) ~ 0.09-0.10")
    ok(0.4 < D_star / dick_star < 0.7,
       "D(x,c*)/(-log c*) in (0.4,0.7): the ~0.5 finite-x Dickman undershoot")

    print(f"\n{PASS} checks pass, {FAIL} fail")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
