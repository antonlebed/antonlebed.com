"""
Exact residue decomposition vs approximate inference: the coupling test.

QUESTION. The Chinese Remainder Theorem splits Z/N (N = product of the first k
primes) into independent residue channels Z/p_i that share no information --
arithmetic is carry-free, each channel blind to the others. A probability
distribution that FACTORS over these channels can therefore be handled
channel-by-channel, exactly and cheaply (cost ~ sum of the p_i). Does this exact
channel decomposition ever BEAT approximate inference (mean field) on a task
where approximation is known to struggle -- and if it does, is the win specific
to the residue structure, or is it just "use exact arithmetic," which any exact
computer performs at table stakes?

The known frontier for exact inference in graphical models: variable
elimination / the junction tree solve it exactly in polynomial time WHEN the
treewidth is bounded (and bounded treewidth is necessary for tractable exact
inference modulo standard complexity assumptions); in general the marginal sum
is #P-hard, which is why mean-field / MCMC approximations are used at all, and
why they are worst (severely miscalibrated) on high-treewidth, frustrated,
strongly-coupled systems. The residue channels are the ZERO-coupling extreme. This script asks
what happens as coupling is dialed up.

SETUP. Over the k channel variables r_i = x mod p_i (x in Z/N) build a pairwise
Markov random field with a coupling strength gamma >= 0:

    P_gamma(x)  proportional to  prod_i f_i(r_i) * prod_{i<j} exp(gamma * h_ij(r_i, r_j)).

At gamma = 0 the distribution factors over channels exactly; gamma > 0 couples
them pairwise. A fixed battery of instances (deterministic single-channel
potentials f_i and pairwise potentials h_ij) is swept over a fixed gamma grid.
Three methods per (instance, gamma):

  TRUE      -- brute force over all N states: exact MAP (argmax) and exact
               per-channel marginals. Cost N = prod p_i.
  CHANNEL   -- the cheap residue-native method: each channel picks argmax_r
               f_i(r) from its OWN potential alone, blind to every coupling term
               (channels share no information). Cost ~ sum of p_i.
  MEANFIELD -- standard mean-field variational fixed point q(x) = prod_i q_i(r_i),
               coordinate ascent from the uniform start (approximate).

Reported per gamma, aggregated over the battery: mean mean-field divergence
KL(q || P_gamma); the fraction of instances whose CHANNEL MAP tuple differs from
the TRUE MAP tuple; the fraction whose MEANFIELD MAP tuple differs from TRUE. A
residue-specific exactness win would appear as a coupling window where the cheap
CHANNEL method stays exact while MEANFIELD has already gone bad.

PREDICTIONS (fixed before the run).
  F1. gamma = 0: mean-field KL(q||P) = 0 (to numerical tolerance) and the CHANNEL
      MAP equals the TRUE MAP on every instance -- on a factored problem the exact
      channel decomposition has NO edge, because mean field is exact there too.
  F2. Mean-field KL is monotone non-decreasing across the gamma grid (approximation
      degrades as coupling grows). [The monotone form is the optimistic clause;
      the run may refine it to "rises from 0, not strictly monotone."]
  F3. The smallest gamma at which the CHANNEL method first errs is <= the smallest
      gamma at which MEANFIELD first errs: there is NO coupling window where
      approximation is bad yet the cheap exact channel method is still right. The
      cheap-and-exact route breaks no later than approximation does.
  F4. At the largest gamma the CHANNEL error fraction is > 0 (cheap != exact), so
      the only method exact under coupling is TRUE (brute), whose cost is
      N = prod p_i, exponential in k. The residue decomposition buys NO speedup
      once the problem is coupled: exact-under-coupling is generic brute force,
      not a residue-specific advantage.

The intended reading: a residue/CRT decomposition is exact-and-cheap exactly on
factored problems, which are exactly the problems where approximation is ALSO
exact -- so the exactness edge and the approximation-hardness are anti-correlated,
and no task lets the residue structure be both load-bearing and beat approximation.

FINDINGS (observation; one deterministic MRF family, k=3, N=105, 6 instances,
5-point gamma grid; 10 checks). All four predictions confirmed on the first run.
  - gamma = 0 (factored): mean-field KL = 1.3e-17 and the CHANNEL MAP equals the
    TRUE MAP on every instance; the exact per-channel marginals equal the
    mean-field marginals. On a factored problem the exact residue decomposition
    has NO edge -- approximation is exact there too (F1).
  - As coupling rises the cheap coupling-blind CHANNEL method and mean field FIRST
    err at the SAME gamma = 0.25 (F3): there is no coupling window where
    approximation is bad yet the cheap exact channel method is still right.
  - Beyond that the two diverge in the direction that SHARPENS the point, not one
    that rescues the residue method: at strong coupling (gamma = 2) the CHANNEL
    error climbs to 0.833 while mean field's MAP RECOVERS to 0 error (mode-seeking
    -- a sharply peaked coupled distribution is easy to locate the mode of), even
    as its marginal KL keeps rising to 0.18 (F2, monotone here). Strong coupling
    is easy for approximation and hard for the coupling-blind residue split.
  - Exactness under coupling therefore requires brute force over all N = prod(p_i)
    states (F4), or more generally junction-tree cost exponential in treewidth --
    generic exact computation, table stakes, with NO residue-specific speedup.
The residue decomposition is exact-and-cheap exactly on the factored problems
where approximation already succeeds; its exactness edge is anti-correlated with
the approximation-hardness that would make an edge worth having. This is the
third measured instance (after exact-vs-approximate vector binding, and the
walled ring-native learning rule) supporting a single CONJECTURE (a pattern
across three instances plus a mechanism, not a proof): an exact algebraic
substrate that deletes the archimedean place wins over approximation only on axes
with no concentration-of-measure rescue, and on exactly those axes the winning
computation is generic exact arithmetic that any exact computer performs at table
stakes -- so the substrate's own structure is conjectured never to become both
load-bearing and scale-decisive.

RUN RECORD: 10 checks passed; wall 0.3 s, peak working set 11.3 MB
(memwatch, 512 MB limit).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import math
from itertools import combinations

PRIMES = [3, 5, 7]              # k = 3 channels, N = 105
N = 1
for p in PRIMES:
    N *= p
K = len(PRIMES)
PAIRS = list(combinations(range(K), 2))
GAMMAS = [0.0, 0.25, 0.5, 1.0, 2.0]
INSTANCES = list(range(6))     # fixed deterministic battery
TOL = 1e-9


def single_pot(inst, i, r):
    """Deterministic single-channel log-potential theta_i(r), with a tiny
    deterministic tie-break so every channel has a unique argmax."""
    base = ((inst * 7 + i * 3 + r * r) % 5) - 2      # integer in [-2, 2]
    return base + 1e-6 * r


def pair_pot(inst, i, j, a, b):
    """Deterministic pairwise log-potential h_ij(a, b), integer in [-1, 1]."""
    return ((inst * 3 + i + j + a * b) % 3) - 1


def residues(x):
    return tuple(x % p for p in PRIMES)


def log_unnorm(inst, gamma, x):
    r = residues(x)
    s = 0.0
    for i in range(K):
        s += single_pot(inst, i, r[i])
    for (i, j) in PAIRS:
        s += gamma * pair_pot(inst, i, j, r[i], r[j])
    return s


def true_distribution(inst, gamma):
    """Exact normalized P_gamma over all N states (brute)."""
    logs = [log_unnorm(inst, gamma, x) for x in range(N)]
    m = max(logs)
    ws = [math.exp(l - m) for l in logs]
    z = sum(ws)
    return [w / z for w in ws]


def true_map_tuple(inst, gamma):
    logs = [log_unnorm(inst, gamma, x) for x in range(N)]
    best = max(range(N), key=lambda x: logs[x])
    return residues(best)


def true_channel_marginals(inst, gamma):
    P = true_distribution(inst, gamma)
    marg = [[0.0] * p for p in PRIMES]
    for x in range(N):
        r = residues(x)
        for i in range(K):
            marg[i][r[i]] += P[x]
    return marg


def channel_map_tuple(inst):
    """Residue-native MAP: per-channel argmax of the single-channel potential
    alone, coupling-blind. gamma-independent by construction."""
    out = []
    for i in range(K):
        p = PRIMES[i]
        out.append(max(range(p), key=lambda r: single_pot(inst, i, r)))
    return tuple(out)


def mean_field(inst, gamma, iters=200):
    """Coordinate-ascent mean field. Returns factored marginals q_i."""
    q = [[1.0 / p] * p for p in PRIMES]
    for _ in range(iters):
        newq = []
        for i in range(K):
            p = PRIMES[i]
            logq = [single_pot(inst, i, r) for r in range(p)]
            for (a, b) in PAIRS:
                if a == i:
                    oi = b
                elif b == i:
                    oi = a
                else:
                    continue
                for r in range(p):
                    exp_h = 0.0
                    for s in range(PRIMES[oi]):
                        hh = (pair_pot(inst, i, oi, r, s) if a == i
                              else pair_pot(inst, oi, i, s, r))
                        exp_h += q[oi][s] * hh
                    logq[r] += gamma * exp_h
            m = max(logq)
            ws = [math.exp(v - m) for v in logq]
            z = sum(ws)
            newq.append([w / z for w in ws])
        q = newq
    return q


def mf_kl(inst, gamma, q):
    """KL(q || P_gamma) with q(x) = prod_i q_i(r_i(x))."""
    P = true_distribution(inst, gamma)
    kl = 0.0
    for x in range(N):
        r = residues(x)
        qx = 1.0
        for i in range(K):
            qx *= q[i][r[i]]
        if qx > 0.0:
            kl += qx * (math.log(qx) - math.log(P[x]))
    return kl


def mf_map_tuple(q):
    return tuple(max(range(len(qi)), key=lambda r: qi[r]) for qi in q)


def run():
    checks = 0
    print(f"primes={PRIMES}  N={N}  pairs={PAIRS}  instances={len(INSTANCES)}")
    print(f"{'gamma':>6} | {'mean MF KL':>12} | {'CHANNEL err':>11} | {'MF err':>7}")

    kl_by_gamma = []
    chan_err_by_gamma = []
    mf_err_by_gamma = []
    for gamma in GAMMAS:
        kls, chan_errs, mf_errs = [], 0, 0
        for inst in INSTANCES:
            tmap = true_map_tuple(inst, gamma)
            cmap = channel_map_tuple(inst)
            q = mean_field(inst, gamma)
            kls.append(mf_kl(inst, gamma, q))
            if cmap != tmap:
                chan_errs += 1
            if mf_map_tuple(q) != tmap:
                mf_errs += 1
        mean_kl = sum(kls) / len(kls)
        chan_frac = chan_errs / len(INSTANCES)
        mf_frac = mf_errs / len(INSTANCES)
        kl_by_gamma.append(mean_kl)
        chan_err_by_gamma.append(chan_frac)
        mf_err_by_gamma.append(mf_frac)
        print(f"{gamma:>6.2f} | {mean_kl:>12.6f} | {chan_frac:>11.3f} | {mf_frac:>7.3f}")

    def first_error_gamma(fracs):
        for g, f in zip(GAMMAS, fracs):
            if f > 0.0:
                return g
        return math.inf

    chan_first = first_error_gamma(chan_err_by_gamma)
    mf_first = first_error_gamma(mf_err_by_gamma)

    # Consistency of the exact channel marginals at gamma = 0 (factored control).
    for inst in INSTANCES:
        marg0 = true_channel_marginals(inst, 0.0)
        q0 = mean_field(inst, 0.0)
        for i in range(K):
            for r in range(PRIMES[i]):
                assert abs(marg0[i][r] - q0[i][r]) < 1e-6
        checks += 1
    print(f"[ok] gamma=0 factored control: true marginals == mean-field ({checks} instances)")

    # F1: gamma = 0 has no residue edge.
    assert kl_by_gamma[0] < TOL, kl_by_gamma[0]
    assert chan_err_by_gamma[0] == 0.0
    checks += 1
    print(f"[ok] F1: gamma=0  MF KL={kl_by_gamma[0]:.2e} < tol, CHANNEL err=0 -- no edge on factored")

    # F2: KL rises from 0; report whether strictly monotone.
    assert kl_by_gamma[-1] > kl_by_gamma[0]
    monotone = all(kl_by_gamma[t + 1] >= kl_by_gamma[t] - 1e-12
                   for t in range(len(GAMMAS) - 1))
    checks += 1
    print(f"[ok] F2: MF KL rises 0 -> {kl_by_gamma[-1]:.4f}; monotone across grid = {monotone}")

    # F3: no window with (MF bad, CHANNEL exact) -- CHANNEL breaks no later than MF.
    assert chan_first <= mf_first, (chan_first, mf_first)
    checks += 1
    print(f"[ok] F3: first CHANNEL error at gamma={chan_first}, first MF error at gamma={mf_first} "
          f"-- CHANNEL breaks no later than MF")

    # F4: cheap != exact under coupling => exact route is brute over N.
    assert chan_err_by_gamma[-1] > 0.0
    checks += 1
    print(f"[ok] F4: at gamma={GAMMAS[-1]} CHANNEL err={chan_err_by_gamma[-1]:.3f} > 0 "
          f"-- exact-under-coupling needs brute over N={N}=prod(p_i), no residue speedup")

    print(f"\n{checks} checks passed.")
    return checks


if __name__ == "__main__":
    run()
