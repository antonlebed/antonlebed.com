"""
THE UINT64 DESIGNED TOWER -- Z/(2^64 - 1) charted whole.
(n = 6 of the Fermat family whose n = 4 member is the
internet-checksum ring, explore_checksum_ring.py, and n = 5 the
machine-word tower, explore_machine_word_tower.py. This is the FIRST
member OFF the all-Fermat spine: 2^32 + 1 = F_5 = 641 * 6700417,
Euler 1732.)

2^64 - 1 = 3 * 5 * 17 * 257 * 641 * 65537 * 6700417: seven prime
channels filling one 64-bit machine word exactly -- a RAD-sized
(k = 7) squarefree all-field designed tower. The chart asks one
question: WHAT SURVIVES OFF THE ALL-FERMAT SPINE, AND WHAT DIES?

Predictions (stated in advance of any run):
  P1. FOLD AT WIDTH 64 SURVIVES (rule, proved + sampled). The free
      mod is width-generic: s = hi*2^64 + lo == hi + lo since
      2^64 == 1, one fold per single add (hi <= 1 at s <= 2^65 - 2;
      2^65 - 1, just beyond, folds twice). The ring's addition is
      native on any 64-bit datapath (end-around carry); the
      interpreter caveat is the n = 5 chart's, unchanged -- no
      benchmark rerun here.
  P2. DESIGNED TOWER, OFF THE SPINE (property, verified).
      Factorization + telescoping M64 = F_0*...*F_5 with F_5
      composite (Euler); all seven factors prime, squarefree
      all-field; phi = 2^45 * 261735 (bit_length 63), 128
      idempotents; and the family's first NON-2-POWER lambda:
      lambda = 2^16 * 3 * 5 * 17449 (6700416 = 2^7 * 3 * 17449).
      The forced 3 (even width) is present, with its one-point
      graded region.
  P3. THE INDEX STACK SPLITS: FIVE MASKS + TWO TRUE MODS (rule,
      verified). The five Fermat channels keep 2-power index moduli
      (masked adds, widths 1+2+4+8+16 = 31); the two F_5 channels
      have index moduli 640 = 2^7 * 5 and 6700416 = 2^7 * 3 * 17449
      -- NOT 2-powers, so mod (p-1) is a true modular add (witness:
      the & (p-2) mask gives the WRONG index at g^320 * g^320 mod
      641). Index word 31 + 10 + 23 = 64 bits >= log2 phi ~ 63.0:
      the spine packed indices exactly; off the spine the first
      padding bit appears. ord(2) = 2^(k+1) on the Fermat channels
      and ord(2) = 64 in BOTH new channels (2^32 == -1 mod each
      F_5 factor): the word's base has order exactly the word
      width, and still generates only channels 3 and 5.
  P4. THE CHEAP-COLLAPSE KNOB DIES, COLLAPSE SURVIVES (rule,
      verified). x^lambda = e_supp(x) at every x (Clifford --
      construction); but lambda is no longer a 2-power, so the
      square-chain costs bit_length(lambda) - 1 = 33 squarings PLUS
      popcount(lambda) - 1 multiplies (vs 16 squarings, 0 multiplies
      at n = 5). Sampled + all 128 supports via constructed
      witnesses (residue 2 on the support, 0 off it -- random draws
      provably cannot reach the rare small supports).
  P5. INCREMENTAL UPDATE SPLITS (rule, verified at n = 6). RFC
      1624's identity HC' = HC + m - m' is channel-local algebra;
      it transfers verbatim to 64-bit words and 7 channels
      (HC'_p = HC_p + m_p - m'_p, each channel reading only m mod p
      and m' mod p). n = 4, 5 records live in the sibling scripts.
  P6. THE COMPARATOR LAW HOLDS SUB-BIT, FAMILY-WIDE (rule +
      instance). SQ = sum N/p has gcd(N, SQ) = 1 (forced,
      explore_rns_comparator.py finding 2); sum 1/p ~ 0.598 < 1, so
      the exact comparator's dot product is NARROWER than
      reconstruction -- but by log2(N/SQ) ~ 0.74 bits, a sub-bit
      margin: bit_length(SQ) = bit_length(N) = 64, zero whole-bit
      savings. Swept members n = 2..6: sum 1/p < 0.6 at each
      (dominated by 1/3 + 1/5), so the law clears and never buys a
      whole bit -- consistent with the earlier verdict (large-prime
      sets only). Beyond n = 6 each member ADDS the reciprocals of
      F_(n-1)'s factors (each factor == 1 mod 2^(n+1), so known
      factorizations move the sum in the sixth decimal); the all-n
      statement is OPEN alongside the factorizations themselves.
  P7. THE ECC PAYLOAD IS THE CHECKSUM RING (property + rule,
      verified). Seven channels = RAD-shaped: the tower split takes
      data = (3, 5, 17, 257), parity = (641, 65537, 6700417) -- and
      the data product is 3*5*17*257 = 65535 = 2^16 - 1: THE DATA
      SPACE OF THE UINT64 TOWER'S ECC IS THE INTERNET-CHECKSUM RING
      (the n = 4 member) -- a 16-bit-WORD payload riding a 64-bit
      word (rate 4/7 by channels; 65535 values, i.e. all 16-bit
      words with 0xFFFF == 0x0000 identified, the family's standing
      two-zero-representatives convention). MDS d = 4 at the
      slack-free boundary: the minimum 4-subset product equals the
      data product. The boundary itself is the TOWER SPLIT'S, not
      this ring's -- data = the four smallest channels makes the
      minimum 4-subset product the data product at every sorted
      k = 7 ring (RAD sits on the same edge at 210); what the
      telescoping buys is WHICH ring the payload is. Consequences
      verified: no two codewords agree on 4 channels (|difference|
      < 65535 <= every 4-subset product, all C(7,4) = 35 swept), a
      3-agreement witness exists (0 vs 21845 = 5*17*257), and ONE
      more data value would kill it (0 vs 65535 agree on all four
      data channels: a 65536-value payload has d = 3). Single-error
      correct verified on random codewords (crt.py ecc_correct).
  P8. FLETCHER IS THE FAMILY'S CHECKSUM (classical contact, fetched
      2026-06-12 + rule for the demo). Fletcher's checksum keeps TWO
      running sums A := A + D[i], B := B + A in one's-complement
      w-bit arithmetic = arithmetic mod 2^w - 1: Fletcher-16 sums
      mod 255 = 3*5*17 (the n = 3 member -- 2^(2^3) - 1 = F_0*F_1*
      F_2), Fletcher-32 mod 65535 (n = 4), Fletcher-64 mod
      4294967295 (n = 5). Every standard Fletcher variant runs both
      its accumulators in a Fermat-family ring; B is the
      position-weighted moment sum (N-i+1)*D[i], so BOTH sums split
      per channel by construction -- each channel runs its own
      Fletcher. (Sources: RFC 1146 defines the accumulators as
      unsigned 1's-complement -- the mod-(2^w - 1) reading, the same
      identification as RFC 1071's; the standard definition uses
      modulus 2^w - 1 explicitly. Real-world deviation: some
      implementations substitute mod 2^w, which leaves the ring --
      the contact is with the defining form.)

RESULTS (the record; checks below encode the measured law):
  All eight predictions CONFIRMED (34 checks, ~3 s). P1: fold law on
  200,000 random sums + 17 edge sums; max folds = 1 on the
  single-add range, 2^65 - 1 the smallest 2-fold sum. P2: as stated;
  phi = 9208981628670443520 = 2^45 * 261735 (bit_length 63); lambda
  = 17153064960 = 2^16 * 261735 (bit_length 34) -- see P4. P3:
  generators (2, 2, 3, 3, 3, 3) full-order in every tabled channel
  (3, 5, 17, 257, 641, 65537) by table construction; smallest
  primitive root mod 6700417 = 5 (order-certified on the three
  maximal divisors of p-1); 2,000 random unit pairs: masked add
  exact in all five Fermat channels, true mod-640 add exact at 641;
  mask witnesses at 641 ((320+320) & 639 = 512, g^512 != 1) and
  6700417 (exponent-level); index widths 31 + 10 + 23 = 64, phi
  bit_length 63; ord(2) = (2, 4, 8, 16, 32) on the spine and 64 =
  the word width in both F_5 channels. P4: pow(x, lambda) =
  e_supp(x) on 2,003 sampled x and all 128 constructed supports;
  cost 33 squarings + 13 multiplies (popcount 14) vs 16 + 0 at
  n = 5. P5: eqn 3 == ring identity == from-scratch and the
  per-channel split, 500 random one-word updates, 7 channels x 500.
  P6: gcd(N, SQ) = 1 with SQ = 11024205608477874323; SQ/N =
  0.597623, log2(N/SQ) = 0.743 bits; bit_length 64 = 64; packed key
  strictly monotone on 100,000 adjacent pairs + correct on 50,000
  random pairs; family sweep sum 1/p = 0.533333 / 0.592157 /
  0.596048 / 0.596063 / 0.597623 at n = 2..6, all < 0.6. P7: data
  product 65535 = M16 exactly; min 4-subset product = 65535 = data
  product (the slack-free boundary, all 35 subsets); 3-agreement
  witness (0 vs 21845 = 5*17*257) + 65536th-value d = 3 witness (0 vs 65535,
  4-channel agreement) both confirmed by direct encoding; 200
  random single-channel errors all detected, located, corrected
  (every channel hit). P8: moduli identities 255/65535/4294967295 =
  members n = 3/4/5; Fletcher-16 on 500 random messages: A = plain
  sum, B = position-weighted moment, both mod 255, both splitting
  per channel (3, 5, 17). Run of 2026-06-12, seed 20260612.

Tier: rule (P1 fold law -- proved algebra, sampled witness; P3, P4,
P5 -- verified at stated ranges, the splits one-line algebra from
channel locality; P7 MDS -- the zero-slack census is exhaustive over
subsets, the agreement bound one-line divisibility); property (P2;
P7 payload identity -- telescoping); classical contact + rule (P8 --
moduli fetched, demo verified); instance + family sweep (P6 -- the
law itself is proved at explore_rns_comparator.py).
Classical contacts: Euler's 1732 factorization of F_5; Fletcher 1982
via RFC 1146 (1's-complement accumulators) + the standard mod-(2^w-1)
definition (fetched 2026-06-12); index-LUT RNS multipliers.
"""

