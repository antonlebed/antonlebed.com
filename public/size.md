# SIZE — what a residue window cannot read, and what reading it costs

The object: a finite ring R = K_1 × ⋯ × K_k read through its
**channels**, the k projections. A map is **channel-local** when each
channel of its value depends only on the same channel of its argument.
Over Z the ring is a squarefree Z/M, an integer x ∈ [0, M) read as its
residues. A **window** is the reading of an element at a set of places;
here it is x mod W for a divisor W of M, and it is proper when W < M.
Over F₂[x], F₂ the field of two elements and x there an indeterminate
rather than an integer, the ring is F₂[x]/f with f squarefree, an
element a of F₂[x]/f read as its residues mod the factors f_i. This page
says which maps a window computes channel by channel, why size is not
among them, why ∞ − k and −k read alike at every finite place once ∞
is divisible by every positive integer, how completely
size hides from a proper window, what the
least exact key for size costs and where a published comparator sits
against it, what a labelling kept by addition can carry of it, and which
part of all this belongs to windows and which to the archimedean place Z
happens to have.

```
QUESTION                       ANSWER                         PRICE
what is channel-local          exactly the polynomials        none
sign, compare, overflow        channel-local at no p < M      the wall
∞ − k against −k               one value at every finite      the order, read
                                place when ∞ is divisible      at no finite
                                by all n                       place
what a window W knows of the   sign-bit bias 0 or 1/2 an      nothing
sign                           element, 0 iff M/W is even
what x mod Q knows of          no element determined until    no pair ordered
 [1, X]                         Q > X/2                        until
                                                               2Q − X ≥ 2
which relations split          equality, divisibility         order fails
 by channel                                                    maximally
the least exact key            (floor(x/m_k), x mod m_k)      all moduli
 (G(x), x mod m_j)                                             but one
a labelling by s labels        exact below x₀, then periodic  order-blind at
 on [0, N), kept by addition    (x₀ + d ≤ s)                   and above s
over F₂[x] instead             the same wall, zero bias,      no carries,
                                an exact-or-flagged read       no silent miss;
                                                               (read: bias from
                                                               the ultrametric
                                                               place, carries
                                                               from char 0)
```

A letter or term not defined above is defined in the section that
answers its row, the sign-bit bias in SIZE.md#the-hiding-lemma.

## The locality criterion
Tier: criterion.
Verifier: proof; size.py::section_l.

On a finite product of finite fields a map R → R is channel-local iff
it is a polynomial function, and the same holds in several variables.

