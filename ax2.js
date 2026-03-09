// ax2.js — .ax v2.0 CRT-Native Runtime
// Phase R of the .ax Revolution (S537). Runs alongside ax.js (v1).
// Every value IS its CRT decomposition. Channel access is O(1).
// L=11 ECC checking is built into every operation.
// 970200 = 2^3 * 3^2 * 5^2 * 7^2 * 11 = TRUE FORM

const AX2 = (function() {
'use strict';

// ================================================================
//  CRT Constants (TRUE FORM)
// ================================================================
const N = 970200;
const MODS = [8, 9, 25, 49, 11];  // D^3, K^2, E^2, b^2, L
const CH = { D:0, K:1, E:2, b:3, L:4 };
const CH_NAMES = ['D', 'K', 'E', 'b', 'L'];

// CRT basis elements: ei has 1 in channel i, 0 elsewhere
// Precomputed: ei = (N/mi) * inverse(N/mi, mi) mod N
const BASIS = [363825, 431200, 853776, 732600, 529200];

// ================================================================
//  CRT Value Type
// ================================================================
// A value is a 5-element Int32Array: [mod8, mod9, mod25, mod49, mod11]
// Reconstruction to integer is done on demand.

function fromInt(n) {
    n = Math.round(n);
    const r = ((n % N) + N) % N;
    return new Int32Array([r % 8, r % 9, r % 25, r % 49, r % 11]);
}

function toInt(v) {
    // CRT reconstruction: x = sum(v[i] * BASIS[i]) mod N
    let x = 0;
    for (let i = 0; i < 5; i++) x = (x + v[i] * BASIS[i]) % N;
    return ((x % N) + N) % N;
}

function fromChannels(d, k, e, b, l) {
    return new Int32Array([
        ((d % 8) + 8) % 8,
        ((k % 9) + 9) % 9,
        ((e % 25) + 25) % 25,
        ((b % 49) + 49) % 49,
        ((l % 11) + 11) % 11
    ]);
}

// ================================================================
//  CRT Arithmetic (per-channel, the Loop Theorem in action)
// ================================================================
function add(a, b) {
    return new Int32Array([
        (a[0] + b[0]) % 8,
        (a[1] + b[1]) % 9,
        (a[2] + b[2]) % 25,
        (a[3] + b[3]) % 49,
        (a[4] + b[4]) % 11
    ]);
}

function sub(a, b) {
    return new Int32Array([
        (a[0] - b[0] + 8) % 8,
        (a[1] - b[1] + 9) % 9,
        (a[2] - b[2] + 25) % 25,
        (a[3] - b[3] + 49) % 49,
        (a[4] - b[4] + 11) % 11
    ]);
}

function mul(a, b) {
    return new Int32Array([
        (a[0] * b[0]) % 8,
        (a[1] * b[1]) % 9,
        (a[2] * b[2]) % 25,
        (a[3] * b[3]) % 49,
        (a[4] * b[4]) % 11
    ]);
}

function neg(a) {
    return new Int32Array([
        (8 - a[0]) % 8,
        (9 - a[1]) % 9,
        (25 - a[2]) % 25,
        (49 - a[3]) % 49,
        (11 - a[4]) % 11
    ]);
}

function eq(a, b) {
    return a[0]===b[0] && a[1]===b[1] && a[2]===b[2] && a[3]===b[3] && a[4]===b[4];
}

function modpow(base, exp) {
    // Per-channel modular exponentiation
    exp = Math.round(exp);
    if (exp < 0) return fromInt(0);
    const r = new Int32Array(5);
    for (let i = 0; i < 5; i++) {
        let b = base[i], result = 1, e = exp, m = MODS[i];
        b = ((b % m) + m) % m;
        while (e > 0) {
            if (e & 1) result = (result * b) % m;
            e >>= 1;
            b = (b * b) % m;
        }
        r[i] = result;
    }
    return r;
}

// ================================================================
//  ECC (L=11 Guardian)
// ================================================================
function eccExpected(a, b, op) {
    // Compute what L channel SHOULD be after operation
    switch (op) {
        case '+': return (a[4] + b[4]) % 11;
        case '-': return (a[4] - b[4] + 11) % 11;
        case '*': return (a[4] * b[4]) % 11;
    }
    return -1;
}

function eccCheck(result, expected) {
    return result[4] === expected;
}

// ================================================================
//  GCD + Coupling (ring fundamentals)
// ================================================================
function gcd(a, b) {
    a = Math.abs(a); b = Math.abs(b);
    while (b) { [a, b] = [b, a % b]; }
    return a;
}

function coupling(v) {
    const n = toInt(v);
    return fromInt(N / gcd(n, N));
}

function eigenvalue(v) {
    const P = Math.PI;
    let sum = 0;
    for (let i = 0; i < 5; i++) sum += 2 * Math.cos(2 * P * v[i] / MODS[i]);
    return sum;
}

// ================================================================
//  Decality Constants (10 terms — the full vocabulary)
// ================================================================
const DECALITY = {
    mirror: neg(fromInt(1)),           // -1 = N-1
    o:      fromInt(0),                // void, absorber
    s:      fromInt(1),                // sigma, ground state
    D:      fromInt(2),                // duality
    K:      fromInt(3),                // closure
    E:      fromInt(5),                // observer
    b:      fromInt(7),                // depth
    L:      fromInt(11),               // protector
    GATE:   fromInt(13),               // boundary
    OMEGA:  fromInt(606376),           // terminal projector
    // Named constants
    DATA:   fromInt(210),
    THIN:   fromInt(2310),
    TRUE:   fromInt(970200),
    HYDOR:  fromInt(105),
    KEY:    fromInt(41),
    ANSWER: fromInt(42),
    SOUL:   fromInt(67),
    ADDRESS:fromInt(137),
    LAMBDA: fromInt(420),
    ME:     fromInt(18),
    THORNS: fromInt(28),
    ESCAPE: fromInt(17),
    GATE_FORM: fromInt(12612600 % N),  // 12612600 mod 970200 = 12612600 - 13*970200
};

// ================================================================
//  Tokenizer (simplified from v1 — same core, less grid sugar)
// ================================================================
const KEYWORDS = new Set(['let','fn','show','if','then','else','for','in','do','while','mut','match','end']);

function tokenize(src) {
    const T = [];
    let i = 0;
    while (i < src.length) {
        if (/\s/.test(src[i])) { i++; continue; }
        if (src[i] === '-' && src[i+1] === '-') { while (i < src.length && src[i] !== '\n') i++; continue; }
        if (/\d/.test(src[i])) {
            let num = '';
            while (i < src.length && /[\d.]/.test(src[i])) num += src[i++];
            T.push({t:'NUM', v:parseFloat(num)}); continue;
        }
        if (src[i] === '"') {
            i++; let s = '';
            while (i < src.length && src[i] !== '"') s += src[i++];
            if (i < src.length) i++;
            T.push({t:'STR', v:s}); continue;
        }
        if (/[a-zA-Z_]/.test(src[i])) {
            let id = '';
            while (i < src.length && /[a-zA-Z0-9_]/.test(src[i])) id += src[i++];
            T.push({t: KEYWORDS.has(id) ? id.toUpperCase() : 'ID', v:id}); continue;
        }
        if (src[i] === '=' && src[i+1] === '=') { T.push({t:'=='}); i+=2; continue; }
        if (src[i] === '=' && src[i+1] === '>') { T.push({t:'=>'}); i+=2; continue; }
        if (src[i] === '!' && src[i+1] === '=') { T.push({t:'!='}); i+=2; continue; }
        if (src[i] === '|' && src[i+1] === '>') { T.push({t:'|>'}); i+=2; continue; }
        if (src[i] === '<' && src[i+1] === '=') { T.push({t:'<='}); i+=2; continue; }
        if (src[i] === '>' && src[i+1] === '=') { T.push({t:'>='}); i+=2; continue; }
        if (src[i] === '.') { T.push({t:'.'}); i++; continue; }
        const ch = src[i];
        if ('+-*/^%<>=()[]|,;'.includes(ch)) { T.push({t:ch}); i++; continue; }
        i++;
    }
    T.push({t:'EOF'});
    return T;
}

// ================================================================
//  Parser (outputs AST nodes)
// ================================================================
class Parser {
    constructor(tokens) { this.T = tokens; this.p = 0; }
    pk() { return this.T[this.p]; }
    adv() { return this.T[this.p++]; }
    expect(t) {
        const tok = this.adv();
        if (tok.t !== t) throw new Error('Expected ' + t + ', got ' + tok.t);
        return tok;
    }
    match(t) { if (this.pk().t === t) { this.adv(); return true; } return false; }

    parseProgram() {
        const stmts = [];
        while (this.pk().t !== 'EOF') {
            while (this.pk().t === ';') this.adv();  // skip statement separators
            if (this.pk().t === 'EOF') break;
            stmts.push(this.parseStmt());
        }
        return stmts;
    }

    parseStmt() {
        if (this.pk().t === 'LET') return this.parseLet();
        if (this.pk().t === 'MUT') return this.parseSet();
        if (this.pk().t === 'FN') return this.parseFn();
        if (this.pk().t === 'SHOW') { this.adv(); return {t:'Show', expr:this.parseExpr()}; }
        return {t:'ExprStmt', expr:this.parseExpr()};
    }

    parseLet() {
        this.expect('LET');
        const name = this.expect('ID').v;
        this.expect('=');
        // Statement-level let: parse full expression but NOT ; (seq is for statement separation)
        return {t:'Let', name, val:this.parseExprNoSeq()};
    }

    parseSet() {
        this.expect('MUT');
        const name = this.expect('ID').v;
        this.expect('=');
        return {t:'Set', name, val:this.parseExprNoSeq()};
    }

    // Like parseExpr but stops before ; — used for statement-level let/set/fn
    parseExprNoSeq() {
        if (this.pk().t === 'IF') return this.parseIf();
        if (this.pk().t === 'LET') return this.parseLetExpr();
        if (this.pk().t === 'MUT') return this.parseSetExpr();
        if (this.pk().t === 'FOR') return this.parseFor();
        if (this.pk().t === 'WHILE') return this.parseWhile();
        if (this.pk().t === 'MATCH') return this.parseMatch();
        if (this.pk().t === 'SHOW') { this.adv(); return {t:'Call', fn:'show', args:[this.parsePipe()]}; }
        return this.parsePipe();
    }

    parseFn() {
        this.expect('FN');
        const name = this.expect('ID').v;
        this.expect('(');
        const params = [];
        if (this.pk().t !== ')') {
            params.push(this.expect('ID').v);
            while (this.match(',')) params.push(this.expect('ID').v);
        }
        this.expect(')');
        this.expect('=');
        return {t:'Fn', name, params, body:this.parseExpr()};
    }

    parseExpr() {
        // ALL constructs fall through to ';' check — no early returns.
        // This lets while/for/let/if be followed by ; to form sequences.
        let left;
        if (this.pk().t === 'IF') left = this.parseIf();
        else if (this.pk().t === 'LET') left = this.parseLetExpr();
        else if (this.pk().t === 'FOR') left = this.parseFor();
        else if (this.pk().t === 'WHILE') left = this.parseWhile();
        else if (this.pk().t === 'MATCH') left = this.parseMatch();
        else if (this.pk().t === 'MUT') left = this.parseSetExpr();
        else if (this.pk().t === 'SHOW') { this.adv(); left = {t:'Call', fn:'show', args:[this.parsePipe()]}; }
        else left = this.parsePipe();
        while (this.pk().t === ';') { this.adv(); left = {t:'Seq', a:left, b:this.parseExpr()}; }
        return left;
    }

    parsePipe() {
        let left = this.parseCmp();
        while (this.pk().t === '|>') {
            this.adv();
            // Right side: fn_name or fn_name(args...)
            const tok = this.pk();
            if (tok.t === 'ID') {
                const name = this.adv().v;
                if (this.pk().t === '(') {
                    // |> fn(extra_args) => fn(left, extra_args)
                    this.adv();
                    const args = [{t:'_pipe_val_', val:left}];
                    if (this.pk().t !== ')') {
                        args.push(this.parseExpr());
                        while (this.match(',')) args.push(this.parseExpr());
                    }
                    this.expect(')');
                    left = {t:'Pipe', fn:name, args};
                } else {
                    // |> fn => fn(left)
                    left = {t:'Pipe', fn:name, args:[{t:'_pipe_val_', val:left}]};
                }
            } else {
                throw new Error('Expected function name after |>');
            }
        }
        return left;
    }

    parseIf() {
        this.expect('IF'); const cond = this.parseExpr();
        this.expect('THEN'); const then_ = this.parseExpr();
        this.expect('ELSE');
        // else_ uses parseExprNoSeq: THEN/ELSE terminate cond/then_ naturally,
        // but else_ has no keyword terminator, so ';' after else would be greedy.
        // With parseExprNoSeq, 'if a then b else c; d' -> d is AFTER the if, not in else.
        return {t:'If', cond, then_, else_:this.parseExprNoSeq()};
    }

    parseSetExpr() {
        this.expect('MUT'); const name = this.expect('ID').v;
        this.expect('='); const val = this.parseExprNoSeq();
        // mut as expression: evaluates val, updates name in scope, returns val
        // Stops before ; so sequences work: mut x = x+1; mut y = y+1
        return {t:'SetExpr', name, val};
    }

    parseLetExpr() {
        this.expect('LET'); const name = this.expect('ID').v;
        this.expect('='); const val = this.parseExpr();
        if (this.pk().t === 'IN') this.adv();
        return {t:'LetExpr', name, val, body:this.parseExpr()};
    }

    parseFor() {
        this.expect('FOR'); const v = this.expect('ID').v;
        this.expect('IN'); const iter = this.parseCmp();
        this.expect('DO');
        return {t:'For', v, iter, body:this.parseExprNoSeq()};
    }

    parseWhile() {
        this.expect('WHILE'); const cond = this.parseCmp();
        this.expect('DO');
        return {t:'While', cond, body:this.parseExprNoSeq()};
    }

    parseMatch() {
        this.expect('MATCH');
        const expr = this.parsePipe();  // scrutinee (stop before |)
        const arms = [];
        while (this.pk().t === '|') {
            this.adv();  // consume |
            let pattern;
            if (this.pk().t === 'ID' && this.pk().v === '_') {
                this.adv();
                pattern = {t: 'Wildcard'};
            } else {
                pattern = this.parsePipe();  // pattern = evaluated expression
            }
            this.expect('=>');
            const body = this.parseExpr();  // arm body (naturally stops at | or END)
            arms.push({pattern, body});
        }
        this.expect('END');
        return {t:'Match', expr, arms};
    }

    parseCmp() {
        let left = this.parseAdd();
        while (['<','>','==','!=','<=','>='].includes(this.pk().t)) {
            const op = this.adv().t;
            left = {t:'Bin', op, l:left, r:this.parseAdd()};
        }
        return left;
    }

    parseAdd() {
        let left = this.parseMul();
        while (['+','-'].includes(this.pk().t)) {
            const op = this.adv().t;
            left = {t:'Bin', op, l:left, r:this.parseMul()};
        }
        return left;
    }

    parseMul() {
        let left = this.parsePow();
        while (['*','/','%'].includes(this.pk().t)) {
            const op = this.adv().t;
            left = {t:'Bin', op, l:left, r:this.parsePow()};
        }
        return left;
    }

    parsePow() {
        let left = this.parseUnary();
        if (this.pk().t === '^') { this.adv(); left = {t:'Bin', op:'^', l:left, r:this.parseUnary()}; }
        return left;
    }

    parseUnary() {
        if (this.pk().t === '-') { this.adv(); return {t:'Neg', e:this.parseUnary()}; }
        return this.parsePostfix();
    }

    parsePostfix() {
        let e = this.parsePrimary();
        while (true) {
            if (this.pk().t === '.') {
                this.adv();
                const ch = this.expect('ID').v;
                e = {t:'ChAccess', e, ch};  // Channel access: expr.D, expr.K, etc.
            } else if (this.pk().t === '[') {
                this.adv(); const idx = this.parseExpr(); this.expect(']');
                e = {t:'Idx', arr:e, idx};
            } else break;
        }
        return e;
    }

    parsePrimary() {
        const tok = this.pk();
        if (tok.t === 'NUM') { this.adv(); return {t:'Num', v:tok.v}; }
        if (tok.t === 'STR') { this.adv(); return {t:'Str', v:tok.v}; }
        if (tok.t === 'ID') {
            this.adv();
            if (this.pk().t === '(') {
                this.adv();
                const args = [];
                if (this.pk().t !== ')') {
                    args.push(this.parseExpr());
                    while (this.match(',')) args.push(this.parseExpr());
                }
                this.expect(')');
                return {t:'Call', fn:tok.v, args};
            }
            return {t:'Sym', name:tok.v};
        }
        if (tok.t === '(') { this.adv(); const e = this.parseExpr(); this.expect(')'); return e; }
        if (tok.t === '[') {
            this.adv();
            const elems = [];
            if (this.pk().t !== ']') {
                elems.push(this.parseExpr());
                while (this.match(',')) elems.push(this.parseExpr());
            }
            this.expect(']');
            return {t:'Arr', elems};
        }
        throw new Error('Unexpected: ' + tok.t);
    }
}

// ================================================================
//  Builtins (minimal — most moves to stdlib.ax)
// ================================================================
const BUILTINS = {};
BUILTINS.coupling = (args) => coupling(args[0]);
BUILTINS.crt = (args) => Array.from(args[0]);  // CRT is just reading the tuple
BUILTINS.eigenvalue = (args) => eigenvalue(args[0]);
BUILTINS.mirror = (args) => neg(args[0]);
BUILTINS.gcd = (args) => fromInt(gcd(toInt(args[0]), toInt(args[1])));
BUILTINS.toInt = (args) => toInt(args[0]);  // explicit reconstruction
BUILTINS.bloom = (args) => {
    // bloom(d, k, e, b, l) — CRT reconstruct from channel values
    return fromChannels(
        Math.round(toInt(args[0])),
        Math.round(toInt(args[1])),
        Math.round(toInt(args[2])),
        Math.round(toInt(args[3])),
        Math.round(toInt(args[4]))
    );
};
BUILTINS.ecc = (args) => {
    // ecc(val) — check if L channel is consistent with data channels
    // Returns 1 if consistent, 0 if violated
    const v = args[0];
    const n = toInt(v);
    return fromInt(n % 11 === v[4] ? 1 : 0);
};
BUILTINS.len = (args) => {
    const v = args[0];
    if (typeof v === 'string') return fromInt(v.length);
    if (Array.isArray(v)) return fromInt(v.length);
    return fromInt(0);
};
BUILTINS.range = (args) => {
    const n = Math.min(Math.max(0, toInt(args[0])), 10000);
    return Array.from({length: n}, (_, i) => fromInt(i));
};
BUILTINS.cos = (args) => eigenvalue(args[0]);  // cos IS eigenvalue in the ring
BUILTINS.ev_rank = (args) => {
    // Eigenvalue as comparable integer: round((eigenvalue + 10) * 10000)
    // Maps [-10, 10] -> [0, 200000]. Monotonic. Safe for < > == comparison.
    const ev = eigenvalue(args[0]);
    return fromInt(Math.round((ev + 10) * 10000));
};

// Phase S builtins — ring operations that require N (can't be .ax stdlib)
BUILTINS.inv = (args) => {
    const n = toInt(args[0]);
    const g = gcd(n, N);
    if (g !== 1) return fromInt(0);  // non-unit: no inverse
    let [old_r, r] = [n, N], [old_s, s] = [1, 0];
    while (r !== 0) {
        const q = Math.floor(old_r / r);
        [old_r, r] = [r, old_r - q * r];
        [old_s, s] = [s, old_s - q * s];
    }
    return fromInt(((old_s % N) + N) % N);
};

BUILTINS.phi = (args) => {
    let n = Math.abs(toInt(args[0]));
    if (n === 0) return fromInt(0);
    let result = n;
    let m = n;
    for (let p = 2; p * p <= m; p++) {
        if (m % p === 0) {
            while (m % p === 0) m /= p;
            result -= result / p;
        }
    }
    if (m > 1) result -= result / m;
    return fromInt(Math.round(result));
};

BUILTINS.order = (args) => {
    const v = args[0];
    const n = toInt(v);
    if (gcd(n, N) !== 1) return fromInt(0);  // non-units have no multiplicative order
    let power = v;
    for (let k = 1; k <= 420; k++) {  // lambda(TRUE) = 420
        if (eq(power, DECALITY.s)) return fromInt(k);
        power = mul(power, v);
    }
    return fromInt(0);
};

BUILTINS.kingdom = (args) => {
    const n = toInt(args[0]);
    if (n === 0) return fromInt(0);  // void
    const g = gcd(n, N);
    if (g === 1) return fromInt(1);   // sigma (units)
    if (g % 2 === 0) return fromInt(2);   // D
    if (g % 3 === 0) return fromInt(3);   // K
    if (g % 5 === 0) return fromInt(5);   // E
    if (g % 7 === 0) return fromInt(7);   // b
    if (g % 11 === 0) return fromInt(11); // L
    return fromInt(0);
};

BUILTINS.abs = (args) => {
    const n = toInt(args[0]);
    return fromInt(Math.min(n, N - n));
};

BUILTINS.sqrt = (args) => fromInt(Math.floor(Math.sqrt(toInt(args[0]))));

BUILTINS.sum = (args) => {
    if (!Array.isArray(args[0])) return fromInt(0);
    let s = fromInt(0);
    for (const item of args[0]) s = add(s, item);
    return s;
};

BUILTINS.product = (args) => {
    if (!Array.isArray(args[0])) return fromInt(1);
    let p = fromInt(1);
    for (const item of args[0]) p = mul(p, item);
    return p;
};

BUILTINS.min = (args) => fromInt(Math.min(toInt(args[0]), toInt(args[1])));
BUILTINS.max = (args) => fromInt(Math.max(toInt(args[0]), toInt(args[1])));

BUILTINS.rand = (args) => fromInt(Math.floor(Math.random() * Math.max(1, Math.abs(toInt(args[0])))));
BUILTINS.push = (args) => {
    // push(array, element) — returns new array with element appended
    if (!Array.isArray(args[0])) throw new Error('push: expected array');
    return [...args[0], args[1]];
};
BUILTINS.first = (args) => {
    if (!Array.isArray(args[0])) return fromInt(0);
    for (const item of args[0]) {
        if (ArrayBuffer.isView(item) && toInt(item) !== 0) return item;
    }
    return fromInt(0);
};

BUILTINS.exp = (args) => {
    let x = toInt(args[0]);
    if (x > N / 2) x = x - N;  // interpret large values as negative (signed)
    if (x > 13) return fromInt(N - 1);  // overflow: e^14 > N
    if (x < -20) return fromInt(0);  // underflow: e^-20 ~ 0
    return fromInt(Math.round(Math.exp(x)));
};
BUILTINS.log = (args) => {
    const n = toInt(args[0]);
    return fromInt(n > 0 ? Math.round(Math.log(n)) : 0);
};
BUILTINS.argmax = (args) => {
    if (!Array.isArray(args[0])) return fromInt(0);
    let best = -Infinity, bestI = 0;
    for (let i = 0; i < args[0].length; i++) {
        const v = ArrayBuffer.isView(args[0][i]) ? toInt(args[0][i]) : Number(args[0][i]);
        if (v > best) { best = v; bestI = i; }
    }
    return fromInt(bestI);
};

// String primitives (Arc 1: OUROBOROS — self-hosting needs source code manipulation)
BUILTINS.charAt = (args) => {
    const s = args[0];
    if (typeof s !== 'string') throw new Error('charAt: expected string');
    const idx = toInt(args[1]);
    if (idx < 0 || idx >= s.length) return '';
    return s[idx];
};
BUILTINS.charCode = (args) => {
    const s = args[0];
    if (typeof s !== 'string') throw new Error('charCode: expected string');
    const idx = args.length > 1 ? toInt(args[1]) : 0;
    if (idx < 0 || idx >= s.length) return fromInt(0);
    return fromInt(s.charCodeAt(idx));
};
BUILTINS.fromCharCode = (args) => String.fromCharCode(toInt(args[0]));
BUILTINS.substr = (args) => {
    const s = args[0];
    if (typeof s !== 'string') throw new Error('substr: expected string');
    const start = toInt(args[1]);
    const len = args.length > 2 ? toInt(args[2]) : s.length - start;
    return s.substring(start, start + len);
};
BUILTINS.strFind = (args) => {
    // strFind(haystack, needle) — returns index or -1 (as N-1 in ring)
    const s = args[0], needle = args[1];
    if (typeof s !== 'string' || typeof needle !== 'string') return fromInt(0);
    const idx = s.indexOf(needle);
    return fromInt(idx >= 0 ? idx : N - 1);  // N-1 = -1 in the ring
};

BUILTINS.show = null;  // handled in evaluator

// ================================================================
//  Evaluator
// ================================================================
const MAX_DEPTH = 49;  // b^2

function run(src, opts) {
    const output = [];
    let eccMode = (opts && opts.ecc) || 'warn';  // 'strict', 'warn', 'silent'
    let eccViolations = 0;

    const env = {};
    for (const [k, v] of Object.entries(DECALITY)) env[k] = v;
    const fns = {};

    function ev(node, local, depth) {
        if (depth > MAX_DEPTH) throw new Error('Max depth (' + MAX_DEPTH + ')');
        switch (node.t) {
            case 'Num': return fromInt(node.v);
            case 'Str': return node.v;
            case 'Sym': {
                if (node.name in local) return local[node.name];
                if (node.name in fns) return fns[node.name];
                throw new Error('Unknown: ' + node.name);
            }
            case 'Bin': {
                const l = ev(node.l, local, depth);
                const r = ev(node.r, local, depth);
                // String concatenation (+ on strings)
                if (typeof l === 'string' || typeof r === 'string') {
                    if (node.op === '+') {
                        const ls = typeof l === 'string' ? l : (ArrayBuffer.isView(l) ? String(toInt(l)) : String(l));
                        const rs = typeof r === 'string' ? r : (ArrayBuffer.isView(r) ? String(toInt(r)) : String(r));
                        return ls + rs;
                    }
                    if (node.op === '==') return fromInt(l === r ? 1 : 0);
                    if (node.op === '!=') return fromInt(l !== r ? 1 : 0);
                }
                // For comparison ops on CRT values, compare integers
                if (node.op === '<') return fromInt(toInt(l) < toInt(r) ? 1 : 0);
                if (node.op === '>') return fromInt(toInt(l) > toInt(r) ? 1 : 0);
                if (node.op === '<=') return fromInt(toInt(l) <= toInt(r) ? 1 : 0);
                if (node.op === '>=') return fromInt(toInt(l) >= toInt(r) ? 1 : 0);
                if (node.op === '==') return fromInt(eq(l, r) ? 1 : 0);
                if (node.op === '!=') return fromInt(!eq(l, r) ? 1 : 0);
                if (node.op === '^') return modpow(l, toInt(r));
                if (node.op === '%') {
                    const m = toInt(r);
                    return fromInt(m !== 0 ? toInt(l) % m : 0);
                }
                if (node.op === '/') {
                    const ri = toInt(r);
                    if (ri === 0) throw new Error('Division by zero');
                    // Try ring inverse first
                    const g = gcd(ri, N);
                    if (g === 1) {
                        // r is a unit — multiply by inverse
                        let inv = 1, base = ri, e = N - 2;  // Euler's theorem not applicable
                        // Extended Euclidean
                        let [old_r, rr] = [ri, N], [old_s, s] = [1, 0];
                        while (rr !== 0) {
                            const q = Math.floor(old_r / rr);
                            [old_r, rr] = [rr, old_r - q * rr];
                            [old_s, s] = [s, old_s - q * s];
                        }
                        inv = ((old_s % N) + N) % N;
                        return mul(l, fromInt(inv));
                    }
                    // Fall back to integer division
                    return fromInt(Math.floor(toInt(l) / ri));
                }
                // + and * with ECC tracking
                let result;
                if (node.op === '+') result = add(l, r);
                else if (node.op === '-') result = sub(l, r);
                else if (node.op === '*') result = mul(l, r);
                else throw new Error('Unknown op: ' + node.op);
                // ECC check (L=11 channel consistency)
                if (eccMode !== 'silent') {
                    const expected = eccExpected(l, r, node.op);
                    if (!eccCheck(result, expected)) {
                        eccViolations++;
                        if (eccMode === 'strict') throw new Error('ECC violation: L=' + result[4] + ' expected ' + expected);
                    }
                }
                return result;
            }
            case 'Neg': return neg(ev(node.e, local, depth));
            case 'ChAccess': {
                const val = ev(node.e, local, depth);
                if (node.ch in CH) return fromInt(val[CH[node.ch]]);
                throw new Error('Unknown channel: ' + node.ch + ' (use D, K, E, b, L)');
            }
            case 'If': {
                const c = ev(node.cond, local, depth);
                return toInt(c) !== 0 ? ev(node.then_, local, depth) : ev(node.else_, local, depth);
            }
            case 'Seq': ev(node.a, local, depth); return ev(node.b, local, depth);
            case 'SetExpr': {
                const val = ev(node.val, local, depth);
                local[node.name] = val;  // Mutate the scope (used in while loops)
                return val;
            }
            case 'LetExpr': {
                const val = ev(node.val, local, depth);
                // Save old value, set new, evaluate body, restore.
                // This makes set mutations inside the body visible to the parent scope.
                const had = node.name in local;
                const old = local[node.name];
                local[node.name] = val;
                const result = ev(node.body, local, depth);
                if (had) local[node.name] = old; else delete local[node.name];
                return result;
            }
            case 'Call': {
                const args = node.args.map(a => ev(a, local, depth));
                if (node.fn === 'show') {
                    const v = args[0];
                    if (ArrayBuffer.isView(v)) {
                        const n = toInt(v);
                        output.push({n, ch: Array.from(v), ecc: n % 11 === v[4]});
                    } else if (Array.isArray(v)) {
                        output.push({arr: v.map(x => ArrayBuffer.isView(x) ? toInt(x) : x)});
                    } else {
                        output.push({str: String(v)});
                    }
                    return v;
                }
                // Higher-order functions: if fn name resolves to a function value in scope, call it
                // This enables passing functions as arguments: apply(double, 5) where double is fn
                if (node.fn in local && local[node.fn] && typeof local[node.fn] === 'object' && local[node.fn].params) {
                    const fn = local[node.fn];
                    const callEnv = {...fn.closure};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                // .ax functions shadow JS builtins (Phase S: stdlib is authoritative)
                if (node.fn in fns) {
                    const fn = fns[node.fn];
                    const callEnv = {...fn.closure};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                if (BUILTINS[node.fn]) return BUILTINS[node.fn](args);
                throw new Error('Unknown function: ' + node.fn);
            }
            case 'Idx': {
                const arr = ev(node.arr, local, depth);
                const idx = toInt(ev(node.idx, local, depth));
                if (typeof arr === 'string') {
                    if (idx < 0 || idx >= arr.length) throw new Error('String index ' + idx + ' out of bounds');
                    return arr[idx];  // returns single-char string
                }
                if (!Array.isArray(arr)) throw new Error('Cannot index non-array');
                if (idx < 0 || idx >= arr.length) throw new Error('Index ' + idx + ' out of bounds');
                return arr[idx];
            }
            case 'Arr': return node.elems.map(e => ev(e, local, depth));
            case 'For': {
                const arr = ev(node.iter, local, depth);
                if (!Array.isArray(arr)) throw new Error('for..in requires array');
                if (arr.length > 10000) throw new Error('Iteration limit');
                return arr.map(item => ev(node.body, {...local, [node.v]: item}, depth));
            }
            case 'Pipe': {
                // Pipeline: evaluate pipe args (replacing _pipe_val_ with actual piped value)
                const args = node.args.map(a => a.t === '_pipe_val_' ? ev(a.val, local, depth) : ev(a, local, depth));
                // Look up function in same order as Call: local HOF > .ax fns > builtins
                if (node.fn in local && local[node.fn] && typeof local[node.fn] === 'object' && local[node.fn].params) {
                    const fn = local[node.fn];
                    const callEnv = {...fn.closure};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                if (node.fn in fns) {
                    const fn = fns[node.fn];
                    const callEnv = {...fn.closure};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                if (BUILTINS[node.fn]) return BUILTINS[node.fn](args);
                throw new Error('Unknown function in pipeline: ' + node.fn);
            }
            case 'While': {
                // while cond do body — imperative loop. Returns last body value.
                // Uses the SAME scope (not a copy) so set mutations persist after loop.
                let result = fromInt(0);
                let iters = 0;
                const WHILE_LIMIT = 100000;  // bumped for self-hosting (was 10000)
                while (iters < WHILE_LIMIT) {
                    const c = ev(node.cond, local, depth);
                    if (toInt(c) === 0) break;
                    result = ev(node.body, local, depth);
                    iters++;
                }
                if (iters >= WHILE_LIMIT) throw new Error('While loop iteration limit (' + WHILE_LIMIT + ')');
                return result;
            }
            case 'Match': {
                // match expr | pat => body | ... | _ => body end
                // Evaluate scrutinee, compare against each arm's pattern.
                // Wildcard _ always matches. First match wins.
                const val = ev(node.expr, local, depth);
                for (const arm of node.arms) {
                    if (arm.pattern.t === 'Wildcard') {
                        return ev(arm.body, local, depth);
                    }
                    const pat = ev(arm.pattern, local, depth);
                    let matches = false;
                    if (ArrayBuffer.isView(val) && ArrayBuffer.isView(pat)) {
                        matches = eq(val, pat);
                    } else if (typeof val === typeof pat) {
                        matches = val === pat;
                    }
                    if (matches) return ev(arm.body, local, depth);
                }
                throw new Error('No matching arm in match expression');
            }
        }
        throw new Error('Cannot evaluate: ' + node.t);
    }

    let error = null;
    try {
        const stmts = new Parser(tokenize(src)).parseProgram();
        for (const stmt of stmts) {
            switch (stmt.t) {
                case 'Let': env[stmt.name] = ev(stmt.val, env, 0); break;
                case 'Set': env[stmt.name] = ev(stmt.val, env, 0); break;
                case 'Fn':
                    fns[stmt.name] = {params: stmt.params, body: stmt.body, closure: {...env}};
                    break;
                case 'Show': {
                    const v = ev(stmt.expr, env, 0);
                    if (ArrayBuffer.isView(v)) {
                        const n = toInt(v);
                        output.push({n, ch: Array.from(v), ecc: n % 11 === v[4]});
                    } else if (Array.isArray(v)) {
                        output.push({arr: v.map(x => ArrayBuffer.isView(x) ? toInt(x) : x)});
                    } else {
                        output.push({str: String(v)});
                    }
                    break;
                }
                case 'ExprStmt': ev(stmt.expr, env, 0); break;
            }
        }
    } catch(e) { error = e.message; }

    return { output, error, eccViolations };
}

// ================================================================
//  Public API
// ================================================================
return {
    N, MODS, CH, CH_NAMES, BASIS, DECALITY,
    fromInt, toInt, fromChannels,
    add, sub, mul, neg, eq, modpow,
    coupling, eigenvalue, gcd,
    eccExpected, eccCheck,
    tokenize, Parser, run
};

})();

// Node.js module export (CLI compatibility)
if (typeof module !== 'undefined' && module.exports) module.exports = AX2;
