"""explore_fermat_reciprocal_tail.py -- does the exact comparator's cost
law clear at EVERY member of the Fermat-spine family, or only at the
six members swept?

QUESTION. The machine-word towers Z/(2^(2^n) - 1) = Z/(F_0 F_1 ... F_(n-1))
carry the exact comparator's cost law (explore_rns_comparator.py: the
packed key beats reconstruction iff sum 1/p < 1 over the channels).
explore_uint64_tower.py swept the members n = 2..6 and read sum 1/p <
0.6 at each, then left the all-n statement OPEN "alongside the
factorizations themselves" -- every later member adds the reciprocals
of F_(n-1)'s prime factors, and F_m is unfactored from m = 12 on. Is
the all-n statement really hostage to the factorizations?

DESIGN. It is not: the reciprocal sum of an UNFACTORED F_k is bounded
without its factors. Two classical inputs. (1) Lucas (1878): for
k >= 2 every prime factor of F_k is == 1 mod 2^(k+2). (2) F_k <
2^(2^k + 1), so the number m of distinct prime factors satisfies
m (k+2) <= 2^k. Hence the j-th prime factor, in increasing order, is
at least j 2^(k+2) + 1, and
    sum_{p | F_k} 1/p  <  H_m / 2^(k+2),   m = floor(2^k / (k+2)),
H_m the harmonic number (H_m <= 1 + ln m). That bound is summable in
k, and from k = 12 on it is tiny. Below 12 the factorizations are
complete and classical -- F_5 (Euler 1732), F_6 (Landry 1880), F_7
(Morrison-Brillhart 1970), F_8 (Brent-Pollard 1980), F_9
(Lenstra-Lenstra-Manasse-Pollard 1990), F_10 (Brent 1995), F_11
(Brent 1988, cofactor primality by Morain) -- and the script does not
TRUST the table: each listed factor is checked to divide, and every
cofactor is checked prime by sympy.isprime (BPSW; the literature's
certificates are the classical contact, the script's check is the
control). The exact contributions of F_0..F_11 plus the tail bound
from k = 12 give an upper bound on the LIMIT sum; every member's sum
is a partial sum of it, monotone in n.

PREDICTIONS, fixed before the run (hand-derived first):
  P1. The tail bound sum_{k >= 12} H_m / 2^(k+2) is below 0.001
      (hand: ~0.0008).
  P2. F_6..F_11 contribute below 3e-5 in total (hand: ~2.4e-5, the
      small factors 274177, 2424833, 319489, 974849 dominating).
  P3. The limit bound lands below 0.6 (hand: ~0.5985) -- so the cost
      law clears at every member, and the all-n statement is a RULE
      (proved from the two classical inputs plus the table), not open.
  KILL OBSERVABLE: the printed LIMIT BOUND at or above 0.6. Then the
  statement stays open and the record's clause stands as written.
  CONTROL: the six swept members' sums must reproduce
  explore_uint64_tower.py's printed 0.533333 / 0.592157 / 0.596048 /
  0.596063 / 0.597623 (n = 2..6).

FINDINGS (post-run edit, copied from the printed output).
  F1. The table reproduces: every listed factor divides its F_k and is
      prime, every cofactor is prime under BPSW (1, 1, 2, 3, 5, 7, 14,
      22, 62, 99, 252, 564 digits), every factor of F_k, k >= 2, is
      == 1 mod 2^(k+2). 47 table checks green.
  F2. Member sums n = 2..12: 0.533333, 0.592157, 0.596048, 0.596063,
      0.597623, 0.597627 (x5), 0.597632 -- the control reproduces the
      six printed sums to the digit. F_6..F_11 contribute 8.24e-06
      (P2 held; the hand estimate 2.4e-5 was the cruder omega/smallest
      bound).
  F3. Tail bound sum_(k=12..400) H_m / 2^(k+2) = 0.000892, the k = 12
      term (m = 292) 0.000408 of it; remainder past k = 400 below
      (K+2)/2^(K+2) = 4e-119 (P1 held).
  F4. LIMIT BOUND 0.598523 < 0.6 (P3 held, margin 0.0015): the cost
      law sum 1/p < 0.6 holds at EVERY member n >= 2 of the
      Fermat-spine family -- RULE, proved from Lucas's congruence and
      the size of F_k, the factorizations past F_11 never consulted.
      The squarefree question (whether the all-field channels survive
      past n = 6) is untouched and stays open.

RUN RECORD. python prime/code/explore_fermat_reciprocal_tail.py --
0.3 s, memory trivial; 53 checks, 0 failed.
"""

