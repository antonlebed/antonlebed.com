# BUDGET — what omitting a place frees at a global constraint

The object: a global constraint over a global field, one local term per
place tied by one relation — the product formula, the partial fractions
of a rational, Hilbert reciprocity, the sum of Brauer invariants, the
degree of a divisor. A place is **omitted** when its term is never
consulted; the **budget** is what the other terms gain. This page proves
that at an exact constraint the budget is the omitted term's own image
in the constraint's group, and that at an inexact one the constraint's
own corrector H cuts it down, less as the omitted term's kernel covers
more of H. It reads the corrector on three faces over number fields, and
shows that the form of the answer never uses the archimedean place's
being archimedean, though its value does, through its local groups, as
R at the product formula and ½Z/Z at the Brauer sum. In the
table, over a number field K, S_f is the set of omitted finite places, r
the unit rank, Reg the regulator, P a prime of the ring of integers and
NP its norm; the rank and volume faces below state the last row, whose
"everything" is the omitted terms' image before the corrector cuts it
down and whose S-units are the global elements realized above the zero
visible family, and the layer face below keeps every place and cuts the local
units.

```
CONSTRAINT          GROUP     OMITTED            BUDGET           CORRECTOR
product formula/Q   R         ∞                  everything       none
partial fractions/Q R/Z       ∞                  everything;      none
                                                  x ∈ Q mod 1 is
                                                  the rest's sum
Hilbert symbols/Q   ±1        any one place      one parity bit   none
Brauer sum/Q        Q/Z       ∞; a prime p       ½Z/Z; all of Q/Z none
degree/F_q(t)       Z         a place of degree  dZ               none
                               d
product formula/K   R         S_f and every ∞    everything; over the class
                                                  0, the S-units:  group and
                                                  rank r + |S_f|,  the unit
                                                  volume Reg·      torus
                                                  index·Π log NP
```

The archimedean place of Q buys the most at the product formula and
the least at the Brauer sum, and at reciprocity it buys what every
place buys. What decides each row whose constraint is exact is the
size of the omitted term's image, a fact about that term's local
group and its map into the constraint's group. At the Brauer sum that
fact is the archimedean place's own: Br(R) = ½Z/Z, while every p-adic
place has Br(Q_p) = Q/Z.

## The budget theorem
Tier: theorem.
Verifier: proof.

Write a constraint as a complex X → ⊕_v L_v → G on the global elements
X, the first map i sending a global element to its local terms and the
second, s, summing their images s_v(l_v) in G, with s ∘ i = 0 and almost
every term 0. It is an
**exact constraint** when every family with s = 0 is i of a global
element. Omit a place w; a set W of places is omitted the same way, its
terms summed into one L_W = ⊕_{v ∈ W} L_v. Then:

1. At an exact constraint a visible family l = (l_v)_{v ≠ w} is the
   visible part of a global element iff s(l), the sum of s_v(l_v) over
   the visible places alone, lies in s_w(L_w). The omission buys
   exactly the image s_w(L_w), and the omitted term is fixed by the
   visible ones up to the kernel of s_w.
2. At any constraint, let the **corrector** H = ker s / im i, the
   families with s = 0 modulo the global ones. A visible family is
   realized iff s(l) lies in s_w(L_w) and some completion has class 0 in
   H. The completions' classes fill one coset of the image of ker s_w in
   H, so the obstruction lives in H modulo that image. H belongs to the
   constraint; the omitted place decides only how much of it its own
   kernel absorbs.

Proof. A global element's terms satisfy s = 0, so its omitted term l_w
has s_w(l_w) = −s(l), which forces s(l) ∈ s_w(L_w). Conversely, if s(l)
lies in that image, some l_w has s_w(l_w) = −s(l), and l completed by
l_w is a family with s = 0; at an exact constraint it is i of a global
element. Two completions of l with s = 0 differ by an element k of ker
s_w at w, which fixes the omitted term up to that kernel, and k placed
at w alone is itself a family with s = 0; so the completions' classes
fill one coset of the image of ker s_w in H, and a completion is global
iff its class in H is 0. At an exact constraint H = 0, which gives 1
again.

## The constraints over Q
Tier: known.
Source: Serre, A Course in Arithmetic (1973), ch. III, the product
formula for Hilbert symbols and the existence theorem; Albert, Brauer,
Hasse and Noether (1932) for the Brauer sum.

All four are exact over Q, and the theorem reads each one off its
local groups.

- The product formula. L_p = Z (the valuation), L_∞ = R
  (log |x| for x ∈ Q×). Every finitely supported vector (e_p) is the
  valuation vector of ±∏ p^(e_p), so omitting ∞ leaves the finite terms
  no constraint at all, and |x| is then forced: it is ∏ p^(e_p).
  Omitting a prime p instead buys only Z·log p.
