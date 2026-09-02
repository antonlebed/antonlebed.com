"""THE EXACTNESS BRIDGE — does computational mechanics' apparatus SEE
the clock condensation at beta_col?

THE QUESTION. The exactness-bridge conjecture: computational
irreducibility (complexity-of-history) acquires exact critical
temperatures through these growth worlds. The incumbent is
computational mechanics: epsilon-machines, statistical complexity C_mu,
excess entropy E, entropy rate h_mu (Crutchfield-Young; Shalizi-
Crutchfield cond-mat/9907176; CSSR cs/0406011). REFUTATION TEST (b): if
statistical complexity is blind to / unmoved by the clock condensation
at beta_col, the bridge does not connect. This script computes the
incumbent's full measure suite on the witness-gap object itself and
reads it against our ledger.

THE OBJECT. The depth-column growth world (THE SOLVABLE
GENESIS, explore_depth_observer.py): histories seed 1 -> 3^t are
exactly the subsets of intermediate levels {1..t-1}, and the route
posterior factorizes into INDEPENDENT level-visit coins
P(visit a) = q_a = 1/(1 + Z_a(beta)), q_a -> q_col = 1/(1 + Z_col(beta)).
The witness gap (our irreducibility object) is this process's entropy;
its ledger (explore_irreducibility_order.py): the rate r(beta) is
analytic with a smooth max at beta_col (root of Z_col = 1, 1.49595),
while the genesis MODE m(beta) = 1{Z_col < 1} JUMPS 0->1 there and the
onset depth a*(beta) diverges logarithmically.

THE INCUMBENT'S READING. Handed this process as a symbol sequence, the
epsilon-machine construction (predictive equivalence of pasts) applies
to the stationary tail: iid Bernoulli(q_col). CSSR's own convergence
theorem requires conditional stationarity + finitely many causal
states; the nonstationary full genesis violates it,
so the tail is the incumbent's home turf and gets the main test; the
full string gets a report-only side leg.

DESIGN (predictions fixed before this file existed; asserts adjudicate).
  S1 EXACT SUITE — the hand-derived epsilon-machine of the tail
     process and the incumbent measures as closed forms on the beta
     grid: C_mu, E, h_mu; smoothness of h_mu across beta_col vs the
     ledger's m(beta) jump.
  S2 MINI-CSSR — a Phase-II-faithful reconstruction (suffix histories
     L <= 4, chi-square split-on-reject at alpha = 0.01 with the
     restricted-alternative rejoin; Phase III determinization OMITTED —
     vacuous at the one reconstructed state, every transition from a
     single state is trivially deterministic) run
     on sampled tail strings at every grid beta: reconstructed state
     count and estimated C_mu vs beta. Plug-in excess-entropy estimate
     (4-block MI) rides along. Side leg: the full nonstationary
     genesis string at two betas, REPORT ONLY.
  S3 THE LEDGER, SAME DATA — exact m(beta) and onset depth a* on the
     grid; empirical deep-tail visit frequency from the SAME sampled
     strings crossing 1/2 at beta_col.
  S4 THE VERDICT TABLE — incumbent column vs ledger column, side by
     side, printed.

Lineage: Z_col/Z_level/bisect_root/binary_entropy are imported from
explore_irreducibility_order.py (the established machinery); the
route-posterior factorization is a verified law of the depth-column
growth world (explore_depth_observer.py S1, exact enumeration at t = 8),
re-grounded here by the S1 route-weight enumeration.

FINDINGS (post-run edit; run record at bottom).

F1 THE ONE-STATE SUITE (rule, proved given the depth-column growth
world's factorization law; verified S1). The route posterior rebuilt from the
ROUTE WEIGHTS (P(S) proportional to prod 1/Z_a; 256 histories
enumerated at t = 9) has level marginals equal to the coins to 1e-12
and a conditional next-symbol distribution PAST-INVARIANT (spreads
2.2e-16 / 1.1e-16 across all 8 / 128 pasts) and equal to the coin — so
the tail genesis process is iid Bernoulli(q_col), predictive
equivalence collapses every past into ONE causal state, and the
incumbent's entire measure suite is C_mu = 0 and E = 0 IDENTICALLY
with h_mu(beta) = h(q_col(beta)) ANALYTIC through beta_col — a smooth
maximum of exactly 1 bit at beta_col (symmetric gaps 4.3e-5 -> 6.8e-7
under halving, central slope 1e-4), while on the same grid the ledger's
Z_col crosses 1 (1.0330 / 0.9685 at beta_col -/+ 0.01): the mode
observable m(beta) jumps 0->1 where every incumbent observable is flat
or smooth.

F2 THE RECONSTRUCTION SEES NOTHING (observation; verified S2). A
Phase-II-faithful mini-CSSR (L <= 4, chi-square at alpha = 0.01,
restricted-alternative rejoin; Phase III omitted, vacuous at one
state; M = 4000 strings of 64 tail symbols)
reconstructs exactly ONE causal state and C_mu_hat = 0.0000 at every
grid beta INCLUDING beta_col — no splits, no alpha-flukes, no feature;
the 4-block plug-in E_hat sits at the estimator's own bias scale
(0.0047-0.0061 vs bias ~0.0051 bits). Side leg (report only): on the
FULL nonstationary genesis string — where CSSR's own convergence
hypotheses (conditional stationarity, finitely many causal states)
are violated — CSSR manufactures
spurious age-states (beta 1.30: 2 states, 0.47 bits; beta 1.55: 1
state): assumption-violation noise, not the transition.

F3 THE TRANSITION IS IN THE HANDED DATA (observation; verified S3).
The SAME sampled strings carry the mode reorganization: the deep-tail
visit frequency crosses 1/2 at the condensation clock to grid
resolution (0.4866 at beta 1.48, 0.5110 at 1.51; at the near-clock
point 1.4959 the exact coin is 0.499960 and the sample 0.5009, within
1 s.e.; every p_hat within 5 s.e. of its coin — the exact coin q_col
is what crosses at beta_col), and the exact ledger shows m = 0 below /
m = 1 above with onset depth a* growing 1 -> 3 as the clock gap falls
0.1 -> 0.001 (the logarithmic divergence, staircase-floored). The
apparatus was not starved — it was handed the transition and cannot
express it.

F4 THE VERDICT — THE REFUTATION TEST FIRES (adjudicated on
F1-F3 and the literature contact). The incumbent's forward suite (h_mu,
C_mu, E), its reconstruction (CSSR), and its retrodiction wing
(crypticity chi = C_mu(+/-) - E, arXiv:0905.3587 — contacted at
abstract level; stationary-only, exact given models, no
endpoint-conditioning) are all functionals of
the PROCESS LAW, and the growth world's flattened genesis law is a
smooth one-coin family: provably nothing in the formalism moves at
beta_col (nor under re-encoding: the move-gap reading of the same
history is iid geometric — memoryless again — so the blindness is not
an artifact of the binary alphabet). Our transition lives in the endpoint-conditioned route
posterior's MODE geometry (retrodiction loss), an object the
incumbent's stationary prediction-memory formalism does not carry.
The exactness bridge does not connect: the conjecture's headline
("complexity-of-history has exact critical temperatures" AS the field
measures complexity-of-history) fails at the attachment point. Test (a)
MISSED for the record: the incumbent owns exact measures GIVEN solved
models (transfer-matrix spin chains, spectral decomposition) and
inferred measures from data, but no critical temperature derived FROM
the complexity apparatus — where a T_c appears it is imported
(Onsager, Bethe; arXiv:1510.08954), and
complexity peaks are reported off-critical in the 2D-Ising literature
(excess entropy T ~ 2.42 vs T_c = 2.269 — contacted at search/abstract
level, not full text). Test (c) moot.

Run: `python explore_exactness_bridge.py` (pure python, no numpy;
trivial memory). RUN RECORD (44 checks pass, ~2 s, seed 200; two full
runs diffed byte-identical): beta_col = 1.49595; h_mu(bits) at
beta = 1.2 / 1.4959 / 1.8 = 0.750283 / 1.000000 / 0.887748; CSSR
states = 1 and C_mu_hat = 0.0000 at all ten betas; E_hat in
[0.0047, 0.0061] (bias 0.0051 at 32000 pairs); p_hat side of 1/2 =
-,-,-,-,-,+,+,+,+,+ across the grid; a*(beta_col + d),
d = 0.1/0.03/0.01/0.003/0.001 = 1/2/2/3/3.
"""

