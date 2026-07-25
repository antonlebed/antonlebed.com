"""
The exact RNS comparator from the diagonal tie-break lemma

An earlier line of work found: the diagonal function D(x) = sum_p
floor(x/p) is channel-linear mod SQ = sum_p N/p, and inside a D-tie
class the residues mod the smallest modulus strictly increase -- so
(D(x), x mod p_min) is an EXACT comparator for any squarefree modulus
set. This script is the implementation layer on the charted lemma: a
reference implementation, exhaustive exactness, the approximate-diagonal
contrast, a measured cost model, and the honest FPGA-niche verdict.
Literature placement: see LITERATURE CONTACT after finding 7.

THE KEY (packed form): key(x) = D(x) * p_min + (x mod p_min), one
integer of width log2(SQ * p_min), strictly increasing on [0, N).
Strict monotonicity over all N values proves exactness on ALL N(N-1)/2
pairs at once (lexicographic order is total + transitive).

FINDINGS (tiers below):

1. THE REFERENCE COMPARATOR IS EXACT (rule, proved + exhaustive).
   key(x) strictly increasing over ALL 510510 RAD values => all
   ~1.30e11 pairs compare exactly (plus 100,000 random pairs direct,
   plus ALL pairs direct at Z/30 and Z/210). The comparator reads only
   residues: one dot product mod SQ + the p_min residue already in the
   RNS word.

2. THE COPRIMALITY IS FORCED, NOT A CONDITION (rule, proved + census).
   For ANY pairwise-coprime modulus set, gcd(N, SQ) = 1 automatically:
   mod a prime p | m_i every term N/m_j (j != i) carries the factor
   m_i, and N/m_i is coprime to p, so SQ = N/m_i != 0 mod p. The
   channel-linear form D = -N^{-1} sum_p x_p (N/p) mod SQ NEVER fails.
   (Census: 300 random prime sets + 300 random pairwise-coprime
   composite sets, gcd = 1 every time. The size-transform chart's
   "when gcd(N, SQ) = 1" hedge is hereby retired: it always holds.)

3. ANY SQUAREFREE SET, THREE TIE REGIMES (rule, verified exhaustive).
   Checksum ring {3,5,17,257} (no channel 2, p_min = 3, tie classes
   reach 3): exact on all 65535 values. Long-tie regime {97,101,103}
   (SQ ~ 0.0299 N, tie classes reach 97 = p_min -- the lemma's cap is
   tight here, the class [0..96] realizes it): exact on all 1,009,091
   values. All-composite set {15,77,221} (p_min = 15): exact on all
   255,255 values -- and it corrected the lemma's wording: later
   tie-class elements need NOT be units off all-prime sets (x = 3 is
   a specimen), the true invariant is that D steps exactly at the
   multiples of the moduli, so NO modulus divides a later class
   element. Hence ANY channel's residue serves as the tie-break, not
   only p_min's (rule, proved + verified in-loop at all three sets +
   RAD); p_min's residue minimizes the packed-key width. (Two
   corrections to the record: an earlier draft said the tie classes
   reach 33; the printed run shows 97. The earlier wording assumed
   later tie-class elements are units; the {15,77,221} run showed
   that is not required, and the wording above reflects the
   correction.)

4. THE APPROXIMATE-DIAGONAL CONTRAST (rule, exhaustive at RAD).
   D alone is monotone but not strict: it returns a false "equal" on
   exactly the phi(N) = 92,160 adjacent tie pairs (never an inverted
   verdict -- the failure is indecision, not disorder). The lemma
   repairs it with the channel-2 parity bit ALREADY IN THE WORD -- the
   same residue compare the standard SQT architecture wires in parallel
   (Dimauro 1993; Piestrak, IPL 2015). Exactness costs one extra
   compare of a residue you already have.

5. THE COST MODEL (measured + width law by construction).
   Width law: log2 SQ = log2 N + log2(sum_p 1/p). The comparator's
   dot product runs at width log2 SQ; reconstruction's at log2 N.
     - On the primorial rungs k >= 3, sum 1/p > 1 (RAD: 1.4028), so
       the diagonal channel is WIDER than the ring: the comparator is
       NOT cheaper than reconstruction on any rung. The on-rung niche
       CLOSES.
     - On designed large-prime sets, sum 1/p ~ k/p_min < 1: 8 primes
       near 2^16 give SQ 13.0 bits under the 128.0-bit N (ratio 0.90);
       8 near 2^32 give 29.0 under 256.0 (ratio 0.89). The saving is
       log2(p_min/k) bits of log2 N -- real, modest, ~10% at practical
       sizes.
     - CPython timing (interpreter-level: big-int
       constant factors, not datapath widths): diagonal-key compare
       within 1.15x of reconstruction at RAD and 1.08x at 8x32-bit;
       MRC ~3-5x slower (sequential digits; fair baseline, inverse
       table precomputed). Python cannot see the width law; the niche
       claim is the datapath's.

6. SIGN AND OVERFLOW RIDE FREE (rule, verified). [x >= N/2] = one key
   compare against a precomputed constant (exhaustive at RAD);
   wraparound of x + y = key(z) < key(x) for z = x + y mod N
   (all 44,100 pairs at Z/210 + 100,000 random RAD pairs). The three
   classic non-positional walls (compare, sign, overflow) all fall to
   the same one channel + one residue.

7. THE NICHE VERDICT (honest). The bar was "exact on ALL pairs AND
   cheaper than reconstruction". Exactness: met everywhere. Cost: on
   the rungs the niche closes (sum 1/p > 1); on all-field designed
   large-prime sets it fires, narrowly -- a ~10% narrower comparison
   datapath than reconstruction, PLUS exactness for log2(p_min) extra
   key bits (the parity bit when 2 is a channel; the dot product's
   width is unchanged), PLUS all channels stay fields
   (meadow + MDS + idempotent logic survive, where the literature's
   redundant-modulus repairs give them up). No Verilog: the on-rung
   story is negative and the off-rung advantage is a width delta, not
   an architecture -- the width law is forced by construction and a
   build would only re-measure it.

LITERATURE CONTACT (sources fetched, not paywalled
originals -- placements below cite what was read):

a. THE RESIDUE TIE-BREAK IS THE STANDARD ARCHITECTURE. The
   sum-of-quotients-technique (SQT) comparator -- the literature's
   name for the D-based one -- resolves D(X) = D(Y) with a parallel
   compare on one channel's residues, x_1 vs y_1 -- the smallest
   modulus in that literature's examples (Dimauro/Impedovo/Pirlo,
   IEEE ToC 1993;
   Piestrak, IPL 2015 showed it runs in parallel at two gate-levels;
   reproduced as Fig. 1 of Electronics 2020, 9, 1784). The lemma's
   residue: the general proof and scope -- no modulus divides a
   tie-class element past the first, so ANY channel's residue
   strictly increases within a class (finding 3; p_min's minimizes
   the packed width) for ANY squarefree set, ties cap at adjacent
   pairs (count phi(N)) with 2 a channel -- plus the packed
   single-key form and findings 2, 5, 6.

b. THE CRITERION AND THE FIELD'S COST AXIS ARE DIFFERENT AXES. The
   width law prices the dot product's WIDTH (log2 SQ vs log2 N); the
   field's negative verdict on diagonal comparators (Piestrak, IPL
   2015: excessive hardware and delay, CRT-based faster) rests on the
   mod-SQ arithmetic being AWKWARD (a multi-operand modular adder mod
   an arbitrary constant) while saving too little width to pay for it
   -- the field's own sample sets already sit on the sum 1/p < 1
   branch (Electronics 2020's "M and SQ differ by 3-5 bits" is SQ
   NARROWER; computed here: {13,15,17} has SQ/N = 0.2024, SQ
   2.30 bits under N). What the criterion adds is the exact law on
   the width axis (SQ/N = sum 1/p, both directions) and the branch
   the field's sets never visit: many-small-prime sets -- every
   primorial rung k >= 3 -- where the diagonal channel is WIDER than
   the ring. The MDF line (Electronics 2020) attacks the awkwardness
   axis instead: a power-of-2 working modulus, at the floor price
   of (c).

c. THE INJECTIVITY FLOOR (property, pigeonhole). The modify-D strands
   -- the modified diagonal function (Electronics 2020, 9, 1784) and
   monotonic core functions (Chervyakov line) -- make the positional
   characteristic STRICTLY monotone on [0, N), so it takes >= N values
   and its computed width can never drop below reconstruction's
   log2 N. A characteristic-based comparator that computes narrower
   than log2 N is therefore FORCED into the split shape: a
   non-injective characteristic plus a tie-break -- and sum 1/p < 1
   prices exactly when the split's computed part (D at log2 SQ) gets
   under the floor.

d. GENERIC-BASE SOTA CONFIRMS THE PAIN IS LIVE, AND THE WIDTH LAW
   PRICES THE DIAGONAL OUT THERE TOO. Didier et al. (arXiv
   2605.18415, 2026): generic-base software comparison at
   cryptographic sizes still costs one MRC of the difference, O(n^2)
   word mults per comparison, plus a redundant modulus; they set the
   diagonal aside as "not suitable for cryptographic-size" -- the
   width law's statement in software terms (log2 SQ ~ log2 N there,
   so D costs a reconstruction-class big-int dot product). Per-number
   characteristics amortize over sort/min/median workloads, but that
   is not ours: per-number MRS conversion (Szabo-Tanaka) amortizes
   the same way. No corpus win at crypto sizes; the honest niche
   stays finding 7's.

Runs on RAD + designed sets; exhaustive where stated. ~3 s, tiny
memory.
"""

