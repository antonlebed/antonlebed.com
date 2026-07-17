"""explore_tame_face.py — the odd-p (tame) face of the constellation law.

THE QUESTION. At p = 2 the arrival landing grades K(i)/K as a full
trichotomy (ramified / unramified / split) over all six ramified
quadratics of Q2. What survives at odd p — and is the trichotomy
structurally THINNED there?

THE HAND LEMMAS (derived before this file existed):

L1 (the arrival window). Arrival class c reaches the seat i* = e/(p-1)
   iff c*p^m = i*, m >= 1: arrival classes exist iff p | i*, i.e.
   p(p-1) | e — minimal e = 2 at p=2, 6 at p=3,
   20 at p=5. Odd-p QUADRATICS have no arrival classes: the whole p=2
   workhorse census has no odd-p analog.

L2 (the tame floor — the ramified letter is banned). Integral seat
   forces (p-1) | e, so v(-p) = e is even and u0 = (-p)/pi^e is a
   unit; Q_p(zeta_p) = Q_p((-p)^{1/(p-1)}) (classical; two lines:
   p = prod_k (zeta^k - 1) = lambda^{p-1} * prod u_k with
   u_k = 1 + zeta + ... + zeta^{k-1} ≡ k mod lambda, so
   prod u_k ≡ (p-1)! ≡ -1 by Wilson — -p = lambda^{p-1} * w, w a
   principal unit, and principal units are (p-1)-th powers by Hensel
   at odd p; equality by degree) makes K(zeta_p) =
   K(u0^{1/(p-1)}) a TAME unit-root extension — UNRAMIFIED always.
   The mu_p floor's alphabet at odd p is {unram, split}; at p = 2 the
   floor constellation is mu_4 and K(i)/K is WILD (deg 2 = p): all
   three letters live. The third letter is a wildness privilege.
   f=1 label (exact, pure fields pi^e = n): zeta_p in K iff
   r = (-p/n mod p) is a (p-1)-th power in F_p^*; no root otherwise
   (any candidate x = u*pi^{e/(p-1)} forces u^{p-1} = -p/pi^e exactly,
   and Fermat pins the residue).

L3 (the splice law). Seat cancellation happens iff a unit's residue
   direction meets a p-torsion member's. At p=2, f=1: ALWAYS (the F_2
   pigeonhole — even zeta_4-out fields splice +1: that is why the ram
   landing was 5 = 2e+1, not the naive 4; an earlier run's F_4 dodge is
   the f=2 escape). At odd p: iff zeta_p in K (the p-1 torsion directions
   exhaust F_p^*; out-fields' mu_p coefficients are non-rational —
   (zeta_3-1)/pi^{i*} squares to -3*zeta_3/pi^e, = -zeta_3 at B and
   -zeta_3/4 at B', a non-residue either way — so out-fields
   never collide and their whole chain is the pure psi-orbit).
   Worked instance (K = Q3(3^{1/6}), class-1 u = 1+t): s = u^3-1 =
   t^3 + 3t + 3t^2 has v = 3 exactly; Phi_9(u) = 3 + 3s + s^2 with
   v(3) = v(s^2) = 6 and cancellation needing a^2 = -1 in F_3 —
   insoluble (x^{p-1} = 1 != -1, every odd p) — so A = 6 identically:
   landing 9 = p*i*, the NAIVE gear value, spectrum rigid.

L4 (the cross-p landing law, m = 1, torsion tot-ram over K). The
   mu_{p^2} constellation is p-1 clusters (of p roots each) whose
   level-c coefficients exhaust F_p^*: a class-c unit collides exactly
   one cluster (forced), dodges at level c+1 (cluster shares its
   coefficient; p-1 free choices remain), avoids the rest at c:
   A = p(c+1) + (p-2)pc, so L = i* + A = p*(i* + 1), EXCEPT +1 when
   c(p-1) = 1 (p=2 quadratics: the mu_4 pair occupies both F_2 values
   at the stop level — Q2(i)'s 7). Regressions it re-reads: zeta8
   class-2 = 2*(4+1) = 10, zeta16 class-4 = 2*(8+1) = 18, Q2(i)
   class-1 = 6+1 = 7 (measured in an earlier run; cited, not re-run). In-field
   starters (m = 0): the p-1 mu_p directions exhaust F_p^*: collide
   one, dodge at i*+1: L = p*i* + 1 — the in-field starter floor at
   every p (zeta9's 10, N12's 4, zeta8 class-4's 9).

L5 (zeta9-membership, the mid-fields). E = Q3(zeta3), lambda =
   zeta3 - 1: lambda^2 = -3*zeta3 (direct), so v_E(-3) = 2. With
   K9 = E(zeta3^{1/3}) and C = E((-3)^{1/3}) (pi^2 is a cube root of
   -3 when pi^6 = -3), D = E(6^{1/3}): Kummer classes differ
   (v_E != 0 mod 3), so zeta9 is NOT in C or D. And C(zeta9)/C is
   TOTALLY ramified (every cubic line of <(-3), zeta3> over E is
   ramified), so the cluster coefficients stay F_3-rational and the
   mid-field class-1 game stops at level 2, above where
   zeta9-rationality bites: same landing 12 as K9, the in/out reading
   living in the SPECTRUM TOP (Krasner caps v(u - zeta9) at the
   conjugate distance 3: top <= 15, no CAP; K9's torsion members die
   at CAP).

THE PREDICTIONS (fixed and hand-attacked before this file existed):

Fields (all f = 1): Q3(sqrt3) x^2-3 out | Q3(zeta3) x^2+3x+3 in |
B x^6-3 out | B' x^6-12 out | C x^6+3 mid | D x^6-6 mid |
K9 Phi_9(x+1) in | E5 x^20-5 out (p=5) | Z25 Phi_25(x+1) in (p=5).

OD1 (arrival window): the quadratics' landing-spectra keys = {1}
    only; starter min 3 = p*i* at sqrt3 (naive dodge, spectrum {3}
    rigid), 4 = p*i*+1 at zeta3 (pigeonhole splice, CAP in spectrum).
OD2 (labels, independent + exact): residue tests certify B, B', E5,
    sqrt3 out (r a non-(p-1)-power); constructed torsion elements
    certify zeta3-quad, C, D, K9, Z25 in (Phi(zeta) = 0 at CAP).
OD3 (out-fields seat-NAIVE): B, B': class-1 and class-3 spectra
    both {9} rigid; full E-chain = the pure psi-law chain.
OD4 (mid/in floors, p=3): C, D, K9: class-1 min 12 = p(i*+1),
    class-3 min 10 = p*i*+1; K9 spectra carry CAP (both classes);
    C, D class-1 top <= 15 with NO CAP; E-chains = psi-law with
    splices {1: 12, 3: 10}.
OD5 (p=5 out): E5 sampled: class-1 and class-5 spectra {25} rigid,
    chain naive.
OD6 (p=5 in): Z25 sampled: class-1 min 30 = p(i*+1), class-5 min
    26 = p*i*+1, CAP in both spectra, chain = psi-law with splices
    {1: 30, 5: 26}.
OD7 (the splice law across the census): chain deviates from the pure
    psi-orbit iff zeta_p in K.
OD8 (gear exactness in fresh range): every sampled orbit obeys
    o(n+1) = psi(o(n)) off the seat and o(n+1) >= psi(o(n)) on it
    (an earlier run's PR-A/A' predictions, here at odd p, new fields).

THE DESIGN. LF machinery of explore_local_clock (imported; f=1,
g = [0,1]); helpers from explore_arrival_defect. Quadratics
EXHAUSTIVE (every representative of U_1/U_amax); e = 6 and e = 20
fields SAMPLED (seeded rng, per-class random units, heavy at the
seat-hitting classes, light elsewhere for the chain; a sampled value
below a frozen minimum falsifies the law outright, a sampled chain
above the psi-law falsifies naivety). Torsion members constructed
exactly (zeta = x+1 at cyclotomic models; zeta3 = (-1 + sqrt(-3))/2
at C and D, the square root Newton-lifted mod p^M) and injected into
the census so the CAP entries are present by construction, and their
Phi-vanishing is the in-label. Landing extraction keyed by start
class as in explore_arrival_defect. Labels never read orbits.
Run: python prime/code/explore_tame_face.py

FINDINGS (entered post-run, copied from printed output).

1. THE TAME THINNESS (rule in range; L1 + L2 verified over the
   census): the odd-p face is doubly thin — no arrival classes below
   e = p(p-1) (the quadratics' spectra keys are {1} only, both
   fields), and the mu_p floor never shows the ramified letter (every
   out-label certified by the even-valuation + non-power residue
   argument: r = 2 at the three p=3 out-fields, r = 4 at E5). The
   p=2 trichotomy's third letter is a wildness privilege.

2. THE SPLICE LAW (rule in range, OD3 + OD7; an earlier run's zeta_p
   gate, now with its residue mechanism and the arrival classes): seat
   cancellation is gated by rational p-torsion. Out-fields are seat-NAIVE — B and B'
   land {9} rigid at BOTH seat-hitting classes (9 = p*i*, the pure
   gear value; spectra single-valued over 600 samples/class), E5
   lands {25} rigid, and all their E-chains equal the pure psi-law
   chain. In-fields splice: zeta3-quad starter 4 = p*i*+1 (N12's
   chain reproduced exhaustively), C/D/K9 chains = psi-law with
   splices {1: 12, 3: 10}, Z25 with {1: 30, 5: 26}. At p = 2 even
   out-fields splice (the F_2 pigeonhole); at odd p the splice IS
   zeta_p-membership.

3. THE CROSS-p LANDING LAW (rule in range, OD4 + OD6): every m = 1
   in/mid arrival lands at p*(i*+1) — 12 = 3*(3+1) at C, D, and K9;
   30 = 5*(5+1) at Z25 — and every in-field starter at p*i*+1 (10 at
   the three sextics, 26 at Z25, 4 at the quadratic). With the p = 2
   face's measured zeta8 (10), zeta16 (18), and Q2(i) (7 = the
   c(p-1) = 1 exception), one formula covers the p = 2 and odd-p
   faces alike.
   (A later run BOUNDS the law's range: at e = 4 quartics of Q2 where
   2's first digit fires — w_1 = 1, half the 48-field sweep — the
   m = 1 arrival drops to p*i*+1 = 9 with both arrival spectra rigid
   {9}; the cluster game this derivation runs is cut off at the first
   digit before it starts. explore_mu8_grading.py MU1/MU2.
   SUBSUMED by a still later run: the general law is L = p*i* +
   min(delta, p^m), delta = v(-p/pi^e - 1) the window defect — this
   census's in/mid fields all measure delta >= p^m, the quartic-bound
   run's lock is delta = 1; explore_tame_readout.py.)

4. THE RAM LETTER LIVES ONE LAYER UP (observation with the hand
   mechanism): the mid-fields' class-1 spectra are {12, 13} — the
   top 13 = 3 + 3*(7/3) + 3 is the approach to the collided cluster
   cut at the FRACTIONAL level 7/3, the first third-level of zeta9's
   expansion over C (C(zeta9)/C is totally ramified of degree 3, L5)
   — the ramified cutoff, banned from the tame floor by L2,
   reappearing at the wild mu_9 layer exactly as at p = 2 (where
   i - 1 = sqrt2*zeta8^3 departs at half-levels). No CAP and nothing
   above 13 in 600 samples/class (Krasner caps the collide at 3).
   (A later run GENERALIZES this: the cut level is a LAW — delta/p,
   delta the Kummer defect of zeta_p in K; explore_cutoff_ladder.py.)

5. THE IN-FIELD FORK PIGEONHOLE (observation with the hand
   mechanism): K9's class-1 spectrum is {12, 16, 17, 18, CAP} — the
   {13, 14, 15} hole is the level-3 fork: the three cluster mates'
   branch residues are pairwise distinct at exact distance 3, so
   they exhaust F_3 and a level-3 stop is impossible — matching the
   level-2 coefficient forces one mate to d >= 4: L = d + 12, the
   torsion-adjacency ladder (u within d of a primitive 9th root lands
   at d + 12), visible as {16, 17, 18} then CAP — a RANGE truncation
   at amax = 18, not a bound; exact torsion dies at CAP. The same
   pigeonhole that prices the floor (L4) prices the fork. The
   mid-field contrast is absolute, not truncated: 13 is a ceiling.

6. THE FOUR-LAYER SUMMARY EXTENDS (synthesis of 1-5 with an earlier
   run's finding 5; rule in range, census p = 2, 3, 5): the transient
   reads the ramification of the p-power
   cyclotomic tower at every censused p, with the odd-p alphabet thinned at
   the tame floor (unram/split only, naive vs splice) and completed
   at the wild layers (fractional cutoffs, residue cutoffs, in-field
   tree games) — the wild/tame divide of the tower is itself part of
   what the transient reads.

RUN RECORD (python explore_tame_face.py, 7.7 s, exit 0): 170,364
checks passed (the per-step gear asserts over ~53K censused orbits —
39,367 exhaustive at the quadratics + ~13.9K sampled — dominate the
count; OD8 green everywhere). Landings as printed:
  Q3(sqrt3)  keys {1}, spectrum {3} rigid, chain naive
  Q3(zeta3)  keys {1}, starter 4, CAP graded, chain spliced (1->4)
  x^6-3      1->{9}  3->{9}   chain naive     (r = 2, out)
  x^6-12     1->{9}  3->{9}   chain naive     (r = 2, out)
  x^6+3      1->{12,13} 3->{10,11,12,13,14,CAP}
  x^6-6      1->{12,13} 3->{10,11,12,13,14,15,...}
  Q3(zeta9)  1->{12,16,17,18,CAP} 3->{10,11,12,13,14,15,...}
  x^20-5     1->{25} 5->{25}  chain naive     (r = 4, out)
  Q5(zeta25) 1->{30,CAP} 5->{26,27,28,29,30,CAP}
Green on the first run; no pre-green failures.
"""

