"""The tie world: the desert one age deeper, and a designed tie
put to STRICT work.

THE QUESTION -- two residues left open around the tie desert. The
working-clause census (explore_working_amnesiac.py) measured plain
breadth as a tie desert: interior-normalizer products injective on
every multi-route dated fiber at beta = 1, ages <= 3. The rogue
world (explore_rogue_world.py) then settled the design side --
recycled-prime menu design manufactures all-beta ties freely (the
normalizer semiring is far from factorial), while the quarantine
theorem bars every COPRIME world (plain breadth included) from
all-beta ties at any age. Two questions survive that settlement:
  (a) THE FINE SIDE. The quarantine theorem leaves single-beta
      ties open, and the beta = 1 measurement stops at age 3. Does
      the desert persist at age 4?
  (b) THE STRICT SIDE. Every strict working amnesiac on record --
      coarse state LEAKS, a refinement cures -- rides symmetric
      (equal-multiset, Lemma C) ties in the depth world; the rogue
      fiber is flat already coarse, nothing to cure. Can a
      menu-DESIGNED, witness-free tie fund a strict cure: one
      dated fiber holding two tie classes at different products,
      so the coarse state leaks at every beta and the pairing
      refinement is spread + flat at every beta?

THE COARSE WORLD W_C (the design, hand-derived before the engine;
every move a power of 2, so every normalizer is a 0/1 polynomial
in the single variable x = 2^-beta). Menu table (states not listed
get (2,), which reaches no route below relevant to the probe
fiber):

    1: (2, 4, 8, 16)    2: (4, 8)      4: (4, 8)     8: (8,)
    16: (8, 16)         64: (2, 4)     128: (2,)

Every move is a power of 2, so with x = 2^-beta the normalizers are
    Z(2) = Z(4) = x^2 + x^3,  Z(8) = x^3,  Z(16) = x^3 + x^4,
    Z(64) = x + x^2,          Z(128) = x.
The probe fiber is the dated endpoint (256, age 3). Hand-enumerated
closure: exactly four routes reach it --
    P = (2, 8, 16)   interiors 1, 2, 16
    Q = (4, 4, 16)   interiors 1, 4, 16
    A = (8, 8, 4)    interiors 1, 8, 64
    B = (16, 8, 2)   interiors 1, 16, 128
(Z(1) is shared by the whole fiber and cancels from every
comparison.) The load-bearing algebra, provable by hand:

    A's product  Z(8) * Z(64)  = x^3 * (x + x^2)   = x^4 (1 + x)
    B's product  Z(16) * Z(128) = (x^3 + x^4) * x  = x^4 (1 + x)

-- identically equal as functions of beta, while the normalizer
MULTISETS {x^3, x + x^2} and {x^3 + x^4, x} DIFFER: a witness-free
tie, not covered by the weight-side symmetry lemma (Lemma C). As a
semiring collision it is a scaling-family instance from
explore_rogue_world.py's census -- Z_A * Z_{cB} = Z_{cA} * Z_B at
A = {2,4}, B = {2}, c = 4 -- here realized as a CLOSED fiber that
also holds a second, DIFFERENT-product tie class: P and Q tie by
EQUAL multisets (Z(2) = Z(4) as polynomials), the Lemma-C shape.
Whole-fiber products: pi_1 = x^5 (1 + x)^2 (P, Q) against
pi_2 = x^4 (1 + x) (A, B); the ratio x (1 + x) is never 1, so the
coarse state Phi = g leaks the route at every beta and the pairing
refinement {P, Q} | {A, B} is spread and flat at every beta -- the
strict working amnesiac, funded by a designed witness-free tie.

THE SLATE (predictions fixed before the engine ran):
  P1  control -- W_B dated to age 3 reproduces the parent: 363
      multi-route fibers, 0 fibers with any tied route pair at
      beta = 1.
  P2  the fine side [TRANSPLANT -- extends the parent's age-3 scan
      one age up on the fineness intuition, which the quarantine
      theorem makes exact only for all-beta ties]: W_B at age 4 is
      still a tie desert at beta = 1.
  P3  W_C's dated fiber (256, 3) holds EXACTLY the four routes
      P, Q, A, B above.
  P4  A and B tie: interior-normalizer products equal at every grid
      beta AND as exact polynomials, with DIFFERENT normalizer
      multisets.
  P5  P and Q tie with EQUAL multisets (the Lemma-C shape).
  P6  Phi = g leaks (whole-fiber posterior non-uniform at every
      grid beta) and the pairing refinement is spread + flat at
      every grid beta and symbolically -- the strict working
      amnesiac lands.
KILLS (observables, not inferences): the fiber print shows routes
other than the four (the hand-closure was wrong); any printed
product pair differs where a tie is predicted; the leak or the cure
fails on any grid beta.

DESIGN. The machinery is imported from explore_working_amnesiac.py
(histories, interiors, prod_inv_z, fibers_dated, BETAS) so the
control runs on the parent's own code path. Symbolic products are
exact integer-coefficient polynomial dicts {exponent: coeff} over
x = 2^-beta, computed by this rig independently and cross-checked
against the imported Fraction evaluation at every grid beta.

RUN RECORD (post-run edit; copied from the printed run). 11 checks,
0 failed, ~0.7 s. Every frozen prediction hit on the first run:
  P1  control: 363 multi-route W_B fibers at age <= 3, 0 tied at
      beta = 1 -- the parent reproduced on its own code path.
  P2  the desert PERSISTS at age 4: 441 age-4 multi-route fibers
      (largest 168 routes), 0 with any tied pair at beta = 1. The
      fine world stays fine one age deeper.
  P3  the (256, 3) fiber is exactly {P, Q, A, B}; printed products
      {5:1, 6:2, 7:1} twice (= x^5 (1+x)^2) and {4:1, 5:1} twice
      (= x^4 (1+x)).
  P4  A/B tie symbolically (all beta at once) and on the grid, with
      multisets [x+x^2, x^3] vs [x, x^3+x^4] -- DIFFERENT: the tie
      escapes Lemma C. Independent-path cross-check (this rig's
      polynomial arithmetic vs the parent's Fraction evaluation)
      clean on all four routes at all grid betas.
  P5  P/Q tie with EQUAL multisets (the Lemma-C contrast pair).
  P6  Phi = g leaks at every grid beta (pi_1 != pi_2; the ratio is
      x (1+x), never 1) and the pairing {P,Q} | {A,B} is spread +
      flat symbolically and on the grid: the strict working
      amnesiac lands at grade S in a multi-route order-carrying
      world.
VERDICT. Both residues settle. (a) The desert persists one age
past the parent's scope: plain breadth stays injective at beta = 1
through age 4, consistent with the quarantine theorem's fineness
reading (coprimality keeps the supply permanently fresh) though
the theorem itself bars only all-beta ties. (b) The strict working
amnesiac's tie supply is not confined to symmetry and tuning:
a designed witness-free tie (a realized scaling-family collision)
funds a leak-then-cure strict amnesiac at grade S -- one fiber,
two tie classes at different products, cured by pairing at every
temperature. The tie itself is proved (an algebraic identity), the
fiber censuses exact and exhaustive at the stated scope.
"""

