# COORDINATES — which coordinate system reads which operation

The object: the integers written in **coordinate systems**, each
writing a number as a tuple of coordinates by a bijection, and above
all in the three classical ones: residues at a set of primes, indices
(a discrete logarithm in each channel) and positional digits, defined
on Z/M for residues (M a product of distinct primes), on the units U(M)
for indices and on Z/b^j for j digits in base b. The exponent vector,
the logarithm the integers themselves carry, stands beside them in the
table below, uncounted: on a finite prime set it is no bijection. Each
system reads some operations cheaply, and an operation it does not
read cheaply is one of its **walls**. This page says which pair of
operations each system reads, proves that no system with two
coordinates or more reads addition, multiplication and size together
coordinate by coordinate,
names three kinds of wall, pins most walls, here and in SIZE.md, to
the least structures that bear them, and reads the Internet checksum,
where digits and residues meet, one prime at a time.

```
SYSTEM             +                  ×              POWERING       SIZE
residues mod M     channel-local      channel-local  exponent read  walled
 (M squarefree)                                      mod λ, y ≥ 1
indices on U(M)    one table per      addition       scaling        —
                    channel, true to
                    no proper
                    quotient but Z/1
exponent vectors   walled             addition       scaling        walled
digits in base b   one carry bit,     not automatic  —              the top
                    no bounded set                                   digit
```

