"""triangle.py -- the digits of an Eisenstein polynomial's coefficients
and the digits of the unit p/pi^e: a unitriangular map, level by level,
at every prime, and the designer that runs it backwards.

QUESTION. Let K/Q_p be totally ramified of degree e, cut out by an
Eisenstein polynomial
    F = x^e + sum_{i=1}^{e-1} p b_i x^i - p d,     d a unit,
with root pi, and let u = p/pi^e, a unit of O_K = Z_p[pi]. Write u in
canonical digits, u = sum_r u_r pi^r with u_r in {0, ..., p - 1}, and
the coefficients in base p, b_i = sum_k b_(i,k) p^k and
d = sum_k delta_k p^k. Give b_(i,k) the LEVEL i + k e and delta_k
the level k e. Every level r >= 1 then carries exactly one coefficient
digit, the one at (i, k) = (r mod e, r div e), with delta_k at i = 0.
How does the digit string of u depend on the coefficient digits?

THE ARGUMENT (written before the engine).
  (1) THE FIXED POINT. F(pi) = 0 reads pi^e = p D with
      D = d - sum b_i pi^i, so u = 1/D. In O_K, p = u pi^e, so
      p^k = u^k pi^(k e), and D is a sum of one monomial per coefficient
      digit, each sitting at its own level times a power of u:
          D = delta_0 + sum_{k>=1} delta_k u^k pi^(k e)
                      - sum_{i,k} b_(i,k) u^k pi^(i + k e).
  (2) THE DIAGONAL. Raise the level-r digit c by one, all other digits
      fixed. D moves by Delta = -u^k pi^r (c a b-digit) or +u^k pi^r
      (c = delta_k, k >= 1), and
          1/(D + Delta) = u - u^2 Delta + u^3 Delta^2 - ...,
      whose terms past the second sit at level >= 2r > r. So u moves by
      a multiple of pi^r whose level-r residue is
          s = +ubar^(k+2)   (b-digit),     s = -ubar^(k+2)   (delta),
      with ubar = 1/dbar, a unit of F_p. Digits of u below r do not move
      (the change is divisible by pi^r), and the level-r digit moves by
      s mod p: a carry out of level r lands at r + e, since p pi^r =
      u pi^(r+e). Hence u_r = s_r c_r + g_r(c_1, ..., c_(r-1)) mod p,
      with g_r a function of the lower levels' digits and of delta_0.
      Nothing uses the value of p or the parity of e.
  (3) THE TRIANGLE. For each r the map (delta_0; c_1, ..., c_r) ->
      (u_0; u_1, ..., u_r) is a bijection F_p^x x F_p^r -> F_p^x x
      F_p^r, unitriangular up to the units s_r: u_0 = 1/delta_0 mod p,
      and level by level (2). Its inverse limit is a bijection from the
      Eisenstein polynomials over Z_p (every b_i in Z_p, d a unit) onto
      the digit strings with u_0 != 0: the digit string of u is a
      complete invariant of the polynomial, and a prescribed prefix
      u_0..u_r is printed by exactly one choice of the coefficient
      digits at levels 0..r, whatever the digits above r: the prefix's
      CELL.
  (4) THE DESIGNER is (3) run backwards: read u at the current design,
      and at level r = 1, 2, ... set c_r to the one value that moves u_r
      onto the target, which (2) says fixes every u_j, j < r. The
      REDUCED design (every digit above r zero) is the unique design
      whose coefficients are integers below p^(r div e + 1) with
      nothing past level r.
  (5) THE SHARP CASES. x^e - p has d = 1 and u = 1: the string
      1, 0, 0, ... at every p and e. ubar = -1 iff d = -1 mod p, the
      third clause of clock.py's head criterion (clock.py); at p = 2 it
      always holds.

TRANSPLANTS. The rows at p = 2 below are hand rows of the record this
script replaces, where the unit was -p/pi^e at odd p; at p = 2 the two
units are one, so the rows carry unchanged. The anchor prediction A is
a transplant from that record's reading of Phi_(2e)(x + 1) at e = 4 to
32.

PREDICTIONS, fixed before the engine ran.
  C  CONTROL. (a) The engine's u satisfies u pi^e = p to the working
     precision, and the digits re-summed give u back to the level read,
     at 42 random polynomials. (b) x^e - p prints
     1, 0, 0, ... to the level read at (p, e) = (2, 2), (2, 8), (2, 16),
     (3, 6), (5, 4), (7, 3). (c) The hand rows at p = 2: e = 2 gives
     u_1 = b_(1,0), u_2 = delta_1 + b_(1,0); e = 4 gives
     u_1 = b_(1,0), u_2 = b_(2,0) + b_(1,0), u_3 = b_(3,0)
     + b_(1,0), at every one of their cells.
  B  THE BIJECTION, exhaustive. Over the cells (delta_0; the coefficient
     digits at levels 1..r) with r = e at (2, 2), (2, 4) and r = 2e at
     (2, 4), (3, 3), (5, 2), and r = e at (3, 6), (5, 4): distinct cells
     print distinct strings u_0..u_r (so the count of strings is the
     count of cells: 4, 16, 256, 2 * 729, 4 * 625, 2 * 729, 4 * 625),
     and each cell prints the same string at two random lifts of its
     higher digits.
  D  THE DIAGONAL, exact. At (2, 2), (2, 4), (2, 6), (2, 8), (2, 12),
     (2, 16), (3, 6), (3, 12), (3, 18), (5, 4), (5, 20), (7, 6), over
     sampled polynomials at EVERY residue dbar and every level
     r <= 3e + 4: raising the level-r digit by a step of 1..p - 1
     leaves u_0..u_(r-1) fixed and moves u_r by that step times s of
     (2), mod p.
  I  THE DESIGNER. Random target strings u_0..u_r at (2, 16) with
     r = 80, (3, 18) with r = 54, (5, 20) with r = 40, (7, 6) with
     r = 30: the designer's reduced design prints the target (its
     coefficients have no digit above level r by construction).
  A  THE ANCHOR. At e = 4, 8, 16, 32 the reduced design printing the
     first 3e/2 - 1 digits of u at Phi_(2e)(x + 1) (the field Q_2 of
     the primitive 2e-th roots of unity, root zeta - 1) is
     x^e + 2x^(e/2) + 4x^(e/4) - 6.
  Z  THE CELL OF ZETA_9. At (p, e) = (3, 6), the cell of Phi_9(x + 1)'s
     digits of u through level e (one cell by (3)) cuts out Q_3(zeta_9)
     at every lift: its reduced design and 20 random lifts of its
     higher digits each hold a root of Phi_9, found digit by digit and
     certified by Hensel's lemma (v(Phi_9(z)) > 2 v(Phi_9'(z))), and so
     does x^6 - 3x^4 + 3. At 2 the matching statement fails: the
     three-term design at e = 4 is not Q_2(zeta_8) (wild.py reads its
     letters), so the prefix through 3e/2 - 1 prints the digits and not
     the field there. The mechanism is Krasner's lemma, and the kill is
     a lift with no certified root, read as the prediction's failure,
     not a proof of absence. Control: x^6 + 3 and x^6 - 3, whose
     fields hold pi^2, a cube root of -3 or 3, which no abelian
     extension of Q_3 holds (Q_3 lacks zeta_3), print no certified
     root.
KILLS, as printed observables: any C line off (nothing below is read);
a B count below the cell count, or a lift that moves the string; a D
(polynomial, level, step) off; an I target not printed; an A design other
than the three-term polynomial at any of the four e; a Z field with no
certified root.

FINDINGS. Every prediction landed: 32/32 checks PASS, no kill fired.
  C  u pi^e = p and the digits re-sum to u past the level read at 42
     polynomials, 0 off; x^e - p prints 1, 0, 0, ... at all six (p, e);
     the hand rows hold at 20 cells, 0 off.
  B  4, 16, 256, 1458, 2500, 1458 and 2500 cells print as many distinct
     strings at (2, 2), (2, 4) to levels 4 and 8, (3, 3), (5, 2), (3, 6)
     and (5, 4); 0 of 16,384 lifts moved a string.
  D  4024 (polynomial, level, step) changes over the twelve (p, e),
     every residue dbar, levels to 3e + 4 (64 at (5, 20)): 0 off, each
     moving u_r by exactly the step times s and no lower digit.
  I  14 random targets, to level 80 at (2, 16), 54 at (3, 18), 40 at
     (5, 20) and 30 at (7, 6), each printed by its reduced design,
     which has no coefficient digit above its level by construction.
  A  At e = 4, 8, 16, 32 the reduced design is x^e + 2x^(e/2) +
     4x^(e/4) - 6, its u's nonzero digits below 3e/2 at exactly
     r = 0, e/2 and 5e/4.
  Z  The cell's reduced design is x^6 + 6x^5 + 6x^4 + 3x^3 - 24, and
     it, 20 random lifts of its digits above level 6 and x^6 - 3x^4 + 3
     each hold a root of Phi_9 with Hensel margin v(Phi_9(z)) = 19 >
     2 x 9 (Phi_9(x + 1) itself, whose root 1 + pi is exact, to the
     precision cap 66): 23 fields, 0 off. The controls x^6 + 3 and
     x^6 - 3 print no root.
  Tiers: (1)-(4) a theorem at every p and e; A a rule, verified at
  e = 4, 8, 16 and 32; Z a rule over the 23 fields named.

RUN RECORD. 32/32, 4.3 s wall, peak working set 13.0 MB under
a memory guard (Z added in a later pass, green on its first run). Two engine bugs came before green, both caught by C: Newton's
iteration for 1/D stopped at its p-adic precision where it doubles
pi-adic precision, short by a factor e (Ca 8 off, and the D and I lines
failing with it); and the reader multiplied by ubar^(-k) where
p^k pi^i = u^k pi^r gives ubar^k, invisible at p = 2 and 3, where
ubar^2 = 1 (Ca off at p = 5 and 7).
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import random
from math import comb

from module_law import Local, check, section, CHECKS

SEED = 1424


class Field:
    """O_K = Z_p[pi]/(F) carried mod p^N, F = x^e + sum p b_i x^i - p d;
    reads the canonical digits of u = p/pi^e to level L."""

    def __init__(self, p, e, b, d, L):
        self.p, self.e, self.b, self.d, self.L = p, e, list(b), d, L
        self.N = L // e + 3
        self.mod = p ** self.N
        g = [-p * d] + [p * b[i] for i in range(1, e)] + [1]
        self.loc = Local(p, g, "eis", "F")
        self.u = self.inverse(self.D())

    def D(self):
        z = [self.d] + [-self.b[i] for i in range(1, self.e)]
        return [c % self.mod for c in z]

    def mul(self, x, y):
        return self.loc.mul(x, y, self.mod)

    def inverse(self, z):
        """Newton's iteration y <- y (2 - z y) from the residue's inverse."""
        y = [pow(z[0], -1, self.p)] + [0] * (self.e - 1)
        prec = 1
        while prec < self.e * self.N:
            corr = [(-c) % self.mod for c in self.mul(z, y)]
            corr[0] = (corr[0] + 2) % self.mod
            y = self.mul(y, corr)
            prec *= 2
        return y

    def pi_pow(self, r):
        return self.loc.pi_pow(r, self.mod)

    def digits(self):
        """Canonical digits u_0..u_L. At level r = i + k e the pi^r
        coefficient of a z with no digit below r is (c_i / p^k) ubar^k
        mod p, since p^k pi^i = u^k pi^r."""
        p, e = self.p, self.e
        z = list(self.u)
        ubar = self.u[0] % p
        out = []
        for r in range(self.L + 1):
            i, k = r % e, r // e
            dig = (z[i] // p ** k) * pow(ubar, k, p) % p
            out.append(dig)
            if dig:
                z = [(a - dig * x) % self.mod
                     for a, x in zip(z, self.pi_pow(r))]
        return out

    def val(self, z):
        return self.loc.val(z, self.N)


# ------------------------------------------------------------ coefficient digits

def cell_to_poly(p, e, d0, digs):
    """digs[r - 1] is the level-r digit; returns (b, d) as integers."""
    b = [0] * e
    d = d0
    for r, c in enumerate(digs, start=1):
        i, k = r % e, r // e
        if i == 0:
            d += c * p ** k
        else:
            b[i] += c * p ** k
    return b, d


def poly_to_cell(p, e, b, d, N):
    digs = []
    for r in range(1, N + 1):
        i, k = r % e, r // e
        x = d if i == 0 else b[i]
        digs.append((x // p ** k) % p)
    return d % p, digs


def read(p, e, b, d, L):
    return Field(p, e, b, d, L).digits()


def random_poly(rng, p, e, K, d0=None):
    """Coefficients with K base-p digits each; d a unit of residue d0."""
    b = [0] + [rng.randrange(p ** K) for _ in range(1, e)]
    d0 = rng.randrange(1, p) if d0 is None else d0
    return b, d0 + p * rng.randrange(p ** (K - 1))


def shift(p, e, r, t, ubar):
    """The move s of argument (2) when the level-r digit rises by t."""
    s = t * pow(ubar, r // e + 2, p)
    return -s if r % e == 0 else s


# ------------------------------------------------------------ sections

def section_control(rng):
    section("C  CONTROL: the reader, x^e - p, the hand rows")
    seen = bad = 0
    for (p, e) in [(2, 2), (2, 4), (2, 8), (2, 16), (3, 6), (5, 4), (7, 3)]:
        for _ in range(6):
            b, d = random_poly(rng, p, e, 5)
            L = 3 * e + 4
            f = Field(p, e, b, d, L)
            pe = f.mul(f.u, f.pi_pow(e))
            want = [p % f.mod] + [0] * (e - 1)
            resum = [0] * e
            for r, c in enumerate(f.digits()):
                if c:
                    resum = [(a + c * x) % f.mod
                             for a, x in zip(resum, f.pi_pow(r))]
            diff = [(a - x) % f.mod for a, x in zip(f.u, resum)]
            seen += 1
            bad += pe != want or f.val(diff) <= L
    check("Ca u pi^e = p, and the digits re-sum to u past the level read",
          bad == 0, f"{seen} polynomials, {bad} off")
    bad = 0
    rows = []
    for (p, e) in [(2, 2), (2, 8), (2, 16), (3, 6), (5, 4), (7, 3)]:
        rows.append(f"({p},{e})")
        bad += read(p, e, [0] * e, 1, 3 * e + 4) != [1] + [0] * (3 * e + 4)
    check("Cb x^e - p prints 1, 0, 0, ...", bad == 0, " ".join(rows))
    bad = n = 0
    for m in range(4):
        digs = [m & 1, m >> 1]
        u = read(2, 2, *cell_to_poly(2, 2, 1, digs), 2)
        n += 1
        bad += u[1:] != [digs[0], (digs[1] + digs[0]) % 2]
    for m in range(16):
        digs = [(m >> j) & 1 for j in range(4)]
        u = read(2, 4, *cell_to_poly(2, 4, 1, digs), 3)
        n += 1
        bad += u[1:4] != [digs[0], (digs[1] + digs[0]) % 2,
                          (digs[2] + digs[0]) % 2]
    check("Cc the hand rows at e = 2 and e = 4", bad == 0,
          f"{n} cells, {bad} off")


def section_bijection(rng):
    section("B  THE BIJECTION, exhaustive over cells")
    for (p, e, N) in [(2, 2, 2), (2, 4, 4), (2, 4, 8), (3, 3, 6),
                      (5, 2, 4), (3, 6, 6), (5, 4, 4)]:
        strings = set()
        cells = lifts = moved = 0
        K = N // e + 1
        for d0 in range(1, p):
            for m in range(p ** N):
                digs = [(m // p ** j) % p for j in range(N)]
                b, d = cell_to_poly(p, e, d0, digs)
                u = tuple(read(p, e, b, d, N))
                cells += 1
                strings.add(u)
                for _ in range(2):
                    b2 = [0] + [x + p ** K * rng.randrange(1, p ** 3)
                                for x in b[1:]]
                    d2 = d + p ** K * rng.randrange(1, p ** 3)
                    lifts += 1
                    moved += tuple(read(p, e, b2, d2, N)) != u
        check(f"B (p, e) = ({p}, {e}), levels 1..{N}: distinct strings",
              len(strings) == cells and moved == 0,
              f"{cells} cells, {len(strings)} strings, "
              f"{moved} of {lifts} lifts moved")


def section_diagonal(rng):
    section("D  THE DIAGONAL: a level-r digit moves u_r by s, nothing below")
    total = 0
    for (p, e, reps) in [(2, 2, 12), (2, 4, 12), (2, 6, 8), (2, 8, 6),
                         (2, 12, 3), (2, 16, 2), (3, 6, 3), (3, 12, 2),
                         (3, 18, 1), (5, 4, 2), (5, 20, 1), (7, 6, 1)]:
        R = 3 * e + 4
        seen = bad = 0
        for j in range(reps * (p - 1)):
            b, d = random_poly(rng, p, e, R // e + 2, 1 + j % (p - 1))
            base = read(p, e, b, d, R)
            for r in range(1, R + 1):
                i, k = r % e, r // e
                for t in range(1, p):
                    b2, d2 = list(b), d
                    if i == 0:
                        d2 += t * p ** k
                    else:
                        b2[i] += t * p ** k
                    new = read(p, e, b2, d2, r)
                    seen += 1
                    bad += (new[:r] != base[:r] or
                            (new[r] - base[r]
                             - shift(p, e, r, t, base[0])) % p != 0)
        total += seen
        check(f"D (p, e) = ({p}, {e}), levels 1..{R}, every dbar",
              bad == 0, f"{seen} changes, {bad} off")
    print(f"  {total} (polynomial, level, t) changes in all")


def design(p, e, target):
    """The reduced design printing target[0..N], set level by level."""
    N = len(target) - 1
    d0 = pow(target[0], -1, p)
    digs = [0] * N
    for r in range(1, N + 1):
        u = read(p, e, *cell_to_poly(p, e, d0, digs), r)
        s = shift(p, e, r, 1, target[0])
        digs[r - 1] = (target[r] - u[r]) * pow(s, -1, p) % p
    return cell_to_poly(p, e, d0, digs)


def section_designer(rng):
    section("I  THE DESIGNER: random targets printed by their reduced design")
    for (p, e, N, reps) in [(2, 16, 80, 4), (3, 18, 54, 3),
                            (5, 20, 40, 3), (7, 6, 30, 4)]:
        bad = 0
        for _ in range(reps):
            target = ([rng.randrange(1, p)]
                      + [rng.randrange(p) for _ in range(N)])
            b, d = design(p, e, target)
            bad += read(p, e, b, d, N) != target
        check(f"I (p, e) = ({p}, {e}), N = {N}", bad == 0,
              f"{reps} targets, {bad} off")


def cyclotomic(e):
    """Phi_(2e)(x + 1) = (x + 1)^e + 1 at e a power of 2, as (b, d)."""
    coef = [comb(e, i) for i in range(e + 1)]
    coef[0] += 1
    return [0] + [coef[i] // 2 for i in range(1, e)], -coef[0] // 2


def section_anchor():
    section("A  THE ANCHOR: the reduced design of zeta_(2e)'s first digits")
    for e in (4, 8, 16, 32):
        N = 3 * e // 2 - 1
        target = read(2, e, *cyclotomic(e), N)
        bb, dd = design(2, e, target)
        want = [0] * e
        want[e // 2] += 1
        want[e // 4] += 2
        terms = " + ".join(f"{2 * c}x^{i}" for i, c in
                           reversed(list(enumerate(bb))) if c)
        check(f"A e = {e}: x^{e} + {terms} - {2 * dd}",
              bb == want and dd == 3,
              "u_r = 1 at r = "
              + str([r for r in range(1, N + 1) if target[r]]))


def phi_eval(f, z, p):
    """Phi_(p^2)(z) = sum_(j<p) z^(j p) and its derivative, in f."""
    one = [1] + [0] * (f.e - 1)
    zp = one
    for _ in range(p):
        zp = f.mul(zp, z)
    inv_z = f.inverse(z)
    val, der, pw = [0] * f.e, [0] * f.e, one
    for j in range(p):
        val = [(a + x) % f.mod for a, x in zip(val, pw)]
        if j:
            t = f.mul(pw, [j * p % f.mod] + [0] * (f.e - 1))
            der = [(a + x) % f.mod for a, x in zip(der, f.mul(t, inv_z))]
        pw = f.mul(pw, zp)
    return val, der


def cyclotomic_root(f, p, depth, beam=12):
    """A root of Phi_(p^2) in f, found digit by digit on z = 1 + ...
    and returned with its Hensel margin, or None."""
    cands = [[1] + [0] * (f.e - 1)]
    for r in range(1, depth):
        scored = []
        for z in cands:
            for a in range(p):
                z2 = [(c + a * x) % f.mod for c, x in zip(z, f.pi_pow(r))]
                v, dv = phi_eval(f, z2, p)
                scored.append((f.val(v), f.val(dv), z2))
        scored.sort(key=lambda t: -t[0])
        for vv, dd, _ in scored:
            if vv > 2 * dd:
                return vv, dd
        cands = [z for _, _, z in scored[:beam]]
    return None


def section_cell(rng):
    section("Z  THE CELL OF ZETA_9: Krasner at 3, not at 2")
    p, e = 3, 6
    phi = [1, 0, 0, 1, 0, 0, 1]
    g = [sum(comb(k, i) * c for k, c in enumerate(phi)) for i in range(7)]
    b0, d0 = [0] + [g[i] // p for i in range(1, e)], -g[0] // p
    target = read(p, e, b0, d0, e)
    bb, dd = design(p, e, target)
    fields = [("Phi_9(x + 1)", b0, d0), ("reduced design", bb, dd),
              ("x^6 - 3x^4 + 3", [0, 0, 0, 0, -1, 0], -1)]
    for k in range(20):
        _, digs = poly_to_cell(p, e, bb, dd, e)
        digs += [rng.randrange(p) for _ in range(2 * e)]
        fields.append((f"lift {k}", *cell_to_poly(p, e, dd % p, digs)))
    bad = 0
    for name, b, d in fields:
        f = Field(p, e, b, d, 8 * e)
        u = read(p, e, b, d, e)
        ok = (u == target) != name.startswith("x^6")
        got = cyclotomic_root(f, p, 4 * e)
        ok &= got is not None
        bad += not ok
        if not name.startswith("lift") or not ok:
            print(f"  {name}: design b={b[1:]} d={d}; u to level "
                  f"{e} {u}; root "
                  f"{'none' if got is None else 'v(Phi) %d > 2 x %d' % got}")
    ctrl = 0
    for name, d in (("x^6 + 3", -1), ("x^6 - 3", 1)):
        got = cyclotomic_root(Field(p, e, [0] * e, d, 8 * e), p, 4 * e)
        ctrl += got is not None
        print(f"  control {name} (non-abelian): root "
              f"{'none' if got is None else 'v(Phi) %d > 2 x %d' % got}")
    check("Zc no certified root in the two non-abelian controls",
          ctrl == 0, f"{ctrl} of 2 certified")
    check("Z every field of the cell, and x^6 - 3x^4 + 3 outside it, "
          "holds a certified root of Phi_9",
          bad == 0, f"{len(fields)} fields, 20 of them lifts, {bad} off")


def main():
    rng = random.Random(SEED)
    section_control(rng)
    if not all(CHECKS):
        print("\ncontrol failed: nothing below is read")
        raise SystemExit(1)
    section_bijection(rng)
    section_diagonal(rng)
    section_designer(rng)
    section_anchor()
    section_cell(rng)
    print()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks PASS")
    if not all(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