- The partial fractions. For x ∈ Q, x ≡ Σ_p {x}_p (mod 1), with {x}_p
  the p-part in L_p = Z[1/p]/Z and the term at ∞ in L_∞ = R/Z. Every
  finite family of p-parts is realized by its sum, and the omitted term
  x mod 1 is that sum. Read at a fraction whose denominator is a
  modulus M, this identity is the partial-fraction reading of size,
  whose truncated sums can wrap and misread a small value as large
  where the same read over F₂[t] cannot (SIZE.md#the-f₂x-control,
  which writes the ring F₂[x]).
- Hilbert reciprocity. The symbols (a, b)_v of the quaternion algebra
  (a, b), generated by anticommuting square roots of a and of b,
  multiply to 1, and every set of places of even size is the
  ramification set of some algebra. Each L_v = {±1} maps onto G, so
  omitting any one place buys one parity bit. Omitting ∞: the visible
  ramification set is any finite set of primes, odd exactly when a < 0
  and b < 0.
- The Brauer sum. Br(Q_p) = Q/Z and Br(R) = ½Z/Z (Frobenius). Omitting
  ∞ buys one bit, of 2-torsion alone: a central simple algebra of odd
  degree has visible invariants summing to 0. Omitting a prime p buys
  all of Q/Z.

The script budget.py::section_q rebuilds 200 valuation vectors on
the primes below 50 with ∏_v |x|_v = 1 exactly, and the partial-fraction
identity on 200 rationals and 200 families. budget.py::section_h
computes the symbols of the 1,444 pairs (a, b), a and b squarefree
with |a|, |b| ≤ 30, at ∞ and at the primes dividing 2ab, every other
symbol being 1. Reciprocity holds at all of them, so the visible set
is odd at exactly the 361 with a < 0 and b < 0, where the symbol at ∞
is −1. It also finds all
128 subsets of the seven primes dividing 510510 = 2·3·5·7·11·13·17 as
visible sets, with a a signed divisor of 510510 and |b| ≤ 200: every
subset of them is the finite ramification set of some algebra.

## The degree control
Tier: theorem.
Verifier: proof; budget.py::section_d.

Over F_q(t), L_P = Z at every place, s = Σ deg(P)·l_P, and G = Z. The
constraint is exact. Omitting a place of degree d buys dZ, so a
visible family is realized iff its degree sum is 0 mod d. The place at
infinity has degree 1 and buys all of Z, as ∞ buys all of R over Q.

Proof. Exactness is the principality of every degree-0 divisor on the
projective line: ∏ P^(a_P) with the place at infinity at −Σ a_P
deg P. The image of Z under l ↦ d·l is dZ, and the budget theorem
does the rest.

So the archimedean place's total budget at the product formula is what
every degree-1 place has over F_q(t), and there are q + 1 of those.
The theorem's form does not use being archimedean. The script reads
the place at infinity by degree, so the degree sums it prints over
F_2(t), 0 on 200 random rational functions, and its counts are the
theorem's arithmetic: with t² + t + 1 (d = 2) or t³ + t + 1 (d = 3)
omitted, the vectors on t, t + 1 and infinity with exponents in
[−2, 2] realized are the 63 and the 41 of 125 whose degree sum is 0
mod d. What it checks is its factorizer, which reads back all 343
vectors built on t, t + 1 and t² + t + 1 with exponents in [−3, 3].

## The rank face
Tier: theorem.
Verifier: proof; budget.py::section_r.

The same constraint read from the omitted side: which omitted terms
occur above the zero visible family. Over a number field K with unit
rank r, class group Cl and class number h = |Cl|, omit a finite set S_f
of finite places and every infinite place from the product formula,
and read the other finite places as 0. With S the set S_f with the
infinite places, the elements realized are the S-units O_S*, and

    1 → O* → O_S* → Z^(S_f) → Cl,   u ↦ (v_P(u)),   a ↦ [∏ P^(a_P)]

is exact. So each omitted finite place buys rank 1, rank O_S* = r + |S_f|,
and the valuation lattice has index in Z^(S_f) equal to the order of
the subgroup of Cl that the classes [P], P ∈ S_f, generate.

Proof, granting Dirichlet's unit theorem and the finiteness of Cl, as
the classical S-unit theorem does. The kernel of the valuation map is
the units. A vector a is the valuation vector of some u iff ∏
P^(a_P) = (u), that is iff its class is trivial, so the lattice is the
kernel of Z^(S_f) → Cl and its index is the order of the image. Cl is
finite, so the lattice has full rank.

