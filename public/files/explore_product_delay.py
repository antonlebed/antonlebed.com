"""The two-stream delay: the least lookahead at which the PRODUCT of
two signed-digit streams is readable, as a criterion in the radix and
the digit set — the delay the field states per algorithm, read here
as a reading game with a lower-bound certificate.

THE QUESTION. A most-significant-first reader of two digit streams
X = 0.x1 x2 ... and Y = 0.y1 y2 ... over radix b and a contiguous
digit set D = {-am..ap} emits the digits of P = X * Y in the same
system. It reads at LOOKAHEAD c when its (t+1)-th output digit is
emitted after the (t+1+c)-th digits of both inputs, and the emitted
prefix is VALID when the true product lies in the prefix's cell,
[P_t - M- b^-t, P_t + M+ b^-t] with M- = am/(b-1), M+ = ap/(b-1),
for every continuation of both inputs. Every arithmetic map the
window prices today has ONE stream and a constant beside it (the
rational-slope criterion) or is the SUM of two streams (the lookahead
criterion); the product of two streams, on-line arithmetic's own
object, is priced by the field per algorithm: the on-line delay of a
multiplier is derived from a range analysis of that multiplier's
residual, and the one general treatment read full-text (Frougny,
Pavelka, Pelantova, Svobodova, DMTCS 2019, Corollary 2.2 restating
Trivedi and Ercegovac 1977) proves an UPPER bound only — for integer
b > 1 and D = {-a..a} with b/2 <= a <= b-1 the rounding multiplier
works at the least delta with

    b/2 + 2 a^2 / (b^delta (b-1)) <= a + 1/2,

and the paper states in so many words that it does not touch the
optimality of delta. Equivalently, with the slack rho = 2a + 1 - b,

    b^delta (b-1) rho >= 4 a^2                              (TE)

— the ADDITION heuristic b^c rho >= 2W of the Lebesgue margin
(explore_margin_wedge.py) times the largest magnitude M = a/(b-1):
the product's interval width is the sum's width scaled by the
operands' size. The question: is (TE) the FLOOR — does every reader,
not one algorithm, need that delay — and what is the floor off the
symmetric diagonal?

THE GAME. The exact law is a safety game, as for the sum. State: the
output prefix q = b^t P_t and the input prefixes u = b^(t+c) X_(t+c),
v = b^(t+c) Y_(t+c), all integers. A round: the adversary appends one
digit to each input, then the reader emits one output digit; the
emission is legal iff the product of the two input boxes — an
interval, its ends at the box's corners since the product is
bilinear — lies inside the new output cell. Scaled by (b-1)^2
b^(2(t+c)) every comparison is between integers. The adversary also
chooses the first c digits of each stream before the first emission
(at c = 0 the reader emits blind). The reader READS at lookahead c
iff it survives every adversary forever; a FINITE adversary tree in
which every legal emission is answered by a losing continuation is a
CERTIFICATE that c fails, so the search to depth T proves lower
bounds and never upper bounds. Upper bounds are readers: (TE) is one
for every symmetric cell it covers, and the CENTRED reader — emit
the digit whose cell centre is nearest the image's centre — is run
inside the same engine as the transplant of the rounding select.

THE ONE-STREAM SPECIALISATION is a lower bound for free: a two-stream
reader whose Y-stream is fixed to a constant's digits is a reader of
scaling by that constant at the same lookahead, so the product's
floor is at least the worst constant slope's (the rational-slope
criterion, explore_slope_proof.py). The engine runs it as an adversary who
plays Y = the corner stream (every digit a, the largest magnitude)
and varies X alone.

SCOPE. Contiguous D with am, ap <= b-1 (M-, M+ <= 1), cells where the
product of two window values is again a window value, i.e. the
corner products [-M+ M-, max(M-^2, M+^2)] lie in [-M-, M+]: a map
whose image leaves the window is unreadable at any lookahead, a range
matter and not a delay. Radices 2..6, every such D, lookahead 0..4,
search depth T rounds.

THE SLATE, frozen before the engine.

P-A THE CONTROL. The same engine run on the SUM reproduces the
    lookahead criterion at every census cell: c_min = 1 iff
    rho >= ceil(am/(b-1)) + ceil(ap/(b-1)), else 2; c = 0 certified
    failing everywhere. Read before any product line.
P-B THE READER CONTROL. The centred reader survives to depth T at
    c = delta_TE on every symmetric cell (TE) covers.
P-C THE FLOOR IS (TE) — a TRANSPLANT from the sum, where the exact
    law sits within one digit of the Lebesgue heuristic and the
    field's algorithm reaches it: at every symmetric cell the
    adversary certifies c = delta_TE - 1 failing, at a certificate
    depth of at most 3 rounds, so c_min = delta_TE exactly there.
P-D THE SECOND STREAM COSTS A DIGIT. The corner-stream adversary
    (one stream varying) certifies failure only below delta_TE - 1
    at (2, {-1,0,1}): the worst constant slope reads at 1 or less
    (its Lebesgue count is at most 1 for slopes of magnitude at
    most 1) while two streams need 2. The floor is set by the
    second stream's uncertainty, not by the product's size.
P-E OFF THE DIAGONAL, a TRANSPLANT of (TE)'s own algebra: with
    ah = max(am, ap) the largest digit and the rounding invariant
    [-(am + 1/2), ap + 1/2], the rounding reader needs
    b^c (b-1) (2 min(am, ap) - b + 1) >= 4 ah^2, a bound that goes
    EMPTY (no delay suffices) when 2 min(am, ap) < b - 1. Prediction:
    the exact floor at asymmetric cells is at most that reader's
    delay and is FINITE where the reader's bound is empty, the
    finite value read off the certificates.

KILLS, frozen as what this rig PRINTS.

K1 A sum cell prints a c_min differing from the lookahead criterion
   -> the engine's convention is not the corpus's; nothing
   downstream is read.
K2 The centred reader dies at c = delta_TE on a symmetric cell ->
   the engine's legality test is wrong (the rounding reader is a
   proof at that delay) or the transplant of the select is not the
   field's; a harness fault, chased before any floor line is read.
K3 A symmetric cell prints "survives to depth T" at
   c = delta_TE - 1 -> the floor is below (TE) or T is shallow; the
   cell is rerun at depth T + 3, and a survival there is the finding
   that (TE) is not the floor, P-C dead at that cell.
K4 A cell prints a certificate at c = delta_TE (adversary wins where
   a reader is proved) -> engine fault, same as K2.
K5 The corner-stream adversary certifies delta_TE - 1 failing at
   (2, {-1,0,1}) -> P-D dead: the floor is already the worst slope's
   and the second stream is free.

POSITIVE CONTROLS, run and read before any verdict line: P-A and
P-B whole.

TWO CORRECTIONS MADE AT THE CONTROL, before any product line was
read. (i) The corpus's addition game realises lookahead c as an
output that LEADS the input by c positions (the flush window: the
j-th emission has weight b^(c-j), made after the j-th input digit),
while the field's on-line delay keeps the output aligned and delays
it; the engine gained an output offset o, the sum control runs at
(delay 0, o = c) and the product at (delay c, o = 0), and the column
"flush c*" runs the product in the corpus's convention as well. (ii)
The one-stream specialisation as first coded fixed Y's DIGITS while
the reader still priced Y's whole box — a restricted adversary, not
a reader that knows the constant; the "scale" kind collapses Y to
the exact constant, which is the rational-slope game.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. The sum through this engine reproduces the
   lookahead criterion at 20/20 census cells (radices 2..5), c = 0
   certified failing at every one. P-A held; K1 never fired.

F2 THE FIELD'S DELAY IS THE FLOOR ON THE DIAGONAL [criterion at each
   cell, rule across the six]. At every symmetric representable
   cell — (2,1,1), (3,2,2), (4,2,2), (4,3,3), (5,3,3), (5,4,4) — the
   exact game's floor c* equals delta_TE (6/6), the adversary
   certifying c = delta_TE - 1 in at most 2 rounds, and the centred
   reader survives at delta_TE (6/6). P-B and P-C held; K2, K3, K4
   never fired.

F3 THE SECOND STREAM COSTS THE DIGIT. At (2,{-1,0,1}) the worst of
   thirteen constant slopes of magnitude at most 1 reads at c = 1
   (7/8 the worst) while two streams need 2; at every cell the
   worst slope reads one below the product's floor except where the
   floor is already 1. P-D held; K5 never fired.

F4 THE TOLERANCE LAW, off the diagonal too [sufficiency a THEOREM
   for every radix and every contiguous D with rho >= 1 on the
   representable cells, by the invariant derived below; necessity a rule at the 13 cells]. The exact floor is the
   least c with

       b^c (b-1) rho >= 2 max(am, ap) (am + ap),

   at 13/13 cells, and the GREEDY reader — any legal digit, no
   backtracking — survives at that c at every cell. On the diagonal
   the right side is 4a^2 and the law is Trivedi-Ercegovac's
   Corollary 2.2, whose hypothesis b/2 <= a is rho >= 1 itself; off
   the diagonal it is new. The rounding
   transplant of P-E is EMPTY at five of the seven asymmetric cells
   and overpays by one at (5,3,4) (2 against the floor 1); the exact
   floor is finite everywhere. P-E's first half held, its formula
   retired.
   The sufficiency argument: with Mh = max(M-, M+) the window's
   largest magnitude, the product of two boxes at input length n is
   an interval of half-width at most h b^-t, h = Mh (M- + M+) b^-c;
   writing it as P_(t-1) + (w +- h') b^-t, a digit p is legal iff
   w lies in [p - M- + h', p + M+ - h'], an interval of length at
   least (M- + M+) - 2h; when that is >= 1 consecutive digits'
   intervals overlap and their union is exactly the range w can
   occupy inside the parent cell, so every legal choice keeps the
   invariant; (M- + M+) - 2h >= 1 is the law.

F5 THE LAW IS THE READING LEMMA'S MARGIN, EXACT. The same inequality
   is the Lebesgue condition "image width at most the level-t
   cover's Lebesgue number (M- + M+ - 1) b^-t": for the product the
   heuristic that overpays by one digit on the sum's wedge
   (explore_margin_wedge.py) is the exact law at every cell scanned.
   The flush-offset convention gives the same floor at 13/13 cells.

VERDICT. The two-stream delay is a criterion in (b, D) at the
scanned cells and a proved upper bound everywhere: readable at c iff
b^c (b-1) rho >= 2 max(am, ap)(am + ap), the "iff" resting on finite
certificates at radices 2..5 and the "if" on the invariant. What
remains open is the necessity side in general — that the adversary
can always steer the residual into a gap between the digits'
tolerance intervals while holding both streams at the corner — and
the census beyond radix 5.

RUN RECORD: pure Python, integers only, standard library; under
memwatch, peak commit 7.2 MB against the 512 MB default; wall
317 s for radices 2..5 (the survival searches are budgeted to about
two million nodes each and are toy-scale evidence; the certificates
are proofs). Prints reproduced by:
python prime/code/explore_product_delay.py 5
"""