import math
import os
import random
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import (Ring, carmichael_lambda, decode, ecc_correct, ecc_detect,
                 ecc_encode, encode, factorize, is_prime, mod_inverse)

random.seed(20260612)

M64 = 2**64 - 1
M16 = 2**16 - 1
PRIMES = (3, 5, 17, 257, 641, 65537, 6700417)
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
print("I. FOLD AT WIDTH 64 SURVIVES (P1)")
print("=" * 68)

SINGLE_ADD_MAX = 2**65 - 2
edges = [0, 1, 2, M64 - 1, M64, M64 + 1, 2 * M64 - 1, 2 * M64,
         2 * M64 + 1, 0x5555555555555555, 0xAAAAAAAAAAAAAAAA,
         0x5555555555555555 + 0xAAAAAAAAAAAAAAAA,
         M64 - 1 + M64, 2**63, 2**64, 2**64 + 2**63 - 1, 3 * M64]
sums = edges + [random.randrange(0, 2**65 - 1) for _ in range(200_000)]
ok_law, ok_range, max_folds = True, True, 0
two_fold_at = None
for s in sums:
    t, folds = s, 0
    while t >> 64:
        t = (t & M64) + (t >> 64)
        folds += 1
    if s <= SINGLE_ADD_MAX:
        max_folds = max(max_folds, folds)
    elif folds > 1 and (two_fold_at is None or s < two_fold_at):
        two_fold_at = s
    if t % M64 != s % M64:
        ok_law = False
    if not (0 <= t <= M64):
        ok_range = False