from fractions import Fraction

from explore_working_amnesiac import (
    BETAS, fibers_dated, interiors, prod_inv_z, zeta, WORLDS,
)

CHECKS = []


def check(name, ok):
    CHECKS.append((name, ok))
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name))


# ------------------------------------------------------- the coarse world

MENU_C = {
    1: (2, 4, 8, 16),
    2: (4, 8),
    4: (4, 8),
    8: (8,),
    16: (8, 16),
    64: (2, 4),
    128: (2,),
}


def menu_coarse(state):
    return MENU_C.get(state, (2,))


def log2_exact(m):
    e = 0
    while m % 2 == 0:
        m //= 2
        e += 1
    assert m == 1, "coarse world move is not a power of 2"
    return e


def z_poly(state):
    """Normalizer as a 0/1 polynomial dict {exponent: coeff} in
    x = 2^-beta."""
    p = {}
    for m in menu_coarse(state):
        e = log2_exact(m)
        p[e] = p.get(e, 0) + 1
    return p


def poly_mul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            out[ea + eb] = out.get(ea + eb, 0) + ca * cb
    return out


def poly_eval(p, beta):
    return sum(c * Fraction(1, 2 ** (e * beta)) for e, c in p.items())


def product_poly(route):
    """Interior-normalizer product, start state excluded (shared by
    the whole fiber), as an exact polynomial."""
    p = {0: 1}
    for s in interiors(route)[1:]:
        p = poly_mul(p, z_poly(s))
    return p


def multiset(route):
    """Interior-normalizer multiset, start excluded, as sorted
    polynomial items."""
    return sorted(
        tuple(sorted(z_poly(s).items())) for s in interiors(route)[1:]
    )


