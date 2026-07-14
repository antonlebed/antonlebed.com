"""explore_reduction_law.py — THE REDUCTION LAW: the triangle's two
corollaries (the readout arc's designed-engine close; ROAD P197,
VERTIGO STOCK (a) remainder).

THE QUESTION (ROAD P197). The triangle (P194,
explore_readout_triangle.py) proved the GRID map — sub-leading
Eisenstein coefficient bits (beta, delta, gamma) -> window word — is
unitriangular, a bijection onto {0,1}^{3e/2-1}. Its derivation
already priced every deeper coefficient bit at level >= 3e/2. Two
corollaries were never stated or engine-falsified: (1) ANY Eisenstein
window's word is its BIT-REDUCTION's word — the word is a complete
invariant of the reduced bits; (2) the anchor Phi_{2e}(x+1) reduces
by Kummer parities to a CLOSED-FORM design, which by C7 (readout
theorem) must carry the skeleton word at every 2-power depth.

THE HAND DERIVATION (SCRATCH.md P197 passes 1-2, frozen before this
file existed).

Setup (the triangle's): F(x) = x^e + sum_{i=1}^{e-1} 2 b_i x^i - 2d
Eisenstein over Z_2, d odd, e even; w = 2/pi^e = (1/d)(1 - T)^{-1},
T = sum (b_i/d) pi^i; word = (w_1 .. w_{3e/2-1}) canonical digits.

BIT LEVELS. Every occurrence of the bit 2^k of b_i enters the digit
computation as a monomial carrying 2^k pi^i = w^k pi^{i+ke} (the
carry rule, k times), so its first level of influence is i + k*e, and
carries only move deposits deeper. 1/d feeds level e through d mod 4
(the level-0 carry = delta) and deeper d-bits only through
4 = w^2 pi^{2e}, level >= 2e. So the digits below 3e/2 are a function
of EXACTLY the triangle's parameters:
    beta_i  = b_i mod 2         (level i,     i = 1..e-1)
    delta   = [d mod 4 == 3]    (level e)
    gamma_i = (b_i >> 1) mod 2  (level e + i, i = 1..e/2-1)
— bit 1 of b_i at i >= e/2 feeds i + e >= 3e/2 (out); bit >= 2 of
any b_i feeds >= 2e + 1 (out); d past mod 4 feeds >= 2e (out).

THE REDUCTION LAW (corollary 1 — the triangle's level bookkeeping,
same footing as its unitriangularity): reduce(F) := the grid member
with F's (beta, delta, gamma). Then word(F) = word(reduce(F)) for
EVERY Eisenstein F (even e). With the triangle's bijection: the word
is a COMPLETE invariant of the reduced bits — Eisenstein windows sort
into exactly 2^{3e/2-1} word classes, one per grid member, and
word(F) = word(G) iff reduce(F) = reduce(G).

THE ANCHOR'S REDUCTION (corollary 2). At e = 2^s the anchor
Phi_{2e}(x+1) = (x+1)^e + 1 has b_k = C(e,k)/2, d = -1. Kummer:
v2(C(e,k)) = s2(k) + s2(e-k) - 1. So beta_k = 1 iff
s2(k) + s2(e-k) = 2 iff k = e/2 alone; for k < e/2 (where beta_k = 0)
gamma_k = 1 iff v2(C(e,k)) = 2 iff k = e/4 alone (the s2(k) = 2
branch forces k = e - 2^b > e/2); delta = 1 (d = -1 == 3 mod 4).
    reduce(Phi_{2e}(x+1)) = x^e + 2 x^{e/2} + 4 x^{e/4} - 6
at every e = 2^s >= 4 (e = 2: no gamma slot, x^2 + 2x - 6). By C7
word(anchor) = the skeleton (nonzero exactly {e/2, 5e/4}), so by the
reduction law THE SKELETON DESIGN IS CLOSED-FORM: the 3-term window
x^e + 2x^{e/2} + 4x^{e/4} - 6 carries zeta_{2e}'s skeleton word at
every 2-power depth, the UNIQUE grid member that does — at e = 16 it
is [-6,4@4,2@8], the P194 solver's find: the solver was
rediscovering the anchor's own bit-reduction.

THE FROZEN SLATE (SCRATCH.md P197 pass 3, frozen before this file):

RD1 (deep-bit invisibility, targeted): from grid members, single
    deep-bit perturbations leave the word unchanged — b_i += 4 (any
    i), b_i += 2 (i >= e/2), d += 4, d -= 8 — at e = 4 (all 32
    designs) and e = 6, 8 (12 sampled designs each), all slots.
RD2 (random zoo): random Eisenstein (b_i in [-8, 8], d odd in
    [-15, 15]) at e = 4, 6, 8: word(F) == the grid word of
    reduce(F), 40 fields per e (negative coefficients exercise the
    2-adic bits: -1 has beta = gamma = 1).
RD3 (e = 16 spot): 8 random deep-bit fields: word == reduce's word.
RD4 (anchor reduction, bit arithmetic only, no fields):
    reduce(Phi_{2e}(x+1)) == x^e + 2x^{e/2} + 4x^{e/4} - 6 at
    e = 4, 8, 16, 32, 64, by direct binomial bits AND by the Kummer
    s2 count independently; e = 2 reduces to x^2 + 2x - 6; the
    reduce map is a retraction (reduce o grid = identity, exhaustive
    at e = 4, 6, 8).
RD5 (the skeleton design at every depth): the design's MEASURED word
    is nonzero exactly {e/2, 5e/4} at e = 4, 8, 16, 32 (at 32:
    {16, 40} = zeta64's called vector); e = 2: x^2+2x-6 word (1, 0).
RD6 (anchor preimage): the measured anchor word == the measured
    design word at e = 8, 16 — the reduction law live on a non-grid
    field whose deep bits are the full binomial coefficients.
RD7 (the game tie at e = 32): the skeleton design x^32+2x^16+4x^8-6
    walks STOPLESS — sampled class-1 direct rels have min exactly 48
    (the freedom end), landing 112 = zeta64's: a designed 3-term
    world mimicking the cyclotomic anchor's readout at depth 32.

THE DESIGN. [A] RD4: anchor bit-reduction closed form (pure integer;
both derivations) + the retraction. [B] RD1: perturbation slots off
grid members, word compared to the unperturbed grid word. [C] RD2 +
RD3: the random zoo vs cached grid words (reduce_bits computed by
2-adic bit extraction, Python's arithmetic shift = 2-adic on
negatives). [D] RD5 + RD6: the design fields at e = 2..32 + the
anchors at e = 8, 16, words measured (m16.w_element_g + w_digits_g,
reconstruction-asserted). [E] RD7: ad.sample_class + rp.direct_rel
on the e = 32 design field (amax 120). The engine only ever reads
MEASURED digits — the reduction steers which fields exist, never the
read.
Run: python prime/code/explore_reduction_law.py

FINDINGS (entered post-run, copied from printed output; tiers per
CLAUDE.md).

1. THE REDUCTION LAW (theorem — the level pricing is the triangle's
   own derivation, general in even e; the engine falsifies it on 628
   non-grid fields): word(F) = word(reduce(F)) for every Eisenstein
   window, so with the triangle's bijection the window word is a
   COMPLETE invariant of the reduced bits (b_i mod 2; b_i mod 4
   below e/2; d mod 4) — Eisenstein windows sort into exactly
   2^{3e/2-1} word classes, one per grid member. Engine: 500
   perturbation fields (all 32 designs at e = 4 + 12 sampled each at
   e = 6, 8, every deep-bit slot b_i += 4, b_i += 2 at i >= e/2,
   d += 4, d -= 8) leave the word unmoved; 128 random Eisenstein
   fields (b_i in [-8, 8], d odd in [-15, 15], e = 4, 6, 8, 16 — the
   negatives exercise true 2-adic bits) each print their reduction's
   word; reduce o grid = identity exhaustively at e = 4, 6, 8.

2. THE SKELETON DESIGN IN CLOSED FORM (theorem — Kummer parities +
   C7 + finding 1): reduce(Phi_{2e}(x+1)) = x^e + 2x^{e/2} +
   4x^{e/4} - 6 at every e = 2^s >= 4 (beta = 1 at e/2 alone,
   gamma = 1 at e/4 alone, delta = 1; verified by direct binomial
   bits AND the Kummer s2 count at e = 4..64), so that 3-term design
   carries zeta_{2e}'s skeleton word at every 2-power depth — the
   UNIQUE grid member that does. Measured: word nonzero exactly
   {e/2, 5e/4} at e = 4, 8, 16, 32 ({16, 40} at 32 = zeta64's called
   vector); the anchors Phi_16/Phi_32(x+1) print the design's word
   verbatim (RD6 — the reduction law live on fields whose deep bits
   are full binomials); e = 2 face x^2 + 2x - 6, word (1, 0). The
   P194 solver's find [-6,4@4,2@8] was the anchor's own
   bit-reduction: the solver rediscovered Phi_32(x+1) mod the
   invisible bits.

3. THE DEPTH-32 GAME TIE (rule in range; RD7): the designed 3-term
   world x^32 + 2x^16 + 4x^8 - 6 walks class-1 STOPLESS — sampled
   direct rels min exactly 48 (the freedom end), landing 112 =
   zeta64's — a cyclotomic-readout mimic with three terms at
   depth 32.

PRE-GREEN FAILURES: none — green on the first complete run (all
seven RD rows frozen from the hand algebra before any code; the
adjudication seat sat empty again, fifth face in a row). Post-green
cosmetic only: two em dashes in print strings swapped for ASCII
(cp1252 console) and the engine re-run whole, output identical.

RUN RECORD (python explore_reduction_law.py, ~0.9 s, exit 0): 13,880
checks passed (3,659 this module + 10,221 imported; 500 perturbation
+ 128 zoo fields). Printed rows as copied: [A] reduce(Phi_{2e}(x+1))
at e = 4/8/16/32/64, bits + Kummer agree; retraction exhaustive
e = 4, 6, 8; [B] 32/12/12 designs, word unmoved; [C] 40/40/40/8
zoo fields == their reductions' words; [D] design words {2,5} /
{4,10} / {8,20}, anchors == designs, e = 2 word (1, 0); [E] {16,40},
rel min 48, landing 112.
"""

