"""rider.py -- the lid when every move must be principal: what a greedy
walk over a number ring pays once it has locked, when each move buys a
core together with the minimal rider that makes it an element.

QUESTION. lid.py proves, for walks whose moves are ideals, that a block
whose last mover sits one tail gap below the next count and whose count
has outgrown the mover's tail price stays so forever, every later
price at most the lid, N^e of its last mover (N the norm, e the
ramification index); and that four statements about a walk are one:
it reaches such a state, some block is clocked infinitely often, it
makes finitely many openings, its prices are bounded infinitely often.
That proof reads places one at a time. In the ELEMENT world a move is a
principal ideal, and its least form is a CORE Q^r at Q's door r together
with a RIDER, a least ideal of the class -r c_Q (element_ring.py): one
move deepens several places, some possibly over the core's own prime.
Does the lid carry, with what price in place of N^e, and does the
four-way equivalence carry with it?

THE OBJECTS. A place Y over p has residue field of N = p^f elements,
ramification e, ladder x_1 = 1 < x_2 < ..., column c(b) = #{j : x_j <
b}, m_Y(j) = x_j + 1, gap G_Y(j) = m_Y(j + 1) - m_Y(j), tail index t_Y
(door.py). Its class in the class group is c_Y. mu(x) is the least norm
of an integral ideal of class x, mu(0) = 1, and a LEAST IDEAL of class x
is one attaining it. The PRICE of Y at door k is
    pi_Y(k) = N^k * mu(-k c_Y),
and Y's TAIL PRICE is Lambda_Y = pi_Y(e_Y). A block is the set of
places over p; its count is V = v_p(L). A HOLDER of the block is a
seated place over p at column exactly V. A CREEPER over p is a place Y
over p that some least ideal contains with multiplicity strictly
between 0 and e_Y: a rider can move it less than one column.

THE ARGUMENT (written before the engine).
  (0) THE BARE DOOR BOUND (element_ring.py (3)), read for every place of
      a vehicle and not only its core: a principal J with v_Y(J) = k
      has N(J) >= pi_Y(k), since J Y^(-k) is integral of class -k c_Y;
      and pi_Y is nondecreasing, since a least ideal of class -(k+j) c_Y
      times Y^j is an integral ideal of class -k c_Y. The least moves at
      a state are the cores at their doors times least ideals, so the
      menu's price is min over Y of pi_Y(door_Y).
  (1) A HOLDER PENDS AT MOST ITS TAIL PRICE. At column V its depth
      a satisfies m(V) <= a < m(V + 1), so its door m(V + 1) - a is at
      most G(V), which is e once V >= t_Y; by (0) the move costs at most
      Lambda_Y, and greed pays no more than any move on its menu.
  (2) THE ELEMENT LID. Call the block over p LIDDED when it has a holder,
      V >= t_Y for every place Y over p, and p^(V+1) >= B, where
          B = max(Lambda over the holders, Lambda over the creepers
              over p).
      Its LID is the largest Lambda over its holders. Then:
      (a) No jump is affordable. Raising V without deepening a place
          over p needs a newly seated place Q (core or rider) with
          p^(V+1) | N(Q) - 1, and any vehicle holding Q costs at least
          N(Q) > p^(V+1) >= B, while a holder pends at most B by (1).
          Deepening a seated place over another prime adds no p-part.
      (b) Every new holder was a holder, is a creeper, or has Lambda at
          most the price that made it. Let a move deepen Y by k and
          leave it in the top column. If k >= e_Y, (0) applied to Y
          inside the vehicle gives Lambda_Y <= pi_Y(k) <= the price paid
          <= the lid. If k < e_Y and Y is the core, it moved at its
          door, so it crossed the count from column V: it was a holder.
          If k < e_Y and Y rides, Y is a creeper. So a holder's Lambda
          never exceeds B, the lid never exceeds B, and with no creeper
          over p the lid never rises; V only grows, keeping p^(V+1) >= B
          and the tails.
      THE ELEMENT LID THEOREM: a lidded block stays lidded, and every
      price the walk pays afterwards is at most its lid at that moment,
      which is at most B. With no creeper over p the lid never rises.
  (3) THE QUADRATIC CASE. Over an imaginary quadratic field the places
      over one prime share Lambda: a split pair is conjugate with
      inverse classes and mu(x) = mu(-x); an inert or ramified prime has
      one place. So each block has ONE tail price and its lid is
      constant once lidded:
          split p:    p * mu(c_P), p when P is principal;
          ramified p: p^2 (2 c_P = 0);
          inert p:    p^2.
      The ramified place is a creeper (a least ideal holds it at most
      once, P^2 = (p) being principal), but it is alone in its block, so
      B is its own Lambda. The ideal lid is the principal case; the
      element lid differs from it exactly at the split non-principal
      places, by the factor mu(c_P) = the leading coefficient of the
      class's reduced form.
  (4) THE LOCK. The four statements stay one. Lidded implies every
      later price at most B; each opening costs at least the norm of
      the place it seats as core, and only finitely many places are
      riders, so finitely many openings follow. Prices bounded
      infinitely often bring cores of bounded norm, each opened once,
      so some seated core crosses its door infinitely often and some
      block's count rises by deepening infinitely often; the count then
      passes every tail and the finitely many Lambda over p, and at the
      state after such a rise the crosser is a holder, so the block is
      lidded. Finitely many openings leave finitely many seated places,
      one of which is a core infinitely often. What is NOT carried: that
      the walk then repeats ONE vehicle forever. The ideal proof of one
      runaway reads single places; here a rider can lag its block by a
      growing number of columns and still move, and whether that can
      keep the vehicle sequence from settling is left open.

THE CLASS GROUP. Gauss's reduced forms of discriminant D (known): a
place over a split or ramified p is the form (p, b, (b^2 - D)/(4p)) with
b^2 = D mod 4p, its conjugate negating b; an inert place is principal;
composition is Dirichlet's (Cohen, A Course in Computational Algebraic
Number Theory, algorithm 5.4.7), then reduction. mu(x) is the leading
coefficient of the reduced form of x (known: the least value a reduced
form properly represents), and it is re-derived here as a shortest path
over the places' classes in (min, x) and by brute enumeration.

PREDICTIONS, frozen before the engine, each naming what the run PRINTS.
  PE0 CONTROL (read first; KILL of the engine). (a) Per field: the
      composition of reduced forms is closed, has the principal form as
      identity and (a, -b, c) as inverse, is associative over every
      triple, and has h elements; every split place times its conjugate
      is principal. (b) mu by the (min, x) path equals the leading
      coefficient and the brute minimum over every ideal of norm up to
      max mu. (c) At Q(sqrt -5) and Q(sqrt -23) the void's tree holds
      the paths 4, 4, 9, 6, 4, ... and 6, 6, 6, 4, ... (element_ring.py
      and its predecessor). (d) At every field of class number 1 the
      element tree's set of price sequences equals the ideal tree's
      (race.py).
  PE1 THE ELEMENT LID. Over every imaginary quadratic field Q(sqrt m),
      -200 <= m <= -1 squarefree, the void walked 40 moves with every tie
      branched and equal states merged, at every state of every end:
      a lidded block stays lidded, its lid never rises, every price paid
      after a lidded state is at most that state's lid (the least over
      its lidded blocks), no jump lands on a lidded block, and every
      holder pends at most its Lambda. Printed: fields, ends, states,
      lidded ends and each violation count. KILL: any count above 0.
  PE2 THE RIDER IS LOAD-BEARING (a measurement, no kill). The prices
      after a lidded state that exceed the IDEAL lid of their state
      (the least, over its lidded blocks, of the largest N^e among a
      block's holders), the element lid being larger. Predicted: some, all at
      fields where a split place of a lidded block is non-principal.
  PE3 THE REACH (a measurement, no kill). Every end lidded within 40
      moves. Printed: the first lidded move's distribution.
  PE4 THE LOCK AND ITS RIDER'S PRIME (a measurement, no kill; a
      question element_ring.py leaves open, its locks each lying over
      one prime by observation). Every end's last 10 moves repeat one
      vehicle. Printed: the ends that do not, and the lock vehicles
      whose support lies over two primes. Predicted from the void:
      none over two primes, since the block over 2 has Lambda at most 4
      (split: 2 * mu(c) = 4 or 2; inert or ramified: 4) and a vehicle
      over two primes costs at least 6. From the principal seeds of norm
      at most 40, walked on one path each, printed without prediction.

TRANSPLANTS, marked. From the ideal world: lid.py's whole argument,
which (2) re-derives with (0) in place of the single-place door. From
element_ring.py: the bare door and the menu as cores times riders,
proved there and re-used here for every place of a vehicle.

FINDINGS (entered after the run, from its output).
  F1 THE CONTROLS (PE0 hit, read first). 122 fields, class numbers 1 to
     20 (9 fields of h = 1, 27 of h = 4, 21 of h = 8, one of h = 20);
     every group closed, associative, with identity and inverses, every
     split pair principal, mu equal to the leading coefficient and the
     brute minimum at every class. The void's trees at Q(sqrt -5) and
     Q(sqrt -23) hold 4, 4, 9, 6, 4, ... and 6, 6, 6, 4, .... At the 9
     fields of class number 1, 150 states, the element menu equals the
     ideal menu at every one.
  F2 THE ELEMENT LID (PE1 hit). 207 ends, 8487 states, 7762 prices paid
     after a lidded state: no lid lost, risen or over B, no price over
     the lid, no jump on a lidded block, no holder over its Lambda. The
     1206 principal seeds of norm at most 40, one path each, the same:
     0 violations.
  F3 THE RIDER IS LOAD-BEARING (PE2 as predicted). 3567 prices exceed
     the ideal lid N^e of their state, at 13 fields: -5, -15, -23, -31,
     -39, -47, -71, -95, -111, -119, -143, -167, -191. By (3) the two
     lids differ only at a split non-principal place, so these are the
     fields where such a block is lidded before a cheaper one; at
     Q(sqrt -5) the split place over 3 lids at 3 * mu(c) = 6.
  F4 THE REACH (PE3). Every end lidded by move 4: move 1 on 2 ends, 2
     on 119, 3 on 66, 4 on 20.
  F5 THE LOCK (PE4, one part missed). 189 of 207 void ends repeat one
     vehicle over their last 10 moves; the 18 that do not are all
     Q(sqrt -15), where the price is 4 at every move of every end. Its
     class of the places over 2 has order 2, so both places lie in it
     and it has TWO least ideals, P2 and P2': the vehicles P2^2 and P2
     P2' tie at 4 forever and the tree follows every interleaving. A
     least ideal need not be unique over a number ring. Void lock
     prices 2, 3, 4, 9, 13, 25; seed lock prices 2 to 47. No lock
     vehicle lies over two primes, from the void or from any seed.

THE SECOND SITTING: WHERE A LOCK'S RIDER CAN SIT. element_ring.py
leaves open whether a lock's rider can lie over another prime than its
core. F5 found none. Is that forced?

THE ARGUMENT (written before its engine).
  (5) Over an imaginary quadratic field, a vehicle W that a walk repeats
      forever lies over one prime. Let S over p be a core of W at door
      r, W = S^r R with R a least ideal of class -r c_S. Then N(R) <=
      p^r: S's conjugate S' (S itself when ramified) has class -c_S, so
      S'^r is an integral ideal of class -r c_S; an inert S is
      principal and R = (1). Suppose R has a place over q != p. Once W
      repeats, only W's places move, so the places of W over q grow
      without bound, the q-count is the largest of their columns and
      rises infinitely often, and at each rise a place Y of W over q is
      a holder, past its tail once the count is. By (1) it pends at most
      Lambda_Y, and by (3) Lambda_Y <= q^2 (split: q * mu(c_Y) <= q * q,
      Y itself lying in c_Y; ramified or inert: q^2). But N(W) = p^r
      N(R) >= p^r N(Y): if N(Y) = q then q <= N(R) <= p^r and N(W) >=
      q^2, with equality only if p^r = q, impossible; if Y is inert,
      N(W) >= p^r q^2 > q^2. So Y pends strictly below N(W), and W is
      not a least move at that state. Hence W has no place over q.
      THEOREM: a lock's rider lies over its core's prime.
      The quadratic field enters twice. Once in Lambda_Y <= q^2, which in
      a field of degree n reads only q^n; and once in the bound
      N(R) <= p^r: over a field of higher degree S's class need not be
      cancelled by a power of the places over p, and the question stays
      open there.

PREDICTIONS, frozen before the engine, each naming what the run PRINTS.
  PR1 THE TABLE (proof check of (3), read first). At every field, the
      places over each prime share one Lambda, and it equals p mu(c)
      for a split place, p^2 for a ramified or inert one. Printed: the
      blocks read, the mismatches, and Q(sqrt -5)'s table. KILL: one.
  PR2 WHERE THE THEOREM BITES. Every split non-principal place S of norm
      at most 60 whose least rider R = MINREP(-c_S) lies over another
      prime is seeded at W^j, W = S R, j = 1, 2, 3, and walked 40 moves
      on one path. Printed: the seeds, how many take W at least once as
      a move (the POSITIVE CONTROL: at least one, or the test is
      vacuous and says so), how many repeat one vehicle over their last
      10 moves, the lid violations, and the lock vehicles over two
      primes. KILL: a lock over two primes, or a lid violation.

FINDINGS OF THE SECOND SITTING (entered after the run, from its output).
  F6 THE TABLE (PR1 hit). 5234 blocks over the primes with a place of
     norm <= 400, 0 mismatches; (3)'s creeper clause holds for a
     non-principal ramified place, a principal one lying in no least
     ideal. Q(sqrt -5): the
     ramified place over 2 at 4, the split pair over 3 at 6 each, the
     ramified place over 5 at 25, the places over 7 at 14.
  F7 WHERE THE THEOREM BITES (PR2 hit, positive control met). 1354
     pairs of a split non-principal place and a least rider over another
     prime, 4062 seeds: 100 take the two-prime vehicle W at least once,
     and every one leaves it. Q(sqrt -5), core over 3 with the ramified
     place over 2 riding, from W: 4, 6, 6, 4, 4, ..., W taken at the
     second and third moves. All 4062 lock, 0 lid violations, and no
     lock vehicle lies over two primes; lock prices from 4 to 121.

RUN RECORD (both sittings). One process, CPython, no numpy: 784,441
checks, 28.5 s, peak working set 78.6 MB.
"""

