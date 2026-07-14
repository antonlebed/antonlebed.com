"""explore_readout_triangle.py — THE TRIANGLE: the full-vector
designed readout (the readout theorem's designed-engine face; ROAD
P194, VERTIGO STOCK (a) remainder; the P190-parked triangularity
hunch).

THE QUESTION (ROAD P194). The readout theorem (P192,
explore_readout_proof.py) proves every arrival class of a totally
ramified f = 1 window of Q_2 reads a window of the canonical digits
of w = 2/pi^e; P190's construction kit places the STOP (the first
nonzero). Open: can a designed window place the WHOLE digit vector
w_1..w_{3e/2-1} — and is the coefficient-to-digit map TRIANGULAR?

THE HAND DERIVATION (SCRATCH.md P194 passes 1-2, frozen before this
file existed).

Setup: F(x) = x^e + sum_{i=1}^{e-1} 2 b_i x^i - 2d Eisenstein
(d odd), pi a root, so with T := sum (b_i/d) pi^i:

    w = 2/pi^e = (1/d) (1 - T)^{-1} = (1/d)(1 + T + T^2 + ...).

THE PARAMETERS (the grid): beta_i = b_i mod 2 (i = 1..e-1) feed
level i; delta = (d mod 4 == 3) feeds level e (1/d = 1 + 2s,
2s = s w pi^e — the level-0 carry); gamma_i = (b_i div 2) mod 2
(i = 1..e/2-1) feed level e+i (2 gamma_i pi^i = gamma_i w pi^{e+i});
all deeper coefficient bits feed >= 3e/2, zeroed in the grid.
COUNT: (e-1) + 1 + (e/2-1) = 3e/2 - 1 = the window length — the
map is SQUARE.

THE TRIANGLE (claim): in the parameter order beta_1..beta_{e-1},
delta, gamma_1..gamma_{e/2-1} (matched to digit levels 1..3e/2-1)
the grid map is UNITRIANGULAR over F_2: digit r = (level-r
parameter) XOR (a function of strictly earlier parameters). Why:
a canonical-digit carry born at level s is deposited from level
s + e up with a w-tail (2 pi^s = w pi^{s+e}), so a window level r
hears carries only from levels s <= r - e (deposit = the level-s
overflow times w_{r-e-s}, every factor a function of parameters at
levels <= r - e) — for r < e none, for r = e the level-0 carry
alone (= delta), for r > e functions of parameters <= r - e; T^k
products (k >= 2) at level r
have all parts < r; even parts of other b_i sit at their own
diagonals or deeper (cross terms 2 gamma_i beta_j land at e+i+j,
strictly past gamma_i's diagonal); each diagonal coefficient is a
unit mod 2 (d odd, w_0 = 1). COROLLARY: the grid map is a BIJECTION
onto {0,1}^{3e/2-1} — every window word printable, each by exactly
one grid design — and the greedy digit-by-digit solve (flip the
level-r parameter iff digit r misses) never disturbs the prefix.

THE FROZEN SLATE (SCRATCH.md P194 pass 3, frozen before this file):

FV1 (bijection census): the full grid's window vectors are pairwise
    distinct = ALL of {0,1}^{3e/2-1} — exhaustive at e = 4 (32),
    e = 6 (256; non-2-power: placement is game-independent),
    e = 8 (2048).
FV2 (triangularity, flip-tested): flipping the level-r parameter
    changes digit r and NO digit < r — exhaustive at e = 4, 6, 8
    (the flip partner is a grid member: lookups, no new fields).
FV3 (greedy placement at e = 16): every target word placed exactly,
    <= 23 flips, prefix never disturbed — 24 random words +
    all-ones + all-zeros + THE SKELETON WORD (nonzero exactly
    {8, 20}): a designed no-stop world carrying zeta32's vector on
    a sparse-grid Eisenstein polynomial.
FV4 (identity row): all-zero parameters = x^e - 2, window all-zero,
    at e = 4, 6, 8, 16.
FV5 (the P190 kit re-read as triangle rows, hand-frozen):
    x^16+2x^8-2 window nonzero EXACTLY {8, 16}; x^16+2x^8-6
    EXACTLY {8}; x^16+4x^4+2x^8-6 EXACTLY {8, 20}.
FV6 (the game tie, end-to-end): for two placed e = 8 words
    (alternating 10101010101; the e = 8 skeleton word, nonzero
    exactly {4, 10}) + the e = 16 skeleton word, sampled arrival
    minima at every class equal 2e + ladder_rel on the placed word,
    rigid below freedom, starters at 2e + 1 — the designed world
    PRINTS the chosen word in its arrival spectra.

THE DESIGN. [A] census: enumerate the full grid at e = 4, 6, 8
(bit r-1 <-> level-r parameter), extract each window by measured
digits (m16.w_element_g + w_digits_g, reconstruction-asserted,
amax = 2e, n = 3e/2), assert FV1 + FV4. [B] flips: for every
(design, parameter) pair compare stored windows — prefix equal,
diagonal digit flipped (FV2). [C] e = 16: FV4 + FV5 spot rows +
FV3 greedy (one measure per level; per-step prefix invariant
asserted). [D] the game tie: build the three placed worlds at
amax = 4e, run m16.sampled_spec (250/class), assert FV6 against
rp.ladder_rel on the measured (= placed) digits. The engine only
ever reads MEASURED digits — the triangle steers the design, never
the read.
Run: python prime/code/explore_readout_triangle.py

FINDINGS (entered post-run, copied from printed output; tiers per
CLAUDE.md).

1. THE TRIANGLE (theorem — the unitriangularity proof is general in
   even e, nowhere using e = 2^s; the engine verifies it
   exhaustively at e = 4, 6, 8 and by placement at e = 16): the
   grid map (beta, delta, gamma) -> (w_1..w_{3e/2-1}) is
   unitriangular over F_2, hence a BIJECTION onto {0,1}^{3e/2-1}.
   Exhaustive: 32 / 256 / 2048 designs give 32 / 256 / 2048
   pairwise-distinct windows (= every word), and ALL flip pairs
   (160 / 2,048 / 22,528) are prefix-clean with the diagonal digit
   hit — the e = 6 row shows placement is game-independent
   (non-2-power e). The identity design x^e - 2 prints the all-zero
   word at e = 4, 6, 8, 16. Parameter count = word length exactly:
   the window word IS the sub-leading Eisenstein coefficient data
   (b_i mod 2 at levels < e; d mod 4 at e; b_i div 2 mod 2 for
   i < e/2 at the levels above e),
   re-encoded bijectively — the readout is a lossless PROGRAMMABLE
   channel, and P190's stop kit is its first-nonzero shadow.

2. FULL-VECTOR PLACEMENT AT e = 16 (rule in range): all 27 target
   words (24 seeded random + all-ones + all-zeros + the skeleton
   word) placed EXACTLY by the greedy solve, 648 measures total
   (24 per word, the bound), per-step prefix invariant asserted at
   every level. The skeleton word (nonzero exactly {8, 20},
   zeta32's vector) resolves to [-6,4@4,2@8] — the P190 rung-56
   witness REDISCOVERED by the solver, and by the triangle's
   bijection (finding 1) that design is the UNIQUE grid member
   carrying zeta32's word.

3. THE GAME TIE (rule in range; FV6): the designed worlds PRINT
   their chosen words in live arrival spectra — e = 8 alternating
   10101010101 -> [-6,6@1,6@2,4@3,2@4,2@5,2@7] (w_1 = 1: the lock,
   all classes rigid {17}), the e = 8 skeleton word 00010000010 ->
   [-6,4@2,2@4] (class minima 18/20/28: the m = 1 floor, the empty
   class-2 window, the stopless top — rels 2/4/12 by the ladder on
   the placed word), the e = 16 skeleton word -> [-6,4@4,2@8] (class-1
   min 56, the no-stop landing); at every class the sampled minimum
   equals 2e + ladder_rel on the measured digits, rigid below
   freedom, starters at 2e + 1 (17/17/33).

4. THE P190 KIT RE-READ (rule in range; FV5): the three hand-frozen
   triangle rows are exact — x^16+2x^8-2 nonzero exactly {8, 16}
   (beta_8 + the T^2 self-product at level 16), x^16+2x^8-6 exactly
   {8} (delta cancels the T^2 term: "mu mod 4 tunes the rel-16
   digit" IS delta), x^16+4x^4+2x^8-6 exactly {8, 20} (gamma_4 at
   level 20) — the kit's carry folklore is the triangle's algebra.

PRE-GREEN FAILURES: none — green on the first complete run (the
three FV5 vectors and the two e = 8 tie predictions were frozen
from the hand algebra before any code; the P152/P187/P188
adjudication seat sat empty again, second face in a row).

RUN RECORD (python explore_readout_triangle.py, 8.6 s, exit 0):
117,909 checks passed (50,248 this module + 67,661 imported; the
flip pairs dominate this module, digit-reconstruction self-checks
the imported count). Printed rows as copied: bijections
32/256/2048; flip pairs 160/2048/22528; 27 words, 648 measures;
tie designs + class minima as in findings 3.
"""