import random
from fractions import Fraction
from math import comb

import explore_local_clock as lc
from explore_arrival_defect import (esub, const_el, landing_spectra,
                                    sample_class, fmt_spec)

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ---------------------------------------------------------------- helpers


def chain_pred(p, e, amax, splices):
    """psi-law E-chain with per-start-class splices {start: landing}."""
    best = [0] * amax
    for start in range(1, amax + 1):
        seat = e // (p - 1)
        sp = (seat, splices[start]) if start in splices else None
        seq = lc.psi_orbit(p, e, amax, start, sp)
        for a in range(1, amax + 1):
            m = sum(1 for v in seq if v < a)
            if m > best[a - 1]:
                best[a - 1] = m
    return [p ** m for m in best]


def gear_check(F, orbits):
    """OD8: two-gear exactness off the seat, lower bound on it."""
    for o in orbits:
        for n in range(len(o) - 1):
            if o[n] >= F.amax or o[n + 1] >= F.CAP:
                break
            want = min(F.p * o[n], o[n] + F.e)
            if o[n] != F.seat:
                ok(o[n + 1] == want,
                   "%s: gear broken off seat: %d -> %d"
                   % (F.name, o[n], o[n + 1]))
            else:
                ok(o[n + 1] >= want,
                   "%s: seat landing below psi: %d -> %d"
                   % (F.name, o[n], o[n + 1]))


