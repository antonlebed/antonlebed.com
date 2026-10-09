# BINDING — what multiplication keeps of a code, and what a sum costs

The object: a finite product of fields R = K_1 × ⋯ × K_k (a squarefree
Z/M, or F_q[x]/f over the field F_q of q elements, with f squarefree and
q a power of the prime p) holding symbols as words, the distance between
two words being the number of channels where they differ. Multiplication
by a unit is **binding**; **bundling** is the addition of bound items in
the **carrier**, the ring that holds them; a **dictionary** is a set of
words. This page says which dictionaries each operation keeps, proves
that the distance which lets a dictionary correct errors forbids reading
a bundle back by unbinding and decoding, and then asks what a store that
bundles anyway, a bipolar vector-symbolic store of D coordinates read
back by correlation, spends to survive the sum. There the carrier may be
any ring, Z/3^P and F_3[x]/x^P for P ≥ 1 among them. The bundle's noise
is a walk on the prime ring Z/c of the carrier's characteristic c, so
the capacity of a bipolar store is capped by c: Z's quotients reach
every c, and F_q[x]'s stay at p.

```
OPERATION          EFFECT                          OVER F_q[x] INSTEAD
binding            the dictionaries closed under   the same
                    products: every group code of
                    the index ring, its distance
addition over Z/M  only the ideals: distance 1     the F_p-linear codes,
                                                    Reed–Solomon (f split)
                                                    at n − ℓ + 1 among them
two-item bundle    no decoder of radius < d        the same
 (C ∋ 0, items ≠ 0) returns an item unbound
                    by its own role
bipolar bundle,    at most ~c² log(Dc) items at     ~p² log(Dp) items
 m items            characteristic c; Z's capacity   or fewer, at every
                    once c > 2m                      precision
```

A letter not defined above is defined in the section that answers its
row: n and ℓ in BINDING.md#the-additive-twin, the dictionary C and its
distance d in BINDING.md#the-superposition-wall.

## The dictionary criterion
Tier: criterion.
Verifier: proof; binding.py::section_d.

A nonempty set of units of R is closed under multiplication by its own
members iff it is a subgroup of the unit group U(R). Through a primitive
root per channel, U(R) is isomorphic to the additive group of the index
ring ∏ Z/(|K_i| − 1), and two units differ at a channel iff their
indices differ there. So a dictionary of units closed under its own
products is a group code in the index ring at the same distance, every
group code there is one, and the distance is the least weight of a
nonzero index vector. Binding by a unit keeps every distance, a ↦ ua + w
for a unit u and any w in R is an isometry, and a product is wrong,
different from the product of the intended words, only at channels
where some factor is wrong.

Proof. A finite set of units closed under multiplication is a subgroup,
since a has finite order and so a⁻¹ = a^(ord a − 1). The index map is a
group isomorphism channel by channel. Multiplication by a unit is a
bijection within each channel, so ua and ub differ at exactly the
channels where a and b do. For the last clause, if a and b are right at
a channel then so is ab.

Coding theory imports through this. The script finds all 54 subgroups of
U(210), checks the 53 nontrivial ones against their least index weights,
and checks three instances. The sign hypercube: over the seven primes 3
to 19 the words ±1 per channel make a binary index at every channel, so
a binary linear code is a dictionary, and Hamming [7, 4, 3] gives 16
words at distance 3, each corrected from any single wrong channel. The
octave: over the seven primes 17, 41, 73, 89, 97, 113, 137, each ≡ 1 mod
8, an element h of order 8 in every channel gives {h^j} with all 28
pairs at distance 7. A cyclic group of units need not carry this: at
Z/510510, the primes 2 to 17, a unit z that is a primitive root at every
odd channel has order 240 and its group has distance 1, since its
channel orders are unequal and z⁶⁰ is 1 at every channel but 17.

## The additive twin
Tier: theorem.
Verifier: proof; binding.py::section_d.

