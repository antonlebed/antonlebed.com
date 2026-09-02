"""explore_function_field_lock.py — the function-field lock.

THE QUESTION (opened at explore_selection_frame.py's honest scope — the
selection frame's clock transfer — with machinery from that same
analysis). D-DYN at
T = 0 over F_2[x]: states are monic polynomials, lambda = the exponent of
(F_2[x]/N)^x, the greedy law takes the LEAST monic m (integer encoding
order — bit i = coeff of x^i — the canonical transfer of Z's "least
m >= 2") with lambda(N*m) > lambda(N). Over Z the cold greedy LOCKS onto
one prime forever (the lock-prime law, explore_lock_prime.py):
which irreducible column does it lock onto here?

Predictions: fixed and hand-attacked BEFORE this script ran (PR1-PR9).
FINDINGS below were written from
the first green run's output.

FINDINGS (run record at bottom; all sections assert).

1. THE DOOR MENU (rule, proved; brute-verified — engine door = full
   encoding-order scan at every checked state: 11 void states + 6 moves
   for every seed < 16). The minimal move is a PRIME POWER g^r (same
   proof as Q's door lemma: a composite's escaping prime-power part is
   smaller in encoding). Three classes, with d = deg g, e = v_g(N),
   c = v2(lambda):
     DEEPEN  (e >= 1):                r = 2^c + 1 - e, cost d*r
     FRESH   (e = 0, (2^d-1) does not divide lambda_odd): r = 1, cost d
     CLOCKED (e = 0, (2^d-1) | lambda_odd):  r = 2^c + 1, cost d*(2^c+1)
   NO GHOSTS: Q's ghost class ("q | lambda, (q-1) not | lambda") needs
   state and clock in the SAME monoid; here the state lives in F_2[x]
   and lambda in Z — "g | lambda" is untyped, and the trichotomy
   collapses to deepen/fresh/clocked. Type separation kills the ghosts.

2. DETERMINISM IS ARCHIMEDEAN (rule; existence proved by the void
   specimen, 295 tie states counted in the census — counting ONE
   representative per door class, so an undercount: every fresh degree
   class with >= 2 irreducibles is itself a within-class tie the count
   skips). Z's D-DYN needed no
   tie-break because prime powers of distinct primes are distinct
   INTEGERS — a size separation. The F_2[x] norm 2^deg collapses costs
   to degrees and ties are generic (the void's first move already:
   clocked x^2 vs fresh x^2+x+1, both degree 2). The tie-break axis Z
   never needed is REQUIRED here; the encoding order (degree-then-lex)
   is the canonical transfer of "least m".

3. THE SPRAWL — NO LOCK (rule, proved; verified 63 seeds x 60 moves).
   The cold greedy over F_2[x] locks onto NOTHING: openings recur
   forever, under ANY tie-break. Proof: every deepening or clocked
   opening raises c by exactly 1 (lands at ceil(log2) = c+1), and NO
   column escapes the escalator — a column's depth is capped at
   2^(c-1) + 1 (its own last landing) or its seed depth, so once
   2^(c-1) clears the seed depths EVERY deepening at clock c costs
   >= 2^(c-1), exponential in the deepening count — while a fresh
   door at cost <= floor(log2 lambda) + 2 always exists (at d =
   bit_length(lambda) + 1, 2^d - 1 > lambda cannot divide
   lambda_odd) and pure deepening only doubles
   lambda per step — the fresh alternative grows LINEARLY in the number
   of deepenings against the door's EXPONENTIAL doubling. Census
   accounting: #deepen + #clocked = c_final - c_seed <= 12 of 60 moves;
   fresh >= 48; mortality empty (a legal move always exists).

4. THE LOCK NEEDS MIXED CHARACTERISTIC (rule — the two lambda
   laws side by side). Q's lock ran on the own-prime pump: lambda(q^a)
   carries q^(a-1) (odd q; the 2-column's 2^(a-2) is the same linear
   shape), LINEAR in depth, so the recurrence invariant prices
   q's door at q forever. In F_2[x] the 1-units are Frobenius-flattened
   — lambda(g^a) carries 2^ceil(log2 a), LOGARITHMIC — so every column
   pumps the ONE shared dyadic clock and no invariant exists. Same
   proof for any F_q[x], char p: 1-unit exponent p^ceil(log_p a)
   (stated here, not run; since brute-run at q = 3, 9 and proved as
   the local module law — explore_module_law.py,
   which also settles general equal-characteristic Dedekind rings:
   move costs diverge, no crystal, at the cost-divergence level).
   Proved direction at this script's close: the lock NEEDS the
   linear pump — over F_q[x], every place is log-pumped and no lock
   exists. The converse was instantiated at Q only;
   explore_number_field_lock.py and explore_module_law.py added
   Z[sqrt(-5)] and Q(sqrt(-23)) censuses,
   with full generality open at exactly the cascade boundary
   (explore_module_law.py Theorem C).

5. THE VOID'S CLOSED FORM (rule in scope T = 60; frontier advance
   proved via Zsigmondy + the direct check at the exception degree 6).
   From N = 1: one clocked opening x^2 (the tie of finding 2, lex-
   resolved), then ONE fresh irreducible per frontier degree d = 2, 3,
   4, ... (always the least of its degree), with depth moves x^(2^j)
   firing exactly at power-of-2 frontiers after the dyadic warm-up x,
   x^2 — those two fire while the frontier is still at 2, the first
   strictly cheapest, not a tie — (x^r is the lex-least monic
   of its degree, so it wins every frontier tie; the run: depth costs
   1, 2, 4, 8, 16, 32 from e_x = 2, 3, 5, 9, 17, 33, frontier reaching
   54). Moves 1-11: 4, 2, 4, 7, 11, 16, 19, 37, 67, 131, 256. x+1
   NEVER opens (its clocked door 2^c + 1 always costs more than the
   frontier's fresh door, and the cheaper depth ride on x fires
   first): the void's lex choice starves the twin place forever.
   DEPTH AND INFINITE SUPPORT CO-OCCUR (e_x -> inf at ~log density
   alongside infinite openings) — but that is NOT breadth, which
   requires every place seated, and finding 6's shadow is exactly what
   forbids it: the sprawl holds the lone depth fate from a support of
   density zero. The correction and its proof (a sibling's clocked
   door is dominated by the seated place's own deepening door, so the
   starvation holds under any tie-break) are
   explore_fate_image_ff.py, which reads this trajectory against the
   fate image and finds it at no corner.

6. THE SIBLING SHADOW (rule, proved; census: fresh degrees pairwise
   distinct in every trajectory). The first fresh opening at degree d
   puts 2^d - 1 into lambda_odd and blocks every same-degree sibling
   forever. explore_selection_frame.py's "same-degree columns share the
   clock" finding turned dynamical. Corollary: deg-1 columns are BORN
   clocked (2^1 - 1 = 1)
   — the seat places (residue field F_2) can never open fresh; they
   enter trajectories only as depth fuel.

7. THE SEAT-LAW ANSWER (synthesis). Does the
   2-adic seat law reach the greedy dynamics? YES, INVERTED — with the
   mechanism split kept honest. What every F_2(x) place shares with
   Q's seat is the CURRENCY: a dyadic 1-unit clock (equal
   characteristic — residue characteristic 2 everywhere). What
   abolishes the lock is the RATE: Frobenius makes every tick
   logarithmic (finding 4), where Q's 2-column ticks its dyadic clock
   LINEARLY (2^(a-2)) — the thermal max at q = 2 came from menu
   poverty (an earlier run's seat-law finding), a different trait of the same seat.
   So the cold echo of the seat law is: the seat's clock currency is
   universal in F_2(x), its tick rate is wild everywhere, and a
   wild-ticking clock holds no lock. Census monopolists (the
   column carrying the tail's depth thread): x, x+1, x^2+x+1 — degree
   <= 2 as priced (deg-3+ depth at 3*2^(c-1) loses to the deg-1
   clocked door 2^c + 1).

Run: `python explore_function_field_lock.py`. RUN RECORD (113141
checks, ~1.2 s): s1 lambda law exact on 93 prime powers (deg g^a <= 8,
direct unit-group exponent); s2 void moves 1-11 as frozen (move 10 =
131 = x^7 + x + 1 = the least deg-7 irreducible, frozen symbolically),
frontier 2..54, depth costs 1, 2, 4, 8, 16, 32, x+1 absent; s4 the
void tie (2 candidates); s3 census 63 seeds x 60 moves: all sprawl,
295 tie states (class-representative count, finding 2's scope),
monopolists {2, 3, 7}. Predictions PR1-PR9
(fixed + hand-attacked pre-run): all hit; no misses.
"""