def phi_torsion(F, z, n):
    """v(Phi_n(z)) for n in {3, 9, 25}: the exact in-label."""
    if n == 3:
        parts = [F.emul(z, z), z, const_el(F, 1)]
    elif n == 9:
        z3 = F.emul(F.emul(z, z), z)
        parts = [F.emul(z3, z3), z3, const_el(F, 1)]
    elif n == 25:
        z5 = F.emul(F.emul(F.emul(F.emul(z, z), z), z), z)
        parts, pw = [const_el(F, 1)], const_el(F, 1)
        for _ in range(4):
            pw = F.emul(pw, z5)
            parts.append(pw)
    else:
        raise ValueError(n)
    tot = parts[0]
    for q in parts[1:]:
        tot = tuple(F.cadd(a, b) for a, b in zip(tot, q))
    return F.val(tot)


def unit_res(n_pure, p):
    """Residue of the unit -p/pi^e = -p/n at pure fields pi^e = n."""
    fr = Fraction(-p, n_pure)
    return fr.numerator * pow(fr.denominator, -1, p) % p


def out_label(F, n_pure, p):
    """L2's exact out-certificate at pure fields pi^e = n_pure:
    r = -p/n mod p is no (p-1)-th power in F_p^*."""
    r = unit_res(n_pure, p)
    ok(F.e % (p - 1) == 0 and F.e % 2 == 0,
       "%s: seat/parity precondition" % F.name)
    ok(all(pow(a, p - 1, p) != r for a in range(1, p)),
       "%s: r = %d is a (p-1)-th power — not an out-field" % (F.name, r))
    return r