Over Z/M every dictionary closed under addition, other than {0}, has
distance 1. Over F_q[x]/f they are the F_p-linear codes, and with f a
product of n distinct linear factors (so n ≤ q), the residues of the
polynomials of degree below ℓ, 1 ≤ ℓ ≤ n, form an additively closed
dictionary at distance n − ℓ + 1, the Reed–Solomon code
(Reed and Solomon, 1960).

Proof. A nonempty additively closed subset of a finite group is a
subgroup, as in the criterion. The additive group of Z/M is cyclic, so
such a subgroup is eZ/M for some e | M; that of F_q[x]/f is a vector
space over F_p, whose subgroups are its subspaces. When e < M take a
prime t dividing M/e, so e | M/t and eZ/M holds M/t, which is 0 at every
channel but t's. Over F_q[x] the residues of a at the n roots are its
values there, and degree obeys deg(a + b) ≤ max(deg a, deg b); a nonzero
a of degree below ℓ has fewer than ℓ roots, so it is nonzero at
n − ℓ + 1 or more of the n; the product of x − α over ℓ − 1 of the roots
α attains it.

The inequality is the ultrametric one at the place at infinity. The
integers below a bound B, which is what the residue code of
TOWER.md#the-residue-codes-distance keeps, are not closed under the sum:
(B − 1) + 1 = B, since |a + b| ≤ |a| + |b| bounds a sum of two words
below B only by 2B, where a maximum would keep it below B. The script
checks the 46 nonzero additive subgroups of Z/210 and Z/2310, and the
distance of Reed–Solomon over F_7 for ℓ = 1 to 6 over every word;
closure holds by construction there, the words being a linear map's
image.

## The superposition wall
Tier: theorem.
Verifier: proof; binding.py::section_w.

Let a dictionary C contain 0, with distance d, let a_1 and a_2 lie in C,
and let ρ_1 and ρ_2 be units. A decoder of radius r returns the
codewords within r channels of its input. Unbinding the bundle
ρ_1 a_1 + ρ_2 a_2 by ρ_1 never returns a_1 under a decoder of radius
r < d when a_2 ≠ 0. The direct sum avoids it at a price in channels: items
multiplied by the idempotents e_S of disjoint channel sets are each
returned exactly on their own set, and only there.

Proof. The unbound word is a_1 + u a_2 with u = ρ_2 ρ_1⁻¹ a unit, and it
differs from a_1 exactly on the support of a_2. Since a_2 and 0 are both
in C, that support has at least d channels (for units 0 is not needed: a
unit is nonzero at every channel, and there are at least d channels), so
the word lies outside a_1's ball of radius r. For the cure, e_S is 1 on
S and 0 elsewhere, so the bundle Σ_j e_{S_j} a_j agrees with a_j on S_j.

The distance that guarantees the correction is what forbids that readout
of the sum, and no step uses an absolute value, the archimedean one or
any other: the proof only counts channels. With the roles known the
bundle is not lost; only unbinding and decoding fail. The script runs
2,000 bundles of the residue code at Z/510510 (data below 210, distance
4) under roles drawn from all its units, decoded at radius 3, with least
noise weight 4, and 2,000 of Reed–Solomon [7, 3, 5] over F_7 at radius
4, with least noise weight 5; neither decoder returns a_1 once. It also
runs 1,000 direct sums at Z/510510 on the channel sets {2, 3, 5},
{7, 11} and {13, 17}, and all are exact.

## The mixing bound
Tier: theorem.
Verifier: proof; binding.py::section_m, binding.py::section_c.

A bipolar store holds D coordinates. Each item is a ±1 vector bound by a
±1 role, and m items are added in a carrier, its additive group G. On
unbinding the true role, each coordinate holds the true item's value
plus the m − 1 step ±1 walk. The model: the other m − 1 items and their
roles are independent uniform ±1 vectors, drawn apart from the N
candidates, and the candidates are equally likely. A readout guesses
the item from the unbound word. If G is a finite abelian group, any
readout then succeeds with probability at most

```
1/N + (D/2) · sqrt(|G| − 1) · λ^(m − 1),
```

