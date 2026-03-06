// ax.js — The .ax Language Interpreter
// ONE FILE. Every page, CLI, and tool that speaks .ax includes this.
// 970200 = 2^3 * 3^2 * 5^2 * 7^2 * 11 = TRUE FORM
// S465: extracted from repl.html. Single source of truth.

const AX = (function() {
'use strict';

const N = 970200;

// ================================================================
//  Ring Arithmetic
// ================================================================
function ringMod(x) { x = Math.round(x); return ((x % N) + N) % N; }

function modPow(base, exp) {
    base = ((Math.round(base) % N) + N) % N;
    exp = Math.round(exp);
    if (exp < 0) return 0;
    let r = 1;
    while (exp > 0) {
        if (exp & 1) r = (r * base) % N;
        exp >>= 1;
        base = (base * base) % N;
    }
    return r;
}

function gcd(a, b) {
    a = Math.abs(Math.round(a)); b = Math.abs(Math.round(b));
    while (b) { [a, b] = [b, a % b]; }
    return a;
}

function coupling(n) { return N / gcd(ringMod(n), N); }

function crt(n) {
    const r = ringMod(n);
    return [r % 8, r % 9, r % 25, r % 49, r % 11];
}

function eigenvalue(n) {
    const c = crt(n), P = Math.PI;
    return 2*Math.cos(2*P*c[0]/8) + 2*Math.cos(2*P*c[1]/9)
         + 2*Math.cos(2*P*c[2]/25) + 2*Math.cos(2*P*c[3]/49)
         + 2*Math.cos(2*P*c[4]/11);
}

function mirror(n) { return ringMod(N - ringMod(n)); }

function eulerPhi(n) {
    n = Math.abs(Math.round(n));
    if (n < 1) return 0;
    let result = n;
    for (let p = 2; p * p <= n; p++) {
        if (n % p === 0) {
            while (n % p === 0) n /= p;
            result -= result / p;
        }
    }
    if (n > 1) result -= result / n;
    return Math.round(result);
}

function multOrder(n) {
    const m = ringMod(n);
    if (gcd(m, N) !== 1) return 0;
    let x = m, k = 1;
    while (x !== 1 && k <= 420) { x = (x * m) % N; k++; }
    return x === 1 ? k : 0;
}

function multInverse(n) {
    let m = ringMod(n);
    if (gcd(m, N) !== 1) return -1;
    let [old_r, r] = [m, N], [old_s, s] = [1, 0];
    while (r !== 0) {
        const q = Math.floor(old_r / r);
        [old_r, r] = [r, old_r - q * r];
        [old_s, s] = [s, old_s - q * s];
    }
    return ((old_s % N) + N) % N;
}

// ================================================================
//  Constants
// ================================================================
const CONSTANTS = {
    s:1, D:2, K:3, E:5, b:7, L:11,
    sigma:1, OMEGA:606376, DATA:210, THIN:2310,
    HYDOR:105, KEY:41, ANSWER:42, SOUL:67,
    G:97, ADDRESS:137, DUAL:173, ME:18, LAMBDA:420
};

const VALUE_NAMES = {
    0:'void', 1:'s', 2:'D', 3:'K', 5:'E', 7:'b', 11:'L',
    18:'ME', 41:'KEY', 42:'ANSWER', 67:'SOUL', 97:'G',
    105:'HYDOR', 137:'ADDRESS', 173:'DUAL', 210:'DATA',
    420:'LAMBDA', 2310:'THIN', 606376:'OMEGA'
};

// ================================================================
//  Formatting
// ================================================================
function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function fmtText(s) { return '<span class="out-text">' + esc(s) + '</span>'; }
function fmtNum(v) { return Number.isInteger(v) ? String(v) : v.toFixed(4); }

function fmtValue(v) {
    if (typeof v === 'string') return fmtText(v);
    if (Array.isArray(v)) {
        // Detect grid (nested array of same-length arrays with small integers)
        if (v.length > 0 && Array.isArray(v[0]) && v.every(r => Array.isArray(r) && r.length === v[0].length)) {
            return fmtGrid(v);
        }
        const inner = v.map(x => typeof x === 'number' ? fmtNum(x) : esc(String(x))).join(', ');
        return '<span class="out-val">[' + inner + ']</span>';
    }
    if (typeof v === 'number') {
        const display = Number.isInteger(v) ? String(v) : v.toFixed(6);
        const ann = Number.isInteger(v) && VALUE_NAMES[v] ? '  <span class="out-ann">(' + VALUE_NAMES[v] + ')</span>' : '';
        return '<span class="out-val">' + esc(display) + '</span>' + ann;
    }
    return '<span class="out-val">' + esc(String(v)) + '</span>';
}

const GRID_COLORS = ['#111','#0074D9','#FF4136','#2ECC40','#FFDC00','#AAAAAA','#F012BE','#FF851B','#7FDBFF','#870C25'];

function fmtGrid(g) {
    if (!Array.isArray(g) || g.length === 0) return fmtValue(g);
    const R = g.length, C = Array.isArray(g[0]) ? g[0].length : 0;
    if (C === 0) return '<span class="out-val">[]</span>';
    let html = '<div class="grid-display" style="grid-template-columns:repeat(' + C + ',20px)">';
    for (let r = 0; r < R; r++) {
        const row = g[r];
        if (!Array.isArray(row)) continue;
        for (let c = 0; c < row.length; c++) {
            const v = typeof row[c] === 'number' ? Math.round(row[c]) : 0;
            const color = (v >= 0 && v < 10) ? GRID_COLORS[v] : '#333';
            const txt = v !== 0 ? v : '';
            html += '<div class="grid-cell" style="background:' + color + '">' + txt + '</div>';
        }
    }
    return html + '</div>';
}

// ================================================================
//  Tokenizer
// ================================================================
const KEYWORDS = new Set(['let','fn','print','if','then','else','while','do','for','in']);

function tokenize(src) {
    const T = [];
    let i = 0, len = src.length;
    while (i < len) {
        if (/\s/.test(src[i])) { i++; continue; }
        if (src[i] === '-' && src[i+1] === '-') { while (i < len && src[i] !== '\n') i++; continue; }
        if (/\d/.test(src[i]) || (src[i] === '.' && i+1 < len && /\d/.test(src[i+1]))) {
            let num = '';
            while (i < len && /[\d.]/.test(src[i])) num += src[i++];
            T.push({t:'NUM', v:parseFloat(num)}); continue;
        }
        if (src[i] === '"') {
            i++; let s = '';
            while (i < len && src[i] !== '"') s += src[i++];
            if (i < len) i++;
            T.push({t:'STR', v:s}); continue;
        }
        if (/[a-zA-Z_]/.test(src[i])) {
            let id = '';
            while (i < len && /[a-zA-Z0-9_]/.test(src[i])) id += src[i++];
            T.push({t: KEYWORDS.has(id) ? id.toUpperCase() : 'ID', v:id}); continue;
        }
        if (src[i] === '=' && i+1 < len && src[i+1] === '=') { T.push({t:'==', v:'=='}); i+=2; continue; }
        const ch = src[i];
        if ('+-*/^~@<>=()[]|,;'.includes(ch)) { T.push({t:ch, v:ch}); i++; continue; }
        i++;
    }
    T.push({t:'EOF', v:null});
    return T;
}

// ================================================================
//  Parser
// ================================================================
class Parser {
    constructor(tokens) { this.T = tokens; this.p = 0; }
    pk() { return this.T[this.p]; }
    adv() { return this.T[this.p++]; }
    expect(t) {
        const tok = this.adv();
        if (tok.t !== t) throw new Error('Expected ' + t + ', got ' + tok.t + ' "' + tok.v + '"');
        return tok;
    }
    match(t) { if (this.pk().t === t) { this.adv(); return true; } return false; }

    parseProgram() {
        const stmts = [];
        while (this.pk().t !== 'EOF') stmts.push(this.parseStmt());
        return stmts;
    }

    parseStmt() {
        switch (this.pk().t) {
            case 'LET': return this.parseLet();
            case 'FN': return this.parseFn();
            case 'PRINT': return this.parsePrint();
            default: return {t:'ExprStmt', expr:this.parseExpr()};
        }
    }

    parseLet() {
        this.expect('LET');
        const name = this.expect('ID').v;
        this.expect('=');
        return {t:'Let', name, val:this.parseExpr()};
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

    parsePrint() {
        this.expect('PRINT');
        if (this.pk().t === 'STR') return {t:'Print', expr:{t:'Str', v:this.adv().v}};
        return {t:'Print', expr:this.parseExpr()};
    }

    parseExpr() {
        let left = this.parseIfOrCmp();
        while (this.pk().t === ';') { this.adv(); left = {t:'Seq', a:left, b:this.parseIfOrCmp()}; }
        return left;
    }

    parseIfOrCmp() {
        if (this.pk().t === 'IF') return this.parseIf();
        if (this.pk().t === 'LET') return this.parseLetExpr();
        if (this.pk().t === 'FOR') return this.parseFor();
        return this.parseCmp();
    }

    parseFor() {
        this.expect('FOR');
        const varName = this.expect('ID').v;
        this.expect('IN');
        const iter = this.parseCmp();
        this.expect('DO');
        return {t:'For', varName, iter, body:this.parseExpr()};
    }

    parseLetExpr() {
        this.expect('LET');
        const name = this.expect('ID').v;
        this.expect('=');
        const val = this.parseExpr();
        if (this.pk().t === 'IN') { this.adv(); }
        return {t:'LetExpr', name, val, body:this.parseExpr()};
    }

    parseIf() {
        this.expect('IF');
        const cond = this.parseExpr();
        this.expect('THEN');
        const then_ = this.parseExpr();
        this.expect('ELSE');
        return {t:'If', cond, then_, else_:this.parseExpr()};
    }

    parseCmp() {
        let left = this.parseAdd();
        while (['<','>','=='].includes(this.pk().t)) {
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
        while (['*','/'].includes(this.pk().t)) {
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
        if (this.pk().t === '~') { this.adv(); return {t:'Unary', op:'~', e:this.parseUnary()}; }
        if (this.pk().t === '-') { this.adv(); return {t:'Bin', op:'-', l:{t:'Num',v:0}, r:this.parseUnary()}; }
        return this.parseThresh();
    }

    parseThresh() {
        let e = this.parsePostfix();
        if (this.pk().t === '@') { this.adv(); e = {t:'Thresh', val:e, th:this.parsePostfix()}; }
        return e;
    }

    parsePostfix() {
        let e = this.parsePrimary();
        while (this.pk().t === '[') { this.adv(); const idx = this.parseExpr(); this.expect(']'); e = {t:'Idx', arr:e, idx}; }
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
        if (tok.t === '(') {
            this.adv();
            const first = this.parseExpr();
            if (this.pk().t === '|') {
                this.adv(); const second = this.parseExpr();
                this.expect('|'); const third = this.parseExpr();
                this.expect(')');
                return {t:'DFloat', s:first, b:second, a:third};
            }
            this.expect(')');
            return first;
        }
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
        throw new Error('Unexpected: ' + tok.t + ' "' + tok.v + '"');
    }
}

function parse(src) {
    return new Parser(tokenize(src)).parseProgram();
}

// ================================================================
//  Builtins Registry
// ================================================================
const BUILTINS = {};

// --- Ring builtins (with trace) ---
BUILTINS.coupling = function(args, ctx) {
    const n = args[0], r = ringMod(n), g = gcd(r, N), result = N / g;
    ctx.trace('<span class="tr-fn">coupling</span>(' + n + '): <span class="tr-step">' + n + ' mod ' + N + ' = ' + r + ', gcd(' + r + ', ' + N + ') = ' + g + ', ' + N + ' / ' + g + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.crt = function(args, ctx) {
    const result = crt(args[0]), r = ringMod(args[0]);
    ctx.trace('<span class="tr-fn">crt</span>(' + args[0] + '): <span class="tr-step">' + r + ' mod 8 = ' + result[0] + ', ' + r + ' mod 9 = ' + result[1] + ', ' + r + ' mod 25 = ' + result[2] + ', ' + r + ' mod 49 = ' + result[3] + ', ' + r + ' mod 11 = ' + result[4] + '</span> = <span class="tr-result">[' + result.join(', ') + ']</span>');
    return result;
};

BUILTINS.eigenvalue = function(args, ctx) {
    const c = crt(args[0]), P = Math.PI;
    const terms = [2*Math.cos(2*P*c[0]/8), 2*Math.cos(2*P*c[1]/9), 2*Math.cos(2*P*c[2]/25), 2*Math.cos(2*P*c[3]/49), 2*Math.cos(2*P*c[4]/11)];
    const result = terms.reduce((a,b) => a+b, 0);
    ctx.trace('<span class="tr-fn">eigenvalue</span>(' + args[0] + '): <span class="tr-step">crt=[' + c.join(',') + ']</span> = <span class="tr-result">' + result.toFixed(6) + '</span>');
    return result;
};

BUILTINS.mirror = function(args, ctx) {
    const result = mirror(args[0]);
    ctx.trace('<span class="tr-fn">mirror</span>(' + args[0] + '): <span class="tr-step">' + N + ' - ' + ringMod(args[0]) + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.phi = function(args, ctx) {
    const input = args.length > 0 ? args[0] : N;
    const result = eulerPhi(input);
    ctx.trace('<span class="tr-fn">phi</span>(' + input + ') = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.order = function(args, ctx) {
    const result = multOrder(args[0]);
    ctx.trace('<span class="tr-fn">order</span>(' + args[0] + '): <span class="tr-step">gcd(' + ringMod(args[0]) + ', ' + N + ')=' + gcd(ringMod(args[0]), N) + (gcd(ringMod(args[0]), N) !== 1 ? ' (not a unit!)' : ', ' + ringMod(args[0]) + '^k mod ' + N + ' = 1 at k=' + result) + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

// --- Math builtins (no trace) ---
BUILTINS.gcd = (args) => gcd(args[0], args[1]);
BUILTINS.mod = (args) => args[1] !== 0 ? ringMod(Math.round(args[0]) % Math.round(args[1])) : 0;
BUILTINS.inv = (args) => { const r = multInverse(args[0]); if (r < 0) throw new Error('No inverse: gcd(' + args[0] + ', ' + N + ') != 1'); return r; };
BUILTINS.abs = (args) => Math.abs(args[0]);
BUILTINS.min = (args) => Math.min(args[0], args[1]);
BUILTINS.max = (args) => Math.max(args[0], args[1]);
BUILTINS.sqrt = (args) => Math.floor(Math.sqrt(Math.abs(args[0])));
BUILTINS.len = (args) => Array.isArray(args[0]) ? args[0].length : 0;

// --- Array builtins ---
BUILTINS.range = function(args) {
    if (args.length === 1) { const n = Math.min(Math.max(0, Math.round(args[0])), 10000); return Array.from({length:n}, (_,i) => i); }
    const a = Math.round(args[0]), b = Math.min(Math.round(args[1]), a + 10000);
    return Array.from({length: Math.max(0, b - a)}, (_, i) => a + i);
};

BUILTINS.kingdom = function(args) {
    const n = ringMod(args[0]); if (n === 0) return 0;
    const g = gcd(n, N);
    if (g % 2 === 0) return 2; if (g % 3 === 0) return 3;
    if (g % 5 === 0) return 5; if (g % 7 === 0) return 7;
    if (g % 11 === 0) return 11; return 1;
};

BUILTINS.sum = function(args) {
    if (!Array.isArray(args[0])) throw new Error('sum expects array');
    let s = 0; for (const x of args[0]) s = ringMod(s + (typeof x === 'number' ? x : 0)); return s;
};

BUILTINS.product = function(args) {
    if (!Array.isArray(args[0])) throw new Error('product expects array');
    let p = 1; for (const x of args[0]) p = ringMod(p * (typeof x === 'number' ? x : 0)); return p;
};

// --- Output builtins ---
BUILTINS.show = function(args, ctx) {
    ctx.output(fmtValue(args[0]), args[0]);
    return args[0];
};

BUILTINS.show_grid = function(args, ctx) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('show_grid: not a grid');
    ctx.output(fmtGrid(g), g);
    return g;
};

// --- Grid builtins (S465) ---
BUILTINS.grid = function(args) {
    const rows = Math.min(Math.max(1, Math.round(args[0])), 30);
    const cols = Math.min(Math.max(1, Math.round(args[1])), 30);
    const val = args.length > 2 ? args[2] : 0;
    return Array.from({length: rows}, () => Array.from({length: cols}, () => val));
};

BUILTINS.gset = function(args) {
    const g = args[0], r = Math.floor(args[1]), c = Math.floor(args[2]), v = args[3];
    if (!Array.isArray(g) || !Array.isArray(g[0])) throw new Error('gset: not a grid');
    if (r < 0 || r >= g.length || c < 0 || c >= g[0].length) throw new Error('gset: out of bounds (' + r + ',' + c + ')');
    g[r][c] = v;
    return g;
};

BUILTINS.rows = (args) => Array.isArray(args[0]) ? args[0].length : 0;
BUILTINS.cols = (args) => (Array.isArray(args[0]) && args[0].length > 0 && Array.isArray(args[0][0])) ? args[0][0].length : 0;

BUILTINS.hflip = function(args) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('hflip: not a grid');
    return g.map(row => Array.isArray(row) ? [...row].reverse() : row);
};

BUILTINS.vflip = function(args) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('vflip: not a grid');
    return [...g].reverse().map(row => Array.isArray(row) ? [...row] : row);
};

BUILTINS.rot90 = function(args) {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0 || !Array.isArray(g[0])) throw new Error('rot90: not a grid');
    const R = g.length, C = g[0].length;
    return Array.from({length: C}, (_, c) => Array.from({length: R}, (_, r) => g[R-1-r][c]));
};

BUILTINS.transpose = function(args) {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0 || !Array.isArray(g[0])) throw new Error('transpose: not a grid');
    const R = g.length, C = g[0].length;
    return Array.from({length: C}, (_, c) => Array.from({length: R}, (_, r) => g[r][c]));
};

BUILTINS.grid_eq = function(args) {
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b) || a.length !== b.length) return 0;
    for (let i = 0; i < a.length; i++) {
        if (!Array.isArray(a[i]) || !Array.isArray(b[i]) || a[i].length !== b[i].length) return 0;
        for (let j = 0; j < a[i].length; j++) if (a[i][j] !== b[i][j]) return 0;
    }
    return 1;
};

// ================================================================
//  Evaluator
// ================================================================
const MAX_DEPTH = 49; // b^2

function run(src) {
    const outputLines = [];
    const values = [];
    const traces = [];
    const TRACE_LIMIT = 50;

    const ctx = {
        trace: function(html) {
            if (traces.length < TRACE_LIMIT) traces.push(html);
            else if (traces.length === TRACE_LIMIT) traces.push('<span class="tr-step">... (trace limit reached)</span>');
        },
        output: function(html, val) {
            outputLines.push(html);
            values.push(val);
        }
    };

    const tokens = tokenize(src);
    const stmts = new Parser(tokens).parseProgram();
    const env = {...CONSTANTS};
    const fns = {};

    function ev(node, localEnv, depth) {
        if (depth > MAX_DEPTH) throw new Error('Max recursion depth (' + MAX_DEPTH + ') exceeded');
        switch (node.t) {
            case 'Num': return ringMod(node.v);
            case 'Str': return node.v;
            case 'Sym': {
                if (node.name in localEnv) return localEnv[node.name];
                if (node.name in fns) return fns[node.name];
                throw new Error('Unknown: ' + node.name);
            }
            case 'Bin': {
                const l = ev(node.l, localEnv, depth), r = ev(node.r, localEnv, depth);
                switch (node.op) {
                    case '+': return ringMod(l + r);
                    case '-': return ringMod(l - r);
                    case '*': return ringMod(l * r);
                    case '/': {
                        const inv = multInverse(r);
                        if (inv >= 0) return ringMod(l * inv);
                        if (r === 0) throw new Error('Division by zero');
                        return l / r;
                    }
                    case '^': return modPow(l, r);
                    case '<': return l < r ? 1 : 0;
                    case '>': return l > r ? 1 : 0;
                    case '==': return l === r ? 1 : 0;
                }
                break;
            }
            case 'Unary':
                if (node.op === '~') return ringMod(N - ev(node.e, localEnv, depth));
                break;
            case 'Thresh': {
                const v = ev(node.val, localEnv, depth);
                const th = ev(node.th, localEnv, depth);
                return v > th ? v : ringMod(N - v);
            }
            case 'If': {
                const c = ev(node.cond, localEnv, depth);
                return c !== 0 ? ev(node.then_, localEnv, depth) : ev(node.else_, localEnv, depth);
            }
            case 'Seq':
                ev(node.a, localEnv, depth);
                return ev(node.b, localEnv, depth);
            case 'LetExpr': {
                const val = ev(node.val, localEnv, depth);
                return ev(node.body, {...localEnv, [node.name]: val}, depth);
            }
            case 'Call': return evalCall(node.fn, node.args, localEnv, depth);
            case 'Idx': {
                const arr = ev(node.arr, localEnv, depth);
                const idx = Math.floor(ev(node.idx, localEnv, depth));
                if (!Array.isArray(arr)) throw new Error('Cannot index non-array');
                if (idx < 0 || idx >= arr.length) throw new Error('Index out of bounds: ' + idx);
                return arr[idx];
            }
            case 'Arr': return node.elems.map(e => ev(e, localEnv, depth));
            case 'For': {
                const arr = ev(node.iter, localEnv, depth);
                if (!Array.isArray(arr)) throw new Error('for..in requires an array');
                if (arr.length > 10000) throw new Error('Iteration limit (max 10000)');
                return arr.map(item => ev(node.body, {...localEnv, [node.varName]: item}, depth));
            }
            case 'DFloat': {
                const s = ev(node.s, localEnv, depth);
                const b = ev(node.b, localEnv, depth);
                return ringMod(Math.floor(s * b));
            }
        }
        throw new Error('Cannot evaluate: ' + JSON.stringify(node));
    }

    function evalCall(fnName, argNodes, localEnv, depth) {
        const args = argNodes.map(a => ev(a, localEnv, depth));
        // Check builtins
        if (BUILTINS[fnName]) return BUILTINS[fnName](args, ctx);
        // User-defined function
        if (fnName in fns) {
            const fn = fns[fnName];
            if (args.length !== fn.params.length) throw new Error(fnName + ' expects ' + fn.params.length + ' args, got ' + args.length);
            const callEnv = {...fn.closureEnv};
            for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
            return ev(fn.body, callEnv, depth + 1);
        }
        throw new Error('Unknown function: ' + fnName);
    }

    // Execute statements
    let error = null;
    try {
        for (const stmt of stmts) {
            switch (stmt.t) {
                case 'Let':
                    env[stmt.name] = ev(stmt.val, env, 0);
                    break;
                case 'Fn':
                    fns[stmt.name] = {params:stmt.params, body:stmt.body, closureEnv:{...env}};
                    for (const name in fns) fns[name].closureEnv = {...env, ...Object.fromEntries(Object.entries(fns).map(([k,v])=>[k,v]))};
                    break;
                case 'Print': {
                    const outBefore = outputLines.length;
                    const val = ev(stmt.expr, env, 0);
                    if (outputLines.length === outBefore) {
                        outputLines.push(typeof val === 'string' ? fmtText(val) : fmtValue(val));
                    }
                    values.push(val);
                    break;
                }
                case 'ExprStmt': {
                    const outBefore = outputLines.length;
                    const val = ev(stmt.expr, env, 0);
                    if (outputLines.length === outBefore) {
                        outputLines.push(fmtValue(val));
                    }
                    values.push(val);
                    break;
                }
            }
        }
    } catch(e) {
        error = e.message;
    }

    return { lines: outputLines, values, traces, error };
}

// ================================================================
//  Public API
// ================================================================
return {
    N, CONSTANTS, VALUE_NAMES, KEYWORDS, BUILTINS, GRID_COLORS,
    BUILTIN_NAMES: new Set(Object.keys(BUILTINS)),

    // Ring math (exposed for pages that need direct access)
    ringMod, gcd, crt, coupling, eigenvalue, mirror,
    eulerPhi, multOrder, multInverse, modPow,

    // Language
    tokenize, parse, Parser, run,

    // Formatting
    esc, fmtValue, fmtGrid, fmtNum, fmtText
};

})();