import sys, os, math, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import RAD_RING, mod_inverse, is_prime

random.seed(76)
R = RAD_RING
N = R.N
K = R.k
PRIMES = R.primes


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# ───────────────────────────────────────────────────────────────────────
# THE REFERENCE IMPLEMENTATION
# ───────────────────────────────────────────────────────────────────────
class DiagonalComparator:
    """Exact RNS comparator from the diagonal tie-break lemma.
    Verified scope: squarefree modulus sets (all primes, or pairwise-
    coprime squarefree composites); construction itself needs only
    pairwise coprimality (the gcd is forced, finding 2).

    key(residues) = D * p_min + r_min, where
      D     = sum_p floor(x/p) = (sum_p c_p x_p) mod SQ   (channel-linear)
      c_p   = (-N^{-1} * (N/p)) mod SQ                     (precomputed)
      r_min = x mod p_min                                  (already in the word)
    Strictly increasing in x on [0, N), so integer-comparing keys is an
    exact comparator. gcd(N, SQ) = 1 is FORCED for pairwise-coprime
    sets (finding 2), so construction never fails.
    """

    def __init__(self, moduli):
        self.moduli = tuple(moduli)
        self.N = math.prod(self.moduli)
        self.SQ = sum(self.N // m for m in self.moduli)
        g = math.gcd(self.N, self.SQ)
        assert g == 1, f"gcd(N, SQ) = {g} != 1 (impossible for pairwise-coprime sets)"
        Ninv = mod_inverse(self.N % self.SQ, self.SQ)
        self.c = tuple((-Ninv * (self.N // m)) % self.SQ for m in self.moduli)
        self.i_min = min(range(len(self.moduli)), key=lambda i: self.moduli[i])
        self.p_min = self.moduli[self.i_min]

    def encode(self, x):
        return tuple(x % m for m in self.moduli)

    def key(self, residues):
        """The packed comparison key. Residue-only input."""
        D = sum(cp * r for cp, r in zip(self.c, residues)) % self.SQ
        return D * self.p_min + residues[self.i_min]

    def compare(self, res_x, res_y):
        """-1 / 0 / +1 for x < y / x == y / x > y. Residue-only."""
        kx, ky = self.key(res_x), self.key(res_y)
        return (kx > ky) - (kx < ky)


def mrc_table(moduli):
    """Precomputed inverse table for mixed-radix conversion (constants
    of the modulus set, computed once -- the fair baseline)."""
    k = len(moduli)
    return [[mod_inverse(moduli[i] % moduli[j], moduli[j]) if j > i else None
             for j in range(k)] for i in range(k)]


def mrc_digits(residues, moduli, inv):
    """Mixed-radix digits (sequential, depth k) -- the classic exact
    comparator baseline. Most-significant digit last: comparing
    reversed digit tuples is integer comparison."""
    k = len(moduli)
    r = list(residues)
    digits = []
    for i in range(k):
        d = r[i]
        digits.append(d)
        for j in range(i + 1, k):
            r[j] = ((r[j] - d) * inv[i][j]) % moduli[j]
    return tuple(reversed(digits))


# ───────────────────────────────────────────────────────────────────────
section("I. EXACTNESS AT RAD: exhaustive monotonicity = all pairs")
# ───────────────────────────────────────────────────────────────────────
# key strictly increasing over x = 0..N-1 proves the comparator exact on
# ALL N(N-1)/2 pairs: for x < y, key(x) < key(y) by transitivity of <,
# and the comparator's verdict is exactly the key order.
cmp_rad = DiagonalComparator(PRIMES)
print(f"RAD: N = {cmp_rad.N}, SQ = {cmp_rad.SQ} (~{cmp_rad.SQ/N:.4f} N), "
      f"p_min = {cmp_rad.p_min}")

prev = -1
res = [0] * K
for x in range(N):
    kx = cmp_rad.key(res)
    assert kx > prev, f"monotonicity fails at x = {x}"
    prev = kx
    for i, p in enumerate(PRIMES):          # increment residues in place
        res[i] += 1
        if res[i] == p:
            res[i] = 0
npairs = N * (N - 1) // 2
print(f"key strictly increasing over all {N} values "
      f"=> exact on all {npairs:.3e} pairs")

# Direct spot confirmation: 100,000 random pairs against integer truth.
for _ in range(100_000):
    x, y = random.randrange(N), random.randrange(N)
    truth = (x > y) - (x < y)
    assert cmp_rad.compare(cmp_rad.encode(x), cmp_rad.encode(y)) == truth
print("100,000 random RAD pairs: verdicts match integer comparison")

# ALL pairs direct at two small rungs (no monotonicity shortcut).
for moduli in ((2, 3, 5), (2, 3, 5, 7)):
    c = DiagonalComparator(moduli)
    enc = [c.encode(x) for x in range(c.N)]
    for x in range(c.N):
        for y in range(c.N):
            assert c.compare(enc[x], enc[y]) == (x > y) - (x < y)
    print(f"Z/{c.N}: all {c.N * c.N} ordered pairs direct -- exact")

# ───────────────────────────────────────────────────────────────────────
section("II. THE COPRIMALITY IS FORCED: gcd(N, SQ) = 1 always")
# ───────────────────────────────────────────────────────────────────────
# Proof: let p be a prime dividing modulus m_i. Every term N/m_j with
# j != i contains the factor m_i, hence is = 0 mod p; the remaining
# term N/m_i is a product of moduli coprime to m_i, hence coprime to p.
# So SQ = N/m_i != 0 mod p for every prime p | N: gcd(N, SQ) = 1.
# The size-transform chart's "when gcd(N, SQ) = 1" was a hedge for a
# theorem. Census below: prime sets and composite pairwise-coprime sets.
POOL = [p for p in range(3, 4000) if is_prime(p)]
for trial in range(300):
    ms = random.sample(POOL, random.randrange(3, 9))
    if random.random() < 0.5:
        ms[0] = 2
    Nt = math.prod(ms)
    SQt = sum(Nt // m for m in ms)
    assert math.gcd(Nt, SQt) == 1
print("300 random prime sets (k = 3..8, half containing 2): gcd(N, SQ) = 1")

for trial in range(300):
    # pairwise-coprime COMPOSITE moduli: products of disjoint prime pairs
    ps = random.sample(POOL, 8)
    ms = [ps[0] * ps[1], ps[2] * ps[3], ps[4] * ps[5], ps[6] * ps[7]]
    Nt = math.prod(ms)
    SQt = sum(Nt // m for m in ms)
    assert math.gcd(Nt, SQt) == 1
print("300 random pairwise-coprime composite sets: gcd(N, SQ) = 1")
print("=> the channel-linear form never fails; no condition to check.")

# ───────────────────────────────────────────────────────────────────────
section("III. ANY SQUAREFREE SET: three tie regimes, exhaustive")
# ───────────────────────────────────────────────────────────────────────
# (a) The checksum ring {3,5,17,257}: no channel 2, p_min = 3 -- tie
#     classes reach 3, tie-break is the mod-3 residue.
# (b) The long-tie regime {97,101,103}: most elements are units, so tie
#     classes are long (lemma caps them at p_min = 97); SQ << N here --
#     the regime where the cost story fires.
# (c) The all-composite set {15,77,221} (p_min = 15 composite): later
#     tie-class elements need NOT be units here (x = 3 is one) -- the
#     working invariant is "no modulus divides x", which is what the
#     in-loop assert checks.
for moduli, label in (((3, 5, 17, 257), "checksum ring"),
                      ((97, 101, 103), "long-tie designed set"),
                      ((15, 77, 221), "all-composite squarefree set")):
    c = DiagonalComparator(moduli)
    prev = -1
    max_tie, cur_tie = 1, 1
    prev_D = -1
    res = [0] * len(moduli)
    for x in range(c.N):
        kx = c.key(res)
        assert kx > prev
        prev = kx
        D = kx // c.p_min
        if D == prev_D:
            cur_tie += 1
            max_tie = max(max_tie, cur_tie)
            # any-channel tie-break (rule): D steps exactly at multiples
            # of the moduli, so NO modulus divides a later tie-class
            # element and no residue is 0 -- every channel's residue
            # strictly increased across this step, not only p_min's
            # (unitness is the all-prime specialization; {15,77,221}
            # has non-unit later elements)
            assert all(res), (label, x)
        else:
            cur_tie = 1
        prev_D = D
        for i, m in enumerate(moduli):
            res[i] += 1
            if res[i] == m:
                res[i] = 0
    print(f"{label} {moduli}: N = {c.N}, SQ/N = {c.SQ/c.N:.4f}, "
          f"max tie class = {max_tie} (<= p_min = {c.p_min}) -- "
          f"exact on all {c.N} values")
    assert max_tie <= c.p_min

# ───────────────────────────────────────────────────────────────────────
section("IV. THE APPROXIMATE-DIAGONAL CONTRAST (exhaustive at RAD)")
# ───────────────────────────────────────────────────────────────────────
# D alone (the literature's diagonal comparator before its repairs):
# monotone, so it never INVERTS a verdict; but it returns "equal" on
# every D-tie pair. Ties at RAD = adjacent pairs {x, x+1} with x+1 a
# unit = phi(N) pairs exactly. The exact key repairs every one with the
# parity residue already in the word.
ties = 0
res = [0] * K
prev_D = None
for x in range(N):
    D = sum(cp * r for cp, r in zip(cmp_rad.c, res)) % cmp_rad.SQ
    if prev_D is not None and D == prev_D:
        ties += 1
        assert math.gcd(x, N) == 1          # the tie partner is a unit
        assert x % 2 == 1                   # parity bit breaks the tie
        assert all(res)                     # any channel's residue does too
    prev_D = D
    for i, p in enumerate(PRIMES):
        res[i] += 1
        if res[i] == p:
            res[i] = 0
print(f"D-only comparator at RAD: false 'equal' on exactly {ties} "
      f"adjacent pairs = phi(N) = {R.phi}; never an inverted verdict")
assert ties == R.phi
print("exact key: 0 errors (section I). Repair cost: one compare of the")
print("channel-2 residue -- already in the RNS word.")

# ───────────────────────────────────────────────────────────────────────
section("V. THE COST MODEL: width law + interpreter timing")
# ───────────────────────────────────────────────────────────────────────
# Width law (by construction): SQ = N * sum 1/p, so
#   log2 SQ = log2 N + log2(sum 1/p).
# The comparator's dot product (k terms c_p * x_p, c_p < SQ) runs at
# width log2 SQ; reconstruction's (B_p * x_p, B_p < N) at log2 N. The
# comparator is narrower than reconstruction iff sum 1/p < 1.
def width_row(moduli, label):
    Nt = math.prod(moduli)
    SQt = sum(Nt // m for m in moduli)
    s = SQt / Nt
    lw, lr = math.log2(SQt), math.log2(Nt)
    verdict = "NARROWER" if s < 1 else "wider"
    print(f"  {label:28s} k={len(moduli):2d}  log2 N = {lr:6.1f}  "
          f"log2 SQ = {lw:6.1f}  sum 1/p = {s:.4f}  -> {verdict}")
    return s

print("Primorial rungs (sum 1/p > 1 from k = 3 on -- the on-rung niche closes):")
from crt import primes_up_to
RUNG_PRIMES = primes_up_to(200)
for k in (2, 3, 5, 7, 10):
    width_row(tuple(RUNG_PRIMES[:k]), f"rung k={k}")

print("Designed large-prime sets (the regime where the niche fires):")
P16 = [p for p in range(65535, 60000, -2) if is_prime(p)][:8]
P32 = [p for p in range(2**32 - 1, 2**32 - 1500, -2) if is_prime(p)][:8]
assert all(is_prime(p) for p in P16 + P32)
s16 = width_row(tuple(P16), "8 primes near 2^16")
s32 = width_row(tuple(P32), "8 primes near 2^32")
assert s16 < 1 and s32 < 1
print(f"  saving = log2(p_min / k) bits of log2 N: "
      f"{-math.log2(s16):.1f} bits of {math.log2(math.prod(P16)):.1f} (16-bit set), "
      f"{-math.log2(s32):.1f} of {math.log2(math.prod(P32)):.1f} (32-bit set)")

# Interpreter timing (honest tier: CPython measures big-int constant
# factors, not datapath widths; the niche claim is
# the datapath's). Per-comparison cost, residues in hand.
def bench(moduli, label, n_pairs=20_000):
    c = DiagonalComparator(moduli)
    Nt = c.N
    B = tuple((Nt // m) * mod_inverse((Nt // m) % m, m) for m in moduli)
    pairs = [(c.encode(random.randrange(Nt)), c.encode(random.randrange(Nt)))
             for _ in range(n_pairs)]

    t0 = time.perf_counter()
    for rx, ry in pairs:
        c.compare(rx, ry)
    t_diag = (time.perf_counter() - t0) / n_pairs

    t0 = time.perf_counter()
    for rx, ry in pairs:
        x = sum(b * r for b, r in zip(B, rx)) % Nt
        y = sum(b * r for b, r in zip(B, ry)) % Nt
        _ = (x > y) - (x < y)
    t_rec = (time.perf_counter() - t0) / n_pairs

    inv = mrc_table(moduli)
    t0 = time.perf_counter()
    for rx, ry in pairs[:n_pairs // 10]:    # MRC is slow; sample
        _ = (mrc_digits(rx, moduli, inv) > mrc_digits(ry, moduli, inv))
    t_mrc = (time.perf_counter() - t0) / (n_pairs // 10)

    print(f"  {label:24s} diagonal {t_diag*1e6:7.2f} us   "
          f"reconstruct {t_rec*1e6:7.2f} us   MRC {t_mrc*1e6:7.2f} us   "
          f"(diag/rec = {t_diag/t_rec:.2f}x)")
    return t_diag, t_rec, t_mrc

# MRC baseline correctness gate (a wrong baseline is a wrong
# measurement): digit tuples must sort exactly as integers.
inv210 = mrc_table((2, 3, 5, 7))
prev_digits = None
for x in range(210):
    d = mrc_digits(tuple(x % m for m in (2, 3, 5, 7)), (2, 3, 5, 7), inv210)
    assert prev_digits is None or d > prev_digits
    prev_digits = d
print("MRC baseline gate: digit order = integer order (all of Z/210)")

print("CPython per-comparison timing (residue input, verdict output):")
bench(PRIMES, "RAD (k=7)")
bench(tuple(P32), "8 primes near 2^32")

# ───────────────────────────────────────────────────────────────────────
section("VI. SIGN AND OVERFLOW RIDE FREE")
# ───────────────────────────────────────────────────────────────────────
# Sign [x >= N/2]: one key compare against the precomputed constant
# key(ceil(N/2)). Exhaustive at RAD.
half = (N + 1) // 2
key_half = cmp_rad.key(cmp_rad.encode(half))
res = [0] * K
for x in range(N):
    assert (cmp_rad.key(res) >= key_half) == (x >= half)
    for i, p in enumerate(PRIMES):
        res[i] += 1
        if res[i] == p:
            res[i] = 0
print(f"sign [x >= {half}] = one key compare vs a constant: "
      f"exhaustive over all {N} RAD values")

# Overflow of x + y (integer sum >= N): z = x + y mod N wraps iff
# key(z) < key(x) (with equality only when y = 0, no wrap). All pairs
# at Z/210; 100,000 random pairs at RAD.
c210 = DiagonalComparator((2, 3, 5, 7))
enc210 = [c210.encode(x) for x in range(210)]
keys210 = [c210.key(e) for e in enc210]
for x in range(210):
    for y in range(210):
        z = (x + y) % 210
        assert (keys210[z] < keys210[x]) == (x + y >= 210)
print("overflow detect (key(z) < key(x)): all 44,100 pairs at Z/210")
for _ in range(100_000):
    x, y = random.randrange(N), random.randrange(N)
    z = (x + y) % N
    assert (cmp_rad.key(cmp_rad.encode(z)) < cmp_rad.key(cmp_rad.encode(x))) \
        == (x + y >= N)
print("overflow detect: 100,000 random RAD pairs")

# ───────────────────────────────────────────────────────────────────────
section("VII. FINDINGS")
# ───────────────────────────────────────────────────────────────────────
print(__doc__[__doc__.index("FINDINGS (tiers"):])

print("ALL CHECKS PASSED")