check("fold(s) == s mod 2^64-1 (200,000 sampled + 17 edge sums)", ok_law)
check("fold lands in [0, 2^64-1]; max folds on the single-add "
      "range = 1 (2^65-1 beyond it needs 2)",
      ok_range and max_folds == 1 and two_fold_at == 2**65 - 1)

print()
print("=" * 68)
print("II. DESIGNED TOWER, OFF THE SPINE (P2)")
print("=" * 68)

U64 = Ring("U64", PRIMES, (1,) * 7)
fermat = [2**(2**k) + 1 for k in range(6)]          # F_0..F_5
check("2^64-1 = 3*5*17*257*641*65537*6700417, squarefree",
      factorize(M64) == {p: 1 for p in PRIMES})
check("telescoping: 2^(2^6)-1 = F_0*...*F_5, and F_5 = 641*6700417 "
      "(Euler) -- the first member off the all-Fermat spine",
      M64 == math.prod(fermat) and fermat[5] == 641 * 6700417
      and all(is_prime(p) for p in PRIMES))
check("the new index moduli factor: 640 = 2^7*5, "
      "6700416 = 2^7*3*17449 (17449 prime)",
      factorize(640) == {2: 7, 5: 1}
      and factorize(6700416) == {2: 7, 3: 1, 17449: 1}
      and is_prime(17449))
