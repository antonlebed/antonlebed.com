"""
THE MACHINE-WORD TOWER -- Z/(2^32 - 1) charted whole. (A smaller
engineering lead, n = 5 of the Fermat family whose n = 4 member is
the internet-checksum ring, explore_checksum_ring.py.)

2^32 - 1 = 4294967295 = 3 * 5 * 17 * 257 * 65537: the FIVE known
Fermat primes F_0..F_4 (telescoping 2^(2^5) - 1 = F_0 ... F_4), a
squarefree all-field designed tower that fills one machine word
exactly. Reduction mod 2^32 - 1 is end-around carry at the word
width -- the RFC 1071 fold one octave up -- so the ring's addition is
native on any 32-bit datapath. The chart below reads the whole
blueprint plus two earlier probes: RFC 1624's
incremental update as a per-channel ring identity, and the forced
channel 3 with its one-point graded region.

Predictions (stated in advance of any run):
  P1. FREE MOD AT THE WORD WIDTH (rule, proved + sampled). For every
      sum s of two words below 2^32, fold(s) = (s & 0xFFFFFFFF) +
      (s >> 32) satisfies fold(s) == s (mod 2^32 - 1), lands in
      [0, 0xFFFFFFFF], and needs at most ONE fold per addition.
      Proof is one line: s = hi*2^32 + lo == hi + lo since 2^32 == 1;
      for a single add hi <= 1, so lo + hi <= 2^32 - 1 at s <=
      2^33 - 2 (the one-fold bound is single-add-scoped: 2^33 - 1,
      just beyond the range, folds twice). The exhaustive 16-bit law
      is at explore_checksum_ring.py; here the range (2^33 sums) is
      sampled + edge-swept, the algebra carrying the tier. The two
      one's-complement zeros 0x00000000 / 0xFFFFFFFF are the two
      representatives of the zero class.
      MEASURED CONTACT (observation, this platform): a Python-int
      benchmark -- per-add fold vs per-add %, and the deferred form
      (accumulate wide, reduce once) both ways. The open question is
      whether the word-width trick buys the reduction even where %
      is one bignum op? (In C the fold is add-with-carry; Python
      ints are the honest local measurement.)
  P2. THE MODULUS IS A DESIGNED TOWER (property, verified).
      Factorization, telescoping, squarefree all-field; phi =
      2*4*16*256*65536 = 2^31, lambda = lcm = 2^16, 32 idempotents.
  P3. THE INDEX-COORDINATE STACK (rule, verified). U(Z/(2^32-1)) =
      U(F_3) x ... x U(F_65537), each factor cyclic of order p - 1 =
      2^(2^k): EVERY index modulus is a power of two. Fixing a
      generator per channel (2, 2, 3, 3, 3 -- full order verified),
      unit multiplication becomes five PARALLEL INDEX ADDS, each a
      masked binary add of width 1/2/4/8/16 -- mod (p-1) is & (p-2)
      -- packing into a 31-bit index word, exactly log2(phi), no
      mixed-radix correction anywhere. (The classic index-LUT RNS
      multiplier, with tables of 3+5+17+257+65537 entries; the edge
      over the literature's non-prime special moduli: all channels
      stay fields.) Verified on random unit pairs, all five channels.
      Side fact: the word's own base is index-shallow -- ord(2) mod
      F_k = 2^(k+1) (since 2^(2^k) == -1 mod F_k), so base 2
      generates only the two smallest channels.
  P4. CHEAP COLLAPSE (rule). x^lambda = x^(2^16) = e_supp(x) in 16
      squarings; sampled + all 32 supports via constructed witnesses
      (residue 2 on the support, 0 off it -- random draws provably
      cannot reach the rare small supports, a lesson learned earlier).
  P5. INCREMENTAL UPDATE SPLITS BY CHANNEL (rule + classical contact,
      RFC 1624). RFC 1624's eqn 3, HC' = ~(~HC + ~m + m'), is -- since
      complement is ring negation -- the identity HC' = HC + m - m'
      (equivalently C' = C - m + m' on the uncomplemented sum): a
      one-word change updates the checksum without re-summing. In the
      tower the identity SPLITS: HC'_p = HC_p + m_p - m'_p per
      channel, each update reading only m mod p and m' mod p.
      Verified at n = 4 (the live RFC ring) and n = 5 (the family
      transfer). The RFC 1141 boundary bug that RFC 1624 exists to
      fix (an update yielding 0xFFFF where from-scratch gives 0x0000,
      "minus zero ... when it should be +0") lives ENTIRELY in the
      two representatives of the ring's zero class -- the ring value
      was never wrong, the byte-equality test was comparing
      representatives.
  P6. THE FORCED 3 AND ITS POVERTY (property + chart line). 3 divides
      2^w - 1 iff w is even, so every Fermat-family ring 2^(2^n) - 1
      (n >= 1) carries channel 3 -- and with it the p = 3 RIGIDITY:
      the graded region of F_3 is the single self-inverse
      point -1, where (-1) OR (-1) = 0 and (-1) AND (-1) = 1 are
      forced. Inside the free-mod family the dodge is parity of the
      width: any ODD w gives a 3-free ring Z/(2^w - 1) with the same
      end-around-carry mod (designed towers dodge by set choice;
      word-width rings by width parity).

RESULTS (the record; checks below encode the measured law):
  All six predictions CONFIRMED (20 checks, ~5 s). P1: fold law on
  200,000 random sums + 17 edge sums; max folds = 1 on the single-add
  range, with 2^33 - 1 (just beyond it) confirmed as the smallest
  2-fold sum. The benchmark ANSWERS THE OPEN QUESTION NO for Python:
  per-add fold 0.052 s vs per-add % 0.043 s per 10^6 adds (median of
  5, CPython 3.12 this machine -- % WINS by ~1.2x: % is ONE bytecode
  op, the fold is three), and the deferred form beats both by ~3.5x
  (accumulate wide,
  reduce once: 0.012-0.015 s). The free-mod claim is a DATAPATH fact
  (fold = add-with-carry where % is a divide unit) -- real on
  CPU/FPGA/JS-bitwise targets, not in an interpreter; the honest
  Python advice is the RFC's own deferred form. P2: as stated
  (crt.py Ring + carmichael_lambda).
  P3: generator orders (2,4,16,256,65536) verified by table
  construction; 2,000 random unit pairs, dlog(xy) = (dlog x +
  dlog y) & (p-2) in all five channels; index widths 1+2+4+8+16 = 31
  = log2 phi; ord(2) = 2^(k+1) in every channel (2, 4, 8, 16, 32).
  P4: x^(2^16) = e_supp(x) in 16 squarings, 2003 sampled x; all 32
  supports hit by constructed witness. P5: eqn 3 == ring identity ==
  from-scratch (mod 65535) on 500 random one-word updates at n = 4;
  per-channel update exact, 4 channels x 500; both checks repeated at
  n = 5 (500 packets of 32-bit words, 5 channels) -- the family
  pattern holds. P6: 3 | 2^w - 1 at exactly the even w, swept w =
  1..64; channel-3 graded region = {2} = {-1} with both forced
  evaluations confirmed mod 3.

Tier: rule (P1 fold law -- proved algebra, sampled witness; P3, P4,
P5 -- verified at the stated ranges, the splits one-line algebra from
channel locality); property (P2; P6's divisibility -- elementary);
observation (the benchmark -- one platform, Python ints only).
Classical contacts: RFC 1624 eqn 3 + its RFC 1141 boundary example;
index-LUT RNS multipliers are classic hardware (the char-2 mirrors,
Fermat-family clause).
"""