import os
import sys
import time
from collections import Counter
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import door as DR  # noqa: E402
import race as RC  # noqa: E402
import winner as WN  # noqa: E402

CHECKS = [0]
N_W = 40        # moves per walk
LOCK_R = 10     # a lock: the last LOCK_R moves repeat one vehicle
SEED_N = 40     # principal seeds up to this norm, one path each
CAP = 20000     # states per step of a tree


def check(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise SystemExit("FAIL: " + msg)


# ---------------------------------------------------------------------------
# the class group by reduced forms

def reduce_form(a, b, c):
    D = b * b - 4 * a * c
    while True:
        k = (b + a - 1) // (2 * a)
        b -= 2 * a * k
        c = (b * b - D) // (4 * a)
        if a > c:
            a, b, c = c, -b, a
            continue
        if a == c and b < 0:
            b = -b
        return a, b, c


def reduced_forms(D):
    out, a = [], 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a) == 0:
                c = (b * b - D) // (4 * a)
                if c >= a and not (a == c and b < 0) and \
                        gcd(gcd(a, abs(b)), c) == 1:
                    out.append((a, b, c))
        a += 1
    return sorted(out)


def xgcd(a, b):
    """(u, v, d) with u a + v b = d = gcd(a, b) >= 0."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if a < 0:
        a, x0, y0 = -a, -x0, -y0
    return x0, y0, a


def compose(f1, f2, D):
    """Dirichlet composition (Cohen 5.4.7), reduced."""
    (a1, b1, c1), (a2, b2, c2) = f1, f2
    if a1 > a2:
        (a1, b1, c1), (a2, b2, c2) = (a2, b2, c2), (a1, b1, c1)
    s = (b1 + b2) // 2
    n = b2 - s
    if a2 % a1 == 0:
        y1, d = 0, a1
    else:
        u, v, d = xgcd(a2, a1)
        y1 = u
    if s % d == 0:
        y2, x2, d1 = -1, 0, d
    else:
        u, v, d1 = xgcd(s, d)
        x2, y2 = u, -v
    v1, v2 = a1 // d1, a2 // d1
    r = (y1 * y2 * n - x2 * c2) % v1
    b3 = b2 + 2 * v2 * r
    a3 = v1 * v2
    check((b3 * b3 - D) % (4 * a3) == 0, "composition off discriminant")
    return reduce_form(a3, b3, (b3 * b3 - D) // (4 * a3))


class Group:
    """The class group as indices into the reduced forms, 0 principal."""

    def __init__(self, D):
        self.D = D
        self.forms = reduced_forms(D)
        self.h = len(self.forms)
        self.ix = {f: i for i, f in enumerate(self.forms)}
        check(self.forms[0][0] == 1, "the principal form first")
        self.mul = [[self.ix[compose(f, g, D)] for g in self.forms]
                    for f in self.forms]
        self.inv = [self.ix[reduce_form(a, -b, c)] for a, b, c in self.forms]
        self.ords = []
        for x in range(self.h):
            k, y = 1, x
            while y != 0:
                y = self.mul[y][x]
                k += 1
            self.ords.append(k)

    def power(self, x, k):
        y = 0
        for _ in range(k % self.ords[x]):
            y = self.mul[y][x]
        return y

    def of_form(self, a, b, c):
        return self.ix[reduce_form(a, b, c)]


def group_control(G):
    """PE0 (a) at one discriminant."""
    h, mul = G.h, G.mul
    for x in range(h):
        check(mul[0][x] == x and mul[x][0] == x, "identity")
        check(mul[x][G.inv[x]] == 0, "inverse")
        for y in range(h):
            check(mul[x][y] == mul[y][x], "commutative")
            for z in range(h):
                check(mul[mul[x][y]][z] == mul[x][mul[y][z]], "associative")


# ---------------------------------------------------------------------------
# a field: its places with their classes, mu and the least ideals

class Field:
    def __init__(self, m):
        self.m = m
        self.D = m if m % 4 == 1 else 4 * m
        self.pls = WN.field(m)
        self.G = G = Group(self.D)
        group_control(G)
        cls, seen = [], Counter()
        for q in self.pls:
            if q.f == 2 and q.e == 1:
                cls.append(0)
                continue
            p = q.p
            b = [b for b in range(0, 2 * p)
                 if (b * b - self.D) % (4 * p) == 0][0]
            sign = -1 if seen[p] else 1
            seen[p] += 1
            cls.append(G.of_form(p, sign * b, (b * b - self.D) // (4 * p)))
        self.cls = cls
        for i, q in enumerate(self.pls):
            if q.e == 1 and q.f == 1 and seen[q.p] == 2 and \
                    i + 1 < len(self.pls) and self.pls[i + 1].p == q.p:
                check(G.mul[cls[i]][cls[i + 1]] == 0,
                      f"Q(sqrt {m}): a split pair's product not principal")
        least = {}
        for q in self.pls:
            c = cls[q.idx]
            if c not in least or q.N < least[c]:
                least[c] = q.N
        INF = float("inf")
        mu = [INF] * G.h
        mu[0] = 1
        changed = True
        while changed:
            changed = False
            for x in range(G.h):
                if mu[x] < INF:
                    for c, n in least.items():
                        y = G.mul[x][c]
                        if mu[x] * n < mu[y]:
                            mu[y] = mu[x] * n
                            changed = True
        self.mu = mu
        self.least = self.least_ideals(max(mu))
        self.lam_rec = [self.price(q, q.e) for q in self.pls]
        self.creep = set()
        for ids in self.least:
            for I in ids:
                for i, k in I:
                    if 0 < k < self.pls[i].e:
                        self.creep.add(i)

    def ideals(self, top):
        """Every integral ideal of norm <= top: (norm, ((idx, k), ...))."""
        small = [q for q in self.pls if q.N <= top]
        out = []

        def rec(j, n, ideal):
            out.append((n, tuple(ideal)))
            for t in range(j, len(small)):
                q = small[t]
                k, nn = 1, n * q.N
                while nn <= top:
                    rec(t + 1, nn, ideal + [(q.idx, k)])
                    k += 1
                    nn *= q.N
        rec(0, 1, [])
        return out

    def least_ideals(self, top):
        """Per class the ideals of least norm, PE0 (b) checked."""
        best = {}
        for n, I in self.ideals(top):
            best.setdefault(self.cls_of(I), []).append((n, I))
        least = []
        for x in range(self.G.h):
            ns = best.get(x, [])
            check(ns, f"Q(sqrt {self.m}): class {x} has no ideal <= {top}")
            lo = min(n for n, I in ns)
            check(lo == self.mu[x], f"Q(sqrt {self.m}): brute mu at {x}")
            check(lo == self.G.forms[x][0],
                  f"Q(sqrt {self.m}): mu is not the leading coefficient")
            least.append([I for n, I in ns if n == lo])
        return least

    def cls_of(self, I):
        x = 0
        for i, k in I:
            x = self.G.mul[x][self.G.power(self.cls[i], k)]
        return x

    def rider_class(self, q, r):
        return self.G.inv[self.G.power(self.cls[q.idx], r)]

    def price(self, q, r):
        return q.N ** r * self.mu[self.rider_class(q, r)]

    def state(self, I):
        st = St()
        for i, k in I:
            st.a[i] = k
            lam = self.pls[i].lam(k)
            st.L = st.L * lam // gcd(st.L, lam)
        return st


def fields():
    for m in range(-1, -201, -1):
        if RC.squarefree(m):
            yield Field(m)


# ---------------------------------------------------------------------------
# the element walk

class St:
    __slots__ = ("a", "L")

    def __init__(self, a=None, L=1):
        self.a, self.L = dict(a or {}), L

    def key(self):
        return tuple(sorted(self.a.items()))


def emenu(F, st):
    """(best price, [vehicle]); a vehicle is ((core idx, door), (idx, k),
    ...), its places sorted after the core."""
    best, out = None, []
    for q in F.pls:
        if best is not None and q.N > best:
            break
        r = DR.door_lcm(q, st.a.get(q.idx, 0), st.L)
        pr = F.price(q, r)
        if best is None or pr < best:
            best, out = pr, []
        if pr == best:
            for I in F.least[F.rider_class(q, r)]:
                v = Counter({q.idx: r})
                for i, k in I:
                    v[i] += k
                out.append(((q.idx, r),) + tuple(sorted(v.items())))
    check(best is not None and best < F.pls[-1].N, "the supply ran out")
    return best, out


def apply(F, st, veh):
    n = St(st.a, st.L)
    for i, k in veh[1:]:
        n.a[i] = n.a.get(i, 0) + k
        lam = F.pls[i].lam(n.a[i])
        n.L = n.L * lam // gcd(n.L, lam)
    check(n.L != st.L, "a vehicle that does not raise lambda")
    return n


class Path:
    __slots__ = ("st", "vehs", "paid")

    def __init__(self, st, vehs, paid):
        self.st, self.vehs, self.paid = st, vehs, paid


def etree(F, st0, n, tally=None):
    """Every tie branched, equal states merged (the first path kept); at
    class number 1 every state's menu is read against race.py's."""
    front = {st0.key(): Path(st0, [], [])}
    for _ in range(n):
        nxt = {}
        for path in front.values():
            best, vehs = emenu(F, path.st)
            succ = set()
            for v in vehs:
                s2 = apply(F, path.st, v)
                k = s2.key()
                succ.add(k)
                if k not in nxt:
                    nxt[k] = Path(s2, path.vehs + [v], path.paid + [best])
            if tally is not None and F.G.h == 1:
                ideal_control(F, path.st, best, succ, tally)
        front = nxt
        check(len(front) <= CAP, "the branch cap")
    return list(front.values())


def ideal_control(F, st, best, succ, tally):
    """PE0 (d): at class number 1 the element menu is race.py's."""
    rs = DR.RSt()
    rs.a, rs.L = dict(st.a), st.L
    b2, types = RC.menu(F.pls, rs, Counter(), True)
    s2 = set()
    for t in types:
        n = DR.rstep(F.pls, rs, t, b2, [], [], Counter())
        s2.add(n.key())
    tally["ctl_states"] += 1
    check(b2 == best and s2 == succ, f"Q(sqrt {F.m}): element and ideal"
          f" menus part at {st.key()}")