import sys

sys.setrecursionlimit(10000)

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


# ----------------------------------------------------- F_2[x] on int encodings
def pdeg(a):
    return a.bit_length() - 1


def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pdivmod(a, b):
    q = 0
    db = pdeg(b)
    while a and pdeg(a) >= db:
        s = pdeg(a) - db
        q ^= 1 << s
        a ^= b << s
    return q, a


def pmod(a, b):
    return pdivmod(a, b)[1]


def pmulmod(a, b, m):
    return pmod(pmul(a, b), m)


def ppow(a, n):
    r = 1
    while n:
        if n & 1:
            r = pmul(r, a)
        a = pmul(a, a)
        n >>= 1
    return r


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def prime_divisors(n):
    out = []
    d = 2
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
    """Rabin irreducibility test on the int encoding."""
    d = pdeg(f)
    if d < 1:
        return False
    if d == 1:
        return True
    if f & 1 == 0:
        return False  # divisible by x
    if bin(f).count("1") % 2 == 0:
        return False  # f(1) = 0
    x = 2
    t = x
    for _ in range(d):
        t = pmulmod(t, t, f)
    if t != x:
        return False
    for p in prime_divisors(d):
        t = x
        for _ in range(d // p):
            t = pmulmod(t, t, f)
        if pgcd(t ^ x, f) != 1:
            return False
    return True


_LEAST_IRR = {}


def least_irr(d):
    """Least (encoding order) irreducible of degree d."""
    if d not in _LEAST_IRR:
        f = 1 << d
        while not is_irr(f):
            f += 1
        _LEAST_IRR[d] = f
    return _LEAST_IRR[d]


_IRR_CLASS = {}


def irr_class(d):
    """All irreducibles of degree d (only called for small d)."""
    if d not in _IRR_CLASS:
        _IRR_CLASS[d] = [f for f in range(1 << d, 2 << d) if is_irr(f)]
    return _IRR_CLASS[d]


def factor_poly(m):
    """Full factorization by trial division (small m only)."""
    fac = {}
    d = 1
    while pdeg(m) >= 1:
        if is_irr(m):
            fac[m] = fac.get(m, 0) + 1
            break
        while d <= pdeg(m) // 2:
            hit = False
            for g in irr_class(d):
                if pmod(m, g) == 0:
                    fac[g] = fac.get(g, 0) + 1
                    m = pdivmod(m, g)[0]
                    hit = True
                    break
            if not hit:
                d += 1
            else:
                break
        else:
            if pdeg(m) >= 1:
                fac[m] = fac.get(m, 0) + 1
                break
    return fac


# ----------------------------------------------------------------- lambda law
def ceil_log2(a):
    return (a - 1).bit_length()  # a >= 1


def lam_pp(d, a):
    """lambda(g^a) for deg g = d (the char-2 1-unit law, re-bruted in s1)."""
    return ((1 << d) - 1) << ceil_log2(a)


def lcm(a, b):
    from math import gcd

    return a // gcd(a, b) * b


def lam_of_fac(fac):
    L = 1
    for g, e in fac.items():
        L = lcm(L, lam_pp(pdeg(g), e))
    return L


def v2(n):
    return (n & -n).bit_length() - 1


# ------------------------------------------------------------- the door menu
def door_menu(fac, lam):
    """All minimal-door candidates: list of (cost, m_enc, kind, g, r).

    kind in {'deepen', 'fresh', 'clocked'}. Returns (best, ties) where
    best is the chosen candidate (min cost, then min encoding) and ties
    is the number of distinct minimal-cost candidate encodings.
    """
    c = v2(lam)
    odd = lam >> c
    two_c1 = (1 << c) + 1
    cands = []
    bound = None
    # deepenings
    for g, e in fac.items():
        d = pdeg(g)
        ok(e <= (1 << c), "deepen precondition e <= 2^c")
        r = two_c1 - e
        cost = d * r
        cands.append((cost, None, "deepen", g, r))
        if bound is None or cost < bound:
            bound = cost
    # openings, degree ascending; fresh at d = lam.bit_length()+1 always legal
    dstar = lam.bit_length() + 1
    for d in range(1, dstar + 1):
        if bound is not None and d > bound:
            break
        md = (1 << d) - 1
        # d = 1: 2^1 - 1 = 1 divides everything -> always transparent
        transparent = d == 1 or odd % md == 0
        if not transparent:
            # FRESH: no deg-d column can exist (it would put md into odd)
            ok(all(pdeg(g) != d for g in fac), "fresh implies no deg-d column")
            cost = d
            cands.append((cost, least_irr(d), "fresh", None, 1))
            if bound is None or cost < bound:
                bound = cost
        else:
            cost = d * two_c1
            if bound is not None and cost > bound:
                continue
            # CLOCKED: least available irreducible of degree d
            avail = [g for g in irr_class(d) if g not in fac]
            if not avail:
                continue
            cands.append((cost, None, "clocked", None, two_c1, avail))
            if bound is None or cost < bound:
                bound = cost
    best_cost = min(x[0] for x in cands)
    # materialize encodings for min-cost candidates only
    finals = []
    for x in cands:
        if x[0] != best_cost:
            continue
        if x[2] == "deepen":
            finals.append((x[0], ppow(x[3], x[4]), "deepen", x[3], x[4]))
        elif x[2] == "fresh":
            finals.append((x[0], x[1], "fresh", x[1], 1))
        else:
            r = x[4]
            g = min(x[5], key=lambda gg: ppow(gg, r))
            finals.append((x[0], ppow(g, r), "clocked", g, r))
    encs = {f[1] for f in finals}
    best = min(finals, key=lambda f: f[1])
    return best, len(encs)


def apply_move(fac, g, r):
    fac = dict(fac)
    fac[g] = fac.get(g, 0) + r
    return fac


def brute_min_move(fac, lam, enc_limit=1 << 12):
    """Ground truth: scan ALL monic m in encoding order (small states only)."""
    for m in range(2, enc_limit):
        mf = factor_poly(m)
        merged = dict(fac)
        for g, e in mf.items():
            merged[g] = merged.get(g, 0) + e
        if lam_of_fac(merged) > lam:
            return m
    raise AssertionError("brute scan exhausted")


def run_traj(seed_fac, T, brute_moves=0):
    """Run T moves of cold D-DYN; return the move log."""
    fac = dict(seed_fac)
    lam = lam_of_fac(fac)
    log = []
    for t in range(T):
        best, nties = door_menu(fac, lam)
        cost, m_enc, kind, g, r = best
        if t < brute_moves:
            bm = brute_min_move(fac, lam)
            ok(bm == m_enc, "PR1 brute door = engine door (%d vs %d)" % (bm, m_enc))
        c_before = v2(lam)
        fac = apply_move(fac, g if kind != "fresh" else m_enc, r)
        lam2 = lam_of_fac(fac)
        ok(lam2 > lam, "chosen move grows lambda")
        if kind in ("deepen", "clocked"):
            ok(v2(lam2) == c_before + 1, "PR8 deepen/clocked raise c by exactly 1")
        else:
            ok(v2(lam2) == c_before, "fresh leaves c fixed")
        log.append((kind, m_enc, cost, g if kind != "fresh" else m_enc, r, nties))
        lam = lam2
    return log, fac, lam


# ============================================================== the sections
def s1_lambda_law():
    """PR9: the char-2 lambda law vs direct unit-group exponent, deg g^a <= 8."""
    from math import gcd as igcd

    n_checked = 0
    for d in range(1, 9):
        for g in irr_class(d):
            a = 1
            while d * a <= 8:
                f = ppow(g, a)
                df = pdeg(f)
                units = [u for u in range(1, 1 << df) if pgcd(u, f) == 1]
                if not units:
                    units = [1]
                L = 1
                for u in units:
                    t, k = u, 1
                    while t != 1:
                        t = pmulmod(t, u, f)
                        k += 1
                    L = L // igcd(L, k) * k
                ok(L == lam_pp(d, a), "PR9 lambda law at g=%d a=%d" % (g, a))
                n_checked += 1
                a += 1
    print("s1 PR9 lambda law: %d prime powers, law exact" % n_checked)


def s2_void():
    """PR3: the void trajectory, first 11 moves frozen; sweep structure."""
    T = 60
    log, fac, lam = run_traj({}, T, brute_moves=11)
    moves = [m for (_, m, _, _, _, _) in log]
    frozen = [4, 2, 4, 7, 11, 16, 19, 37, 67, None, 256]
    for i, want in enumerate(frozen):
        if want is None:
            ok(pdeg(moves[i]) == 7 and is_irr(moves[i]), "PR3 move 10 = deg-7 irr")
            ok(moves[i] == least_irr(7), "PR3 move 10 least deg-7 irr")
        else:
            ok(moves[i] == want, "PR3 move %d: %d != %d" % (i + 1, moves[i], want))
    ok(3 not in fac, "x+1 never opens (void, T=%d)" % T)
    kinds = [k for (k, _, _, _, _, _) in log]
    ok(kinds[0] == "clocked", "PR3 the void's first move is a CLOCKED opening")
    fresh_degs = [pdeg(m) for (k, m, _, _, _, _) in log if k == "fresh"]
    ok(fresh_degs == sorted(set(fresh_degs)), "void fresh degrees strictly ascend")
    ok(fresh_degs[0] == 2 and fresh_degs == list(
        range(2, 2 + len(fresh_degs))
    ), "void frontier sweeps consecutive degrees from 2")
    deep_g = {g for (k, _, _, g, _, _) in log if k == "deepen"}
    ok(deep_g == {2}, "void depth thread rides x only")
    deep_costs = [c for (k, _, c, _, _, _) in log if k == "deepen"]
    ok(all(b == 2 * a for a, b in zip(deep_costs[2:], deep_costs[3:])),
       "PR8 monopolist deepening costs double (post-warmup)")
    print("s2 PR3 void trajectory: moves 1-11 =", moves[:11])
    print("   frontier swept degrees 2..%d; depth thread on x at costs %s"
          % (max(fresh_degs), deep_costs))
    return log


def s3_census():
    """PR2/PR4/PR5/PR6/PR7: all monic seeds deg 1..5 + the void, T = 60."""
    T = 60
    total_ties = 0
    tie_states = 0
    monopolists = {}
    for seed in [1] + list(range(2, 64)):
        seed_fac = factor_poly(seed) if seed > 1 else {}
        log, fac, lam = run_traj(seed_fac, T, brute_moves=(6 if seed < 16 else 0))
        kinds = [k for (k, _, _, _, _, _) in log]
        nfresh = kinds.count("fresh")
        nother = T - nfresh
        ok(nfresh >= 48, "PR5 fresh >= 48 (seed %d: %d)" % (seed, nfresh))
        ok(nother <= 12, "PR5 deepen+clocked <= 12 (seed %d)" % seed)
        ok("fresh" in kinds[-10:], "PR5 an opening in the final 10 (seed %d)" % seed)
        fd = [pdeg(m) for (k, m, _, _, _, _) in log if k == "fresh"]
        ok(len(fd) == len(set(fd)), "PR4 sibling shadow: fresh degrees distinct (seed %d)" % seed)
        tail_deep = {g for (k, _, _, g, _, _) in log[30:] if k == "deepen"}
        ok(len(tail_deep) <= 1, "PR7 one monopolist in the tail (seed %d)" % seed)
        if tail_deep:
            g = tail_deep.pop()
            ok(pdeg(g) <= 2, "PR7 monopolist degree <= 2 (seed %d)" % seed)
            monopolists[seed] = g
        total_ties += sum(nt - 1 for (_, _, _, _, _, nt) in log if nt > 1)
        tie_states += sum(1 for (_, _, _, _, _, nt) in log if nt > 1)
    ok(tie_states > 0, "PR2 tie states exist")
    print("s3 census (63 seeds, T=%d): all sprawl; tie states %d (excess candidates %d)"
          % (T, tie_states, total_ties))
    print("   monopolists: %s" % sorted(set(monopolists.values())))
    return tie_states


def s4_void_tie():
    """PR2 specimen: the void's first move is a genuine degree tie."""
    best, nties = door_menu({}, 1)
    ok(nties >= 2, "PR2 the void's first move is tied (%d candidates)" % nties)
    ok(best[1] == 4, "lex resolves the void tie to x^2")
    print("s4 PR2 void tie: %d minimal-cost candidates, lex takes enc 4 = x^2" % nties)


def main():
    s1_lambda_law()
    s2_void()
    s4_void_tie()
    s3_census()
    print("ALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