import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import Ring, carmichael_lambda, decode, encode, factorize

random.seed(20260612)

M32 = 0xFFFFFFFF      # 2^32 - 1
M16 = 0xFFFF          # 2^16 - 1 (the n = 4 member, for P5)
CHECKS = []


def check(name, ok):
    CHECKS.append((name, ok))
    print(("  PASS  " if ok else "  FAIL  ") + name)


def fold(s, width, mask):
    """End-around carry: fold bits above the width back in, repeat."""
    while s >> width:
        s = (s & mask) + (s >> width)
    return s


print("=" * 68)
print("I. FREE MOD AT THE WORD WIDTH (P1)")
print("=" * 68)

# The law fold(s) == s mod M is one-line algebra (2^32 == 1 mod M)
# and holds for ANY s; the max-one-fold bound (hi <= 1, lo + hi <=
# 2^32 - 1) holds only on the single-add range [0, 2^33 - 2], so its
# tracking is scoped there (2^33 - 1 is the smallest 2-fold sum:
# fold -> 2^32 -> 1). The 16-bit ring's exhaustive law is at
# explore_checksum_ring.py; here sample + edges, the algebra carrying
# the tier.
SINGLE_ADD_MAX = 2**33 - 2
edges = [0, 1, 2, M32 - 1, M32, M32 + 1, 2 * M32 - 1, 2 * M32,
         2 * M32 + 1, 0x55555555, 0xAAAAAAAA,
         0x55555555 + 0xAAAAAAAA, 0xFFFFFFFE + 0xFFFFFFFF,
         0x80000000, 0x100000000, 0x17FFFFFFF, 3 * M32]