def canon_path(F, st0, n):
    st, vehs, paid = st0, [], []
    for _ in range(n):
        best, vs = emenu(F, st)
        v = min(vs)
        st = apply(F, st, v)
        vehs.append(v)
        paid.append(best)
    return Path(st, vehs, paid)


# ---------------------------------------------------------------------------
# the element lid read off a state

def tail(q):
    return DR.tail_index(q.lad)[0]


def holders(F, st, p):
    V = DR.vp(st.L, p)
    return V, [q for q in F.pls if q.p == p and st.a.get(q.idx, 0) >= 1
               and DR.column(q.lad, st.a[q.idx]) == V]


def block_read(F, st, p):
    """(lidded, lid, B, holders) of the block over p at st."""
    V, hold = holders(F, st, p)
    if not hold:
        return False, None, None, hold
    over = [q for q in F.pls if q.p == p]
    lid = max(F.lam_rec[q.idx] for q in hold)
    B = max([lid] + [F.lam_rec[q.idx] for q in over if q.idx in F.creep])
    ok = all(V >= tail(q) for q in over) and p ** (V + 1) >= B
    return ok, lid, B, hold


def read_path(F, st0, path, tot):
    """PE1 and PE2 along one path: the first lidded move, or None."""
    states = [st0]
    for v in path.vehs:
        states.append(apply(F, states[-1], v))
    lidded, first = {}, None
    for t, st in enumerate(states):
        tot["states"] += 1
        now = {}
        for p in {F.pls[i].p for i in st.a}:
            ok, lid, B, hold = block_read(F, st, p)
            if ok:
                now[p] = (lid, B, hold)
                for q in hold:
                    r = DR.door_lcm(q, st.a[q.idx], st.L)
                    tot["holder_over"] += F.price(q, r) > F.lam_rec[q.idx]
        tot["lid_lost"] += sum(p not in now for p in lidded)
        for p, (lid, B, hold) in now.items():
            if p in lidded:
                tot["lid_rise"] += lid > lidded[p][0]
                tot["over_B"] += lid > lidded[p][1]
                lidded[p] = (lid, lidded[p][1])
            else:
                lidded[p] = (lid, B)
        if t > 0:
            before = states[t - 1]
            for p in lidded:
                V, hold = holders(F, st, p)
                tot["jump_on_lid"] += V > DR.vp(before.L, p) and not hold
        if not now:
            continue
        if first is None:
            first = t
        cur = min(lid for lid, B, hold in now.values())
        ideal = min(max(q.N ** q.e for q in hold)
                    for lid, B, hold in now.values())
        if t < len(path.paid):
            tot["paid_after"] += 1
            tot["over"] += path.paid[t] > cur
            if path.paid[t] > ideal:
                tot["over_ideal"] += 1
                tot.setdefault("over_ideal_at", set()).add(F.m)
    return first


