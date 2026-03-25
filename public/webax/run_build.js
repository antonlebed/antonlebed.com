/* run_build.js — ☠️ SCAFFOLDING. Minimal WASM runner for deep_build.wasm.
   All build logic lives in .ax (build_entry.ax). This runner only provides:
   file I/O imports (readFile, writeBinary) + show_str console output.
   Replaces build_native.js (137L hand-written JS → ~60L generic runner).
   Usage: node webax/run_build.js */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const COMPILER = path.join(ROOT, 'anton/code/deep_build.wasm');
const CWD = __dirname; /* readFile paths relative to webax/ */

/* Read length-prefixed i32 string from WASM memory */
function readString(mem, ptr) {
  const m = new Int32Array(mem.buffer);
  const len = m[ptr / 4];
  let s = '';
  for (let i = 0; i < len; i++) s += String.fromCharCode(m[ptr / 4 + 1 + i]);
  return s;
}

async function main() {
  const wasmBytes = fs.readFileSync(COMPILER);
  let inst = null;
  let topLevelExprCount = 0;
  let errorCount = 0;

  /* All 36 DOM imports as stubs. Only readFile (#34) and writeBinary (#35) are real. */
  const noop = () => 0;
  const imports = {
    env: {
      show_int: v => v,
      show_str: ptr => {
        if (!inst) return ptr;
        const s = readString(inst.exports.memory, ptr);
        if (s.startsWith('warning:') || s.startsWith('  top-level') || s.startsWith('error:')) {
          console.log(s);
          if (s.match(/top-level expr/)) topLevelExprCount++;
          if (s.startsWith('error:')) errorCount++;
        } else if (s.includes(':')) {
          /* Build output: site.wasm, _app.html, worker.js sizes */
          console.log(s);
        }
        return ptr;
      },
      /* DOM stubs (di 0-33): most pages need these, build_entry doesn't use them */
      dom_create: noop, dom_text: noop, dom_attr: noop, dom_style: noop,
      dom_append: noop, dom_body: noop, dom_inner: noop, dom_on: noop,
      dom_query: noop, dom_head_meta: noop, get_hash: noop, dom_value: noop,
      dom_on1: noop, repl_eval: noop, dom_on2: noop, dom_window: noop,
      cvs_getctx: noop, cvs_fillrect: noop, cvs_clearrect: noop, cvs_strokerect: noop,
      cvs_fillstyle: noop, cvs_strokestyle: noop, cvs_linewidth: noop, cvs_beginpath: noop,
      cvs_arc: noop, cvs_fill: noop, cvs_stroke: noop, cvs_filltext: noop,
      cvs_moveto: noop, cvs_lineto: noop, cvs_setsize: noop,
      raf: noop, key_state: noop, cvs_font: noop,
      /* CLI (di 36) + SPA (di 37-38) + scroll (di 39) */
      cliArgs: noop, dom_set_root: noop, dom_spa_init: noop, dom_scroll: noop, get_category: noop,
      /* Real file I/O (di 34-35) */
      readFile: function(pathPtr) {
        const filePath = readString(inst.exports.memory, pathPtr);
        const fullPath = path.join(CWD, filePath);
        const content = fs.readFileSync(fullPath, 'utf8');
        /* Allocate WASM memory via exported js_alloc — each call gets unique arena block */
        const resultPtr = inst.exports.js_alloc(content.length);
        const m = new Int32Array(inst.exports.memory.buffer);
        /* js_alloc already set m[resultPtr/4] = content.length, fill chars */
        for (let i = 0; i < content.length; i++) m[resultPtr / 4 + 1 + i] = content.charCodeAt(i);
        return resultPtr;
      },
      writeBinary: function(pathPtr, dataPtr) {
        const filePath = readString(inst.exports.memory, pathPtr);
        const fullPath = path.join(CWD, filePath);
        const m = new Int32Array(inst.exports.memory.buffer);
        const len = m[dataPtr / 4];
        const bytes = new Uint8Array(len);
        for (let i = 0; i < len; i++) bytes[i] = m[dataPtr / 4 + 1 + i];
        /* Validate WASM before writing (only for .wasm files) */
        if (filePath.endsWith('.wasm')) {
          const valid = WebAssembly.validate(bytes);
          console.log(`${filePath}: ${bytes.length} bytes (valid=${valid})`);
          if (!valid) { console.error('ERROR: Compiler produced invalid WASM'); process.exit(1); }
        } else {
          console.log(`${filePath}: ${bytes.length} bytes`);
        }
        fs.writeFileSync(fullPath, bytes);
        return len;
      }
    }
  };

  const { instance } = await WebAssembly.instantiate(wasmBytes, imports);
  inst = instance;

  /* Grow memory: ~3GB for large site compilations */
  const targetPages = 48000; /* ~3GB */
  inst.exports.memory.grow(targetPages - 16);
  console.log(`Memory: ${(targetPages * 65536 / 1048576) | 0}MB`);

  /* Run build — build_entry.ax logic executes as _main() */
  const t0 = Date.now();
  inst.exports._main();
  const dt = Date.now() - t0;
  console.log(`Build: ${dt}ms`);

  /* Build guards (S976 lesson) */
  if (errorCount > 0) {
    console.error(`BUILD GUARD: ${errorCount} error(s). Fix before deploying.`);
    process.exit(1);
  }
  if (topLevelExprCount > 1) {
    console.error(`BUILD GUARD: ${topLevelExprCount} top-level expression(s) (expected 1). Content bleed?`);
    process.exit(1);
  }
  console.log('Build complete.');
}

main().catch(e => { console.error(e); process.exit(1); });