sums = edges + [random.randrange(0, 2**33 - 1) for _ in range(200_000)]
ok_law, ok_range, max_folds = True, True, 0
two_fold_at = None
for s in sums:
    t, folds = s, 0
    while t >> 32:
        t = (t & M32) + (t >> 32)
        folds += 1
    if s <= SINGLE_ADD_MAX:
        max_folds = max(max_folds, folds)
    elif folds > 1 and two_fold_at is None:
        two_fold_at = s
    if t % M32 != s % M32:
        ok_law = False
    if not (0 <= t <= M32):
        ok_range = False
check("fold(s) == s mod 2^32-1 (200,000 sampled + 17 edge sums)", ok_law)
check("fold lands in [0, 0xFFFFFFFF]; max folds on the single-add "
      "range = 1 (2^33-1 beyond it needs 2)",
      ok_range and max_folds == 1 and two_fold_at == 2**33 - 1)
check("two zeros: 0x00000000 and 0xFFFFFFFF both == 0 mod 2^32-1",
      0 % M32 == 0 and M32 % M32 == 0)

# MEASURED CONTACT: Python-int benchmark, per-add reduction both ways
# plus the deferred (accumulate wide, reduce once) forms. Median of 5
# runs of 10^6 word adds; words pre-drawn so the loop times only
# add + reduce.
words = [random.randrange(0, 2**32) for _ in range(1_000_000)]


def bench(f):
    ts = []
    for _ in range(5):
        t0 = time.perf_counter()
        f()
        ts.append(time.perf_counter() - t0)
    return sorted(ts)[2]


def run_fold_per_add():
    acc = 0
    for w in words:
        acc += w
        acc = (acc & M32) + (acc >> 32)
    return acc


def run_mod_per_add():
    acc = 0
    for w in words:
        acc = (acc + w) % M32
    return acc


def run_deferred_fold():
    acc = 0
    for w in words:
        acc += w
    return fold(acc, 32, M32)


def run_deferred_mod():
    return sum(words) % M32


t_fold, t_mod = bench(run_fold_per_add), bench(run_mod_per_add)
t_dfold, t_dmod = bench(run_deferred_fold), bench(run_deferred_mod)
winner = "%" if t_mod < t_fold else "fold"
print(f"  bench (10^6 adds, median of 5): per-add fold {t_fold:.3f} s, "
      f"per-add % {t_mod:.3f} s "
      f"({winner} wins, {max(t_fold, t_mod) / min(t_fold, t_mod):.2f}x)")
