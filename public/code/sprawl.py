"""sprawl.py -- the dynamics demand over F_2[x]: why it never locks, why it
opens at most one place of each degree, and the walk from the void in
closed form.

QUESTION. Over Z the greedy dynamics walk locks onto one prime
(growth.py); at a place of mixed characteristic a tick of lambda costs
a constant p^(ef), and in equal characteristic the tick price is
unbounded (module_law.py). What does the walk do over F_2[x], and what
does its support look like?

THE OBJECT. States are nonzero polynomials N over F_2 (all monic),
encoded as integers with bit i the coefficient of x^i, so 2 = x,
3 = x + 1, 7 = x^2 + x + 1, and the integer order is degree first,
then lexicographic from the top: the ENCODING ORDER, the canonical
reading of "the least m". lambda(N) is the exponent of
(F_2[x]/N)^x; at an irreducible g of degree d, lambda(g^a) =
(2^d - 1) 2^(ceil log2 a) (growth.py, checked there against the unit
group), and lambda(N) is the lcm over the prime powers of N. The walk
takes m >= 2 least in the encoding order with lambda(Nm) > lambda(N).
Write c = v_2(lambda) and lambda_odd for the odd part.

THE ARGUMENT (written before the engine).
  (1) THE DOOR MENU. If m raises lambda, some prime power g^r of m
      raises it alone; g^r divides m, so it has degree <= deg m and is
      smaller in the encoding unless m = g^r. So every pick is a prime
      power, and at g (degree d, a = v_g(N)) the least raising power
      is: DEEPENING (a >= 1) r = 2^c + 1 - a, since the 2-part must
      pass 2^c and (2^d - 1) already divides lambda, and a <= 2^c
      because lambda carries 2^(ceil log2 a); OPENING AT EXPONENT 1 (a = 0,
      (2^d - 1) not dividing lambda_odd) r = 1; CLOCKED OPENING (a = 0,
      (2^d - 1) dividing lambda_odd) r = 2^c + 1. A deepening or a
      clocked opening raises c by exactly one and leaves lambda_odd; an opening at exponent 1 leaves c. There is no ghost: the ghost's condition
      over Z, q dividing lambda, compares a place with a number, and
      here the place lives in F_2[x] and lambda in Z.
  (2) THE SIBLING SHADOW. Once some place g of degree d is seated,
      (2^d - 1) divides lambda, so every other place h of degree d is
      clocked, its least move of degree d(2^c + 1), while g's own
      deepening has degree d(2^c + 1 - a) with a >= 1: strictly less. So no
      sibling of a seated place is ever picked, under any tie-break
      among moves of one degree: the walk opens at most one place of
      each degree, and none at a degree the seed already seats. Its
      support holds at most one of the roughly 2^d/d places of each
      degree d beyond the seed's, a set of density zero, so the fate
      called BREADTH (every place seated) never occurs.
  (3) THE SPRAWL. An opening at exponent 1 always exists: at the least d
      with (2^d - 1) not dividing lambda_odd, which is at most
      bit_length(lambda_odd) + 1. Suppose the openings stop. Then
      lambda_odd is fixed, so that opening's degree is fixed, while
      every move raises c by one. A column's depth is at most its seed
      depth or 2^(c' - 1) + 1, c' the clock at its last pick, so once
      2^(c - 1) passes every seed depth each deepening has degree >=
      2^(c - 1) and each clocked opening more: the other moves outgrow
      the opening at exponent 1, a contradiction. So openings at
      exponent 1 recur forever under any tie-break, no place is ever the
      whole tail, and a legal move always exists. Over F_q[x] the
      argument should transfer on E(a) = p^(ceil log_p a)
      (module_law.py); it is not run here.
  (4) THE VOID IN CLOSED FORM. From N = 1 the walk opens x at exponent 2
      (clocked, c = 0: the tie at degree 2 with x^2 + x + 1 goes to
      x^2), then deepens x with x and x^2, reaching x^5, c = 3. After
      that, by induction, x sits at 2^j + 1 with c = j + 1 and its least
      move has degree 2^j, and the FRONTIER d, the least degree with
      (2^d - 1) not dividing lambda_odd, has every degree 2..d-1 opened
      at exponent 1, one place each. The frontier advances by exactly
      one per opening at exponent 1: by Zsigmondy's theorem 2^n - 1 has
      a prime factor dividing no 2^k - 1 with k < n, for every n >= 2
      but 6, and at n = 6 the factor 9 of 63 divides none of 3, 7, 15,
      31. While x's least move has degree 2^j the frontier lies in
      [2^(j-1), 2^j], so the opening at exponent 1 is strictly cheaper
      until the frontier reaches 2^j. Every other move is dominated by
      x's least move: x + 1 is clocked at degree 2^c + 1 = 2^(j+1) + 1;
      a clocked place of degree d' >= 2 costs d'(2^c + 1); a place
      opened at exponent 1 deepens at degree d 2^c. So the walk is: x^2,
      x, x^2, then for d = 2, 3, 4, ... the least irreducible of degree
      d, preceded at every d = 2^j >= 4 by x^d, which wins that degree's
      tie as the least monic of its degree. x + 1 never enters: the
      sibling shadow at degree 1.

DESIGN. Standard library only; one process; the F_2[x] arithmetic and
lambda imported from growth.py. States are carried as factorizations,
never multiplied out, and irreducibility is Rabin's test.
  C  POSITIVE CONTROL, before any verdict: the menu of (1) against a
     scan of every m in the encoding order, lambda(Nm) computed by
     factoring N m, at every state met with deg N + deg(pick) <= 18,
     over the void's walk and the first moves from every seed.
  S  the census: the void and every monic of degree 1 to 5 (63 seeds),
     60 moves each, under two tie-breaks at the least degree, the least
     encoding and the greatest. Per trajectory: openings at exponent 1,
     the count of other moves against c_final - c_seed, and the sibling
     shadow (no opening at a degree already seated).
  V  the void, 60 moves, against the closed form of (4); the first
     11 picks; x's depth; the frontier; x + 1 absent.

PREDICTIONS, fixed before the run (the census figures are those of the
script this one replaces).
  C  the menu equals the scan at every state checked.
  S  every trajectory under both tie-breaks: other moves = c_final -
     c_seed <= 12, openings at exponent 1 >= 48 of 60, no opening at a
     seated degree.
  V  the walk equals the closed form at all 60 moves; the first 11
     picks are 4, 2, 4, 7, 11, 16, 19, 37, 67, 131, 256; x's depth
     ends at 65; the frontier reaches 54; x + 1 never picked.
A KILL is any printed disagreement in C, in the sibling-shadow or
other-move counts of S, or in V: each refutes a step of the argument.
The bound on openings at exponent 1 in S is an observation.

FINDINGS. Every prediction landed: 11/11 checks PASS.
  C  Rabin's test agrees with factoring at every polynomial of degree
     <= 10; the menu's pick is the least raising m of the encoding
     scan at 318 states, 0 off.
  S  63 seeds x 60 moves under the least-encoding tie-break: 3386
     openings at exponent 1, 379 deepenings, 15 clocked openings; under
     the greatest: 3400, 377 and 3. On both, every trajectory's count of
     other moves equals c_final - c_seed, no opening lands at a degree
     already seated, the fewest openings at exponent 1 is 53 of 60 and
     the most other moves 7.
  V  the void's 60 picks equal the closed form of (4); the first 11 are
     4, 2, 4, 7, 11, 16, 19, 37, 67, 131, 256; x ends at depth 65 (depth
     moves at degrees 4, 8, 16, 32); the openings at exponent 1 are one
     irreducible of each degree 2..54; x + 1 never enters.
  Tiers: the door menu, the sibling shadow, the sprawl and the void's
  closed form are theorems, each proved in the argument above and
  verified in the ranges printed.

RUN RECORD. 11/11, 0.8 s wall, 8.4 MB peak commit under a memory guard. The
first run printed 10/11: the positive control found the menu off at 6 of
315 states, because it fixed the least degree before adding the clocked
openings and so dropped a clocked opening cheaper than the door-1
opening (seeds 19, 25 and 31, lambda = 15: the scan picks x^2 at degree
2, the menu took the opening at exponent 1 of degree 3). The fix
recomputes the least degree after the clocked openings; the S and V
lines printed the same figures before and after, since a trajectory's
count of other moves is c_final - c_seed along either path and the void
never meets the case.
"""

