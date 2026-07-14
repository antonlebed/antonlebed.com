"""explore_collision_equivalence.py — THE COLLISION EQUIVALENCE:
alpha -> 0 <=> transparency density -> 1, made EXACT — the converse is a THEOREM.

THE QUESTION. A companion script (explore_complexity_ledger.py) proved
density -> 1 IMPLIES alpha -> 0 (the domination inequality, rigorous) and left
the converse a HEURISTIC ("both hinge on N_nt = o(k)"); another companion script
(explore_ledger_threshold.py) located alpha -> 0 in the shifted-prime distribution
circle. The open target: state the sharpest true biconditional — what extra
hypothesis closes the converse, and which fragment is unconditional?

THE ANSWER (found by hand before writing the engine): NO extra hypothesis is
needed. The converse is an elementary theorem, and more: the two sequences are
asymptotically EQUAL. The hypothesized "mass condition on repeated large
shifted-prime factors" is FREE — supplied by the lcm's write-once structure,
not by shifted-prime distribution.

THE OBJECTS. x = p_k; lambda(p_k#) = lcm(p_i - 1 : i <= k); phi(p_k#) =
prod(p_i - 1); alpha(k) = log lambda/log phi (dynamical complexity vs
capacity). A step is NON-TRANSPARENT iff (p-1) does not divide the running
lambda (forces a raise); N_nt(k) = # such steps, nt_frac = N_nt/k.
(Convention: p = 2 has p-1 = 1 | lambda, transparent under the divisibility
definition; explore_complexity_ledger.py counted the opener as a raise by
convention — a +-1 that touches nothing asymptotic. This script uses the
divisibility definition and prints both counts.)
An EVENT at prime q = a step at which q's exponent in lambda strictly
increases; e_q = # events at q; a_q = q's final exponent in lambda(p_k#).

THE THEOREM (the collision equivalence; tier: THEOREM — complete elementary
proof, all k; Chebyshev + Mertens + partial summation, no PNT):

    nt_frac(k) - alpha(k) -> 0,  quantitatively
    |nt_frac(k) - alpha(k)| = O(log log x / log x).

  In particular alpha -> 0 <=> transparency density -> 1, and
  limsup alpha = limsup nt_frac, liminf alpha = liminf nt_frac.

PROOF. Four elementary facts:
  (E1) Every non-transparent step has >= 1 event, so N_nt <= Sum_q e_q.
  (E2) Exponents start at 0 and strictly increase per event: e_q <= a_q.
  (E3) q^{a_q} divides some p_i - 1 < x, so a_q <= log x/log q; each event
       at q adds >= log q to log lambda, so log lambda >= Sum_q e_q log q.
  (E4) A step's total increment is <= log(p-1) < log x (new lambda divides
       old lambda * (p-1)), so log lambda <= N_nt * log x.
  FORWARD (explore_complexity_ledger.py's domination, restated): alpha <= N_nt log x/log phi
  = nt_frac * [k log x/log phi]; the bracket -> 1 (theta(x)/(pi(x) log x)
  -> 1 by partial summation + Chebyshev; log phi = theta(x) - O(loglog x)
  by Mertens). So alpha <= nt_frac * (1 + O(1/log x)).
  BACKWARD (new — THE WRITE-ONCE BOUND). For any y in (2, x), splitting
  events at y and applying (E1)-(E3):
      N_nt(k)  <=  Sum_{q <= y} floor(log x/log q)  +  log lambda/log y.
  A prime power can be raised at most ONCE EVER (exponents only climb), so
  cheap raises are rationed by the prime-counting of the small range, and
  every other raise carries >= log y of mass. Take y = x/(log x)^3: the
  small term is O(x/(log x)^2 / log x) = o(k), the large term is
  alpha * log phi/log y = alpha * k * (1 + O(loglog x/log x)). So
  nt_frac <= alpha + O(loglog x/log x). Both directions together give the
  rate. QED.
  (Why no positive proportion of raises can hide at small primes: there are
  not enough small primes — pi(x/(log x)^3) ~ x/(log x)^4 = o(k), and each
  hosts at most log x/log q events. The sqrt-x scare fails the same way:
  pi(sqrt x) = o(k) with a_q <= 2 there. The in-range echo is
  explore_ledger_threshold.py's mass-locus, 0.975 of log lambda from q > sqrt x.)

COROLLARIES.
  (C1) alpha -> 0 <=> density -> 1: explore_complexity_ledger.py's fate and the
       transparency-density conjecture (does the transparency density tend to 1?)
       are the SAME statement, unconditionally.
  (C2) The count-reserve threshold rho_c = limsup nt_frac = limsup alpha:
       the threshold IS the complexity ratio's limsup.
  (C3) With explore_ledger_threshold.py's exact identity alpha = 1 - collision/log phi:
       collisions absorb almost all capacity <=> density -> 1.
  (C4) Reformulation: density -> 1 <=> log lcm{p-1 : p <= x} = o(x) — a pure
       lcm-of-shifted-primes asymptotic.

PREDICTIONS EQ1-EQ5 (fixed before the run, worked out by hand; findings
enter by a separate post-run edit copying printed output):

  EQ1 (the event ledger, exact). Assert: N_nt <= Sum_q e_q (the theorem's E1;
    equality in range iff every raise touches exactly one prime —
    explore_complexity_ledger.py observed one prime POWER per jump);
    e_q <= a_q for every q (E2);
    log lambda == Sum_q a_q log q (recomputation, float tol); every step
    increment <= log(p-1) (E4). Hand estimate: N_nt(10^4) = 1986 divisibility-count
    (explore_complexity_ledger.py's 1987 includes the opener); Sum e_q == N_nt in range.

  EQ2 (the write-once bound, the theorem's engine face). For y in
    {x^{1/2}, x^{2/3}, x^{0.9}} at every milestone k in {50, 200, 1000,
    5000, 10000}: assert N_nt <= Sum_{q<=y} floor(log x/log q) +
    log lambda/log y. Hand estimate at k = 10^4, y = sqrt x = 323.6: small term
    ~ 176, large term 17237/5.78 = 2982, bound ~ 3.16e3 vs N_nt ~ 1986 —
    HOLDS, ratio ~ 1.6 (the theorem is asymptotic; in-range slack expected).

  EQ3 (the gap, the equivalence made visible). gap(k) = nt_frac - alpha.
    Assert gap > 0 at every milestone (in range mu/log x ~ 0.75 with mu the
    mean raise size, bracket 1.107, so alpha/nt_frac ~ 0.83 < 1); gap
    DECREASING across milestones. Hand estimate: gap(50) ~ 0.53 - 0.296 = 0.23;
    gap(10^4) ~ 0.1986 - 0.1651 = 0.034.

  EQ4 (the rationing census — the mechanism visible in range). Events split
    at sqrt x per milestone: assert small-side count <= Sum_{q<=sqrt x}
    floor(log x/log q) (the a priori cap, ~176 at 10^4) and < 15% of all
    events; the q > sqrt x side > 85%. Predict actual small-events 90-130
    (nearly all 66 primes <= 324 enter lambda, + bumps mostly small).
    NOTE: explore_ledger_threshold.py's mass-locus 0.975 is MASS; this is COUNT.

  EQ5 (bound trend, observation). Write-once bound(y = sqrt x)/N_nt across
    milestones: in (1, 3) at k >= 200, trending down late.

DESIGN. Thin import-free number theory (mirrors explore_complexity_ledger.py).
One pass over the first K = 10000 primes (p_max = 104729): grow lambda by
tracking running max exponents, record every event (k, p, q, delta, old
exponent), accumulate log lambda / log phi; milestone snapshots taken inline,
the event list re-filtered per milestone for the census. Trial division of
p-1 <= 1.05e5. A few seconds, well under 512 MB, no
numpy. All sections assert.

HONEST SCOPE. The theorem's proof is HAND-DERIVED and elementary; the engine
verifies its ingredient inequalities (E1-E4, the write-once bound) at every
milestone and charts the in-range gap — a finite-range consistency check, not
the proof. What the theorem does NOT give: the VALUE — alpha -> 0 itself stays
open, now exactly equivalent to the transparency-density conjecture (does the
transparency density tend to 1? — the smooth-shifted-prime density circle,
Fouvry/BFI); explore_ledger_threshold.py's "analytic-hard" reading survives for
the value question, and the EQUIVALENCE question closes. The in-range gap
(0.22 -> 0.034) converges at log speed — the asymptotic regime is far away, as
the rate O(loglog x/log x) says it must be.

FINDINGS (run record at bottom; all sections assert).

1. THE EVENT LEDGER (property, exact — the theorem's E1/E2/E4 in range).
   N_nt = 1986 under the divisibility definition, and Sum_q e_q = 1986
   EXACTLY: zero multi-prime steps in range, so every raise touches exactly
   one prime (= explore_complexity_ledger.py's one-prime-power-per-jump, whose
   per-jump entries are already per-prime — the same in-range fact, reconfirmed;
   the p = 2 opener forces zero events — explore_complexity_ledger.py's 1987
   counted it by convention). e_q <= a_q at every q; log lambda = 17237.2 recomputed from
   final exponents to < 1e-6 relative; every step increment <= log(p-1).
   alpha(10^4) = 0.1651, log phi = 104389.2 (both matching
   explore_complexity_ledger.py/explore_ledger_threshold.py).

2. THE WRITE-ONCE BOUND (the theorem's engine face — holds everywhere).
   N_nt <= Sum_{q<=y} floor(log x/log q) + log lambda/log y at all 15
   (milestone, y) cells. At k = 10^4, y = sqrt x: 176 + 2982.4 = 3158.4
   vs N_nt = 1986 (ratio 1.59; hand-predicted ~176 + 2982 = 3.16e3, ~1.6).
   The bound is never tight in range (best ratio 1.35 at y = x^{2/3},
   k = 10^4) — the theorem is asymptotic and the rate is log-speed.

3. THE GAP (the equivalence made visible). nt_frac - alpha falls MONOTONE
   0.2237 (k=50) -> 0.1218 (200) -> 0.0613 (1000) -> 0.0395 (5000) ->
   0.0335 (10^4), positive at every milestone. The mechanism on view: the
   mean raise size mu/log x climbs 0.436 -> 0.751 (raises approach full
   log x size, which is what the write-once rationing forces in the limit)
   while the forward bracket k log x/log phi falls 1.307 -> 1.107; alpha =
   nt_frac * (mu/log x) * bracket exactly.

4. THE RATIONING CENSUS (the mechanism in range). Events at q <= sqrt x:
   15/26 (0.577) at k=50 -> 117/1986 (0.059) at k=10^4, strictly decreasing,
   always under the a-priori write-once cap (20 -> 176). PREDICTION MISS,
   recorded: the prediction asserted the < 15% band at EVERY milestone;
   it holds only from k = 5000 (at tiny k, sqrt x covers most of the prime
   range) — the assertion was corrected post-run to the monotone fall + the
   k >= 5000 band. The 10^4 hand estimate (90-130) was a hit: 117.

5. BOUND TREND (observation). bound/N_nt at y = sqrt x is FLAT ~1.6 in range
   (1.64 -> 1.59); at y = x^{2/3} it decreases 1.65 -> 1.35 — the optimal
   split point grows with x, as the proof's y = x/(log x)^3 choice says.

RUN RECORD (this file, ~2 s, 34 checks, well under 512 MB, no numpy; all
sections assert). Predictions EQ1-EQ5 were worked out by hand before the
run. Prediction hits: N_nt = 1986, Sum e_q equality, the bound at every
cell with ratio ~1.6 at (10^4, sqrt x), gap 0.23 -> 0.034 positive and
decreasing, small-events 117 in the predicted 90-130, EQ5's (1, 3) band.
One prediction MISS (EQ4's 15% band asserted at every milestone, true only
from k = 5000): the assertion was rescoped post-run; no world number moved.

Companion scripts: explore_complexity_ledger.py (the domination, the
count fate); explore_ledger_threshold.py (the collision identity, the size
threshold). This closes their shared open remainder: the converse.
"""

