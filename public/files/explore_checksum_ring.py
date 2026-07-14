"""
BUILD: THE INTERNET-CHECKSUM RING -- RFC 1071 lives in a designed
tower.

RFC 1071 (the IP/TCP/UDP checksum) sums 16-bit words in one's
complement: add, then fold the carry back in (end-around carry). Since
2^16 == 1 (mod 2^16 - 1), the fold is reduction mod 65535 -- the
checksum is arithmetic in Z/(2^16 - 1). The gem is what that modulus
IS: 65535 = 3 * 5 * 17 * 257, four distinct FERMAT primes -- a
squarefree all-field designed tower, the n = 4 member of
the nim index-ring family 2^(2^n) - 1 = F_0 ... F_(n-1) (the char-2
mirrors). Every internet packet checksums inside a
tower ring with the full blueprint. The mod-65535 reading of RFC 1071
is classical (the RFC's appendix, IEN 45, derives the checksum from
digit sums computing remainders mod radix - 1 -- never the phrase
"mod 2^16 - 1", but the same fact); the designed-tower reading --
field channels, parallel split, cheap collapse -- is the chart below.

Predictions (stated in advance of any run):
  P1. THE FOLD IS THE REDUCTION (rule, exhaustive). For EVERY 17-bit
      sum s in [0, 2^17 - 2] (the full range of one addition of two
      16-bit words), the end-around-carry fold satisfies
      fold(s) == s (mod 65535), with result in [0, 0xFFFF]. The two
      one's-complement zeros 0x0000 and 0xFFFF are the two
      representatives of the zero class. Multi-word accumulation
      (32-bit accumulator, fold twice -- the RFC's deferred-carry
      form) agrees with the word-sum mod 65535 on random packets.
      The final complement is RING NEGATION (~cs & 0xFFFF = 65535 -
      cs), so the transmitted field is -(sum of words) mod 65535 and
      receiver validity is the identity sum + checksum == 0: EVERY
      step of RFC 1071 is arithmetic in Z/65535.
  P2. THE MODULUS IS A DESIGNED TOWER (property, verified). 65535 =
      3 * 5 * 17 * 257, squarefree, all four channels prime fields;
      phi = 2*4*16*256 = 2^15; lambda = lcm(2,4,16,256) = 2^8 = 256;
      16 idempotents. The telescoping identity 2^(2^4) - 1 =
      F_0 F_1 F_2 F_3 ties it to the n = 4 nim rung (whose unit group
      is cyclic of exactly this order -- explore_nimber_tower.py).
  P3. THE CHECKSUM SPLITS BY CHANNEL (rule). Addition is
      channel-local, so the folded sum's residue mod p depends only
      on the words mod p: one packet checksum IS four independent
      field checksums (mod 3, 5, 17, 257) running in parallel by
      construction. Verified on random packets per channel.
  P4. THE CHEAP COLLAPSE (rule, lambda = 2^8). x^lambda = e_supp(x)
      in 8 squarings for every x (sampled + every idempotent hit by
      some x); the cheap-collapse knob of the Fermat family at n = 4.

RESULTS (the record; checks below encode the measured law):
  All four predictions CONFIRMED (12 checks). P1: exhaustive fold law
  over all 131,071 single-add sums, max one fold per add; 500 random
  packets (1..64 words), deferred-carry accumulator == word-sum mod
  65535 every time, complement = ring negation on every packet, RFC
  round-trip to 0. P2:
  factorization, telescoping, phi, lambda as stated (crt.py Ring +
  carmichael_lambda). P3: 500 packets x 4 channels -- per-channel
  word-sums mod p equal the folded checksum's channel residues
  exactly. P4: x^256 = e_supp(x) in 8 squarings, 2003 sampled x; all
  16 supports hit via constructed witnesses (residue 2 on the support,
  0 off it) -- random sampling provably cannot reach the rare small
  supports (a zero mod 17 AND 257 is ~1/4369 per draw), so the
  by-subset construction is the honest exhaustive. Two first-run check
  fixes were harness-side only (factorize's return format; the
  witness construction replacing sampling), no prediction moved.

Tier: rule (P1, P3, P4 -- exhaustive/sampled at the stated ranges;
P1's fold law and P3's locality are one-line algebra, the run is the
witness); property (P2, by construction). Classical contact: RFC 1071
states the mod-2^16-1 reading; Fermat-prime factorization of 2^16 - 1
is elementary. The designed-tower chart entry: the
char-2 mirrors.
"""

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import Ring, carmichael_lambda, decode, encode, factorize

random.seed(20260611)

M16 = 0xFFFF          # 2^16 - 1 = 65535
CHECKS = []


def check(name, ok):
    CHECKS.append((name, ok))
    print(("  PASS  " if ok else "  FAIL  ") + name)


def fold16(s):
    """RFC 1071 end-around carry: fold bits above 16 back in, repeat."""
    while s >> 16:
        s = (s & M16) + (s >> 16)
    return s


