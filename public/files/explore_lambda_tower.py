"""
Lambda through the primorial tower.

For each rung k (product of first k primes), compute:
  - lambda = lcm(p_1 - 1, ..., p_k - 1)
  - phi = product of (p_i - 1)
  - jump factor = lambda(k) / lambda(k-1)
  - which primes are lambda-transparent (jump factor = 1)
  - new prime factors introduced by each p_k - 1
  - number of divisors of lambda (= achievable order levels)
  - plateau structure, Linnik ordering, transparency density
"""

from math import gcd, log
from sympy import factorint, prime, divisor_count

def lcm(a, b):
    return a * b // gcd(a, b)

def compute_tower(k_max):
    rows = []
    running_lcm = 1
    running_lcm_factors = {}
    running_phi = 1

    for k in range(1, k_max + 1):
        p = prime(k)
        pm1 = p - 1
        pm1_factors = factorint(pm1)

        prev_lcm = running_lcm
        running_lcm = lcm(running_lcm, pm1)
        running_phi *= pm1

        new_factors = {}
        for q, e in pm1_factors.items():
            old_e = running_lcm_factors.get(q, 0)
            if e > old_e:
                new_factors[q] = (old_e, e)

        for q, (old_e, new_e) in new_factors.items():
            running_lcm_factors[q] = new_e

        jump = running_lcm // prev_lcm if prev_lcm > 0 else running_lcm
        transparent = (jump == 1) and k > 1

        rows.append({
            'k': k, 'p': p, 'pm1': pm1,
            'pm1_factors': pm1_factors,
            'lambda': running_lcm, 'phi': running_phi,
            'jump': jump, 'transparent': transparent,
            'new_factors': new_factors,
            'lambda_factors': dict(running_lcm_factors),
            'num_divisors': int(divisor_count(running_lcm)),
        })

    return rows

def fmt(factors):
    if not factors:
        return "1"
    parts = []
    for p in sorted(factors):
        e = factors[p]
        parts.append(f"{p}^{e}" if e > 1 else str(p))
    return " * ".join(parts)

def main():
    K_MAX = 50

    print(f"PRIMORIAL TOWER: LAMBDA SEQUENCE (k=1..{K_MAX})")
    print("=" * 90)
    print()

    rows = compute_tower(K_MAX)

    # --- Table 1: the sequence ---
    print(f"{'k':>3} {'p':>4} {'p-1':>5} {'lambda':>14} {'jump':>6} {'trans':>5} {'#div':>5}")
    print("-" * 50)

    for r in rows:
        t = "YES" if r['transparent'] else ""
        print(f"{r['k']:>3} {r['p']:>4} {r['pm1']:>5} {r['lambda']:>14,} "
              f"{r['jump']:>6} {t:>5} {r['num_divisors']:>5}")

    print()

    # --- Table 2: what each prime contributes ---
    print("WHAT EACH PRIME CONTRIBUTES")
    print("-" * 70)
    for r in rows[:30]:
        pm1_str = fmt(r['pm1_factors'])
        if r['new_factors']:
            new_parts = []
            for q in sorted(r['new_factors']):
                old_e, new_e = r['new_factors'][q]
                if old_e == 0:
                    new_parts.append(f"{q}^{new_e}" if new_e > 1 else str(q))
                else:
                    new_parts.append(f"{q}^{old_e}->{q}^{new_e}")
            new_str = ", ".join(new_parts)
        else:
            new_str = "(transparent)"
        print(f"  k={r['k']:>2}, p={r['p']:>3}: p-1 = {pm1_str:>20}  new: {new_str}")

    print()

    # --- Plateau structure ---
    print("PLATEAU STRUCTURE")
    print("-" * 60)
    plateaus = []
    i = 0
    while i < len(rows):
        lam = rows[i]['lambda']
        start = i
        while i < len(rows) and rows[i]['lambda'] == lam:
            i += 1
        length = i - start
        if length >= 2:
            plateaus.append({
                'lambda': lam,
                'start_k': rows[start]['k'], 'end_k': rows[i-1]['k'],
                'start_p': rows[start]['p'], 'end_p': rows[i-1]['p'],
                'length': length,
            })

    for pl in plateaus:
        print(f"  lambda={pl['lambda']:>20,}: k={pl['start_k']}-{pl['end_k']}"
              f" (primes {pl['start_p']}-{pl['end_p']}), length {pl['length']}")

    print()

    # --- Lambda-prime ordering (Linnik) ---
    print("LAMBDA-PRIME ORDERING (Linnik function)")
    print("-" * 60)

    first_intro = {}
    for r in rows:
        for q in r['new_factors']:
            if q not in first_intro:
                first_intro[q] = (r['k'], r['p'])

    ordered = sorted(first_intro.items(), key=lambda x: x[1][0])
    for q, (k, p) in ordered:
        print(f"  q={q:>3} enters lambda at k={k:>2} via p={p:>3} (p-1={p-1})")

    print()
    print("Order inversions: 11 < 7, 23 < 13, 17 at k=27 (very late)")
    print()

    # --- Transparency density ---
    print("TRANSPARENCY DENSITY")
    print("-" * 40)
    for w in [10, 20, 30, 40, 50]:
        if w > K_MAX:
            break
        count = sum(1 for r in rows[:w] if r['transparent'])
        print(f"  k=1..{w}: {count}/{w} ({100*count/w:.0f}%)")

    print()

    # --- Growth rate ---
    print("GROWTH RATE: log(lambda)/log(phi)")
    print("-" * 40)
    for r in rows:
        if r['lambda'] > 1 and r['phi'] > 1:
            ratio = log(r['lambda']) / log(r['phi'])
            if r['k'] % 5 == 0 or r['k'] <= 10:
                print(f"  k={r['k']:>2}: {ratio:.4f}")

    print()

    # --- Lambda factorization at key rungs ---
    print("LAMBDA FACTORIZATION AT KEY RUNGS")
    print("-" * 60)
    for r in rows:
        if r['k'] in [4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50]:
            print(f"  k={r['k']:>2}: lambda = {fmt(r['lambda_factors']):>40}"
                  f"  ({r['num_divisors']} order levels)")

if __name__ == "__main__":
    main()
