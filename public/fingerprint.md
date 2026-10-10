# FINGERPRINT — one real number reads a residue tuple up to sign

The object: the cosine sum Θ_M(n) of a residue n over the prime-power
factors of any modulus M. It is two things at once: 2k minus the squared
chord distance from 0 to the point n on the torus that draws each of the
k **channels**, n mod q for the prime-power factors q of M, as a unit
circle, and an eigenvalue of the channel-step graph. It forgets the sign in
each channel and nothing else. The primorials Z/p_k#, the products of
the first k primes, are one squarefree case; the proof needs only that
the factors are powers of distinct primes.

## The fingerprint
Tier: property.
Verifier: fingerprint.py::section_g; fingerprint.py::section_c;
fingerprint.py::section_e.

Let M = q_1 q_2 ⋯ q_k with the q_j powers of k distinct primes, so that
Z/M is read through the k channels n mod q_j. The **fingerprint** of n is
the real number

```
Θ_M(n)  =  Σ_j 2cos(2πn / q_j),
```

a function of the channels alone. The **sign class** of n at q_j is the lesser
of n and −n mod q_j, between 0 and q_j/2, and Θ_M depends only on the
class tuple, so changing the sign of n in any one channel leaves it
unchanged. Those sign changes are multiplication by the **sign group**
G_M = {g : g ≡ ±1 mod every q_j}, of order 2 to the number of factors
above 2.

Θ_M has two other readings, both by construction.

The torus. Draw channel j as q_j points on a unit circle and Z/M as the
product of the circles. Since 2cos t = 2 − 4sin²(t/2),

```
Θ_M(n)  =  2k − |d(n)|²,      |d(n)|²  =  Σ_j 4sin²(πn / q_j),
```

where |d(n)|² is the squared chord distance from 0 to the point n. The
fingerprint is that squared distance, measured down from 2k.

The spectrum. The **channel-step graph** is the Cayley graph of Z/M whose
steps are ±1 in one channel, the product of the cycles C_{q_j} (at
q_j = 2 the two steps coincide and the edge is counted twice). Its
eigenvectors are the characters ψ_m(x) = exp(2πi Σ_j m_j x_j/q_j),
with x_j = x mod q_j, labelled by CRT coordinates m_j = m mod q_j, and
ψ_m's eigenvalue is Θ_M(m). The label matters: the additive character
x ↦ exp(2πi mx/M) is ψ with coordinates m·u_j, where u_j is the inverse
of M/q_j mod q_j, so its eigenvalue is Θ_M at the twisted label.
Along the primorials, through Z/30 every u_j is ±1 and the twist
moves no label up to sign; it first moves one at Z/210, where u = 3 at
5 and u = 4 at 7. Off them it can bite sooner: at Z/15, u = 2 at 5.

## The fingerprint theorem
Tier: theorem; observation (the least gaps between fingerprints).
Verifier: proof; fingerprint.py::section_r; fingerprint.py::section_z;
fingerprint.py::section_e; fingerprint.py::section_g.

For every modulus M, Θ_M(n) = Θ_M(m) iff m = gn for some g in the sign
group: n and m agree in every channel up to sign, independently. So
the distinct fingerprints number

```
Π_j (⌊q_j / 2⌋ + 1),
```

each prime power q multiplying the count by ⌊q/2⌋ + 1. Two equivalent
statements follow: on the torus, the chord distance from the origin
fixes a point of Z/M up to reflecting each circle; in the spectrum, each
eigenvalue's multiplicity is the size of one sign orbit, so each
eigenvalue is as simple as multiplication by the sign group allows. At
Z/510510, for instance, 18,144 real numbers name 18,144 orbits, the
largest of 64 elements.

The proof has three steps. Suppose two class tuples give one sum, and
let δ_j = 2cos(2πc/q_j) − 2cos(2πc′/q_j), c and c′ being the two
tuples' sign classes at q_j, so that the δ_j sum to 0.

Isolation. The prime powers are coprime, so the Galois group of
Q(ζ_M) is the product of the groups of the Q(ζ_{q_j}). Average the
vanishing sum over the subgroup fixing ζ_{q_j}: δ_j is fixed and every
other channel's difference becomes its average over its own group, a
rational number. So every δ_j is rational.

One channel. At q = p^e, the value 2cos(2πc/q) generates the real
subfield of Q(ζ_{p^a}) with p^a = q/gcd(c, q), its **exact level**, and
irrational values of different exact levels generate fields of different
degree. A rational difference of two irrational values puts both in one
field, where values of one exact level are Galois conjugates with one
common trace, so the difference equals its own average, 0. A rational
minus an irrational value is irrational. So a nonzero rational δ_j needs
two rational values, and by Niven's theorem (I. Niven, Irrational
Numbers, 1956, Corollary 3.12) the rational values of 2cos at rational
multiples of 2π are 2, 1, 0, −1 and −2. Hence the nonzero rational
differences are ±4 at q = 2; ±2 and ±4 at the larger powers of 2 (values
2, 0, −2); ±3 at the powers of 3 (values 2, −1); and none at a power of
any p ≥ 5. Within a channel 2cos is strictly decreasing on the class
range, so δ_j = 0 means equal classes.

The clash. Only the 2-power and the 3-power channels can carry a
nonzero δ, and there is at most one of each. A zero sum then needs a
difference in {0, ±2, ±4} at the 2-power channel to cancel one in
{0, ±3} at the 3-power channel, so both are 0 and every class agrees.

At q = 2 the set is read by hand: the values are 2 and −2, so the
differences are ±4. The script checks the middle step exactly, in
integer arithmetic, at every prime power 3 ≤ q ≤ 200. For each it builds
the minimal polynomial of 2cos(2π/q), certifies it irreducible, and
reduces every pair difference modulo it; a pair's difference is rational
iff the reduction is constant, so the rational-difference set is read
with no float anywhere. The 59 computed sets of rational differences
between distinct classes are exactly as the one-channel step says:
nonempty at every power of 2 from 4 and of 3, and empty elsewhere, the
four at 3, 4, 8 and 9 read first as a positive control. The last step
uses that the primes are distinct: two channels at one prime can
cancel, as channels 2 and 4 do (−4 against 4) and channels 3 and 9 do
(−3 against 3). In floats, the class tuples' fingerprints are distinct
at ten moduli, the seven primorials Z/2 to Z/510510 and 8·9·5·7·11,
16·27·5·7 and 4·9·25·49, which is the statement there,
and the fibre through every n is its sign orbit at Z/210, Z/2310, Z/360
and Z/900.

The theorem is exact in the reals and costly in digits. Reading n's sign
orbit back off Θ_M needs an error below half the least gap between
fingerprints, and that gap, computed, falls from 1 at Z/6 to 1.9 × 10⁻⁷
at Z/510510: the one number carries every channel. The gap falls
with the count of class tuples, but not in step: 16·27·5·7,
8·9·5·7·11 and Z/30030, at 1512, 1800 and 2016 class tuples, have the
gaps 4.3, 6.5 and 6.8 × 10⁻⁶, and 4·9·25·49, four channels and 4875
class tuples, has 3.0 × 10⁻⁷, below Z/30030's at six channels.
