"""explore_double_birth.py — the ledger's serial law: one new prime power
per lambda jump, characterized as record disjointness and searched far.

THE QUESTION. The tower's complexity ledger holds one unproved singleton
law: on the primorial schedule, every lambda jump introduces EXACTLY ONE
new prime power (rule, verified k <= 10^4 — never two at once). What IS
that law, and how far does it hold?

THE CHARACTERIZATION (theorem, hand-proved before this script existed).
Write f(m) = least prime p with p ≡ 1 (mod m). On the primorial schedule
lambda_k = lcm(p_i - 1 : i <= k), so v_q(lambda_k) = max over p' <= p_k
of v_q(p' - 1). Adding the prime p bumps base q (raises v_q(lambda))
  iff  v_q(p - 1) > v_q(p' - 1) for every prime p' < p
  iff  no prime below p is ≡ 1 (mod q^v), v = v_q(p - 1)
  iff  p = f(q^v).
And if p = f(q^j) for ANY j >= 1: no earlier prime is ≡ 1 (mod q^j),
hence none is ≡ 1 (mod q^v) either (j <= v and q^j | q^v), so p = f(q^v)
and p bumps q. So: p bumps base q iff p lies in the RECORD SET
R_q = {f(q^j) : j >= 1}, and the new prime power is then q^{v_q(p-1)}.
COROLLARY: the singleton law holds for all k iff the record sets R_q are
PAIRWISE DISJOINT across bases q. A violation — a "double birth" — is a
prime p with p = f(m1) = f(m2) for prime powers m1, m2 of distinct bases.

THE COVERAGE LEMMA (hand-proved). If p is a double birth with witnesses
m1, m2, then m1*m2 | p - 1 (coprime, both divide), so min(m1, m2) <=
sqrt(p - 1). Hence a search that (a) computes f(m) for every prime power
m <= X, and (b) for each record prime p = f(m) in that table factors the
cofactor t = (p-1)/m and checks, for every prime r | t with r != base(m),
that p > f(r^{v_r(p-1)}) — note v_r(p-1) = v_r(t), so the check is cheap
— is COMPLETE for every double-birth prime p with p - 1 < X^2. The
margin p / f(r^{v_r(t)}) >= 1 is the observable; margin 1 IS a double
birth. (For r = base(m), extra factors of the base in t raise the same
base's record level — one prime power, not a collision.)

PREDICTIONS DB1-DB4 (fixed before the run; hand-worked above and below;
the findings section enters by a separate post-run edit):

  DB1 (positive control, must pass before any verdict is read). A direct
    tower walk to k = 2000 — lambda as a factored dict, jumps read off
    valuation increases — agrees with the record test jump-for-jump:
    identical bumped-base sets at every k, and the previously recorded
    totals: 438 new-prime jumps + 30 power-bump jumps
    (explore_density_extended.py's schedule walk).
    Hand checks: p=3 bumps 2 (f(2)=3); p=5 bumps 2 at level 2 (f(4)=5);
    p=7 bumps 3 (f(3)=7); p=13 bumps NOTHING (12 = 4*3, f(4)=5 < 13,
    f(3)=7 < 13, and lcm(1,2,4,6,10) = 60 already holds 12).

  DB2 (the search). No double birth among all prime powers m <= X
    (X = 10^6 default, extended if wall-clock allows): every f-value
    bucket holds one base, and every cofactor margin is > 1. By the
    coverage lemma this certifies the singleton law for EVERY prime
    p <= X^2 (10^12 at the default), a ~10^7x extension of the verified
    range (k <= 10^4 reaches p = 104729).

  DB3 (closest calls). The minimum cofactor margin is 7/3, at p = 7 =
    f(3) with t = 2, m2 = 2, f(2) = 3 (hand-derived); margins grow with
    p with no drift toward 1 at scale. The top-20 smallest margins
    concentrate at tiny p.

  DB4 (the price — why the law is heuristically true yet a proof is out
    of reach). For a record prime p = f(m1), a second base needs a prime
    power m2 | t = (p-1)/m1 with NO prime below p ≡ 1 (mod m2);
    heuristically P ~ exp(-pi(p)/phi(m2)). Typically t = O(polylog p),
    so m2 <= t is polylog and each term is exp(-p/polylog p); a balanced
    split m1 ~ m2 ~ sqrt(p) instead prices EACH record at
    exp(-c*sqrt(p)/log p). Summing over p converges fast with all mass
    at the first few primes — so the law should hold for ALL p, while
    any proof would need least-prime-in-AP control (that f(m2) < p for
    one specific m2) at every scale at once, the same wall the corpus's
    other Linnik contacts name. The empirical margin table is the shape
    check on this heuristic.

KILL OBSERVABLE (frozen). The rig PRINTS "DOUBLE BIRTH" with p, m1, m2
if any f-bucket holds two bases or any cofactor margin equals 1. What a
hit would MEAN is weighed after the run, not here.

RESOURCES. One process; memory flat (no value table — the margin scan
is the detector, see search()); wall-clock ~1 s at X = 10^6, ~11 s at
10^7, ~130 s at 10^8 (peak 203 MB under the watchdog). Deterministic MR
bases valid far beyond every value touched.

FINDINGS (entered post-run from printed output; runs at X = 10^6, 10^7,
10^8, control identical in all three).

  DB1 PASS. "control k<=2000: new-prime jumps 438, power-bump jumps 30"
    — the previously recorded totals, and the characterization matched the direct
    valuation walk jump-for-jump (no CHARACTERIZATION MISMATCH line, a
    per-prime assertion over all 2000).

  DB2 PASS — THE LAW HOLDS TO 10^16 (rule, verified). At X = 10^8:
    "search X=100000000: 5762848 record primes over 5761455 bases;
    double births: 0", with "largest cofactor t = 284 at
    p = 20829174293, m = 73342163" — every record's cofactor sits seven
    orders of magnitude under the 10^10 bound the scan's completeness
    needs, asserted per record. By the coverage lemma this is COMPLETE for every
    double-birth prime p with p - 1 < 10^16: no lambda jump below that
    height introduces two new prime powers. The prior verified range was
    k <= 10^4 (p = 104729); this is ~10^11 times higher.

  DB3 PASS. Smallest cofactor margin 2.333 = 7/3 at p = 7, m = 3,
    m2 = 2 — exactly the hand-derived minimum — then 11/3, 29/5, 19/3,
    23/3, ... The top-20 closest calls all sit at p < 600, so every
    margin beyond them — every record prime above 600 — is at least
    34.6: nothing drifts toward 1 at scale, the shape DB4's heuristic
    predicts.

  DB4 stands as argued (heuristic, not a run result): the expected
    number of double births converges with its mass at the first few
    primes, all of which are enumerated clean, so the law should hold
    for ALL p — while a proof would need least-prime-in-AP control at
    every scale at once, which no current technology gives.

VERDICT. The singleton law is now a THEOREM-SHAPED reduction (the
record characterization and the disjointness reformulation are proved)
carrying a verified range of p <= 10^16 and a convergent-price
heuristic for the rest. The serial ledger — the tower's modulus learns
exactly one prime power per jump — is record disjointness of the
least-prime-in-AP function across prime-power progressions.
"""