def lock_read(F, path, tot, key):
    tail_v = path.vehs[-LOCK_R:]
    if len({v[1:] for v in tail_v}) != 1:
        tot[key + "_unlocked"] += 1
        tot.setdefault(key + "_unlocked_at", []).append(F.m)
        return
    v = tail_v[0]
    tot[key + "_locked"] += 1
    tot.setdefault(key + "_prices", Counter())[path.paid[-1]] += 1
    if len({F.pls[i].p for i, k in v[1:]}) > 1:
        tot.setdefault(key + "_two", []).append(
            (F.m, path.paid[-1], [(F.pls[i].name, k) for i, k in v[1:]]))


# ---------------------------------------------------------------------------
# the sections

def section_control(Fs):
    print("PE0  CONTROLS")
    hs = Counter(F.G.h for F in Fs)
    print(f"  {len(Fs)} fields; class numbers (h: fields) "
          f"{sorted(hs.items())}; every group closed, associative, with "
          f"identity and inverses; every split pair principal; mu equal to "
          f"the leading coefficient and the brute minimum at every class")
    by = {F.m: F for F in Fs}
    for m, want in ((-5, [4, 4, 9, 6] + [4] * 8), (-23, [6, 6, 6] + [4] * 9)):
        ends = etree(by[m], St(), len(want))
        seqs = {tuple(pth.paid) for pth in ends}
        check(tuple(want) in seqs, f"PE0 (c) at {m}")
        print(f"  Q(sqrt {m}): the void's tree holds {want[:5]} ...; "
              f"{len(ends)} end(s)")
    tally = Counter()
    for F in Fs:
        if F.G.h == 1:
            etree(F, St(), 12, tally)
    print(f"  class number 1: {tally['ctl_states']} states, element menu "
          f"equal to the ideal menu at every one")