def rfc1071_checksum(words):
    """RFC 1071 deferred-carry form: wide accumulator, fold at the end.
    Returns the folded SUM (not yet complemented)."""
    acc = 0
    for w in words:
        acc += w
    return fold16(acc)


print("=" * 68)
print("I. THE FOLD IS THE REDUCTION (P1)")
print("=" * 68)

# Exhaustive: every possible single-addition sum of two 16-bit words.
ok_law, ok_range, max_folds = True, True, 0
for s in range(0, 2**17 - 1):
    t, folds = s, 0
    while t >> 16:
        t = (t & M16) + (t >> 16)
        folds += 1
    max_folds = max(max_folds, folds)
    if t % 65535 != s % 65535:
        ok_law = False
    if not (0 <= t <= 0xFFFF):
        ok_range = False
check("fold(s) == s mod 65535, ALL 131071 single-add sums", ok_law)
check("fold lands in [0, 0xFFFF]; max folds per add = 1",
      ok_range and max_folds == 1)
check("two zeros: 0x0000 and 0xFFFF both == 0 mod 65535",
      0x0000 % 65535 == 0 and 0xFFFF % 65535 == 0)

ok_acc, ok_compl = True, True
for _ in range(500):
    words = [random.randrange(0, 2**16)
             for _ in range(random.randrange(1, 65))]
    cs = rfc1071_checksum(words)
    if cs % 65535 != sum(words) % 65535:
        ok_acc = False
    # RFC convention: transmit ~cs; receiver folds data + checksum,
    # complements, expects 0.
    if (~fold16(cs + (~cs & M16)) & M16) not in (0,):
        ok_compl = False
    # The complement IS ring negation: ~cs & 0xFFFF = 65535 - cs, so
    # the transmitted field is -(sum of words) mod 65535.
    if (~cs & M16) % 65535 != (-cs) % 65535:
        ok_compl = False
check("deferred-carry accumulator == word-sum mod 65535 (500 packets)",
      ok_acc)
check("complement = ring negation (transmitted field = -sum); "
      "round-trips to 0", ok_compl)

print()
print("=" * 68)
print("II. THE MODULUS IS A DESIGNED TOWER (P2)")
print("=" * 68)

CHK = Ring("CHECKSUM", (3, 5, 17, 257), (1, 1, 1, 1))
fermat = [2**(2**k) + 1 for k in range(4)]          # F_0..F_3
check("65535 = 3*5*17*257, squarefree",
      factorize(65535) == {3: 1, 5: 1, 17: 1, 257: 1})
check("all four factors are Fermat primes F_0..F_3",
      fermat == [3, 5, 17, 257])
check("telescoping: 2^(2^4) - 1 = F_0*F_1*F_2*F_3",
      2**16 - 1 == fermat[0] * fermat[1] * fermat[2] * fermat[3])
check("phi = 2^15, lambda = 2^8, 16 idempotents",
      CHK.phi == 2**15 and CHK.lam == 256
      and carmichael_lambda(65535) == 256 and CHK.num_idempotents == 16)

print()
print("=" * 68)
print("III. THE CHECKSUM SPLITS BY CHANNEL (P3)")
print("=" * 68)

ok_split = True
for _ in range(500):
    words = [random.randrange(0, 2**16)
             for _ in range(random.randrange(1, 65))]
    cs = rfc1071_checksum(words) % 65535
    for i, p in enumerate(CHK.primes):
        if sum(w % p for w in words) % p != encode(cs, CHK)[i]:
            ok_split = False
check("checksum mod p computable from words mod p alone, "
      "4 channels x 500 packets", ok_split)

print()
print("=" * 68)
print("IV. THE CHEAP COLLAPSE (P4)")
print("=" * 68)

def collapse(x):
    """x^256 via 8 squarings."""
    for _ in range(8):
        x = (x * x) % 65535
    return x

ok_col = True
sample = random.sample(range(65535), 2000) + [0, 1, 65534]
for x in sample:
    tgt = tuple(1 if r else 0 for r in encode(x, CHK))
    if encode(collapse(x), CHK) != tgt:
        ok_col = False
check("x^256 = e_supp(x) in 8 squarings (2003 sampled x)", ok_col)

# Every support subset, by constructed witness (residue 2 mod p on the
# support, 0 off it; 2 != 0 in every channel): collapse must land on
# exactly e_S -- random sampling cannot reach the rare small supports.
ok_all = True
for bits in range(16):
    S = tuple((bits >> i) & 1 for i in range(4))
    x = decode(tuple(2 * b % p for b, p in zip(S, CHK.primes)), CHK)
    if encode(collapse(x), CHK) != S:
        ok_all = False
check("all 16 supports: constructed witness collapses to its e_S",
      ok_all)

print()
print("=" * 68)
fails = [n for n, ok in CHECKS if not ok]
if fails:
    print(f"FAILURES ({len(fails)}): " + "; ".join(fails))
    sys.exit(1)
print(f"ALL CHECKS PASSED ({len(CHECKS)})")
