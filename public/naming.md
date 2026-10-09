# NAMING — which primes divide a set's Euler characteristic

The object: a finite set S of primes, its ring Z/N with N the product
of S, and the clique complex X(S) of that ring's Hamming graph: the
complex's homotopy type, the integer −χ(S) it hands over, the weight
law deciding which primes outside S divide that integer, with bounds
on how often and how soon they do, how the answer sits along a smaller set, and
why no automorphism of prime order outside S realizes it as a cover.
When S is the first k primes its ring is the rung Z/p_k#, and the
page says so wherever it reads the set that way; the complex needs no
primes at all.

## The complex
Tier: theorem.
Verifier: proof; naming.py::section_x.

Let n_1, …, n_m ≥ 2 and N = n_1 ⋯ n_m. The **Hamming graph** on the
N tuples joins two tuples that differ in exactly one coordinate, the
Cartesian product of the complete graphs K_{n_i}; for a set S of primes
it joins two residues of Z/N that differ in exactly one channel, the
residue mod one prime of S. Its
**clique complex** X fills in every clique. Then X is homotopy equivalent
to a wedge of circles, with

```
b1  =  1 + N (m − 1 − Σ 1/n_i),      b_j = 0 for j ≥ 2,
−χ  =  N (m − 1 − Σ 1/n_i)  =  b1 − 1.
```

Proof. If u, v differ in coordinate i and v, w in coordinate i′ ≠ i,
then u, w differ in both and are not adjacent, so every clique lies in
a line, the set of all tuples agreeing with one tuple off one
coordinate. The maximal
cliques are the L = Σ N/n_i lines, two lines meet in at most one
vertex, and each vertex lies on m lines. Replace each line's simplex
by the cone on its vertices: both are contractible and glued along the
same vertices, so X is homotopy equivalent to the vertex–line graph,
bipartite and connected, with N + L vertices and mN edges. Its first
Betti number is mN − (N + L) + 1.

b1 = N holds at sizes {2, 3, 5}, where both are 30, and nowhere else:
b1 = N means Σ 1/n_i = m − 2 + 1/N, sizes ≥ 2 cap the left side at
m/2 and so force m ≤ 3, m = 1 and m = 2 have none (m = 1 puts
−1 + 1/N on the right, below the left's 1/N, and m = 2 asks
n_1 + n_2 = 1), and at m = 3 the sum
exceeds 1, so the least size is 2 and (n_2 − 2)(n_3 − 2) = 3.

The script computes the Betti numbers b0 to b3 over GF(2) from
boundary ranks,
with the cliques found from adjacency alone and never from lines, on
twenty size tuples up to (2, 3, 5, 7), where b1 = 384, after three
control complexes including a 2-sphere; it lists the maximal cliques
and searches size multisets for b1 = N.

## The naming integer
Tier: property.
Verifier: proof; naming.py::section_i.

For a set S of m primes with product N, the **naming integer** is −χ(S),
minus the Euler characteristic of the complex X(S):

```
−χ(S)  =  N (g − 1),      g  =  Σ_{p ∈ S} (1 − 1/p).
```

A prime s outside S names S when s divides −χ(S). Members never
divide it: modulo a member p, every term of N(m − 1) − Σ_{r ∈ S} N/r vanishes
except −N/p, which is prime to p. And 2 never names: when every member is
odd, −χ ≡ (m − 1) − m = −1 (mod 2). A single prime has −χ = −1 and
names nothing; Z/pq has −χ = (p − 1)(q − 1) − 1, and Z/30 has
−χ = 29. For the rung's primes, the first k, −χ is prime to every
prime up to p_k and exceeds 1 from k = 3, so all its prime factors lie
beyond p_k: Euclid's argument.

The quantity g is also the mean Hamming distance from any residue of
Z/N, since a uniform residue differs from a fixed one at p with
chance 1 − 1/p, so −χ is the sum over x in Z/N of (d(0, x) − 1),
with d the Hamming distance, the number of channels where two residues differ.
This is a recount, not a second fact: both sides count mN − N − L.

## The weight law
Tier: criterion.
Verifier: proof; naming.py::section_w.

A prime s outside S names S iff the weights

```
w_s(p)  =  1 − p⁻¹   (mod s)
```

of the members of S sum to 1 in Z/s. Proof: N is invertible mod s,
so s divides N(g − 1) iff g ≡ 1 (mod s), and g read in Z/s is the sum
of the weights.

Naming is one linear equation over Z/s on the indicator vector of S,
and it reads each member only through its residue mod s. A member
p ≡ 1 (mod s) has weight 0 and can be added or removed without
changing whether s names S. At s = 2 every odd prime has weight 0, the
law's form of "2 never names". At s = 3 the weights are 0 (p ≡ 1) and
2 (p ≡ 2), so 3 names a set S without 3 iff the number of members
≡ 2 (mod 3) is ≡ 2 (mod 3).

The same law answers the question for a whole pool. A pool of primes
without s has a subset that s names iff 1 is a subset sum of the pool's
weights; the empty sum is 0, so no empty set slips in. The script
checks the law over all 21,202 pairs of a nonempty set from the first
nine primes and a prime s ≤ 200 outside it, where the weight p⁻¹ in
place of 1 − p⁻¹ fails 962 times.

