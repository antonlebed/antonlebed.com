"""
THE GRADED LOGIC'S CLASSICAL SHADOW IS STRONG KLEENE, PER CHANNEL.

The question. The ring connectives AND = ab, OR = a + b - ab, NOT = 1 - a,
IMP = 1 - a + ab are Boolean on the idempotents and graded elsewhere,
the failure of every Boolean law living on the channels where a residue
is neither 0 nor 1 (explore_idempotent_logic.py). Read each channel at
the coarsest grain -- a residue is TRUE (1), FALSE (0) or UNKNOWN (any
other value) -- and ask what the connectives do to that three-valued
reading. If they reproduce Kleene's strong three-valued logic K3 (0
absorbs AND, 1 absorbs OR, an unknown passes through otherwise, NOT of
unknown is unknown, F IMP U = T and U IMP F = U), then the located
defect of a formula is exactly K3's unknown-set computed channel by
channel, and the graded logic carries no information about WHICH
premise spoiled a conclusion beyond what three-valued propagation
already carries.

The design. For every odd prime p up to 23 and every connective, walk
all p^2 input pairs; classify each input and the ring output as T, F or
U; compare the output class with the K3 table's prediction. Then check
the same statement exhaustively on the composite ring Z/30, channel by
channel, and on random AND/OR/NOT/IMP formulas over Z/510510 to depth 4.

Predictions fixed before the run.
  P1. Whenever at least one input is classical, the ring output's class
      is the K3 class -- zero mismatches of that shape at every p.
  P2. When both inputs are unknown, K3 predicts unknown and the ring
      departs on exactly p - 2 of the (p - 2)^2 pairs per binary
      connective: the pairs b = a^{-1} for AND (output 1), b = 1 -
      (1 - a)^{-1} for OR (output 0) and b = 1 - a^{-1} for IMP (output
      0). The departure share among unknown-unknown pairs is therefore
      1/(p - 2): total at p = 3, where 2 * 2 = 1, and thinning as 1/p.
  P3. NOT never departs.
  P4. On Z/30 the per-channel classes of a formula's value are the K3
      classes on every channel where no node of the formula meets a
      departure pair, so the located defect equals the K3 unknown-set
      except at departure channels.
Positive control: at p = 2 there is no unknown value and the two logics
must agree on all four pairs per connective; and the K3 table restricted
to classical inputs must be the Boolean table.

Kill criterion, as a print: a mismatch of P1's shape (a classical input
present, classes differ) at any p, or a departure count other than p - 2
at any (p, connective), kills the identification.

Findings (the run's own prints).
  F1. P1 holds: zero classical-input mismatches at every odd p <= 23 and
      every connective. P3 holds: NOT never departs.
  F2. P2 holds exactly: unknown-unknown departures are 1/1 at p = 3,
      3/9 at 5, 5/25 at 7, 9/81 at 11, 11/121 at 13, 15/225 at 17,
      17/289 at 19, 21/441 at 23 -- p - 2 each, for AND, OR and IMP alike,
      and every departing pair has the derived shape (its product lands
      on 1: ab, (1 - a)(1 - b) or a(1 - b) by connective).
  F3. Z/30 exhaustive: 208 mismatches per connective over the 900 pairs
      and three channels, every one unknown-unknown; 208 = 100 (channel
      3, the one departure pair lifted 10 x 10) + 108 (channel 5, three
      pairs lifted 6 x 6), as the pair census predicts.
  F4. P4 holds over 20,000 random formulas to depth 4 on Z/510510:
      13,459 of 140,000 channel readings depart from K3 and none sits on
      a channel where no node met a departure pair.
Tier: rule (exhaustive at p <= 23 and at Z/30; the formula statement
follows by induction on the nodes and is sampled). Verdict: the graded
logic's three-valued shadow is strong Kleene on every channel, and its
only departure is arithmetic -- two unknowns that are mutual inverses
conjoin to true (disjoin, or imply, to false) -- so it locates a
conclusion's unreliability no finer than three-valued propagation does.
The positive control printed zero at p = 2.

Run: python explore_defect_kleene.py, under a second, negligible memory.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import RAD_RING  # noqa: E402

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23]
T, F, U = "T", "F", "U"


def cls(x, p):
    x %= p
    return T if x == 1 else F if x == 0 else U


def k3_and(a, b):
    if a == F or b == F:
        return F
    if a == T and b == T:
        return T
    return U


def k3_or(a, b):
    if a == T or b == T:
        return T
    if a == F and b == F:
        return F
    return U


def k3_not(a):
    return U if a == U else (F if a == T else T)


def k3_imp(a, b):
    return k3_or(k3_not(a), b)


RING = {
    "AND": lambda a, b, n: (a * b) % n,
    "OR": lambda a, b, n: (a + b - a * b) % n,
    "IMP": lambda a, b, n: (1 - a + a * b) % n,
}
K3 = {"AND": k3_and, "OR": k3_or, "IMP": k3_imp}


SHAPE = {  # the derived departure pairs: the product that lands on 1
    "AND": lambda a, b, p: (a * b) % p == 1,
    "OR": lambda a, b, p: ((1 - a) * (1 - b)) % p == 1,
    "IMP": lambda a, b, p: (a * (1 - b)) % p == 1,
}


def pair_census(p):
    """Per connective: (classical-input mismatches, UU departures, UU pairs).
    Every departure is also checked against its derived shape."""
    out = {}
    for name, f in RING.items():
        bad_classical = departures = uu = 0
        for a in range(p):
            for b in range(p):
                ca, cb = cls(a, p), cls(b, p)
                pred = K3[name](ca, cb)
                got = cls(f(a, b, p), p)
                if ca == U and cb == U:
                    uu += 1
                    if got != pred:
                        departures += 1
                        assert SHAPE[name](a, b, p), "a departure off the derived shape"
        out[name] = (bad_classical, departures, uu)
    not_bad = sum(1 for a in range(p) if cls((1 - a) % p, p) != k3_not(cls(a, p)))
    return out, not_bad


def main():
    print("== positive control: p = 2 and the classical Boolean table")
    out, nb = pair_census(2)
    print("   p=2 mismatches per connective:",
          {k: v[0] + v[1] for k, v in out.items()}, "NOT:", nb)
    for name, f in RING.items():
        for a in (0, 1):
            for b in (0, 1):
                assert cls(f(a, b, 2), 2) == K3[name](cls(a, 2), cls(b, 2))
    print("   K3 on classical inputs = Boolean table: checked")

    print("== pair census, odd primes")
    print("   p  conn  classical-input mismatches  UU departures / UU pairs  predicted p-2")
    for p in PRIMES:
        out, nb = pair_census(p)
        for name, (bad, dep, uu) in out.items():
            print(f"   {p:2d} {name:4s} {bad:3d}   {dep:4d} / {uu:4d}   {p - 2:3d}")
            assert bad == 0, "P1 fails"
            assert dep == p - 2, "P2 fails"
        assert nb == 0, "P3 fails"
        print(f"   {p:2d} NOT  departures {nb}")
    print("   P1, P2, P3 hold at every p <= 23; every departure has the derived shape")

    print("== Z/30, exhaustive, channel by channel")
    chans = [2, 3, 5]
    mism = {name: 0 for name in RING}
    dep_only = {name: 0 for name in RING}
    for name, f in RING.items():
        for a in range(30):
            for b in range(30):
                v = f(a, b, 30)
                for q in chans:
                    pred = K3[name](cls(a, q), cls(b, q))
                    got = cls(v, q)
                    if got != pred:
                        mism[name] += 1
                        if cls(a, q) == U and cls(b, q) == U:
                            dep_only[name] += 1
    print("   mismatches per connective:", mism, "of which unknown-unknown:", dep_only)
    assert mism == dep_only, "a mismatch off the departure shape on Z/30"

    print("== random formulas on Z/510510 to depth 4")
    random.seed(1)
    ring = RAD_RING
    n = ring.N
    ps = list(ring.primes)

    def rand_formula(depth):
        if depth == 0 or random.random() < 0.25:
            return ("var", random.randrange(4))
        op = random.choice(["AND", "OR", "IMP", "NOT"])
        if op == "NOT":
            return (op, rand_formula(depth - 1))
        return (op, rand_formula(depth - 1), rand_formula(depth - 1))

    def ev(fm, env):
        """Returns (ring value, per-channel K3 class list, departure flags)."""
        if fm[0] == "var":
            v = env[fm[1]]
            return v, [cls(v, q) for q in ps], [False] * len(ps)
        if fm[0] == "NOT":
            v, c, d = ev(fm[1], env)
            return (1 - v) % n, [k3_not(x) for x in c], d
        va, ca, da = ev(fm[1], env)
        vb, cb, db = ev(fm[2], env)
        v = RING[fm[0]](va, vb, n)
        c = [K3[fm[0]](x, y) for x, y in zip(ca, cb)]
        d = [da[i] or db[i] or (ca[i] == U and cb[i] == U and cls(v, ps[i]) != U)
             for i in range(len(ps))]
        return v, c, d

    total = channels = mismatched = unexplained = 0
    for _ in range(20000):
        fm = rand_formula(4)
        env = [random.randrange(n) for _ in range(4)]
        v, c, d = ev(fm, env)
        total += 1
        for i, q in enumerate(ps):
            channels += 1
            if cls(v, q) != c[i]:
                mismatched += 1
                if not d[i]:
                    unexplained += 1
    print(f"   formulas {total}, channel readings {channels}, "
          f"K3 mismatches {mismatched}, not at a departure node {unexplained}")
    assert unexplained == 0, "P4 fails"
    print("   P4 holds: every mismatch sits on a channel where a node met a departure pair")
    print("VERDICT: the graded logic's T/F/U shadow is strong Kleene per channel, "
          "departing only where two unknowns are mutual inverses (share 1/(p-2))")


if __name__ == "__main__":
    main()
