"""The output comparator: is a comparator on a unit's OUTPUT exactly
free, the delay of max(G(x), z) equal to the delay of G?

THE QUESTION. A comparator inside a fused unit is exactly free: for
every map G of streams the on-line delay of G(w, max(y, z)) equals the
delay of G(w, y), the upper half because the fused image lies inside
G's image of a box of its own inputs, the lower half because the
adversary ties z's digits to y's and hands the reader G's own game
(explore_comparator_delay.py, theorems (3) and (4)). A comparator on
an output, max(G(x), z) with z a stream of the input window, has only
the upper half: its image lies inside G's image or inside z's cell,
and a cell strictly contains no overlap zone, so it costs at most G's
delay. Whether it costs exactly G's delay was left open: the diagonal
argument has no partner stream to tie, z being compared with a value
no input stream carries.

THE ROUTE (proved here on paper, the rig its check). The constant
stream of digit -a- spells the window's bottom exactly: its prefix of
length n is u_n = -a- (b^n - 1)/(b - 1), whose cell has lower end
-a- b^n over (b - 1) b^n = -M-. Where G's image over the root lies at
or above -M- -- at output offset o = 0 representability puts it inside
the root cell [-M-, M+] -- the point map z = -M- makes max(G(x), z) =
G(x) for every x. A reader of max(G(x), z) at lookahead c, fed the
constant z, is then a reader of G at lookahead c: the cell it commits
at depth t after reading depth t + c contains max(G(x'), z') for every
continuation of both prefixes, hence G(x') for every continuation of
x's. So if G has no reader at c, neither has the comparator, and

  THE OUTPUT COMPARATOR THEOREM. For every map G whose image over the
  window lies inside the window, the delay of max(G(x), z) equals the
  delay of G, and the delay of min(G(x), z) likewise (z = +M+, the
  constant stream of digit a+).

The same holds whenever the partner is read at the output's own scale
(at offset o the partner b^o z spans the output window), since the
constant bottom stream then sits at or below every value of G.

WHERE THE ROUTE STOPS. At o = 1 with the partner at the input scale,
the output window is b times the input window and z = -M- sits INSIDE
G's range: max(G, -M-) is a clamp of G, not G. The clamp dies at c iff
some G-death box has its overlap zone strictly above -M- (at depth 1
the zone between output cells q and q + 1 is [q + 1 - M-, q + M+],
above -M- iff q >= 0). The sum's death boxes translate along the
prefix lattice (u -> u + b^n, legal while the prefix stays in range),
so a zone at q >= 0 is expected; that expectation is a TRANSPLANT of
the theorem's conclusion into a case it does not cover, and the rig
decides it. A cell where the clamp survives at L* - 1 and the FREE
partner also fails to certify is a cell where the comparator on the
sum's output is cheaper than the sum -- a finding, not a failure.

THE ENGINE. explore_comparator_delay.py's PieceGame (interval
evaluation on the integer endpoints of the input cells, exhaustive
adversary tree, a certificate at r rounds a proof of death, a survival
of the search never a floor), with two additions: an interval map for
max(G, z) and min(G, z) over the product and the sum, the partner
optionally scaled by b^o to the output's scale; and a CONSTANT
confinement of the adversary, one stream's digit fixed, the theorem's
own witness (49 or 25 moves a round instead of 343 or 125 at three
streams, 7 or 5 at two). The confined game is HARDER for the reader
than G's own -- its image is [lo_G, max(hi_G, hi of z's cell)], a
superset of G's -- so a confined certificate comes at a round at most
G's, and, the adversary being weakened, is a certificate for the full
game.

THE SLATE, frozen before the engine ran.

P-A THE CONTROLS. (i) x y at o = 0 over the 7 representable cells of
    radices 2..4: certified at c* - 1 and surviving at c*, the product
    law (explore_comparator_delay.py F4 reads the fused unit at the
    same rounds 2, 1, 2, 1, 2, 2, 1). (ii) x + y at o = 1 over the 20
    cells of radices 2..5: certified at L* - 1 at the 10 cells with
    L* = 2, surviving at L* at 20 of 20 (the lookahead criterion).
    (iii) max(x, z) with z confined constant -a-, at c = 0, o = 0:
    survives at 20 of 20 cells, as the identity does -- the confined
    max of a stream against the bottom is the stream.
P-B THE THEOREM AT o = 0 [theorem; the print its check]. max(x y, z)
    and min(x y, z) at o = 0 over the 7 representable cells: the
    confined adversary (z constant -a- for max, +a+ for min) certifies
    at c* - 1 at every cell, at a round at most the product's own;
    the full adversary survives the search at c* at every cell.
P-C THE PARTNER AT THE OUTPUT'S SCALE [theorem; the print its check].
    max(x + y, b z) at o = 1 over the 20 cells of radices 2..5: the
    confined adversary certifies at L* - 1 at the 10 cells with L* = 2,
    at a round at most the sum's own (one); the full adversary survives
    the search at L* at 20 of 20.
P-D THE CLAMP [the transplant; the rig decides]. max(x + y, z) at
    o = 1, z at the input scale, over the 20 cells: certified at
    L* - 1 at the 10 cells with L* = 2 -- by the confined adversary
    where the clamp alone kills, else by the free one -- and surviving
    at L* at 20 of 20. The print records, per cell, which adversary
    certified.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a disagreement (a product or sum cell off its law, a
   confined max(x, z) cell certified at c = 0) -> the engine or the
   confinement is not the comparator rig's; nothing below is read.
K2 A P-B or P-C cell prints a survival at c* - 1 (L* - 1) against the
   confined adversary to a searched depth at or beyond the bare unit's
   certificate round -> the theorem is WRONG as written; the
   derivation is redone before anything below is read.
K3 A P-B or P-C cell prints a certificate at c* (L*) -> the upper half
   (explore_comparator_delay.py (4)) is wrong; same consequence.
K4 A P-D cell prints a survival at L* - 1 against the FREE adversary
   to a searched depth at or beyond 1 -> the comparator on the sum's
   output at the input scale is cheaper than the sum at that cell;
   the cell is the finding.
K5 A P-D cell prints a certificate at L* -> impossible by the upper
   half; an engine bug, nothing read.

POSITIVE CONTROL: P-A whole, before any comparator line is read.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. x y at o = 0: certified at c* - 1 at rounds 2,
   1, 2, 1, 2, 2, 1 at (2,1,1), (3,1,2), (3,2,2), (4,1,3), (4,2,2),
   (4,2,3), (4,3,3) and surviving at c* at 7 of 7, the rounds the
   fused unit read. x + y at o = 1: certified at L* - 1 in one round
   at the 10 cells with L* = 2, surviving at L* at 20 of 20. max(x, z)
   with z confined to the bottom survives c = 0 at 20 of 20. K1 never
   fired.

F2 THE THEOREM AT o = 0 [theorem; the rig its check at 7 cells each].
   max(x y, z) with z confined to the bottom and min(x y, z) with z
   confined to the top: certified at c* - 1 at every representable
   cell, at rounds 2, 1, 2, 1, 2, 2, 1 -- EQUAL to the product's own
   at every cell, not merely at most -- and surviving at c* against
   the full adversary at 7 of 7 (searched depth 1, the 343-ary tree;
   the floor is the theorem's). K2 and K3 never fired.

F3 THE PARTNER AT THE OUTPUT'S SCALE [theorem; the rig its check].
   max(x + y, b z) at o = 1: certified at L* - 1 in one round by the
   confined adversary at the 10 cells with L* = 2, the sum's own
   round, and surviving at L* at 20 of 20. K2 and K3 never fired.

F4 THE CLAMP IS AS HARD AS THE SUM [theorem (the translation lemma
   below, found after the print); the rig its check at 20 cells].
   max(x + y, z) at o = 1 with z at the input scale: the confined
   adversary -- the clamp max(x + y, -M-) -- certifies at L* - 1 in
   one round at all 10 cells with L* = 2; the free adversary certifies
   at the same round; both survive at L* at 20 of 20. Every cell with
   L* = 1 is exact by the offset alone. K4 and K5 never fired.

  THE TRANSLATION LEMMA. A depth-n box of the sum has image
  [m - 2 a-, m + 2 a+] over (b - 1) b^n, m = u + v the digit sum of the
  two prefixes, so death at a box is a property of m alone, and every
  integer m' in [2 u_min, 2 u_max] is the digit sum of some legal pair
  (rho >= 1 makes every integer of the prefix range a prefix). At
  offset 1 the output cells of depth t have lower ends (q - M-)
  b^(1-t), so the zone between cells q and q + 1 is [(q + 1 - M-)
  b^(1-t), (q + M+) b^(1-t)], and m -> m + b^(c+1) (n = t + c) moves
  the image by b^(1-t), one zone up: a death box's zone index q is
  carried to q + 1 by a legal box while m + b^(c+1) stays in range.
  Take the top of the orbit, m > 2 u_max - b^(c+1): the strict
  containment lo < (q + 1 - M-) b^(1-t) then reads q > lo b^(t-1) - 1
  + M- with lo b^(t-1) > 2 M+ b^(t-1) - 2 (M+ + M-) b^(t-1-n) - 1,
  and the right side is at least -1 exactly when 2 a+ (b - 1) + a-
  (b - 2) >= b (b - 1), which a- + a+ >= b guarantees (equality at
  a+ = 1, a- = b - 1); so q > -1, q >= 0, and the zone's lower end
  (q + 1 - M-) b^(1-t) is strictly above -M-. There the clamp's
  image [max(lo, -M-), hi] still strictly contains the zone, so the
  clamp dies wherever the sum dies, at every cell with rho >= 1 and
  every lookahead; with the upper half, the delay of max(x + y, z)
  EQUALS the sum's. Nothing in the lemma is the sum's beyond the
  image being a translate of one interval by the digit sum: it holds
  for every map whose box images translate along the prefix lattice.

VERDICT. A comparator on an output is EXACTLY free: for every map G
whose range fits the window, and for a partner at the output's own
scale under any G, the constant bottom stream makes the comparator the
unit itself; for the sum with its partner at the input scale, the
translation lemma. A datapath's delay table is its arithmetic
skeleton's with the comparators deleted, on an output as inside a
unit.

RUN RECORD: pure Python, integers only, standard library; imports the
engine from explore_comparator_delay.py; under memwatch, peak commit
12.0 MB against the 512 MB default; wall 155 s at the default radix
5 (the smoke run at radix 3, 19 s). Reproduced by
python prime/code/explore_output_comparator.py [BMAX]
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_comparator_delay as cd  # noqa: E402

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------------------ interval maps
# Inputs are integer intervals at scale s = (b-1) b^n. The product sits
# at scale s^2; the partner is lifted to that scale by multiplying by
# s. A partner at the output's scale is multiplied by b^o besides.

def iv_max_xy_z(ivs, s):        # max(x y, z), o = 0
    lo, hi = cd._prod(ivs[0], ivs[1])
    l2, h2 = ivs[2]
    return max(lo, l2 * s), max(hi, h2 * s), s * s


def iv_min_xy_z(ivs, s):        # min(x y, z), o = 0
    lo, hi = cd._prod(ivs[0], ivs[1])
    l2, h2 = ivs[2]
    return min(lo, l2 * s), min(hi, h2 * s), s * s


def iv_max_sum_z(ivs, s):       # max(x + y, z), o = 1, z at the input scale
    (l0, h0), (l1, h1), (l2, h2) = ivs
    return max(l0 + l1, l2), max(h0 + h1, h2), s


def make_max_sum_bz(b):         # max(x + y, b z), o = 1, z at the output's scale
    def f(ivs, s):
        (l0, h0), (l1, h1), (l2, h2) = ivs
        return max(l0 + l1, b * l2), max(h0 + h1, b * h2), s
    return f


def iv_max_x_z(ivs, s):         # max(x, z), o = 0
    (l0, h0), (l1, h1) = ivs
    return max(l0, l1), max(h0, h1), s


# ---------------------------------------------------------- confinement

class ConstGame(cd.PieceGame):
    """PieceGame with one stream's digit FIXED: `const` = (index, digit).
    The adversary's moves are every digit vector with that coordinate
    at that digit; the reader is unchanged."""

    def __init__(self, b, am, ap, c, k, fmap, o=0, const=None):
        super().__init__(b, am, ap, c, k, fmap, o)
        if const is not None:
            i, d = const
            self.moves = [mv for mv in self.moves if mv[i] == d]


def cert_and_survival(cell, k, fmap, o, L, T, const):
    """The certificate at L - 1 (confined if `const`, else free) and the
    survival search at L against the full adversary. Returns
    (cert, depth1, survives, depth2)."""
    b, am, ap = cell
    cert, d1 = (None, 0)
    if L - 1 - o >= 0:
        cert, d1 = ConstGame(b, am, ap, L - 1 - o, k, fmap, o,
                             const).certificate_depth(T)
    surv, d2 = ConstGame(b, am, ap, L - o, k, fmap, o).certificate_depth(
        T, budget=cd.SURVIVAL_BUDGET)
    return cert, d1, surv, d2


def run_block(name, k, fmap, o, law, bmax, T, rep=None, const=None,
              fmap_of_b=None):
    rows = []
    print(f"\n=== {name}: o = {o}, radices 2..{bmax}"
          + (f", stream {const[0]} confined to digit {const[1]}"
             if const else ", free adversary"))
    print("  cell rho | L* | cert at L*-1 [depth] | survives at L* [depth]")
    for cell in cd.census(bmax):
        b, am, ap = cell
        if rep is not None and not rep(b, am, ap):
            print(f"  ({b},{am},{ap}) not representable at o = {o}")
            continue
        L = law(b, am, ap)
        f = fmap_of_b(b) if fmap_of_b else fmap
        cst = None
        if const is not None:
            cst = (const[0], -am if const[1] == "bottom" else ap)
        cert, d1, sr, d2 = cert_and_survival(cell, k, f, o, L, T, cst)
        print(f"  ({b},{am},{ap}) rho={am+ap+1-b} | L*={L} | "
              f"{'-' if L - 1 - o < 0 else (cert if cert is not None else 'survives')} [{d1}] | "
              f"{'yes' if sr is None else 'NO at round ' + str(sr)} [{d2}]")
        rows.append((cell, L, cert, d1, sr is None, d2))
    return rows


def main():
    T = 12
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    b3 = min(bmax, 4)
    t0 = time.time()

    print("=== P-A (i): x y at o = 0, the product law")
    xy = run_block("x y", 2, cd.iv_xy, 0, cd.product_law, b3, T,
                   rep=cd.product_representable)
    prod_round = {}
    for cell, L, cert, d1, surv, d2 in xy:
        if L - 1 >= 0:
            ok(cert is not None, f"K1 x y survives c*-1 at {cell}")
            prod_round[cell] = cert
        ok(surv, f"K1 x y certified at c* at {cell}")

    print("\n=== P-A (ii): x + y at o = 1, the lookahead criterion")
    s2 = run_block("x + y", 2, cd.iv_sum2, 1, cd.sum_law, bmax, T)
    sum_round = {}
    for cell, L, cert, d1, surv, d2 in s2:
        if L - 2 >= 0:
            ok(cert is not None, f"K1 x + y survives L*-1 at {cell}")
            sum_round[cell] = cert
        ok(surv, f"K1 x + y certified at L* at {cell}")

    print("\n=== P-A (iii): max(x, z) at c = 0 with z confined to the bottom")
    n_alive = 0
    for (b, am, ap) in cd.census(bmax):
        cert, depth = ConstGame(b, am, ap, 0, 2, iv_max_x_z, 0,
                                (1, -am)).certificate_depth(T, budget=cd.SURVIVAL_BUDGET)
        ok(cert is None, f"K1 confined max(x, z) certified at c = 0 at ({b},{am},{ap})")
        n_alive += cert is None
        print(f"  ({b},{am},{ap}) | c = 0: "
              f"{'survives' if cert is None else 'CERTIFIED at round ' + str(cert)} [{depth}]")
    print(f"  confined max(x, z): {n_alive} of {len(cd.census(bmax))} survive at c = 0")

    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return

    print("\n=== P-B: the theorem at o = 0 -- max(x y, z), min(x y, z)")
    for name, fmap, side in (("max(x y, z)", iv_max_xy_z, "bottom"),
                             ("min(x y, z)", iv_min_xy_z, "top")):
        rows = run_block(name, 3, fmap, 0, cd.product_law, b3, T,
                         rep=cd.product_representable, const=(2, side))
        exact = 0
        for cell, L, cert, d1, surv, d2 in rows:
            if L - 1 >= 0:
                ok(cert is not None and cert <= prod_round[cell],
                   f"K2 {name} at {cell}: confined certificate {cert} [{d1}] "
                   f"against the product's round {prod_round[cell]}")
            ok(surv, f"K3 {name} certified at c* at {cell}")
            exact += (L == 0 or cert is not None) and surv
        print(f"  {name}: {len(rows)} cells, exactly G's delay at {exact}")

    print("\n=== P-C: the partner at the output's scale -- max(x + y, b z) at o = 1")
    rows = run_block("max(x + y, b z)", 3, None, 1, cd.sum_law, bmax, T,
                     const=(2, "bottom"), fmap_of_b=make_max_sum_bz)
    exact = 0
    for cell, L, cert, d1, surv, d2 in rows:
        if L - 2 >= 0:
            ok(cert is not None and cert <= sum_round[cell],
               f"K2 max(x + y, b z) at {cell}: confined certificate {cert} [{d1}] "
               f"against the sum's round {sum_round[cell]}")
        ok(surv, f"K3 max(x + y, b z) certified at L* at {cell}")
        exact += (L == 1 or cert is not None) and surv
    print(f"  max(x + y, b z): {len(rows)} cells, exactly the sum's delay at {exact}")

    print("\n=== P-D: the clamp -- max(x + y, z) at o = 1, z at the input scale")
    clamp = run_block("max(x + y, z)", 3, iv_max_sum_z, 1, cd.sum_law, bmax, T,
                      const=(2, "bottom"))
    free = run_block("max(x + y, z)", 3, iv_max_sum_z, 1, cd.sum_law, bmax, T)
    by_clamp = by_free = cheaper = 0
    for (cell, L, cc, dc, sc, _), (_, _, cf, df, sf, d2) in zip(clamp, free):
        ok(sf, f"K5 max(x + y, z) certified at L* at {cell}")
        if L - 2 < 0:
            continue
        if cc is not None:
            by_clamp += 1
            who = f"clamp kills at round {cc}"
        elif cf is not None:
            by_free += 1
            who = f"clamp survives [{dc}], free adversary kills at round {cf}"
        else:
            cheaper += 1
            who = f"K4 SURVIVES L*-1 against the free adversary [{df}]: cheaper than the sum"
        print(f"  {cell}: {who}")
    print(f"  max(x + y, z): {len(clamp)} cells; at the {by_clamp + by_free + cheaper} "
          f"with L* = 2: certified by the clamp at {by_clamp}, by the free partner "
          f"alone at {by_free}, cheaper than the sum at {cheaper}")

    print(f"\nwall {time.time()-t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