where λ is the largest |μ̂(χ)| over nontrivial characters of the step
law μ; the bound is empty, λ = 1, when a nontrivial character is
constant on the steps' support, as on ±1 when g is even. For ±1 on a
cyclic carrier, G = Z/g with g odd, λ = cos(π/g). With g even the bound
holds with |G| − 1 replaced by g − 2 and λ by cos(2π/g), since every
hypothesis then puts each coordinate on the same parity coset. The
capacity, the most items a store retrieves at a fixed success rate above
1/N, is at most of order g² log(Dg).

Proof. Write η for the uniform law and let the walk take m − 1 steps.
The upper bound lemma of Diaconis and Shahshahani (1981) gives

```
4‖μ^(*(m−1)) − η‖² ≤ Σ_{χ ≠ 1} |μ̂(χ)|^(2(m−1)) ≤ (|G| − 1) λ^(2(m−1)).
```

Under each hypothesis the bundle's law is a product over the D
coordinates, of factors each within ‖μ^(*(m−1)) − η‖ of uniform. Total
variation is subadditive over products, so every hypothesis's law lies
within D · ‖μ^(*(m−1)) − η‖ of η^D. That law does not depend on the
hypothesis, so the N decision regions share at most mass 1 under it.
With g even, a coordinate is an odd item value plus m − 1 odd steps, so
under every hypothesis it lies on the coset of parity m, and the
reference law is uniform there. The walk and the uniform law η′ on its
own coset, of parity m − 1, have equal transforms at j = 0 and j = g/2,
so Cauchy–Schwarz over that coset's g/2 points and Plancherel give

```
4‖μ^(*(m−1)) − η′‖² ≤ ½ Σ_{j ∉ {0, g/2}} cos(2πj/g)^(2(m−1))
                   ≤ ½ (g − 2) cos(2π/g)^(2(m−1)),
```

within the stated bound. A store whose other items are drawn from the
N candidates is outside the model.