def census(F, rng, heavy, n_heavy, n_light, extra=()):
    """Sampled census: heavy classes deep, all classes light; plus
    constructed exact units. Returns (spectra, orbits)."""
    spec, orbits = {}, []

    def eat(units):
        for u in units:
            o = F.orbit(u)
            orbits.append(o)
            if F.seat is not None and F.seat in o:
                i = o.index(F.seat)
                if i + 1 < len(o):
                    spec.setdefault(o[0], set()).add(o[i + 1])

    for c in heavy:
        eat(sample_class(F, c, n_heavy, rng))
    for c in range(1, F.amax):
        eat(sample_class(F, c, n_light, rng))
    eat(extra)
    return spec, orbits


def newton_sqrt(c, p, pM, x0):
    """Square root of c mod p^M from a seed root mod p (odd p)."""
    x = x0
    for _ in range(12):
        x = (x + c * pow(x, -1, pM)) * pow(2, -1, pM) % pM
    assert (x * x - c) % pM == 0
    return x


# ------------------------------------------------------------------- run


def run():
    rng = random.Random(185)
    print("THE TAME FACE — the constellation law at odd p")
    print("=" * 64)

    # ---------------- section 1: the odd-p quadratics (exhaustive)
    print("\n[1] Q3(sqrt3), Q3(zeta3): no arrival classes; the splice gate")
    F = lc.LF("Q3(sqrt3)", 3, [0, 1], [-3, 0, 1], 10)
    spec, orbits = census(F, rng, [], 0, 0, extra=list(F.units()))
    ok(set(spec) == {1}, "sqrt3: arrival keys %s != {1}" % sorted(spec))
    ok(spec[1] == {3}, "sqrt3: starter spectrum %s != {3} (naive p*i*)"
       % sorted(spec[1]))
    out_label(F, 3, 3)                            # pi^2 = 3
    ch = lc.chain_from_orbits(3, orbits, F.amax)
    ok(ch == chain_pred(3, 2, F.amax, {}),
       "sqrt3: chain not the pure psi-law: %s" % ch)
    gear_check(F, orbits)
    print("  sqrt3  keys {1}, spectrum {3} rigid, chain naive %s" % ch)

    F = lc.LF("Q3(zeta3)", 3, [0, 1], [3, 3, 1], 10)
    z3 = ((1,), (1,))                             # zeta3 = x + 1
    ok(phi_torsion(F, z3, 3) >= F.CAP, "zeta3-quad: Phi_3(x+1) != 0")
    spec, orbits = census(F, rng, [], 0, 0, extra=list(F.units()) + [z3])
    ok(set(spec) == {1}, "zeta3: arrival keys %s != {1}" % sorted(spec))
    ok(min(spec[1]) == 4, "zeta3: starter min %d != 4 = p*i*+1"
       % min(spec[1]))
    ok(F.CAP in spec[1], "zeta3: no CAP entry (torsion dies)")
    ch = lc.chain_from_orbits(3, orbits, F.amax)
    ok(ch == chain_pred(3, 2, F.amax, {1: 4}),
       "zeta3: chain not psi-law + splice(1->4): %s" % ch)
    gear_check(F, orbits)
    print("  zeta3  keys {1}, starter 4 = p*i*+1, CAP graded, chain %s" % ch)

    # ---------------- section 2: the out sextics (seat-naive, rigid)
    print("\n[2] x^6-3, x^6-12: out-fields are seat-naive (OD3)")
    for name, n_pure in [("Q3(3^{1/6})", 3), ("Q3(12^{1/6})", 12)]:
        F = lc.LF(name, 3, [0, 1], [-n_pure, 0, 0, 0, 0, 0, 1], 18)
        r = out_label(F, n_pure, 3)
        spec, orbits = census(F, rng, [1, 3], 600, 60)
        ok(set(spec) <= {1, 3}, "%s: seat keys %s" % (name, sorted(spec)))
        ok(spec[1] == {9}, "%s: class-1 spectrum %s != {9} rigid"
           % (name, sorted(spec[1])))
        ok(spec[3] == {9}, "%s: class-3 spectrum %s != {9} rigid"
           % (name, sorted(spec[3])))
        ch = lc.chain_from_orbits(3, orbits, F.amax)
        ok(ch == chain_pred(3, 6, F.amax, {}),
           "%s: chain not naive: %s" % (name, ch))
        gear_check(F, orbits)
        print("  %-14s r=%d out; landings %s; chain naive"
              % (name, r, fmt_spec(F, spec)))

    # ---------------- section 3: the mid and in sextics (p=3 floors)
    print("\n[3] x^6+3, x^6-6, Q3(zeta9): the floors 12 and 10 (OD4)")
    for name, eis, mid in [
            ("Q3((-3)^{1/6})", [3, 0, 0, 0, 0, 0, 1], True),
            ("Q3(6^{1/6})", [-6, 0, 0, 0, 0, 0, 1], True),
            ("Q3(zeta9)", [3, 9, 18, 21, 15, 6, 1], False)]:
        F = lc.LF(name, 3, [0, 1], eis, 18)
        if name == "Q3(zeta9)":
            z9 = ((1,), (1,), (0,), (0,), (0,), (0,))   # zeta9 = x + 1
            ok(phi_torsion(F, z9, 9) >= F.CAP, "zeta9: Phi_9(x+1) != 0")
            extra = [z9, F.emul(F.emul(z9, z9), z9)]    # + zeta3
        else:
            inv2 = pow(2, -1, F.pM)
            if eis[0] == 3:                       # pi^6 = -3: sqrt-3 = pi^3
                u = 1
            else:                                 # pi^6 = 6: sqrt-3 = u*pi^3
                u = newton_sqrt((-inv2) % F.pM, 3, F.pM, 1)
            z3c = tuple(((-inv2) % F.pM,) if j == 0 else
                        ((u * inv2) % F.pM,) if j == 3 else (0,)
                        for j in range(6))        # zeta3 = (-1 + sqrt-3)/2
            ok(phi_torsion(F, z3c, 3) >= F.CAP,
               "%s: constructed zeta3 fails Phi_3" % name)
            # L2 consistency both ways: the in-residue IS a square
            ok(any(pow(a, 2, 3) == unit_res(-eis[0], 3)
                   for a in range(1, 3)),
               "%s: in-field residue not a square" % name)
            extra = [z3c]
        spec, orbits = census(F, rng, [1, 3], 600, 60, extra=extra)
        ok(min(spec[1]) == 12, "%s: class-1 min %d != 12 = p(i*+1)"
           % (name, min(spec[1])))
        ok(min(spec[3]) == 10, "%s: class-3 min %d != 10 = p*i*+1"
           % (name, min(spec[3])))
        ok(F.CAP in spec[3], "%s: class-3 misses CAP (zeta3 dies)" % name)
        if mid:
            top = max(v for v in spec[1])
            ok(F.CAP not in spec[1],
               "%s: class-1 shows CAP — zeta9 in K?!" % name)
            ok(top <= 15, "%s: class-1 top %d > 15 (Krasner)" % (name, top))
        else:
            ok(F.CAP in spec[1], "zeta9: class-1 misses CAP")
        ch = lc.chain_from_orbits(3, orbits, F.amax)
        ok(ch == chain_pred(3, 6, F.amax, {1: 12, 3: 10}),
           "%s: chain not psi-law + splices {1:12, 3:10}: %s" % (name, ch))
        gear_check(F, orbits)
        print("  %-14s landings %s" % (name, fmt_spec(F, spec)))

    # ---------------- section 4: p = 5 (sampled): E5 out, Z25 in
    print("\n[4] x^20-5, Q5(zeta25): the p=5 face (OD5, OD6)")
    F = lc.LF("Q5(5^{1/20})", 5, [0, 1], [-5] + [0] * 19 + [1], 32)
    r = out_label(F, 5, 5)
    spec, orbits = census(F, rng, [1, 5], 300, 25)
    ok(set(spec) <= {1, 5}, "E5: seat keys %s" % sorted(spec))
    ok(spec[1] == {25}, "E5: class-1 spectrum %s != {25} rigid"
       % sorted(spec[1]))
    ok(spec[5] == {25}, "E5: class-5 spectrum %s != {25} rigid"
       % sorted(spec[5]))
    ch = lc.chain_from_orbits(5, orbits, F.amax)
    ok(ch == chain_pred(5, 20, F.amax, {}), "E5: chain not naive")
    gear_check(F, orbits)
    print("  E5     r=%d out; landings %s; chain naive"
          % (r, fmt_spec(F, spec)))

    # Phi_25(x+1) coefficients, computed exactly
    phi25 = [0] * 21
    for j in range(5):
        for k in range(5 * j + 1):
            phi25[k] += comb(5 * j, k)
    F = lc.LF("Q5(zeta25)", 5, [0, 1], phi25, 32)
    z25 = tuple(((1,) if j <= 1 else (0,)) for j in range(20))
    ok(phi_torsion(F, z25, 25) >= F.CAP, "zeta25: Phi_25(x+1) != 0")
    z5c = z25
    for _ in range(4):
        z5c = F.emul(z5c, z25)                    # zeta25^5 = zeta5
    spec, orbits = census(F, rng, [1, 5], 300, 25, extra=[z25, z5c])
    ok(min(spec[1]) == 30, "Z25: class-1 min %d != 30 = p(i*+1)"
       % min(spec[1]))
    ok(min(spec[5]) == 26, "Z25: class-5 min %d != 26 = p*i*+1"
       % min(spec[5]))
    ok(F.CAP in spec[1] and F.CAP in spec[5], "Z25: torsion CAP missing")
    ch = lc.chain_from_orbits(5, orbits, F.amax)
    ok(ch == chain_pred(5, 20, F.amax, {1: 30, 5: 26}),
       "Z25: chain not psi-law + splices {1:30, 5:26}")
    gear_check(F, orbits)
    print("  Z25    landings %s" % fmt_spec(F, spec))

    print("\n%d checks passed" % CHECKS)


if __name__ == "__main__":
    run()
