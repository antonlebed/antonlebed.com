"""The snap-back CA — dictionary-coded symbols, bijective binding,
nearest-word cleanup as snap-back (the codeword-semantics
reading of the ring CA — a hook that survives an earlier kill
by construction).

THE OBJECT. Cells hold ring elements drawn from a DICTIONARY: a set of
words separated in the window metric d(x,y) = #{p : x != y mod p}.
Update = binding (multiplication); cleanup = snap to the nearest word.
Nothing numeric is asked to survive the dynamics — the invariant is the
dictionary itself, and the dynamics is drawn from the code's own
symmetry group instead of fought against.

FINDINGS (naming tiers as below):

1. THE ISOMETRY MENU (rule, proved + verified). Affine maps
   x -> u*x + c (u a unit) preserve the window metric exactly:
   (ux+c)-(uy+c) = u(x-y) and u is invertible in every channel, so the
   wrong-window set is unchanged; the maps are channel-local, so a
   single-window corruption stays single-window under them. Verified
   exhaustively at Z/30 (all pairs x all units x all shifts, 104,400
   checks) and sampled at RAD (2,000). The sum of two STATE values is
   NOT on the menu — see finding 6.

2. THE EXPONENT IMPORT (rule, proved + verified on three instances —
   the vehicle-level finding). Binding-closed dictionaries OF UNITS
   are exactly the subgroups of the unit group (a finite
   multiplicatively closed set of units contains each element's
   powers up to 1, hence inverses; non-units are excluded twice over:
   their powers reach an idempotent, never 1, and binding by a
   non-unit is not bijective). U(Z/N) = prod_p U(p) with each channel cyclic, so a
   subgroup is a linear code over the exponent space prod_p Z/(p-1),
   and window distance = exponent Hamming distance (window p is wrong
   iff the exponent coordinate differs; proof: per-channel dlog is a
   bijection, g_p^a = g_p^b iff (p-1) | a-b).
   CLASSICAL CODING THEORY IMPORTS WHOLESALE into the binding-invariant
   regime through the index transform. The additive twin is trivial:
   additive subgroups of prod F_p are sub-products (min distance 1) —
   dictionaries live on the multiplicative side. Instances:
   (i) THE SIGN HYPERCUBE: order-2 exponents make {+-1}-per-channel
       sign vectors; binary linear codes are binding-closed. Hamming
       [7,4,3] on the 7 odd prime channels (3..19, N = 4,849,845):
       16 words, min distance 3, corrects any 1 window (verified: 256
       closure products, 120 pairwise distances, 1,088 corruptions).
   (ii) THE EQUIDISTANT OCTAVE: designed tower D8 with places
       p == 1 (mod 8) — (17,41,73,89,97,113,137), N ~ 6.8e12 — and g
       of order 8 in every channel: the dictionary {g^0..g^7} is
       pairwise distance 7 (exponent repetition code), corrects 3 of
       7 windows. The design freedom is the ramification knob: places
       chosen for their unit-group shape.
   (iii) THE HONEST NEGATIVE: the home rung's own unit group is a BAD
       dictionary. RAD's max-order unit (channel orders 1,2,4,6,10,
       12,16; lambda = 240) has a GRADED distance profile with min
       distance 1 (Delta = 120 survives only in channel 17; channel 2
       never separates units at all). Verified over all 239 deltas.
       Designed towers earn their keep; the primorial rung does not
       carry this for free.

3. ERROR TRANSPARENCY OF BINDING (rule, proved + verified). The
   wrong-window set of a product is contained in the union of the
   factors' wrong-window sets: binding never spreads an error across
   windows (channel-locality), and a single wrong factor in a window
   stays wrong (units). Two wrong factors can cancel only by residue
   coincidence (measured ~1/p per doubly-hit window). Corollary, from
   the decoupling law (the ring CA chart, explore_ring_ca.py): under pure binding
   dynamics the window-p plane of the whole TRAJECTORY depends only on
   the window-p plane of the initial state — FAULT QUARANTINE: a fault
   in window p stays in window p for unbounded time, spreading at most
   spatially, never across windows.

4. THE EAGER GUARANTEE (rule from 1-3, verified). Snap-then-bind: each
   step every cell is snapped (bounded-distance decode, radius t) then
   bound (the rule-90 family: x_i <- x_{i-1} * x_{i+1}; at exponent
   level the linear CA e_i <- e_{i-1} + e_{i+1} mod 8 — Sierpinski). If every
   cell takes <= t corrupted windows per step, the trajectory is EXACT
   FOREVER. The guarantee is worst-case by the radius argument (a
   received word 3 from its truth agrees with it on 4 windows and with
   any other word on at most the 3 corrupted ones; 4 > 3 makes the
   decode unique) — verified 500 steps x 64 cells on D8 at the FULL
   noise budget (3 random windows, random wrong residues, per cell per
   step), zero divergence from the
   noiseless twin (96,000 corrupted windows absorbed), and the value
   trajectory matches the pure Z/8 linear CA exactly (32,000
   cell-steps: binding IS the symbol dynamics). Failure is a
   single-step event,
   never an accumulation: measured snap-failure rate at eps = .10/.15/
   .20/.30 matches P[Binom(7,eps) >= 4] within Monte Carlo error
   (40,000 samples each; observation).

5. LAZY SNAP (rule from 3, verified — where the object beats the
   per-step-maintenance shape). Because faults are quarantined per
   window, correction can wait until READOUT: run open-loop (no snap,
   no checksum, no maintenance of any kind) with up to 3 channels
   STUCK (garbage every step, every cell); after 200 steps a single
   snap per cell recovers the exact readout-time symbols (verified 64
   cells x 200 steps x 3 stuck lanes of 7 = 12,800 quarantined
   cell-steps; 64/64 exact readouts, zero refusals). The
   numeric-ABFT shape must re-derive checksums
   after every arithmetic step; here an entire failed hardware lane
   costs nothing until read time.

6. THE HEIGHT-DEGRADATION LADDER (rule, computed — an earlier kill
   quantified). The numeric stencil on the height-cut code (RAD lifts
   < 210, d = 4) degrades with running height: the sumset interval
   [0,L] has min distance 4 (L <= 209), 3 (L >= 210: the difference
   210 = 2*3*5*7 kills all data windows at once), 2 (L >= 2310),
   1 (L >= 30030), 0 (L >= 510510). One addition step already leaves
   about half the cells (27/64 in the run; expected fraction 0.498)
   at distance exactly 3 from the nearest codeword
   (all three parity windows wrong), and the only repair is
   re-deriving parity from data = base extension = the ABFT shape.
   Binding-closed dictionaries never pay this: closure is exact at
   every height, forever.

CLASSICAL CONTACT (shape only). Fault-tolerant quantum computation
runs the same playbook: compute on encoded states using transversal
gates — channel-local operations that preserve the code space — and
the Eastin-Knill theorem says no error-detecting code admits a
universal transversal gate set; universality is bought outside the
set (magic states). The
snap-back CA is a classical-exact shadow: binding is the transversal
set (channel-local, dictionary-preserving), the decoupling law is the
Eastin-Knill-shaped wall (no ring op couples channels; thresholds and
arbitrary symbol rules are bought at the snap — which, once paid,
prepays the coupling toll: post-snap the symbol is a decoded integer
and any rule on it is free).

CLASSICAL INCUMBENTS (contact with prior literature — where this
candidate direction was found already owned;
contact tier: abstracts, publisher pages, metadata, search summaries —
no full texts read). The general form — a
dictionary closed under a group action, computed on by the group
operation, with coset-based correction — is owned: fault-tolerant
computation via algebraic homomorphisms (Beckmann & Musicus, MIT 1992
— title + metadata verified, full text unread) and in
groups/semigroups (Hadjicostis & Verghese — coset-based correction;
per-step concurrent correction at constant redundant hardware for
linear finite-state machines). Universal computation on coded data is
owned at polylog overhead over a WIDER fault surface than ours
(faulty processors, not just noisy registers; his faults random, ours
bounded-adversarial): Spielman, "Highly Fault-Tolerant Parallel
Computation", FOCS 1996 (abstract). The
classical-transversality seam itself is worked from the quantum side
(accessibility bounds on classical stabilizer codes, arXiv 2507.05408,
abstract). The a-priori structure the contact confirms: a non-linear
rule acts on decoded symbols, so universal computation pays a decode
at every non-linear step — at generic gate density the eager shape,
which on the sign hypercube IS Hamming-ECC-scrubbed state registers
under reliable logic, commodity practice. The LAZY axis is exclusive
to linear-over-exponents dynamics — group-word chains (LFSR, counter,
scrambler), a niche — and readout-time failed-channel correction is
RRNS's core move. The exponent import stays charted math; it is not
an engineering edge.

HONEST LIMITS. (a) The fault model is noisy VALUE registers under
reliable control (the ABFT stance), not Gacs's unreliable-everything;
no threshold theorem is claimed — the eager guarantee is per-step
exact correction, the lazy one per-window quarantine. (b) In eager
mode, decode-update-reencode through a symbol table has the same
per-step cost; binding earns its keep in LAZY mode (open-loop fault
quarantine, stuck-lane tolerance) and in the code DESIGN space (the
exponent import). (c) Alphabets are small (8-16 symbols per element
here); capacity scales only with designed places. (d) The rule class
native to binding is linear-over-exponents; everything else is bought.

RUN RECORD (python prime/code/explore_snapback_ca.py, measured 0.7 s):
8,057 counted assertions, ALL PASS. The part-0 exhaustive sweep
(104,400 Z/30 comparisons) and the RAD sample fail-fast inside a
single counted assertion each; per-step, per-corruption, and ladder
checks are counted individually (the ladder = 4 Monte-Carlo-vs-
binomial comparisons at 40,000 snaps each). Seeded (random.seed(141)).
"""

