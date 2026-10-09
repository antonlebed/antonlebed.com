# TRIPLE — what a cubic field's split primes carry

The object: a complex cubic field K of discriminant d_K, its class
group Cl of order h, and the classes of its degree-1 places. A totally
split prime p = P₁P₂P₃ carries a triple of classes, and since
P₁P₂P₃ = (p) the triple lies in
M = {(a, b, c) ∈ Cl³ : a + b + c = 0}, of order h². A partially split
prime carries one degree-1 class. The questions: which triples occur,
which class the partial place takes, and how the shortfall of principal
places at a finite cut, which over an imaginary quadratic field the
prime-ideal powers account for (PRINCIPAL.md), behaves one degree up.
The engine is cubic.py; the verifiers are triple.py, conductor.py,
shortfall.py and seat.py.

cubic.py, in pure Python, takes a complex cubic field to its maximal
order from a binary cubic form (Delone and Faddeev), the places over any
prime, the class group and the class of a degree-1 place, by a bounded
search that placed every place these runs needed. Its class group is
checked against the analytic class number formula: the relations give h
and the regulator Reg up to one integer factor m, and h·Reg over the
formula's value, its Euler product taken to 3·10⁴, reads 0.9962 to
1.0027 at all 8336 complex cubic fields with |d_K| ≤ 50000, where m ≥ 2
would put it near 2 or above. The truncated product carries no proved
error bound, so this is numerical evidence and not a proof
(triple.py::section_controls). The enumeration is checked against an
independent count of the complex fields to |d_K| ≤ 6000 (888) and by
Hasse's count at conductor 1; an independent record counts 3133 complex
fields with h > 1 to |d_K| ≤ 50000 where this enumeration finds 3134 (a
recorded miss of triple.py's K1).

The answer, in two lines: the triples fill a subgroup R of M whose index
is 3^t, t counting the primes q ≡ 1 mod 3 that divide the conductor f of
d_K = f²d₀ (d₀ fundamental), plus one when 9 | f and 3 splits in Q(√d_K)
(TRIPLE.md#the-genus-index-law; proved at 3-rank at most 1 and wherever
t = 0 or t is the 3-rank; verified to |d_K| ≤ 50000), so the triples
fail to fill M exactly at the fields the discriminant names; the partial
place is uniform on Cl whatever R is. At a finite cut the principal
places run short as they do over an imaginary quadratic field, but at
degree 3 the prime-ideal powers account for only about a third of it at
cut 1000 (an observation); the rest reads as a fixed weight missing at
the primes below a few hundred (a pattern), carried mostly by the
partial places at that cut (an observation), to which the explicit
formula gives no square term; and at 2-rank 1 the least odd partial
place lies outside 2Cl far more often than half (an observation).

## The triple is a homomorphism
Tier: property.
Verifier: proof; triple.py::section_controls.

Let N be the Galois closure of K, H the Hilbert class field of K and H̃
the Galois closure of H over Q. A prime p splits totally in K exactly
when its Frobenius in Gal(H̃/Q) lies in Gal(H̃/N). With K₁, K₂, K₃ the
conjugates of K in N and H₁, H₂, H₃ the matching conjugates of H,
restriction to Hᵢ is a homomorphism Gal(H̃/N) → Gal(Hᵢ/Kᵢ) = Cl, and
with 𝔓 the prime of H̃ over p whose Frobenius is read, Pᵢ = 𝔓 ∩ Kᵢ, so
by Artin the triple is the image of Frobenius under a homomorphism into
M. Chebotarev fills Gal(H̃/N), so the realized set R is a subgroup of M;
conjugation permutes the copies, so R is stable under S₃ acting on
coordinates; each coordinate map is onto, since H₁ ∩ N = K₁
(TRIPLE.md#the-partial-place-is-uniform), so every projection of R is
onto Cl. The closure [P₁] + [P₂] + [P₃] = 0 holds at every totally split
prime the script classes, the 37608 triples it keeps among them; where
each place is classed on its own, above the primes whose places generate
the relations, this tests the class map, and below them the relation (p)
forces it.

## The stable subgroups
Tier: theorem.
Verifier: proof; triple.py::section_groups.

An S₃-stable subgroup R of M with every projection onto Cl contains
M ∩ (3Cl)³, and is the preimage of W ⊗ St + V ⊗ D for a subspace W of
V = Cl/3Cl, where St is the sum-zero permutation module of S₃ over F₃
and D its diagonal. Its index in M is 3^(r − dim W), r the 3-rank.

Proof. For (a, b, c) ∈ R, the transposition (12) gives (b, a, c) ∈ R, so
(a − b, b − a, 0) ∈ R; permuting, (a − c, c − a, 0) ∈ R; the two sum to
(3a, −3a, 0), since b + c = −a. As a runs over Cl, R holds every
(3a, −3a, 0), and with its permutations all of M ∩ (3Cl)³. So R is the
preimage of a stable subspace of the sum-zero triples of V, which is V ⊗
St. In characteristic 3 the module St is uniserial: its only stable line
is D = {(λ, λ, λ) : λ ∈ F₃}, since λ + λ + λ = 0, its top St/D carries
the sign,
and for a 3-cycle γ the map γ − 1 kills D and carries St/D
isomorphically onto D. For a stable subspace U let V₀ ⊆ V be its
intersection with V ⊗ D and W ⊆ V its image in V ⊗ (St/D); γ − 1 maps U
into itself, so W ⊆ V₀. Write u ∈ U as x⊗(1, −1, 0) + y⊗(1, 1, 1); then
u + (12)u = 2y⊗(1, 1, 1) lies in U, so y ∈ V₀ and the first coordinate
x + y lies in V₀ + W = V₀, so a U projecting onto V has V₀ = V: it
contains V ⊗ D and is W ⊗ St + V ⊗ D, of codimension r − dim W.

When 3 ∤ h, V = 0 and R is all of M. At 3-rank 1 it is M or
Δ = {a ≡ b ≡ c mod 3Cl}, of index 3; at h = 3 the candidates 0, D and M
are the smallest case, 0 excluded by the projection. Computably Δ is a
lattice membership (with Cl = Zⁿ/Λ, 3Cl is (Λ + 3Zⁿ)/Λ); the
scalar test (h/3)(a − b) = 0 agrees with it only where the 3-part is
cyclic, and above 3-rank 1 it passes every triple. Over thirteen groups
with h ≤ 18 the stable subgroups projecting onto Cl number exactly the
subspaces of F₃^r, graded by index as the theorem says, each containing
M ∩ (3Cl)³.

## The genus index law
Tier: rule (verified at every complex cubic field with |d_K| ≤ 50000).
Verifier: triple.py::section_genus.

Write d_K = f²d₀ with d₀ the fundamental discriminant of the resolvent
k = Q(√d_K) and f the conductor. Let t be the number of primes
q ≡ 1 (mod 3) dividing f, plus one when 9 | f and 3 splits in k. Then
[M : R] = 3^t, and R is the triples agreeing modulo the subgroup G of Cl
cut out by the fields below.

The argument has two halves. Below: each such q, or the 9, names a
cyclic cubic field F of conductor q or 9 with KF/K unramified. At a
q ≡ 1 (mod 3) this is Abhyankar's lemma: q splits in k, since an inert
or ramified q ≡ 1 offers χ, the cubic character of k cutting out N, only
pieces fixed by the conjugation σ of k/Q
(TRIPLE.md#the-conductors-primes-are-forced), and, χ being tame at q, q
∥ f, so v_q(d_K) = 2, and q is totally and tamely ramified in K, F is
tamely ramified at q alone with index 3, and F is real; at the 9, where
the ramification is wild, it is local class field theory at 3: 3 splits
in k and N/k ramifies over it, so 3 = 𝔮³ in K with K_𝔮 a ramified cyclic
cubic extension of Q₃; the cubic characters of Z₃* form a group of order
3, read on (1 + 3Z₃)/(1 + 9Z₃), so F's character at 3 is K_𝔮's or its
inverse times an unramified one, and KF/K is unramified at 𝔮. The t
fields are abelian over Q with coprime conductors and K is not Galois,
so their compositum meets K in Q and the t fields together give an
unramified extension of K of degree 3^t, cutting out a subgroup G of
index 3^t in Cl. F is Galois over Q, so a Frobenius restricts to F
identically from all three copies, and R lies in {a ≡ b ≡ c mod G}, of
index 3^t in M. Above: a further cubic character of k that the triple
could see independently must be fixed by the conjugation of k/Q and
unramified over N, and such a line needs a split conductor prime
(TRIPLE.md#the-sign-of-the-second-line-is-the-regime), so the index is
at most 3^t. That half is proved at 3-rank 1; where t is the 3-rank r,
since the stable subgroups give index at most 3^r; and at t = 0 at every
3-rank: under each quotient Cl → Z/3 the triples' image is D or St, and
D would give a σ-fixed cubic character of k whose field is unramified
over N, which needs a split conductor prime, so every quotient reads St
and R = M. At 3-rank 2 or more with 1 ≤ t < r the count below is what
the rule rests on, at the one such field in range.

So Cl/G ≅ (Z/3)^t, the Galois group of the t fields' compositum over K,
3^t divides h and t ≤ r, which holds at all 8336 fields. At every field
with h > 1 — 3134, each read through ten or more split primes — the
index of the subgroup the triples and their permutations generate is
exactly 3^t: 1767 fields with 3 ∤ h, 1018 at 3-rank 1 with t = 0, 347 at
3-rank 1 with t = 1, and the 2 of 3-rank 2 below. The generated subgroup
lies in R, R being stable, so its index bounds [M : R] from above, and
the below half bounds it from below, so at every such field the count
settles the index given cubic.py's class groups, with no appeal to
chance. At h = 3 and |d_K| ≤ 6000 the 83 fields split 38 at index 3 and
45 at index 1. The two fields of 3-rank 2, |d_K| = 24843
(f = 91 = 7·13, t = 2) and 47628 (f = 126 = 2·3²·7, t = 1), read index 9
and index 3, the first proved and the second the one field with
1 ≤ t < r. A uniform Frobenius on R prices any event at its size over
|R| = h²/3^t.

## The conductor's primes are forced
Tier: rule (verified at every complex cubic field with
|d_K| ≤ 50000; the sketch below covers the primes other than 3).
Verifier: conductor.py::section_admissible;
conductor.py::section_ranks.

A prime q ≡ 1 (mod 3) divides f only when it splits in k, a prime q ≡ 2
(mod 3) only when it is inert, v₃(f) ≤ 2, and v₃(f) = 1 only where
3 | d₀. The cubic character χ of k cutting out N has conductor (f) and
is inverted by the conjugation σ (its conductor is Hasse's: d_K = f²d₀
for a cubic field whose Galois closure is N), so at each prime of k over
f that σ fixes its local part needs a piece of the local units' 3-part
that σ inverts, and at a pair of primes that σ swaps a nontrivial
3-part: an inert q ≡ 1 or a ramified q ≠ 3 offers only fixed pieces (at
an inert q the 3-part of F_(q²)* lies in F_q*, as 3 ∤ q + 1, and at a
ramified prime the residue field is F_q, both fixed by σ, the higher
units being pro-q), a split q ≡ 2 none at all. The 3-part of (O_k/f)*
then splits under σ prime by prime — one fixed and one inverted cyclic
factor at a split q ≡ 1 or at 9 | f with 3 split or inert, one inverted
at an inert q ≡ 2 or at 3 ∥ f, one fixed and two inverted at 9 | f with
3 ramified — and the engine reads these ranks at all 2468 fields with
f > 1. So the conductor is not free data: which primes may divide it is
fixed by their residues mod 3 and how they split in k.

## The sign of the second line is the regime
Tier: theorem (3-rank 1).
Verifier: proof; conductor.py::section_ranks;
conductor.py::section_sign.

At 3-rank 1 the triples read mod 3Cl cut out, over N, a field whose
largest abelian piece over k is an extension E of type (3, 3) containing
N and unramified over N. In Gal(E/k), of type (3, 3), σ inverts the
quotient Gal(N/k), and the **second line** is the kernel Gal(E/N); σ
fixes the second line when R = Δ and inverts it when R = M, and these
are the two regimes. A cubic character of k fixed by σ is usable when
its field, joined to N, is unramified over N (said below as its field
being unramified over N); a usable one exists only when t ≥ 1, so the
index law's above half holds at 3-rank 1 by proof; when t ≥ 1 the genus
law's below fields give one.

Proof. Since σ inverts Cl(k), the σ-fixed 3-part of the ray class group
mod f comes from the local units (O_k/f)*. E/N unramified at a prime
𝔭 | f asks that each character of Gal(E/k) restrict on the local units
into ⟨χ_𝔭⟩, χ_𝔭 the local part of χ at 𝔭; where σ fixes 𝔭 that group
holds no nontrivial fixed character, and where σ swaps 𝔭 with its
conjugate the local cubic characters form a line spanned by χ_𝔭. So a
usable fixed line needs a split conductor prime with nontrivial local
3-part, that is t ≥ 1. If the triples' image under a quotient φ: Cl →
Z/3 is D, as at 3-rank 1 when R = Δ and as the genus law uses at t = 0,
let H′ be the cubic unramified extension of K that φ cuts out and
J = H′₁N, which at 3-rank 1 is E, of degree 9 over k as H₁ ∩ N = K₁
(TRIPLE.md#the-partial-place-is-uniform). The three coordinates of a
triple agree modulo ker φ, so H′₁N = H′₂N = H′₃N and J is Galois over Q.
The transposition fixing K₁ restricts to σ on k, and any lift acts on
H′₁ as an element of the abelian Gal(H′₁/K₁), so σ acts trivially on
Gal(J/N) ≅ Gal(H′₁/K₁); σ inverts Gal(N/k), and 2 being invertible on a
group of order 9 the two parts each have order 3: Gal(J/N), at 3-rank 1
the second line, is fixed, so the fixed character of k vanishing on the
inverted part is usable, and t ≥ 1. If the image under φ is the sum-zero
module St, as at 3-rank 1 when R = M, its field L = H′₁H′₂H′₃N is
unramified over N and Galois over Q, and Γ = Gal(L/k) has order 27 and
is not cyclic. Its commutators fill the diagonal and Γ modulo it is
abelian, so by Burnside Γ^ab is (Z/3)², and σ acts on its line from St
by the sign: inverted.

Existence alone does not sort. A σ-fixed cubic character of k exists at
9 | f whatever 3 does in k, and is unusable at exactly the 150 fields
with 9 | f, 3 not split and no q ≡ 1 dividing f. At all 1018 fields of
3-rank 1 with t = 0 the ray class group mod f has a σ-inverted line
beyond χ's, checked through sufficient conditions for its σ-inverted
part to have 3-rank at least 2, and the second line of E is inverted, E
being unramified over N, by the proof above, t = 0 forcing R = M. At
t = 1 the same sufficient conditions give an inverted line of the ray
class group mod f beyond χ's at 121 of the 347 (at d₀ = −3 they count
the cube roots of unity once, a lower bound), beside the usable fixed
one there, its field unramified over N wherever, at every σ-fixed
conductor prime, the 3-part of the local units has a σ-inverted part of
3-rank at most 1, which holds at all but 23 fields of 3-rank 1 (the
least |d_K| among them 11907); at the t = 1 fields among those 23 the
script leaves it undecided. So neither which fixed characters exist,
usability aside, nor which inverted ones exist decides R; usability
does, and with it the sign σ puts on the second line of the E the
triples cut out.

## Gerth's rank law at conductor 1
Tier: known.
Source: F. Gerth III, Ranks of 3-class groups of non-Galois cubic
fields, Acta Arith. 30 (1976) 307–322, Theorem 3.4.

If f = 1, so that N/k is unramified, then rk₃ Cl(K) = rk₃ Cl(k) − 1:
3 divides h exactly when the resolvent has 3-rank at least 2.

The triples prove one direction: if f = 1 and 3 | h, the resolvent has
3-rank at least 2. With no conductor prime, take any quotient Cl → Z/3:
the triples' image in the sum-zero triples of Z/3 is D or St. D would
give, as in the block above, a fixed unramified cubic character of k,
which σ forbids; so it is St, and the extension of type (3, 3) built
there is unramified over k. The engines read the law at the ranks that
occur: over the 5868 fields with f = 1 and |d_K| ≤ 50000, cubic.py's
class group and the resolvent's class group, read as binary quadratic
forms by principal.py, sit at 3-ranks (0, 1) at 5460 fields and (1, 2)
at 408, none off (conductor.py::section_corner). Hasse's count of cubic
fields of discriminant d₀, (3^ρ − 1)/2 with ρ the 3-rank of Cl(k)
(H. Hasse, Math. Z. 31 (1930) 565–582), checks the enumeration at f = 1
at all 3043 fundamental d₀ with −10000 ≤ d₀ < 0
(conductor.py::section_controls).

## The partial place is uniform
Tier: theorem.
Verifier: proof; triple.py::section_partial.

The degree-1 place over a partially split prime has its class
equidistributed on Cl, at every complex cubic field and whatever R is.

Proof. Frobenius at a partially split p is a transposition fixing one
copy, say K₁: an element of Gal(H̃/K₁) outside Gal(H̃/N). Restriction
maps Gal(H̃/N) onto Gal(H₁/(H₁ ∩ N)), a subgroup of Cl of index
[H₁ ∩ N : K₁], which divides [N : K₁] = 2. H₁/K₁ is unramified at every
place, the real one included, while N/K₁ ramifies at the real place of
K₁, since N is totally complex. So H₁ ∩ N = K₁, Gal(H̃/N) maps onto Cl,
and so does its other coset in Gal(H̃/K₁), the elements over the
transposition fixing K₁; Chebotarev spreads [P₁] evenly. Over a
quadratic field Chebotarev in its Hilbert class field likewise spreads a
split place evenly over its class group.

So the possible values of R differ only in the split primes, and one
place cannot tell them apart in the limit. At a finite cut the partial
place is principal at 0.3247 over the index-3 fields with h = 3 to
|d_K| ≤ 24000 and p < 1000, and at 0.3121 over the index-1 fields, a
ratio of 1.0405 ± 0.0175, 2.3 standard errors counted as if places were
independent, which places of one field are not, while the split places'
per-place shares read 0.3216 and 0.3224 (an observation).

## The classes of the prime powers
Tier: theorem.
Verifier: proof; triple.py::section_groups.

Gal(H̃/Q) is an extension of S₃ by R, and it splits: complex conjugation
lifts a transposition with order 2, and every lift g of a 3-cycle is, by
Chebotarev, the Frobenius of some prime p inert in K, so g³ restricts on
each Hᵢ to the Artin symbol of the principal ideal pO_Kᵢ and g³ = e;
with R abelian and a complement over each Sylow subgroup of S₃,
Gaschütz's theorem gives the complement. So Gal(H̃/Q) = R ⋊ S₃. Where
R = M the group has order 6h², and an element (v, s) squares to e when
s = 1 and 2v = 0 (|Cl[2]|² of them) or s is a transposition and
v + sv = 0, i.e. v = (a, −a, 0) up to the order of coordinates
(h for each of three): 3h + |Cl[2]|² in all. It cubes to e when s = 1
and 3v = 0 (|Cl[3]|²) or s is a 3-cycle, where
v + sv + s²v = (a + b + c)(1, 1, 1) = 0 always (h² for each of two):
2h² + |Cl[3]|². Every inert prime's cube, the identity as the splitting
showed, carries the all-principal triple at every h.

## The shortfall is a fixed weight at the small primes
Tier: pattern (complex cubic fields with h ≥ 2: cuts 10³ to 10⁴ over
|d_K| ≤ 12000, the cut 2·10⁴ over |d_K| ≤ 3000, and the single places
over |d_K| ≤ 24000, those with p < 2000 beyond 12000).
Verifier: triple.py::section_partial; shortfall.py::section_sweep;
shortfall.py::section_collapse; shortfall.py::section_closure.

The level of a set of classes is the one defined over a quadratic field
at PRINCIPAL.md#the-shortfall-is-the-prime-powers, read here raw over
the degree-1 places below a cut X or over Π_C, all prime-ideal powers of
K in class C weighted 1/j for a j-th power. At cut 1000, over the 535 fields to
|d_K| ≤ 12000:

```
cell                     fields   raw       in prime powers
T, the trivial class     535      0.9244    0.9489
S, nontrivial squares    313      1.0176    1.0226
O, outside 2Cl           291      1.0570    1.0196
```

The powers remove 66% of the non-squares' excess but only 32% of the
trivial class's deficit at cut 1000; over an imaginary quadratic field
they flattened every class by cut 10⁴, where the trivial class here, in
powers, still reads 0.9931 ± 0.0008. The rest is no lower-order main
term like the prime-power correction, nor a piece of the size li(√X) a
zero near the centre would give. Its deficit δ = 1 − η, η the level of T
counted in prime powers, falls 0.0511, 0.0313, 0.0125, 0.0069 at cuts
10³, 2·10³, 5·10³, 10⁴, and δ·li(X) reads 9.1, 9.9, 8.6, 8.6: a fixed
missing weight diluting as 1/li(X), where the zero's piece would hold
δ·li(X) growing as li(√X). Per nontrivial class δ/(h − 1) stays within
about a factor two across h = 2 to 7 at every cut, its largest over its
least reading 1.54, 1.35, 1.99 and 2.00 at 10³, 2·10³, 5·10³ and 10⁴.

The weight sits at the smallest primes. The principal level of a single
unramified degree-1 place, h when it is principal and 0 when not,
averages 0.33 to 0.49 at p = 2 to 7, 0.54 to 0.86 up to 90, 0.82 to 0.98
up to 400, and within 0.06 of 1 above, through the largest places read
(p < 10⁴, p < 2·10⁴ at |d_K| ≤ 3000, p < 2000 beyond 12000). It moves
with the discriminant, but far less than a floor does: split into bands
of |d_K| doubling to 24000, the larger fields run lower near p = 100
(0.85 and 0.82 from ln p = 4.5 to 5, against 0.97 and 0.98 in the two
smallest bands), while binned by ln p − a ln |d_K| the bands' χ²/dof
barely moves with a (1.97 at a = 0, least 1.57 at a = ½, 2.44 at a = 1),
where the same scan over imaginary quadratic fields, whose least
principal prime is at least |d|/4 at discriminant d, finds that floor's
a = 1 at χ²/dof 0.55 against 15.2 at a = 0. The trivial class in prime
powers over the fields to |d_K| ≤ 3000 reads 0.9973 ± 0.0010 by cut
2·10⁴, 2.7 standard errors short of 1. Why the smallest places of a
complex cubic field avoid the trivial class, what sets the few hundred,
and how that scale grows with |d_K| are open. The weight summed over the
classes equals the count taken from how each prime splits, without the
class map, to 5·10⁻¹³.

## The partial fiber has no square term
Tier: property.
Verifier: proof; seat.py::section_fibers.

Split the degree-1 places over unramified primes into two fibers: the
split fiber, three places over each totally split p, and the partial
fiber, one place over each partially split p. The partial fiber's count
in a class is a count of primes whose Frobenius in Gal(H̃/Q) = R ⋊ S₃ (R
the realized subgroup of M) lies in a set Σ of conjugacy classes, and
the explicit formula for such a count carries a term at p^j exactly when
Frob_p^j lies in Σ; the split fiber's, 0 to 3 places a prime, is a class
function of Frobenius summed the same way. The partial fiber's Σ has a
transposition for its S₃-part, and a square (v, s)² = (v + sv, s²) has
its S₃-part in A₃. So the partial fiber holds no square and carries no
prime-square term, only the odd powers j ≥ 3 of its own places. Every
other power of an unramified prime ideal belongs to the split fiber,
including the square of a partial Frobenius, (v, τ)² = (2a, −a, −a) with
τ its transposition and a = [P₁], which is P₁² beside the degree-2
place.

An observation, read over the 535 fields with h ≥ 2 and |d_K| ≤ 12000 at
cut 1000, each fiber with its own powers put back (standard errors 0.004
to 0.006):

```
fiber     cell   raw      in its own powers
split     T      0.9458   0.9812
          O      1.0512   0.9895
partial   T      0.9108   0.9103
          O      1.0769   1.0835
```

The powers take the split fiber's excess outside 2Cl to just below 1,
and they move no partial cell by more than 0.0066, the cube sliver. So
the fixed weight the shortfall block reads is mostly the partial
fiber's: its trivial deficit, 0.090, and its surplus outside 2Cl stand
where the explicit formula has no prime-square term to pay them, while
the split fiber keeps a trivial deficit of 0.019.

## The least partial place leans non-square
Tier: observation (two disjoint populations of complex cubic fields of
2-rank 1, |d_K| ≤ 24000 and 24000 < |d_K| ≤ 48000).
Verifier: seat.py::section_seat; seat.py::section_rank;
seat.py::section_generation; seat.py::section_two;
seat.py::section_least; seat.py::section_controls.

At 2-rank 1 the group Cl/2Cl has order 2 and partial places lie outside
2Cl at share ½ in the limit over primes
(TRIPLE.md#the-partial-place-is-uniform). Order a field's odd partially
split primes by size and call a place's index in that order its
position. The position-1 place is outside 2Cl at 0.837 ± 0.014 over the
688 fields to |d_K| ≤ 24000 and 0.800 ± 0.014 over the 844 beyond.
Pooled, the share reads 0.817, 0.691, 0.654, 0.624 at positions 1 to 4
and 0.59 to 0.64 through position 10, where the partial places between
500 and 1000 sit at 0.5036. At h = 2, where 2Cl is the trivial class,
the least odd partial place is non-principal in 84% and 81% of the
fields.

At fixed primes the share follows the position. At position 1 it is
0.819, 0.822, 0.831 and 0.814 where that place lies over 3, 5, 7 and 11,
while over one range of primes, the places over 11 to 29, a place of
position at least 3 reads 0.634 ± 0.008 against a position-1 place's
0.788 ± 0.025, the two drawn from different fields, so a trait of the
field is not held fixed. So the preference reads as one for being the
least partial place, whichever prime that is. It is not forced by the
class group's generation: the prime ideals of norm up to the Minkowski
bound generate Cl, but at every one of the 1532 fields some other such
place already lies outside 2Cl, so no field forces its least partial
place there. How 2 splits grades it: 0.959 ± 0.013 where 2 = P³, 0.900
where 2 = P²P′, 0.81 to 0.85 where 2 splits or is inert, and 0.695 where
2 is partially split, so that the least odd partial place is second
among all partial places. It falls with |d_K|, 0.837 to 0.800 across the
two populations (1.9 standard errors), and with 2 counted the least
place reads 0.983 over the fields to 6000, a rehearsal's, against 0.841
beyond; at fixed h = 4 the two populations agree. Whether it decays to
½, how fast, and what puts a non-square first are open. At 2-rank 1,
Cl/2Cl names one unramified quadratic extension of K, and a partial
place outside 2Cl is one inert in it.

## Open fronts

What puts a non-square first. The effect is about being first;
generation forces no field, and no splitting type of 2 forces it, 2 = P³
reading 213 of 222. Open: why the ramification of 2 grades it, and
whether the share at position 1 decays to ½.
