# GATES — what a reader of words decides, and what it pays

The object: one channel F_p of a squarefree ring (LOGIC.md), its units a
cyclic group of order n = p − 1, and a reader holding L leaves x_1, … ,
x_L, written a, b or x where one or two are in play. The reader builds
words from the leaves with the ring operations of its **alphabet** and
reads each word through the ladder's gates (LOGIC.md#the-ladder),
G_m(w) = [w^m = 1] for m | n; a readout is any Boolean function of
finitely many gate bits. A shadow, a predicate on residues (LOGIC.md),
is read here on leaf tuples as the set of tuples where it holds, and the
reader decides it when some readout equals membership at every tuple. A
ring gate reads 1 exactly when every channel's gate does, so every claim
here is per channel. This page says which shadows each alphabet decides
and what a decision costs in gates and in word operations.

```
READER                   DECIDES EXACTLY                FIRST WALL
the pair ◇, □            two bits per leaf, and the     a AND NOT a: the
 (LOGIC)                 envelope they bound            floor stuck at 0
the ladder G_m           the profile (ord a,            relative order,
 (LOGIC, one leaf)       ord(1 − a))                    [ab = 1]
monomial words           a unit leaf tuple up to one    any shadow that
                         power map x_i ↦ x_i^u; at the  splits an orbit
                         gate count the orbit-cost
                         theorem prices, each orbit
a letter list, e.g.      the letter tuple up to one     the next letter:
 {a, b, 1 − a, 1 − b}    power map; the ±1-ratio lines  [a + b = 3], p = 7
                         among what that decides
the meadow closure       every shadow; [x = c] at one   none: the price
                         gate and a mask                moves into word
                                                        operations
```

A letter or term not defined above is defined in the section on this
page that answers its row, or in LOGIC.md for the first two rows: the
power map's u in GATES.md#the-word-orbits, the gate [x = c] and its mask
in GATES.md#the-meadow-closure.

## The word orbits
Tier: theorem.
Verifier: proof; gates.py::section_w.

Over the monomial alphabet (**MUL**, the product, and **INV**, the
meadow inverse, which on a unit leaf x_i is the power x_i^(n−1)) a word
is a monomial x^e = ∏ x_i^(e_i), e ∈ (Z/n)^L; in this section x is the
whole tuple (x_1, … , x_L). Two unit tuples x and x′ give every word the
same gate bits iff x′ = (x_1^u, … , x_L^u) for one unit u mod n. So a
shadow on unit tuples is decided iff it is constant on the orbits of
the maps x ↦ x^u.

Proof. The evaluation map ev_x: e ↦ x^e is a homomorphism
(Z/n)^L → F_p^×, and the bits G_1(x^e) are its kernel. Two tuples with
one kernel have images of equal order in a cyclic group, hence one image
H, and ev_x′ = β ∘ ev_x for an automorphism β of H. An automorphism of
a cyclic group is a power map y ↦ y^u with u prime to |H|, and u lifts
to a unit mod n, so x′_i = x_i^u for every i. Conversely x ↦ x^u
preserves every order.
An orbit-constant shadow is a union of finitely many orbits, each cut
out by finitely many gates.