import math
from fractions import Fraction

from sympy import isprime

FAILS = 0
N_CHECKS = 0


def check(name, ok):
    global FAILS, N_CHECKS
    N_CHECKS += 1
    if not ok:
        FAILS += 1
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


def fermat(k):
    return 2 ** (2 ** k) + 1


# The classical table: the listed factors of F_k in increasing order;
# the remaining cofactor (F_k divided by them) must be prime.
LISTED = {
    0: [], 1: [], 2: [], 3: [], 4: [],
    5: [641],
    6: [274177],
    7: [59649589127497217],
    8: [1238926361552897],
    9: [2424833, 7455602825647884208337395736200454918783366342657],
    10: [45592577, 6487031809,
         4659775785220018543264560743076778192897],
    11: [319489, 974849, 167988556341760475137,
         3560841906445833920513],
}

print("=" * 68)
print("I. THE TABLE F_0..F_11, VERIFIED RATHER THAN TRUSTED")
factors = {}
for k in range(12):
    n = fermat(k)
    cof = n
    fs = []
    for q in LISTED[k]:
        check(f"F_{k}: {q} divides and is prime", cof % q == 0 and isprime(q))
        cof //= q
        fs.append(q)
    check(f"F_{k}: cofactor ({len(str(cof))} digits) is prime", isprime(cof))
    fs.append(cof)
    check(f"F_{k}: product of the listed primes is F_{k}",
          math.prod(fs) == n and len(set(fs)) == len(fs))
    factors[k] = fs
    if k >= 2:
        check(f"F_{k}: every factor == 1 mod 2^{k + 2} (Lucas)",
              all((q - 1) % 2 ** (k + 2) == 0 for q in fs))

print()
print("=" * 68)
print("II. THE MEMBER SUMS n = 2..12 (partial sums of the limit)")
contrib = {k: sum(Fraction(1, q) for q in factors[k]) for k in range(12)}
member = {}
running = Fraction(0)
for k in range(12):
    running += contrib[k]
    member[k + 1] = running
for n in range(2, 13):
    print(f"  n = {n:2d}: sum 1/p = {float(member[n]):.6f}")
printed = [0.533333, 0.592157, 0.596048, 0.596063, 0.597623]
check("control: members n = 2..6 reproduce explore_uint64_tower.py's "
      "printed sums to six decimals",
      all(round(float(member[n]), 6) == v for n, v in zip(range(2, 7), printed)))
late = float(sum(contrib[k] for k in range(6, 12)))
print(f"  F_6..F_11 contribute {late:.2e}")
check("P2: F_6..F_11 contribute below 3e-5", late < 3e-5)

print()
print("=" * 68)
print("III. THE TAIL BOUND k >= 12 -- no factorization needed")


def tail_term(k):
    m = (2 ** k) // (k + 2)
    harmonic = 1.0 + math.log(m)  # H_m <= 1 + ln m
    return harmonic / 2 ** (k + 2)


K_MAX = 400
tail = sum(tail_term(k) for k in range(12, K_MAX + 1))
# Beyond K_MAX: 1 + ln m <= 1 + k ln 2 <= k for k >= 4, so every term is
# below k / 2^(k+2), and sum_{k > K} k / 2^(k+2) = (K+2) / 2^(K+2).
remainder = (K_MAX + 2) / 2.0 ** (K_MAX + 2)
tail_bound = tail + remainder
print(f"  sum_(k=12..{K_MAX}) H_m / 2^(k+2) = {tail:.6f}  (+ remainder <= {remainder:.1e})")
check("P1: the tail bound is below 0.001", tail_bound < 0.001)
check("the tail's first term (k = 12) already dominates: m = "
      f"{(2 ** 12) // 14}, term {tail_term(12):.6f}",
      tail_term(12) > 0.4 * tail)

print()
print("=" * 68)
print("IV. THE LIMIT BOUND")
limit_bound = float(member[12]) + tail_bound
print(f"  sum through F_11: {float(member[12]):.6f}")
print(f"  LIMIT BOUND     : {limit_bound:.6f}")
check("P3: the limit bound is below 0.6 -- the cost law clears at every "
      "member n >= 2 of the Fermat-spine family (rule, proved)",
      limit_bound < 0.6)
check("and below 1 by a wide margin: every member's comparator beats "
      "reconstruction, never by a whole bit (log2(1/0.6) < 1)",
      limit_bound < 1 and math.log2(1 / limit_bound) < 1)

print()
print(f"{N_CHECKS} checks, {FAILS} failed")
raise SystemExit(1 if FAILS else 0)