import sys

# ---------------------------------------------------------------- primality
# Deterministic Miller-Rabin for n < 3.3 * 10^24 with the fixed base set
# below (valid for n < 3,317,044,064,679,887,385,961,981 — Sorenson/Webster).
_MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
_SMALL_PRIMES = []


def _sieve_small(limit):
    bs = bytearray([1]) * (limit + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(limit ** 0.5) + 1):
        if bs[i]:
            bs[i * i:: i] = b"\x00" * len(bs[i * i:: i])
    return [i for i in range(limit + 1) if bs[i]]


def is_prime(n):
    if n < 2:
        return False
    for p in _SMALL_PRIMES[:25]:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in _MR_BASES:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


_f_cache = {}


def f(m, cache=True):
    """Least prime ≡ 1 (mod m)."""
    if m in _f_cache:
        return _f_cache[m]
    cand = 1 + m
    while True:
        if is_prime(cand):
            if cache:
                _f_cache[m] = cand
            return cand
        cand += m


# ------------------------------------------------------- DB1: the control
def control(K=2000):
    """Direct tower walk vs the record characterization, k <= K."""
    # first K primes
    primes = []
    n = 2
    while len(primes) < K:
        if is_prime(n):
            primes.append(n)
        n += 1
    lam = {}  # prime -> exponent, lambda as a factored dict
    new_prime_jumps = power_bump_jumps = 0
    for idx, p in enumerate(primes):
        # factor p - 1
        m, fac = p - 1, {}
        for q in _SMALL_PRIMES:
            while m % q == 0:
                fac[q] = fac.get(q, 0) + 1
                m //= q
            if q * q > m:
                break
        if m > 1:
            fac[m] = fac.get(m, 0) + 1
        bumped_walk = [q for q, e in fac.items() if e > lam.get(q, 0)]
        # record test: p bumps q iff p == f(q^{v_q(p-1)})
        bumped_rec = [q for q, e in fac.items() if f(q ** e) == p]
        if sorted(bumped_walk) != sorted(bumped_rec):
            print("CHARACTERIZATION MISMATCH at p =", p,
                  bumped_walk, bumped_rec)
            return False
        if len(bumped_walk) > 1:
            print("DOUBLE BIRTH in control at p =", p, bumped_walk)
        if len(bumped_walk) == 1:
            q = bumped_walk[0]
            if q in lam:
                power_bump_jumps += 1
            else:
                new_prime_jumps += 1
        for q, e in fac.items():
            if e > lam.get(q, 0):
                lam[q] = e
    print(f"  control k<={K}: new-prime jumps {new_prime_jumps}, "
          f"power-bump jumps {power_bump_jumps} "
          f"(recorded: 438 + 30 at k<=2000)")
    return new_prime_jumps == 438 and power_bump_jumps == 30


