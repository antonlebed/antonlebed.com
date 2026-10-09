"""relative.py -- the jump set read off the cofactor of the root of unity,
coefficient by coefficient: Pagano's relative reading, and the points past it.

QUESTION. Let K/Q_p be totally ramified of degree e, cut out by an
Eisenstein F with root pi, holding a primitive p^N-th root of unity
zeta and no primitive p^(N+1)-th one, so the bend s = e/(p - 1) = c_0
p^M with p not dividing c_0, e* = p s, and zeta - 1 = pi^c tau with c =
s/p^(N-1) and tau a unit, the root's COFACTOR (cofactor.py). The jump
set of Pagano (Jump sets in local fields, arXiv:1810.09975) is the
invariant of the principal units as a filtered Z_p-module
(staircase.py reads it as the staircase of the class maxima). Does the
whole jump set read off tau?

THE RELATIVE DIGITS. E_N = Q_p(zeta) has uniformizer lam = zeta - 1 and
K/E_N is totally ramified of degree c, so pi has an Eisenstein
polynomial g(x) = x^c + sum_(iota<c) a_iota x^iota over E_N, and every x in O_K is uniquely
sum_(iota<c) alpha_iota pi^iota with alpha_iota in O_(E_N) = Z_p[lam].
From g(pi) = 0, pi^c = -sum a_iota pi^iota, and pi^c = lam/tau gives

    1/tau = -sum_(iota<c) (a_iota/lam) pi^iota.

So the Eisenstein coefficients over E_N are the relative digits of
1/tau: writing 1/tau greedily in the monomials lam^k pi^iota, each at
K-level c k + iota with a digit in {0, ..., p - 1}, the monomials of one
iota forming COEFFICIENT COLUMN iota, which first
receives a digit at k_iota = v(a_iota) - 1, and the COEFFICIENT-COLUMN LEVEL

    l_iota = v_K(a_iota pi^iota) = c (k_iota + 1) + iota,
             1 <= iota < c,   l_c = c,

is read off tau alone, with no polynomial over E_N ever written down.

THE OUTSIDE READ (full text, Section 10). Pagano's Theorem 10.1, for any
g in Eis(e_j, Q_q(zeta_(p^(j+1)))), e_j = e/(p^j (p - 1)), so j = N - 1
and e_j = c here, and with no separability hypothesis: give each
monomial the weight w(a_iota x^iota) = e_j v(a_iota) + iota, which is
l_iota, run his procedure over the monomials of weight at most e, and
it returns i_1 < ... < i_s equal to the points (i, beta) of the jump
set of Q_q(zeta)[x]/g with p^(beta(i) - N) i < e, with beta(i_k) =
v_p(alpha_k) + N and p^(v_p(alpha_k)) i_k = l_(alpha_k). His Theorem
1.11 is the case N = 1 under strong separability, where nothing lies
past e; his Section 10 shows (x^2 + 2x + 2 over Q_2) that past it the
reading fails. So the question reduces to the FAR POINTS, those with
p^(beta - N) i >= e.

THE DERIVATION (on paper, before the engine).
  (1) THE NEAR READING, the procedure as a staircase. A coefficient column iota
      with l_iota <= e gives the candidate (l_iota / p^(v_p(iota)),
      v_p(iota) + N) of weight rho^(v_p(iota) + N) of it; the procedure
      keeps the candidates that are minimal for the order (i, b) <= (i',
      b') iff b <= b' and the weight of (i, b) is at most that of (i',
      b'). The coefficient column iota = c (a_c = 1) is the first point (c_0, M +
      1), weight e*. A coefficient column with v_p(iota) > v_p(c) has beta > M + 1
      and weight above e*, so it is dominated by the first point; the
      procedure still drops it, his filter v_p(iota) <= v_p(c), since
      such a column can have v_p(l_iota) < v_p(iota) and give no
      integer candidate.
  (2) TWO CANDIDATES FOR A FAR COEFFICIENT COLUMN, frozen here. (A) the same formula
      carried past e. (B) the WEIGHT e + p^(N-1) l_iota, pulled back to
      its point: subtract e while above e*, stop at e* (point (e*, q)),
      otherwise divide by p while p divides. (B) is the rigid seat's
      weight: the cofactor readout makes the seat's departure p^(N-1)
      times the level of tau's principal part where it applies, and that
      level is min(l_iota) - c, so e* + dep = e + p^(N-1) min(l_iota).
      (A) and (B) agree when l_iota <= p c, which covers every l_iota <= e
      at N = 1; at N >= 2 they part at the first l_iota above p c.
  (3) PRECISION. A coefficient column absent below e* + M e has weight past e* + (M
      + 1) e under either reading, so beta >= M + 2, dominated by the
      first point: the read stops there. tau = lam pi^(e - c) / (p D),
      D = d - sum b_i pi^i (so pi^e = p D), accurate to level L + 1 - c
      when the root is (staircase.py's search at precision L + N e + 1).

THE ENGINE. The truth is staircase.py's: N off G, a root found by its
pruned search, and Pagano's Proposition 3.39 read verbatim off that
root. At every primitive p^N-th root zeta^a, tau is formed as above and
1/tau is expanded greedily in lam^k pi^iota, lam = zeta^a - 1, giving
l_iota.
A RELATIVE DESIGNER builds fields to order: a relative Eisenstein g
over Z[zeta_(p^N)], its coefficients a_iota = lam^(v_iota) times a small
unit, is carried to Q_p as its norm, the determinant of multiplication
by g on the basis 1, zeta, ..., zeta^(phi - 1), taken fraction-free
over Z[x]; the norm is pi's Eisenstein polynomial over Q_p, and the
field's N is read, never assumed.

TRANSPLANTS. (B)'s formula is the second point's weight, imported to
every coefficient column; nothing proves a later point obeys it. That the procedure
equals the staircase of (1) is read off his procedure's text and is
checked by T below, not assumed.

POPULATIONS. Controls: Q_2(zeta_8), Q_3(zeta_9), Q_2(zeta_16). The 59
fields of staircase.py, same seed. Designs over E_N at (p, N, c) =
(2, 1, 8), (2, 1, 12), (3, 1, 6), (3, 1, 9), (5, 1, 5), (2, 2, 4),
(2, 2, 6), (2, 2, 8), (2, 3, 2), (2, 3, 4), (3, 2, 2), (3, 2, 3), six
each, every a_iota zero with probability 1/3 and otherwise of valuation
1 to 4 (a_0 of valuation 1), so coefficient-column levels land on both sides of e.

PREDICTIONS, fixed before the run.
  C  CONTROL, run first. The three cyclotomic fields print the one point
     (1, N) as the truth and as the near reading (the coefficient column iota = c
     alone), with N = 3, 2, 4 read.
  D  THE DESIGNER. At every design the norm is Eisenstein of degree c
     phi(p^N), and the field read holds zeta_(p^N) (N read >= N built).
  T  THEOREM 10.1, the positive control, read before X. At every field
     and every primitive root, the near points of the truth (p^(beta -
     N) i < e) equal the minimal candidates of (1) among coefficient columns with
     l_iota < e whose own i satisfies it. (As frozen; i there is the
     candidate's first coordinate l_iota / p^(v_p(iota)).)
  I  INVARIANCE. The multiset of coefficient-column levels may move with the root;
     the readings below never do.
  X  THE FAR POINTS. At every field and every root, the minimal points
     of {near candidates from (1)} with {far candidates by (B)} are the
     whole jump set. (A) carried past e is printed beside it and
     predicted to fail wherever a far coefficient column has l_iota > p c.
KILLS, as printed observables: a C line off (nothing below is read); a
design whose norm is not Eisenstein; one (field, root) off T (the
engine, not the theorem, is then wrong); one (field, root) off X kills
(B) as the far reading, and the printed far rows are then the data for
the next derivation.

FINDINGS. C, D, T and I landed; X's kill fired, and the check now
prints that verdict.
  C  Q_2(zeta_8), Q_3(zeta_9) and Q_2(zeta_16) read N = 3, 2, 4 and the
     one point (1, N), as truth and as near reading, at every root.
  D  72 designs, every norm Eisenstein of degree c phi(p^N), and N read
     at least N built at every one. Fields by N read: 30, 76, 21, 3, 1
     at N = 1 to 5.
  T  THEOREM 10.1 HOLDS AS READ: at all 131 fields (59 of staircase.py
     and 72 designs) and all 504 (field, root) readings, the near points
     of the truth are the minimal near candidates. The procedure is the
     staircase of (1) with his coefficient column filter
     v_p(iota) <= v_p(c); without it the first run stopped on the
     integer-candidate assert before any check was read.
  I  No reading moved with the root.
  X  KILLED AS FROZEN. (B) is off at 73 of 131 fields and (A) carried
     past e at 56. The decisive rows are the BARE fields, whose 1/tau
     has no digit off coefficient column 0 below the bound, so that (1), (A) and
     (B) all read the first point alone: 15 of them hold far points,
     and those points depend only on (p, N, c): (5, 2) at (2, 2, 2);
     (5, 3), (13, 2) at (2, 2, 4); (15, 2) at (2, 2, 6); (5, 4), (13,
     3), (29, 2) at (2, 2, 8); (9, 3) at (2, 3, 2); (9, 4), (25, 3) at
     (2, 3, 4); (17, 4) at (2, 4, 2); (19, 2) at (3, 2, 3). So the far
     points are not read off tau's relative digits coefficient by coefficient
     alone;
     at a bare field they are the base's, carried by the constant
     coefficient column. Where coefficient columns do reach past e, the skeleton's points and
     the coefficient column candidates can collide and cancel: at e = 8, N = 2, c =
     4, coefficient column 2 at l = 10 and the bare point (5, 3) share a weight,
     and the field designed to lam = 11 holds neither.
  Tiers: T is Pagano's theorem (known), reproduced; the far points
  being missed by the coefficient columns alone is an observation with its
  witnesses above. The far points themselves are known: the reduction
  maps in the proof of the same paper's Theorem 9.1 (property (P.1))
  read every point with p^(beta - N) i < e* by reducing the unit
  normalized from g, carries of p-th powering included.

RUN RECORD. 7/7, 78.6 s wall, peak working set 14.1 MB under
a memory guard. The first full run stopped at the filter assert; the second
read X's kill; the later runs replace the X check with its fired
verdict and print the bare rows and the count by N, every other number
unchanged.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import random

from module_law import check, section, CHECKS, vp
from weld import Units, weight
from staircase import read_deep, root_search, pagano_reading, \
    population as staircase_population, cyclo, SEED as STAIRCASE_SEED

SEED = 1431
DESIGN_SPECS = [(2, 1, 8), (2, 1, 12), (3, 1, 6), (3, 1, 9), (5, 1, 5),
                (2, 2, 4), (2, 2, 6), (2, 2, 8), (2, 3, 2), (2, 3, 4),
                (3, 2, 2), (3, 2, 3)]
PER_SPEC = 6


# ------------------------------------------------------------ polynomials

def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                  for i in range(n)])


def psub(a, b):
    return padd(a, [-x for x in b])


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return ptrim(out)


def pdiv_exact(a, b):
    """a / b over Z[x], the division known to be exact."""
    a, b = ptrim(a), ptrim(b)
    if a == [0]:
        return [0]
    q = [0] * (len(a) - len(b) + 1)
    r = list(a)
    for k in range(len(q) - 1, -1, -1):
        top = r[k + len(b) - 1]
        assert top % b[-1] == 0, "inexact division"
        t = top // b[-1]
        q[k] = t
        if t:
            for j, y in enumerate(b):
                r[k + j] -= t * y
    assert all(x == 0 for x in r), "inexact division"
    return ptrim(q)


def det_zx(M):
    """Determinant over Z[x], Bareiss fraction-free."""
    M = [[ptrim(x) for x in row] for row in M]
    n, sign, prev = len(M), 1, [1]
    for k in range(n - 1):
        if M[k][k] == [0]:
            for r in range(k + 1, n):
                if M[r][k] != [0]:
                    M[k], M[r] = M[r], M[k]
                    sign = -sign
                    break
            else:
                return [0]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = pdiv_exact(psub(pmul(M[i][j], M[k][k]),
                                          pmul(M[i][k], M[k][j])), prev)
        prev = M[k][k]
    return [sign * x for x in M[n - 1][n - 1]]


# ------------------------------------------------------------ the designer

def cyclo_basis(p, N):
    """phi and zeta^t reduced mod Phi_(p^N), as coefficient vectors."""
    q = p ** (N - 1)
    phi = (p - 1) * q
    Phi = [0] * (phi + 1)
    for t in range(p):
        Phi[t * q] = 1
    pw, T = [], 2 * phi + 16
    for t in range(T):
        v = [0] * T
        v[t] = 1
        for top in range(len(v) - 1, phi - 1, -1):
            if v[top]:
                f = v[top]
                for j, cf in enumerate(Phi):
                    v[top - phi + j] -= f * cf
        pw.append(v[:phi])
    return phi, pw


def lam_poly(coeffs):
    """sum coeffs[k] lam^k, lam = zeta - 1, as a polynomial in zeta."""
    out = [0]
    lp = [1]
    for cf in coeffs:
        if cf:
            out = padd(out, [cf * x for x in lp])
        lp = pmul(lp, [-1, 1])
    return out


def norm_design(p, N, A):
    """(e, b, d) of the norm of x^c + sum_(i<c) A[i](zeta) x^i, each A[i]
    a list of coefficients in lam."""
    c = len(A)
    phi, pw = cyclo_basis(p, N)
    # g = sum_j G_j(x) zeta^j, G_j in Z[x]
    G = [[0] * (c + 1) for _ in range(phi)]
    G[0][c] = 1
    for i, a in enumerate(A):
        z = lam_poly(a)
        vec = [0] * phi
        for t, cf in enumerate(z):
            if cf:
                for j in range(phi):
                    vec[j] += cf * pw[t][j]
        for j in range(phi):
            G[j][i] += vec[j]
    # matrix column m: g zeta^m reduced
    Mx = [[[0] for _ in range(phi)] for _ in range(phi)]
    for m in range(phi):
        for j in range(phi):
            if any(G[j]):
                for r in range(phi):
                    cf = pw[j + m][r]
                    if cf:
                        Mx[r][m] = padd(Mx[r][m], [cf * x for x in G[j]])
    tot = det_zx(Mx)
    e = len(tot) - 1
    if tot[e] < 0:
        tot = [-x for x in tot]
    ok = (e == c * phi and tot[e] == 1
          and all(x % p == 0 for x in tot[:e]) and tot[0] % p ** 2 != 0)
    if not ok:
        return None
    b = [0] + [tot[i] // p for i in range(1, e)]
    return e, b, -tot[0] // p


def random_design(rng, p, N, c):
    """Coefficient lists in lam for a_0..a_(c-1): a_0 of valuation 1."""
    A = []
    for i in range(c):
        if i and rng.random() < 1 / 3:
            A.append([0])
            continue
        v = 1 if i == 0 else rng.randint(1, 4)
        unit = rng.choice([u for u in range(1, p * p) if u % p])
        a = [0] * v + [unit]
        if rng.random() < 0.5:
            a.append(rng.randrange(p))
        A.append(a)
    return A


# ------------------------------------------------------------ the reader

def level(z, e, p, mod, cap):
    best = cap
    for j, x in enumerate(z):
        x %= mod
        if x:
            best = min(best, e * vp(x, p) + j)
    return best


def column_levels(p, e, b, d, V, zeta, c, bound):
    """l_iota for 1 <= iota <= c off the relative digits of 1/tau, tau
    = (zeta - 1)/pi^c; None where coefficient column iota has no digit below
    bound."""
    mod = V.mod
    lam = [(zeta[0] - 1) % mod] + [x % mod for x in zeta[1:]]
    P = V.mul(lam, V.loc.pi_pow(e - c, mod))
    assert all(x % p == 0 for x in P), "lam pi^(e - c) not in p O"
    mod2 = mod // p
    Q = [(x // p) % mod2 for x in P]
    D = [d % mod] + [(-x) % mod for x in b[1:]]
    di = pow(d, -1, mod)
    Dinv = [(x * di) % mod for x in V.inv([(x * di) % mod for x in D])]
    tau = [x % mod2 for x in V.mul(Q, Dinv)]
    t0 = pow(tau[0] % p, -1, p)
    ti = [(x * t0) % mod for x in V.inv([(x * t0) % mod for x in tau])]
    y = [x % mod2 for x in ti]
    lampow = [V.one]
    kmax = bound // c + 1
    for _ in range(kmax):
        lampow.append(V.mul(lampow[-1], lam))
    first = {}
    while True:
        r = level(y, e, p, mod2, bound)
        if r >= bound:
            break
        k, i = divmod(r, c)
        mono = [x % mod2 for x in V.mul(lampow[k], V.loc.pi_pow(i, mod))]
        j = r % e
        lead_y = (y[j] // p ** (r // e)) % p
        lead_m = (mono[j] // p ** (r // e)) % p
        assert lead_m, "monomial off its level"
        dg = lead_y * pow(lead_m, -1, p) % p
        y = [(a - dg * m) % mod2 for a, m in zip(y, mono)]
        if i and i not in first:
            first[i] = k
    out = {i: c * (first[i] + 1) + i for i in first}
    out[c] = c
    return out


# ------------------------------------------------------------ the readings

def point_of_weight(p, e, W):
    """The point (i, beta) in T* with rho^beta(i) = W, W >= e*."""
    s = e // (p - 1)
    es = p * s
    if W == es:
        M = vp(s, p)
        return (s // p ** M, M + 1)
    bt = 0
    while W > es:
        W -= e
        bt += 1
    if W == es:
        return (es, bt)
    while W % p == 0:
        W //= p
        bt += 1
    return (W, bt)


def near_candidate(p, N, i, li):
    v = vp(i, p)
    a = li // p ** v
    assert a * p ** v == li
    return (a, v + N)


def minimal(p, e, pts):
    pts = set(pts)
    W = {q: weight(p, e, *q) for q in pts}
    return sorted(q for q in pts
                  if not any(r != q and r[1] <= q[1] and W[r] <= W[q]
                             for r in pts))


def is_near(p, e, N, q):
    return p ** (q[1] - N) * q[0] < e


def readings(p, e, N, cols):
    """The near reading, (B) and (A) carried past e."""
    near, far_B, far_A = [], [], []
    c = max(cols)
    for i, li in cols.items():
        if vp(i, p) > vp(c, p):
            continue
        cand = near_candidate(p, N, i, li)
        if li < e:
            near.append(cand)
        else:
            far_A.append(cand)
            far_B.append(point_of_weight(p, e, e + p ** (N - 1) * li))
    nearset = [q for q in minimal(p, e, near) if is_near(p, e, N, q)]
    return dict(near=nearset,
                B=minimal(p, e, near + far_B),
                A=minimal(p, e, near + far_A))


# ------------------------------------------------------------ one field

def read_field(p, e, b, d):
    rec = read_deep(p, e, b, d)
    N, L, M, s = rec["N"], rec["L"], rec["M"], rec["s"]
    Lp = L + N * e + 1
    root = root_search(p, e, b, d, N, Lp)
    if root is None:
        return dict(rec=rec, N=N, J=None)
    J = pagano_reading(p, e, rec, root)[0]
    V = Units(p, e, b, d, Lp)
    c = s // p ** (N - 1)
    bound = rec["es"] + M * e
    assert bound <= L + 1 - c, "coefficient column read past the root's precision"
    z = [x % V.mod for x in root]
    rows = []
    for a in range(1, p ** N):
        if a % p:
            cols = column_levels(p, e, b, d, V, V.pw(z, a), c, bound)
            rows.append((a, cols, readings(p, e, N, cols)))
    return dict(rec=rec, N=N, J=J, c=c, rows=rows)


def verdicts(p, e, f):
    N, J = f["N"], f["J"]
    nearJ = [q for q in J if is_near(p, e, N, q)]
    okT = all(r["near"] == nearJ for _, _, r in f["rows"])
    okX = all(r["B"] == J for _, _, r in f["rows"])
    okA = all(r["A"] == J for _, _, r in f["rows"])
    okI = len({(tuple(r["B"]), tuple(r["A"]), tuple(r["near"]))
               for _, _, r in f["rows"]}) == 1
    far = [q for q in J if not is_near(p, e, N, q)]
    return okT, okX, okA, okI, far


def show(p, e, label, f):
    c, N = f["c"], f["N"]
    a, cols, r = f["rows"][0]
    colstr = " ".join(f"{i}:{li}" for i, li in sorted(cols.items()))
    print(f"  p={p} e={e:2d} N={N} c={c} {label:34s} J {f['J']}")
    print(f"      coefficient columns {colstr}  (p c = {p * c})  B {r['B']}  "
          f"A {r['A']}")


# ------------------------------------------------------------ sections

def section_control():
    section("C  CONTROL: the cyclotomic fields read their one point")
    for name, p, N in [("Q_2(zeta_8)", 2, 3), ("Q_3(zeta_9)", 3, 2),
                       ("Q_2(zeta_16)", 2, 4)]:
        e, b, d = cyclo(p, N, 1, [])
        f = read_field(p, e, b, d)
        want = [(1, N)]
        ok = (f["N"] == N and f["J"] == want
              and all(r["near"] == want and r["B"] == want
                      for _, _, r in f["rows"]))
        check(f"C {name}: N = {N}, {want}", ok,
              f"N {f['N']}, J {f['J']}, near "
              f"{[r['near'] for _, _, r in f['rows']][:2]}")


def designs(rng):
    out, bad = [], 0
    for p, N, c in DESIGN_SPECS:
        for _ in range(PER_SPEC):
            A = random_design(rng, p, N, c)
            got = norm_design(p, N, A)
            if got is None:
                bad += 1
                continue
            e, b, d = got
            vals = [next(k for k, x in enumerate(a) if x) if any(a)
                    else None for a in A]
            out.append((f"E_{N} c={c} v={vals}", p, e, b, d, N))
    return out, bad


def section_fields(rng):
    section("D, T, I, X  THE DESIGNER, THEOREM 10.1, INVARIANCE, "
            "THE FAR POINTS")
    rows = [(lbl, p, e, b, d, Ng) for lbl, p, e, b, d, Ng in
            staircase_population(random.Random(STAIRCASE_SEED))]
    des, bad_eis = designs(rng)
    rows += des
    n = dict(fields=0, roots=0, far=0, farfields=0, three=0, bare=0)
    bad = dict(D=bad_eis, T=0, I=0, X=0, A=0)
    for label, p, e, b, d, Ng in rows:
        f = read_field(p, e, b, d)
        if f["J"] is None or f["N"] < Ng:
            bad["D"] += 1
            print(f"    OFF {label}: N read {f['N']}, built {Ng}")
            continue
        okT, okX, okA, okI, far = verdicts(p, e, f)
        n["fields"] += 1
        n.setdefault("byN", {})
        n["byN"][f["N"]] = n["byN"].get(f["N"], 0) + 1
        n["roots"] += len(f["rows"])
        n["far"] += len(far)
        n["farfields"] += bool(far)
        n["three"] += len(f["J"]) >= 3
        if far and all(set(cols) == {f["c"]} for _, cols, _ in f["rows"]):
            n["bare"] += 1
            print(f"    BARE {label}: no coefficient column below the bound, far "
                  f"points {far}")
        bad["T"] += not okT
        bad["X"] += not okX
        bad["A"] += not okA
        bad["I"] += not okI
        if far or not (okT and okX):
            show(p, e, label, f)
        if not okT:
            print(f"    OFF T: near {[r['near'] for _, _, r in f['rows']]}")
        if not okX:
            print(f"    OFF X at roots "
                  f"{[a for a, _, r in f['rows'] if r['B'] != f['J']]}")
    print(f"  {n['fields']} fields, {n['roots']} (field, root) readings, "
          f"{n['three']} with three or more points; {n['far']} far points "
          f"at {n['farfields']} fields; (A) carried past e off at "
          f"{bad['A']} fields; fields by N {dict(sorted(n['byN'].items()))}")
    check("D every design Eisenstein, N read >= N built", bad["D"] == 0,
          f"{len(des)} designs and {len(rows) - len(des)} staircase.py "
          f"fields, {bad['D']} off")
    check("T Theorem 10.1: the near points are the near reading",
          bad["T"] == 0, f"{n['fields']} fields, {bad['T']} off")
    check("I the readings do not move with the root", bad["I"] == 0,
          f"{bad['I']} off")
    check("X KILLED as frozen: the coefficient columns alone miss the far points",
          bad["X"] > 0 and bad["A"] > 0 and n["bare"] > 0,
          f"(B) off at {bad['X']} of {n['fields']} fields, (A) at "
          f"{bad['A']}; {n['bare']} fields read no coefficient column past the first "
          f"and still hold far points")


def main():
    rng = random.Random(SEED)
    section_control()
    if not all(CHECKS):
        print("\ncontrol failed: nothing below is read")
        raise SystemExit(1)
    section_fields(rng)
    print()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks PASS")
    if not all(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