import sys, os, math, random
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_irreducibility_order import (  # lineage: established machinery
    Z_col, Z_level, binary_entropy, bisect_root,
)

CHECKS = 0

def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1

LOG2 = math.log(2.0)

def h_bits(p):
    """Binary entropy in BITS (the incumbent's convention)."""
    return binary_entropy(p) / LOG2

def q_col(beta):
    return 1.0 / (1.0 + Z_col(beta))

def q_level(a, beta):
    return 1.0 / (1.0 + Z_level(a, beta))

# The condensation clock (the ledger's critical temperature).
BETA_COL = bisect_root(lambda b: Z_col(b) - 1.0, 1.40, 1.60)

# The beta grid brackets the clock, densest around it.
BETAS = [1.20, 1.30, 1.40, 1.45, 1.48, round(BETA_COL, 4), 1.51, 1.55,
         1.65, 1.80]

# ------------------------------------------------------------------ S1
def s1():
    print("S1 THE EXACT SUITE (the incumbent's measures, closed form)")
    # The one-causal-state lemma, grounded OUTSIDE the coin form: the
    # route posterior is rebuilt from the ROUTE WEIGHTS (the
    # depth-column growth world's wall-priced normalizer: P(S) proportional to
    # prod_{a in S} 1/Z_a over the visited intermediate states),
    # enumerated over all 2^(t-1) histories at t = 9, and checked for
    # (i) level marginals = the coins q_a = 1/(1+Z_a) and (ii) the
    # conditional next-symbol distribution past-INVARIANT and equal to
    # the coin, across every past. A wrong coin formula or a broken
    # factorization fails here; the product form never enters.
    beta = 1.45
    t = 9
    zs = [Z_level(a, beta) for a in range(1, t)]
    weights = {}
    for S in range(1 << (t - 1)):
        w = 1.0
        for a in range(t - 1):
            if (S >> a) & 1:
                w *= 1.0 / zs[a]
        weights[S] = w
    tot = sum(weights.values())
    for a in range(t - 1):
        marg = sum(w for S, w in weights.items() if (S >> a) & 1) / tot
        ok(abs(marg - 1.0 / (1.0 + zs[a])) < 1e-12,
           "route-weight marginal != coin at level %d" % (a + 1))
    spreads = []
    for pos in (3, 7):          # bit pos = level pos+1; pasts = bits < pos
        conds = []
        for past in range(1 << pos):
            num = den = 0.0
            for S, w in weights.items():
                if (S & ((1 << pos) - 1)) == past:
                    den += w
                    if (S >> pos) & 1:
                        num += w
            conds.append(num / den)
        spread = max(conds) - min(conds)
        spreads.append(spread)
        ok(spread < 1e-12,
           "one-state lemma: conditional next-dist varies across pasts")
        ok(abs(conds[0] - 1.0 / (1.0 + zs[pos])) < 1e-12,
           "conditional != coin at level %d" % (pos + 1))
    print("  one causal state (route-weight enumeration, t = 9, 256 "
          "histories): marginals = coins to 1e-12 (8 levels); conditional "
          "P(next|past) past-invariant, spreads %.1e / %.1e over 8 / 128 "
          "pasts, equal to the coin" % (spreads[0], spreads[1]))

    # The suite on the grid. C_mu and E are identically 0 for the
    # one-state machine; h_mu = h(q_col) in bits.
    print("  beta      h_mu(bits)  C_mu  E   | Z_col")
    for b in BETAS:
        z = Z_col(b)
        print("  %-8.4f  %-10.6f  0     0   | %.6f" % (b, h_bits(q_col(b)), z))

    # Smoothness of h_mu across beta_col vs the ledger jump: the
    # symmetric gap |h(beta_col+d) - h(beta_col-d)| must vanish with d
    # (continuity), and the central first difference must -> 0 (the
    # smooth max), while Z_col - 1 changes sign across the same point.
    gaps, slopes = [], []
    for d in (0.02, 0.01, 0.005):
        hi, lo = h_bits(q_col(BETA_COL + d)), h_bits(q_col(BETA_COL - d))
        gaps.append(abs(hi - lo))
        slopes.append((hi - lo) / (2 * d))
    ok(gaps[0] > gaps[1] > gaps[2], "h_mu gap not shrinking")
    ok(abs(slopes[2]) < 0.02, "h_mu central slope at beta_col not ~0")
    ok(h_bits(q_col(BETA_COL)) > 0.999999, "h_mu(beta_col) != 1 bit")
    ok(Z_col(BETA_COL - 0.01) > 1.0 > Z_col(BETA_COL + 0.01),
       "ledger jump: Z_col does not cross 1 at beta_col")
    print("  h_mu across beta_col: gaps %.2e -> %.2e -> %.2e (continuous), "
          "central slope %.4f (smooth max at 1 bit)" %
          (gaps[0], gaps[1], gaps[2], slopes[2]))
    print("  ledger: Z_col(beta_col -/+ 0.01) = %.4f / %.4f -> m jumps 0->1"
          % (Z_col(BETA_COL - 0.01), Z_col(BETA_COL + 0.01)))