print(f"  phi = {U64.phi} = 2^45 * 261735 (bit_length {U64.phi.bit_length()})")
print(f"  lambda = {U64.lam} = 2^16 * 261735 (bit_length {U64.lam.bit_length()})")
check("phi = 2^45 * 261735 (bit_length 63), 128 idempotents",
      U64.phi == 2**45 * 261735 and U64.phi.bit_length() == 63
      and U64.num_idempotents == 128)
check("lambda = 2^16 * 3 * 5 * 17449 -- the family's first "
      "non-2-power lambda",
      U64.lam == 2**16 * 3 * 5 * 17449
      and carmichael_lambda(M64) == U64.lam
      and U64.lam & (U64.lam - 1) != 0)
check("the forced 3 is present (width 64 even; one-point graded "
      "region, the p=3 rigidity)",
      M64 % 3 == 0 and (2 + 2 - 2 * 2) % 3 == 0 and (2 * 2) % 3 == 1)

print()
print("=" * 68)
print("III. THE INDEX STACK SPLITS: FIVE MASKS + TWO TRUE MODS (P3)")
print("=" * 68)

# Full dlog tables where the table is small (all channels but
# 6700417); table construction itself certifies full order.
GENS = {3: 2, 5: 2, 17: 3, 257: 3, 641: 3, 65537: 3}
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
check("generators (2,2,3,3,3,3) have full order p-1 in every "
      "tabled channel (incl. 641)", ok_gen)

