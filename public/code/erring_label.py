"""
erring_label.py -- a monotone size label that addition keeps up to an
error: the least error at each reach.

QUESTION. mu nondecreasing from [0, N) onto s labels, the cuts
0 = c_0 < c_1 < ... < c_{s-1} < c_s = N, label a the interval
I_a = [c_a, c_{a+1}). A(a, b) is a plurality value of mu(x + y) over the
ordered pairs (x, y) in I_a x I_b with x + y < N; the ERROR is the number
of such pairs where mu(x + y) differs from A, the REACH the number of
pairs x < y with mu(x) < mu(y). Which cuts trace the front, the least
error at reach at least r, and in what closed form?

THE ARGUMENT (written before this script; T(n) = n(n + 1)/2).
  (D1) Zero error is the additive labelling law's hypothesis, so mu is
       exact on [0, x0) and d-periodic after; monotone forces d = 1 and
       mu(x) = x below x0, so saturation min(x, s - 1) is the only
       zero-error labelling at 1 < s < N.
  (D2) Every pair touching the top interval sums into it, so only the
       cells inside [0, c)^2 err, c = c_{s-1}; once 2c - 1 <= N none of
       their pairs is truncated and the error does not move with N.
  (D3) s = 2: E = C(c, 2), R = c(N - c) for c <= (N + 1)/2. For c > N/2,
       d = N - c, the one erring cell sends d(2c - 1 - d)/2 pairs into
       [c, N), fewer than its T(c) below c, so E = d(2c - 1 - d)/2, which
       exceeds C(d, 2) by d(c - d) > 0: c is beaten by d at equal reach.
       On c = 1..floor(N/2) reach and error both rise strictly, so these
       c are the front.
  (D4) s = 3, alpha = c_1, beta = c - alpha >= alpha, 2c - 1 <= N:
       E = 3 C(alpha, 2) + min(T(c - 2 alpha), beta^2 - T(c - 2 alpha));
       the min is always its first term, T(beta - alpha) <= T(beta - 1)
       < beta^2/2; continuum optimum alpha = 2c/7, E ~ (3/14) c^2. For
       beta < alpha the cells err C(alpha, 2), T(beta), T(beta) and 0,
       so E = C(alpha, 2) + 2 T(beta); its swap alpha' = beta errs at most
       3 C(beta, 2) + T(alpha - beta), and twice the difference is
       2[alpha(beta - 1) - beta^2 + 3 beta] >= 2(3 beta - 1) > 0. So the
       least error at s = 3 is D4's minimum over alpha <= c/2.
  (D5) At reach r much less than N^2 the front is E ~ kappa_s (r/N)^2,
       kappa_s the limsup over c of e_{s-1}(c)/c^2, e_m(c) the least
       error of m intervals filling [0, c) with sums >= c in the overflow
       label.
  (D6) Plurality is the least-error table by the error's definition, so
       no other table moves the optimum down; a table constrained to
       A(a, b) >= max(a, b) could move it up.
  NEIGHBOURS. Ratio-2 cuts with the plurality table are the floating-
  point exponent of a sum; the RNS core function and approximate-CRT
  sign detection are size estimates read off the residues, not kept
  from labels alone; rounding to multiples of w is the high digit of
  mixed radix rounded, its error the dropped carry.

PREDICTIONS AND KILLS (written before the run).
  K1 zero-error cut sets are saturation alone, s = 2..6, N = s+1..24.
  K2 the s = 2 front is c <= ceil(N/2), E = C(c, 2), N = 3..60. The
     first run compared the front against every c <= ceil(N/2) and
     printed 29 faults, one per odd N: there c = (N + 1)/2 ties
     c = (N - 1)/2 in reach with more error, so it is off the front.
     The prediction held; the check now asks for c = 1..floor(N/2).
     D3's c > N/2 count is checked at every such c, N = 3..60.
  K3 the error of a cut set with 2c - 1 <= N is the same at N + 7,
     s = 3, 4, N = 8..30.
  K4 e_2(c) equals D4's minimum over alpha, c = 2..120; D4's beta < alpha
     count and its swap at every alpha > c/2, c = 3..80.
  K5 e_m(c)/c^2 printed: e_2 within 0.01 of 3/14 at c = 120; e_3 below.
  K6 cuts in ratio 2 (t, 2t, 4t, ...) against the front at their reach,
     s = 3, 4. Written as "dies if they are equal", no scale named; the
     engine reads t >= 2 (t = 1 is saturation) and fails only if no
     scale sits above.
  K7 (written after K1..K6) a lean that kappa_m, the limsup over c of
     e_m(c)/c^2 at fixed m, tends with m to a limit above 0.12: dies if
     a local search prints below 0.12 at any m <= 10, c = 300. (At fixed
     c the limit over m is 0: m = c singletons is saturation.)
  K8 (written after K7's prints) rounding of width w with a top interval
     [4c/5, c) tends to 1/10: dies if w = 10, c = 2000 prints outside
     [0.0990, 0.105].

FINDINGS (from the printed run; the controls passed first).
  K1 held: saturation is the only zero-error cut set at all 100 cells
     (s, N), s = 2..6, N = s+1..24; D1 proves it at every 1 < s < N.
  K2 held: the s = 2 front is c = 1..floor(N/2), E = C(c, 2), N = 3..60;
     D3's count held at all 870 cut sets with c > N/2.
  K3 held: 4740 cut sets with 2c - 1 <= N err the same at N + 7.
  K4 held: e_2(c) equals D4's minimum at every c = 2..120, and all 1560
     cut sets with beta < alpha, c = 3..80, err C(alpha, 2) + 2 T(beta)
     and more than their swap.
  K5 held: e_m(c)/c^2 at the largest c run, 0.4958 (m = 1, c = 120),
     0.2125 (m = 2, c = 120; 3/14 = 0.2143), 0.1738 (m = 3, c = 120),
     0.1572 (m = 4, c = 60), each rising in c, so each sits a little
     under its limit. Witnesses (0, 35, 120), (0, 22, 69, 120),
     (0, 8, 25, 41, 60): the inner cut ratio is 120/35 = 3.4 at m = 2,
     toward 7/2, and the upper intervals at m = 4 (17, 16, 19) are
     near equal, not geometric.
  K6 held as the engine reads it, mixed as written: ratio-2 cuts sit on
     the front at s = 3, N = 60 at t = 1, 2, 3 and 20 (saturation, the
     two smallest scales, and the uniform cuts) and strictly above it at
     every other scale run; at s = 4, N = 40 on it at t = 1 only, above
     at every t >= 2; 33 of the 36 scales t >= 2 above, the gap up to
     4.8x (s = 3, t = 29: 516 against 108; at s = 4 up to 2.9x, t = 9:
     232 against 81). The floating-point exponent is not the
     least-error label past its smallest scales.
  K7 (search, upper bounds; the search recovers e_3(120) = 2503 and
     e_4(60) = 566 first): e_m(300)/300^2 for m = 2..10 prints 0.2136,
     0.1747, 0.1592, 0.1510, 0.1477, 0.1354, 0.1309, 0.1224, 0.1218,
     its bar 0.12 uncrossed (now a print, since the lean dies by K8 and
     a better search would cross it). Its witnesses are a rounding
     quantizer: m = 9 cuts at 14, 43, 71, 100, 128, 157, 185, 216, near
     (k + 1/2) 28.5, then one wide top interval [216, 300).
  K8 the construction it suggests: round(x / w) on [0, 4c/5), the top
     interval [4c/5, c), c = 2000, prints 0.1301, 0.1149, 0.1077, 0.1028
     at w = 100, 50, 25, 10 (m = 18, 34, 66, 162), toward the continuum
     u^2/8 + (1 - u)^2/2 at u = 4/5, which is 1/10: rounding errs on 1/4
     of the pairs it sees, the carry of a rounded high digit, and the
     top interval's cells err where the sum crosses c. At fixed m the
     construction's e/c^2 holds still in c (w = c/20, m = 18: 0.1299,
     0.1302 at c = 1000, 4000; m = 34: 0.1149, 0.1150; m = 66: 0.1075,
     0.1074), so it bounds each kappa_m, and the bound falls toward 1/10
     as m grows. So the limsup of kappa_m over m is at most 1/10, and
     the lean (a limit above 0.12) is dead. Open: whether any fine
     partition errs locally on less than rounding's 1/4, which with the
     top interval's trade would make 1/10 the limit of kappa_m.
  D6 read: at every front point printed (s = 3, 4, N = 24) the
     plurality table, ties to the larger label, never shrinks a size
     (no "table shrinks" line), so the constraint does not move the
     front there.
  The front, read at N = 24: at s = 3 its cuts run (1, 2) saturation,
  (2, 7), (3, 10), (4, 13) at ratio near 7/2, to (8, 16) uniform; at
  s = 4 from (1, 2, 3) to (6, 12, 18). The uniform cuts close it: at
  s = 3, N = 60 and s = 4, N = 40 they reach the most and err the
  front's least there (570, 270).

OPEN, with its handle. Whether any fine partition errs locally below
rounding's 1/4. A block of width b (one cell's sums, near-uniform in
position) over cuts spaced W >= b, its position uniform mod W, errs on
the fraction (b/W)(1/4): equal widths (b = 2w, W = w, triangular) give
1/4 at phase 1/2, and a narrow summand over w_Y = w_Z gives 1/4 averaged
over the shift. Beating it needs w(X + Y) much wider than w(X) + w(Y)
on most of the mass, while X << Y puts X + Y near Y. Turning this into
a bound summed over the cells, the overflow region excepted, would make
1/10 the limit of kappa_m, given that a fine region and one wide top
interval are the optimal shape, itself unproved.

CONTROLS. s = N has error 0 and reach C(N, 2); saturation has error 0
and reach (s - 1)(N - s + 1) + C(s - 1, 2); the closed-form cell counts
agree with a pair-by-pair count on every cut set at N = 12, s = 2..5.
"""