from growth import (lcm, v2, pdeg, pmul, pdivmod, ppow, pfactor,
                    lam_f2_pp)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if detail else ""))


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# ------------------------------------------------------ F_2[x], any degree
def pmod(a, m):
    return pdivmod(a, m)[1]


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def is_irr(f):
    """Rabin's test: f of degree n is irreducible iff x^(2^n) = x mod f
    and gcd(x^(2^(n/l)) - x, f) = 1 for every prime l | n."""
    n = pdeg(f)
    if n == 1:
        return True
    pw = [2]
    for _ in range(n):
        pw.append(pmod(pmul(pw[-1], pw[-1]), f))
    if pw[n] != 2:
        return False
    return all(pgcd(pw[n // l] ^ 2, f) == 1 for l in prime_factors(n))


EXTREME = {}


def extreme_irr(d, greatest):
    """The least (or greatest) irreducible of degree d in the encoding."""
    if (d, greatest) not in EXTREME:
        f = (1 << (d + 1)) - 1 if greatest else 1 << d
        while not is_irr(f):
            f += -1 if greatest else 1
        EXTREME[(d, greatest)] = f
    return EXTREME[(d, greatest)]


ALL = {}


def irr_of_degree(d):
    if d not in ALL:
        ALL[d] = [f for f in range(1 << d, 1 << (d + 1)) if is_irr(f)]
    return ALL[d]


# ------------------------------------------------------------- the walk
def lam(st):
    L = 1
    for g, a in st.items():
        L = lcm(L, lam_f2_pp(pdeg(g), a))
    return L


def menu(st, greatest=False):
    """Every least move of (1) at the least degree; returns the pick."""
    L = lam(st)
    c = v2(L)
    odd = L >> c
    cands = []
    for g, a in st.items():
        assert a <= 1 << c, "a column deeper than the clock allows"
        cands.append((pdeg(g) * ((1 << c) + 1 - a), g, (1 << c) + 1 - a,
                      "deepen"))
    d0 = 1
    while odd % ((1 << d0) - 1) == 0:
        d0 += 1
    g0 = extreme_irr(d0, greatest)
    assert g0 not in st, "a seated place of the exponent-1 degree"
    cands.append((d0, g0, 1, "at 1"))
    best = min(t[0] for t in cands)
    d = 1
    while d * ((1 << c) + 1) <= best:
        if odd % ((1 << d) - 1) == 0:
            for g in irr_of_degree(d):
                if g not in st:
                    cands.append((d * ((1 << c) + 1), g, (1 << c) + 1,
                                  "clocked"))
        d += 1
    best = min(t[0] for t in cands)
    low = [t for t in cands if t[0] == best]
    pick = (max if greatest else min)(low, key=lambda t: ppow(t[1], t[2]))
    return pick


def walk(seed, T, greatest=False):
    st = dict(seed)
    log = []
    for _ in range(T):
        deg, g, r, kd = menu(st, greatest)
        seated = {pdeg(h) for h in st}
        log.append((g, r, deg, kd, v2(lam(st)), pdeg(g) in seated
                    and kd != "deepen"))
        st[g] = st.get(g, 0) + r
    return log, st


def state_poly(st):
    N = 1
    for g, a in st.items():
        N = pmul(N, ppow(g, a))
    return N


def lam_poly(f):
    L = 1
    for g, a in pfactor(f).items():
        L = lcm(L, lam_f2_pp(pdeg(g), a))
    return L


def brute_pick(N, stop):
    """The least m >= 2 in the encoding with lambda(Nm) > lambda(N)."""
    L = lam_poly(N)
    for m in range(2, stop + 1):
        if lam_poly(pmul(N, m)) != L:
            return m
    return None


# ------------------------------------------------------------- sections
SEEDS = [{}] + [pfactor(f) for f in range(2, 64)]


def section_control():
    section("C  POSITIVE CONTROL: the menu against the encoding scan")
    irr_ok = all(is_irr(f) == (len(pfactor(f)) == 1
                               and list(pfactor(f).values()) == [1])
                 for f in range(2, 1 << 11))
    check("C0 Rabin's test agrees with factoring at every polynomial of "
          "degree <= 10", irr_ok)
    tested = bad = 0
    for seed in SEEDS:
        st = dict(seed)
        for _ in range(12):
            deg, g, r, kd = menu(st)
            N = state_poly(st)
            if pdeg(N) + deg > 18 or deg > 9:
                break
            move = ppow(g, r)
            tested += 1
            bad += brute_pick(N, move) != move
            st[g] = st.get(g, 0) + r
    check("C1 the menu's pick = the least raising m in the encoding, "
          "deg N + deg m <= 18", bad == 0, f"{tested} states, {bad} off")


def section_s():
    section("S  THE SPRAWL and THE SIBLING SHADOW: 63 seeds x 60 moves")
    for greatest in (False, True):
        name = "greatest" if greatest else "least"
        fresh_min, nonfresh_bad, shadow_bad, nonfresh_max = 60, 0, 0, 0
        kinds = {}
        for seed in SEEDS:
            log, st = walk(seed, 60, greatest)
            c0, c1 = v2(lam(seed)), v2(lam(st))
            nf = sum(mv[3] != "at 1" for mv in log)
            nonfresh_bad += nf != c1 - c0
            nonfresh_max = max(nonfresh_max, nf)
            fresh_min = min(fresh_min, 60 - nf)
            shadow_bad += sum(mv[5] for mv in log)
            for mv in log:
                kinds[mv[3]] = kinds.get(mv[3], 0) + 1
        print(f"  tie-break {name}: kinds {kinds}; fewest openings at "
              f"exponent 1 {fresh_min}; most other moves {nonfresh_max}")
        check(f"S1 ({name}) other moves = c_final - c_seed on every "
              f"trajectory", nonfresh_bad == 0, f"{nonfresh_bad} off")
        check(f"S2 ({name}) no opening at a degree already seated (the "
              f"menu's openings at exponent 1 avoid them by construction; "
              f"the clocked ones are tested)",
              shadow_bad == 0, f"{shadow_bad} openings")
        check(f"S3 ({name}) at least 48 openings at exponent 1 of 60, at "
              f"most 12 other moves", fresh_min >= 48 and nonfresh_max <= 12)


def closed_form(T):
    out, d = [4, 2, 4], 2
    while len(out) < T:
        if d >= 4 and d & (d - 1) == 0:
            out.append(1 << d)
        out.append(extreme_irr(d, False))
        d += 1
    return out[:T]


def section_v():
    section("V  THE VOID: 60 moves against the closed form")
    log, st = walk({}, 60)
    picks = [ppow(g, r) for (g, r, deg, kd, c, sh) in log]
    print("  first 11 picks:", picks[:11])
    fresh_degs = [pdeg(g) for (g, r, deg, kd, c, sh) in log if kd == "at 1"]
    print(f"  x's depth {st.get(2)}; degrees opened at exponent 1 "
          f"{fresh_degs[0]}.."
          f"{fresh_degs[-1]}; x + 1 seated: {3 in st}")
    check("V1 the walk equals the closed form at all 60 moves",
          picks == closed_form(60))
    check("V1 the first 11 picks are 4, 2, 4, 7, 11, 16, 19, 37, 67, 131, "
          "256", picks[:11] == [4, 2, 4, 7, 11, 16, 19, 37, 67, 131, 256])
    check("V1 x ends at depth 65, the degrees opened at exponent 1 run "
          "2..54 one each, "
          "x + 1 never enters", st.get(2) == 65
          and fresh_degs == list(range(2, 55)) and 3 not in st)


def main():
    section_control()
    section_s()
    section_v()
    print()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