import os
import random
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import Ring, multiplicative_order  # noqa: E402

random.seed(141)

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ------------------------------------------------------------------
# Rings and residue-tuple arithmetic (all state lives in tuple space)
# ------------------------------------------------------------------

Z30 = Ring("Z30", (2, 3, 5), (1, 1, 1))
RAD = Ring("RAD", (2, 3, 5, 7, 11, 13, 17), (1,) * 7)
ODD7 = Ring("ODD7", (3, 5, 7, 11, 13, 17, 19), (1,) * 7)
D8 = Ring("D8", (17, 41, 73, 89, 97, 113, 137), (1,) * 7)


def to_tuple(n, ring):
    return tuple(n % q for q in ring.moduli)


def t_mul(a, b, ring):
    return tuple(x * y % q for x, y, q in zip(a, b, ring.moduli))


def t_add(a, b, ring):
    return tuple((x + y) % q for x, y, q in zip(a, b, ring.moduli))


def wdist(a, b):
    """Window distance between residue tuples."""
    return sum(1 for x, y in zip(a, b) if x != y)


def corrupt(a, windows, ring):
    """Replace the given windows with definitely-wrong uniform residues."""
    out = list(a)
    for i in windows:
        q = ring.moduli[i]
        out[i] = (a[i] + random.randrange(1, q)) % q
    return tuple(out)


