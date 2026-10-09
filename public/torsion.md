# TORSION — which torsion a curve holds, by monomials and by degree

The object: a plane curve f(x, y) = 0 over F_p and a unit pair
P = (a, b) whose order is m = lcm(ord a, ord b). Its orbit is the pairs
(a^u, b^u), u a unit mod m (the orbits of GATES.md#the-word-orbits). The
curve holds the orbit **stably** when every pair of it lies on the
curve. Which orders m a curve can hold stably in the codeword species
defined below, counted first by its monomials s and then by its degree
D, is a fact about cyclic codes: the cyclic code (Φ_m) of length m, its
minimum distance d, and its low-weight words.

```
SOME CURVE WITH            HOLDS CODEWORD ORDER m   BECAUSE
s monomials                iff q_min(m) ≤ s         d(Φ_m) = q_min(m)
degree D, m even           at every D ≥ 1           the antipodal word
degree D, m = q odd prime  iff D ≥ κ(q) = Θ(√q)     the triangle covers Z/q
degree D, other odd m      iff D ≥ q_min(m) − 1     the gon; three exclusions
```

## The fiber criterion
Tier: criterion.
Verifier: proof; torsion.py::section_f.

Fix θ of order m and write P = (θ^A, θ^B), gcd(A, B, m) = 1. The
monomial x^i y^j takes the value θ^(Ai + Bj), so f(a^t, b^t) = F(θ^t),
where the **collected fiber**

```
F(T) = Σ_e c_e T^e  in F_p[T]/(T^m − 1),
c_e = the sum of f's coefficients over the monomials with Ai + Bj ≡ e.
```

The orbit is held iff Φ_m divides F. Either F = 0, and f vanishes on
the whole group ⟨P⟩, the **group species**. Or F is a nonzero codeword of
(Φ_m), the **codeword species**.

Proof. As u runs over the units mod m, θ^u runs over the primitive
m-th roots, which are the roots of Φ_m and distinct in F_p. And F, of
degree below m, vanishes at every m-th root iff it is 0.

The group species is the finite shadow of Lang's theorem on torsion
points of subvarieties of tori (Lang 1965, the proof credited there to
Ihara, Serre and Tate): whole cyclic groups lie on the curve. What
follows concerns the codeword species, and the table's q_min(m), κ(q),
antipodal word, gon and three exclusions are bound in the blocks below,
the last three at TORSION.md#the-menu-law, TORSION.md#the-gon-theorem
and TORSION.md#the-realizability-law.

The script checks the criterion against brute force at every unit pair
of F_p, p = 7, 11, 13, 31. It runs a battery of every line x + y = η,
the pentagon conic below, x²y − 1, xy + 1, x⁸ + x⁴ + 1 and 24 random
curves of degree up to 4, 64,164 tests in all. The lines give back the
skeleton of GATES.md#the-crystallographic-skeleton.

## The menu law
Tier: theorem.
Verifier: proof; torsion.py::section_m.

For m > 1 the minimum distance of (Φ_m) is q_min(m), the least prime
factor of m, over every field of characteristic prime to m that holds a
primitive m-th root of unity. Weight 1 never occurs, and weight 2 occurs
iff m is even. So some curve with at most s monomials holds codeword
torsion of order m iff q_min(m) ≤ s.

Proof. Lower bound, the BCH bound: the units mod m hold q_min − 1
consecutive integers. Take t₀ ≡ 1 modulo every prime r | m; then
t₀ + k ≡ 1 + k is nonzero mod r for k ≤ q_min − 2. A nonzero sum of
w ≤ q_min − 1 terms c_e θ^(et) cannot vanish at w consecutive t, since
the determinant is Vandermonde in the distinct nodes θ^e. Upper bound:
with q = q_min(m), the **q-gon**

```
(T^m − 1)/(T^(m/q) − 1) = 1 + T^(m/q) + … + T^((q−1)m/q)
```

vanishes at every primitive root, because θ^(m/q) is a primitive q-th
root. At q = 2 it is the antipodal word 1 + T^(m/2). A single term T^e
vanishes nowhere. The one-variable curve Σ_(h<q) x^(hm/q) realizes the
law with q monomials.

The lower half is the BCH bound, known. What the law adds is its reading
on curves: the monomial count admits torsion by least prime, and even
orders are admitted at every size. A line has s = 3, so codeword torsion
on lines has q_min(m) ≤ 3. The lines x + y = η with η ≠ 0 narrow this to
the orders 2, 3 and 6, the crystallographic list {1, 2, 3, 4, 6} less
order 1, which is the group species, and order 4, which needs η = 0
(GATES.md#the-crystallographic-skeleton, at every p ≥ 5; the script's
control at p = 7, 11, 13, 31), while the line x + y = 0 holds every even
order, the pairs (θ, −θ); by the realizability law the codeword orders
some line holds are the even m and 3. The script checks the run of units
at every m ≤ 3000, the q-gon at m ≤ 60, exhausts the supports below
q_min at m = 9, 15, 21, 25, 35, 45, and finds weight 2 at exactly the
even m ≤ 30.

## The pentagon conic
Tier: theorem.
Verifier: proof; torsion.py::section_p.

At every prime p ≡ 1 mod 5 the conic y² + xy + x + y + 1 = 0 holds
exactly one stable orbit of order 5, the pairs (θ^u, θ^(2u)), and it is
of the codeword species. So a conic holds an order no line holds, at
five monomials, the fewest the menu law allows for order 5.

Proof. The exponents are {0, A, B, A + B, 2B}, and (Φ_5) is the line of
the all-ones word, so the orbit is held iff the five exponents are all
of Z/5. Collisions would give coefficient sums of two to five 1s, which
are nonzero at p > 5 and so never the group species; at B ≡ 0 the
exponents collide. Otherwise scaling (A, B) jointly by a unit to B = 1
leaves {0, A, 1, A + 1, 2}, which is Z/5 only at A = 3, and
(3, 1) = 3·(1, 2) mod 5. The script finds this one orbit at p = 11, 31,
41, 61.

## The exponent reduction
Tier: criterion.
Verifier: proof; torsion.py::section_r.

With m dividing p − 1, so that orbits of order m exist, a curve of
degree at most D holds a codeword-species orbit of order m iff some
(A, B) with gcd(A, B, m) = 1 has a nonzero (Φ_m)-codeword supported in the
**triangle exponent set**

```
E(A, B, D) = {Ai + Bj mod m : i, j ≥ 0, i + j ≤ D}.
```

D_min(m) is the least D at which this holds.

Proof. The collected fiber of a degree-D curve lies in E(A, B, D). Any
vector on E is the fiber of a curve with one monomial per exponent.
Joint scaling by a unit and the swap of x and y preserve the question,
so the script works over scaling classes, calling a class (A, B) live
when E(A, B, D) carries a nonzero codeword. It checks the reduction at
degree 1 by brute force over every line and every pair of order m at
(m, p) = (3, 7) and (9, 19). The first finds 12 held (line, pair) incidences
of the codeword species, the six lines μ(1 + x + y), μ ≠ 0, on the pairs
(2, 4) and (4, 2), beside 36 of the group species, and the pairs' one
scaling class, (1, 2), is the one live class. The second finds no
incidence of the codeword species and no live class.

## The triangle cover number
Tier: rule (verified q ≤ 149; the bracket proved).
Verifier: torsion.py::section_k.

At an odd prime m = q the code (Φ_q) is the line of the all-ones word,
so a codeword on E needs E = Z/q, and scaling, after the swap when
A ≡ 0, makes A = 1. So D_min(q) = κ(q), the least D such that
{i + Bj : i + j ≤ D} covers Z/q for some B. That is the least diameter
of a directed double-loop network on Z/q with steps 1 and B. Its bracket:

```
(κ + 1)(κ + 2)/2 ≥ q,        κ(q) ≤ 2⌈√q⌉ − 1,        κ(q) ≤ q − 2.
```

The first is a count. The second uses B = ⌈√q⌉ and D = 2B − 1, whose
rows [jB, jB + D − j], j ≤ B, chain from 0 to B² + B − 1. The third
uses B = 2 and D = q − 2, whose first two rows are [0, q − 2] and
[2, q − 1]. The network literature's lower bound ⌈√(3q)⌉ − 2 is the
sharper floor (Wong and Coppersmith 1974 for steps 1 and B; Fiol,
Yebra, Alegre and Valero 1987 for any steps). The script computes κ
at the 34 odd primes up to 149:

```
q   3  5  7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
κ   1  2  3  4  5  6  6  7  8  8  9 10 10 10 12 12 12
q  67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149
κ  14 13 14 14 14 16 16  16  17  16  17  17  18  18  20  19  20
```

28 of the 34 sit on the network floor, and 53, 67, 73, 89, 103 and 137
sit one above it. κ is not monotone: κ(107) = 16 < 17 = κ(103). At
q = 5, 7, 11, 13 a direct search for a nonzero codeword on E agrees
with the cover on both sides of κ(q).

## The class capacity
Tier: theorem.
Verifier: proof; torsion.py::section_l.

Let gcd(A, B, m) = 1 and D ≤ q_min(m) − 2. For every divisor m″ > 1 of
m, each class of Ai + Bj modulo m″ holds at most D + 1 points (i, j) of
the degree-D triangle.

Proof. Every prime of m″ exceeds D + 1. If A is a unit mod m″, each
j ≤ D fixes i mod m″, and m″ > D leaves at most one i. Otherwise a prime
r | gcd(A, m″) cannot divide B, so Bj fixes j mod r, at most one j
below r. With j fixed, the solutions i form one progression of step
m″/gcd(A, m″), which is 1 (one row of at most D + 1 points) or exceeds
D (one point).

## The squared-prime exclusion
Tier: theorem.
Verifier: proof; torsion.py::section_l.

If q = q_min(m) and q² | m, no nonzero (Φ_m)-codeword lies in any
E(A, B, D) with gcd(A, B, m) = 1 and D ≤ q − 2; at a larger gcd,
E(3, 6, 1) = {0, 3, 6} at m = 9 carries Φ₉ itself.

Proof. Write m = Q·m′ with Q = q^k the q-part, k ≥ 2, and slice the
codeword c by the class x mod Q into words γ_x on Z/m′. For each unit u
of Z/m′, the vector x ↦ γ̂_x(u) of transforms is a (Φ_Q)-codeword, and
the words of (Φ_Q) are those invariant under x ↦ x + Q/q. So
γ_x − γ_(x+Q/q) lies in (Φ_m′). Both slices sit in the class of x mod q,
because q divides Q/q, and that class holds at most q − 1 exponents.
Every prime of m′ exceeds q, so this is below the menu law's distance,
and the difference is 0 (at m′ = 1 the code (Φ₁) is 0 itself). Then c is
invariant under translation by the order-q element, so its support is a
union of cosets of the order-q subgroup ⟨m/q⟩. Each coset lies in one
class mod q: q points against a capacity of q − 1. So c = 0. At m′ = 1
and odd q this is the case m = q^k, k ≥ 2, of the realizability law's
last row.

## The coverage cap
Tier: rule (proved: analytic for ℓ ≥ 213, exhaustive at every prime
below).
Verifier: coverage_cap.py::section_y, coverage_cap.py::section_o,
coverage_cap.py::section_l, coverage_cap.py::section_x,
coverage_cap.py::section_f.

For a prime ℓ, a multiplier B ≢ 0, 1 mod ℓ and 0 ≤ D ≤ ℓ − 2, every
class w mod ℓ holds at most ⌊D/2⌋ + 1 points (i, j) of the degree-D
triangle with i + Bj ≡ w. At B = 1 the class D holds D + 1.

The proof is analytic for ℓ ≥ 213 and exhaustive below. Put U = D − j
and V = i: the class i + Bj ≡ w becomes V ≡ w − BD + BU, so the proof
reads the count as a translate of the lattice {(U, V) : V ≡ BU mod ℓ},
of determinant ℓ, inside the triangle 0 ≤ V ≤ U ≤ D. Three exact
symmetries hold, the involutions B ↔ 1 − B and time reversal B ↔ 1/B,
and a duality carrying D to ℓ − 3 − D with the cap transferred exactly,
beside one exact count, equicoverage: (ℓ − 1)/2 at every class when
D = ℓ − 2. So only D ≤ (ℓ − 3)/2 needs proving, and the maximum is
constant on the orbit of B under the group of six maps the two
involutions generate.

With b = min(B, ℓ + 1 − B), write a point of the class as
i + bj = w + Wℓ; the points sharing one **wrap number** W are at most
⌊D/b⌋ + 1, and the wrap numbers span at most bD/ℓ, which settles bD < ℓ
and every D with D² < ℓ. Above that, the points lie on lines along a
shortest lattice vector (t′, s′), t′ ≥ 1, of length λ, in the frame
(U, V) of the triangle 0 ≤ V ≤ U ≤ D, which gives two bounds. For λ ≥ 7,
a unimodal-sum bound using Brunn's concavity of chords gives
D²/(2ℓ) + √2·D/λ + √2·λD/ℓ + 1. For λ < 7, n consecutive lattice points
along the vector inside the triangle satisfy (n − 1)·ρ ≤ D, with ρ = s′,
t′ or t′ − s′ as s′ > t′, 0 ≤ s′ ≤ t′ or s′ < 0, which gives
D²/(2ℓ) + √2·λD/ℓ + ⌊D/ρ⌋ + 1. The directions with ρ ≤ 4 are the orbits of
2, 3 and 4: the orbit of 2 is settled by one wrap number, and the others
by the two wrap numbers that carry points at B = −2 and −3, which give
D/3 + 2, below the cap for D ≥ 10, the smaller D falling under D² < ℓ.
Every case lands below the cap at ℓ ≥ 213. The script checks each
symmetry exactly at the primes from 5 to 47 (equicoverage at every
modulus from 5 to 79), and against brute force the product of the
wrap-number bounds at the primes from 5 to 103, the two lattice bounds
at ℓ = 211 and 401, three D each, and the run count (n − 1)·ρ ≤ D on
54,240 random runs; the unimodal-sum inequality beneath both lattice
bounds is proved, with no test of its own. It runs the assembled case
split at every B and every D ≤ (ℓ − 3)/2 for the primes 213 ≤ ℓ ≤ 449
and ℓ = 1009, the cases D² < ℓ and the orbit of 2 left to their proofs,
and the cap itself at every prime ℓ ≤ 211, every D and every B, 596,366
triples. Among the 48,172 triples the symmetries and the wrap-number
counts leave to brute force, equality holds only at
(ℓ, D, B) = (13, 5, 4) and (13, 5, 10).

## The two-prime majority
Tier: theorem.
Verifier: proof; torsion.py::section_t.

Let m = qq′ with q < q′ odd primes, gcd(A, B, m) = 1 and D ≤ q − 2.
Suppose E(A, B, D) either misses a class mod q′ or holds at most
(q − 1)/2 exponents in every class mod q′. Then no nonzero
(Φ_m)-codeword lies in it. The coverage cap supplies the second
hypothesis whenever A is a unit mod q′ and B/A ≢ 0, 1, since
⌊(q − 2)/2⌋ + 1 = (q − 1)/2. At A ≡ 0, B ≡ 0 or B ≡ A mod q′, the
residues mod q′ take at most D + 1 < q′ values, and E misses a class.

Proof. Let c be a (Φ_m)-codeword supported in E, a function of e mod m.
Its transform lies on the non-units, the multiples of q or of q′. By the
CRT this means c(e₁, e₂) = α(e₁) + γ(e₂), with
e₁ = e mod q and e₂ = e mod q′. If E misses the class e₂ = σ, then
α(e₁) = −γ(σ) at every e₁, so α is a constant ν. Any e₂ with
ν + γ(e₂) ≠ 0 then fills its whole class mod q′, q cells against a class
capacity of q − 1. Otherwise, for each e₂, at most (q − 1)/2 of the q
values e₁ have α(e₁) ≠ −γ(e₂). So −γ(e₂) is α's strict-majority value ξ,
one ξ for every e₂. Then c = α(e₁) − ξ, and any e₁ with α(e₁) ≠ ξ fills
its whole class mod q, q′ cells against q − 1. In both cases c = 0.

At m = 143 and 221 the script finds every scaling class in one of the
two cases: 19 and 22 classes miss a residue, 67 and 106 are capped.

## The gon theorem
Tier: theorem.
Verifier: proof; torsion.py::section_g.

For odd M, every nonzero word of (Φ_M) with weight below 2·q_min(M) is a
**scalar gon**: one constant on one coset of the order-t subgroup of
Z/M, for a prime t | M. Below, "gon" means scalar gon, and an r-gon is a
gon on a coset of the order-r subgroup; the q-gon above is the one with
constant 1 on the order-q subgroup itself.

Proof, by induction on the number of distinct primes of M. At a prime
power M = r^a a word of (Φ_M) has its transform on the multiples of r,
so it is invariant under x ↦ x + M/r and weighs r times the number of
order-r cosets it meets: below 2r, one r-gon. Otherwise let r be M's
largest prime, M = M′·r^a with M′ > 1 prime to r, and slice by Z/r^a.
Within each coset of the order-r subgroup of Z/r^a the slices are
congruent modulo (Φ_M′). A coset whose slices are equal and nonzero
weighs at least r ≥ q_min; a coset holding two differing slices weighs
at least q_min(M′) = q_min(M). So below 2·q_min exactly one coset is
nonzero. If its slices are equal, the word is invariant under the
order-r translation, and weight below 2r leaves one r-gon. If they
differ and one is zero, every slice of the coset lies in (Φ_M′), each
nonzero one weighing at least q_min: exactly one survives, a gon of M′
by induction and so a gon of M. If they differ and none is zero, the r
slices weigh at least (r − 2) + q_min ≥ 2·q_min, since M′ has a prime
below r and so r ≥ q_min + 2.

In characteristic 0, Lam and Leung determine which numbers of m-th
roots of unity can sum to zero (J. Algebra 224, 2000), sums with
nonnegative coefficients; signed low-weight words over F_p are outside
their classification. The script spot-checks the theorem at M = 143,
169 and 1859. At each M, at four sampled gon cosets the full coset
carries exactly a scalar gon and the coset less a point carries
nothing, and so do 30 random gon-free supports of size 2·q_min − 1.

## The coset collapse
Tier: theorem.
Verifier: proof; torsion.py::section_g.

If m is odd with at least three prime factors counted with multiplicity
and q = q_min(m) with q² ∤ m, no nonzero (Φ_m)-codeword lies in any
E(A, B, D) with gcd(A, B, m) = 1 and D ≤ q − 2.

Proof. Slice c by x mod q into words γ_x on Z/M, M = m/q. For each unit
of Z/M the transforms across x lie in (Φ_q), the constants, so the
slices are congruent mod (Φ_M). A slice difference weighs at most
2(D + 1) ≤ 2q − 2 < 2·q_min(M), so by the gon theorem it is 0 or a
scalar gon. If γ_x − γ_x₀ and γ_y − γ_x₀ were gons on different cosets,
the slice difference γ_x − γ_y would combine them, meeting in at most
one point, and weigh at least 2·q_min(M) − 2 > 2q − 2. So
γ_x = γ_x₀ + μ_x·G for one gon G, supported on a coset of the order-t
subgroup (G = 0 if the slices are all equal, and the next step then
kills c outright). Off supp(G) the slices agree, and a nonzero common
value would fill a class mod M, q cells against q − 1.
So c lies in one coset of the order-qt subgroup, one class mod m/(qt).
Since m has three prime factors, m/(qt) > 1, and that class holds at
most q − 1 exponents, below d = q. So c = 0.

The script finds no codeword at D = q − 2 over every scaling class at
m = 385 and 1001, nor at 60 seeded draws (A, B) each at 2431 = 11·13·17
and 1859 = 11·13².

## The realizability law
Tier: rule (proved; its m = qq′ case rests on the coverage cap, whose
proof is exhaustive below ℓ = 213).
Verifier: torsion.py::section_l, coverage_cap.py::section_f.

The least degree of a curve holding a codeword-species orbit of order
m > 1 is

```
D_min(m) = 1              m even
         = κ(q)           m = q an odd prime
         = q_min(m) − 1   every other odd m
```

The even row is the antipodal word at (A, B) = (m/2, 1). The prime row
is the triangle cover number. At every other odd m the q-gon enters at
(A, B) = (m/q, 1) and D = q − 1. Below it the three exclusions are
exhaustive: q² | m, m = qq′, or at least three prime factors, counted
with multiplicity, with q² ∤ m. The monomial threshold q_min(m) is the
same for q and for every m whose least prime is q, and the degree
threshold separates them: a prime order costs κ(q) = Θ(√q), while a
composite order pays q − 1 in full. Conics hold 5 but not 25 or 35
(2 against 4), and quintics hold 13 while 169 waits for degree 12.
Conics hold exactly the even orders, 5 and the multiples of 3. The law
holds at every p with m dividing p − 1, so that orbits of order m exist:
every lower bound is free of the characteristic, and every realization
has coefficients 0 and 1; the runs use the least such p.

The script excludes D = q_min − 2 over every scaling class at the prime
powers 9, 25, 27, 49, 81, 121 and at the composites 15, 21, 33, 35, 45,
55, 63, 75, 77, 99, 105, 143, 221. At each it rebuilds a realization at
D = q_min − 1 as an actual curve on an actual orbit.