Its H is the class group extended by the unit torus, the hyperplane
Σ z_σ = 0 in R^(r + 1), one coordinate z_σ per infinite place σ, modulo
log O* (the Arakelov class group), so the constraint is inexact unless
h = 1 and r = 0, as over Q. The
omitted set W, finite terms balanced by infinite ones, has a joint
kernel that maps onto the torus extended by the subgroup the classes [P]
generate. So the index is the part of Cl the omission absorbs, and it
depends on which places are omitted. The obstruction left to the visible
side is Cl modulo that subgroup, and the volume face below reads the
covolume of the S-units' logs. Over Q(√−5), with h = 2, the places over
2, 3, 11, 29 (ramified, split, inert, split) give ranks 1, 2, 1, 2 and
indices 2, 2, 1, 1. Over Q(√10), with h = 2, the places over 2, 3, 41
and the set {2, 41} give indices 2, 2, 1, 2. Over Q(√2), with h = 1,
every index is 1. The script finds S-units by search, which bounds each
index from above, and certifies each index 2 by a norm equation
x² − Dy² = ±NP with no integer solution, K = Q(√D), O_K = Z[√D] and
NP the norm of P: by exhaustion at D = −5, and modulo 5 at D = 10. At
a split prime one place suffices, its conjugate's class being the
inverse.

## The volume face
Tier: theorem.
Verifier: proof; budget.py::section_v.

Over a number field with regulator Reg, taken with the normalized
absolute values (|·|_σ = |·|² at a complex place), the S-regulator is

    Reg_S = Reg · [Z^(S_f) : lattice] · ∏_{P ∈ S_f} log NP,

each omitted place paying its own covolume log NP (NP = p^f for P over
the prime p with residue degree f, so p² at an inert p of a quadratic
field), with no cross term beyond the index:
the classical S-regulator formula, proved here in the block's terms.

Proof. Take a basis ε_1, …, ε_r, u_1, …, u_n of O_S* modulo torsion, the
ε_j fundamental units and n = |S_f|, with the valuation vectors
(v_P(u_i))_P a basis of the valuation lattice. Drop one infinite
place, and give the log matrix one column per remaining infinite
place σ and per P ∈ S_f. Its rows are
(log |ε_j|_σ, 0, …, 0) and (log |u_i|_σ, −v_P(u_i) log NP), so it is
block triangular, and its determinant is Reg times the lattice's
determinant times ∏ log NP.

The script evaluates the formula: over Q(√10), Reg = log(3 + √10) =
1.818446 and Reg_S = 34.764796 at the places over 2 and the two over
41. It builds the log matrix in the proof's block form from S-units
chosen to span a lattice of the certified index, so its ratio
Reg_S / (Reg ∏ log NP) equals that index by construction and prints
only the arithmetic; the index itself is certified by the rank face.
The index is where the class group reappears in the volume.

## The layer face
Tier: rule (the formula known; the excess proved when the units are
±1, and its bound at a conjugate pair proved; the census verified at
the 21 pairs of places over 3, 7, 17, 23 of Q(√2)).
Verifier: budget.py::section_l.

Omit less: keep every place, but cut the local units at P to the residue
layer (O/P)*. What the cut frees is the layer ∏ (O/P)*, reduced by the
global units' image and extended by Cl: the ray class group mod m = ∏ P,
of order h · ∏ |(O/P)*| / |im|, im the image of the global units in ∏
(O/P)* (the classical ray class number formula; Neukirch, Algebraic
Number Theory, 1999, ch. VI). The local factor is per place, by the CRT.
The units' image is not: im is one joint object, generated by at most r + 1
elements, and the excess ρ = ∏ |im_P| / |im| measures its failure to be
the product of the per-place images.  When the units are ±1 and n places
of odd residue characteristic, each im_P is {±1} and im is the diagonal,
so ρ = 2^(n − 1), unbounded in the place count. Over Q(√−5) the places
over 3 give ρ = 2, and one place over 7 added gives ρ = 4; the formula
then gives ray class numbers 4 and 24. Over Q(√2), with ε = 1 + √2 of
norm −1, 7 of the 21 pairs have ρ > 1. The places are named by the
residue they send √2 to: P7(3) · P23(5) has product 132 against a joint
image of 66, while P7(3) · P17(6) factors. The conjugate pairs over 7,
17 and 23 carry 3, 16 and 11; 16 and 11 are the two largest excesses,
and P3 against either place over 17 gives 4, above the pair over 7. At a
conjugate pair the norm ties the residues of ε at the two places, its
conjugate being ε′ = −ε⁻¹: an element of the joint image trivial at one
place is ±1 at the other, so the joint image is at most twice one
place's, and ρ is at least half the other's. So the layer's order is a
product over the places, and the units' image is not.