import sys
import time

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def ceil_div(x, y):
    return -(-x // y)


# ---------------------------------------------------------------- game

class Game:
    """The two-stream reading game at lookahead c for one map.

    Scales: an input prefix u of length n = t + c stands for the box
    (u - M-, u + M+) * b^-n; times (b-1) b^n the box is the integer
    interval [(b-1)u - am, (b-1)u + ap]. The image of two boxes under
    the map, at scale (b-1)^2 b^(2n) for the product and (b-1) b^n
    for the sum, is compared with the output cell at level t+1,
    [(b-1)q - am, (b-1)q + ap] * b^-(t+1) / (b-1), by cross
    multiplication so every test is on integers.
    """

    def __init__(self, b, am, ap, c, kind, o=0, slope=None):
        self.b, self.am, self.ap, self.c, self.kind = b, am, ap, c, kind
        self.o = o   # output offset: the j-th emission has weight b^(o-j)
        self.D = list(range(-am, ap + 1))
        self.pairs = [(x, y) for x in self.D for y in self.D]
        if kind == "scale":
            # ONE stream: Y is the exact constant yn/yd, known to the
            # reader; the adversary plays X alone (the rational-slope
            # game in this engine's convention).
            self.yn, self.yd = slope
            self.pairs = [(x, 0) for x in self.D]

    def image(self, u, v, n):
        """Integer interval of the map's image over the two boxes at
        input length n, with its scale factor s (image / s is the
        real interval)."""
        b, am, ap = self.b, self.am, self.ap
        x1, x2 = (b - 1) * u - am, (b - 1) * u + ap
        y1, y2 = (b - 1) * v - am, (b - 1) * v + ap
        if self.kind == "sum":
            return x1 + y1, x2 + y2, (b - 1) * b ** n
        if self.kind == "scale":
            e1, e2 = x1 * self.yn, x2 * self.yn
            return min(e1, e2), max(e1, e2), (b - 1) * b ** n * self.yd
        corners = (x1 * y1, x1 * y2, x2 * y1, x2 * y2)
        return min(corners), max(corners), (b - 1) ** 2 * b ** (2 * n)

    def legal(self, u, v, n, q, t):
        """The image at input length n lies inside the level-t cell
        of output prefix q."""
        b, am, ap, o = self.b, self.am, self.ap, self.o
        lo, hi, s = self.image(u, v, n)
        clo, chi = (b - 1) * q - am, (b - 1) * q + ap
        # cell = [clo, chi] b^(o-t) / (b-1);  image = [lo, hi] / s
        cs, bo = (b - 1) * b ** t, b ** o
        return lo * cs >= clo * bo * s and hi * cs <= chi * bo * s

    def legal_digits(self, u, v, n, q, t):
        return [p for p in self.D if self.legal(u, v, n, self.b * q + p, t + 1)]

    def centred_digit(self, u, v, n, q, t):
        """The digit whose cell centre is nearest the image centre,
        among the legal ones; None if none is legal."""
        b, am, ap, o = self.b, self.am, self.ap, self.o
        lo, hi, s = self.image(u, v, n)
        best, bestd = None, None
        for p in self.D:
            q1 = b * q + p
            if not self.legal(u, v, n, q1, t + 1):
                continue
            # cell centre (2(b-1)q1 + ap - am) b^(o-t-1) / (2(b-1));
            # image centre (lo + hi) / (2s); compare by cross terms
            cc = 2 * (b - 1) * q1 + (ap - am)
            d = abs((lo + hi) * (b - 1) * b ** (t + 1) - cc * b ** o * s)
            if bestd is None or d < bestd:
                best, bestd = p, d
        return best

    # -- the search: reader survives `rounds` more rounds from (u,v,q,t)?
    def survives(self, u, v, q, t, rounds, reader=None, adv_pairs=None):
        """True iff the reader survives `rounds` further rounds against
        every adversary continuation (adv_pairs restricts the
        adversary's digit pairs; reader=None means the reader may pick
        any legal digit — the exact game; reader='centred' fixes the
        strategy)."""
        if rounds == 0:
            return True
        pairs = adv_pairs if adv_pairs is not None else self.pairs
        n = t + self.c
        for (x, y) in pairs:
            u1, v1 = self.b * u + x, self.b * v + y
            if reader in ("centred", "greedy"):
                p = (self.centred_digit(u1, v1, n + 1, q, t) if reader == "centred"
                     else next(iter(self.legal_digits(u1, v1, n + 1, q, t)), None))
                if p is None:
                    return False
                if not self.survives(u1, v1, self.b * q + p, t + 1, rounds - 1,
                                     reader, adv_pairs):
                    return False
            else:
                alive = False
                for p in self.legal_digits(u1, v1, n + 1, q, t):
                    if self.survives(u1, v1, self.b * q + p, t + 1, rounds - 1,
                                     reader, adv_pairs):
                        alive = True
                        break
                if not alive:
                    return False
        return True

    def opening_states(self, adv_pairs=None):
        """All (u, v) after the adversary's first c digits of each."""
        pairs = adv_pairs if adv_pairs is not None else self.pairs
        states = [(0, 0)]
        for _ in range(self.c):
            states = [(self.b * u + x, self.b * v + y)
                      for (u, v) in states for (x, y) in pairs]
        return states

    def reader_survives(self, rounds, reader=None, adv_pairs=None):
        """The whole game from the empty prefix: root legality, then
        `rounds` rounds."""
        for (u, v) in self.opening_states(adv_pairs):
            if not self.legal(u, v, self.c, 0, 0):
                return False
            if not self.survives(u, v, 0, 0, rounds, reader, adv_pairs):
                return False
        return True

    def certificate_depth(self, max_rounds, reader=None, adv_pairs=None,
                          budget=2_000_000):
        """Least number of rounds at which the adversary wins, or None
        if the reader survives `depth` rounds, where depth is the
        largest r <= max_rounds keeping pairs^(c + r) within the node
        budget (a survival is toy-scale evidence, never a proof; a
        certificate is a proof). Returns (r or None, depth searched)."""
        import math
        pairs = adv_pairs if adv_pairs is not None else self.pairs
        k = len(pairs)
        depth = max(1, min(max_rounds,
                           int(math.log(budget) / math.log(k)) - self.c))
        for r in range(0, depth + 1):
            if not self.reader_survives(r, reader, adv_pairs):
                return r, depth
        return None, depth


# ----------------------------------------------------------- closed forms

def delta_te(b, a):
    """Least delta with b^delta (b-1)(2a+1-b) >= 4a^2; None if empty."""
    rho = 2 * a + 1 - b
    if rho <= 0:
        return None
    d = 0
    while b ** d * (b - 1) * rho < 4 * a * a:
        d += 1
    return d


def delta_te_asym(b, am, ap):
    """The rounding reader's transplant off the diagonal:
    b^c (b-1)(2 min - b + 1) >= 4 max^2; None if empty."""
    ah, al = max(am, ap), min(am, ap)
    m = 2 * al - b + 1
    if m <= 0:
        return None
    d = 0
    while b ** d * (b - 1) * m < 4 * ah * ah:
        d += 1
    return d


def delta_law(b, am, ap):
    """The tolerance law: least c with b^c (b-1) rho >= 2 ah W, where
    ah = max(am, ap), W = am + ap, rho = W + 1 - b — the width of the
    product image at the window's largest corner against the slack,
    the digits' legal intervals then tiling every residual."""
    rho, ah, W = am + ap + 1 - b, max(am, ap), am + ap
    d = 0
    while b ** d * (b - 1) * rho < 2 * ah * W:
        d += 1
    return d


def sum_law(b, am, ap):
    rho = am + ap + 1 - b
    sig = ceil_div(am, b - 1) + ceil_div(ap, b - 1)
    return 1 if rho >= sig else 2


def representable(b, am, ap):
    """Corner products of the window lie in the window (M- = am/(b-1),
    M+ = ap/(b-1), both <= 1 by the census bound): the negative corner
    -M+ M- >= -M- iff M+ <= 1 (given), the positive corner
    max(M-^2, M+^2) <= M+ iff am^2 <= ap (b-1)."""
    return am * am <= ap * (b - 1)


def census(bmax):
    cells = []
    for b in range(2, bmax + 1):
        for am in range(0, b):
            for ap in range(0, b):
                rho = am + ap + 1 - b
                if rho < 1:
                    continue
                cells.append((b, am, ap))
    return cells


SLOPES = [(1, 1), (7, 8), (5, 6), (4, 5), (3, 4), (2, 3), (5, 8), (3, 5),
          (1, 2), (2, 5), (1, 3), (1, 4), (1, 5)]


# ------------------------------------------------------------------ main

def main():
    T = 6          # certificate search depth in rounds (survival depth is budgeted)
    CMAX = 4
    BMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    t0 = time.time()

    print("=== P-A: the SUM through this engine against the lookahead criterion")
    cells = census(BMAX)
    agree = 0
    for (b, am, ap) in cells:
        law = sum_law(b, am, ap)
        g0 = Game(b, am, ap, 0, "sum", o=0)
        d0, _ = g0.certificate_depth(T)
        ok(d0 is not None, f"sum c=0 survives at ({b},{am},{ap})")
        cmin = None
        for c in range(1, 3):
            g = Game(b, am, ap, 0, "sum", o=c)   # the corpus's convention
            if g.certificate_depth(T)[0] is None:
                cmin = c
                break
        if cmin == law:
            agree += 1
        else:
            ok(False, f"sum ({b},{am},{ap}): engine c_min={cmin} law={law}")
    print(f"  sum cells {len(cells)}: engine agrees with the criterion at "
          f"{agree}/{len(cells)}; c=0 certified failing at every cell: "
          f"{'yes' if not FAILURES else 'NO'}   [{time.time()-t0:.1f}s]")

    print("\n=== PRODUCT census: b <= %d, contiguous D with am, ap <= b-1, "
          "representable cells" % BMAX)
    print("  cell (b,am,ap) rho | dTE dTE-asym | c* [cert depth at c*-1, "
          "survival depth] | centred@dTE centred@c* | tolerance law, greedy "
          "reader at it | worst one-stream "
          "slope's c | c* at the flush offset o=c")
    sym_exact = sym_total = 0
    law_agree = law_total = 0
    cent_ok = cent_total = 0
    asym_rows = []
    for (b, am, ap) in cells:
        if not representable(b, am, ap):
            continue
        rho = am + ap + 1 - b
        dte = delta_te(b, am) if am == ap else None
        dta = delta_te_asym(b, am, ap)
        # exact floor search: least c surviving depth T
        cstar, certs, sdepth = None, {}, None
        for c in range(0, CMAX + 1):
            g = Game(b, am, ap, c, "product")
            d, sdepth = g.certificate_depth(T)
            if d is None:
                cstar = c
                break
            certs[c] = d
        # centred reader at dTE (or at cstar when off-diagonal)
        cent = None
        if dte is not None:
            cent = Game(b, am, ap, dte, "product").certificate_depth(
                T, "centred")[0] is None
            cent_total += 1
            cent_ok += 1 if cent else 0
            ok(cent, f"K2 centred reader dies at dTE={dte} on ({b},{am},{ap})")
            if cstar is not None:
                ok(cstar <= dte, f"K4 certificate at dTE on ({b},{am},{ap})")
                sym_total += 1
                if cstar == dte:
                    sym_exact += 1
                else:
                    print(f"  K3 candidate: ({b},{am},{ap}) c*={cstar} < dTE={dte}")
        # the one-stream specialisation: the worst constant slope among
        # a small set of magnitudes at most M+ (the reader KNOWS the
        # constant), each a lower bound on the two-stream floor
        cc, worst = 0, None
        for (yn, yd) in SLOPES:
            if yn * (b - 1) > ap * yd:      # slope above the window's top
                continue
            for c in range(0, CMAX + 1):
                if Game(b, am, ap, c, "scale", slope=(yn, yd)).certificate_depth(
                        T)[0] is None:
                    if c > cc:
                        cc, worst = c, (yn, yd)
                    break
        # the centred reader at the exact floor (a witness reader), and
        # the GREEDY reader (first legal digit, no backtracking) at the
        # tolerance law's delay, the strategy the sufficiency proof uses
        centc = None
        if cstar is not None:
            centc = Game(b, am, ap, cstar, "product").certificate_depth(
                T, "centred")[0] is None
        dlaw = delta_law(b, am, ap)
        greedy = Game(b, am, ap, dlaw, "product").certificate_depth(
            T, "greedy")[0] is None
        ok(greedy, f"greedy reader dies at the law's c={dlaw} on ({b},{am},{ap})")
        law_total += 1
        law_agree += 1 if cstar == dlaw else 0
        # the corpus's flush convention (output leading by c) for the STITCH
        cflush = None
        for c in range(0, CMAX + 1):
            g = Game(b, am, ap, 0, "product", o=c)
            if g.certificate_depth(T)[0] is None:
                cflush = c
                break
        prev = certs.get((cstar or 0) - 1)
        print(f"  ({b},{am},{ap}) rho={rho} | dTE={dte} asym={dta} | "
              f"c*={cstar} [cert {prev}, survived {sdepth}] | centred={cent} "
              f"centred@c*={centc} | law={dlaw} greedy@law={greedy} "
              f"| worst slope c={cc} at {worst} "
              f"| flush c*={cflush}"
              f"   [{time.time()-t0:.0f}s]")
        if am != ap:
            asym_rows.append((b, am, ap, dta, dlaw, cstar))

    print(f"\n  symmetric cells with a proved floor (c* = dTE): "
          f"{sym_exact}/{sym_total}; centred reader alive at dTE: "
          f"{cent_ok}/{cent_total}")
    print(f"  tolerance law b^c (b-1) rho >= 2 max(am,ap) (am+ap) equals c* at "
          f"{law_agree}/{law_total} cells; greedy reader alive at the law: "
          f"{'all' if not any('greedy' in f for f in FAILURES) else 'NOT all'}")
    print("  asymmetric cells (b,am,ap, rounding-transplant delay, tolerance "
          "law, exact c*):")
    for row in asym_rows:
        print("   ", row)

    print(f"\nwall {time.time()-t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    sys.exit(main())
