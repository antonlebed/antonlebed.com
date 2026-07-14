"""
Meaning as codeword: operationalize "a meaning" as a ring element and
test the three
properties named -- exact composition/decomposition (VSA
binding), snap-to-whole (Gestalt = codeword), element-as-operator
(activity theory) -- plus the one wall the substrate was expected to
pay, measured, with its ring-native cure.

Setting: RAD = Z/510510 (rung k=7, tower split: data {2,3,5,7},
parity {11,13,17}; crt.py). A CONCEPT is a valid ECC codeword -- a
data value n < 210 carried on all 7 channels. The claim under test is:
binding/unbinding exact where
HRR/SPA's is approximate, and cleanup a DECODER WITH A GUARANTEE
where the literature's cleanup memory is probabilistic
nearest-neighbor. Nearest neighbor in the literature: Plate's HRR /
Eliasmith's Semantic Pointer Architecture -- circular-convolution
binding, correlation unbinding, both approximate by construction.
(Honesty note: XOR-binding substrates -- Kanerva's binary spatter
codes -- also unbind a single pair exactly, XOR being an involution;
the guarantee-backed cleanup and the datum-as-operator ring structure
are the legs the binary family does not carry.)

FINDINGS (tier per item; adjudication recorded after the run):

 1 (property, verified): BINDING IS EXACT. bind(r, f) = r*f, unbind =
   multiply by the meadow inverse. Exact for EVERY unit role and EVERY
   filler -- exhaustive on Z/210 (48 units x 210 fillers), sampled on
   RAD (10^4 pairs), chained roles unbind in either order (S1).
 2 (observation, measured): THE HRR CONTRAST. Circular-convolution
   binding at d=512 unbinds to cosine 0.710 mean (self-noise; never
   1.0), so recovery NEEDS a cleanup memory and is probabilistic:
   measured cleanup accuracy 100% at (d=512, M=1000) single-pair,
   86.3% at (d=64, M=1000) 3-pair bundles. The ring's unbind is exact
   at any lexicon size -- no cleanup step exists to fail (S2).
 3 (rule, proved from d = 4 + exhaustive): SNAP-TO-WHOLE HAS THREE
   EXACT ZONES. MDS d=4 makes the perceptual basin sharp: (a) any single
   corrupted window (all 210 x 51 cases) and any 3 erased windows
   (all 210 x 35 cases) decode to the whole exactly; (b) TWO
   corrupted windows are always detected and NEVER mis-snapped (the
   view moved 2 windows from its whole, and every OTHER whole is
   >= d - 2 = 2 away -- a mis-snap would need distance <= 1, i.e.
   2 + 1 < d, which d = 4 forbids); (c) THREE corrupted windows can
   produce an ILLUSION -- the view snaps to a DIFFERENT valid whole
   (witness printed), never to garbage -- but rarely: 0.58% of 5000
   random weight-3 views (29 illusions, the rest refused; every snap
   a valid other whole, every view detected). Basin volume is exactly
   52 tuples per concept; basins are disjoint; coverage
   210*52/510510 = 2.14% -- beyond radius 1 the percept honestly
   refuses instead of hallucinating (S3).
 4 (rule for the wall, proved + verified; property for the cure):
   THE SUPERPOSITION WALL IS THE MINIMUM DISTANCE. The classical VSA
   bundle (elementwise SUM of bound pairs) carries no cleanup here,
   and for codeword fillers the failure is EXACT: unbinding
   r1*f1 + r2*f2 returns f1 + noise where noise = r1^{-1}*r2*f2
   shares f2's support (units preserve support), and every nonzero
   codeword has tuple weight >= d = 4 (a nonzero f2 < 210 vanishes
   on at most 3 channels: any 4-window product >= 210) -- the query
   sits at distance >= 4 from f1's codeword, outside the radius-1
   basin, ALWAYS. Retrieval = 0/2000 verified, every noise weight
   >= 4; the lone escape is the degenerate empty second item
   (f2 = 0, P = 1/210). With a ring-valued SECOND item instead (the
   queried filler must stay a codeword for cleanup to have a
   target), the rate is exactly the basin fraction 52/510510 ~ 1e-4:
   unit multiplication is a bijection, so uniform f2 makes the noise
   exactly uniform. The contrast: quasi-orthogonality -- what makes bundle
   noise NEARLY INVISIBLE in high-dimensional real space -- is an
   archimedean resource the ring does not have; here the same d
   that guarantees the snap forbids the sum. THE CURE is
   ring-native: bundle = DIRECT SUM. Idempotent slots (roles =
   channel windows) give exact retrieval of every stored item, hard
   capacity = the channel partition; multiplicative binding composes
   with slots (a role bound INSIDE a slot window unbinds exactly)
   (S4).
 5 (property, verified): ELEMENT-AS-OPERATOR. Every element is both
   datum and map: op_x = multiply-by-x, and op_x(1) = x -- the datum
   is read back by acting on 1 (the regular representation is
   faithful; an IDENTITY, free by construction -- stated, not
   check-numbered). Meadow laws exhaustive on Z/210: x*pinv(x)*x = x,
   x*pinv(x) = e_supp(x); pinv inverts unit actions exactly and
   recovers the surviving window for non-units: pinv(x)*(x*f) =
   e_supp(x)*f. The operator's reach IS its window support:
   |image(op_x)| = product of support primes, all 210 elements --
   unit <=> bijective action (S5).
 6 (rule, exhaustive end-to-end): THE SCENE PIPELINE. Grammar =
   windows: AGENT = channels {2,3} (6 values), PATIENT = {5},
   ACTION = {7}; every data value n < 210 IS a valid scene
   (bijective grammar, zero syntax overhead). All 210 scenes x all
   51 single-window corruptions snap back and read out all three
   parts exactly; all 35 triple-erasure patterns reconstruct (the
   minimal 4-window product is 2*3*5*7 = 210 = the scene space,
   exactly sized) (S6).

PREDICTIONS (stated before the run):
 PR1: S1 exhaustive + sampled, zero failures.            LANDED.
 PR2: HRR self-noise mean cosine in (0.2, 0.95) at d=512;
      cleanup accuracies reported, no threshold assert.  LANDED (0.710).
 PR3: S3 sweeps exhaustive, zero failures; weight-2 never
      mis-snaps; a weight-3 illusion witness exists.     LANDED.
 PR4: additive-bundle retrieval < 1% of 2000 trials;
      slot records 100%.                                 LANDED, SHARPENED
      TWICE: (i) the first run drew f2 uniform INCLUDING 0 and measured
      0.30% -- 30x the basin fraction. The excess was entirely the
      degenerate term (f2 = 0 makes the noise vanish; P = 1/210 =
      0.48%), i.e. an empty second slot, not a survived superposition.
      (ii) The prediction itself was the wrong mechanism for codeword
      fillers: the rate is not ~1e-4 but EXACTLY 0 (noise weight >= d,
      the minimum-distance argument above) -- caught the understatement,
      and S4a now verifies the weight floor.
 PR5: S5 laws exhaustive on Z/210, sampled on RAD.       LANDED.
 PR6: S6 pipeline exhaustive, zero failures.             LANDED.

Run record: ALL 21 CHECKS PASS, ~3 s (seeded: random 98, numpy 98).
Regime: RAD exhaustive where the lexicon is the full 210 (S3a/b/c, S5
Z/210 rows, S6), 22-concept exhaustive + 3000 random for weight-2
(S3d/e; the first run's list carried a duplicate 209 -- '23-scene' was
22 distinct, label fixed round 5), 5000 random weight-3 views for the
zone-3 census (S3g, folded in),
sampled 500-10000 for RAD-sized claims (S1b/c, S4, S5c); HRR at d=512
and d=64, M=1000, 300 cleanup trials per cell + the ring cell (S2b,
300/300). Note: the original S2b was check(True) and the
original op_x(1) = x row a Python tautology -- both vacuous checks,
replaced by the ring cell and a prose clause (21 -> 20 checks).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
import sys
from itertools import combinations
from math import gcd, prod

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import (RAD_RING, DATA_RING, encode, decode, decode_partial,
                 ecc_encode, ecc_syndrome, ecc_correct, idempotent,
                 mod_inverse)

random.seed(98)

CHECKS = 0
def check(label, cond):
    global CHECKS
    CHECKS += 1
    status = "PASS" if cond else "FAIL"
    print(f"  [{status}] {label}")
    if not cond:
        raise SystemExit(f"CHECK FAILED: {label}")


def meadow_pinv(x, ring):
    """The meadow pseudo-inverse: per-channel inverse where nonzero, 0 else."""
    t = encode(x, ring)
    pt = tuple(mod_inverse(r, q) if r != 0 else 0 for r, q in zip(t, ring.moduli))
    return decode(pt, ring)


def support_channels(x, ring):
    return frozenset(i for i, q in enumerate(ring.moduli) if x % q != 0)


# ─────────────────────────────────────────────────────────────────────
# S1. BINDING IS EXACT
# ─────────────────────────────────────────────────────────────────────

def s1_bind_unbind():
    print("\nS1. EXACT BIND/UNBIND (bind = multiply, unbind = meadow inverse)")
    R = DATA_RING  # Z/210, exhaustive
    units = [r for r in range(R.N) if gcd(r, R.N) == 1]
    fails = 0
    for r in units:
        rinv = meadow_pinv(r, R)
        for f in range(R.N):
            if (rinv * ((r * f) % R.N)) % R.N != f:
                fails += 1
    check(f"S1a Z/210 exhaustive: {len(units)} units x {R.N} fillers, "
          f"unbind exact ({len(units)*R.N} cases, {fails} failures)", fails == 0)

    R = RAD_RING
    fails = 0
    for _ in range(10_000):
        r = random.randrange(R.N)
        while gcd(r, R.N) != 1:
            r = random.randrange(R.N)
        f = random.randrange(R.N)
        if (meadow_pinv(r, R) * ((r * f) % R.N)) % R.N != f:
            fails += 1
    check(f"S1b RAD sampled: 10000 (unit, filler) pairs, unbind exact", fails == 0)

    fails = 0
    for _ in range(1_000):
        r1, r2 = (random.randrange(R.N) for _ in range(2))
        while gcd(r1, R.N) != 1: r1 = random.randrange(R.N)
        while gcd(r2, R.N) != 1: r2 = random.randrange(R.N)
        f = random.randrange(R.N)
        bound = (r2 * ((r1 * f) % R.N)) % R.N
        a = (meadow_pinv(r1, R) * ((meadow_pinv(r2, R) * bound) % R.N)) % R.N
        b = (meadow_pinv(r2, R) * ((meadow_pinv(r1, R) * bound) % R.N)) % R.N
        if a != f or b != f:
            fails += 1
    check("S1c chained roles unbind in either order (1000 trials)", fails == 0)


# ─────────────────────────────────────────────────────────────────────
# S2. THE HRR CONTRAST (measured)
# ─────────────────────────────────────────────────────────────────────

def s2_hrr_contrast():
    print("\nS2. THE HRR CONTRAST (circular convolution, measured)")
    import numpy as np
    rng = np.random.default_rng(98)

    def cconv(a, b):
        return np.fft.irfft(np.fft.rfft(a) * np.fft.rfft(b), n=len(a))

    def ccorr(a, b):  # approximate unbinding (Plate involution)
        return np.fft.irfft(np.conj(np.fft.rfft(a)) * np.fft.rfft(b), n=len(a))

    def cos(a, b):
        return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

    d = 512
    sims = []
    for _ in range(1000):
        r = rng.normal(0, 1 / d ** 0.5, d)
        f = rng.normal(0, 1 / d ** 0.5, d)
        sims.append(cos(ccorr(r, cconv(r, f)), f))
    mean_sim = sum(sims) / len(sims)
    print(f"  d=512 unbound-vs-filler cosine: mean {mean_sim:.3f}, "
          f"min {min(sims):.3f}, max {max(sims):.3f}  (exact would be 1.0)")
    check("S2a HRR unbinding is approximate: mean cosine in (0.2, 0.95)",
          0.2 < mean_sim < 0.95)

    # cleanup accuracy: single pair at d=512, 3-pair bundle at d=64
    for d, npairs, label in ((512, 1, "single pair"), (64, 3, "3-pair bundle")):
        M = 1000
        lex = rng.normal(0, 1 / d ** 0.5, (M, d))
        lexn = lex / np.linalg.norm(lex, axis=1, keepdims=True)
        hits = 0
        trials = 300
        for _ in range(trials):
            idxs = rng.choice(M, npairs, replace=False)
            roles = rng.normal(0, 1 / d ** 0.5, (npairs, d))
            s = np.zeros(d)
            for j in range(npairs):
                s += cconv(roles[j], lex[idxs[j]])
            q = ccorr(roles[0], s)
            best = int(np.argmax(lexn @ (q / np.linalg.norm(q))))
            hits += (best == idxs[0])
        print(f"  d={d}, M={M}, {label}: cleanup accuracy {hits}/{trials} "
              f"({100*hits/trials:.1f}%)")

    # the ring cell of the same table: identical task, codeword lexicon
    R = RAD_RING
    ring_hits = 0
    for _ in range(300):
        f = random.randrange(210)
        r = random.randrange(R.N)
        while gcd(r, R.N) != 1: r = random.randrange(R.N)
        got = (meadow_pinv(r, R) * ((r * f) % R.N)) % R.N
        ring_hits += (got == f)
    check("S2b the ring cell of the same task: 300/300 exact retrieval, "
          "no cleanup step to fail", ring_hits == 300)


# ─────────────────────────────────────────────────────────────────────
# S3. SNAP-TO-WHOLE: THREE EXACT ZONES
# ─────────────────────────────────────────────────────────────────────

def s3_snap_to_whole():
    print("\nS3. SNAP-TO-WHOLE (MDS cleanup: guaranteed / detected / illusion)")
    R = RAD_RING
    D = prod(R.moduli[i] for i in R.data_channels)  # 210 concepts

    # zone 1: radius 1 -- guaranteed snap (exhaustive)
    fails = 0
    for n in range(D):
        cw = ecc_encode(tuple(n % R.moduli[i] for i in R.data_channels), R)
        for ch in range(R.k):
            q = R.moduli[ch]
            for wrong in range(q):
                if wrong == cw[ch]:
                    continue
                bad = list(cw); bad[ch] = wrong
                corrected, loc = ecc_correct(tuple(bad), R)
                if corrected != cw or loc != ch:
                    fails += 1
    check(f"S3a all {D} concepts x 51 single-window corruptions snap back "
          f"exactly ({D*51} cases)", fails == 0)

    # erasures: any 3 windows lost, whole reconstructed (exhaustive)
    fails = 0
    for n in range(D):
        cw = ecc_encode(tuple(n % R.moduli[i] for i in R.data_channels), R)
        for erased in combinations(range(R.k), 3):
            kept = [i for i in range(R.k) if i not in erased]
            if decode_partial(cw, R, kept) % prod(R.moduli[i] for i in kept) != n:
                fails += 1
    check(f"S3b all {D} concepts x 35 triple-erasure patterns reconstruct "
          f"({D*35} cases)", fails == 0)

    # basin geometry: 52 tuples per basin, all basins disjoint
    basin = set()
    per = 1 + sum(q - 1 for q in R.moduli)
    for n in range(D):
        cw = ecc_encode(tuple(n % R.moduli[i] for i in R.data_channels), R)
        basin.add(cw)
        for ch in range(R.k):
            for wrong in range(R.moduli[ch]):
                if wrong != cw[ch]:
                    bad = list(cw); bad[ch] = wrong
                    basin.add(tuple(bad))
    check(f"S3c basins disjoint: {D} x {per} = {D*per} distinct tuples; "
          f"coverage {D*per}/{R.N} = {100*D*per/R.N:.2f}% of tuple space",
          len(basin) == D * per)

    # zone 2: weight-2 always detected, never mis-snapped
    fails = 0
    # 22 distinct concepts (range(0,210,11) already ends at 209 = 11*19)
    scenes = sorted(set(range(0, D, 11)) | {1, 2})
    for n in scenes:
        cw = ecc_encode(tuple(n % R.moduli[i] for i in R.data_channels), R)
        for c1, c2 in combinations(range(R.k), 2):
            for w1 in range(R.moduli[c1]):
                if w1 == cw[c1]: continue
                for w2 in range(R.moduli[c2]):
                    if w2 == cw[c2]: continue
                    bad = list(cw); bad[c1] = w1; bad[c2] = w2
                    syn = ecc_syndrome(tuple(bad), R)
                    corrected, loc = ecc_correct(tuple(bad), R)
                    # detected (nonzero syndrome) and refused (no false snap)
                    if all(s == 0 for s in syn) or loc is not None:
                        fails += 1
    n_cases = len(scenes) * 1022
    check(f"S3d weight-2 views: always detected, never mis-snapped "
          f"({len(scenes)}-concept exhaustive, {n_cases} cases)", fails == 0)

    fails = 0
    for _ in range(3000):                                # + random sweep
        n = random.randrange(D)
        cw = ecc_encode(tuple(n % R.moduli[i] for i in R.data_channels), R)
        c1, c2 = random.sample(range(R.k), 2)
        bad = list(cw)
        bad[c1] = random.choice([v for v in range(R.moduli[c1]) if v != cw[c1]])
        bad[c2] = random.choice([v for v in range(R.moduli[c2]) if v != cw[c2]])
        syn = ecc_syndrome(tuple(bad), R)
        corrected, loc = ecc_correct(tuple(bad), R)
        if all(s == 0 for s in syn) or loc is not None:
            fails += 1
    check("S3e weight-2 random sweep across all scenes (3000 trials): "
          "detected, refused", fails == 0)

    # zone 3: the illusion witness -- weight 3 can snap to ANOTHER whole
    c, cprime = 0, 30
    cw = ecc_encode(tuple(c % R.moduli[i] for i in R.data_channels), R)
    cwp = ecc_encode(tuple(cprime % R.moduli[i] for i in R.data_channels), R)
    diff = [i for i in range(R.k) if cw[i] != cwp[i]]
    bad = list(cw)
    for i in diff[:3]:
        bad[i] = cwp[i]                       # 3 windows drift toward c'
    corrected, loc = ecc_correct(tuple(bad), R)
    snapped = decode_partial(corrected, R, list(R.data_channels))
    print(f"  illusion witness: concept {c} corrupted in 3 of the 4 windows "
          f"where {cprime}'s codeword differs -> snaps to {snapped}")
    check(f"S3f weight-3 illusion exists AND lands on a VALID other whole "
          f"(snapped to {snapped} = {cprime}, a codeword -- never garbage)",
          snapped == cprime and loc is not None)

    # how often does zone 3 fool the decoder? (folded in)
    refuse = illusion = 0
    ok = True
    for _ in range(5000):
        n = random.randrange(D)
        cw = ecc_encode(tuple(n % R.moduli[i] for i in R.data_channels), R)
        bad = list(cw)
        for ch in random.sample(range(R.k), 3):
            bad[ch] = random.choice(
                [v for v in range(R.moduli[ch]) if v != cw[ch]])
        syn = ecc_syndrome(tuple(bad), R)
        ok = ok and any(s != 0 for s in syn)   # weight 3 < d: detected
        corrected, loc = ecc_correct(tuple(bad), R)
        if loc is None:
            refuse += 1
        else:
            m = decode_partial(corrected, R, list(R.data_channels))
            ok = ok and (m != n and m < D)     # a VALID other whole
            illusion += 1
    print(f"  zone-3 census: {refuse} refusals, {illusion} illusions "
          f"({100*illusion/5000:.2f}%) of 5000 random weight-3 views")
    check("S3g zone 3 is honest: always detected, illusions are the rare "
          "minority (< 1% measured), and every snap is a valid other whole",
          ok and 0 < illusion < refuse)


# ─────────────────────────────────────────────────────────────────────
# S4. THE SUPERPOSITION WALL + THE DIRECT-SUM CURE
# ─────────────────────────────────────────────────────────────────────

def s4_superposition():
    print("\nS4. THE SUPERPOSITION WALL (additive bundle) + THE CURE (slots)")
    R = RAD_RING
    D = 210
    # THE WALL IS THE MINIMUM DISTANCE (proved): the unbound query is
    # q = f1 + noise with noise = r1^{-1}*r2*f2, and units preserve
    # support, so weight(noise) = weight(f2's tuple) >= d = 4 for every
    # NONZERO codeword f2 (a nonzero f2 < 210 vanishes on at most 3
    # channels: any 4-window product >= 210). The query sits at distance
    # >= 4 from f1's codeword -- retrieval probability is EXACTLY 0 for
    # codeword fillers, not merely ~the basin fraction (that rate holds
    # for a uniform ring-valued SECOND item: units make noise uniform).
    # f2 = 0 is the degenerate term (empty second item -> noise vanishes
    # -> retrieval trivially succeeds, P = 1/210): excluded, the wall is
    # about a REAL superposition. First run kept it and measured 0.30%
    # -- exactly the degenerate term's order, not basin hits.
    trials, hits, min_noise_wt = 2000, 0, R.k
    for _ in range(trials):
        f1, f2 = random.randrange(D), random.randrange(1, D)
        r1 = random.randrange(R.N)
        while gcd(r1, R.N) != 1: r1 = random.randrange(R.N)
        r2 = random.randrange(R.N)
        while gcd(r2, R.N) != 1: r2 = random.randrange(R.N)
        s = ((r1 * f1) % R.N + (r2 * f2) % R.N) % R.N
        q = (meadow_pinv(r1, R) * s) % R.N              # f1 + noise
        noise_wt = sum(1 for v in encode((q - f1) % R.N, R) if v != 0)
        min_noise_wt = min(min_noise_wt, noise_wt)
        corrected, _ = ecc_correct(encode(q, R), R)
        syn_clean = all(v == 0 for v in ecc_syndrome(corrected, R))
        got = decode_partial(corrected, R, list(R.data_channels))
        if syn_clean and got == f1 and decode(corrected, R) < D:
            hits += 1
    rate = hits / trials
    print(f"  additive-bundle retrieval: {hits}/{trials} = {100*rate:.2f}% "
          f"(proved 0 for codeword fillers; min noise weight seen: "
          f"{min_noise_wt}, floor d = 4)")
    check("S4a the wall: retrieval = 0/2000 and every noise term has "
          "weight >= 4 = d -- the wall IS the minimum distance",
          hits == 0 and min_noise_wt >= 4)

    # the cure: bundle = direct sum over idempotent slots
    slots = ((0, 1, 2), (3, 4), (5, 6))     # windows {2,3,5} {7,11} {13,17}
    slot_mods = [prod(R.moduli[i] for i in s) for s in slots]
    fails = 0
    for _ in range(1000):
        xs = [random.randrange(m) for m in slot_mods]
        rec = 0
        for s_ch, x in zip(slots, xs):
            rec = (rec + idempotent(frozenset(s_ch), R) * x) % R.N
        for s_ch, m, x in zip(slots, slot_mods, xs):
            if decode_partial(encode(rec, R), R, list(s_ch)) != x:
                fails += 1
    check(f"S4b the cure: idempotent slots {slot_mods} -- every stored item "
          f"retrieved exactly (1000 records x 3 slots)", fails == 0)

    # binding still composes with slots: a unit role inside one slot
    fails = 0
    m0 = slot_mods[0]
    for _ in range(500):
        u = random.randrange(m0)
        while gcd(u, m0) != 1: u = random.randrange(m0)
        x = random.randrange(m0)
        rec = (idempotent(frozenset(slots[0]), R) * ((u * x) % m0)) % R.N
        got = decode_partial(encode(rec, R), R, list(slots[0]))
        if (mod_inverse(u, m0) * got) % m0 != x:
            fails += 1
    check("S4c slot + binding compose: role-bound filler inside slot 0 "
          "unbinds exactly (500 trials)", fails == 0)


# ─────────────────────────────────────────────────────────────────────
# S5. ELEMENT-AS-OPERATOR
# ─────────────────────────────────────────────────────────────────────

def s5_element_as_operator():
    print("\nS5. ELEMENT-AS-OPERATOR (datum = map; reach = window support)")
    # op_x(1) = x is an IDENTITY (the multiplicative unit reads the datum
    # back -- faithfulness through 1 is free by construction), so it gets
    # a prose clause, not a check that cannot fail.
    R = DATA_RING  # Z/210, exhaustive
    fails_meadow = fails_supp = fails_img = 0
    for x in range(R.N):
        px = meadow_pinv(x, R)
        e_s = idempotent(support_channels(x, R), R)
        if (x * px * x) % R.N != x:
            fails_meadow += 1
        if (x * px) % R.N != e_s:
            fails_supp += 1
        img = len({(x * f) % R.N for f in range(R.N)})
        if img != prod(R.moduli[i] for i in support_channels(x, R)):
            fails_img += 1
    check("S5a meadow laws exhaustive on Z/210: x*pinv(x)*x = x and "
          "x*pinv(x) = e_supp(x)", fails_meadow == 0 and fails_supp == 0)
    check("S5b |image(op_x)| = product of support primes, all 210 elements "
          "(unit <=> bijective action)", fails_img == 0)

    R = RAD_RING
    fails = 0
    for _ in range(1000):
        x, f = random.randrange(R.N), random.randrange(R.N)
        e_s = idempotent(support_channels(x, R), R)
        if (meadow_pinv(x, R) * ((x * f) % R.N)) % R.N != (e_s * f) % R.N:
            fails += 1
    check("S5c RAD sampled: pinv(x)*(x*f) = e_supp(x)*f -- the operator's "
          "reach is its window support (1000 trials)", fails == 0)


# ─────────────────────────────────────────────────────────────────────
# S6. THE SCENE PIPELINE (end-to-end)
# ─────────────────────────────────────────────────────────────────────

def s6_scene_pipeline():
    print("\nS6. THE SCENE PIPELINE (grammar = windows; degrade -> snap -> read)")
    R = RAD_RING
    D = 210

    def parts(n):  # AGENT mod 6 (windows {2,3}), PATIENT mod 5, ACTION mod 7
        return (n % 6, n % 5, n % 7)

    seen = {parts(n) for n in range(D)}
    check("S6a bijective grammar: 210 scenes <-> 6 agents x 5 patients x "
          "7 actions, no syntax overhead", len(seen) == 210)

    fails = 0
    for n in range(D):
        cw = ecc_encode(tuple(n % R.moduli[i] for i in R.data_channels), R)
        for ch in range(R.k):
            for wrong in range(R.moduli[ch]):
                if wrong == cw[ch]:
                    continue
                bad = list(cw); bad[ch] = wrong
                corrected, _ = ecc_correct(tuple(bad), R)
                m = decode_partial(corrected, R, list(R.data_channels))
                if parts(m) != parts(n):
                    fails += 1
    check(f"S6b all 210 scenes x 51 corruptions: snap, then AGENT/PATIENT/"
          f"ACTION all exact ({210*51} cases)", fails == 0)

    fails = 0
    for n in range(D):
        cw = ecc_encode(tuple(n % R.moduli[i] for i in R.data_channels), R)
        for erased in combinations(range(R.k), 3):
            kept = [i for i in range(R.k) if i not in erased]
            if parts(decode_partial(cw, R, kept)) != parts(n):
                fails += 1
    check(f"S6c all 35 triple-erasure patterns x 210 scenes: parts exact "
          f"from any 4 windows (min 4-window product = 210 = scene space)",
          fails == 0)


if __name__ == "__main__":
    import time
    t0 = time.time()
    print("MEANING AS CODEWORD -- the exact VSA")
    s1_bind_unbind()
    s2_hrr_contrast()
    s3_snap_to_whole()
    s4_superposition()
    s5_element_as_operator()
    s6_scene_pipeline()
    print(f"\nALL {CHECKS} CHECKS PASS  ({time.time()-t0:.1f} s)")