# ------------------------------------------------------------------ S2
NSTR = 4000    # strings per beta
SLEN = 64      # tail symbols per string
LMAX = 4
CHI2_CRIT_1DF = 6.635   # alpha = 0.01
MIN_COUNT = 25

def sample_tail(beta, rng):
    """NSTR iid-Bernoulli(q_col) strings (the stationary tail)."""
    q = q_col(beta)
    return [[1 if rng.random() < q else 0 for _ in range(SLEN)]
            for _ in range(NSTR)]

def sample_genesis(beta, rng, t=49):
    """Full nonstationary genesis strings: coins q_1..q_{t-1}."""
    qs = [q_level(a, beta) for a in range(1, t)]
    return [[1 if rng.random() < q else 0 for q in qs]
            for _ in range(NSTR)]

def suffix_counts(strings):
    """next-symbol counts for every past-suffix up to LMAX."""
    counts = defaultdict(lambda: [0, 0])
    for s in strings:
        n = len(s)
        for i in range(n):
            lim = min(LMAX, i)
            for L in range(lim + 1):
                counts[tuple(s[i - L:i])][s[i]] += 1
    return counts

def chi2_gof(child, pooled):
    """Chi-square of child counts against the pooled state distribution."""
    n = child[0] + child[1]
    tot = pooled[0] + pooled[1]
    stat = 0.0
    for x in (0, 1):
        p = pooled[x] / tot if tot else 0.5
        e = n * p
        if e < 1e-12:
            if child[x] > 0:
                return float("inf")
            continue
        stat += (child[x] - e) ** 2 / e
    return stat

