"""The split free half layer by layer: the Chebotarev fingerprint of z(p).

THE QUESTION
------------
The apparition-density scan (explore_apparition_density.py) left one
ingredient unproved: at split p = 1 mod 4 with j = v2(p-1) >= 2, the
probability that v2(ord alpha) <= 1 was priced at 2^-(j-1) by naive
Kummer independence, and only the AGGREGATE density (1/3 generic,
7/24 Pell) was measured. The Hasse route settles it: the independence
is a THEOREM. Hasse's even/odd-order density method (Math. Ann. 166,
1966), run for the golden window by Lagarias (Pacific J. Math. 118,
1985; errata 162, 1994, touching only a 3-adic Laxton case) and for
every negative-norm quadratic unit by Moree (J. Theorie des Nombres
de Bordeaux 8, 1996), computes the density of {p : 2^e || z(p)} as an
alternating sum of reciprocal degrees of the fields
K_{r,s} = Q(sqrt D, theta^(1/2^r), zeta_{2^s}), theta = -alpha^2,
via the Chebotarev density theorem. The KUMMER-LAYER degrees -
adjoining 2-power roots of theta over the cyclotomic base - are
FULL, and the reason is the norm: N(alpha) = -1 is negative, hence
not a square in the real field Q(sqrt D), so Q(sqrt alpha)/Q is not
normal (Halter-Koch's criterion), which blocks every collapse in
that layer. The one collapse anywhere is classical and cyclotomic -
sqrt 2 inside Q(zeta_8) at D = 2 - and it moves only the joint
distribution of (split, v2(p-1)): that shift is the whole Pell
correction, and the free-half conditional it leaves untouched.
Moree's Theorem 3 then states exactly the scanned quantities:
density of z = 2 mod 4 is 1/3 for D > 2 and 7/24 for D = 2 -
unconditional theorems. (Our alpha at window a is a negative-norm
unit of O_D for D the squarefree kernel of a^2 + 4, D = 2 exactly on
the Pell family; any two such units are +- odd powers of one
fundamental unit and odd powers share v2(ord) at every prime, so the
theorem applies at every constant-a window.)

The theorem predicts more than the aggregate: a PER-LAYER grid the
old scan never read. For split p with j = v2(p-1) >= 2, Chebotarev
equidistribution in the Kummer tower gives the exact conditional
distribution of e = v2(z(p)):

    P(e = 0 | split, j) = 2^(1-j)      (v2(ord alpha) = 2)
    P(e = 1 | split, j) = 2^(1-j)      (v2(ord alpha) <= 1, the
                                        certificate cell)
    P(e = s | split, j) = 2^(s-j)      for 2 <= s <= j - 1
                                        (v2(ord alpha) = s + 1)

- summing to 1, IDENTICAL across generic and Pell windows (the
Pell correction lives entirely in the joint distribution of (split,
j), never in the layer conditionals; cross-checked cell-by-cell
against Moree's Tables I.1 and II.1). This grid is the theorem's
fingerprint, finer than any aggregate: does it hold at every layer?

THE DESIGN (predictions frozen before the run)
------------------------------------------------------------------
K0  Positive control: aggregate totals per window reproduce the
    parent scan - z = 2 mod 4 density within 0.002 of 1/3 (generic)
    / 7/24 (Pell) at 10^6. PREDICTION: green.
K1  Structural asserts on every split p = 1 mod 4: e = 0 or 1
    possible at every j; e >= 2 only with e <= j - 1 (since
    v2(ord alpha) <= j). PREDICTION: no violation (theorem).
K2  The layer grid: windows a in {1, 2, 3, 4, 5, 6, 7, 8, 10, 12,
    14, 82}, odd primes p <= 10^6, split p = 1 mod 4 bucketed by
    (j, e) for j = 2..6, e in {0, 1, 2, ..., 5, tail}. OBSERVABLE:
    measured conditional against the predicted cell, per window.
    PREDICTION: every cell with predicted count >= 100 sits within
    3 binomial sigma of its prediction; the kill-shape observable
    is any such cell beyond 5 sigma.
K3  Pell rows: no split p = 5 mod 8 exists (j = 2 row EMPTY at
    a = 2, 14, 82), and the j >= 3 conditionals match the SAME
    grid as generic windows. PREDICTION: j = 2 count is zero and
    every j >= 3 cell passes K2's band.

RESOURCE: pure Python, no numpy; sieve to 10^6 as bytearray;
O(log p) per prime. Estimate ~20 s, < 50 MB.

FINDINGS (entered after the run by a separate edit)
------------------------------------------------------------------
THE GRID HOLDS AT EVERY CELL. K0 green: all 12 aggregate densities
within 2e-3 of their theorem values (max |dev| 8.4e-4, a = 12). K1
green: no structural violation at any split p = 1 mod 4. K2: every
grid cell with predicted count >= 100 sits within 3 sigma of its
Chebotarev prediction - worst deviation anywhere 2.4 sigma (a = 5,
j = 4, e = 1); the 5-sigma kill-shape did not fire. K3 green: the
j = 2 row is EMPTY at a = 2, 14, 82 (no split p = 5 mod 8 exists
over Q(sqrt 2)) and every Pell j >= 3 cell passes the same band as
the generic grid - the layer conditionals are family-independent
exactly as the theorem says, the Pell correction living entirely in
the joint distribution of (split, j). The three Pell rows print
identical grids to the cell - the odd-power sharing law at work
(alpha = (1 + sqrt 2)^{1, 3, 5}).

TIERS. The layer grid law and the aggregate densities 1/3 and 7/24:
THEOREM - Hasse's method, executed by Lagarias (1985) at the golden
window and by Moree (1996, Theorem 3) for every negative-norm unit,
the Kummer degrees full because N(alpha) = -1 is not a square in
the real field Q(sqrt D). This run confirms the fingerprint at 12
windows, odd primes to 10^6, every cell within 3 sigma. What this
settles: the apparition densities were a pattern with one unproved
ingredient (the Kummer independence at split m = 1 mod 4); that
ingredient is a proved theorem, so the densities are theorems.

RUN RECORD (python prime/code/explore_kummer_layers.py, ~25 s;
verbatim):

odd primes to 1000000: 78497

K0 aggregate control (z = 2 mod 4 density vs 1/3 | 7/24)
  a= 1 D=   5  density 0.3337  pred 0.3333  |dev| 4.0e-04
  a= 2 D=   8  density 0.2922  pred 0.2917  |dev| 5.0e-04
  a= 3 D=  13  density 0.3335  pred 0.3333  |dev| 1.7e-04
  a= 4 D=  20  density 0.3337  pred 0.3333  |dev| 4.0e-04
  a= 5 D=  29  density 0.3333  pred 0.3333  |dev| 4.2e-05
  a= 6 D=  40  density 0.3331  pred 0.3333  |dev| 2.2e-04
  a= 7 D=  53  density 0.3332  pred 0.3333  |dev| 1.1e-04
  a= 8 D=  68  density 0.3334  pred 0.3333  |dev| 4.7e-05
  a=10 D= 104  density 0.3326  pred 0.3333  |dev| 7.4e-04
  a=12 D= 148  density 0.3342  pred 0.3333  |dev| 8.4e-04
  a=14 D= 200  density 0.2922  pred 0.2917  |dev| 5.0e-04
  a=82 D=6728  density 0.2922  pred 0.2917  |dev| 5.0e-04

K2/K3 layer grid: conditional P(e | split, j) vs 2^(1-j), 2^(1-j), 2^(e-j)
  a= 1 D=   5 split1mod4=19514 cells=14 worst |z|=1.7 sigma at (j=5,e=4)
  a= 2 D=   8 split1mod4=19552 cells=15 worst |z|=1.3 sigma at (j=5,e=2) (j2 empty)
  a= 3 D=  13 split1mod4=19561 cells=14 worst |z|=1.7 sigma at (j=4,e=0)
  a= 4 D=  20 split1mod4=19514 cells=14 worst |z|=1.7 sigma at (j=5,e=4)
  a= 5 D=  29 split1mod4=19529 cells=14 worst |z|=2.4 sigma at (j=4,e=1)
  a= 6 D=  40 split1mod4=19566 cells=14 worst |z|=1.0 sigma at (j=6,e=4)
  a= 7 D=  53 split1mod4=19521 cells=14 worst |z|=1.9 sigma at (j=3,e=1)
  a= 8 D=  68 split1mod4=19510 cells=14 worst |z|=1.1 sigma at (j=6,e=4)
  a=10 D= 104 split1mod4=19579 cells=14 worst |z|=2.1 sigma at (j=6,e=4)
  a=12 D= 148 split1mod4=19483 cells=14 worst |z|=1.3 sigma at (j=3,e=1)
  a=14 D= 200 split1mod4=19552 cells=15 worst |z|=1.3 sigma at (j=5,e=2) (j2 empty)
  a=82 D=6728 split1mod4=19552 cells=15 worst |z|=1.3 sigma at (j=5,e=2) (j2 empty)

verdict: every cell within 3 sigma

(the Pell rows show cells=15 where generic rows show 14: with every
split prime = 1 mod 8, the Pell large-j layers collect more samples
and one extra cell crosses the count-100 floor)
"""

