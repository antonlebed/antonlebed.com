"""
explore_embedding.py -- the surface->ring EMBEDDING: can a native rule map raw
strings to ring elements so a grammatical transform becomes multiplicative?

THE QUESTION. explore_vsa_encoder.py established that the ring gives exact
COMPOSITION (bind = multiply, unbind = meadow inverse) and the analogy machinery
even EXTRACTS the shared transform from data (T = form(anchor, c) *
form(anchor, cite)^-1, the lexeme cancels), so held-out (lexeme, cell) analogies
complete at 1.000 -- PROVIDED the paradigm arrives already arranged as ring units
form(lex, cell) = L_lex * K_cell. The one unlearned, data-facing piece it left
open is the EMBEDDING: the map phi from SURFACE FORMS (strings) to ring elements.
Real morphology hands you strings ("walk", "walked", "walks"), not ring units.
Can a RING-NATIVE (exact, non-gradient) rule supply an embedding under which a
grammatical transform is multiplicative and unbindable, so the analogy machinery
generalizes to held-out lexemes from RAW STRINGS -- without a hand-given codebook
AND without re-importing the deleted archimedean similarity metric?

THE KEY OBJECT. The natural native embedding is the MONOID HOMOMORPHISM
  phi_hom(s) = prod_{symbol in s} u[symbol]   (mod N)
-- assign each alphabet symbol a fixed ring UNIT u[symbol], map a string to the
PRODUCT of its symbols' units (empty string -> 1). Because it is a homomorphism,
phi_hom(stem . suffix) = phi_hom(stem) * phi_hom(suffix), so for CONCATENATIVE
(stem + affix) morphology the extracted transform
  T_cell = phi_hom(anchor_cell) * phi_hom(anchor_cite)^-1 = phi_hom(suffix_cell)
           * phi_hom(suffix_cite)^-1
is LEXEME-INDEPENDENT (the stem cancels), so a held-out lexeme completes exactly
from the STRUCTURAL embedding -- no per-lexeme codebook, no metric. This is the
unit-encoding cure of explore_vsa_encoder.py lifted to strings: a GENERIC
structural constraint (alphabet -> units), not a per-task codebook.

THE RING. RAD = Z/510510 (k = 7, factors {2,3,5,7,11,13,17}); exact binding and
the meadow laws carry on any product of fields, so RAD suffices. Alphabet symbols
map to random units; position-tagged variants map (symbol, position) to units.

THE THREE SPLITS (the native/blind boundary, at the embedding level).
  1. CONCATENATIVE (stem + affix string): phi_hom -> shared exact transform
     (SURVIVE). But ring multiply is COMMUTATIVE, so phi_hom is ORDER-BLIND
     (bag-of-symbols): anagram surface forms collide (spot/post/stop/tops/pots
     -> one element), and prefixation is indistinguishable from suffixation of
     the same morphemes. Composition native, ORDER lost -- the ring's native
     blind spot, at the embedding.
  2. POSITION-TAGGED phi_pos(s) = prod_i u[(s[i], i)] restores order (anagrams
     separate), BUT the affix now sits at stem-length-dependent positions, so
     T_cell depends on stem length -> the shared transform BREAKS unless every
     stem has equal length. Order and shared-transform EXCHANGE.
  3. FUSIONAL (vowel mutation / suppletion: foot->feet, go->went -- no shared
     substring transform): phi_hom gives no shared transform, so held-out
     analogy fails (KILL). Rescuing it needs either a per-lexeme CODEBOOK
     (covers only SEEN lexemes -> no held-out generalization) or a stem-
     SIMILARITY metric (which stems pattern together -- the DELETED archimedean
     gradient). Either way a re-import.

THE HAND-DERIVATION (frozen pre-engine; adjudicated in the RUN RECORD).
  Convention (re-derived from the engine, never remembered): phi_hom(s) = prod(u[c] for c in s) mod N,
  empty -> 1; u[c] a fixed random unit per symbol. Transform sending the citation
  cell to cell c: T_c = phi(anchor_c) * inv(phi(anchor_cite)) (inv = pow(., -1, N),
  exact since phi of a unit product is a unit). Applied to query lexeme q:
  pred = T_c * phi(q_cite); correct iff pred == phi(q_c).
  Concatenative hand check (letters as units): stem "wk", cite suffix "", cell
  suffix "ed"; anchor stem "wk", query stem "jm".
    phi(wk) = u_w u_k; phi(wked) = u_w u_k u_e u_d; T_ed = phi(wked) phi(wk)^-1
    = u_e u_d. query phi(jm) = u_j u_m; pred = T_ed phi(jm) = u_e u_d u_j u_m
    = phi(jmed) = phi(jm . ed). EXACT.
  Order-blind hand check: phi(spot) = u_s u_p u_o u_t = phi(stop) = phi(tops)
    (same multiset) -- distinct anagrams share one ring element; and
    phi("re"+stem) = phi(stem+"re") -- prefix vs suffix indistinguishable.
  Fusional hand check: T from foot->feet = phi(feet) phi(foot)^-1
    = (u_f u_e u_e u_t)(u_f u_o u_o u_t)^-1 = u_e^2 u_o^-2; applied to go
    (u_g u_o): pred = u_g u_e^2 u_o^-1 != phi(went) -- the transform is not
    shared, analogy fails under phi_hom.

PREDICTIONS (fixed before the run; adjudicated post-run in the RUN RECORD).
  PR1 (concatenative SURVIVE; ~rule). phi_hom completes held-out analogies at
      1.000 on concatenative paradigms with DISTINCT (non-anagram) stems, from
      raw strings, with no per-lexeme codebook. A non-homomorphic control (a
      random unit per distinct string) scores ~0 -- the lift rides the
      homomorphism, not the format.
  PR2 (order cost; observation). Order-blindness surfaces as phi_hom
      NON-INJECTIVITY (anagram forms -> one ring element; prefix/suffix homophony),
      NOT an analogy-accuracy drop (colliding forms map to one element, so the
      exact-match check still passes each). Measured as the phi collision count =
      the embedding's information loss.
  PR3 (position-tag trade; observation + rule). phi_pos restores order (zero
      anagram collisions) but the shared-transform completion falls to ~0 when
      stem lengths VARY, holding 1.000 only at FIXED stem length -- order and
      shared transform exchange.
  PR4 (fusional KILL; observation). phi_hom completes held-out fusional analogies
      at ~0 (transform not shared). RESCUE CONTROL (the real-null proof): an
      embedding that RESPECTS the fusional relation (forms built as L_lex * T_cell)
      restores 1.000, and a codebook trained on SEEN lexemes completes seen at
      1.000 but held-out at 0 -- so the rescue re-imports either the deleted
      similarity metric or a codebook that does not extend to held-out. PR4's null
      is a live rig (PR1's 1.000), not a dead one.

THE KILL-SHAPE (printed observable). PR4 fires (fusional phi_hom ~0) AND PR1
fires (concatenative phi_hom 1.000 -- rig alive) AND the rescue control restores
fusional to 1.000 (the null is real, generalization returns only with the
re-imported structure). THE SURVIVE-SHAPE: some native, non-metric, codebook-free
rule generalizes held-out FUSIONAL forms.

POSITIVE CONTROLS (run before any verdict is read). (a) the homomorphism law
phi_hom(s . t) == phi_hom(s) * phi_hom(t) on samples. (b) the hand pair: T_ed
applied to "jm" yields phi("jmed") exactly. (c) the anagram collision count equals
the number of multiset-equal surface-form classes. (d) unit inverse:
phi(s) * inv(phi(s)) == 1 on sampled forms. (e) the fusional rescue restores 1.000.

FINDINGS (tiers inline; run record below; all sections assert).

1. THE CONCATENATIVE EMBEDDING IS NATIVE AND CODEBOOK-FREE (rule, mechanism-proved
   + S1). The char-product homomorphism phi_hom completes every held-out
   (lexeme, cell) analogy at 55/55 = 1.000 on a concatenative paradigm read from
   RAW STRINGS, while a non-homomorphic control (a random unit per distinct surface
   string) scores 0/55 = 0.000. The mechanism is an algebraic identity:
   phi_hom(stem . suffix) = phi_hom(stem) * phi_hom(suffix), so the extracted
   transform T_cell = phi_hom(suffix_cell) * phi_hom(suffix_cite)^-1 is
   lexeme-independent -- the stem cancels exactly, as in the citation-form unbind of
   explore_vsa_encoder.py, but now the embedding is STRUCTURAL (assign each alphabet
   symbol a unit), not a per-paradigm codebook. So the surface->ring embedding is
   FREE for concatenative morphology: the analogy machinery runs on raw strings with
   no learned per-lexeme table and no similarity metric.

2. THE PRICE OF THAT EMBEDDING IS ORDER-BLINDNESS (rule + observation; S2). Ring
   multiplication is commutative, so phi_hom is a BAG-OF-SYMBOLS map: it is
   NON-INJECTIVE on anagrams (13 surface forms collapse to 3 distinct ring values =
   3 multiset classes, 10 collisions) and cannot distinguish prefixation from
   suffixation of the same morphemes (phi("re"+stem) == phi(stem+"re") for 3/3
   stems). Crucially this is INFORMATION LOSS in the embedding (distinct strings ->
   one element, so the ring form cannot be DECODED back to its string), NOT an
   analogy-accuracy drop -- colliding forms map to one element, so the exact-match
   completion still passes each. Composition is native; ORDER is the deleted content,
   at the embedding level -- the same blind spot the vehicle carries throughout.

3. ORDER AND THE SHARED TRANSFORM EXCHANGE (rule + observation; S3). The
   position-tagged embedding phi_pos(s) = prod_i u[(s[i], i)] RESTORES order (4
   anagrams -> 4 distinct values), curing finding 2 -- but it BREAKS the shared
   transform: the affix now sits at stem-length-dependent positions, so T_cell is
   lexeme-independent only when stems share a length. phi_pos completes held-out
   analogies at 33/33 = 1.000 on FIXED-length stems and 0/33 = 0.000 on
   VARYING-length stems (the rig gives the anchor a UNIQUE length so the collapse
   is exact and seed-robust; without that the transfer accuracy is the fraction of
   stems sharing the anchor's length -- same mechanism, a less clean number).
   Order-faithfulness and the lexeme-free transform are traded across these two
   NATURAL embeddings -- the two-poles exchange of explore_dual_merge.py (a native
   division reads unbounded branching but flat-role independence dies to carry it),
   here reappearing at the surface->ring map itself; an echo across two constructions,
   not a proof that no embedding holds both.

4. THE FUSIONAL EMBEDDING HITS THE DELETED METRIC (observation at scope; S4). On
   suppletive fusional morphology (idiosyncratic cell forms sharing no substring
   transform), phi_hom completes held-out analogies at 0/33 = 0.000 -- the transform
   is genuinely lexeme-specific, so no homomorphic embedding shares it. The null is a
   LIVE rig, not a dead one: finding 1's 1.000 shows the machinery generalizes when a
   shared transform exists, and a RESCUE embedding that respects the relation by
   construction (forms built as L_lex * T_cell) restores 33/33 = 1.000. But that
   rescue is a re-import: a codebook trained on SEEN lexemes completes seen forms at
   15/15 = 1.000 and held-out forms at 0/18 = 0.000 (a held-out lexeme has no learned
   code), and reading a held-out fusional form off the surface into an L_lex that
   makes its transform shared requires knowing which stems pattern together -- a stem
   SIMILARITY gradient, the deleted archimedean metric. So fusional generalization is
   recoverable only by supplying the deleted structure.

THE VERDICT. The surface->ring embedding SPLITS on morphological type exactly along
the vehicle's native/blind boundary. For CONCATENATIVE morphology the embedding is
FREE: a char-product homomorphism (a generic structural constraint, not a codebook)
makes the paradigm exactly multiplicative and the analogy machinery of
explore_vsa_encoder.py runs on raw strings with held-out generalization at 1.000 --
so the last data-facing piece of the learning redesign is native for the
order-invariant half of morphology. But every escape from the two limits routes back
to a wall the vehicle already has: order-faithfulness costs the shared transform
(finding 3 = the two-poles exchange), and suppletive (non-concatenative) generalization
costs the deleted similarity metric (finding 4 = the archimedean re-import; the
partial-regularity fusional case — inflection classes — is a reopen, below). This
unifies the embedding frontier with the resource-forced deletion of the archimedean
place: the two NATURAL embeddings each pay one side -- the homomorphism shares the
transform but loses order, the position-tagged embedding keeps order but breaks the
transform -- so the order/composition exchange the dissolution casts proved (for
unbounded branching vs flat-role independence; explore_dual_merge.py,
explore_noncommutative_merge.py) REAPPEARS at the string->ring map. This is an ECHO
across two constructions, not a fresh impossibility proof: no claim that NO embedding
does both, only that the two native ones each pay the same tax the deleted place
charges. The learning-redesign
hunt, as framed around growth and encoding, is near-exhausted: the ring supplies
exact composition, the analogy machinery extracts the transform, and the embedding is
native for concatenative structure -- the residue that is NOT native (order, fusion)
is precisely the deleted archimedean content, not a missing learning rule. Honest
limit: toy scope (RAD, a Latin alphabet, these paradigm families, suppletion as the
fusional extreme); the homomorphism identity and the position-length trade are rules
(mechanism-proved), the generalization rates, the collision counts, and the fusional
verdict are observations at scope. Reopen-guard: a native, non-metric, codebook-free
rule that generalizes held-out FUSIONAL forms -- e.g. a partial-regularity
(inflection-class) embedding whose class assignment is itself ring-native.
(Settled 2026-08, explore_similarity_carrier.py: the guard fired for
TAXONOMY-SHAPED inflection classes -- agreement depth along the tower
filtration reads a ball-constant class exactly, so held-out fusional forms
complete with no metric and no codebook; what that carrier provably refuses
is non-ultrametric similarity, the chain shape. This finding's own scope
survives: reading class membership off the SURFACE still costs what it says.)

RUN RECORD (python explore_embedding.py, ~1 s, trivial memory):
  S0 controls: homomorphism law (2000); hand pair T_ed*'jm' == phi('jmed'); anagram
     11 forms -> 4 distinct phi == 4 classes; phi(s)*inv == 1 (500)
  S1 concat:   phi_hom held-out 55/55 = 1.000; non-homomorphic control 0/55 = 0.000
  S2 order:    13 forms -> 3 distinct phi (10 collisions); prefix/suffix homophony 3/3
  S3 postrade: phi_pos anagrams 4 -> 4 (order restored); fixed-len 33/33 = 1.000;
     varying-len 0/33 = 0.000
  S4 fusional: phi_hom 0/33 = 0.000; rescue (relation-respecting) 33/33 = 1.000;
     codebook seen 15/15 = 1.000, held-out 0/18 = 0.000
  TOTAL 2512 checks, exit 0.

ADJUDICATION vs the predictions fixed before the run (git history). All four
predictions landed as derived. PR1 (concatenative 1.000, control 0) and PR3 (position
tags: fixed-length 1.000, varying-length 0) and PR4 (fusional 0; rescue and codebook-
on-seen 1.000, codebook-on-held-out 0) landed exactly. PR2 landed in its
HAND-ATTACK-CORRECTED form: order-blindness surfaces as phi NON-INJECTIVITY (10
anagram collisions, prefix/suffix homophony), not as an analogy-accuracy drop -- the
first framing of PR2 (an accuracy drop proportional to the anagram fraction) was
caught wrong on paper before the engine, because colliding forms map to one ring
element and the exact-match check still passes each. No engine surprise this run; the
pre-engine hand-attack absorbed the one design error.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import random
from math import prod, gcd
from collections import Counter

CHECKS = 0

N = 510510                                  # RAD modulus
FACTORS = [2, 3, 5, 7, 11, 13, 17]          # RAD channels
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
MAXLEN = 16                                  # position tags 0..MAXLEN-1


def check(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# --------------------------------------------------------- ring machinery

def is_unit(x):
    return gcd(x % N, N) == 1


def inv_unit(x):
    return pow(x % N, -1, N)


def rand_unit(rng):
    while True:
        x = rng.randrange(1, N)
        if is_unit(x):
            return x


def symbol_units(rng):
    """A fixed random unit per alphabet symbol (the char embedding)."""
    return {ch: rand_unit(rng) for ch in ALPHABET}


def pos_units(rng):
    """A fixed random unit per (symbol, position) -- the position-tagged embedding."""
    return {(ch, i): rand_unit(rng)
            for ch in ALPHABET for i in range(MAXLEN)}


def phi_hom(s, u):
    """The monoid homomorphism: string -> product of symbol units (empty -> 1)."""
    v = 1
    for ch in s:
        v = (v * u[ch]) % N
    return v


def phi_pos(s, u):
    """Position-tagged: string -> product of (symbol, position) units."""
    v = 1
    for i, ch in enumerate(s):
        v = (v * u[(ch, i)]) % N
    return v


# --------------------------------------------------- the analogy protocol

def complete(forms, phi, n_lex, n_cell, anchor=0, cite=0):
    """Fill every held-out (lexeme != anchor, cell != cite) by the transform
    T_c = phi(anchor_c) * inv(phi(anchor_cite)) applied to phi(lex_cite). forms is
    {(lex, cell): surface_string}. Returns (correct, total)."""
    E = {k: phi(v) for k, v in forms.items()}
    a_cite_inv = inv_unit(E[(anchor, cite)])
    correct = total = 0
    for c in range(n_cell):
        if c == cite:
            continue
        T = (E[(anchor, c)] * a_cite_inv) % N
        for i in range(n_lex):
            if i == anchor:
                continue
            pred = (T * E[(i, cite)]) % N
            correct += (pred == E[(i, c)])
            total += 1
    return correct, total


# ------------------------------------------------------- paradigm builders

def distinct_stems(rng, n, length, alphabet):
    """n distinct strings of the given length with distinct symbol MULTISETS
    (non-anagram) -- so phi_hom separates them."""
    out, seen = [], set()
    while len(out) < n:
        s = "".join(rng.choice(alphabet) for _ in range(length))
        key = tuple(sorted(s))
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
    return out


def concatenative(rng, n_lex, length=4):
    """form(lex, cell) = stem . suffix_cell; cite suffix is empty. Distinct,
    non-anagram stems over consonants; suffixes over a disjoint symbol set."""
    stems = distinct_stems(rng, n_lex, length, "bcdfghjklmnpqrstvwxz")
    suffixes = ["", "ed", "es", "ing", "en", "er"]              # cell 0 = citation
    forms = {(i, c): stems[i] + suffixes[c]
             for i in range(n_lex) for c in range(len(suffixes))}
    return forms, len(suffixes), stems, suffixes


def concatenative_fixed_vs_var(rng, n_lex):
    """Two concatenative paradigms for the position-tag trade: one with all stems
    the SAME length, one with VARYING lengths. Same suffix set."""
    cons = "bcdfghjklmnpqrstvwxz"
    fixed_stems = distinct_stems(rng, n_lex, 4, cons)
    # The anchor (index 0, the transform source) is given a UNIQUE length (2;
    # every other stem 3..6) so the varying-length collapse is EXACT and
    # seed-robust: a length-2 anchor's affix occupies positions no length>=3 stem
    # can, so the extracted transform transfers to ZERO other lexemes. Without a
    # unique anchor length the transfer accuracy is the (seed-dependent) fraction
    # of stems sharing the anchor's length -- the point (order restored, transform
    # broken) is the same, but the number would not be a robust 0.
    var_stems = ["".join(rng.choice(cons) for _ in range(2))]
    seen = set()
    while len(var_stems) < n_lex:
        L = rng.choice([3, 4, 5, 6])
        s = "".join(rng.choice(cons) for _ in range(L))
        key = tuple(sorted(s))
        if key in seen:
            continue
        seen.add(key)
        var_stems.append(s)
    suffixes = ["", "ed", "es", "ing"]
    mk = lambda st: {(i, c): st[i] + suffixes[c]
                     for i in range(n_lex) for c in range(len(suffixes))}
    return mk(fixed_stems), mk(var_stems), len(suffixes)


def suppletive_fusional(rng, n_lex, n_cell=4):
    """Each lexeme's non-citation cells are IDIOSYNCRATIC strings sharing no
    shared multiplicative transform (the suppletion extreme: go->went). Citation
    is a distinct stem; each other cell is an independent distinct string."""
    used = set()
    def fresh(length):
        while True:
            s = "".join(rng.choice(ALPHABET) for _ in range(length))
            if s not in used:
                used.add(s)
                return s
    forms = {}
    for i in range(n_lex):
        forms[(i, 0)] = fresh(4)
        for c in range(1, n_cell):
            forms[(i, c)] = fresh(rng.choice([4, 5, 6]))
    return forms, n_cell


def relation_respecting(rng, n_lex, n_cell=4):
    """The RESCUE embedding: forms built AS L_lex * T_cell (units), so the
    transform IS shared -- the relation is supplied by construction (a codebook /
    the deleted metric). Returns a {(lex, cell): ring_element} map, not strings."""
    L = [rand_unit(rng) for _ in range(n_lex)]
    T = [rand_unit(rng) for _ in range(n_cell)]
    return {(i, c): (L[i] * T[c]) % N
            for i in range(n_lex) for c in range(n_cell)}, n_cell


# --------------------------------------------------------- S0: controls

def s0_controls():
    print("S0: positive controls")
    rng = random.Random(20250609)
    u = symbol_units(rng)
    for _ in range(2000):
        s = "".join(rng.choice(ALPHABET) for _ in range(rng.randrange(0, 8)))
        t = "".join(rng.choice(ALPHABET) for _ in range(rng.randrange(0, 8)))
        check(phi_hom(s + t, u) == (phi_hom(s, u) * phi_hom(t, u)) % N,
              "homomorphism law failed")
    print("  homomorphism law phi(s.t) == phi(s)*phi(t) (2000 samples)")

    T = (phi_hom("wked", u) * inv_unit(phi_hom("wk", u))) % N
    pred = (T * phi_hom("jm", u)) % N
    check(pred == phi_hom("jmed", u), "hand pair jmed failed")
    print(f"  hand pair: T_ed applied to 'jm' == phi('jmed')  (T = phi(wked)/phi(wk))")

    vocab = ["spot", "stop", "tops", "pots", "opts", "post",
             "cat", "act", "listen", "silent", "alpha"]
    vals = [phi_hom(w, u) for w in vocab]
    classes = len(set(tuple(sorted(w)) for w in vocab))
    check(len(set(vals)) == classes,
          f"anagram collision count {len(set(vals))} != classes {classes}")
    print(f"  anagram collisions: {len(vocab)} forms -> {len(set(vals))} distinct"
          f" phi values == {classes} multiset classes")

    for _ in range(500):
        s = "".join(rng.choice(ALPHABET) for _ in range(rng.randrange(1, 8)))
        v = phi_hom(s, u)
        check((v * inv_unit(v)) % N == 1, "unit inverse failed")
    print("  phi(s) a unit: phi(s)*inv(phi(s)) == 1 (500 samples)")


# --------------------------------------- S1: the concatenative SURVIVE

def s1_concatenative(n_lex=12):
    print("\nS1: concatenative -- phi_hom generalizes from raw strings (PR1)")
    rng = random.Random(41)
    u = symbol_units(rng)
    forms, n_cell, stems, suffixes = concatenative(rng, n_lex)
    cv, tv = complete(forms, lambda s: phi_hom(s, u), n_lex, n_cell)
    # control: a random unit per DISTINCT surface string (non-homomorphic)
    strset = sorted(set(forms.values()))
    cmap = {s: rand_unit(rng) for s in strset}
    cc, tc = complete(forms, lambda s: cmap[s], n_lex, n_cell)
    print(f"  {n_lex} lexemes x {n_cell} cells; stems {stems[:3]}..., suffixes {suffixes}")
    print(f"  phi_hom (homomorphism) held-out exact: {cv}/{tv} = {cv/tv:.3f}")
    print(f"  non-homomorphic control held-out exact: {cc}/{tc} = {cc/tc:.3f}")
    check(cv == tv, "phi_hom did not complete every held-out concatenative cell")
    check(cc == 0, "control completed a held-out cell (should be structureless)")
    print("  => the char-product homomorphism makes concatenative morphology")
    print("     exactly multiplicative -- native, codebook-free, from raw strings")


# ------------------------------------------------ S2: the order cost

def s2_order_cost():
    print("\nS2: the order cost -- phi_hom is order-blind (PR2)")
    rng = random.Random(7)
    u = symbol_units(rng)
    # a vocabulary loaded with anagrams
    vocab = ["spot", "stop", "tops", "pots", "opts", "post",
             "team", "meat", "mate", "tame", "listen", "silent", "enlist"]
    vals = [phi_hom(w, u) for w in vocab]
    n_classes = len(set(tuple(sorted(w)) for w in vocab))
    print(f"  {len(vocab)} surface forms -> {len(set(vals))} distinct phi values"
          f"  (= {n_classes} multiset classes): {len(vocab) - len(set(vals))} collisions")
    check(len(set(vals)) == n_classes and n_classes < len(vocab),
          "anagram collisions not as derived")
    # prefix vs suffix homophony
    stems = ["lock", "read", "wind"]
    homophones = sum(phi_hom("re" + s, u) == phi_hom(s + "re", u) for s in stems)
    print(f"  prefix vs suffix: phi('re'+stem) == phi(stem+'re') for {homophones}"
          f"/{len(stems)} stems -- prefixation indistinguishable from suffixation")
    check(homophones == len(stems), "prefix/suffix not homophonous under phi_hom")
    print("  => order-blindness is phi NON-INJECTIVITY (info loss / undecodability),")
    print("     not an analogy-accuracy drop -- the native blind spot at the embedding")


# --------------------------------------- S3: the position-tag trade

def s3_position_trade(n_lex=12):
    print("\nS3: position tags restore order but break the shared transform (PR3)")
    rng = random.Random(3)
    up = pos_units(rng)
    fixed, var, n_cell = concatenative_fixed_vs_var(rng, n_lex)
    cf, tf = complete(fixed, lambda s: phi_pos(s, up), n_lex, n_cell)
    cvr, tvr = complete(var, lambda s: phi_pos(s, up), n_lex, n_cell)
    # anagram separation under phi_pos
    anas = ["spot", "stop", "tops", "pots"]
    sep = len(set(phi_pos(w, up) for w in anas))
    print(f"  phi_pos anagram separation: {len(anas)} forms -> {sep} distinct phi"
          f" values (order restored)")
    print(f"  fixed-length stems   held-out exact: {cf}/{tf} = {cf/tf:.3f}")
    print(f"  varying-length stems held-out exact: {cvr}/{tvr} = {cvr/tvr:.3f}")
    check(sep == len(anas), "phi_pos did not separate anagrams")
    check(cf == tf, "phi_pos fixed-length did not generalize")
    check(cvr / tvr < 0.1, "phi_pos varying-length unexpectedly generalized")
    print("  => order and the shared transform EXCHANGE: phi_pos separates anagrams")
    print("     but the affix's length-dependent position breaks the lexeme-free T")


# ------------------------------------------ S4: the fusional KILL

def s4_fusional(n_lex=12):
    print("\nS4: fusional -- phi_hom fails; rescue re-imports the metric (PR4)")
    rng = random.Random(9)
    u = symbol_units(rng)
    fus, n_cell = suppletive_fusional(rng, n_lex)
    ch, th = complete(fus, lambda s: phi_hom(s, u), n_lex, n_cell)
    print(f"  suppletive fusional (idiosyncratic cell forms, no shared substring):")
    print(f"  phi_hom held-out exact: {ch}/{th} = {ch/th:.3f}  (transform not shared)")
    check(ch / th < 0.1, "phi_hom unexpectedly generalized fusional forms")

    # rescue A: an embedding that RESPECTS the relation (forms = L_lex * T_cell)
    resc, _ = relation_respecting(random.Random(9), n_lex, n_cell)
    cr, tr = complete(resc, lambda x: x, n_lex, n_cell)   # forms already ring elts
    print(f"  rescue (relation-respecting embedding L_lex*T_cell): {cr}/{tr} ="
          f" {cr/tr:.3f}")
    check(cr == tr, "relation-respecting rescue did not restore generalization")

    # rescue B: a codebook trained on SEEN lexemes; held-out lexeme has no code
    seen = set(range(n_lex // 2))
    codebook = {(i, c): resc[(i, c)] for (i, c) in resc if i in seen}
    seen_ok = held_ok = seen_tot = held_tot = 0
    for c in range(1, n_cell):
        # transform from an anchor within the seen set
        T = (codebook[(0, c)] * inv_unit(codebook[(0, 0)])) % N
        for i in range(n_lex):
            if i == 0:
                continue
            truth = resc[(i, c)]
            if i in seen:
                pred = (T * codebook[(i, 0)]) % N
                seen_ok += (pred == truth); seen_tot += 1
            else:
                # held-out lexeme: ABSENT from the codebook (a lookup table has no
                # entry for an unseen key), so nothing places it; the only
                # surface-native fallback is phi_hom, already 0/33 above.
                held_tot += 1
    print(f"  codebook on SEEN lexemes: {seen_ok}/{seen_tot} = {seen_ok/max(seen_tot,1):.3f};"
          f" HELD-OUT absent from table: {held_ok}/{held_tot} (no learned code, phi_hom 0/33)")
    check(seen_ok == seen_tot and held_ok == 0,
          "codebook did not show the seen/held-out split")
    print("  => fusional generalization returns only with the relation supplied by")
    print("     construction (metric) or a codebook that does not extend to held-out")


if __name__ == "__main__":
    s0_controls()
    s1_concatenative()
    s2_order_cost()
    s3_position_trade()
    s4_fusional()
    print(f"\nALL SECTIONS PASS -- {CHECKS} checks, exit 0")