def section_lid(Fs):
    print("PE1 - PE4  THE ELEMENT LID FROM THE VOID")
    tot, reach, t0 = Counter(), Counter(), time.time()
    for F in Fs:
        tot["fields"] += 1
        for path in etree(F, St(), N_W):
            tot["ends"] += 1
            first = read_path(F, St(), path, tot)
            if first is None:
                tot["unlidded"] += 1
            else:
                reach[first] += 1
            lock_read(F, path, tot, "void")
    print(f"  {tot['fields']} fields, {tot['ends']} ends, {tot['states']} "
          f"states, {tot['paid_after']} prices paid after a lidded state "
          f"({time.time() - t0:.1f} s)")
    print(f"  PE1 violations: lid lost {tot['lid_lost']}, lid risen "
          f"{tot['lid_rise']}, lid over B {tot['over_B']}, price over the "
          f"lid {tot['over']}, jump on a lidded block {tot['jump_on_lid']},"
          f" holder over its Lambda {tot['holder_over']}")
    for k in ("lid_lost", "lid_rise", "over_B", "over", "jump_on_lid",
              "holder_over"):
        check(tot[k] == 0, "PE1: " + k)
    at = sorted(tot.get("over_ideal_at", set()))
    print(f"  PE2 prices over the ideal lid N^e: {tot['over_ideal']}, at "
          f"{len(at)} fields {at}")
    print(f"  PE3 ends lidded {tot['ends'] - tot['unlidded']}, not "
          f"{tot['unlidded']}; first lidded move (move: ends) "
          f"{sorted(reach.items())}")
    print(f"  PE4 locked ends {tot['void_locked']}, not "
          f"{tot['void_unlocked']} {tot.get('void_unlocked_at', [])}; lock "
          f"prices {sorted(tot.get('void_prices', Counter()).items())}; "
          f"over two primes {tot.get('void_two', [])}")
    return tot