def main():
    print("=" * 72)
    print("S1 control: W_B dated to age 3 (the parent's tie desert)")
    print("=" * 72)
    menu_b, max_age = WORLDS["W_B"]
    fib3 = fibers_dated(menu_b, max_age)
    multi3 = {k: v for k, v in fib3.items() if len(v) >= 2}
    tied3 = 0
    for key, routes in multi3.items():
        wv = [prod_inv_z(menu_b, r, 1) for r in routes]
        tied3 += (len(set(wv)) < len(wv))
    print("  multi-route fibers at age <= 3: %d; fibers with any tied "
          "pair at beta=1: %d" % (len(multi3), tied3))
    check("P1 parent reproduced (363 fibers, 0 tied)",
          len(multi3) == 363 and tied3 == 0)

    print("=" * 72)
    print("S2 the fine side one age deeper: W_B dated to age 4")
    print("=" * 72)
    fib4 = fibers_dated(menu_b, 4)
    multi4 = {k: v for k, v in fib4.items()
              if len(v) >= 2 and k[1] == 4}
    tied4 = 0
    biggest = 0
    for key, routes in multi4.items():
        biggest = max(biggest, len(routes))
        wv = [prod_inv_z(menu_b, r, 1) for r in routes]
        tied4 += (len(set(wv)) < len(wv))
    print("  age-4 multi-route fibers: %d (largest %d routes); fibers "
          "with any tied pair at beta=1: %d"
          % (len(multi4), biggest, tied4))
    check("P2 the desert persists at age 4 (0 tied)", tied4 == 0)

    print("=" * 72)
    print("S3 the coarse world W_C: the probe fiber (256, 3)")
    print("=" * 72)
    fibc = fibers_dated(menu_coarse, 3)
    fiber = sorted(fibc[(256, 3)])
    print("  routes in the (256, 3) fiber:")
    for r in fiber:
        print("    %-12s interiors %s  product %s"
              % (r, interiors(r), dict(sorted(product_poly(r).items()))))
    expected = sorted([(2, 8, 16), (4, 4, 16), (8, 8, 4), (16, 8, 2)])
    check("P3 fiber is exactly {P, Q, A, B}", fiber == expected)

    P, Q = (2, 8, 16), (4, 4, 16)
    A, B = (8, 8, 4), (16, 8, 2)

    print("=" * 72)
    print("S4 the factor-shuffle tie (A, B): equal products, "
          "different multisets")
    print("=" * 72)
    pa, pb = product_poly(A), product_poly(B)
    ma, mb = multiset(A), multiset(B)
    print("  A product %s  multiset %s" % (sorted(pa.items()), ma))
    print("  B product %s  multiset %s" % (sorted(pb.items()), mb))
    grid_tie = all(
        prod_inv_z(menu_coarse, A, b) == prod_inv_z(menu_coarse, B, b)
        for b in BETAS)
    cross = all(
        poly_eval(product_poly(r), b) * poly_eval(z_poly(1), b)
        == 1 / prod_inv_z(menu_coarse, r, b)
        for r in fiber for b in BETAS)
    check("P4a A/B products equal symbolically (all beta at once)",
          pa == pb)
    check("P4b A/B products equal on the beta grid (imported path)",
          grid_tie)
    check("P4c A/B normalizer multisets DIFFER (no Lemma-C witness)",
          ma != mb)
    check("independent-path cross-check (poly vs Fraction, all routes)",
          cross)

    print("=" * 72)
    print("S5 the contrast pair (P, Q): equal products by EQUAL "
          "multisets")
    print("=" * 72)
    pp, pq = product_poly(P), product_poly(Q)
    mp, mq = multiset(P), multiset(Q)
    check("P5a P/Q products equal symbolically", pp == pq)
    check("P5b P/Q multisets EQUAL (the Lemma-C shape)", mp == mq)

    print("=" * 72)
    print("S6 the strict working amnesiac: leak, then cure by pairing")
    print("=" * 72)
    leak = all(
        prod_inv_z(menu_coarse, P, b) != prod_inv_z(menu_coarse, A, b)
        for b in BETAS)
    check("P6a Phi = g leaks (pi_1 != pi_2 at every grid beta)",
          leak and pp != pa)
    blocks = [(P, Q), (A, B)]
    spread = all(len(set(blk)) >= 2 for blk in blocks)
    flat_sym = (pp == pq) and (pa == pb)
    flat_grid = all(
        prod_inv_z(menu_coarse, r1, b) == prod_inv_z(menu_coarse, r2, b)
        for (r1, r2) in blocks for b in BETAS)
    check("P6b pairing refinement spread + flat (grid and symbolic) "
          "-- grade S", spread and flat_sym and flat_grid)

    print("=" * 72)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("%d checks, %d failed" % (len(CHECKS), n_fail))


if __name__ == "__main__":
    main()