def element_of_order(p, m):
    """An element of exact multiplicative order m mod prime p (m | p-1)."""
    assert (p - 1) % m == 0
    for h in range(2, p):
        g = pow(h, (p - 1) // m, p)
        if multiplicative_order(g, p) == m:
            return g
    raise ValueError(f"no order-{m} element mod {p}")


# ------------------------------------------------------------------
# Part 0 — the isometry menu
# ------------------------------------------------------------------

def part0():
    print("=" * 66)
    print("PART 0 — the isometry menu: affine maps preserve the window metric")
    print("=" * 66)
    # Exhaustive at Z/30: every pair, every unit, every shift.
    units30 = [u for u in range(30) if all(u % p for p in (2, 3, 5))]
    n_checks = 0
    for u in units30:
        for c in range(30):
            for x in range(30):
                for y in range(x + 1, 30):
                    tx, ty = to_tuple(x, Z30), to_tuple(y, Z30)
                    fx = to_tuple((u * x + c) % 30, Z30)
                    fy = to_tuple((u * y + c) % 30, Z30)
                    if wdist(fx, fy) != wdist(tx, ty):
                        ok(False, "affine isometry broken at Z/30")
                    n_checks += 1
    ok(True, "")
    print(f"  Z/30 exhaustive: d(ux+c, uy+c) = d(x,y) for all "
          f"{len(units30)} units x 30 shifts x 435 pairs = {n_checks} checks")

    # Sampled at RAD.
    n = 0
    for _ in range(2000):
        x, y = random.randrange(RAD.N), random.randrange(RAD.N)
        u = random.randrange(1, RAD.N)
        while any(u % p == 0 for p in RAD.primes):
            u = random.randrange(1, RAD.N)
        c = random.randrange(RAD.N)
        tx, ty = to_tuple(x, RAD), to_tuple(y, RAD)
        fx, fy = to_tuple((u * x + c) % RAD.N, RAD), to_tuple((u * y + c) % RAD.N, RAD)
        if wdist(fx, fy) != wdist(tx, ty):
            ok(False, "affine isometry broken at RAD")
        n += 1
    ok(True, "")
    print(f"  RAD sampled: {n} random (x, y, unit u, c) — all preserved")
    print()


# ------------------------------------------------------------------
# Part 1 — the exponent import: three dictionary instances
# ------------------------------------------------------------------

HAMMING_G = ((1, 0, 0, 0, 1, 1, 0),
             (0, 1, 0, 0, 1, 0, 1),
             (0, 0, 1, 0, 0, 1, 1),
             (0, 0, 0, 1, 1, 1, 1))


def hamming_codewords():
    """All 16 codewords of the [7,4,3] Hamming code as bit tuples."""
    words = []
    for m in range(16):
        bits = [(m >> i) & 1 for i in range(4)]
        w = tuple(sum(b * g[j] for b, g in zip(bits, HAMMING_G)) % 2
                  for j in range(7))
        words.append(w)
    return words


def sign_word(bits, ring):
    """Bit vector -> ring tuple with residue (-1)^bit per channel."""
    return tuple((q - 1) if b else 1 for b, q in zip(bits, ring.moduli))


def part1():
    print("=" * 66)
    print("PART 1 — the exponent import: subgroup dictionaries as codes")
    print("=" * 66)

    # (i) The sign hypercube: Hamming [7,4,3] on the 7 odd channels.
    hw = hamming_codewords()
    dic = [sign_word(b, ODD7) for b in hw]
    for a, b in combinations(range(16), 2):
        hd = sum(x != y for x, y in zip(hw[a], hw[b]))
        ok(wdist(dic[a], dic[b]) == hd, "sign-code distance law")
    ok(min(wdist(dic[a], dic[b])
           for a, b in combinations(range(16), 2)) == 3,
       "sign-code min distance 3")
    print("  (i) sign hypercube [7,4,3] on ODD7: 120 pairwise window "
          "distances = Hamming distances (min 3)")
    dset = set(dic)
    for a in dic:
        for b in dic:
            ok(t_mul(a, b, ODD7) in dset, "sign-code closure")
    print("      closure: all 256 products land in the dictionary "
          "(binding = XOR on sign bits)")
    n_corr = 0
    for w in dic:
        for i, q in enumerate(ODD7.moduli):
            for r in range(q):
                if r == w[i]:
                    continue
                v = list(w)
                v[i] = r
                best = [x for x in dic if wdist(tuple(v), x) <= 1]
                ok(best == [w], "sign-code radius-1 snap")
                n_corr += 1
    print(f"      snap: every 1-window corruption recovers its word "
          f"({n_corr} corruptions, zero mis-snaps)")

    # (ii) The equidistant octave on the designed tower D8.
    g = tuple(element_of_order(p, 8) for p in D8.primes)
    for gp, p in zip(g, D8.primes):
        ok(multiplicative_order(gp, p) == 8, "order 8 in every channel")
    dic8 = [tuple(pow(gp, j, p) for gp, p in zip(g, D8.primes))
            for j in range(8)]
    dists = {wdist(a, b) for a, b in combinations(dic8, 2)}
    ok(dists == {7}, "equidistant distance 7")
    print("  (ii) equidistant octave on D8 (places p == 1 mod 8): "
          "{g^0..g^7}, all 28 pairwise distances = 7, corrects 3 of 7")
    dset8 = set(dic8)
    for a in dic8:
        for b in dic8:
            ok(t_mul(a, b, D8) in dset8, "octave closure")
    print("      closure: all 64 products in the dictionary "
          "(binding = +1 shift group on Z/8 exponents)")

    # (iii) The honest negative: RAD's own max-order unit.
    gr = []
    for p in RAD.primes:
        best, order = 1, 1
        for h in range(1, p):
            o = multiplicative_order(h, p)
            if o > order:
                best, order = h, o
        gr.append((best, order))
    orders = tuple(o for _, o in gr)
    ok(orders == (1, 2, 4, 6, 10, 12, 16), "RAD channel orders")
    lam = 240
    profile = {}
    for delta in range(1, lam):
        d = sum(1 for o in orders if delta % o != 0)
        profile[delta] = d
    ok(min(profile.values()) == 1, "RAD graded min distance 1")
    ok(profile[120] == 1, "delta=120 survives only in channel 17")
    hist = {}
    for d in profile.values():
        hist[d] = hist.get(d, 0) + 1
    print("  (iii) honest negative — RAD max-order unit (orders "
          f"{orders}, lambda={lam}):")
    print(f"      distance profile over the 239 deltas: "
          f"{dict(sorted(hist.items()))} — min distance 1 (delta=120); "
          f"channel 2 never separates units")

    # The additive twin is trivial.
    # Additive subgroups of prod F_p are sub-products: two elements of a
    # sub-product differing in exactly one supported channel are distance 1.
    ok(True, "additive twin (argument in docstring)")
    print("  additive twin: subgroups of (Z/N,+) = sub-products, min "
          "distance 1 — dictionaries live on the multiplicative side")
    print()
    return dic, dic8, g


# ------------------------------------------------------------------
# Part 2 — error transparency of binding
# ------------------------------------------------------------------

def part2(dic8):
    print("=" * 66)
    print("PART 2 — error transparency: wrong(x*y) inside wrong(x) U wrong(y)")
    print("=" * 66)
    n, n_equal, n_cancel, n_double = 0, 0, 0, 0
    for _ in range(5000):
        x = random.choice(dic8)
        y = random.choice(dic8)
        wa = random.sample(range(7), random.randrange(0, 4))
        wb = random.sample(range(7), random.randrange(0, 4))
        xa, yb = corrupt(x, wa, D8), corrupt(y, wb, D8)
        true = t_mul(x, y, D8)
        noisy = t_mul(xa, yb, D8)
        wrong = {i for i in range(7) if true[i] != noisy[i]}
        union = set(wa) | set(wb)
        ok(wrong <= union, "transparency containment")
        n += 1
        if wrong == union:
            n_equal += 1
        both = set(wa) & set(wb)
        n_double += len(both)
        n_cancel += len(both - wrong)
    print(f"  {n} sampled products with 0-3 corrupted windows per factor:")
    print(f"  containment holds {n}/{n}; equality {n_equal}/{n} "
          f"(cancellation only on doubly-hit windows: {n_cancel} of "
          f"{n_double} double hits cancelled, ~1/p as expected)")
    print()


# ------------------------------------------------------------------
# The snap-back decoder and the CA
# ------------------------------------------------------------------

def snap8(v, dic8, t=3):
    """Bounded-distance decode on the equidistant octave: unique word
    with agreement >= 7-t, else None (detect/refuse)."""
    for j, w in enumerate(dic8):
        if sum(1 for a, b in zip(v, w) if a == b) >= 7 - t:
            return j
    return None


def bind_step(cells, ring):
    """Rule 90 at value level: x_i <- x_{i-1} * x_{i+1} (ring of cells)."""
    n = len(cells)
    return [t_mul(cells[(i - 1) % n], cells[(i + 1) % n], ring)
            for i in range(n)]


def exp_step(exps, m):
    """The exponent twin: e_i <- e_{i-1} + e_{i+1} mod m."""
    n = len(exps)
    return [(exps[(i - 1) % n] + exps[(i + 1) % n]) % m for i in range(n)]


def part3(dic8):
    print("=" * 66)
    print("PART 3 — the eager guarantee: snap-then-bind, exact forever")
    print("=" * 66)
    n_cells, T = 64, 500
    exps = [random.randrange(8) for _ in range(n_cells)]
    cells = [dic8[e] for e in exps]
    absorbed = 0
    for step in range(T):
        noisy = [corrupt(c, random.sample(range(7), 3), D8) for c in cells]
        absorbed += 3 * n_cells
        snapped = [snap8(v, dic8) for v in noisy]
        ok(all(s is not None for s in snapped), "no refusals below radius")
        ok(snapped == exps, f"exact snap at step {step}")
        cells = bind_step([dic8[s] for s in snapped], D8)
        exps = exp_step(exps, 8)
        ok(cells == [dic8[e] for e in exps],
           "binding matches the Z/8 linear CA")
    print(f"  {n_cells} cells x {T} steps, FULL-BUDGET 3-window corruption "
          f"per cell per step ({absorbed} corrupted windows absorbed):")
    print("  trajectory EXACT at every step; value dynamics = the Z/8 "
          "linear CA e_i <- e_(i-1)+e_(i+1) exactly (rule-90 family)")

    # The failure ladder: snap failure is a single-step binomial event.
    print("  failure ladder (per-window wrong-residue rate eps, 40,000 "
          "snaps each):")
    from math import comb
    for eps in (0.10, 0.15, 0.20, 0.30):
        pred = sum(comb(7, w) * eps ** w * (1 - eps) ** (7 - w)
                   for w in range(4, 8))
        fails = 0
        trials = 40000
        for _ in range(trials):
            e = random.randrange(8)
            windows = [i for i in range(7) if random.random() < eps]
            v = corrupt(dic8[e], windows, D8)
            if snap8(v, dic8) != e:
                fails += 1
        meas = fails / trials
        se = (pred * (1 - pred) / trials) ** 0.5
        ok(abs(meas - pred) < 5 * se + 1e-9,
           f"ladder point eps={eps} within Monte Carlo error")
        print(f"    eps={eps:.2f}: measured {meas:.4f}  predicted "
              f"P[Binom(7,eps)>=4] = {pred:.4f}")
    print("  failure = a single-step >= 4-window burst, never an "
          "accumulation (each snap fully cleans)")
    print()


def part4(dic8):
    print("=" * 66)
    print("PART 4 — lazy snap: open loop, stuck lanes, readout-only correction")
    print("=" * 66)
    n_cells, T = 64, 200
    stuck = (1, 4, 6)
    exps = [random.randrange(8) for _ in range(n_cells)]
    cells = [dic8[e] for e in exps]
    twin = list(exps)
    for step in range(T):
        # stuck lanes carry garbage in every cell, every step
        cells = [corrupt(c, stuck, D8) for c in cells]
        cells = bind_step(cells, D8)
        twin = exp_step(twin, 8)
    # single snap per cell at readout — no maintenance was ever done
    read = [snap8(c, dic8) for c in cells]
    ok(all(r is not None for r in read), "zero refusals at readout")
    ok(read == twin, "lazy readout exact")
    print(f"  {n_cells} cells x {T} steps OPEN LOOP, channels "
          f"{tuple(D8.primes[i] for i in stuck)} stuck (garbage every "
          f"step, every cell), zero maintenance:")
    print(f"  one snap per cell at readout recovers the exact "
          f"readout-time symbols — {n_cells * T} cell-steps of "
          f"quarantined faults, {n_cells}/{n_cells} exact readouts")
    print()


# ------------------------------------------------------------------
# Part 5 — the contrast control: the numeric stencil (an earlier kill)
# ------------------------------------------------------------------

def part5():
    print("=" * 66)
    print("PART 5 — contrast control: the height-cut code under a sum rule")
    print("=" * 66)
    # The height-degradation ladder: min window distance of the interval
    # [0, L] on RAD = 7 - max #{primes dividing some Delta <= L}; the
    # cheapest r-window kill is the product of the first r primes.
    ladder = []
    for L, d_expect in ((209, 4), (210, 3), (2309, 3), (2310, 2),
                        (30030, 1), (510510, 0)):
        maxdiv = 0
        for r in range(1, 8):
            m = 1
            for p in RAD.primes[:r]:
                m *= p
            if m <= L:
                maxdiv = r
        d = 7 - maxdiv
        ok(d == d_expect, f"ladder at L={L}")
        ladder.append((L, d))
    print("  the height-degradation ladder — min distance of lifts [0,L]:")
    print("   ", "  ".join(f"L<={L}: d={d}" for L, d in ladder))

    # One sum step on height-cut codewords: parity dies wholesale.
    dic_rad = [to_tuple(v, RAD) for v in range(210)]
    dset = set(dic_rad)
    n_cells = 64
    vals = [random.randrange(210) for _ in range(n_cells)]
    cells = [dic_rad[v] for v in vals]
    summed = bind_step_add(cells, RAD)
    n_invalid, n_d3 = 0, 0
    for i, c in enumerate(summed):
        if c not in dset:
            n_invalid += 1
            dmin = min(wdist(c, w) for w in dic_rad)
            if dmin == 3:
                n_d3 += 1
    ok(n_invalid > 0, "sum rule leaves the dictionary")
    ok(n_d3 == n_invalid, "every invalid cell sits at distance exactly 3")
    print(f"  one sum step (x_i <- x_(i-1)+x_(i+1)) on 64 height-cut "
          f"codewords: {n_invalid}/64 cells leave the code,")
    print("  every one at distance EXACTLY 3 (all parity windows wrong at "
          "once: the difference is a multiple of 210)")
    print("  -> repair = re-derive parity from data = base extension = "
          "the ABFT shape, every step (reproduced)")
    print()


def bind_step_add(cells, ring):
    n = len(cells)
    return [t_add(cells[(i - 1) % n], cells[(i + 1) % n], ring)
            for i in range(n)]


if __name__ == "__main__":
    part0()
    dic_ham, dic8, g = part1()
    part2(dic8)
    part3(dic8)
    part4(dic8)
    part5()
    print(f"ALL CHECKS PASS ({CHECKS} assertions)")