print(f"  deferred: accumulate + fold-once {t_dfold:.3f} s, "
      f"+ %-once {t_dmod:.3f} s")
check("all four reduction routes agree on the words' checksum",
      run_fold_per_add() % M32 == run_mod_per_add()
      == run_deferred_fold() % M32 == run_deferred_mod())

print()
print("=" * 68)
print("II. THE MODULUS IS A DESIGNED TOWER (P2)")
print("=" * 68)

MW = Ring("MWORD", (3, 5, 17, 257, 65537), (1, 1, 1, 1, 1))
fermat = [2**(2**k) + 1 for k in range(5)]          # F_0..F_4
check("2^32-1 = 3*5*17*257*65537, squarefree",
      factorize(M32) == {3: 1, 5: 1, 17: 1, 257: 1, 65537: 1})
check("all five factors are Fermat primes F_0..F_4",
      fermat == [3, 5, 17, 257, 65537])
check("telescoping: 2^(2^5) - 1 = F_0*F_1*F_2*F_3*F_4",
      M32 == fermat[0] * fermat[1] * fermat[2] * fermat[3] * fermat[4])
check("phi = 2^31, lambda = 2^16, 32 idempotents",
      MW.phi == 2**31 and MW.lam == 2**16
      and carmichael_lambda(M32) == 2**16 and MW.num_idempotents == 32)

print()
print("=" * 68)
print("III. THE INDEX-COORDINATE STACK (P3)")
print("=" * 68)

# Generators per channel (smallest primitive roots); the dlog table
# construction itself verifies full order: g returns to 1 exactly at
# step p-1 iff the p-1 powers are distinct.
GENS = {3: 2, 5: 2, 17: 3, 257: 3, 65537: 3}
dlog = {}
ok_gen = True
for p, g in GENS.items():
    table, x = {}, 1
    for i in range(p - 1):
        if x in table:
            ok_gen = False
            break
        table[x] = i
        x = x * g % p
    if x != 1 or len(table) != p - 1:
        ok_gen = False
    dlog[p] = table
check("generators (2,2,3,3,3) have full order p-1 in every channel",
      ok_gen)

# Multiplication of units = five parallel index adds; every index
# modulus p-1 is a power of two, so mod (p-1) is the masked add
# & (p-2). 2,000 random unit pairs.
ok_add = True
units = []
while len(units) < 4000:
    x = random.randrange(1, M32)
    if all(x % p for p in MW.primes):
        units.append(x)
for x, y in zip(units[:2000], units[2000:]):
    xy = x * y % M32
    for p in MW.primes:
        if dlog[p][xy % p] != (dlog[p][x % p] + dlog[p][y % p]) & (p - 2):
            ok_add = False
check("unit mul = 5 parallel masked index adds (2,000 random pairs)",
      ok_add)
check("index widths 1+2+4+8+16 = 31 bits = log2(phi)",
      sum((p - 1).bit_length() - 1 for p in MW.primes) == 31
      and MW.phi == 2**31)

# The word's own base is index-shallow: 2^(2^k) == -1 mod F_k, so
# ord(2) = 2^(k+1) -- base 2 generates only channels 3 and 5.
ok_ord2 = True
for k, p in enumerate(MW.primes):
    if pow(2, 2**k, p) != p - 1 or pow(2, 2**(k + 1), p) != 1:
        ok_ord2 = False
check("ord(2) mod F_k = 2^(k+1), all five channels (2,4,8,16,32)",
      ok_ord2)

print()
print("=" * 68)
print("IV. THE CHEAP COLLAPSE (P4)")
print("=" * 68)


def collapse32(x):
    """x^(2^16) via 16 squarings."""
    for _ in range(16):
        x = x * x % M32
    return x


ok_col = True
sample = random.sample(range(M32), 2000) + [0, 1, M32 - 1]
for x in sample:
    tgt = tuple(1 if r else 0 for r in encode(x, MW))
    if encode(collapse32(x), MW) != tgt:
        ok_col = False