def mini_cssr(strings):
    """CSSR Phase II (split-on-reject, restricted-alternative rejoin);
    Phase III omitted (vacuous at one state). Returns (n_states,
    C_mu_hat)."""
    counts = suffix_counts(strings)
    states = [{()}]

    def pooled(state):
        acc = [0, 0]
        for suf in state:
            c = counts.get(suf, (0, 0))
            acc[0] += c[0]; acc[1] += c[1]
        return acc

    for L in range(1, LMAX + 1):
        children = sorted(suf for suf in counts
                          if len(suf) == L and sum(counts[suf]) >= MIN_COUNT)
        for suf in children:
            parent_state = next((st for st in states if suf[1:] in st), None)
            if parent_state is None:
                continue
            if chi2_gof(counts[suf], pooled(parent_state)) < CHI2_CRIT_1DF:
                parent_state.add(suf)
                continue
            for st in states:            # restricted alternative
                if st is parent_state:
                    continue
                if chi2_gof(counts[suf], pooled(st)) < CHI2_CRIT_1DF:
                    st.add(suf)
                    break
            else:
                states.append({suf})

    # stationary weights from LMAX-suffix frequencies: each observed
    # LMAX-suffix belongs to the state holding its LONGEST assigned
    # suffix (the suffix-machine semantics).
    def state_of(suf):
        for L in range(len(suf), -1, -1):
            probe = suf[len(suf) - L:]
            for k, st in enumerate(states):
                if probe in st:
                    return k
        return None

    weights = defaultdict(float)
    total = 0.0
    for suf, c in counts.items():
        if len(suf) == LMAX:
            k = state_of(suf)
            if k is not None:
                n = c[0] + c[1]
                total += n
                weights[k] += n
    cmu = 0.0
    for k, w in weights.items():
        if w > 0:
            p = w / total
            cmu -= p * math.log(p, 2)
    n_live = sum(1 for w in weights.values() if w > 0)
    return max(n_live, 1), cmu

def block_mi(strings, blk=4, stride=8):
    """Plug-in MI (bits) between adjacent blk-blocks: the E estimate."""
    joint = defaultdict(int)
    n = 0
    for s in strings:
        for i in range(blk, len(s) - blk + 1, stride):
            x = tuple(s[i - blk:i]); y = tuple(s[i:i + blk])
            joint[(x, y)] += 1
            n += 1
    px, py = defaultdict(int), defaultdict(int)
    for (x, y), c in joint.items():
        px[x] += c; py[y] += c
    mi = 0.0
    for (x, y), c in joint.items():
        mi += (c / n) * math.log((c * n) / (px[x] * py[y]), 2)
    return mi, n