import sys

BOUND = 10**6
WINDOWS = (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 82)
PELL = {2, 14, 82}
JMAX = 6  # layers j = 2..JMAX read against the grid


def sieve_primes(n):
    mark = bytearray([1]) * (n + 1)
    mark[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if mark[i]:
            mark[i * i :: i] = bytearray(len(mark[i * i :: i]))
    return [i for i in range(3, n + 1) if mark[i]]  # odd primes only


def u_pair(a, n, p):
    """(U_n, U_{n+1}) mod p by fast doubling."""
    u, v = 0, 1
    for bit in bin(n)[2:]:
        uu = (u * ((2 * v - a * u) % p)) % p
        vv = (u * u + v * v) % p
        u, v = uu, vv
        if bit == "1":
            u, v = v, (a * v + u) % p
    return u, v


def v2_of_z(a, p):
    """(v2(z(p)), chi) for odd prime p not dividing D = a*a+4.

    chi = +1 split, -1 inert. z | p - chi; strip the 2-part of
    N = p - chi down to the odd part m, then U_m = 0 mod p iff z | m
    (z's odd part always divides m); doubling back up locates v2(z).
    """
    D = a * a + 4
    chi = pow(D, (p - 1) // 2, p)
    chi = 1 if chi == 1 else -1
    N = p - chi
    e = (N & -N).bit_length() - 1
    m = N >> e
    u, v = u_pair(a, m, p)
    if u == 0:
        return 0, chi
    # z does not divide m: double until U hits zero; U_{2k} = U_k*(2U_{k+1} - a U_k)
    for t in range(1, e + 1):
        u, v = (u * ((2 * v - a * u) % p)) % p, (u * u + v * v) % p
        if u == 0:
            return t, chi
    raise AssertionError("z(p) found dividing neither m*2^e; rig bug")


def predicted(j, e):
    """P(v2(z) = e | split, v2(p-1) = j) from the Kummer layer theorem."""
    if e in (0, 1):
        return 2.0 ** (1 - j)
    if 2 <= e <= j - 1:
        return 2.0 ** (e - j)
    return 0.0


def main():
    primes = sieve_primes(BOUND)
    print("odd primes to %d: %d" % (BOUND, len(primes)))

    print("\nK0 aggregate control (z = 2 mod 4 density vs 1/3 | 7/24)")
    all_grids = {}
    for a in WINDOWS:
        D = a * a + 4
        total = 0
        yes = 0
        # grid[(j, e)] over split p = 1 mod 4; e capped at JMAX for bucketing
        grid = {}
        n_split1 = 0
        for p in primes:
            if D % p == 0:
                continue
            total += 1
            e, chi = v2_of_z(a, p)
            if e == 1:
                yes += 1
            if chi == 1 and p % 4 == 1:
                j = ((p - 1) & -(p - 1)).bit_length() - 1
                n_split1 += 1
                # K1 structural asserts
                assert e <= 1 or e <= j - 1, (a, p, j, e)
                if 2 <= j <= JMAX:
                    grid[(j, e)] = grid.get((j, e), 0) + 1
        pred = 7.0 / 24.0 if a in PELL else 1.0 / 3.0
        dens = yes / total
        dev = abs(dens - pred)
        assert dev < 2e-3, (a, dens, pred)
        print("  a=%2d D=%4d  density %.4f  pred %.4f  |dev| %.1e" % (a, D, dens, pred, dev))
        all_grids[a] = (grid, n_split1)

    print("\nK2/K3 layer grid: conditional P(e | split, j) vs 2^(1-j), 2^(1-j), 2^(e-j)")
    kill = False
    for a in WINDOWS:
        grid, n_split1 = all_grids[a]
        # per-j totals
        jtot = {}
        for (j, e), c in grid.items():
            jtot[j] = jtot.get(j, 0) + c
        if a in PELL:
            assert jtot.get(2, 0) == 0, (a, "split p=5 mod 8 exists on a Pell row")
        ncells = 0
        worst = 0.0
        worst_cell = None
        for j in range(2, JMAX + 1):
            n = jtot.get(j, 0)
            if n == 0:
                continue
            for e in range(0, j):
                q = predicted(j, e)
                if q == 0.0 or n * q < 100:
                    continue
                ncells += 1
                obs = grid.get((j, e), 0)
                sigma = (n * q * (1 - q)) ** 0.5
                zdev = abs(obs - n * q) / sigma
                if zdev > worst:
                    worst, worst_cell = zdev, (j, e, obs, n)
                assert zdev < 5.0, (a, j, e, obs, n, q, zdev)  # kill-shape
                if zdev > 3.0:
                    kill = True
                    print("  WARN a=%d cell (j=%d,e=%d): obs %d of %d, pred %.4f, %.1f sigma"
                          % (a, j, e, obs, n, q, zdev))
        j2note = " (j2 empty)" if a in PELL else ""
        je, ee, obs, n = worst_cell
        print("  a=%2d D=%4d split1mod4=%d cells=%d worst |z|=%.1f sigma at (j=%d,e=%d)%s"
              % (a, a * a + 4, n_split1, ncells, worst, je, ee, j2note))
    print("\nverdict: %s" % ("SOME CELL PAST 3 SIGMA (see WARN)" if kill else "every cell within 3 sigma"))


if __name__ == "__main__":
    sys.exit(main())