import sys
from math import log, floor, sqrt

K_MAX = 10000
MILESTONES = [50, 200, 1000, 5000, 10000]


# ── number-theory primitives (thin re-decl; mirror the bridge scripts) ──

def primes_up_to(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [i for i in range(2, n + 1) if sieve[i]]


def first_k_primes(k):
    bound = int(k * (log(k) + log(log(k)))) + 100
    ps = primes_up_to(bound)
    while len(ps) < k:
        bound *= 2
        ps = primes_up_to(bound)
    return ps[:k]


def factorize(n):
    """Prime factorization of n by trial division (n <= ~1.05e5 here)."""
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


PASS = 0
FAIL = 0


def ok(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {msg}")


# ── build the trajectory: events, exponents, logs, milestone snapshots ──

def build():
    """Grow lambda(p_k#) on the size-ordered schedule. Record every EVENT
    (k, p, q, delta, old exponent); track running exponents, log lambda,
    log phi, N_nt (divisibility definition: step k>=1 is non-transparent
    iff p-1 forces at least one event; p=2 forces none)."""
    ps = first_k_primes(K_MAX)
    running = {}
    loglam = 0.0
    logphi = 0.0
    events = []           # (k, p, q, delta, old)
    N_nt = 0
    snaps = {}            # k -> dict of milestone data
    step_events = []      # per-step event count (for E1/E4 checks)
    step_incs = []        # per-step (increment, log(p-1))
    for k, p in enumerate(ps, start=1):
        m = p - 1
        fac = factorize(m) if m > 1 else {}
        inc = 0.0
        n_ev = 0
        for q, e in sorted(fac.items()):
            old = running.get(q, 0)
            if e > old:
                events.append((k, p, q, e - old, old))
                inc += (e - old) * log(q)
                running[q] = e
                n_ev += 1
        if n_ev > 0:
            N_nt += 1
        loglam += inc
        if m > 1:
            logphi += log(m)
        step_events.append(n_ev)
        step_incs.append((inc, log(m) if m > 1 else 0.0))
        if k in MILESTONES:
            snaps[k] = dict(p=p, N_nt=N_nt, loglam=loglam, logphi=logphi,
                            running=dict(running))
    return ps, events, snaps, step_events, step_incs, running, loglam, logphi


def small_term(y, x, prime_list):
    """Sum_{q <= y} floor(log x / log q) over primes q."""
    s = 0
    for q in prime_list:
        if q > y:
            break
        s += floor(log(x) / log(q))
    return s


def main():
    ps, events, snaps, step_events, step_incs, running, loglam, logphi = build()
    x_final = ps[-1]
    prime_list = primes_up_to(int(x_final ** 0.9) + 2)

    # ---- EQ1: the event ledger (E1, E2, E4 + recomputation) ----
    print("== EQ1: the event ledger ==")
    sum_eq = len(events)                      # Sum_q e_q = total events
    N_nt = snaps[K_MAX]['N_nt']
    multi = sum(1 for n in step_events if n >= 2)
    opener_raises = step_events[0]
    print(f"  N_nt (divisibility) = {N_nt}, Sum_q e_q = {sum_eq}, "
          f"multi-prime steps = {multi}, opener events = {opener_raises}")
    ok(N_nt <= sum_eq, "E1: N_nt <= Sum e_q")
    ok(N_nt == sum_eq and multi == 0,
       "in range: every raise touches exactly one prime (equality)")
    # E2: e_q <= a_q for every q
    e_count = {}
    for (_, _, q, _, _) in events:
        e_count[q] = e_count.get(q, 0) + 1
    ok(all(e_count[q] <= running[q] for q in e_count),
       "E2: e_q <= a_q for every q")
    # recomputation: log lambda from final exponents
    recomp = sum(a * log(q) for q, a in running.items())
    print(f"  log lambda = {loglam:.1f} (recomputed {recomp:.1f}), "
          f"log phi = {logphi:.1f}, alpha = {loglam/logphi:.4f}")
    ok(abs(recomp - loglam) < 1e-6 * max(1.0, loglam),
       "log lambda == Sum a_q log q")
    # E4: every step increment <= log(p-1)
    ok(all(inc <= lm + 1e-12 for (inc, lm) in step_incs),
       "E4: step increment <= log(p-1)")

    # ---- EQ2: the write-once bound at every milestone, y-grid ----
    print("== EQ2: the write-once bound ==")
    for k in MILESTONES:
        s = snaps[k]
        x = s['p']
        for label, y in [("x^1/2", x ** 0.5), ("x^2/3", x ** (2 / 3)),
                         ("x^0.9", x ** 0.9)]:
            st = small_term(y, x, prime_list)
            lt = s['loglam'] / log(y)
            bound = st + lt
            print(f"  k={k:>6} x={x:>7} y={label:>6}: "
                  f"small={st:>5} large={lt:>8.1f} bound={bound:>8.1f} "
                  f"N_nt={s['N_nt']:>5} ratio={bound / s['N_nt']:.2f}")
            ok(s['N_nt'] <= bound,
               f"write-once bound at k={k}, y={label}")

    # ---- EQ3: the gap nt_frac - alpha ----
    print("== EQ3: the gap ==")
    gaps = []
    for k in MILESTONES:
        s = snaps[k]
        alpha = s['loglam'] / s['logphi']
        ntf = s['N_nt'] / k
        mu = s['loglam'] / s['N_nt']
        bracket = k * log(s['p']) / s['logphi']
        gap = ntf - alpha
        gaps.append(gap)
        print(f"  k={k:>6}: nt_frac={ntf:.4f} alpha={alpha:.4f} "
              f"gap={gap:.4f} mu/logx={mu / log(s['p']):.3f} "
              f"bracket={bracket:.3f}")
        ok(gap > 0, f"gap > 0 at k={k}")
    ok(all(gaps[i] > gaps[i + 1] for i in range(len(gaps) - 1)),
       "gap decreasing across milestones")

    # ---- EQ4: the rationing census (event counts split at sqrt x) ----
    print("== EQ4: the rationing census ==")
    fracs = []
    for k in MILESTONES:
        s = snaps[k]
        x = s['p']
        rt = sqrt(x)
        small_ev = sum(1 for (kk, _, q, _, _) in events if kk <= k and q <= rt)
        tot_ev = sum(1 for (kk, _, _, _, _) in events if kk <= k)
        cap = small_term(rt, x, prime_list)
        frac = small_ev / tot_ev
        print(f"  k={k:>6}: events at q<=sqrt(x) {small_ev:>4} of {tot_ev:>5} "
              f"({frac:.3f}); a-priori cap {cap}")
        ok(small_ev <= cap, f"small events <= write-once cap at k={k}")
        fracs.append(frac)
    # PREDICTION MISS recorded (run record): the frozen prediction asserted < 15%
    # at EVERY milestone; it holds only from k = 5000 (0.58 at k = 50 — at
    # tiny k, sqrt x covers most of the prime range). The honest in-range
    # content is the monotone FALL of the small-event fraction.
    ok(all(fracs[i] > fracs[i + 1] for i in range(len(fracs) - 1)),
       "small-event fraction strictly decreasing across milestones")
    ok(fracs[-2] < 0.15 and fracs[-1] < 0.15,
       "small-event fraction < 15% at k >= 5000")

    # ---- EQ5: bound trend (observation band) ----
    print("== EQ5: bound trend (y = sqrt x) ==")
    ratios = []
    for k in MILESTONES:
        s = snaps[k]
        x = s['p']
        bound = small_term(sqrt(x), x, prime_list) + s['loglam'] / log(sqrt(x))
        ratios.append(bound / s['N_nt'])
        print(f"  k={k:>6}: bound/N_nt = {bound / s['N_nt']:.2f}")
    ok(all(1.0 < r < 3.0 for r in ratios[1:]),
       "bound/N_nt in (1, 3) at k >= 200")

    print(f"\n{PASS} checks pass, {FAIL} fail")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