import random

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_mu8_grading as mu8
import explore_mu16_face as m16
import explore_mu32_face as m32
import explore_readout_proof as rp

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ------------------------------------------------------------ the grid


def grid_eis(e, bits):
    """Grid design -> Eisenstein coefficients (low -> high, monic).
    bit r-1 <-> level-r parameter: beta_r (r < e), delta (r = e),
    gamma_{r-e} (r > e)."""
    b = [0] * e                          # b[i], i = 1..e-1
    for r in range(1, e):
        if bits >> (r - 1) & 1:
            b[r] += 1
    for i in range(1, e // 2):
        if bits >> (e - 1 + i) & 1:
            b[i] += 2
    d = 3 if bits >> (e - 1) & 1 else 1
    return [-2 * d] + [2 * b[i] for i in range(1, e)] + [1]


def window(e, bits, amax=None):
    """Measured window vector (w_1..w_{3e/2-1}) of a grid design."""
    F = lc.LF("t%d_%d" % (e, bits), 2, [0, 1], grid_eis(e, bits),
              amax if amax else 2 * e)
    w = m16.w_element_g(F)
    digs = m16.w_digits_g(F, w, n=3 * e // 2)
    return tuple(digs[1:])


# ------------------------------------------- [A] + [B] census and flips


def census(e):
    nbits = 3 * e // 2 - 1
    wins = [window(e, bits) for bits in range(1 << nbits)]
    ok(wins[0] == (0,) * nbits, "e=%d: identity x^e-2 not silent" % e)
    ok(len(set(wins)) == 1 << nbits, "e=%d: grid map not injective" % e)
    for bits in range(1 << nbits):
        for j in range(nbits):
            other = wins[bits ^ (1 << j)]
            ok(wins[bits][:j] == other[:j],
               "e=%d bits=%d flip %d moved the prefix" % (e, bits, j))
            ok(wins[bits][j] != other[j],
               "e=%d bits=%d flip %d missed its diagonal" % (e, bits, j))
    print("[A/B] e = %d: %d designs -> %d distinct windows "
          "(bijection); %d flip pairs prefix-clean, diagonal hit"
          % (e, 1 << nbits, 1 << nbits, (1 << nbits) * nbits))


# ------------------------------------------------- [C] greedy placement


def solve(e, word):
    """Greedy full-vector placement; returns (bits, measures)."""
    nbits = 3 * e // 2 - 1
    bits, measures = 0, 0
    for r in range(1, nbits + 1):
        vec = window(e, bits)
        measures += 1
        ok(vec[:r - 1] == word[:r - 1],
           "e=%d greedy: prefix broke at level %d" % (e, r))
        if vec[r - 1] != word[r - 1]:
            bits ^= 1 << (r - 1)
    vec = window(e, bits)
    measures += 1
    ok(vec == word, "e=%d greedy: final window != word" % e)
    return bits, measures


def spot_rows_16():
    rows = (("x16+2x8-2", [-2] + [0] * 7 + [2] + [0] * 7 + [1], {8, 16}),
            ("x16+2x8-6", [-6] + [0] * 7 + [2] + [0] * 7 + [1], {8}),
            ("x16+4x4+2x8-6",
             [-6, 0, 0, 0, 4, 0, 0, 0, 2] + [0] * 7 + [1], {8, 20}))
    for name, eis, nz in rows:
        F = lc.LF(name, 2, [0, 1], eis, 32)
        w = m16.w_element_g(F)
        digs = m16.w_digits_g(F, w, n=24)
        got = {r for r in range(1, 24) if digs[r]}
        ok(got == nz, "%s: nonzero %s != frozen %s" % (name, got, nz))
        print("  [C] %s: window nonzero exactly %s (FV5)"
              % (name, sorted(nz)))


# --------------------------------------------------- [D] the game tie


def game_tie(e, word, rng, per_class=250):
    bits, _ = solve(e, word)
    F = lc.LF("tie%d_%d" % (e, bits), 2, [0, 1], grid_eis(e, bits),
              4 * e)
    w = m16.w_element_g(F)
    digs = m16.w_digits_g(F, w, n=3 * e // 2)
    ok(tuple(digs[1:]) == word, "tie e=%d: world does not carry word" % e)
    classes = tuple(1 << k for k in range((e.bit_length() - 1) + 1))
    spec = m16.sampled_spec(F, rng, classes, per_class)
    for c in classes[:-1]:               # arrival classes (c < e)
        mu = (e // c).bit_length() - 1
        rel = rp.ladder_rel(e, mu, digs)
        end = 3 * e // 2 if c == 1 else 1 << mu
        ok(min(spec[c]) == 2 * e + rel,
           "tie e=%d c=%d: min %s != %d" % (e, c, sorted(spec[c]),
                                            2 * e + rel))
        if rel < end:
            ok(spec[c] == {2 * e + rel},
               "tie e=%d c=%d: spectrum %s not rigid" % (e, c, spec[c]))
    ok(min(spec[e]) == 2 * e + 1, "tie e=%d: starters != %d"
       % (e, 2 * e + 1))
    print("  [D] e = %d word %s: design %s prints it — class minima "
          "= the ladder at every class, starters %d"
          % (e, "".join(map(str, word)),
             m32.poly_name(tuple(grid_eis(e, bits)[:-1])), 2 * e + 1))


# ---------------------------------------------------------------- run


def run():
    rng = random.Random(194)

    print("== [A/B] the bijection census + flip triangularity ==")
    for e in (4, 6, 8):
        census(e)

    print("== [C] e = 16: identity + spot rows + greedy placement ==")
    ok(window(16, 0) == (0,) * 23, "e=16: identity x^16-2 not silent")
    spot_rows_16()
    skel16 = tuple(1 if r in (8, 20) else 0 for r in range(1, 24))
    words = [tuple(rng.randrange(2) for _ in range(23))
             for _ in range(24)]
    words += [(1,) * 23, (0,) * 23, skel16]
    total_meas = 0
    for word in words:
        bits, meas = solve(16, word)
        total_meas += meas
        ok(meas <= 24, "e=16: %d measures" % meas)
    print("  [C] %d words placed exactly (incl. all-ones, all-zeros, "
          "the skeleton word), %d measures total" % (len(words),
                                                     total_meas))
    skel_bits, _ = solve(16, skel16)
    print("  [C] the skeleton-word design: %s"
          % m32.poly_name(tuple(grid_eis(16, skel_bits)[:-1])))

    print("== [D] the game tie: designed worlds print their words ==")
    game_tie(8, (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1), rng)
    game_tie(8, tuple(1 if r in (4, 10) else 0 for r in range(1, 12)),
             rng)
    game_tie(16, skel16, rng)

    imported = (lc.CHECKS + ad.CHECKS + mu8.CHECKS + m16.CHECKS
                + m32.CHECKS + rp.CHECKS)
    print("ALL GREEN: %d checks passed (%d this module + %d imported)"
          % (CHECKS + imported, CHECKS, imported))


if __name__ == "__main__":
    run()