def section_seeds(Fs):
    print("PE4  THE PRINCIPAL SEEDS, ONE PATH EACH")
    tot, t0 = Counter(), time.time()
    for F in Fs:
        for n, I in F.ideals(SEED_N):
            if not I or F.cls_of(I) != 0:
                continue
            st0 = F.state(I)
            path = canon_path(F, st0, N_W)
            tot["seeds"] += 1
            if read_path(F, st0, path, tot) is None:
                tot["unlidded"] += 1
            lock_read(F, path, tot, "seed")
    print(f"  {tot['seeds']} seeds ({time.time() - t0:.1f} s); lid "
          f"violations {sum(tot[k] for k in ('lid_lost', 'lid_rise', 'over_B', 'over', 'jump_on_lid', 'holder_over'))},"
          f" unlidded {tot['unlidded']}")
    for k in ("lid_lost", "lid_rise", "over_B", "over", "jump_on_lid",
              "holder_over"):
        check(tot[k] == 0, "PE1 at the seeds: " + k)
    print(f"  locked {tot['seed_locked']}, not {tot['seed_unlocked']} "
          f"{tot.get('seed_unlocked_at', [])}; lock prices "
          f"{sorted(tot.get('seed_prices', Counter()).items())}")
    two = tot.get("seed_two", [])
    print(f"  lock vehicles over two primes: {len(two)}; the first "
          f"{two[:6]}")