## Every odd prime names a set
Tier: theorem; rule (the first rungs, verified at every odd prime
s < 200).
Verifier: proof; naming.py::section_w.

Every prime s ≥ 3 names some subset of the first k primes once
those primes include s − 1 primes other than s that are not ≡ 1
(mod s). Proof: by the Cauchy–Davenport theorem, adding a nonzero
weight w to a set A of subset sums in Z/s gives A ∪ (A + w) with at
least min(s, |A| + 1) elements, so s − 1 nonzero weights reach every
residue, 1 included. Dirichlet's theorem supplies such primes, so
every odd prime names a set at some rung and at every later one.

The proved rung is the one holding s − 1 primes of nonzero weight, and
for s below 200 the measured one meets it only at s = 3. Over the odd
primes s below 200 the first rung at which s names a set runs from 3
to 9, 41 arriving at rung 8 through −χ({17, 19}) =
287 = 7 · 41, and the two ways of reading it, the scan of −χ over
every subset of the first twelve primes and the walk of subset sums of
the weights, agree at every one. How late a prime can first name a
set, between the few rungs measured and that proved rung, is open.

## The baseline
Tier: theorem.
Verifier: proof; naming.py::section_b.

Over a pool P of primes not containing s, the number of subsets that s
names is 2^|P|/s up to an error, by the characters of Z/s:

```
| #{S ⊆ P : s names S} − 2^|P|/s |
      ≤  ((s − 1)/s) · 2^|P| · max_{j ≠ 0} Π_{p ∈ P} |cos(π j w_s(p) / s)|.
```

Each factor with w_s(p) ≠ 0 is at most cos(π/s) < 1, so the naming
fraction, the share of the pool's subsets that s names, tends to 1/s
exponentially in the number of pool primes not ≡ 1 (mod s), while a
pool made only of primes ≡ 1 (mod s), all of weight 0, names nothing.
The script reads ten pools, the first 6 and the first 9 primes other
than s for each prime s from 3 to 13, each count inside its bound (at
s = 13 over six primes the bound exceeds 2^6/13, so only its upper
side tests),
and the weight-0 pool of primes ≡ 1 (mod 3) below 50 at exactly 0.

## The slices
Tier: theorem.
Verifier: proof; naming.py::section_s.

For a nonempty T inside S, fixing the coordinates of S ∖ T cuts the
vertices of X(S) into c = N_S/N_T classes, N_S and N_T the products of
S and T, and each class induces a copy of X(T), a slice. Their first
homology injects jointly into X(S)'s:

```
H1(X(T))^c  ↪  H1(X(S)),      rank c · b1(T).
```

Proof: the equivalence of the complex above is built line by line, so
it restricts to each slice, and in the vertex–line graph the slices are
disjoint subgraphs, each
its vertices and its T-lines, and a subgraph's cycle space is a
subspace of the graph's. The count
b1(S) − 1 = c(b1(T) − 1) + N_S Σ_{p ∈ S∖T} (1 − 1/p) is the naming
integer's algebra, and read against the weight law it says that for s
outside S naming T, s names S exactly when the weights of S ∖ T sum to
0 mod s. The injection is what the slices add beyond that count.
The script computes the image rank over GF(2) at all 50 pairs with T a
proper subset of S inside {2, 3, 5, 7}, after a control whose cycles are
boundaries and map to rank 0. Of the 50, the 22 whose T has two or more
primes test a nonzero
rank; the rest have b1(T) = 0.

## No free automorphism of outside prime order
Tier: theorem.
Verifier: proof; naming.py::section_a.

A prime s outside S names S iff b1(S) − 1 is a multiple of s, iff
X(S) is homotopy
equivalent to an s-fold cover of a connected graph: an s-fold cover
multiplies the Euler characteristic by s, and a wedge of 1 + s(β − 1)
circles is an s-fold cover of a wedge of β circles. No simplicial
automorphism of X(S) supplies the cover, whose deck group fixes no
point: every automorphism of prime order s, for s outside S, fixes a
vertex. Proof: the factors K_p are prime for
the Cartesian product and pairwise non-isomorphic, so the automorphisms
are the products of permutations of each coordinate (Sabidussi); a
coordinate's permutation of order s has p − s·(its number of s-cycles)
fixed points, never 0 since s does not divide p. The script counts 12
automorphisms at sizes (2, 3) and 8 at (2, 2), where equal factors
swap; finds no element of order s without a fixed vertex at the three
pairs ({2, 5, 7}, 3), ({3, 5, 7}, 2) and ({2, 3, 7}, 5); and at s = 5
inside {2, 5, 7}, where the hypothesis fails, finds 12,120 without
one. Each still fixes a point: its coordinate at 2 is the identity and
its coordinate at 7 fixes a residue, since 5 does not divide 7, so it
maps the line along 5 through those two to itself and fixes the centre
of its simplex, as it must, since no member of S divides −χ(S).