The script computes the walk's law exactly as integer path counts, for
g = 3, 5, 7, 9, 27, 81 and walks of at most 60 steps, and for g = 4, 8,
16, 32, 64 against the coset's uniform law. Over the odd g the largest
log ratio of total variation to its bound is −0.059, at g = 3, where
that bound is nearly tight, and it falls to −1.522 at g = 81; the
success bound, 1/N plus D times it, is loose: where it falls below 1,
the MAP readout's success above chance in the capacity sweep
(BINDING.md#the-capacity-sweep) prints as 0.01 at two decimals.

## The characteristic cap
Tier: theorem.
Verifier: proof; binding.py::section_c.

Let the carrier have finite characteristic c > 0, the additive order of
1. A ±1 bundle lives in the prime ring Z/c, so the mixing bound holds
with g = c whatever the carrier's size, and when c > 2m the carrier
reads a bundle of m items exactly as Z does; when c is odd, c > m
already gives every candidate Z's likelihood. Every nonzero quotient of
F_q[x], read to any number of digits at any place, has c = p (at p = 2
the two signs coincide and a bipolar store holds nothing); Z's quotients
reach every c.

Proof. A sum of ±1's is an element of the prime ring, and every
readout's law is a law on it. Over Z the unbound coordinate lies in
[−m, m], and 2m + 1 consecutive integers stay distinct mod c once
c > 2m, so every candidate's likelihood, and every readout, agrees
with Z's. A likelihood reads the m − 1 step walk at a bundle value
less a candidate; that value and every point of the walk's support
share a parity and lie within 2m of each other, so they differ by 2j
with |j| ≤ m, and an odd c divides 2j only when it divides j. So for
odd c > m no two of them meet mod c, though the centred lift that the
correlation readout reads still wraps.

## The capacity sweep
Tier: pattern (toy scale: D = 1,000, N = 100, 200 trials per m).
Verifier: binding.py::section_c.

The capacity m* is the largest m on the grid 1, 2, 3, 4, 6, 8, 12, 16,
24, 32, 48, 64, 96, 128 that retrieves at 90% or more; success need not
be monotone in m, so a smaller m can fail below it. The maximum a
posteriori (**MAP**) readout scores each candidate v by Σ log ν(b − v),
b the unbound word, under the carrier's own walk law ν = μ^(*(m−1)). The
correlation readout, the standard one for such stores, scores each
candidate by its dot product with the unbound word read in the centred
lift of Z/c to (−c/2, c/2]. The F_3[x]/x^P rows are F_3's by the
characteristic cap, fixed by the theorem rather than evidence for it:

```
CARRIER                       c         MAP m*          CORRELATION m*
Z                             0         64              64
Z/3^P,       P = 1, 2, 3, 4   3^P       4, 16, 64, 64   3, 8, 32, 64
F_3[x]/x^P,  P = 1, 2, 3, 4   3         4, 4, 4, 4      3, 3, 3, 3
F_p,  p = 3, 5, 7, 11, 13     p         4, 8, 16, 24, 32   3, 6, 3, 8, 16
```

Capacity grows with c alike on Z/3^P, whose addition carries between its
P base-3 digits, and on F_p, one digit with no carry, though the two
families share a c only at 3; every finite arm's MAP m* here lies past
the wrap at c/2. The mixing bound (BINDING.md#the-mixing-bound) permits
retrieval of m items once c exceeds the order of √(m / log(Dc)); it does
not explain the capacities seen: solved for 90%, it permits m up to 10,
34, 70, 181 and 257 on F_p for p = 3, 5, 7, 11, 13, where the sweep
measures 4, 8, 16, 24 and 32. On Z the MAP weight at the value t of one
coordinate of the unbound word is ½ log((m + t)/(m − t)), half the log
of a ratio of adjacent binomial coefficients: monotone in t and near t/m
while |t| is well below m, and Z's two readouts' rows agree. Where the
characteristic cap gives every likelihood Z's, the residue fixes the
coordinate's value and the MAP readout makes Z's choices: Z/81's MAP
weights equal Z's at every value at m = 48 and 64, as Z/130's do at
m = 64, where c > 2m. Every other finite arm's capacity edge here has c
odd and m even, and c odd makes a residue name one value t in (−c, c) of
the parity of m. The MAP score is unchanged by a positive factor on its
weights, so each edge's weight is compared with Z's times the factor
that makes the two equal at t = 2; agreement at t = 2 is then by
construction, and only the lifts past it test anything. Within 1%, the
weight keeps Z's shape one lift further, to |t| ≤ 4, on Z/9 at m = 16,
F_11 at m = 24 and F_13 at m = 32, parting at t = 6, and to 20 on Z/27
at m = 64, the factor within 0.01 of 1 at all four; a coordinate's sum
over Z lies past that radius with probability 0.210, 0.307, 0.377 and
0.008. On F_5 at m = 8 and F_7 at m = 16 it parts at t = 4
(factors 0.91 and 0.93), and on F_3 at m = 4, whose only nonzero lifts
are ±2, any odd weight is a multiple of Z's, so nothing is decided. So,
among the edges with c ≤ m, only at Z/27's does the agreement reach past
almost every sum; at the others, within 1%, Z's shape survives at most
one lift past t = 2. The radii are the 1% band's: an absolute band of
0.01 gives 0, 0, 2, 4, 6, 6 and 20 at c = 3, 5, 7, 9, 11, 13, 27. The
cap is set in the prime ring Z/c, where every readout's law lives: an
invariant of the characteristic, whatever the place. That is why
F_q[x]'s cap on a bipolar store stays at p as P grows, where Z/3^P's
rises with its size. A wrap reverses the correlation readout's sign: on
F_3 at m = 2 the true item's expected correlation per coordinate is −½,
so it retrieves at rate 0 where the MAP readout retrieves at rate 1, and
yet retrieves at m = 3, which is F_3's m*. On F_7 the correlation
readout retrieves at 0.42 at m = 4 and at chance or below, 0.00 to 0.01,
from m = 6 on, where F_5 still retrieves at 0.97 at m = 6: that is why
its column is not monotone in p.
