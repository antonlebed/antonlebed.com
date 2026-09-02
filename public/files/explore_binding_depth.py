"""Exact vs approximate unbinding at composition depth: is there a scaling edge?

QUESTION
--------
Vector-symbolic architectures (VSA / hyperdimensional computing) bind a role to a
filler and later unbind to recover it. In Holographic Reduced Representations (HRR,
Plate 1995/2003) binding is circular convolution and unbinding is circular
correlation, which for the usual random atoms is only APPROXIMATE: a single unbind
returns the filler at cosine well below 1, so retrieval needs a cleanup memory that
can fail (unitary atoms restore an exact per-level inverse -- see G1c). An exact
substrate (unbind = a true multiplicative inverse) returns the filler at cosine 1
at every depth. The question for scaling: does approximate unbinding's degradation
with COMPOSITION DEPTH give an exact substrate an advantage that changes the SCALING
CURVE (register size or accuracy vs depth), not merely a constant factor -- and does
it survive a fair fight against the incumbent at table stakes?

INCUMBENT CONTACT (full text, at design time)
---------------------------------------------
- Plate, "Holographic Reduced Representations" (IEEE TNN 1995; book 2003): circular
  convolution binding, correlation (approximate-inverse) unbinding; the recovered
  vector is the filler plus noise whose scale falls with dimension, so retrieval is
  probabilistic and leans on a cleanup codebook.
- Kent, Frady, Sommer, Olshausen, "Resonator Networks 2: factorization performance
  and capacity" (Neural Computation 2020; arXiv 1906.11684): the state of the art
  for factoring a product of several bound code vectors. Operational capacity --
  the largest search space (product of codebook sizes) solvable at >=99% accuracy --
  scales as M_max ~ N^2 in the vector dimension N, measured for factor counts 2..7.
  Beyond that operating point accuracy collapses from 1.0 to near zero. The analysis
  rests explicitly on quasi-orthogonality: random +/-1 vectors in large N are "very
  nearly orthogonal" (concentration of measure). So resolving F factors of codebook
  size M needs N >~ M^(F/2): dimension GROWS EXPONENTIALLY in the number of factors,
  and the resource that makes superposed items separable is concentration of measure
  in high dimension -- a metric (archimedean) resource.

The exact substrate under study deletes exactly that metric resource: its channels
are distinct prime residues with no notion of near-orthogonality or averaging.
Exact unbinding on it is a multiplicative inverse in the unit group of a fixed
modulus (see explore_meaning_codeword.py for the codeword/VSA record). So the fair
question is whether "exact at every depth" buys a real scaling win, or whether the
places where it wins are places the incumbent never needed to be, and the places the
incumbent is used are powered by the very resource the exact substrate lacks.

DESIGN
------
HRR over R^D. An atom is a random unit vector. Bind is real circular convolution
(via FFT); unbind is circular correlation (convolution with the involution). A
codebook holds M atoms; cleanup is nearest atom by cosine.

G1 -- the RANDOM-atom depth limit (the naive/strawman incumbent; G1c below measures the
good one, which fixes it). Build a depth-d composite c = k_1 * k_2 * ... * k_d * x (all
convolutions; k_i keys, x the deep filler, all drawn from the codebook). Recover x by
unbinding every key in turn --
no cleanup is possible mid-chain because the intermediate products are not codebook
atoms. Sweep depth d and dimension D in {256, 512, 1024, 2048}; record d*, the
largest depth at which nearest-atom cleanup of the recovered vector still returns x
at >= 99% over trials.

G1b -- the incumbent's real capacity axis (superposition), added mid-run when G1's
pure-chain framing proved to be the wrong wall. Bundle m bound (role, filler) pairs into
one vector, query with one role, clean up the filler; sweep m at each D, record m*, the
largest m retrieved at >= 95% over trials.

G1c -- the GOOD incumbent at pure-chain depth (added in review, to measure the claim G1
only asserted). Same pure chain, but with UNITARY atoms (|FFT| = 1 at every bin), Plate's
fix: the involution is now an EXACT inverse, so unbinding is noise-free. Depth up to 200
at fixed D; report the worst-case cosine of the recovered filler.

G2 -- the exact substrate (fixed register, any depth). The same protocol with exact
arithmetic: atoms are units of a fixed modulus N (the primorial ring Z/510510), bind
is multiplication mod N, unbind is multiplication by the modular inverse. Recover x
from c = x * prod(keys) mod N at depths up to 1000.

G3 -- the fair fight (what the exact win costs). Corrupt a fraction rho of the stored
composite and recover. HRR: additive Gaussian corruption of the D coordinates. Exact:
flip digits of the integer's mixed-radix (CRT) representation. Record rho*, the
largest corruption at which recovery still succeeds at >= 90% over trials.

PREDICTIONS (fixed before the run)
----------------------------------
G1  d*(D) increases monotonically and roughly LINEARLY with D (mechanism: d unbinds
    accumulate independent noise, variance ~ d/D, cleanup fails near d* ~ D / (2 ln M));
    doubling D roughly doubles d*. So the HRR register must grow linearly with depth.
    Positive control: at d = 1 the recovered cosine is already < 1 (an approximate
    incumbent, not exact by accident).
G1b (frozen pre-run in the working notes, git; recorded here in review) superposition
    capacity m* grows ~LINEARLY with D, m*(2D) ~ 2 m*(D) (Frady SNR = sqrt(D/m)) -- the
    incumbent's capacity is a concentration-of-measure resource. [Outcome in findings:
    direction confirmed, but growth SUB-LINEAR at these finite sizes -- a partial miss.]
G1c (frozen before its run, added in review) the UNITARY incumbent recovers the filler at
    cosine ~ 1 (> 0.99) even at depth 200, at FIXED D -- because |FFT| = 1 makes the
    per-level inverse exact. So the GOOD incumbent already carries pure-chain depth at a
    fixed register; the exact substrate's edge on this axis is therefore NIL, not even a
    constant. (This measures what G1's finding argued from the Plate contact.)
G2  exact recovery is correct at EVERY tested depth up to 1000 at a FIXED register
    size (one integer < N), O(d) multiplies -- register size constant in depth.
G3  HRR tolerates a positive corruption fraction: rho* > 0 (graceful degradation from
    concentration of measure). Exact recovery is catastrophic: rho* = 0 (any single
    digit flip yields the wrong atom, no basin). The exact substrate's fixed-register,
    any-depth recall is bought by surrendering the noise robustness that is the
    incumbent's reason to exist -- so against a fair incumbent (plain modular
    arithmetic, a struct, a hash table) it is table stakes, not a scaling edge.

FINDINGS (tier: observation + argument; the scaling claims cite full-text sources)
----------------------------------------------------------------------------------
The verdict is NEGATIVE: exact unbinding buys no defensible scaling advantage over
approximate VSA at composition depth. The advantage is NIL for pure-chain depth (unitary
atoms carry it free, G1c), a CONSTANT factor where per-level cleanup is needed (known
codebook), and TABLE-STAKES where intermediates are novel (no codebook, G2) -- never a
change in the scaling curve.

G1 -- prediction MISSED, recorded. With random (non-unitary) atoms a pure unbind chain
dies at depth 1 for every dimension D in {256, 512, 1024, 2048}; the single-unbind cosine
is ~0.71 at every D (measured 0.708-0.714) -- the approximate-inverse noise floor for a
random atom (SNR ~ 1, so cos ~ 1/sqrt(2)), a distinct mechanism from the m=2 bundling
identity that happens to share the value (there is no superposition at depth 1). The frozen
prediction d* ~ D was wrong: the approximate-inverse noise of a random atom is O(1) per
level (its power spectrum is non-flat), not O(1/D), so depth does not grow with D. The
error was importing the superposition capacity law (variance ~ 1/D) into the pure-chain
setting, which has a different, unitarity-gated noise source. The depth-carrying incumbent
uses unitary atoms (Plate's noise-free per-level inverse) or per-level cleanup -- neither
is a dimension scaling.

G1b -- direction confirmed, rate sub-linear at these sizes. Superposition capacity
m* (max bundled pairs retrieved at >=95%) = 10, 14, 18, 25 at D = 256, 512, 1024, 2048:
monotone growth with dimension. The measured m*/D falls (0.039 -> 0.012), so growth is
sub-linear at these finite sizes; the asymptotic law is linear (Frady's SNR = sqrt(D/m)).
Either way the incumbent's capacity is a DIMENSION-DRIVEN concentration-of-measure
resource -- the archimedean resource the primorial ring deletes by construction (distinct
prime channels, no near-orthogonality, no averaging).

G1c -- confirmed, and it sharpens the negative verdict. With UNITARY atoms the recovered filler
stays at cosine 1.0000 through depth 200 at fixed D = 1024: |FFT| = 1 makes the per-level
inverse EXACT, so the good incumbent carries pure-chain depth for free, in a fixed
register. So pure composition depth was never the real approximate-VSA wall (G1's
random-atom death is a strawman the incumbent fixes with unitary vectors); the exact
substrate's edge on the pure-chain-depth axis is NIL, not even a constant. The genuine
walls are elsewhere -- SUPERPOSITION (G1b, concentration-limited) and NOVEL intermediates
(G2, no cleanup) -- and neither yields the exact substrate a scaling win (below).

G2 -- confirmed. Exact recovery of a codeword filler through a product of up to 1000
non-codebook keys is correct at every depth, in a FIXED 19-bit register (Z/510510). So an
exact multiplicative inverse carries NOVEL intermediates (the partial products, which are
not codebook atoms) to unbounded depth at constant register size. This is the DISCRETE
version of approximate VSA's one true depth wall -- continuous Spatial Semantic Pointers /
fractional power encoding have no cleanup and lose the value after about two composition
steps -- but clearing it is ordinary modular arithmetic, and the ring does NOT address the
CONTINUOUS-value regime those methods exist for, so it is no win over them, only a
restatement that exact discrete arithmetic is exact.

G3 -- confirmed. HRR recovers a bound pair under 50% coordinate corruption (graceful
degradation, rho* = 0.50); the exact substrate fails at the first flipped residue digit
(rho* = 0.00, no basin). The exact substrate's fixed-register, any-depth exactness is
bought by surrendering the corruption tolerance that is the incumbent's entire reason to
exist -- a concentration-of-measure property no ring channel can supply.

THE PRUNING LEMMA (the load-bearing synthesis). Exactness cannot beat approximation on any
axis whose approximate method is rescued by concentration of measure (superposition
capacity, near-orthogonality, factoring by crosstalk-limited search). Every approximate-VSA
capacity limit contacted below traces to that metric resource, and the primorial ring
deletes precisely that place. So on VSA's home axes the ring is structurally handicapped;
and on the one axis where the metric rescue is unavailable -- carrying NOVEL intermediates
to depth (G2) -- the exact substrate's win reduces to "use exact arithmetic," which is
table-stakes against a plain modular register, a struct, or a hash table, and forfeits the
robustness (G3) that motivates VSA in the first place. By the fair-fight principle (an edge
counts only if it survives the rival substrate emulating it at table stakes), this
direction does not yield a scaling advantage. See explore_meaning_codeword.py for the exact
binding/unbinding record on the ring.

INCUMBENT CONTACT (full text, at design and mint time)
- Plate, HRR (IEEE TNN 1995; thesis 1994 App. C-E): retrieval SNR = sqrt(D/m); the
  community "0.71" has TWO roots -- the m=2 bundling identity cos = 1/sqrt(m) and the
  single-unbind approximate-inverse SNR ~ 1 (G1 here measures the latter); pure nested
  chains need unitary vectors to avoid per-level noise; recursive decode needs an
  auto-associative cleanup over the full item set.
- Kent, Frady, Sommer, Olshausen, Resonator Networks 2 (Neural Computation 2020, arXiv
  1906.11684): operational capacity M_max ~ N^2 (quadratic in dimension, peak at 3 factors),
  accuracy collapses beyond the operating point; the analysis rests on quasi-orthogonality.
- Frady, Kleyko, Sommer 2018; Gallant, Okaywe 2013; Thomas, Dasgupta, Rosing 2021: bundling
  capacity is extensive (a fixed number of bits per dimension), driven by concentration of
  measure (near-orthogonality, CLT crosstalk, Johnson-Lindenstrauss).
- Kleyko et al. survey 2022; Gayler 2003: per-level cleanup resets noise but REQUIRES the
  intermediate to be a member of a finite known codebook; novel composites are the open gap.
- Spatial Semantic Pointers / fractional power encoding (arXiv 2412.00488, full HTML): no
  cleanup mechanism ("the uncorrupted vectors occupy a manifold, not a point"); the value is
  unrecoverable after about two composition steps -- the one genuine depth-scaling wall.
- A SPOTTED, UNREAD lead in the exact-residue direction: a vector-symbolic Lisp with
  residue (CRT) arithmetic (arXiv 2511.08767, TITLE ONLY -- not fetched). It suggests
  prior work on the tower's own exact-residue angle; contact full-text before any reopen.
  It does NOT establish "no edge" (unread), and it is not load-bearing for the verdict --
  the negative verdict rests on the pruning lemma + the fair-fight measurements (G1b, G2, G3).

RUN RECORD
8 checks, ~3 s, < 512 MB, fixed seeds. G1 prediction missed (per-level noise O(1) for
random atoms) -- recorded, the true D-independent fact asserted. G1b direction confirmed,
growth sub-linear at these finite sizes (partial). G1c (added in review to measure the
good incumbent) confirmed first run: unitary depth-200 cosine 1.0000. G2, G3 confirmed
first run. Positive controls: cos(d=1) = 0.71 (an approximate incumbent, not exact by
accident); exact rho* = 0 (no error-correcting basin without added parity). Findings
entered post-run by a separate edit from the printed output.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np

from crt import Ring


# ---------------------------------------------------------------- HRR primitives
def make_codebook(M, D, rng):
    V = rng.standard_normal((M, D))
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    return V


def make_unitary_codebook(M, D, rng):
    # unit-magnitude spectrum: |FFT| = 1 at every bin, so v * involution(v) = delta
    # exactly -- circular convolution is a rotation and unbinding is a NOISE-FREE inverse
    # (Plate's fix for deep structures). Unit time-domain norm by Parseval.
    nb = D // 2 + 1
    V = np.empty((M, D))
    for i in range(M):
        phase = rng.uniform(-np.pi, np.pi, size=nb)
        phase[0] = 0.0                       # DC real
        if D % 2 == 0:
            phase[-1] = 0.0                  # Nyquist real
        V[i] = np.fft.irfft(np.exp(1j * phase), n=D)
    return V


def bind(a, b):
    # real circular convolution
    return np.fft.irfft(np.fft.rfft(a) * np.fft.rfft(b), n=a.shape[-1])


def unbind(c, a):
    # circular correlation = convolution with the involution a[-i]
    inv = a[(-np.arange(a.shape[-1])) % a.shape[-1]]
    return bind(c, inv)


def cosine(u, v):
    return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))


def cleanup_ok(r, codebook, true_idx):
    sims = codebook @ r
    return int(np.argmax(sims)) == true_idx


# --------------------------------------------------------- G1: HRR depth limit
def g1_depth_limit(D, M=256, depths=None, trials=40, seed=0):
    rng = np.random.default_rng(seed + D)
    cb = make_codebook(M, D, rng)
    if depths is None:
        # sweep past the predicted cliff d* ~ D / (2 ln M); cap to bound runtime
        top = min(4 * D // 3, 500)
        depths = list(range(1, top, max(1, D // 64)))
    d_star = 0
    d1_cos = None
    for d in depths:
        ok = 0
        cos_acc = 0.0
        for _ in range(trials):
            idx = rng.integers(0, M, size=d + 1)  # d keys + filler
            keys, xi = idx[:-1], idx[-1]
            c = cb[xi].copy()
            for k in keys:
                c = bind(c, cb[k])
            r = c
            for k in keys:
                r = unbind(r, cb[k])
            cos_acc += cosine(r, cb[xi])
            ok += cleanup_ok(r, cb, xi)
        rate = ok / trials
        if d == 1:
            d1_cos = cos_acc / trials
        if rate >= 0.99:
            d_star = d
        elif d_star:
            break
    return d_star, d1_cos


# --------------------------------- G1b: HRR superposition capacity (m* ~ D)
def g1b_capacity(D, M=512, trials=120, thresh=0.95, seed=1):
    rng = np.random.default_rng(seed + D)
    cb = make_codebook(M, D, rng)
    m_star = 0
    for m in range(1, 90):                         # uniform fine grid across all D
        ok = 0
        for _ in range(trials):
            idx = rng.integers(0, M, size=(m, 2))  # (role, filler) pairs
            bundle = np.zeros(D)
            for role, fill in idx:
                bundle += bind(cb[role], cb[fill])
            role0, fill0 = idx[0]
            r = unbind(bundle, cb[role0])          # query with the first role
            ok += cleanup_ok(r, cb, int(fill0))
        if ok / trials >= thresh:
            m_star = m
        elif m_star:
            break
    return m_star


# ------------------- G1c: UNITARY HRR carries pure-chain depth at fixed register
def g1c_unitary_depth(D=1024, M=256, max_depth=200, trials=20, seed=2):
    rng = np.random.default_rng(seed)
    cb = make_unitary_codebook(M, D, rng)
    min_cos = 1.0
    for _ in range(trials):
        idx = rng.integers(0, M, size=max_depth + 1)
        keys, xi = idx[:-1], idx[-1]
        c = cb[xi].copy()
        for k in keys:
            c = bind(c, cb[k])
        r = c
        for k in keys:
            r = unbind(r, cb[k])
        min_cos = min(min_cos, cosine(r, cb[int(xi)]))
    return min_cos


# ------------------------------------------------- G2: exact substrate, fixed N
def g2_exact(max_depth=1000, M=256, seed=0):
    ps = [2, 3, 5, 7, 11, 13, 17]  # Z/510510, the primorial ring RAD
    ring = Ring("RAD", ps, [1] * len(ps))
    N = ring.N
    rng = np.random.default_rng(seed)
    # a codebook of units of Z/N
    units = []
    while len(units) < M + 1 + max_depth:
        cand = int(rng.integers(2, N))
        if np.gcd(cand, N) == 1:
            units.append(cand)
    filler = units[0]
    all_ok = True
    reg_bits = N.bit_length()  # register size, constant in depth
    for d in range(1, max_depth + 1):
        keys = units[1:1 + d]
        prod = 1
        for k in keys:
            prod = (prod * k) % N
        c = (filler * prod) % N
        inv = pow(prod, -1, N)
        x_hat = (c * inv) % N
        if x_hat != filler:
            all_ok = False
            break
    return all_ok, reg_bits, N


# ------------------------------------------- G3: robustness (the fair fight)
def g3_robustness(D=1024, M=256, depth=1, rhos=None, trials=60, seed=0):
    rng = np.random.default_rng(seed)
    if rhos is None:
        rhos = [0.0, 0.02, 0.05, 0.1, 0.2, 0.35, 0.5]
    cb = make_codebook(M, D, rng)
    hrr_rho_star = 0.0
    for rho in rhos:
        ok = 0
        for _ in range(trials):
            idx = rng.integers(0, M, size=depth + 1)
            keys, xi = idx[:-1], idx[-1]
            c = cb[xi].copy()
            for k in keys:
                c = bind(c, cb[k])
            # corrupt a fraction rho of coordinates with same-scale Gaussian noise
            mask = rng.random(D) < rho
            c = c.copy()
            c[mask] += rng.standard_normal(int(mask.sum())) * (np.std(c) if D else 1.0)
            r = c
            for k in keys:
                r = unbind(r, cb[k])
            ok += cleanup_ok(r, cb, xi)
        if ok / trials >= 0.90:
            hrr_rho_star = rho

    # exact: flip mixed-radix (CRT) digits of the integer composite
    ps = [2, 3, 5, 7, 11, 13, 17]
    ring = Ring("RAD", ps, [1] * len(ps))
    N = ring.N
    primes = ring.primes
    units, filler = [], None
    while len(units) < depth + 1:
        cand = int(rng.integers(2, N))
        if np.gcd(cand, N) == 1:
            units.append(cand)
    filler, keys = units[0], units[1:]
    prod = 1
    for k in keys:
        prod = (prod * k) % N
    c = (filler * prod) % N
    exact_rho_star = 0.0
    for rho in rhos:
        if rho == 0.0:
            continue
        ok = 0
        for _ in range(trials):
            res = [c % p for p in primes]  # CRT digits
            nflip = max(1, int(round(rho * len(primes))))
            flip = rng.choice(len(primes), size=nflip, replace=False)
            for j in flip:
                res[j] = (res[j] + 1 + int(rng.integers(0, primes[j] - 1))) % primes[j]
            c_bad = _crt(res, primes)  # reconstruct the corrupted composite
            inv = pow(prod, -1, N)
            x_hat = (c_bad * inv) % N
            ok += (x_hat == filler)
        if ok / trials >= 0.90:
            exact_rho_star = rho
    return hrr_rho_star, exact_rho_star


def _crt(residues, primes):
    N = 1
    for p in primes:
        N *= p
    x = 0
    for p, r in zip(primes, residues):
        Ni = N // p
        x = (x + r * Ni * pow(Ni, -1, p)) % N
    return x


# ------------------------------------------------------------------------ main
def main():
    checks = 0

    print("=" * 68)
    print("G1  pure-unbind chain, random atoms -- the approximate incumbent")
    print("-" * 68)
    Ds = [256, 512, 1024, 2048]
    d_stars = []
    d1_cos_last = None
    for D in Ds:
        d_star, d1_cos = g1_depth_limit(D)
        d_stars.append(d_star)
        d1_cos_last = d1_cos
        print(f"  D={D:5d}   d* (max reliable depth) = {d_star:4d}   cos(d=1) = {d1_cos:.3f}")
    # FROZEN PREDICTION G1 (d* proportional to D) MISSED. With random (non-unitary)
    # atoms the approximate-inverse noise is O(1) per level, not O(1/D): a pure unbind
    # chain dies at depth ~1 for every D. Recorded as a miss; the true, D-independent
    # fact is asserted here. The depth-carrying incumbent needs unitary atoms (Plate's
    # noise-free per-level inverse) or per-level cleanup -- neither is a D-scaling.
    assert max(d_stars) <= 3, d_stars          # depth dies immediately, D-independent
    checks += 1
    assert d1_cos_last < 0.999, d1_cos_last    # positive control: approximate (cos ~ 0.71)
    checks += 1
    print("  -> random-atom pure chain dies at depth ~1 for every D (cos = 0.71);")
    print("     G1 prediction (d* ~ D) MISSED -- per-level noise is O(1), not O(1/D)")

    print("=" * 68)
    print("G1b HRR superposition capacity -- the incumbent's resource is archimedean")
    print("-" * 68)
    m_stars = []
    for D in Ds:
        m_star = g1b_capacity(D)
        m_stars.append(m_star)
        print(f"  D={D:5d}   m* (max bundled pairs retrieved) = {m_star:4d}   "
              f"m*/D = {m_star / D:.3f}")
    assert all(m_stars[i] <= m_stars[i + 1] for i in range(len(m_stars) - 1)), m_stars
    checks += 1
    assert m_stars[-1] >= 2 * m_stars[0], m_stars   # capacity grows substantially with D
    checks += 1
    print("  -> m* rises with D (sub-linear at these finite sizes; the asymptotic law is")
    print("     linear): capacity is a dimension-driven concentration-of-measure resource")

    print("=" * 68)
    print("G1c UNITARY HRR -- the good incumbent carries pure-chain depth for free")
    print("-" * 68)
    unit_cos = g1c_unitary_depth(max_depth=200)
    print(f"  D=1024  depth=200  worst-case cos(recovered, true) = {unit_cos:.4f}")
    assert unit_cos > 0.99, unit_cos           # unitary inverse is exact => depth free
    checks += 1
    print("  -> unitary atoms carry pure-chain depth at fixed D; exact unbinding's edge")
    print("     on this axis is NIL (not even a constant) -- G1's argument, measured")

    print("=" * 68)
    print("G2  exact substrate -- fixed register, any depth")
    print("-" * 68)
    all_ok, reg_bits, N = g2_exact(max_depth=1000)
    print(f"  ring Z/{N}  register = {reg_bits} bits (CONSTANT in depth)")
    print(f"  exact recovery correct at every depth 1..1000: {all_ok}")
    assert all_ok
    checks += 1

    print("=" * 68)
    print("G3  the fair fight -- what the exact win costs (robustness)")
    print("-" * 68)
    hrr_rho, exact_rho = g3_robustness()
    print(f"  HRR   rho* (max corruption still recovered) = {hrr_rho:.2f}  (graceful)")
    print(f"  exact rho* (max corruption still recovered) = {exact_rho:.2f}  (catastrophic)")
    assert hrr_rho > 0.0, hrr_rho          # HRR degrades gracefully
    checks += 1
    assert exact_rho == 0.0, exact_rho     # exact fails at any corruption
    checks += 1

    print("=" * 68)
    print(f"OK  {checks} checks")


if __name__ == "__main__":
    main()