check("x^(2^16) = e_supp(x) in 16 squarings (2003 sampled x)", ok_col)

# Every support subset, by constructed witness (residue 2 mod p on the
# support, 0 off it; 2 != 0 in every channel) -- random sampling
# provably cannot reach the rare small supports.
ok_all = True
for bits in range(32):
    S = tuple((bits >> i) & 1 for i in range(5))
    x = decode(tuple(2 * b % p for b, p in zip(S, MW.primes)), MW)
    if encode(collapse32(x), MW) != S:
        ok_all = False
check("all 32 supports: constructed witness collapses to its e_S",
      ok_all)

print()
print("=" * 68)
print("V. INCREMENTAL UPDATE SPLITS BY CHANNEL (P5)")
print("=" * 68)

# RFC 1624 eqn 3 at the live n = 4 ring: HC' = ~(~HC + ~m + m'), all
# sums folded at width 16. Ring reading: ~x & M16 = M16 - x = -x, so
# eqn 3 is HC' = HC + m - m' mod 65535.
CHK = Ring("CHECKSUM", (3, 5, 17, 257), (1, 1, 1, 1))


def incr_checks(ring, mask, width, label):
    """Both P5 checks on one ring: eqn 3 == ring identity ==
    from-scratch, and the per-channel split."""
    ok_eqn, ok_chan = True, True
    M = mask  # the modulus is also the all-ones mask (2^w - 1)
    for _ in range(500):
        ws = [random.randrange(0, mask + 1)
              for _ in range(random.randrange(2, 65))]
        i = random.randrange(len(ws))
        m, m2 = ws[i], random.randrange(0, mask + 1)
        C = fold(sum(ws), width, mask)
        HC = ~C & mask
        # eqn 3, computed the RFC's way (fold-as-you-go)
        hc_rfc = ~fold((~HC & mask) + (~m & mask) + m2, width, mask) & mask
        # the ring identity
        hc_ring = (HC + m - m2) % M
        # from scratch
        ws2 = list(ws)
        ws2[i] = m2
        hc_scratch = ~fold(sum(ws2), width, mask) & mask
        if not (hc_rfc % M == hc_ring % M == hc_scratch % M):
            ok_eqn = False
        # per-channel: each channel's update reads only m, m' mod p
        for j, p in enumerate(ring.primes):
            if (encode(HC % M, ring)[j] + m % p - m2 % p) % p \
                    != encode(hc_scratch % M, ring)[j]:
                ok_chan = False
    check(f"eqn 3 == HC + m - m' == from-scratch mod {M} "
          f"(500 updates, {label})", ok_eqn)
    check(f"per-channel update HC'_p = HC_p + m_p - m'_p exact, "
          f"{ring.k} channels ({label})", ok_chan)


incr_checks(CHK, M16, 16, "n=4")
incr_checks(MW, M32, 32, "n=5")

print()
print("=" * 68)
print("VI. THE FORCED 3 AND ITS POVERTY (P6)")
print("=" * 68)

check("3 | 2^w - 1 at exactly the even widths (w = 1..64 swept)",
      all((((2**w - 1) % 3 == 0) == (w % 2 == 0)) for w in range(1, 65)))

# The p = 3 rigidity: F_3's graded region (outside {0,1}) is the
# single self-inverse point -1 = 2, and the ring-polynomial logic
# (a OR b = a+b-ab, a AND b = ab) is forced there.
check("channel-3 graded region = {-1}: (-1) OR (-1) = 0, "
      "(-1) AND (-1) = 1 mod 3",
      [x for x in range(3) if x not in (0, 1)] == [2]
      and (2 + 2 - 2 * 2) % 3 == 0 and (2 * 2) % 3 == 1)

print()
print("=" * 68)
fails = [n for n, ok in CHECKS if not ok]
if fails:
    print(f"FAILURES ({len(fails)}): " + "; ".join(fails))
    sys.exit(1)
print(f"ALL CHECKS PASSED ({len(CHECKS)})")