# 6700417: certify the smallest primitive root by the three maximal
# proper divisors of p-1 = 2^7 * 3 * 17449 (no table -- 6.7M entries
# would be a memory hog for nothing; the certificate is the proof).
P7BIG = 6700417
g_big = None
for g in range(2, 100):
    if all(pow(g, (P7BIG - 1) // q, P7BIG) != 1 for q in (2, 3, 17449)):
        g_big = g
        break
print(f"  smallest primitive root mod 6700417: {g_big} (order-certified)")
check("a certified generator exists mod 6700417 (cyclic channel)",
      g_big is not None)

# Unit multiplication: masked index adds on the five Fermat channels,
# TRUE mod-(p-1) add at 641 (tabled). 2,000 random unit pairs.
ok_mask, ok_mod = True, True
units = []
while len(units) < 4000:
    x = random.randrange(1, M64)
    if all(x % p for p in PRIMES):
        units.append(x)
for x, y in zip(units[:2000], units[2000:]):
    xy = x * y % M64
    for p in (3, 5, 17, 257, 65537):
        if dlog[p][xy % p] != (dlog[p][x % p] + dlog[p][y % p]) & (p - 2):
            ok_mask = False
    if dlog[641][xy % 641] != (dlog[641][x % 641] + dlog[641][y % 641]) % 640:
        ok_mod = False
check("unit mul = masked index adds in all 5 Fermat channels "
      "(2,000 random pairs)", ok_mask)
check("unit mul = TRUE mod-640 index add at 641 (2,000 random pairs)",
      ok_mod)

# The mask DIES off the spine: at 641, g^320 * g^320 = g^640 = 1 but
# (320 + 320) & 639 = 512 and g^512 != 1. Same algebra at 6700417
# (p-1 not a 2-power), witnessed exponent-level.
x320 = pow(3, 320, 641)
check("mask witness at 641: (320+320) & 639 = 512, g^512 != 1 "
      "while g^640 = 1",
      (640 & 639) == 512 and x320 * x320 % 641 == 1
      and pow(3, 512, 641) != 1)
mbig = (P7BIG - 1) & (P7BIG - 2)
check("mask witness at 6700417: g^((p-1) & (p-2)) != 1 while "
      "g^(p-1) = 1",
      pow(g_big, mbig, P7BIG) != 1 and pow(g_big, P7BIG - 1, P7BIG) == 1)

# Index word: 31 masked bits + two true-mod fields of 10 and 23 bits.
mask_bits = sum((p - 1).bit_length() - 1 for p in (3, 5, 17, 257, 65537))
mod_bits = (640 - 1).bit_length() + (6700416 - 1).bit_length()
print(f"  index word: {mask_bits} masked + {mod_bits} true-mod = "
      f"{mask_bits + mod_bits} bits; log2 phi ~ "
      f"{math.log2(U64.phi):.4f}")
check("index word 31 + 33 = 64 bits >= phi bit_length 63 -- the "
      "first padding bit off the spine",
      mask_bits == 31 and mod_bits == 33
      and U64.phi.bit_length() == 63)

# ord(2): 2^(k+1) on the spine; 64 = the word width in BOTH F_5
# channels (2^32 == -1 mod each factor).
ok_ord2 = all(pow(2, 2**k, p) == p - 1 and pow(2, 2**(k + 1), p) == 1
              for k, p in enumerate((3, 5, 17, 257, 65537)))
ok_ord2_new = all(pow(2, 32, p) == p - 1 and pow(2, 64, p) == 1
                  for p in (641, P7BIG))
check("ord(2) = 2^(k+1) on the spine (2,4,8,16,32); ord(2) = 64 = "
      "the word width in both F_5 channels",
      ok_ord2 and ok_ord2_new)

print()
print("=" * 68)
print("IV. THE CHEAP-COLLAPSE KNOB DIES, COLLAPSE SURVIVES (P4)")
print("=" * 68)

LAM = U64.lam
sq_cost, mul_cost = LAM.bit_length() - 1, bin(LAM).count("1") - 1
print(f"  collapse exponent lambda: {sq_cost} squarings + {mul_cost} "
      f"multiplies (n = 5 had 16 + 0)")
ok_col = True
sample = [random.randrange(0, M64) for _ in range(2000)] + [0, 1, M64 - 1]
for x in sample:
    tgt = tuple(1 if r else 0 for r in encode(x, U64))
    if encode(pow(x, LAM, M64), U64) != tgt:
        ok_col = False
check("x^lambda = e_supp(x) (2,003 sampled x)", ok_col)

ok_all = True
for bits in range(128):
    S = tuple((bits >> i) & 1 for i in range(7))
    x = decode(tuple(2 * b % p for b, p in zip(S, PRIMES)), U64)
    if encode(pow(x, LAM, M64), U64) != S:
        ok_all = False
check("all 128 supports: constructed witness collapses to its e_S",
      ok_all)
check("the knob is dead: lambda needs multiplies (popcount > 1), "
      "33 squarings vs 16 (and 0 multiplies) at n = 5",
      mul_cost > 0 and sq_cost == 33
      and carmichael_lambda(2**32 - 1) == 2**16)

print()
print("=" * 68)
print("V. INCREMENTAL UPDATE SPLITS BY CHANNEL (P5)")
print("=" * 68)

# RFC 1624 eqn 3 at n = 6: 64-bit words, 7 channels (n = 4, 5 records
# live in the sibling scripts).
ok_eqn, ok_chan = True, True
for _ in range(500):
    ws = [random.randrange(0, M64 + 1)
          for _ in range(random.randrange(2, 65))]
    i = random.randrange(len(ws))
    m, m2 = ws[i], random.randrange(0, M64 + 1)
    C = fold(sum(ws), 64, M64)
    HC = ~C & M64
    hc_rfc = ~fold((~HC & M64) + (~m & M64) + m2, 64, M64) & M64
    hc_ring = (HC + m - m2) % M64
    ws2 = list(ws)
    ws2[i] = m2
    hc_scratch = ~fold(sum(ws2), 64, M64) & M64
    if not (hc_rfc % M64 == hc_ring % M64 == hc_scratch % M64):
        ok_eqn = False
    for j, p in enumerate(PRIMES):
        if (encode(HC % M64, U64)[j] + m % p - m2 % p) % p \
                != encode(hc_scratch % M64, U64)[j]:
            ok_chan = False
check("eqn 3 == HC + m - m' == from-scratch mod 2^64-1 (500 updates)",
      ok_eqn)
check("per-channel update HC'_p = HC_p + m_p - m'_p exact, 7 channels",
      ok_chan)

print()
print("=" * 68)
print("VI. THE COMPARATOR LAW HOLDS SUB-BIT, FAMILY-WIDE (P6)")
print("=" * 68)

SQ = sum(M64 // p for p in PRIMES)
ratio = SQ / M64
print(f"  SQ = {SQ}; SQ/N = {ratio:.6f}; "
      f"log2(N/SQ) = {math.log2(M64 / SQ):.3f} bits")
check("gcd(N, SQ) = 1 (the forced-coprimality rule's instance)",
      math.gcd(M64, SQ) == 1)
check("sum 1/p < 1 but sub-bit: bit_length(SQ) = bit_length(N) = 64 "
      "-- zero whole-bit savings",
      SQ < M64 and SQ.bit_length() == 64 and M64.bit_length() == 64)

# The packed key (explore_rns_comparator.py reference construction).
Ninv = mod_inverse(M64 % SQ, SQ)
CFS = tuple((-Ninv * (M64 // p)) % SQ for p in PRIMES)


def key(x):
    D = sum(cp * (x % p) for cp, p in zip(CFS, PRIMES)) % SQ
    return D * 3 + x % 3


ok_adj = all(key(x) < key(x + 1)
             for x in (random.randrange(0, M64 - 1)
                       for _ in range(100_000)))
ok_rand = True
for _ in range(50_000):
    a, b = random.randrange(0, M64), random.randrange(0, M64)
    if (key(a) < key(b)) != (a < b) or (key(a) == key(b)) != (a == b):
        ok_rand = False
check("packed key strictly monotone (100,000 adjacent + 50,000 "
      "random pairs)", ok_adj and ok_rand)

# Family sweep: every member's sum 1/p stays under 0.6 (the tail
# 1/257 + ... only shrinks the headroom by epsilon).
members = {2: [3, 5], 3: [3, 5, 17], 4: [3, 5, 17, 257],
           5: [3, 5, 17, 257, 65537], 6: list(PRIMES)}
sweeps = {n: sum(1 / p for p in ps) for n, ps in members.items()}
for n, s in sweeps.items():
    print(f"  n = {n}: sum 1/p = {s:.6f}")
check("sum 1/p < 0.6 < 1 at every member n = 2..6 (the law clears "
      "family-wide, never by a whole bit)",
      all(s < 0.6 for s in sweeps.values()))

print()
print("=" * 68)
print("VII. THE ECC PAYLOAD IS THE CHECKSUM RING (P7)")
print("=" * 68)

D_PROD = math.prod(PRIMES[i] for i in U64.data_channels)
check("tower split: data = (3,5,17,257), parity = (641,65537,6700417)",
      U64.data_channels == (0, 1, 2, 3)
      and tuple(PRIMES[i] for i in U64.parity_channels)
      == (641, 65537, 6700417))
check("data product = 65535 = 2^16-1: the payload IS the "
      "internet-checksum ring (n = 4); rate 4/7 channels, a "
      "16-bit-word payload (0xFFFF == 0x0000 identified)",
      D_PROD == M16 and M16.bit_length() == 16)

# Zero slack: min product over all 35 4-subsets IS the data product.
prods4 = [math.prod(S) for S in combinations(PRIMES, 4)]
check("min 4-subset product = 65535 = data product (the tower "
      "split's slack-free boundary, all 35 subsets)",
      min(prods4) == D_PROD == M16)

# d = 4 exactly: a 3-agreement witness exists; one more data value
# would create a 4-agreement (d = 3).
w3 = 5 * 17 * 257  # 21845 < 65535: codewords 0 and 21845 agree on 3
cw0, cw1 = encode(0, U64), encode(w3, U64)
agree3 = sum(a == b for a, b in zip(cw0, cw1))
cw_kill = encode(M16, U64)  # the 65536th value: agrees with 0 on 4
agree4 = sum(a == b for a, b in zip(cw0, cw_kill))
check("d = 4 exactly: 0 vs 21845 agree on 3 channels; the 65536th "
      "value (65535) would agree with 0 on 4 -- zero slack is sharp",
      agree3 == 3 and agree4 == 4)

# Single-error correction on random codewords, every channel hit.
ok_ecc = True
for t in range(200):
    data = random.randrange(0, D_PROD)
    cw = ecc_encode(encode(data, U64)[:4], U64)
    ch = t % 7 if t < 7 else random.randrange(7)
    p = PRIMES[ch]
    bad = list(cw)
    bad[ch] = (bad[ch] + random.randrange(1, p)) % p
    corrected, located = ecc_correct(tuple(bad), U64)
    if not ecc_detect(tuple(bad), U64) or corrected != cw or located != ch:
        ok_ecc = False
check("200 random single-channel errors: detected, located, "
      "corrected (every channel hit)", ok_ecc)

print()
print("=" * 68)
print("VIII. FLETCHER IS THE FAMILY'S CHECKSUM (P8)")
print("=" * 68)

check("the Fletcher moduli ARE members n = 3/4/5: 255 = 3*5*17 = "
      "2^(2^3)-1, 65535, 4294967295",
      255 == 3 * 5 * 17 == 2**8 - 1
      and 65535 == 3 * 5 * 17 * 257
      and 4294967295 == 3 * 5 * 17 * 257 * 65537)


def fletcher16(data):
    """The defining recurrences, mod 255 (1's-complement reading)."""
    A = B = 0
    for d in data:
        A = (A + d) % 255
        B = (B + A) % 255
    return A, B


ok_A, ok_B, ok_split = True, True, True
for _ in range(500):
    msg = [random.randrange(0, 256) for _ in range(random.randrange(1, 65))]
    A, B = fletcher16(msg)
    n = len(msg)
    if A != sum(msg) % 255:
        ok_A = False
    if B != sum((n - j) * d for j, d in enumerate(msg)) % 255:
        ok_B = False
    # both sums split: each channel computes its own Fletcher
    for p in (3, 5, 17):
        Ap = Bp = 0
        for d in msg:
            Ap = (Ap + d) % p
            Bp = (Bp + Ap) % p
        if Ap != A % p or Bp != B % p:
            ok_split = False
check("A = the plain sum mod 255 (500 random messages)", ok_A)
check("B = the position-weighted moment sum (N-i+1)*D[i] mod 255",
      ok_B)
check("both sums split per channel (3, 5, 17): each channel runs "
      "its own Fletcher", ok_split)

print()
print("=" * 68)
fails = [n for n, ok in CHECKS if not ok]
if fails:
    print(f"FAILURES ({len(fails)}): " + "; ".join(fails))
    sys.exit(1)
print(f"ALL CHECKS PASSED ({len(CHECKS)})")