def section_table(Fs):
    print("PR1  THE TABLE")
    blocks = bad = 0
    for F in Fs:
        for p in sorted({q.p for q in F.pls if q.N <= 400}):
            over = [q for q in F.pls if q.p == p]
            want = set()
            for q in over:
                if q.e == 1 and q.f == 1:
                    want.add(p * F.mu[F.cls[q.idx]])
                else:
                    want.add(p * p)
            got = {F.lam_rec[q.idx] for q in over}
            blocks += 1
            bad += len(got) != 1 or got != want
    print(f"  {blocks} blocks, mismatches {bad}")
    check(bad == 0, "PR1: the table")
    F = [F for F in Fs if F.m == -5][0]
    print(f"  Q(sqrt -5): " + ", ".join(
        f"{q.name} Lambda {F.lam_rec[q.idx]}" for q in F.pls[:5]))


def section_bite(Fs):
    print("PR2  WHERE THE THEOREM BITES")
    tot, t0 = Counter(), time.time()
    for F in Fs:
        for q in F.pls:
            if q.N > 60 or q.e != 1 or q.f != 1 or F.cls[q.idx] == 0:
                continue
            for R in F.least[F.rider_class(q, 1)]:
                if all(F.pls[i].p == q.p for i, k in R):
                    continue
                W = Counter({q.idx: 1})
                for i, k in R:
                    W[i] += k
                places = tuple(sorted(W.items()))
                tot["places"] += 1
                for j in (1, 2, 3):
                    st0 = F.state(tuple((i, j * k) for i, k in places))
                    path = canon_path(F, st0, N_W)
                    tot["seeds"] += 1
                    took = [t for t, v in enumerate(path.vehs)
                            if v[1:] == places]
                    tot["took"] += bool(took)
                    if took and "took_ex" not in tot:
                        tot["took_ex"] = (F.m, q.name, j, path.paid[:8],
                                          took[:5])
                    if read_path(F, st0, path, tot) is None:
                        tot["unlidded"] += 1
                    lock_read(F, path, tot, "bite")
    print(f"  {tot['places']} (place, rider) pairs, {tot['seeds']} seeds "
          f"({time.time() - t0:.1f} s); taking W at least once {tot['took']}"
          f"; example (field, core, j, prices, moves taking W) "
          f"{tot.get('took_ex')}")
    viol = sum(tot[k] for k in ("lid_lost", "lid_rise", "over_B", "over",
                                "jump_on_lid", "holder_over"))
    print(f"  locked {tot['bite_locked']}, not {tot['bite_unlocked']}; lid "
          f"violations {viol}, unlidded {tot['unlidded']}; lock prices "
          f"{sorted(tot.get('bite_prices', Counter()).items())}; locks over "
          f"two primes {tot.get('bite_two', [])}")
    check(viol == 0, "PR2: the lid")
    check(tot["bite_unlocked"] == 0, "PR2: every seed locks")
    check(not tot.get("bite_two"), "PR2: a lock over two primes")


def main():
    t0 = time.time()
    Fs = list(fields())
    section_control(Fs)
    section_lid(Fs)
    section_seeds(Fs)
    section_table(Fs)
    section_bite(Fs)
    print(f"\n{CHECKS[0]} checks, {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