from itertools import combinations
from math import comb

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tail = f"  ({detail})" if detail else ""
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{tail}")


def g(t):
    return t * (t + 1) // 2 if t > 0 else 0


def below(n1, n2, t):
    """#{(i, j) : 0 <= i < n1, 0 <= j < n2, i + j < t}."""
    return g(t) - g(t - n1) - g(t - n2) + g(t - n1 - n2)


def cells(cuts, N):
    """For each ordered cell (a, b): its surviving pairs and the count
    landing in each label."""
    s = len(cuts) - 1
    out = {}
    for a in range(s):
        u1, n1 = cuts[a], cuts[a + 1] - cuts[a]
        for b in range(s):
            u2, n2 = cuts[b], cuts[b + 1] - cuts[b]
            base = u1 + u2
            tot = below(n1, n2, N - base)
            if tot == 0:
                continue
            land = [below(n1, n2, min(cuts[c + 1], N) - base)
                    - below(n1, n2, cuts[c] - base) for c in range(s)]
            out[(a, b)] = (tot, land)
    return out


def error(cuts, N):
    return sum(tot - max(land) for tot, land in cells(cuts, N).values())


def reach(cuts):
    L = [cuts[i + 1] - cuts[i] for i in range(len(cuts) - 1)]
    return (sum(L) ** 2 - sum(x * x for x in L)) // 2