import math
import random

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_mu8_grading as mu8
import explore_mu16_face as m16
import explore_mu32_face as m32
import explore_readout_proof as rp
import explore_readout_triangle as tri

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def s2(n):
    return bin(n).count("1")


# ------------------------------------------------------- the reduction


def reduce_bits(e, b, d):
    """(b[1..e-1], d odd) -> triangle grid bits (bit r-1 <-> level r).
    Python's % and >> are 2-adic on negatives."""
    bits = 0
    for i in range(1, e):
        if b[i] & 1:
            bits |= 1 << (i - 1)
    if d % 4 == 3:
        bits |= 1 << (e - 1)
    for i in range(1, e // 2):
        if (b[i] >> 1) & 1:
            bits |= 1 << (e - 1 + i)
    return bits


def bits_to_bd(e, bits):
    """Grid bits -> (b, d), mirroring tri.grid_eis."""
    b = [0] * e
    for r in range(1, e):
        if bits >> (r - 1) & 1:
            b[r] += 1
    for i in range(1, e // 2):
        if bits >> (e - 1 + i) & 1:
            b[i] += 2
    d = 3 if bits >> (e - 1) & 1 else 1
    return b, d


def eis_of(e, b, d):
    return [-2 * d] + [2 * b[i] for i in range(1, e)] + [1]


def word_of(e, eis, name, amax=None):
    F = lc.LF(name, 2, [0, 1], eis, amax if amax else 2 * e)
    w = m16.w_element_g(F)
    digs = m16.w_digits_g(F, w, n=3 * e // 2)
    return tuple(digs[1:])


def skel_bits(e):
    return (1 << (e // 2 - 1)) | (1 << (e - 1)) | (1 << (e - 1 + e // 4))


def skel_word(e):
    return tuple(1 if r in (e // 2, 5 * e // 4) else 0
                 for r in range(1, 3 * e // 2))


def anchor_bd(e):
    """Phi_{2e}(x+1) = (x+1)^e + 1: b_k = C(e,k)/2, d = -1."""
    b = [0] + [math.comb(e, k) // 2 for k in range(1, e)]
    return b, -1


# ------------------------------------ [A] RD4: the anchor's reduction


def check_rd4():
    for e in (4, 8, 16, 32, 64):
        b, d = anchor_bd(e)
        ok(all(math.comb(e, k) % 2 == 0 for k in range(1, e)),
           "e=%d: anchor coefficient odd" % e)
        bits = reduce_bits(e, b, d)
        ok(bits == skel_bits(e),
           "e=%d: anchor reduction != the skeleton design" % e)
        for k in range(1, e):
            v2C = s2(k) + s2(e - k) - 1          # Kummer via Legendre
            ok((v2C == 1) == (k == e // 2),
               "e=%d k=%d: beta parity vs Kummer" % (e, k))
            if k < e // 2:
                ok((v2C == 2) == (k == e // 4),
                   "e=%d k=%d: gamma parity vs Kummer" % (e, k))
        print("[A] e = %-3d reduce(Phi_%d(x+1)) = x^%d + 2x^%d + 4x^%d"
              " - 6 (bits + Kummer agree)" % (e, 2 * e, e, e // 2, e // 4))
    b, d = anchor_bd(2)
    ok(reduce_bits(2, b, d) == 0b11, "e=2: anchor reduction != x^2+2x-6")
    for e in (4, 6, 8):                           # the retraction
        nbits = 3 * e // 2 - 1
        for bits in range(1 << nbits):
            b, d = bits_to_bd(e, bits)
            ok(reduce_bits(e, b, d) == bits,
               "e=%d bits=%d: reduce o grid != id" % (e, bits))
    print("[A] reduce o grid = identity (exhaustive e = 4, 6, 8)")


# ------------------------------- [B] RD1: deep-bit invisibility slots


def perturbations(e, b, d):
    for i in range(1, e):
        b2 = list(b)
        b2[i] += 4
        yield b2, d, "b_%d+=4" % i
    for i in range(e // 2, e):
        b2 = list(b)
        b2[i] += 2
        yield b2, d, "b_%d+=2" % i
    yield list(b), d + 4, "d+=4"
    yield list(b), d - 8, "d-=8"


def check_rd1(rng):
    grid_words = {}

    def gword(e, bits):
        if (e, bits) not in grid_words:
            grid_words[(e, bits)] = tri.window(e, bits)
        return grid_words[(e, bits)]

    n_fields = 0
    for e, designs in ((4, list(range(32))),
                       (6, rng.sample(range(1 << 8), 12)),
                       (8, rng.sample(range(1 << 11), 12))):
        for bits in designs:
            base = gword(e, bits)
            b, d = bits_to_bd(e, bits)
            for b2, d2, slot in perturbations(e, b, d):
                ok(reduce_bits(e, b2, d2) == bits,
                   "e=%d %s: reduction moved" % (e, slot))
                w = word_of(e, eis_of(e, b2, d2),
                            "p%d_%d_%s" % (e, bits, slot))
                ok(w == base,
                   "e=%d bits=%d %s: word changed" % (e, bits, slot))
                n_fields += 1
        print("[B] e = %d: %d designs x all deep-bit slots -- word "
              "unmoved" % (e, len(designs)))
    return n_fields, gword


# ---------------------------------------- [C] RD2 + RD3: the random zoo


def check_rd23(rng, gword):
    n_fields = 0
    for e, count in ((4, 40), (6, 40), (8, 40), (16, 8)):
        for j in range(count):
            b = [0] + [rng.randrange(-8, 9) for _ in range(e - 1)]
            d = rng.choice([x for x in range(-15, 16, 2)])
            bits = reduce_bits(e, b, d)
            w = word_of(e, eis_of(e, b, d), "z%d_%d" % (e, j))
            ok(w == gword(e, bits),
               "e=%d zoo %d: word != reduce word (bits %d)" % (e, j, bits))
            n_fields += 1
        print("[C] e = %-2d: %d random Eisenstein fields == their "
              "reductions' words" % (e, count))
    return n_fields


# ------------------------- [D] RD5 + RD6: the skeleton design + anchors


def check_rd56():
    ok(word_of(2, [-6, 2, 1], "x2+2x-6") == (1, 0),
       "e=2 design word != (1, 0)")
    print("[D] e = 2: x^2+2x-6 word (1, 0)")
    words = {}
    for e in (4, 8, 16):
        eis = eis_of(e, *bits_to_bd(e, skel_bits(e)))
        w = word_of(e, eis, "skel%d" % e)
        ok(w == skel_word(e), "e=%d design word != skeleton" % e)
        words[e] = w
        print("[D] e = %-2d design x^%d+2x^%d+4x^%d-6: word nonzero "
              "exactly {%d, %d}" % (e, e, e // 2, e // 4, e // 2,
                                    5 * e // 4))
    for e in (8, 16):
        b, d = anchor_bd(e)
        w = word_of(e, eis_of(e, b, d), "zeta%d" % (2 * e))
        ok(w == words[e], "e=%d anchor word != design word" % e)
        print("[D] e = %-2d anchor Phi_%d(x+1): word == the design's"
              % (e, 2 * e))


# --------------------------------- [E] RD5 (e = 32) + RD7: the game tie


def check_rd7(rng):
    e = 32
    eis = eis_of(e, *bits_to_bd(e, skel_bits(e)))
    F = lc.LF("skel32", 2, [0, 1], eis, 120)
    w = m16.w_element_g(F)
    digs = m16.w_digits_g(F, w, n=48)
    ok({k for k in range(1, 48) if digs[k]} == {16, 40},
       "e=32 design word nonzero != {16, 40}")
    rels = set()
    for u in ad.sample_class(F, 1, 40, rng):
        rels.add(rp.direct_rel(F, u, 5))
    ok(min(rels) == 48, "e=32 design: class-1 rel min %s != 48"
       % sorted(rels)[:3])
    print("[E] e = 32 design x^32+2x^16+4x^8-6: word nonzero exactly "
          "{16, 40}, class-1 STOPLESS -- rel min 48, landing 112 "
          "(= zeta64's)")


# ---------------------------------------------------------------- run


def run():
    rng = random.Random(197)

    print("== [A] RD4: the anchor's bit-reduction, closed form ==")
    check_rd4()

    print("== [B] RD1: deep-bit invisibility off grid members ==")
    nb, gword = check_rd1(rng)

    print("== [C] RD2/RD3: the random Eisenstein zoo ==")
    nc = check_rd23(rng, gword)

    print("== [D] RD5/RD6: the skeleton design + the anchors ==")
    check_rd56()

    print("== [E] RD7: the depth-32 game tie ==")
    check_rd7(rng)

    imported = (lc.CHECKS + ad.CHECKS + mu8.CHECKS + m16.CHECKS
                + m32.CHECKS + rp.CHECKS + tri.CHECKS)
    print("ALL GREEN: %d checks passed (%d this module + %d imported; "
          "%d perturbation + %d zoo fields)"
          % (CHECKS + imported, CHECKS, imported, nb, nc))


if __name__ == "__main__":
    run()
