"""
Moment resonance chain through the primorial tower.

Two possible interpretations of "n-th moment over units":
  A) Power moment:    M(n) = E[cos^n(2*pi*x/N)]     (cos raised to n)
  B) Frequency moment: F(n) = E[cos(2*pi*n*x/N)]     (cos at frequency n)

B is the Ramanujan sum c_N(n)/phi(N). For squarefree N it factors as:
  c_p(n) = p-1 if p|n, else -1.
  c_N(n) = product over p|N of c_p(n).
  F(n) = c_N(n) / phi(N).

This has an exact "lights up when p|n" structure.
"""

from math import cos, pi, gcd

def units(N):
    return [x for x in range(N) if gcd(x, N) == 1]

def ramanujan_sum(n, primes_of_N):
    result = 1
    for p in primes_of_N:
        if n % p == 0:
            result *= (p - 1)
        else:
            result *= -1
    return result

def main():
    rings = [
        (30,     [2, 3, 5]),
        (210,    [2, 3, 5, 7]),
        (2310,   [2, 3, 5, 7, 11]),
        (510510, [2, 3, 5, 7, 11, 13, 17]),
    ]

    for N, primes in rings:
        U = units(N)
        phi = len(U)

        print(f"\nZ/{N}  primes={primes}, phi={phi}")
        print(f"{'n':>4} {'F(n) computed':>16} {'F(n) Ramanujan':>16}"
              f" {'match':>5} {'p|n':>15}")
        print("-" * 75)

        for n in range(1, 36):
            f_comp = sum(cos(2 * pi * n * x / N) for x in U) / phi
            c_N = ramanujan_sum(n, primes)
            f_ram = c_N / phi

            match = abs(f_comp - f_ram) < 1e-10
            divs = [p for p in primes if n % p == 0]
            div_str = ",".join(str(p) for p in divs) if divs else "-"
            marker = ""
            if abs(f_comp) > 0.01:
                marker = " <<"

            print(f"{n:>4} {f_comp:>16.10f} {f_ram:>16.10f}"
                  f" {'OK' if match else 'FAIL':>5} {div_str:>15}{marker}")

    # Self-resonance
    print()
    print("=" * 60)
    print("SELF-RESONANCE: F(p) for each ring prime p")
    print("=" * 60)

    N = 510510
    primes = [2, 3, 5, 7, 11, 13, 17]
    phi = 92160

    for p in primes:
        c = ramanujan_sum(p, primes)
        f = c / phi

        # the formula: c_p(p) = p-1, c_q(p) = -1 for q != p
        # so c_N(p) = (p-1) * product_{q != p} (-1)
        # = (p-1) * (-1)^6 = (p-1) for 7 primes (6 others)
        num_others = len(primes) - 1
        expected_c = (p - 1) * ((-1) ** num_others)

        print(f"  p={p:>2}: c_N(p) = {c:>10,}, F(p) = {f:>14.10f},"
              f"  (p-1)*(-1)^{num_others} = {expected_c:>10}")

    print()
    print("=" * 60)
    print("RESONANCE LADDER")
    print("=" * 60)
    print()
    print("When ALL ring primes divide n (i.e., N | n):")

    for N, primes in rings:
        phi_N = 1
        for p in primes:
            phi_N *= (p - 1)
        c_all = 1
        for p in primes:
            c_all *= (p - 1)
        # c_all = phi(N)
        f_all = c_all / phi_N
        print(f"  Z/{N}: F(N) = phi(N)/phi(N) = {f_all}")

    print()
    print("When NO ring prime divides n (gcd(n,N) = 1):")
    for N, primes in rings:
        phi_N = 1
        for p in primes:
            phi_N *= (p - 1)
        c_none = (-1) ** len(primes)
        f_none = c_none / phi_N
        k = len(primes)
        print(f"  Z/{N}: F(n) = (-1)^{k}/phi = {f_none:.2e}"
              f"  (Mobius: mu(N) = {(-1)**k})")

    print()
    print("When exactly one ring prime p divides n:")
    N = 510510
    primes = [2, 3, 5, 7, 11, 13, 17]
    phi = 92160
    for p in primes:
        c = (p - 1) * ((-1) ** (len(primes) - 1))
        f = c / phi
        print(f"  p={p:>2}: F(n) = {f:>14.10f}  =  (p-1) * (-1)^6 / phi"
              f"  =  {p-1}/{phi}")

    print()
    print("=" * 60)
    print("THE RESONANCE STRUCTURE")
    print("=" * 60)
    print()
    print("F(n) = c_N(n) / phi(N)")
    print("     = product_{p|N} [(p-1) if p|n else -1] / product_{p|N} (p-1)")
    print("     = product_{p|N} [1 if p|n else -1/(p-1)]")
    print()
    print("Each channel p contributes factor:")
    print("  1      if p | n  (resonance: channel p is 'on')")
    print("  -1/(p-1) if p !| n  (anti-resonance: channel p is 'off')")
    print()
    print("So F(n) separates into 'on' and 'off' channels:")

    for n in [1, 2, 3, 5, 6, 7, 10, 11, 14, 15, 21, 30, 35, 42, 210]:
        on = [p for p in primes if n % p == 0]
        off = [p for p in primes if n % p != 0]
        f = 1.0
        for p in off:
            f *= (-1.0 / (p - 1))
        on_str = ",".join(str(p) for p in on) if on else "-"
        off_str = ",".join(str(p) for p in off) if off else "-"
        print(f"  n={n:>3}: on={on_str:>20}, off={off_str:>20},"
              f" F = {f:>14.10f}")

if __name__ == "__main__":
    main()
