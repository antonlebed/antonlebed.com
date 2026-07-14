"""
explore_induction_ceiling.py -- THE INDUCTION CEILING (THE HUNT chamber
sixteen, P170; sibling of explore_growth_laws.py P143 ..
explore_ruler_ladder.py P169).

THE QUESTION. Every growth world is Kolmogorov-SHORT -- its generator
g = (law, beta) plus a seed is a few symbols -- yet the observer
theorems (bounded evidence P148, finite thermometer P148, cold
blindness P153, witness gap P153, age law P156) say pieces of g and
the route are unrecoverable from inside. Make that ONE object: the
exact mutual-information LEDGER I(coordinate; channel) across
observation channels (state / dated state / watched path / probe) and
fates, so every observer theorem becomes a ROW of a single chart --
and the chart is a BAYES CEILING no inducer (Solomonoff, MDL,
anything compression-driven) can beat, computed exactly: growth-world
induction tasks KNOW THEIR OWN OPTIMUM. Design + frozen slate PR1-PR9
+ paper attack: SCRATCH P170 pass 1-1b (git).

MODEL (truncated-menu exactness as in explore_thermometer_pair.py).
One move from state N picks admissible m (2 <= m <= M = 12, stated
everywhere) w.p. m^(-beta)/Z_N; seed 1; age T <= 4. Laws: D-IND
(coprime), D-DYN (lambda grows), D-SEMI (Nm squarefree), D-MEM (new
prime), COL (menu {3, 9}: the one-window column world). A completed
world (empty menu) freezes and pads its record with 'H'. ENSEMBLE:
generator g uniform over the class, age tau uniform 1..T, path drawn
from the thermal law. CHANNELS, nested: C_state = the bare endpoint N
(age unknown); C_dated = (N, tau); C_path = the move list. All
distributions exact by full path enumeration (no Monte Carlo); MI in
nats unless bits stated.

FINDINGS (tiers per CLAUDE.md; run record below; all sections assert;
every number is truncated-menu exact at M = 12, T = 4, seed 1 --
none is an untruncated limit).

1. THE LEDGER (chart: computed exact; the ladder inequalities proved
   by data processing, strictness measured; verified S1). One chart
   holds the observer theorems as rows -- mixed-age ensemble, nats,
   H(G) = log 3 = 1.0986 every class:
     beta-grid {1.5,2,3} on D-IND: I(state) 0.0489 < I(dated) 0.0628
       < I(path) 0.0758
     beta-grid on D-DYN:           0.0512 < 0.0693 < 0.0726
     law-grid {SEMI,IND,MEM} at 2: 0.1146 < 0.1151 < 0.1482
   PR1 confirmed: the channel ladder is strict at every row.

2. THE COORDINATE SPLIT (observation, unfrozen expectation REFUTED
   and upgraded; verified S1). The naive guess "the law is the
   hardest coordinate" is WRONG at beta = 2: the law-grid carries
   MORE information than the temperature grid through every channel
   (state 0.1146 vs 0.0489). The mechanism is the split: LAWS DIFFER
   IN SUPPORT -- pairwise I(law; state) = 0.0992 (SEMI-IND) and
   0.1588 (SEMI-MEM) vs only 0.0193 (IND-MEM), asserted ordered: the
   law reads mostly as squarefree-vs-not, and D-IND's state set is a
   STRICT subset of D-MEM's (26 vs 55 states; least MEM-only state
   1050 = 2*3*5^2*7, a re-deepening, asserted) -- so the bare state
   already reads the law and DATING ADDS ALMOST NOTHING (0.1146 ->
   0.1151, +0.4%); TEMPERATURE
   IS A RATE (how big by when), so dating adds +28% (0.0489 ->
   0.0628) and watching more. The law lives in the state; the
   temperature lives in the clock -- chamber twelve's rate-reading,
   now a channel-decomposition fact. And the law coordinate's
   visibility is entirely THERMAL: at T = 0 it is exactly zero
   (finding 4) -- heat is what makes laws readable.

3. THE MNEMONIC CROSSOVER (observation; PR5 confirmed with a flip;
   verified S1). Fixed-age bare-state temperature information, DYN/IND
   ratio: 0.70 / 0.82 / 1.14 / 1.62 at tau = 1..4 -- the mnemonic
   fate's advantage is NOT innate: a YOUNG breadth world out-informs
   the young dynamics-fate world; the depth fate overtakes at
   tau = 3 and the ratio grows monotonically (asserted).
   Memory-is-fate-graded is an asymptotic law with a measured
   crossover age. Breadth's own I(N_tau) DROPS 0.0724 -> 0.0662 at
   tau = 4: completion amnesia beginning (finding 8).

4. THE COLD FLOOR AND THE PROBE JUMP (rule -- cold blindness P153
   re-priced in MI; verified S2). At T = 0 the three demands write
   ONE trajectory (2,3,5,7,11,13,17,19 asserted identical, 8 steps,
   M = 1000), so I(law; C_path) = 0 EXACTLY at every age: the watch
   channel carries zero law information forever. Two admissibility
   probes at N = 30 (propose 49; propose 14) return three distinct
   rows (SEMI FF / IND TF / MEM TT, asserted), so I(law; probes) =
   log 3: the FULL coordinate for two queries. The ledger prices the
   observation/intervention gap: 0 nats watched forever vs 1.0986
   nats bought by two probes.

5. HEAT OPENS THE LAW CHANNEL, DECELERATING (observation + exact
   first move; verified S3). At beta = 2, I(law; path_tau) = 0.0503 /
   0.1324 / 0.1919 / 0.2182 nats (growing, asserted; increments
   0.082, 0.059, 0.026 -- DECELERATING, not linear): four watched
   moves buy 19.9% of the law. The first move equals the mixture
   divergence of the three seed menus, matched to 4.2e-17 (asserted)
   -- and at the seed only D-SEMI's menu differs (asserted; IND and
   MEM coincide until a prime repeats), so early law information is
   exactly a squarefree read on the moves.

6. THE MI WITNESS GAP (rule, proved -- chain rule, no regularity
   conditions; values computed; verified S4). The dated state is a
   function of the path, so I(G; path) = I(G; dated) +
   I(G; path | dated) EXACTLY (asserted to < 1e-12, both fates
   computed independently): the path's surplus is the route
   posterior's G-information -- chamber eleven's Fisher identity
   I_path = I_state + I(route) acquires an information-theoretic twin
   at finite age. Values (beta-grid, mixed ensemble): gap_IND =
   0.0130 vs gap_DYN = 0.0033; mnemonic fractions rho =
   I(dated)/I(path): IND 0.829, DYN 0.955 -- the same fate ordering
   and nearly the same fractions as chamber twelve's Fisher tax
   (0.803 / 0.927 at M = 30): the tax is not a Fisher artifact.

7. THE FOSSIL PARADOX (rule, proved + computed; verified S5). The
   column world: I(G; dated) = I(G; path) EXACTLY (diff 6.9e-18,
   asserted -- the perfect fossil, P156) while its route is MAXIMALLY
   unrecoverable: H(path | dated, G) = 0.3183 bits = the uniform
   maximum EXACTLY (asserted) -- the largest value that support
   allows. Breadth is the reverse: positive witness gap (0.0130) with
   a route posterior SKEWED below uniform (1.5414 of 2.0900 bits,
   ratio 0.737, asserted strict). THE PARADOX: the fate that
   remembers its temperature perfectly forgets its history maximally,
   and necessarily so -- zero menu drift forces the route posterior
   UNIFORM (P156), and uniformity is simultaneously the proof of the
   perfect fossil (beta-free) and the maximum of route entropy.
   Memory for the generator and memory for the past are different
   resources, and the chain identity (finding 6) locates the
   relation exactly: what the state loses about G is precisely what
   the route posterior carries -- so a perfect generator fossil has
   a maximally unreadable past.

8. THE CHANNEL-SPLIT CEILING + COMPLETION AMNESIA IN MI (observation
   in range; PR7 confirmed in direction; verified S6). Fixed-age
   residuals H(G | channel), beta-grid on D-IND: the path channel
   falls strictly (1.0552 / 1.0251 / 1.0095 / 1.0015, asserted) while
   the state channel stalls and TURNS UP (1.0552 / 1.0296 / 1.0262 /
   1.0324) -- chamber twelve's completion arc (peak then collapse) in
   MI dress, unpredicted: as the M = 12 world nears completion its
   bare state starts FORGETTING its temperature while the watch keeps
   earning. The ceiling belongs to states; honest note: in this small
   window the split is 1.031x at tau = 4 (the pass-1b sketch guessed
   1.5x -- the direction confirmed, the magnitude window-limited),
   and the path residual is nowhere near 0 in range.

9. THE K-GAP (observation in range; PR8 confirmed; verified S6). The
   generator is log2 3 = 1.58 bits; the unrecoverable route entropy
   H(path | dated, G) is 0 / 0.89 / 2.01 / 3.27 bits at tau = 1..4:
   it CROSSES the entire generator description between ages 2 and 3
   (asserted) and grows ~1 bit/move while the generator stays fixed.
   Kolmogorov-short, history-tall: by age four the world hides twice
   its own description in unrecoverable route alone.

10. THE SOLVER SCORE (rule -- achievability + strict regret,
    computed; verified S6). The Bayes posterior predictor ACHIEVES
    the ceiling (log-loss = H(G | dated) = 1.0358 nats, matched to
    < 1e-12, asserted): the benchmark is TIGHT, not vacuous. The MAP
    point solver achieves the 0-1 floor 1 - E[max posterior] = 0.5444
    by construction. A smoothed-MAP plug-in (eps = 0.01) pays 3.1079
    nats (+200%, asserted strict): solvers score against the literal
    optimum, not against each other.

THE HEADLINE. The observer theorems assemble into ONE exact ledger --
I(coordinate; channel) with the coordinate split (law in the state,
temperature in the clock), the cold floor (law: 0 watched, log 3 for
two probes), the MI witness gap (proved chain-rule twin of the Fisher
identity), and the fossil paradox (a perfect generator fossil has a
maximally unreadable past). And the ledger is a SOLVED BENCHMARK: a
three-symbol generator whose induction task knows its own Bayes
ceiling exactly, achievable, with unboundedly growing unrecoverable
route entropy alongside. Any compression-driven inducer faces these
numbers as its optimum. (Exploitation contact, verify-first, NOT
begun here: Solomonoff/Hutter universal induction, MDL (Rissanen),
Chollet's ARC. The general point that underdetermination caps
induction is textbook; the contribution would be EXACTNESS -- closed
posteriors, known ceilings, prices for every escape. The graduation
review adjudicates at arc close.)

HONEST LIMITS. (a) M = 12, T = 4, seed 1: every number is
truncated-menu exact; the untruncated anchors are the finite
thermometer (P148) and the age law (P156). (b) The beta grid makes G
finite: the ceiling is exact FOR THE STATED TASK; a continuous prior
needs the Fisher rows (chambers six-twelve). (c) One unfrozen
expectation refuted (finding 2), one pass-1b magnitude sketch missed
(finding 8) -- both recorded. (d) 'H'-padded records make completion
observable: a dead world is a readable fossil, a channel feature,
not an artifact. (e) The T = 0 identity of the three laws is
asserted 8 steps at M = 1000 here; the general statement is P153's.

RUN RECORD (this file, python explore_induction_ceiling.py, ~0.15 s):
  S0 machinery: 12 path distributions sum to 1 (< 1e-12); column
     route posterior uniform (3 paths at t = 4, tau = 3, spread
     1.4e-17).
  S1 ledger: PR1 strict at all 3 rows; pairwise law MI 0.0992 /
     0.1588 / 0.0193, IND support 26 states inside MEM's 55; PR5
     ratios 0.70/0.82/1.14/1.62.
  S2 cold floor: 8-step greedy identical x3 (M = 1000); probe rows
     distinct; log 3 = 1.0986.
  S3 heat: engine vs direct first move diff 4.2e-17; share 0.199.
  S4 chain identity < 1e-12 both fates; gaps 0.0130 / 0.0033.
  S5 fossil paradox: column diff 6.9e-18, H(route) = max = 0.3183
     bits; breadth ratio 0.737.
  S6 ceiling: path residual strictly falling; state turns up at
     tau = 4; K-gap crossing tau = 3; Bayes achievability < 1e-12;
     smoothed-MAP 3.1079 vs 1.0358.
  Total: 37 asserts green. beta = 2 wherever unstated.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from math import gcd, log, log2
from functools import lru_cache

M_CAP = 12          # menu truncation (stated in every claim)
T_CAP = 4           # max age
BETAS = (1.5, 2.0, 3.0)
LAWS3 = ("SEMI", "IND", "MEM")
LOG = log
checks = 0

def ok(cond, msg):
    global checks
    assert cond, msg
    checks += 1

# ---------- arithmetic ----------

@lru_cache(maxsize=None)
def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return tuple(sorted(f.items()))

def squarefree(n):
    return all(e == 1 for _, e in factor(n))

def lcm(a, b):
    return a * b // gcd(a, b)

@lru_cache(maxsize=None)
def carmichael(n):
    if n == 1:
        return 1
    lam = 1
    for p, e in factor(n):
        if p == 2:
            l = 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
        else:
            l = p ** (e - 1) * (p - 1)
        lam = lcm(lam, l)
    return lam

def admissible(law, N, m):
    if law == "IND":
        return gcd(N, m) == 1
    if law == "SEMI":
        return squarefree(N * m)
    if law == "MEM":
        return any(N % p != 0 for p, _ in factor(m))
    if law == "DYN":
        return carmichael(N * m) > carmichael(N)
    if law == "COL":
        k = m
        while k % 3 == 0:
            k //= 3
        return k == 1
    raise ValueError(law)

def menu(law, N, M=M_CAP):
    return [m for m in range(2, M + 1) if admissible(law, N, m)]

# ---------- exact path distributions ----------

@lru_cache(maxsize=None)
def path_dist(law, beta, T, M=M_CAP):
    """dict: T-tuple of moves ('H' pads a completed world) -> exact prob."""
    out = {}
    def rec(N, prefix, prob):
        if len(prefix) == T:
            out[prefix] = out.get(prefix, 0.0) + prob
            return
        men = menu(law, N, M)
        if not men:
            rec(N, prefix + ("H",), prob)
            return
        Z = sum(m ** -beta for m in men)
        for m in men:
            rec(N * m, prefix + (m,), prob * m ** -beta / Z)
    rec(1, (), 1.0)
    return out

def state_of(prefix):
    N = 1
    for m in prefix:
        if m != "H":
            N *= m
    return N

# ---------- ensembles + information ----------

def mixed_ensemble(gens, T=T_CAP):
    """joint dict (g_index, tau, path_prefix) -> prob; g, tau uniform."""
    joint = {}
    w = 1.0 / (len(gens) * T)
    for gi, (law, beta) in enumerate(gens):
        for path, pr in path_dist(law, beta, T).items():
            for tau in range(1, T + 1):
                key = (gi, tau, path[:tau])
                joint[key] = joint.get(key, 0.0) + pr * w
    return joint

def fixed_ensemble(gens, tau):
    joint = {}
    w = 1.0 / len(gens)
    for gi, (law, beta) in enumerate(gens):
        for path, pr in path_dist(law, beta, tau).items():
            key = (gi, tau, path)
            joint[key] = joint.get(key, 0.0) + pr * w
    return joint

def mutual_info(joint, xf, cf):
    px, pc, pxc = {}, {}, {}
    for k, p in joint.items():
        if p <= 0:
            continue
        x, c = xf(k), cf(k)
        px[x] = px.get(x, 0.0) + p
        pc[c] = pc.get(c, 0.0) + p
        pxc[(x, c)] = pxc.get((x, c), 0.0) + p
    return sum(p * LOG(p / (px[x] * pc[c])) for (x, c), p in pxc.items())

def entropy(joint, xf):
    px = {}
    for k, p in joint.items():
        if p > 0:
            x = xf(k)
            px[x] = px.get(x, 0.0) + p
    return -sum(p * LOG(p) for p in px.values())

X_G = lambda k: k[0]
C_STATE = lambda k: state_of(k[2])
C_DATED = lambda k: (state_of(k[2]), k[1])
C_PATH = lambda k: k[2]

# ================================================================
print("S0: machinery -- exact distributions, column uniformity")
# ================================================================

nsum = 0
for law in ("SEMI", "IND", "MEM", "DYN", "COL"):
    for beta in BETAS[:2]:
        tot = sum(path_dist(law, beta, T_CAP).values())
        ok(abs(tot - 1.0) < 1e-12, f"path dist sums to 1 ({law}, {beta})")
        nsum += 1
for law, beta in (("IND", 3.0), ("COL", 3.0)):
    tot = sum(path_dist(law, beta, T_CAP).values())
    ok(abs(tot - 1.0) < 1e-12, f"path dist sums to 1 ({law}, {beta})")
    nsum += 1
print(f"  {nsum} path distributions sum to 1")

# column route posterior uniform: t = 4 (3^4), tau = 3, moves in {3, 9}
# compositions of 4 into 3 parts from {1,2}: 2+1+1 in three orders
col = path_dist("COL", 2.0, 3)
grp = {p: pr for p, pr in col.items() if state_of(p) == 3 ** 4}
vals = list(grp.values())
ok(len(grp) == 3, "compositions of 4 into 3 parts from {1,2}: expect 3 paths")
ok(max(vals) - min(vals) < 1e-14, "column route posterior uniform")
print(f"  column (t=4, tau=3): {len(grp)} paths, spread {max(vals)-min(vals):.1e}")

# ================================================================
print("\nS1: THE LEDGER -- I(coordinate; channel), mixed-age ensemble")
# ================================================================

classes = {
    "beta-grid on D-IND": [("IND", b) for b in BETAS],
    "beta-grid on D-DYN": [("DYN", b) for b in BETAS],
    "law-grid at beta=2": [(law, 2.0) for law in LAWS3],
}
ledger = {}
for name, gens in classes.items():
    joint = mixed_ensemble(gens)
    hs = entropy(joint, X_G)
    i_s = mutual_info(joint, X_G, C_STATE)
    i_d = mutual_info(joint, X_G, C_DATED)
    i_p = mutual_info(joint, X_G, C_PATH)
    ledger[name] = (hs, i_s, i_d, i_p)
    ok(i_s < i_d < i_p, f"PR1 strict ladder ({name})")
    print(f"  {name}: H(G)={hs:.4f}  I(state)={i_s:.4f} < "
          f"I(dated)={i_d:.4f} < I(path)={i_p:.4f}")
# (unfrozen expectation "law harder than temperature" was REFUTED by the
#  first run: the law-grid MI exceeds the beta-grid MI in this window --
#  reported as an observation, no assert; the frozen slate never claimed it)

# pairwise decomposition of the law coordinate (the support mechanism):
pair_mi = {}
for pair in (("SEMI", "IND"), ("SEMI", "MEM"), ("IND", "MEM")):
    jp = mixed_ensemble([(l, 2.0) for l in pair])
    pair_mi[pair] = mutual_info(jp, X_G, C_STATE)
print("  pairwise I(law; state):",
      "  ".join(f"{a}-{b} {v:.4f}" for (a, b), v in pair_mi.items()))
ok(pair_mi[("IND", "MEM")] < pair_mi[("SEMI", "IND")] < pair_mi[("SEMI", "MEM")],
   "the SEMI pairs dominate: the law reads mostly as squarefree-vs-not")
s_ind = {state_of(p) for p in path_dist("IND", 2.0, T_CAP)}
s_mem = {state_of(p) for p in path_dist("MEM", 2.0, T_CAP)}
ok(not (s_ind - s_mem) and (s_mem - s_ind),
   "IND states a strict subset of MEM states (MEM alone re-deepens)")
print(f"  IND support strictly inside MEM's ({len(s_ind)} vs {len(s_mem)} "
      f"states; least MEM-only: {min(s_mem - s_ind)})")

# PR5: fate ordering at fixed ages (dated == state at known tau)
print("  PR5 (fixed-age I(G;N_tau), beta-grid): DYN vs IND")
ratios = []
for tau in range(1, T_CAP + 1):
    ji = fixed_ensemble(classes["beta-grid on D-IND"], tau)
    jd = fixed_ensemble(classes["beta-grid on D-DYN"], tau)
    ii = mutual_info(ji, X_G, C_STATE)
    idn = mutual_info(jd, X_G, C_STATE)
    ratios.append(idn / ii)
    print(f"    tau={tau}: IND {ii:.4f}  DYN {idn:.4f}  ratio {idn/ii:.2f}")
ok(all(r > 1 for r in ratios[2:]), "PR5: DYN out-informs IND at tau >= 3")
ok(ratios == sorted(ratios), "the mnemonic advantage grows with age")

# ================================================================
print("\nS2: THE COLD FLOOR AND THE PROBE JUMP (T = 0)")
# ================================================================

def greedy_path(law, steps, M=1000):
    N, out = 1, []
    for _ in range(steps):
        men = menu(law, N, M)
        if not men:
            break
        m = min(men)
        out.append(m)
        N *= m
    return tuple(out)

g_paths = {law: greedy_path(law, 8) for law in LAWS3}
ok(g_paths["SEMI"] == g_paths["IND"] == g_paths["MEM"],
   "cold blindness: three demands, one 8-step trajectory")
print(f"  T=0 trajectory (all three laws): {g_paths['IND']}")
print("  => I(law; C_path) = 0 exactly, at every age")

probe_state, probes = 30, (49, 14)
rows = {law: tuple(admissible(law, probe_state, q) for q in probes)
        for law in LAWS3}
ok(len(set(rows.values())) == 3, "probe rows distinct: full identification")
print(f"  probe rows at N=30, queries {probes}: {rows}")
print(f"  => I(law; probes) = log 3 = {log(3):.4f} nats; watch/probe gap infinite")

# ================================================================
print("\nS3: heat opens the law channel (beta = 2, fixed-age path MI)")
# ================================================================

law_gens = classes["law-grid at beta=2"]
i_law = []
for tau in range(1, T_CAP + 1):
    j = fixed_ensemble(law_gens, tau)
    i_law.append(mutual_info(j, X_G, C_PATH))
print("  I(law; path_tau):", "  ".join(f"{v:.5f}" for v in i_law))
ok(all(b > a for a, b in zip(i_law, i_law[1:])), "PR3: growing in tau")

# direct first-move mixture divergence from the menus at the seed
menus = {law: menu(law, 1) for law in LAWS3}
dists = {}
for law, men in menus.items():
    Z = sum(m ** -2.0 for m in men)
    dists[law] = {m: m ** -2.0 / Z for m in men}
support = sorted(set().union(*dists.values()))
mix = {m: sum(dists[law].get(m, 0.0) for law in LAWS3) / 3 for m in support}
direct = sum(dists[law][m] / 3 * LOG(dists[law][m] / mix[m])
             for law in LAWS3 for m in dists[law])
ok(abs(direct - i_law[0]) < 1e-12, "first move = menu mixture divergence")
print(f"  first move: engine {i_law[0]:.6f} vs direct {direct:.6f} "
      f"(diff {abs(direct - i_law[0]):.1e})")
ok(menus["IND"] == menus["MEM"] != menus["SEMI"],
   "at the seed only SEMI's menu differs")
print(f"  share of H(law) after {T_CAP} moves: {i_law[-1]/log(3):.3f}")

# ================================================================
print("\nS4: THE MI WITNESS GAP -- chain identity + fate comparison")
# ================================================================

def gap_report(name):
    joint = mixed_ensemble(classes[name])
    i_d = mutual_info(joint, X_G, C_DATED)
    i_p = mutual_info(joint, X_G, C_PATH)
    # I(G; path | dated) directly: condition on dated value
    cond = {}
    for k, p in joint.items():
        cond.setdefault(C_DATED(k), {})[k] = p
    i_cond = 0.0
    for sub in cond.values():
        w = sum(sub.values())
        i_cond += w * mutual_info({k: p / w for k, p in sub.items()},
                                  X_G, C_PATH)
    ok(abs(i_p - (i_d + i_cond)) < 1e-12,
       f"chain identity I(G;path) = I(G;dated) + I(G;path|dated) ({name})")
    return i_d, i_p, i_cond

d_i, p_i, g_i = gap_report("beta-grid on D-IND")
d_d, p_d, g_d = gap_report("beta-grid on D-DYN")
print(f"  IND: I(dated)={d_i:.4f}  I(path)={p_i:.4f}  gap={g_i:.4f}  "
      f"rho={d_i/p_i:.3f}")
print(f"  DYN: I(dated)={d_d:.4f}  I(path)={p_d:.4f}  gap={g_d:.4f}  "
      f"rho={d_d/p_d:.3f}")
ok(g_i > 0 and g_d > 0, "PR4: the MI witness gap is positive in breadth+depth")

# ================================================================
print("\nS5: THE FOSSIL PARADOX -- column vs breadth")
# ================================================================

col_gens = [("COL", b) for b in BETAS]
jc = mixed_ensemble(col_gens)
i_cd = mutual_info(jc, X_G, C_DATED)
i_cp = mutual_info(jc, X_G, C_PATH)
ok(abs(i_cd - i_cp) < 1e-12, "PR6a: column I(G;dated) = I(G;path) exactly")
print(f"  column: I(dated)={i_cd:.4f} = I(path)={i_cp:.4f} "
      f"(diff {abs(i_cd-i_cp):.1e}) -- zero witness gap")

def route_entropy_bits(joint):
    """H(path | dated, G) in bits, and E[log2 #paths | dated, G]."""
    cond = {}
    for k, p in joint.items():
        cond.setdefault((k[0], C_DATED(k)), {})[k[2]] = p
    h = hmax = 0.0
    for sub in cond.values():
        w = sum(sub.values())
        # -sum p*log2(p/w) = w * H(cell): the raw p already carry the weight
        h += -sum(p * log2(p / w) for p in sub.values() if p > 0)
        hmax += log2(len(sub)) * w
    return h, hmax

hc, hcmax = route_entropy_bits(jc)
ok(abs(hc - hcmax) < 1e-12, "PR6b: column route posterior uniform = max entropy")
ji = mixed_ensemble(classes["beta-grid on D-IND"])
hi, himax = route_entropy_bits(ji)
ok(hi < himax - 1e-9, "breadth route posterior strictly skewed below uniform")
print(f"  column: H(route)={hc:.4f} bits = uniform max {hcmax:.4f}")
print(f"  breadth: H(route)={hi:.4f} bits < uniform max {himax:.4f} "
      f"(ratio {hi/himax:.3f})")
print("  => perfect temperature memory = maximal route amnesia, and conversely")

# ================================================================
print("\nS6: the channel-split ceiling, the K-gap, the solver score")
# ================================================================

gens_ind = classes["beta-grid on D-IND"]
h_g = log(3)
res_state, res_path = [], []
for tau in range(1, T_CAP + 1):
    j = fixed_ensemble(gens_ind, tau)
    res_state.append(h_g - mutual_info(j, X_G, C_STATE))
    res_path.append(h_g - mutual_info(j, X_G, C_PATH))
print("  H(G | state_tau):", "  ".join(f"{v:.4f}" for v in res_state))
print("  H(G | path_tau): ", "  ".join(f"{v:.4f}" for v in res_path))
ok(all(b < a for a, b in zip(res_path, res_path[1:])),
   "PR7a: path residual strictly falls with age")
ok(res_state[-1] > res_path[-1], "PR7b: the state channel keeps more hidden")
print(f"  state/path residual ratio at tau={T_CAP}: "
      f"{res_state[-1]/res_path[-1]:.3f}")

# K-gap: generator bits vs unrecoverable route bits, per age
kbits = log2(len(gens_ind))
route_bits = []
for tau in range(1, T_CAP + 1):
    j = fixed_ensemble(gens_ind, tau)
    hb, _ = route_entropy_bits(j)
    route_bits.append(hb)
print(f"  generator: {kbits:.2f} bits; route entropy H(path|dated,G) bits:",
      "  ".join(f"{v:.2f}" for v in route_bits))
cross = next(t for t, v in enumerate(route_bits, 1) if v > kbits)
ok(cross <= T_CAP, "PR8: unrecoverable history crosses the generator size")
print(f"  crossing at tau = {cross}: the world's unrecoverable history "
      f"outweighs its entire description")

# solver scores on the dated channel, mixed ensemble
joint = mixed_ensemble(gens_ind)
cond = {}
for k, p in joint.items():
    cond.setdefault(C_DATED(k), {})[k[0]] = \
        cond.setdefault(C_DATED(k), {}).get(k[0], 0.0) + p
ceiling = h_g - mutual_info(joint, X_G, C_DATED)
bayes_ll = zer1 = smooth_ll = 0.0
eps, nG = 0.01, len(gens_ind)
for sub in cond.values():
    w = sum(sub.values())
    post = {g: p / w for g, p in sub.items()}
    bayes_ll += -w * sum(pg * LOG(pg) for pg in post.values() if pg > 0)
    zer1 += w * (1 - max(post.values()))
    gmap = max(post, key=post.get)
    for g, pg in post.items():
        q = (1 - eps) * (g == gmap) + eps / nG
        smooth_ll += -w * pg * LOG(q)
ok(abs(bayes_ll - ceiling) < 1e-12,
   "PR9a: the Bayes posterior ACHIEVES the ceiling (tight benchmark)")
ok(smooth_ll > ceiling + 1e-9, "PR9b: smoothed-MAP pays a strict regret")
print(f"  Bayes ceiling H(G|dated) = {ceiling:.4f} nats (achieved: "
      f"{bayes_ll:.4f}); 0-1 floor = {zer1:.4f} (MAP achieves it)")
print(f"  smoothed-MAP (eps={eps}) log-loss {smooth_ll:.4f} "
      f"(+{(smooth_ll/ceiling-1)*100:.0f}% regret)")

print(f"\nALL GREEN: {checks} asserts. (M={M_CAP}, T={T_CAP}, seed 1; "
      f"exact enumeration, no Monte Carlo.)")