This is an elementary fact about cyclic groups, and the G_1 bits alone
already carry it. What it adds over the one-leaf ladder is relative
position: with a primitive leaf a, the word bits pin b's discrete log to
the base a, so b is fixed once a is, and [ab = 1], which escapes every
one-leaf reader (LOGIC.md#the-ladders-reach), is the single gate
G_1(ab). Every word's discrete log (dlog) is a linear form in the
leaves' dlogs, so no single word's dlog is bilinear in them; a shadow
defined by a bilinear form is still decided when orbit-constant, as
[dlog a · dlog b ≡ 0 mod n] is. Three orders do not
suffice: in F_17 the dlog pairs (1, 2) and (1, 6) to the base 3,
(a, b) = (3, 9) and (3, 15), share (ord a, ord b, ord ab) = (16, 8, 16)
and lie in different orbits. The
two-leaf gates G_m(ab⁻¹) read [ord(a/b) | m], a family of congruences on
the units ordered as the divisors m are.

The script checks kernel classes against orbits on all of (Z/n)² for
eight n from 6 to 24 and on (Z/6)³ and (Z/8)³, and by field arithmetic
on every unit pair of F_p for p = 5, … , 23.

## The crystallographic skeleton
Tier: theorem.
Verifier: proof; gates.py::section_x.

Call a tuple stable for a shadow when its whole orbit lies inside it.
On a line a + b = c with c ≠ 0 and p ≥ 5 the stable unit points are
exactly:

```
c = 2      (1, 1)
c = −2     (−1, −1)
c = −1     (z, z⁻¹), ord z = 3     present iff p ≡ 1 mod 3
c = 1      (z, z⁻¹), ord z = 6     present iff p ≡ 1 mod 3
other c    none
```

The line c = 0 is the coset shadow [ab⁻¹ = −1] and wholly stable; the
order-4 pairs lie on it. Every line c ≠ 0 is undecided by monomial
words in the leaves at every p ≥ 5,
and every shadow is decided at p = 3.

Proof. The unit u = −1 sends a point of the line to one with
a⁻¹ + b⁻¹ = c, that is (a + b)/(ab) = c, so ab = 1 and a + a⁻¹ = c.
Stability under every unit then puts every primitive d-th root z,
d = ord a, on z + z⁻¹ = c, that is z² − cz + 1 = 0: φ(d) ≤ 2, so
d ∈ {1, 2, 3, 4, 6}, and d = 4 has trace 0. A line c ≠ 0 holds p − 2
unit points and at most two stable ones, so some orbit straddles it.
At p = 3 the only unit mod 2 is 1, and every orbit is a point.

The list is the crystallographic restriction's, by a counting twin of
its reason: over Q a primitive d-th root of unity has degree φ(d) and
one shared trace allows degree at most 2, while here F_p holds φ(d)
primitive d-th roots and one quadratic z² − cz + 1 holds at most two.
The script walks every orbit at every prime 5 ≤ p ≤ 97 and every c, and
finds exactly the table's stable points.

## The alphabet ladder
Tier: theorem.
Verifier: proof; gates.py::section_a.

Fix a finite list of letters, ring words in the leaves: the leaves
alone, or a and 1 − a, or a, b, 1 − a and 1 − b. Monomials in the
letters read the letter tuple up to one shared power map, every letter
raised to one u, by the word orbits applied to the letters, so on
tuples whose letters are units a letter list decides exactly the
shadows constant on letter-tuple orbits. (A letter reading 0 reads 0
in every word that holds it, so which letters vanish is read as well.)
More words over the same letters decide nothing new; only a new letter
can split an orbit.

The script checks, beside the theorem and as no part of it, that two
graded values of one leaf (neither 0 nor 1, LOGIC.md) give every
monomial in the letters {a, 1 − a} the same gate bits iff their letter
pairs share an orbit, at every prime p from 5 to 23; these letters
refine the one-leaf ladder's reading (ord a, ord(1 − a)) first at p = 11.
The letters {a, b, 1 − a, 1 − b} make gate shadows of the eight lines on
which a letter ratio is ±1 (a + b ∈ {0, 1, 2}, a − b ∈ {0, 1, −1}, and
2a = 1, 2b = 1 from one leaf each; the script checks the six joining
both leaves at every prime p from 5 to 19, each constant on four-letter
orbits); at p = 7 the pairs (3, 3) and (5, 5) share a four-letter orbit
(u = 5) and only the second lies on a + b = 3.

## The meadow closure
Tier: theorem.
Verifier: proof; gates.py::section_a.

With NOT applied to words as well as to letters, one graded leaf, a
unit other than 1, makes every constant, and every shadow is decided.
For a unit a ≠ 1,

```
NOT(a⁻¹) · (NOT a)⁻¹ · a = ((a − 1)/a) · (1/(1 − a)) · a = −1,
```

then 2 = NOT(−1) and c = NOT(−1 · (c − 1)) by induction, so for every
residue c a word w_c reads c at every unit other than 1. For graded c
and the leaf x, [x = c] = G_1(x · w_c(x)⁻¹): on {0, 1} every word reads
0 or 1, so the gate misfires only at x = 1, where every w_c built this
way reads 1 (the −1 word reads 0 there), and a second gate, NOT G_1(x),
masks it. On inputs where a second leaf
is graded, c built from it, the one gate suffices. [x = 0] and [x = 1]
are the pair's own bits (LOGIC.md#the-pair). A tuple is pinned leaf by
leaf, so every shadow of any number of leaves is a readout of these
gates. So the obstruction of the word orbits, a shadow that splits an
orbit, is a fact about alphabets that apply NOT only to letters: once
NOT nests freely, the power maps no longer commute with the words, and
no orbit survives.

The script checks the identity at every unit a ≠ 1, that the closure
of every graded residue is all of F_p, and the gate with its mask
against [x = c] at every x and every graded c, for p ≤ 31.

## The orbit-cost theorem
Tier: theorem.
Verifier: proof; gates.py::section_o.

In discrete-log coordinates the monomial gate shadows are exactly the
character kernels of V = (Z/n)^L. Let C = ⟨v⟩ have order d, let O be its
generators, v's multiples by the units, and let r(C) be the rank of V/C,
the least number of characters whose common kernel is C. With ω(d) the
number of primes dividing d, deciding O costs exactly r(C) + ω(d) gates,
and the proof holds for any finite abelian V.

Proof. A kernel K either contains C, a cut gate, or meets C in a proper
subgroup, a separator of restriction order ε = [C : C ∩ K]. All of O
shares one bit pattern, so a family decides O iff the atom holding O,
the points sharing its bits, is O itself: with τ cut gates meeting in D ⊇ C
and s separators, every point of D outside O lies in some separator's
kernel. A separator ψ kills a point when its kernel holds it: the point
ξ + uv of a coset exactly when uψ(v) = −ψ(ξ), a condition on u mod ε.

- Upper: r(C) cut gates meeting in C, and for each prime q | d the
  separator (d/q)χ₀, where χ₀(v) has order d; within C it kills uv
  iff q | u.
- Forced: the point qv of C needs a separator with ε | q, so each
  prime of d owns a separator of order exactly q: ω(d) of them.
- Duality: let t be a prime at which V/C reaches its rank r(C). The
  sequence 0 → D/C → V/C → V/D → 0 gives r(C) ≤ τ + ρ, where ρ is
  the t-rank of D/C. So it suffices that s ≥ ω(d) + ρ.
- Localization: take a coset ξ + C whose class has prime order ℓ, and
  let ℓξ = kv. A separator of order ε prime to ℓ kills only the class
  u ≡ −k/ℓ mod ε, so if ℓ ∤ d every killed class passes through one
  point u₀ and u₀ + 1 survives: D/C has torsion only at primes of d,
  and ρ = 0 unless t | d. If ℓ | d and ℓ ∤ k, a separator with ℓ | ε
  kills nothing (it would need ε | ℓu + k) and the rest pass through
  one point again. So k ≡ 0 mod ℓ, and ξ − (k/ℓ)v is a lift of order
  ℓ: D[ℓ] maps onto the ℓ-socle of D/C with kernel C[ℓ], and the
  lifts below are taken along a linear section of that map.
- Linearity: on the coset of such a lift ξ at t, ψ(ξ) has order
  dividing t. If t ∤ ε the killed class is u ≡ 0 mod ε, which holds
  no unit; if t | ε it is u ≡ u₁ mod ε with u₁ a multiple of ε/t,
  which holds a unit only when ε = t. So only separators of order t
  reach the unit positions, and each kills one class mod t, a linear
  functional of the socle point. The units mod d meet every nonzero
  class mod t, so each nonzero socle point needs every nonzero
  value.
- Rigidity: functionals spanning fewer than ρ dimensions leave a nonzero
  point in their common kernel, and ρ independent ones form a basis with
  a point on which all of them read −1, which misses the value 1 when t
  is odd. At t = 2 the positions 2u, u a unit, are killed only by an
  order-2 separator reading 0 or by one of order 4: either the order-2
  ones take both values, ρ + 1 of them, or an order-4 separator stands
  beside them; an order-4 separator kills only even positions, so the
  order-2 ones must still give the value 1, ρ of them. Either way the
  prime t holds at least ρ + 1 separators (at ρ = 0, the forced one).

The other primes of d hold ω(d) − 1 forced separators of other orders,
so s ≥ ω(d) + ρ; if t ∤ d, ρ = 0 and the forced ones suffice. The
cost is at least r(C) + ω(d).

One leaf, V of rank 1: [ord x = d] costs ω(d) + 1, or ω(n) at
d = n, and a divisor filter [ord x | m] costs 1, or 0 at m = n, where
it is constant. At two leaves
r(C) = 1 iff d = n, and 2 otherwise. So the order-6 residue pair on
a + b = 1, the skeleton's, costs 3 gates at p = 7, where d = n, and 4
at p = 13. The script checks the one-leaf law at 54 targets over n = 6,
12, 30, 60 and 360. It finds r(C) two ways at ten orbits in groups of
rank two to four, seven of them (Z/n)^L and three mixed for the general
V, Z/6 × (Z/3)², Z/12 × (Z/2)² and Z/24 × (Z/2)², with rank-3 cuts and
separators of order 4 and 8. It runs the
upper construction at the law and fails every smaller family, 457,450
of them at the primitive orbit of a pair at p = 31 (V = (Z/30)²), and
checks the rigidity bound by exhaustion at five (t, rank) pairs.

## The height floor
Tier: theorem.
Verifier: proof; gates.py::section_h.

At the meadow level [x = c] costs one gate and its mask, so the
price moves into word operations. Let the height h_p(c) be the fewest
operations (MUL, INV, NOT) in a one-leaf word reading c at every unit
other than 1. Then

```
max_c h_p(c)  ≥  f_p = min{t : W(0) + … + W(t) ≥ p − 2},
W(0) = 1,  W(t) = 2W(t − 1) + Σ_{i+j=t−1} W(i)W(j),
```

which grows without bound. W(t) counts the words of cost exactly t
whatever p is, and each graded constant needs a word of its own. The
route of the meadow closure decides [x = c] with h_p(c) + 2 operations,
and h_p(−1) ≤ 6 by its identity.

The floor is a count, logarithmic in p: W(t) ≥ 3W(t − 1), and W grows no
faster than a constant times (4 + 2√3)^t, the rate set by the
singularity of its generating function G = 1 + 2yG + yG² at y = 1 − √3/2.
It is loose at the two primes whose exact heights were computed: at p = 5
and 7 they reach 7 and 11 against floors 1 and 2, and h_p(−1) = 6 at
both.