def error_brute(cuts, N):
    s = len(cuts) - 1
    mu = [a for a in range(s) for _ in range(cuts[a], cuts[a + 1])]
    cnt = {}
    for x in range(N):
        for y in range(N - x):
            cnt.setdefault((mu[x], mu[y]), [0] * s)[mu[x + y]] += 1
    return sum(sum(v) - max(v) for v in cnt.values())


def cutsets(N, s):
    for inner in combinations(range(1, N), s - 1):
        yield (0,) + inner + (N,)


def front(N, s):
    """Pareto points (R, E, cuts): no other cut set has reach >= R and
    error <= E with one strict; one witness each."""
    pts = sorted(((reach(c), error(c, N), c) for c in cutsets(N, s)),
                 key=lambda p: (-p[0], p[1]))
    out, best = [], None
    for R, E, c in pts:
        if best is None or E < best:
            out.append((R, E, c))
            best = E
    return out[::-1]


def least_at(fr, r):
    return min(E for R, E, _ in fr if R >= r)


def sat(N, s):
    return tuple(range(s)) + (N,)


def section_controls():
    print("controls")
    ok = all(error(tuple(range(N + 1)), N) == 0
             and reach(tuple(range(N + 1))) == comb(N, 2)
             for N in range(2, 30))
    check("control: s = N errs nowhere and reaches C(N, 2)", ok,
          "N = 2..29")
    ok = all(error(sat(N, s), N) == 0 and reach(sat(N, s))
             == (s - 1) * (N - s + 1) + comb(s - 1, 2)
             for N in range(3, 30) for s in range(2, N))
    check("control: saturation errs nowhere, reach by hand", ok,
          "N = 3..29, s = 2..N-1")
    bad = n = 0
    for s in range(2, 6):
        for c in cutsets(12, s):
            n += 1
            bad += error(c, 12) != error_brute(c, 12)
    check("control: closed-form cell counts match pair-by-pair counts",
          bad == 0, f"{n} cut sets at N = 12, {bad} faults")
    bad = sum(error(c, 9) != 0 for c in [(0, 4, 9), (0, 2, 5, 9)])
    check("control: the error sees a non-saturating cut set",
          bad == 2, "(0,4,9) and (0,2,5,9) at N = 9 both err")