# ------------------------------------------------- DB2/DB3: the far search
def search(X):
    """f(m) for every prime power m <= X; cofactor-margin detection.

    A value collision f(m1) = f(m2) = p across bases is EQUIVALENT to a
    margin-1 hit in the cofactor scan: m2's base divides t = (p-1)/m1,
    and p = f(m2) forces p = f(base^{v(t)}) (the characterization above),
    which the scan tests directly. So no value table is kept, the scan
    also sees witnesses m2 > X, and memory stays flat.
    """
    sieve = bytearray([1]) * (X + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(X ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:: i] = b"\x00" * len(sieve[i * i:: i])
    margins = []  # (margin, p, m, m2) smallest cofactor margins
    n_records = 0
    n_bases = 0
    double = 0
    max_t = (0, 0, 0)  # largest cofactor seen: (t, p, m)
    for q in range(2, X + 1):
        if not sieve[q]:
            continue
        n_bases += 1
        m = q
        seen = set()
        while m <= X:
            p = f(m, cache=(m <= 100000))
            if p not in seen:
                seen.add(p)
                n_records += 1
                # cofactor margins: t = (p-1)/m, other-base prime powers.
                # The remnant after trial division by primes <= 10^5 is a
                # prime power ONLY if t < 10^10 (a remnant with two
                # distinct prime factors > 10^5 would exceed 10^10), so
                # the completeness of this scan REQUIRES the bound below.
                t = (p - 1) // m
                assert t < 10 ** 10, (p, m, t)
                if t > max_t[0]:
                    max_t = (t, p, m)
                tt = t
                for r in _SMALL_PRIMES:
                    if r * r > tt:
                        break
                    if tt % r == 0:
                        e = 0
                        while tt % r == 0:
                            tt //= r
                            e += 1
                        if r != q:
                            fr = f(r ** e)
                            if fr == p:
                                print("DOUBLE BIRTH (margin):",
                                      p, m, r ** e)
                                double += 1
                            if p < fr * 1000:
                                margins.append((p / fr, p, m, r ** e))
                if tt > 1 and tt != q:
                    # tt is prime here (cofactor remnant after the loop)
                    fr = f(tt)
                    if fr == p:
                        print("DOUBLE BIRTH (margin):", p, m, tt)
                        double += 1
                    if p < fr * 1000:
                        margins.append((p / fr, p, m, tt))
            m *= q
    margins.sort()
    print(f"  search X={X}: {n_records} record primes over "
          f"{n_bases} bases; double births: {double}")
    print(f"  largest cofactor t = {max_t[0]} at p = {max_t[1]}, "
          f"m = {max_t[2]} (completeness needs t < 10^10 at every "
          f"record: asserted)")
    print("  coverage: complete for every double-birth prime p with "
          f"p - 1 < {X}^2 = {X*X}")
    print("  20 smallest cofactor margins (margin, p, m, m2):")
    for row in margins[:20]:
        print("   ", f"{row[0]:.3f}", row[1], row[2], row[3])
    return double == 0


def main():
    global _SMALL_PRIMES
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
    _SMALL_PRIMES = _sieve_small(100000)
    import time
    t0 = time.time()
    ok1 = control(2000)
    print(f"  [control {time.time()-t0:.1f}s]")
    print("DB1 control:", "PASS" if ok1 else "FAIL")
    if not ok1:
        print("POSITIVE CONTROL FAILED — no verdict may be read.")
        return
    t0 = time.time()
    ok2 = search(X)
    print(f"  [search {time.time()-t0:.1f}s]")
    print("DB2 search:", "no double birth" if ok2 else "HIT — see prints")


if __name__ == "__main__":
    main()
