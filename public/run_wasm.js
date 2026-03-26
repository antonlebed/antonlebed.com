#!/usr/bin/env node
/* run_wasm.js -- Generic WASM runner. Replaces run_axc.js + run_build.js.
   Loads any .wasm, provides standard imports, calls _main().
   Usage: node run_wasm.js <file.wasm> [args passed to cliArgs()]
   readFile/writeBinary resolve relative to CWD.
   writeBinary("-", data) writes to stdout. show_str goes to stderr. */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

function readStr(mem, ptr) {
  const m = new Int32Array(mem.buffer);
  const len = m[ptr / 4];
  let s = '';
  for (let i = 0; i < len; i++) s += String.fromCharCode(m[ptr / 4 + 1 + i]);
  return s;
}
function writeStr(mem, ptr, str) {
  const m = new Int32Array(mem.buffer);
  m[ptr / 4] = str.length;
  for (let i = 0; i < str.length; i++) m[ptr / 4 + 1 + i] = str.charCodeAt(i);
}

(async () => {
  const wasmPath = process.argv[2];
  if (!wasmPath) { process.stderr.write('Usage: node run_wasm.js <file.wasm> [args...]\n'); process.exit(1); }
  const fwdArgs = process.argv.slice(3);
  const wasmBytes = fs.readFileSync(wasmPath);
  let inst;

  const noop = () => 0;
  const { instance } = await WebAssembly.instantiate(wasmBytes, {
    env: {
      show_int: v => { process.stderr.write('  ' + v + '\n'); return v; },
      show_str: p => {
        if (inst) process.stderr.write(readStr(inst.exports.memory, p) + '\n');
        return p;
      },
      dom_create: noop, dom_text: noop, dom_attr: noop, dom_style: noop,
      dom_append: noop, dom_body: noop, dom_inner: noop, dom_on: noop,
      dom_query: noop, dom_head_meta: noop, get_hash: noop, dom_value: noop,
      dom_on1: noop, repl_eval: noop, dom_on2: noop, dom_window: noop,
      cvs_getctx: noop, cvs_fillrect: noop, cvs_clearrect: noop, cvs_strokerect: noop,
      cvs_fillstyle: noop, cvs_strokestyle: noop, cvs_linewidth: noop, cvs_beginpath: noop,
      cvs_arc: noop, cvs_fill: noop, cvs_stroke: noop, cvs_filltext: noop,
      cvs_moveto: noop, cvs_lineto: noop, cvs_setsize: noop,
      raf: noop, key_state: noop, cvs_font: noop,
      dom_set_root: noop, dom_spa_init: noop, dom_scroll: noop, get_category: noop,
      shell_exec: p => {
        const cmd = readStr(inst.exports.memory, p);
        try { execSync(cmd, { stdio: 'inherit', shell: 'bash' }); return 0; }
        catch (e) { return e.status || 1; }
      },
      readFile: p => {
        const fp = readStr(inst.exports.memory, p);
        const full = path.resolve(fp);
        const content = fs.readFileSync(full, 'utf8');
        const ptr = inst.exports.js_alloc(content.length);
        const m = new Int32Array(inst.exports.memory.buffer);
        for (let i = 0; i < content.length; i++) m[ptr / 4 + 1 + i] = content.charCodeAt(i);
        return ptr;
      },
      writeBinary: (pp, dp) => {
        const fp = readStr(inst.exports.memory, pp);
        const m = new Int32Array(inst.exports.memory.buffer);
        const len = m[dp / 4];
        if (fp === '-') {
          const buf = Buffer.alloc(len);
          for (let i = 0; i < len; i++) buf[i] = m[dp / 4 + 1 + i];
          process.stdout.write(buf);
        } else {
          const bytes = new Uint8Array(len);
          for (let i = 0; i < len; i++) bytes[i] = m[dp / 4 + 1 + i];
          if (fp.endsWith('.wasm')) {
            const valid = WebAssembly.validate(bytes);
            process.stderr.write(fp + ': ' + bytes.length + ' bytes (valid=' + valid + ')\n');
            if (!valid) { process.stderr.write('ERROR: Invalid WASM\n'); process.exit(1); }
          } else {
            process.stderr.write(fp + ': ' + bytes.length + ' bytes\n');
          }
          fs.writeFileSync(path.resolve(fp), bytes);
        }
        return len;
      },
      cliArgs: () => {
        const ptr = inst.exports.js_alloc(fwdArgs.length);
        const m = new Int32Array(inst.exports.memory.buffer);
        for (let i = 0; i < fwdArgs.length; i++) {
          const sp = inst.exports.js_alloc(fwdArgs[i].length);
          const m2 = new Int32Array(inst.exports.memory.buffer);
          m2[sp / 4] = fwdArgs[i].length;
          for (let j = 0; j < fwdArgs[i].length; j++) m2[sp / 4 + 1 + j] = fwdArgs[i].charCodeAt(j);
          new Int32Array(inst.exports.memory.buffer)[ptr / 4 + 1 + i] = sp;
        }
        return ptr;
      }
    }
  });
  inst = instance;
  inst.exports.memory.grow(48000);
  process.stderr.write('Memory: ' + ((48016 * 65536 / 1048576) | 0) + 'MB\n');
  inst.exports._main();
})().catch(e => { process.stderr.write('run_wasm: ' + e.message + '\n'); process.exit(1); });