def section_zero():
    print("K1  zero error")
    faults = n = 0
    for s in range(2, 7):
        for N in range(s + 1, 25):
            zero = [c for c in cutsets(N, s) if error(c, N) == 0]
            n += 1
            faults += zero != [sat(N, s)]
    check("zero-error cut sets: saturation only", faults == 0,
          f"{n} cells (s, N), {faults} faults")


def section_two():
    print("K2  s = 2")
    faults = 0
    for N in range(3, 61):
        fr = front(N, 2)
        want = [(c * (N - c), comb(c, 2)) for c in range(1, N // 2 + 1)]
        faults += [(R, E) for R, E, _ in fr] != want
        faults += any(c[1] > (N + 1) // 2 or E != comb(c[1], 2)
                      for R, E, c in fr)
    check("s = 2 front: c = 1..floor(N/2), E = C(c, 2)", faults == 0,
          f"N = 3..60, {faults} faults")
    faults = n = 0
    for N in range(3, 61):
        for c in range(N // 2 + 1, N):
            d = N - c
            n += 1
            faults += error((0, c, N), N) != d * (2 * c - 1 - d) // 2
    check("s = 2, c > N/2: E = d(2c - 1 - d)/2, d = N - c", faults == 0,
          f"{n} cut sets, N = 3..60, {faults} faults")


def section_nfree():
    print("K3  N-freeness")
    faults = n = 0
    for s in (3, 4):
        for N in range(8, 31):
            for c in cutsets(N, s):
                if 2 * c[-2] - 1 <= N:
                    n += 1
                    faults += error(c, N) != error(c[:-1] + (N + 7,), N + 7)
    check("N-freeness: error equal at N and N + 7", faults == 0,
          f"{n} cut sets, {faults} faults")


def inner(m, c):
    """e_m(c) and the cut sets attaining it: m intervals fill [0, c),
    the overflow label above, N = 2c - 1."""
    N = 2 * c - 1
    best, arg = None, []
    for mid in combinations(range(1, c), m - 1):
        cuts = (0,) + mid + (c, N)
        E = error(cuts, N)
        if best is None or E < best:
            best, arg = E, [cuts[:-1]]
        elif E == best:
            arg.append(cuts[:-1])
    return best, arg


def d4(c):
    T = g
    best = None
    for al in range(1, c):
        be = c - al
        if be < al:
            continue
        E = 3 * comb(al, 2) + min(T(c - 2 * al), be * be - T(c - 2 * al))
        best = E if best is None else min(best, E)
    return best


def section_three():
    print("K4  s = 3 inner closed form")
    faults = 0
    for c in range(2, 121):
        e, _ = inner(2, c)
        faults += e != d4(c)
    check("s = 3 inner closed form: e_2(c) = D4's min over alpha",
          faults == 0, f"c = 2..120, {faults} faults")
    faults = n = 0
    for c in range(3, 81):
        N = 2 * c - 1
        for al in range(c // 2 + 1, c):
            be = c - al
            n += 1
            E = error((0, al, c, N), N)
            faults += E != comb(al, 2) + 2 * g(be)
            faults += E <= error((0, be, c, N), N)
    check("s = 3, beta < alpha: E = C(alpha, 2) + 2 T(beta), above its swap",
          faults == 0, f"{n} cut sets, c = 3..80, {faults} faults")


def section_kappa():
    print("K5  e_m(c)/c^2")
    runs = {1: (30, 60, 120), 2: (30, 60, 120), 3: (30, 60, 120),
            4: (20, 40, 60)}
    last = {}
    for m, cs in runs.items():
        for c in cs:
            e, arg = inner(m, c)
            last[m] = e / c / c
            print(f"    m = {m}  c = {c:4d}  e = {e:6d}  e/c^2 = "
                  f"{e / c / c:.4f}  cuts {arg[0]}"
                  + (f" (+{len(arg) - 1} more)" if len(arg) > 1 else ""))
    print(f"    3/14 = {3 / 14:.4f}")
    check("e_2(120)/120^2 within 0.01 of 3/14; e_3(120) below e_2(120)",
          abs(last[2] - 3 / 14) < 0.01 and last[3] < last[2],
          f"e_2 {last[2]:.4f}, e_3 {last[3]:.4f}, e_4(60) {last[4]:.4f}")


def section_geo():
    print("K6  ratio-2 cuts against the front")
    above = n = 0
    for s, N in ((3, 60), (4, 40)):
        fr = front(N, s)
        t = 1
        while t * 2 ** (s - 2) < N:
            cuts = (0,) + tuple(t * 2 ** i for i in range(s - 1)) + (N,)
            R, E = reach(cuts), error(cuts, N)
            F = least_at(fr, R)
            print(f"    s = {s} N = {N} t = {t:2d}  cuts {cuts}  R = {R}"
                  f"  E = {E}  front E = {F}")
            if t >= 2:
                n += 1
                above += E > F
            t += 1
        U = [round(N * i / s) for i in range(s + 1)]
        R, E = reach(tuple(U)), error(tuple(U), N)
        print(f"    s = {s} N = {N} uniform {tuple(U)}  R = {R}  E = {E}"
              f"  front E = {least_at(fr, R)}  max R {fr[-1][0]}")
    check("ratio-2 cuts sit above the front at t >= 2", above > 0,
          f"{above} of {n} above")


def section_show():
    print("the front, read")
    for s, N in ((3, 24), (4, 24)):
        fr = front(N, s)
        print(f"    s = {s} N = {N}: {len(fr)} points")
        for R, E, c in fr:
            tbl = cells(c, N)
            mono = all(max(range(s), key=lambda k: (land[k], k))
                       >= max(a, b) for (a, b), (_, land) in tbl.items())
            print(f"      R = {R:4d}  E = {E:4d}  cuts {c[1:-1]}"
                  f"{'' if mono else '  table shrinks'}")


def descend(cuts, c, steps=(1, 2, 3, 5, 8, 13)):
    """Coordinate moves on the inner cuts of (0, ..., c) until none
    lowers the error; the overflow label above c, N = 2c - 1."""
    N = 2 * c - 1
    cur = list(cuts)
    best = error(tuple(cur) + (N,), N)
    moved = True
    while moved:
        moved = False
        for i in range(1, len(cur) - 1):
            for d in steps:
                for sgn in (-1, 1):
                    v = cur[i] + sgn * d
                    if cur[i - 1] < v < cur[i + 1]:
                        trial = cur[:i] + [v] + cur[i + 1:]
                        E = error(tuple(trial) + (N,), N)
                        if E < best:
                            cur, best, moved = trial, E, True
    return best, tuple(cur)


def search(m, c, seed=0):
    """Least error found for m intervals on [0, c): grown from the
    m - 1 optimum by a cut added in each gap, plus scaled restarts."""
    import random
    rng = random.Random(seed)
    if m == 1:
        return error((0, c, 2 * c - 1), 2 * c - 1), (0, c)
    prev = search(m - 1, c, seed)[1]
    starts = []
    for i in range(len(prev) - 1):
        if prev[i + 1] - prev[i] > 1:
            mid = (prev[i] + prev[i + 1]) // 2
            starts.append(tuple(sorted(prev[:i + 1] + (mid,) + prev[i + 1:])))
    for _ in range(4):
        starts.append((0,) + tuple(sorted(rng.sample(range(1, c), m - 1)))
                      + (c,))
    return min(descend(st, c) for st in starts)


def section_far():
    print("K7  the least error per c^2 as m grows (search, upper bounds)")
    e3, e4 = search(3, 120)[0], search(4, 60)[0]
    check("control: the search recovers the exhaustive e_3(120), e_4(60)",
          (e3, e4) == (2503, 566), f"{e3}, {e4}")
    if (e3, e4) != (2503, 566):
        return
    c, low = 300, 1.0
    for m in range(2, 11):
        e, cuts = search(m, c)
        low = min(low, e / c / c)
        print(f"    m = {m:2d}  c = {c}  e = {e:6d}  e/c^2 = {e / c / c:.4f}"
              f"  cuts {cuts}")
    print(f"    K7's bar 0.12 at c = 300, m <= 10: least {low:.4f} "
          f"(the lean dies by K8, not here)")


def rounding(c, w, u):
    """Cuts of round(x / w) on [0, u c), one top interval [u c, c)."""
    top = round(u * c)
    mid, k = [], 0
    while round((k + 0.5) * w) < top:
        mid.append(round((k + 0.5) * w))
        k += 1
    return (0,) + tuple(mid) + (top, c)


def section_round():
    print("K8  the rounding construction toward 1/10")
    one = rounding(120, 1000, 0.3)
    want = 3 * comb(36, 2) + g(120 - 72)
    check("control: one interval below the top is D4's case",
          one == (0, 36, 120) and error(one + (239,), 239) == want,
          f"cuts {one}, e = {error(one + (239,), 239)}, D4 {want}")
    cuts = rounding(30, 8, 0.8)
    E = error(cuts + (59,), 59)
    check("control: rounding cuts at (k + 1/2) w; their error matches "
          "the pair loop", cuts == (0, 4, 12, 20, 24, 30)
          and E == error_brute(cuts + (59,), 59), f"cuts {cuts}, e = {E}")
    c = 2000
    for w in (100, 50, 25, 10):
        cuts = rounding(c, w, 0.8)
        E = error(cuts + (2 * c - 1,), 2 * c - 1)
        print(f"    c = {c}  w = {w:3d}  m = {len(cuts) - 1:3d}  e/c^2 = "
              f"{E / c / c:.4f}")
    check("the construction tends to 1/10: w = 10 within [0.0990, 0.105]",
          0.0990 <= E / c / c <= 0.105, f"{E / c / c:.4f}")
    for k in (20, 40, 80):
        row, ms = [], set()
        for cc in (1000, 2000, 4000):
            cuts = rounding(cc, cc / k, 0.8)
            ms.add(len(cuts) - 1)
            row.append(error(cuts + (2 * cc - 1,), 2 * cc - 1) / cc / cc)
        print(f"    w = c/{k}, m in {sorted(ms)}: e/c^2 at c = 1000, 2000, "
              f"4000: " + ", ".join(f"{x:.4f}" for x in row))


def main():
    section_controls()
    if not all(CHECKS):
        print("\nCONTROL FAILED: nothing below is read.")
        raise SystemExit(1)
    section_zero()
    section_two()
    section_nfree()
    section_three()
    section_kappa()
    section_geo()
    section_show()
    section_far()
    section_round()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