Proof. A polynomial is evaluated channel by channel
(LOGIC.md#the-pair uses this half). Conversely the channel map
K_i → K_i is a Lagrange polynomial of degree below |K_i|, and the CRT
glues the channels' coefficients degree by degree into one polynomial
over R. In several variables the Lagrange basis is a product of
one-variable ones.

Read as dynamics, this is a decoupling. A cellular automaton on R whose
rule is built from ring operations (sums, products, constants, and so
every power map, the meadow inverse of LOGIC.md#the-meadow included) is
the product of k independent automata, one per channel: channel i's
trajectory depends only on channel i's initial state. By the converse,
every k-tuple of arbitrary per-channel rules is one such rule. A
threshold inside a channel therefore comes free, and no ring rule
couples two channels.

The fields are needed. Over Z/8 the maps whose value mod 2 depends only
on the argument mod 2 number 2² · 4⁸ = 262,144, while the polynomial
maps number 1,024 (Kempner's count); over F₂[x]/x³ the numbers are the
same. The script counts the polynomial maps as the span of the powers:
all 108 channel-local maps of Z/6 among its 46,656, exhaustively; the
16 and 1,024 of F₂[x]/(x(x + 1)) and F₂[x]/(x(x² + x + 1)) and the
1,024 of Z/8 and of F₂[x]/x³, against channel-local totals counted by
hand; and it lifts seeded maps of Z/30 in one and two variables.

## The size wall
Tier: theorem.
Verifier: proof; size.py::section_w.

Read x ∈ Z/M as its least residue, M any modulus, and the channel at a
prime p | M as x mod p. For every prime p | M with p < M, the sign
[x ≥ M/2], the comparison [x < y] and the overflow [x + y ≥ M] are not
channel-local at p: none is a function of the arguments' residues mod p
alone. So on a squarefree ring with at least two channels none is a
polynomial, and no channel-local bijection T makes one local: sign ∘ T
is channel-local at no prime p | M with p < M either.

Proof. Let b = p⌈M/(2p)⌉. Then b ≡ 0 mod p, and M/2 ≤ b ≤ M − 1
because p ≤ M/2. The sign reads 0 at 0 and 1 at b; the comparison
reads 0 at (0, 0) and 1 at (0, b); the overflow reads 0 at (0, 0) and
1 at (b, b). A channel-local bijection acts by a bijection on each
channel, so its inverse is channel-local, and a local sign ∘ T would
make sign = (sign ∘ T) ∘ T⁻¹ local; the same holds for comparison and
overflow with T applied to both arguments.

The wall is locality, not linearity: no change of coordinates inside
the channels, linear or not, exposes size. At a prime M there is one
channel and every map is a polynomial; the wall needs a proper window.

## Infinity at a finite place
Tier: property.
Verifier: proof.

Adjoin to Z an element H above every integer, in an ordered ring A, and
write ∞ − k for H − k: it lies above every integer, while −k lies below
0. A finite place of A is a ring map f into a finite ring, of
characteristic m say. When H is divisible in A by every positive
integer, f(H) = m·f(H/m) = 0 at every finite place, so ∞ − k and −k
have one residue at every finite place at once. Over Z the places together
separate every pair, Z → Ẑ being one-to-one; here they read ∞ − k and
−k as one value, and the order tells them apart. The order is read
at no finite place: for every x ≠ 0, x and (1 − 2m)x agree mod m and
have opposite signs. Divisibility is a choice: an infinite hyperinteger
can have any residue point a ∈ Ẑ. For each a the sets
{n ≥ 1 : n ≡ a mod lcm(1, …, j)} are nested and infinite, so a
nonprincipal ultrafilter on the positive integers holding all of them
makes the hyperinteger [n] infinite with residue a
at every modulus, and ∞ − k reads a − k, apart from −k at exactly the
moduli where a is not 0.

The neighbours sort by which half they keep. Ẑ keeps every residue and
no order: n! → 0 there, so ∞ − 1 read as the limit of n! − 1 is −1
itself.
Conway's omnific integers keep the order and read only the constant
term: they are the sums x = Σ b_y ω^y with b_0 ∈ Z and no negative
exponent (L'Innocente, Mantova, arXiv:1710.07304, which writes
ω = 2·ω/2 = 3·ω/3), so x − b_0 is n times an omnific integer and
x ≡ b_0 mod n; the map to Ẑ has image Z. The hyperintegers keep both,
the residues of the infinite element [n] chosen by the ultrafilter: Benci
and Di Nasso's numerosity gives a cofinite set of positive integers the
size α − k, and whether α is even depends on the ultrafilter
(Wenmackers, arXiv:2408.03344). A computable shadow is the big-M
method's a + bH, ordered by b first, with H's residues set to 0 here,
since the method has none. Made finite, H = M and 0 ≤ a < M, the pair
(b, a) is x in mixed radix, and an overflow of x + y, x and y in
[0, M), kept as a value is the high digit
⌊(x + y)/M⌋: the overflow bit itself, which the wall puts at no channel
and SIZE.md#the-least-key prices as one key compare.

## The hiding lemma
Tier: theorem.
Verifier: proof; size.py::section_h.

Let M be any modulus, W a proper divisor and c = M/W. In every fiber of
the window W the **sign-bit bias**, the number of the fiber's points at or
above M/2 less half the fiber's size, is exactly 0 when c is even and
exactly half an element in absolute value when c is odd. The cyclic
orientation of every triple of distinct points is undetermined by the
window.

Proof. The fiber of r mod W is the ladder r + jW, j < c. For even c
exactly c/2 points lie at or above M/2 = (c/2)W. For odd c the points
j ≥ (c + 1)/2 always do, and the point j = (c − 1)/2 does iff
r ≥ W/2, so the count is (c ± 1)/2. For orientation, translate the
triple's base point to 0; orientation becomes comparison of the other
two on (0, M). Each ladder holds a nonzero element at most W and one
at least (c − 1)W ≥ W, so pairing the extremes both ways gives both
orientations, unless both ladders' nonzero parts are {W} at c = 2,
where no distinct triple exists.

Neither squarefreeness nor a product is used; the hiding is a fact about
coarsening a cyclic group. On a rung Z/p_k# (TOWER.md#the-rung) the
bias is exactly 0 as soon as the channel 2 is unread. The script checks
every fiber of every proper window up to M = 240 and every orientation
class up to M = 60.

## The half-coverage law
Tier: theorem.
Verifier: proof; size.py::section_c.

Read x ∈ [1, X] through x mod Q, for any Q ≤ X. Exactly max(0, 2Q − X)
elements are determined, and some pair is ordered with certainty iff
2Q − X ≥ 2. So at or below half coverage, Q ≤ X/2, no element is
determined and no pair is ordered, whether or not Q divides X; a coarser
fact can still be certain, as residue 0 certifies x ≥ Q. When Q divides
X the best guess of [a < b] from the residues is right on exactly
X(X + Q − 2)/2 of the X(X − 1) ordered pairs.

Proof. The fiber of x has one lift iff x − Q < 1 and x + Q > X, which
holds for the 2Q − X elements of [X − Q + 1, Q]. Every fiber's least
lift is at most Q and its greatest exceeds X − Q, so two fibers are
ordered only if X − Q + 1 ≤ a < b ≤ Q for their lifts, which needs
2Q − X ≥ 2; then X − Q + 1 and X − Q + 2 are both determined. At
Q | X each fiber is a ladder of c = X/Q points. Two different fibers
compare one way on c(c + 1)/2 of their c² pairs, and a fiber with
itself splits its c(c − 1) ordered pairs evenly. Summed, the correct
guesses are X(X + Q − 2)/2.

A proper window of Z/M has W ≤ M/2, so it never passes half coverage. At
Q | X the guess is right with probability 1/2 + (Q − 1)/(2(X − 1)):
order leaks from the first nontrivial window, Q = 2, while certainty
waits for half.

## The conjunctive split
Tier: theorem.
Verifier: proof; size.py::section_r.

Call a relation on Z/M **conjunctive** when it equals the conjunction of
its projections to the channels. On a squarefree ring equality and
divisibility are conjunctive; with two channels or more the order
x ≤ y fails maximally, every projection being all of F_p × F_p. A
nonempty relation is conjunctive iff at every split of one channel
against the rest it is a rectangle, of Boolean rank 1.

Proof. Divisibility x | y means y = xz for some z, which by the CRT
holds iff y mod p = 0 wherever x mod p = 0, channel by channel. For the order,
the pairs with x < p ≤ y ≤ 2p − 1 < M all have x < y, and their
residues at channel p run over every pair, so the conjunction is
everything. For the criterion, a conjunction
of channel relations is a rectangle at every split. Conversely a
nonempty set that at every coordinate is the product of its projection and its
co-projection contains every point whose coordinates lie in the
projections: start from a point of the set and replace one coordinate
at a time.

Cyclic betweenness, the ternary relation on distinct a, b, w that holds
when (b − a) mod M < (w − a) mod M, so that b comes before w on the way
up from a around the cycle, is not conjunctive either. The slice of a
conjunctive relation at a fixed argument is a conjunction of channel
relations, hence conjunctive. At base point a = 0 betweenness slices to
0 < b < w, which is not: at every channel p the pair (1, 1) is
realized by (b, w) = (1, 1 + p), so the conjunction of projections
holds (1, 1), which the slice does not.
The script checks the three binary relations exhaustively at Z/210,
betweenness as a ternary relation at Z/6 and Z/30, and the rank
criterion at Z/30 on equality, divisibility and order.

## The least comparator
Tier: known.
Source: Babenko, Piestrak, Chervyakov, Deryabin, Electronics 10 (2021)
1041; Dimauro, Impedovo, Pirlo, IEEE Trans. Comput. 42 (1993) 608.

For pairwise coprime moduli m_1 < ⋯ < m_k with product M, a key is
a map sending each x ∈ [0, M) to a tuple of integers, its values are
ordered lexicographically, and a key compares exactly when that order
agrees with the order of x on [0, M). The key (⌊x/m_k⌋, x mod m_k)
compares exactly. The 2021 paper works with core
functions, weighted sums of the quotients ⌊x/m_i⌋. It
names ⌊x/m_k⌋ the minimum-range monotonic core function, shows that the
diagonal function D(x) = Σ ⌊x/m_i⌋ of 1993 is the core function with
every weight equal to 1, and argues that no core function of
smaller range compares.

## The least key
Tier: theorem.
Verifier: proof; size.py::section_q; size.py::section_d;
size.py::section_k.

Write x_i = x mod m_i for the residue at the modulus m_i, prime or not,
the moduli ordered m_1 < ⋯ < m_k as above, and keys compared as in
SIZE.md#the-least-comparator; among the keys (G(x), x mod m_j) that
compare exactly, over all G and all j, call one a **least key** when its
first coordinate takes the fewest values. For each j, whatever G is,
G takes at least M/m_j values, since the M/m_j elements of one class
mod m_j need distinct values.
⌊x/m_k⌋ attains that count, M/m_k values against the largest modulus
m_k, and it is one dot product of the residues modulo M/m_k: it equals
(B − x_k)·m_k⁻¹ there, B the CRT value of the other residues. Since
x = m_k⌊x/m_k⌋ + (x mod m_k), the key is x itself in mixed radix. Its
first coordinate is that dot product, one reconstruction modulo M/m_k
(the product of every modulus but the largest), and no exactly comparing
key (G(x), x mod m_j) has a first coordinate with fewer than M/m_k
values. Sign is one key compare against ⌈M/2⌉, and the overflow of x + y
is the compare key(z) < key(x) for z = x + y mod M. The key is handed
over as size.py's least_key(residues, moduli) and compare(a, b, moduli),
residue words in and the verdict out.

The diagonal is never the least for k ≥ 2, since D rises at every
multiple of m_1 and so takes at least M/m_1 > M/m_k values. Paired
with any residue it still keys exactly. D(x + 1) − D(x) counts the moduli
dividing x + 1, so inside a run of constant D every residue climbs
without wrapping, and (D(x), x mod m_j) is exact for every j. With
S = Σ M/m_i, gcd(M, S) = 1 and D < S, so D is one dot product mod S,
D ≡ −M⁻¹ Σ (M/m_i) x_i. It is narrower than a full reconstruction mod M
iff Σ 1/m_i < 1, which no rung Z/p_k# (TOWER.md#the-rung) from Z/30 on
meets, and it is never narrower than ⌊x/m_k⌋. The script checks the dot
product for ⌊x/m_k⌋ at every x of four sets, Z/510510 among them, where
M/m_k = 30,030 against S = 716,167, D's dot product at 2,000 seeded x of
each, and the rung sums Σ 1/p_i from k = 1 to 10.

## A published comparator against the least key
Tier: rule (proved from the pseudocode; no mismatch at 118,485
pairs).
Verifier: rns_compare.py::section_price; rns_compare.py::section_exact;
rns_compare.py::section_controls.

Didier, El Mrabet, Glandus and Robert (arXiv:2605.18415, 2026) compare
two residue numbers at any pairwise coprime moduli with one redundant
modulus m_a coprime to M. They convert the residues of (x − y) mod M to
mixed radix, reduce that value mod m_a, and answer x ≥ y iff it matches
the redundant channel's (x − y) mod m_a. If x < y the converted value is
x − y + M and differs from the redundant reading by M mod m_a, never 0.
So the redundant channel tests which way the difference wrapped and
computes nothing of it.

Against the least key, the method reconstructs once per compared pair.
It computes all n mixed-radix digits of the difference, n the number of
moduli without m_a; that digit map is one-to-one on [0, M), so it
carries log2 M bits. The least key instead reconstructs each operand
once, modulo every modulus but the largest, and is reused across every
comparison that operand enters; for a single comparison it
reconstructs twice, each modulo the product of n − 1 moduli, against
the method's one conversion over n: a count of reconstructions, not of
multiplications, which the script prices for the method alone.
Implemented from its Algorithms 1 to 3 it costs n(n − 1)/2 + (n − 1)
modular multiplications: 5, 27 and 35 at n = 3, 7 and 8. That is one
under the paper's Table 1, whose Algorithm 3 loop runs from the second
digit while its text counts n. The conversion it presents finishes in
n − 1 rounds even with its digits computed in parallel, each digit's
steps in turn and each step as soon as the digit it reads is final; the
table's O(log n) parallel time rests on a conversion the paper cites and
does not present.

The script runs the method against integer comparison at every pair of
{3, 5, 7} and {4, 9, 5} (m_a = 11 and 7) and at random pairs with a
corner list (equal values, differences of m_a and 2m_a, the ends of
the range) at the primes 2 to 17, at {15, 77, 221} with m_a = 4, and
at eight primes above 2¹⁶: no mismatch at 11,025 and 32,400 pairs
exhaustively and 50,020, 20,020 and 5,020 at random with the corners.
Its controls, a comparator that always answers ≥ and the method with
m_a = 15 dividing M = 105, each fail at all 5460 pairs with x < y.

## The additive labelling law
Tier: theorem.
Verifier: proof; size.py::section_a.

Carry size beside the residues in one small **labelling**: a map μ from
[0, N) into a set of s < N labels, not all of which need be used, that
addition keeps current, μ(x + y) a function of μ(x) and μ(y) whenever
x + y < N, say μ(x + y) = A(μ(x), μ(y)). Then μ(x + 1) = A(μ(x), μ(1)),
so μ is one point's orbit under the self-map A(·, μ(1)) of an s-set:
exact on a prefix [0, x₀) and periodic with period d after it,
x₀ + d ≤ s. Each such pair is a congruence of ([0, N), +), its quotient
the cyclic monoid of index x₀ and period d, so up to relabelling there
are exactly s(s + 1)/2 such labellings once N > s, and multiplication
keeps each of them current for free. Every label appears below x₀ + d,
so a value below x₀ is read exactly off its label, while at or above x₀
a label names a value only up to a multiple of d, and two values u < v
at or above s are never ordered by their labels: v's label already
labels a value below x₀ + d ≤ s ≤ u. A labelling that orders the values
0 to h carries more than h labels, and the one escape left to a
labelling addition keeps is a label map allowed to be wrong somewhere on
the range. On Z/M with wraparound, a labelling addition keeps exactly
has a group congruence for fibers, the cosets of a subgroup, so it is
reduction mod some m | M, which multiplication keeps too: one more
residue. A depth-first search over every labelling at N = 8, 10, 12, 14
and s from 2 to 5, assuming no shape, finds exactly the 136 the count
predicts.

## The F₂[x] control
Tier: theorem.
Verifier: proof; size.py::section_f.

Over F₂[x]/f, f squarefree with at least two irreducible factors, read a
as its representative of degree below deg f. The locality criterion
holds as stated, and the top degree bit [deg a = deg f − 1] is
channel-local at no channel, so the wall's core is unchanged. Three
things the Z side has are gone:

- The sign-bit bias, with the top degree bit as the sign, is 0 at every
  proper window, where over Z it is half an element whenever M/W is odd.
- In F₂[x] the degree of a product is the sum of the degrees, with no
  carry.
- The partial-fraction read is exact or says it cannot tell. The t
  leading Laurent coefficients of a/f, summed over the channels, give
  deg a exactly or are all zero, and zero means deg a < deg f − t. Over
  Z, an integer y ∈ [0, M) with residues y_i = y mod m_i has
  y/M = frac(Σ y_i w_i/m_i) with w_i = (M/m_i)⁻¹ mod m_i, and the sum of
  the terms' t-bit truncations can wrap below 0 and read a small y as a
  large one, with no flag.

Proof. The wall: for f_i ≠ f, 0 and f_i x^(deg f − 1 − deg f_i) agree
mod f_i. The bias: a fiber of the proper window g | f is a coset
r + g·P, P running over the polynomials of degree below
e = deg f − deg g ≥ 1, and the top bit is 1 exactly where P's
coefficient at x^(e − 1) is set, on half the coset. The degree: F₂[x]
is a domain, and leading coefficients multiply. The read: write
a/f = Σ b_i/f_i in partial fractions, deg b_i < deg f_i; a sum of
proper fractions is proper, so the integer parts of the b_i x^t/f_i add
without carries to (a x^t) div f, whose
degree is deg a + t − deg f when that is nonnegative, and which is 0
otherwise.

Which difference owns what, as a reading of the proofs rather than a
further theorem. Z and F₂[x] differ twice: Z has an archimedean place
and F₂(x) does not, since degree reads its place at infinity, and Z has
characteristic 0 where F₂[x] has 2. The zero bias is the place's. Over
every F_q[x], deg(r + g·P) = deg g + deg P for P ≠ 0 and every r of
degree below deg g, which is the ultrametric inequality at infinity. So
at every degree from deg g up, every fiber of a proper window has the
same degree profile, the whole ring's share at each degree, and a window
reads nothing of a degree there. Over Z the absolute value is not
ultrametric, r + jW exceeding max(r, jW) once both are nonzero, and the
share moves by half an element at odd M/W. Carries go with the
characteristic instead: the 2-adic integers carry with no archimedean
place, and the silent miss rides on the carries. The information wall of
COORDINATES.md, no channel-local read deciding size, needs neither. The
script checks all 31 proper windows, every a and every t from 1 to
deg f = 10 at f = x(x + 1)(x² + x + 1)(x³ + x + 1)(x³ + x² + 1), the
degree profile at all 15 proper windows of
x(x + 1)(x² + 1)(x² + x + 2) over F₃, and finds the Z wrap at y = 1
at Z/510510 with 16 bits.

## Open fronts

The additive labelling law leaves one escape, a label map allowed to be
wrong somewhere on the range. Open: where must such a label map err, and
how much of the range can it keep correct, derived rather than measured?
The labellings that addition keeps current on the whole range are all
counted by the law.