def s2():
    print("S2 MINI-CSSR ON SAMPLED TAIL STRINGS "
          "(M = %d, len %d, L <= %d, alpha = 0.01)" % (NSTR, SLEN, LMAX))
    rng = random.Random(200)
    results = []
    print("  beta      states  C_mu_hat  E_hat(4-blk)")
    for b in BETAS:
        strings = sample_tail(b, rng)
        ns, cmu = mini_cssr(strings)
        e_hat, npairs = block_mi(strings)
        results.append((b, ns, cmu, e_hat))
        print("  %-8.4f  %-6d  %-8.4f  %.4f" % (b, ns, cmu, e_hat))
    bias = 225.0 / (2 * npairs * math.log(2))
    print("  (plug-in MI bias scale ~ %.4f bits at %d pairs)" % (bias, npairs))

    states_list = sorted(r[1] for r in results)
    ok(states_list[len(states_list) // 2] == 1,
       "median reconstructed state count != 1")
    ok(max(r[2] for r in results) <= 0.05, "C_mu_hat exceeds 0.05 bits")
    ok(max(r[3] for r in results) <= 0.02, "E_hat exceeds 0.02 bits")
    at_col = [r for r in results if abs(r[0] - BETA_COL) < 5e-3][0]
    med_cmu = sorted(r[2] for r in results)[len(results) // 2]
    ok(at_col[2] - med_cmu <= 0.02,
       "C_mu_hat carries a spike at beta_col")
    print("  -> no reconstructed structure, no feature at beta_col")

    print("  side leg (REPORT ONLY): full nonstationary genesis strings")
    for b in (1.30, 1.55):
        strings = sample_genesis(b, rng)
        ns, cmu = mini_cssr(strings)
        print("    beta %.2f: states %d, C_mu_hat %.4f "
              "(CSSR assumptions violated: nonstationary)" % (b, ns, cmu))
    return results

# ------------------------------------------------------------------ S3
def onset_depth(beta, amax=400):
    """a*(beta) = shallowest a with Z_a < 1 (the mode onset), beta > beta_col."""
    for a in range(1, amax + 1):
        if Z_level(a, beta) < 1.0:
            return a
    return None

def s3():
    print("S3 THE LEDGER, SAME DATA")
    # exact: the mode jump and the onset-depth divergence
    ds = (0.1, 0.03, 0.01, 0.003, 0.001)
    onsets = [onset_depth(BETA_COL + d) for d in ds]
    ok(all(o is not None for o in onsets), "onset depth not found")
    ok(all(onsets[i] <= onsets[i + 1] for i in range(len(onsets) - 1))
       and onsets[-1] > onsets[0],
       "onset depth a* not growing as beta -> beta_col+")
    print("  a*(beta_col + d) for d = %s: %s (divergence as d -> 0)"
          % (list(ds), onsets))
    for b in (1.30, 1.45):
        ok(onset_depth(b) is None, "mode suffix nonempty below beta_col")
    print("  m(beta) = 0 below beta_col (no a with Z_a < 1 at 1.30, 1.45)")

    # empirical: the SAME sampled strings' deep-tail visit frequency
    rng = random.Random(200)   # same seed -> same strings as S2
    print("  beta      q_col(exact)  p_hat(sampled)  side of 1/2")
    for b in BETAS:
        strings = sample_tail(b, rng)
        tot = sum(sum(s) for s in strings)
        n = NSTR * SLEN
        p_hat = tot / n
        se = math.sqrt(0.25 / n)
        q = q_col(b)
        side = "+" if p_hat > 0.5 else "-"
        print("  %-8.4f  %-12.6f  %-14.6f  %s" % (b, q, p_hat, side))
        ok(abs(p_hat - q) < 5 * se, "sampled visit rate off its coin")
        if b < BETA_COL - 5e-3:
            ok(p_hat < 0.5, "visit rate above 1/2 below beta_col")
        if b > BETA_COL + 5e-3:
            ok(p_hat > 0.5, "visit rate below 1/2 above beta_col")
    print("  -> the mode reorganization IS in the handed data: the visit "
          "frequency crosses 1/2 at beta_col (grid resolution; the exact "
          "coin q_col crosses there)")

# ------------------------------------------------------------------ S4
def s4(cssr_results):
    print("S4 THE VERDICT TABLE (incumbent vs ledger)")
    print("  beta      | h_mu    C_mu  E     states  C_mu_hat | m   a*")
    for (b, ns, cmu, _e) in cssr_results:
        z = Z_col(b)
        m = 1 if z < 1.0 else 0
        a_star = onset_depth(b) if m else None
        print("  %-8.4f  | %.4f  0     0     %-6d  %-7.4f  | %d   %s"
              % (b, h_bits(q_col(b)), ns, cmu, m,
                 a_star if a_star is not None else "-"))

def main():
    print("THE EXACTNESS BRIDGE — computational mechanics vs the ledger")
    print("beta_col = %.5f (root of Z_col = 1)" % BETA_COL)
    ok(abs(BETA_COL - 1.49595) < 5e-4, "beta_col off the established record")
    s1()
    results = s2()
    s3()
    s4(results)
    print("ALL CHECKS PASS (%d)" % CHECKS)

if __name__ == "__main__":
    main()