λ = lcm(p − 1) over the channels, Carmichael's exponent of a squarefree
M, and the table's y ≥ 1 is the exponent of a power x^y. Size is walled
under residues once M has two channels or more (SIZE.md#the-size-wall);
at a prime M the one channel reads it. Size under indices and powering
under digits are not decided here, and their cells are left empty (—).
The exponent vector is read on a finite prime set, as a residue system
is read at a finite set of channels, and there size is walled outright:
1 and every prime outside the set share the zero vector.

Three kinds of wall appear. Size under residues at two channels or more
is an **information wall**: no channel-local read, of any size, decides
it (SIZE.md#the-size-wall). Addition under indices is a **structure
wall**: the data sits in one channel, but as a table that compresses to
no proper quotient but Z/1 (proved below, p ≥ 5). Powering under
residues is a **type wall**: the exponent must be read in another ring.

## The two-readings criterion
Tier: criterion.
Verifier: proof; coordinates.py::section_b.

Greedy numeration on a scale 1 = T₀ < T₁ < T₂ < ⋯ writes n with digits
d_i, taking at each step from the top the largest multiple of T_i
that fits. The low prefix Σ_{i<j} d_i T_i equals n mod T_j for every
n and j iff the scale is a divisibility chain, T_j | T_i for i ≥ j.
On every scale, chain or not, digit strings compared from the top are
compared as numbers; that half is known (Shallit, Numeration systems,
linear recurrences, and regular sets, Waterloo report 1991, sec. 2;
ICALP 1992): the greedy representation is order-preserving.

Proof. Greedy leaves the part of n below position i under T_i. On a
chain the prefix is under T_j and n minus it is a sum of multiples of
T_i, i ≥ j, each 0 mod T_j. Conversely n = T_i is the single digit 1
at i, prefix 0, which forces T_j | T_i. For order, at the first
differing position d_i < d′_i, and what is left of the smaller number
is below T_i.

So size and order come with greedy and residues come with the chain.
The scales on which the two readings coincide are exactly the
divisibility chains: a positional base, and every mixed radix on a
chain. Zeckendorf keeps
only the greedy half; a residue system keeps only the residue half.
The script checks the criterion on all 9,139 scales (1, T₁, T₂, T₃)
with T₃ ≤ 40 and all 3,876 scales of length 5 up to 20, and greedy
order on the first set, each scale at every n up to twice its top
term, which holds the witness n = T_i.

## The carry wall
Tier: theorem.
Verifier: proof; coordinates.py::section_a.

In base b, no bounded set of digit positions, fixed relative to j as j
grows and joined by a fixed block of low digits, reads digit j of
x + y. One carry bit, read from the least significant digit up,
computes the whole sum.

Proof. Given the set, pick a position ℓ < j outside it and above the
low block, which exists once j is large. Let x = Σ_{i=ℓ}^{j−1} (b − 1)bⁱ
and compare y = b^ℓ with y′ = 0. The inputs differ only at ℓ, and x + y
= b^j has digit j equal to 1 while x + y′ < b^j has digit j equal to 0.

It is known that no synchronous automaton recognizes the graph
x·y = z in any base. Addition is recognized by one, the carry bit its
state, so a second for x·y = z would make (N, +, ×), N the natural
numbers, an automatic structure; an automatic structure has a
decidable first-order theory (Hodgson; Khoussainov and Nerode), and
(N, +, ×) does not (Church).

## Addition and multiplication each decide
Tier: known.
Source: Presburger 1929; Mostowski 1952; Putnam 1957; Villemaire 1992;
Korec 1993 and 1995; Bès 1997; all as given in Bès, A survey of
arithmetical definability (Proposition 5, Theorems 23 and 36, the notes
on Pascal triangles); J. Robinson, J. Symbolic Logic 14 (1949) 98.

(N, +) has a decidable theory (Presburger), and so does (N∖{0}, ×).
Through the exponent vector, (N∖{0}, ×) is the weak direct power of
(N, +): one copy at every prime, all but finitely many coordinates zero.
A weak power of a decidable structure is decidable (Mostowski). So
reading every valuation at every prime costs no decidability, and on the
additive side neither does reading size, since < is definable in (N, +);
beside × it does, since < defines the successor and × with the
successor defines + (J. Robinson, 1949): z = x + y iff
(xz + 1)(yz + 1) = z²(xy + 1) + 1 with z ≠ 0, or x = y = z = 0, as the
identity reduces to (x + y)z = z². (N, +, ×) is
undecidable though neither half is. The undecidable expansions of
(N, +) that the survey charts add a trace of multiplication; a
noncomputable set is undecidable by its membership sentences alone and
needs none. The squares define × (Putnam), and so do the predicates
V_k(x), the largest power of k dividing x, at two multiplicatively
independent bases (Villemaire).
Pascal's triangle mod n, B_n(x, y) = C(x + y, x) mod n, reads at each p
dividing n whether adding x and y in base p carries (Lucas), and is
decidable beside + at a prime power but defines + and × by itself once n
has two primes, as at 6 (Korec). Each of these definitions is the
multiplicative side meeting the additive one. Residues at finitely many
primes add only periodic sets, which (N, +) already defines, so even
joined with size they decide.

## The suffix and floor reads
Tier: criterion.
Verifier: proof; coordinates.py::section_s.

For m ≥ 2, in base b [m | n] is a function of the last j digits iff
m | b^j, so some suffix reads it iff rad(m) | rad(b). On a chain of
moduli 1 = M₀ | M₁ | M₂ | ⋯, at depth t with M_t ≥ 2 and lookahead
c ≥ 0, ⌊n/m⌋ mod M_t is a function of n mod M_(t+c) iff m·M_t | M_(t+c).

Proof. n and n + b^j share the suffix, and at n = 0 they disagree
unless m | b^j; conversely, if m | b^j the suffix n mod b^j fixes
n mod m. For the floor, write M′ = M_(t+c). The step
⌊(n + M′)/m⌋ − ⌊n/m⌋ is the constant M′/m when m | M′, which is
0 mod M_t iff m·M_t | M′. Otherwise it
takes both values ⌊M′/m⌋ and ⌊M′/m⌋ + 1 as n runs over the residues
mod m, and two consecutive integers are never both 0 mod M_t.

On the primorial chain M_t = p₁⋯p_t this reads ⌊n/m⌋ at depth t iff m is
squarefree with every prime factor above p_t, and the least lookahead is
exactly π(P(m)) − t, P(m) the largest prime factor of m. So division by
m is read only at the depths t with p_t below m's least prime, and at no
depth from that prime's on. Divisibility behaves the other way: every
squarefree m divides the primorials from some depth on. At a fixed base
the two reads coincide, both holding iff rad(m) | rad(b); on the
primorial chain they part. The script finds exactly the twelve readable
cells (t, m) the criterion predicts for 2 ≤ m ≤ 30 and M_(t+c) ≤ 2,310.

## The Internet checksum
Tier: theorem.
Verifier: proof; checksum.py::section_r; checksum.py::section_c;
checksum.py::section_b; checksum.py::section_u; checksum.py::section_w.

Where digits and residues meet: at M = b − 1 a base-b numeral is
congruent to its digit sum, since b ≡ 1. The Internet checksum is that
meeting at b = 2¹⁶. RFC 1071 sums a message's 16-bit words in ones'
complement and sends the complement; its appendix (IEN 45) reads the
sum as the remainder mod 2¹⁶ − 1, the end-around carry as the
reduction, and the complement is negation. The ones' complement +0
and −0, 0x0000 and 0xFFFF, are the two representatives of the class
0. The modulus is 65535 = 3 · 5 · 17 · 257, the Fermat primes F₀ to
F₃, so the checksum is four checksums, one per prime.

Each prime reads a bit by its position alone. At the Fermat prime
F_j = 2^(2^j) + 1, 2^(2^j) ≡ −1, so a bit at position a of any word
counts at F_j as ±2^(a mod 2^j), with sign (−1)^⌊a/2^j⌋: the four primes
read the position mod 2, 4, 8 and 16, and none reads which word holds
it. Three properties of the standard follow, one prime at a time.

- The byte swap. Swapping the bytes of every word multiplies the sum
  by 2⁸, which is 1 at 3, 5 and 17 and −1 at 257: the swap is
  invisible to three primes and a sign at the fourth, which is RFC
  1071's byte-order independence.
- The update. Changing a word from m to m′ moves the field by m − m′,
  prime by prime. RFC 1141's update, HC + m + ~m′ with HC the stored
  checksum field, is that identity, and the defect RFC 1624 corrects is
  a choice of representative. On an update that leaves a nonzero word,
  as every IP header keeps, RFC 1141's update returns 0xFFFF only where
  recomputation gives 0x0000, the same class mod 65535, as in RFC 1624's
  own example. Where recomputation gives 0x0000 RFC 1141's update may
  return either: from the field recomputation wrote, with the other
  words summing to −0, m = 0 and m′ = 0xFFFF, RFC 1141, RFC 1624 and
  recomputation all give 0x0000. When an update from a field
  recomputation wrote leaves every word zero, RFC 1141 and recomputation
  give 0xFFFF, and RFC 1624's update, taking the other representative,
  gives 0x0000. These follow from the classes and one fact: a ones'
  complement sum is 0x0000 only when every term is, so recomputation
  gives 0xFFFF only on an all-zero message, and on a field recomputation
  wrote, RFC 1624's sum ~HC + ~m + m′ is never 0x0000, since ~HC = 0
  makes the message all zero and ~m = 0xFFFF. So RFC 1624 never returns
  0xFFFF there, and equals recomputation byte for byte except where the
  update leaves every word zero.
- The two-bit errors. Flips at positions a and a′ within their words
  (0 to 15), one 0 → 1 and one 1 → 0, are missed at F_j iff a ≡ a′ mod
  2^(j+1); two flips the same way iff a − a′ ≡ 2^j mod 2^(j+1). The
  checksum misses what every prime misses. Same-way pairs: odd at 3
  and ≡ 2 mod 4 at 5 contradict, so none is missed. Opposite pairs:
  missed iff a = a′, the same position in two words, which 257 alone
  decides; the same-way pairs 257 misses, eight apart, the prime 3
  catches. Over two distinct bit positions of a k-word message with
  uniform bit values the missed share is (k − 1)/(2(16k − 1)), half of
  the 16k(k − 1)/2 same-position pairs among 16k(16k − 1)/2, tending to
  the 1/32 that IEN 45 quotes.

The script checks the fold at every sum of two words, the per-prime
reading at every position, the swap on 500 random messages, both updates
on 500 random one-word changes, one in five steered to a zero sum, and
the three computations at the two edges above, each prime's miss set by
residue arithmetic at every pair of positions within a word for same-way
and opposite flip pairs, and the missed share over every pair of bit
positions and every bit value at 1 to 4 words, the checksum recomputed
each time.

## The valuation row
Tier: theorem.
Verifier: proof; coordinates.py::section_v.

Write n by its exponent vector (v_p(n))_p. Multiplication is the
coordinatewise sum. Addition is walled: for every finite prime set W,
no function of the W-coordinates of x and y gives any W-coordinate of
x + y.

Proof. Fix p ∈ W. By the CRT there is y_u with
y_u ≡ p^u − 1 mod p^(u+1) and y_u ≡ 1 mod the other primes of W. Then
y_u and 1 both have the zero vector on W, while v_p(1 + y_u) = u takes
every value u ≥ 1.

## The index coordinates
Tier: property.
Verifier: coordinates.py::section_i.

For squarefree M, U(Z/M) is the product of the cyclic (Z/p)^*. A
primitive root per channel gives the bijection U(Z/M) → ∏ Z/(p − 1) onto
the index ring, under which multiplication is addition and powering is
scaling. x is an e-th power iff gcd(e, p − 1) divides its index at every
p, with ∏ gcd(e, p − 1) roots, and x is a square mod p iff its index
there is even. The exponent of the index ring is λ = lcm(p − 1), below
∏(p − 1) once two odd primes are present, so no rung from Z/30 on
(TOWER.md) has a primitive root: the index exists only channel by
channel. The script checks the bijection at
M = 510510 = 2·3·5·7·11·13·17 (92,160 units) and the root counts there,
1,440 squares with 64 roots each and 10,240 cubes with 9.

## The Zech wall
Tier: theorem.
Verifier: proof; coordinates.py::section_z.

At a channel p with primitive root g, addition in index coordinates is
the unary table ζ(i) = ind(1 + gⁱ), defined off the one i with gⁱ = −1.
For every p ≥ 5, ζ is compatible with no quotient Z/(p − 1) → Z/q,
q | p − 1, 2 ≤ q ≤ (p − 1)/2, so it agrees with no polynomial on
Z/(p − 1) where it is defined.

Proof. Indices mod q sort (Z/p)^* into the cosets of the subgroup H of
index q, of order h = (p − 1)/q ≥ 2. Compatibility says (1 + wx)/(1 + x)
lies in H for every w ∈ H and every x ∈ (Z/p)^* outside {−1, −1/w},
which is p − 3 values when w ≠ 1. Fix w ≠ 1. For z ∈ H,
1 + wx = z(1 + x) reads x(w − z) = z − 1: z = w has no solution, z = 1
gives x = 0, and every other z gives one admissible x. So exactly
h − 2 < p − 3 of the required x comply, and each other x gives two
indices equal mod q whose Zech values are not. A polynomial over
Z/(p − 1) respects every quotient.

The index map is a channel-local bijection, so addition, where the sum
is a unit, stays channel-local in index coordinates, and the locality
criterion (SIZE.md#the-locality-criterion) cannot see this wall. It costs one
table of p − 2 entries per channel. The size wall costs what no table of
any size supplies. The script checks all 263 pairs (p, q) with p < 200,
and every w ≠ 1 when p < 60.

## The support log
Tier: theorem.
Verifier: proof; coordinates.py::section_g.

x^(λ+1) = x for every x in Z/M, λ Carmichael's exponent of M, iff M is
squarefree. Then every x is the pair (supp x, the indices of x on supp
x), supp x the set of channels where x ≠ 0. Multiplication intersects
supports and adds indices, x^λ is the idempotent of supp x, and for
M > 2 the meadow inverse x^(λ−1) (LOGIC.md#the-meadow) negates the
indices (at M = 2, λ = 1 and 0⁰ = 1).

Proof. On a squarefree M each channel is a field and p − 1 | λ. When
p² | M, M/p is nonzero with square 0, so its (λ + 1)-th power is 0. The
rest is the index coordinates applied on each support, where x^λ is 1
at every channel of the support and 0 off it.

So the logarithm reaches the whole ring as a pair, the support and an
index, and log 0 = −∞ is a drop to a smaller support. On the units the
index coordinate reads × as addition. Off them no coordinate does: a map
f into a group with f(0) + f(x) = f(0·x) = f(0) is constant. The support
stands in its place.

## The exponent wall
Tier: theorem.
Verifier: proof; coordinates.py::section_e.

For a prime p ≥ 3 and y ≥ 1, x^y is not a function of
(x mod p, y mod p): at every such y the pairs (y, y + p) disagree
exactly at the p − 2 residues x outside {0, 1}. It is a function of x
mod p and y mod (p − 1) for positive y only. At p = 2, x^y = x for every
y ≥ 1, so there is no wall there, and the only failure of either reading
is 0⁰ = 1.

Proof. x^(y+p) = x^y·x^p = x^(y+1) by Fermat, which differs from x^y
iff x^y(x − 1) ≠ 0. For positive y, x^(y+p−1) = x^y at every x,
0 included, while 0⁰ = 1 and 0^(p−1) = 0.

So the exponent of a power belongs to the index ring, with the zero
exponent excluded, and the residue reading reads its base but not its
exponent.

## The rigidity dichotomy
Tier: theorem.
Verifier: proof; coordinates.py::section_r.

On Z/M a coordinate system is a bijection x ↦ (x_1, … , x_r) onto a
product of sets of two elements or more, and it reads an operation
coordinate by coordinate when each coordinate of the result is a
function of the same coordinate of the arguments. The systems with two
coordinates or more that read + coordinate by coordinate are exactly,
up to relabelling each coordinate's values, the coprime factorizations
of Z/M into two factors or more, each above 1. Each of them reads ×
coordinate by coordinate as well, and walls size: the sign [x ≥ M/2]
is a function of no coordinate. So no coordinate system with two
coordinates or more reads +, × and size together; the one-coordinate
system Z/M reads all three and splits nothing. On the unit group
alone, multiplication is not rigid: U(M) can have decompositions that
cross the channels, three of four at M = 30.

Proof. When + is read coordinate by coordinate, each coordinate,
relabelled, is a surjective group homomorphism, so the system is an
isomorphism onto a product of quotients, which is an internal direct sum
of subgroups of Z/M. A cyclic group has one subgroup per order, and two
of them meet in the subgroup whose order is the gcd, so the summands
have pairwise coprime orders a_i with product M. Each summand is an
ideal, so a product of elements of two different summands is 0,
and × splits by summand. For a summand of order a < M, the elements 0
and a⌈M/(2a)⌉ share that coordinate while the sign [x ≥ M/2] reads 0 and
1 (SIZE.md#the-size-wall). U(30) ≅ C₂ × C₄ has four direct
decompositions, and three cross the channels: two take the C₄
{1, 17, 19, 23}, against {1, 11} or {1, 29}, and the third pairs the
channel's C₄ {1, 7, 13, 19} with the C₂ {1, 29}.

Each pair of operations has its own home: (+, ×) the residues,
(×, powering) the indices, and (+, size) the digits, where the + read is
a scan and not a bounded set of digit positions. The Zech wall is the
price of the index row and the size wall the price of the residue row. The
script counts 4, 4, 1 and 14 additive decompositions of Z/30, Z/60, Z/12
and Z/210, one per coprime factorization into two factors or more.

## The bearers
Tier: theorem.
Verifier: proof; coordinates.py::section_p; size.py::section_h.

A **bearer** of a wall, or of a law the walls rest on, is a structure on
which it holds. Every bearer in the table below is a finite ring or a
finite abelian group, and none needs the rungs. The carry wall and the
addition wall of the valuation row live on the integers themselves,
outside the table. Conjunctive and failing maximally are
SIZE.md#the-conjunctive-split's terms. There are two kinds of row. An
**exact row** names a hypothesis its wall or law needs: on a structure
without it, it fails. A **sufficient
row** names only the hypothesis its proof uses.

```
BEARER                      WALL / LAW                            KIND
a cyclic group and a        sign and orientation hidden           exact
 proper quotient             (SIZE, the hiding lemma)
any composite Z/M           quantifying over channels:            exact
                             no polynomial computes [x = 0]
one field, p ≥ 5; p ≥ 3     the Zech wall; the exponent wall      exact
two coprime windows         order fails maximally                 exact
two cyclic groups of        the order-divisibility wall:          exact
 non-coprime orders          ord(x) | ord(y) not conjunctive
squarefree                  x^(λ+1) = x; the meadow               exact
squarefree                  channel-local = polynomial            sufficient
```

Proofs of the rows not proved elsewhere on these pages. The **quantifier
wall**, LOGIC.md#the-pair's wall on quantifying over channels, is read
here at its least bearer. A polynomial on Z/M is compatible with every
quotient Z/A, and a proper divisor A > 1 would need [0 = 0] ≡ [A = 0]
mod A, that is 1 ≡ 0; at a prime [x = 0] is 1 − x^(p−1), so the wall
needs the composite. For order, a window A that is a proper divisor of M
suffices, since u = s < A and v = s′ + A ≤ 2A − 1 < M realize every
residue pair (s, s′) at A with u ≤ v; no field is used. Two coprime
windows whose product is M make a coordinate system, so that the
conjunction is defined, and with one coordinate, Z/M itself, order is
read. On C_n1 × C_n2 the relation ord(x) | ord(y) is conjunctive iff
gcd(n1, n2) = 1, and fails maximally iff n1 = n2. Its first projection
is the set of pairs with ord x₁ | lcm(ord y₁, n2), all of them iff n1 |
n2, and its second, by symmetry, is full iff n2 | n1. When gcd(n1, n2) =
1, ord x₁ is prime to n2, so the projection is ord x₁ | ord y₁, and
since ord x is the product of its coprime parts the conjunction is the
relation. At a prime r dividing both, x of order r in the first factor
against y = 0 lies in both projections but not in the relation. The
least bearer where the relation fails without failing maximally is C₂ ×
C₄ = U(15). On the rungs the order-divisibility wall first appears at
Z/30, whose channels 3 and 5 are the first two with unit orders 2 and 4
sharing a prime, and that pair is the bearer U(15) itself.

The locality criterion's row is sufficient only: its proof uses the
fields, yet Z/4 still has as many polynomial maps as maps whose value
mod 2 depends only on the argument mod 2, 64, and Z/8 is the first
failure (size.py::section_l). The script checks the quantifier wall
against the whole span of polynomial functions at Z/4, Z/6, Z/8 and Z/9
(Kempner's counts 64, 108, 1,024 and 19,683), order at Z/6 and at Z/36
through the windows 4 and 9, and the order-divisibility relation on all
45 pairs 2 ≤ n1 ≤ n2 ≤ 10.
