/* ☠️ SCAFFOLDING — Cloudflare Worker: SPA routing + SSR.
   Browser → bootstrap.html (WASM + DOM imports).
   Crawler → SSR: same site.wasm, string-based imports → full HTML.
   Same .ax code, two surfaces. WYSIWYG by construction.
   Dies when WASI provides native server-side DOM. */

import siteWasm from './public/site.wasm';

const CRAWLERS = /bot|crawl|spider|slurp|facebookexternalhit|whatsapp|telegram|claude-web|gptbot|chatgpt-user|perplexity|cohere|bytespider|ia_archiver|embedly|quora|pinterest|applebot|yandex|bingpreview|linkedinbot/i;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    /* Static assets (.html, .js, .wasm, .png, .jpg, .css) */
    if (url.pathname.includes('.')) {
      return env.ASSETS.fetch(request);
    }

    /* Detect crawler by User-Agent */
    const ua = request.headers.get('user-agent') || '';
    if (!CRAWLERS.test(ua)) {
      /* Browser — serve bootstrap.html (WASM + DOM path) */
      return env.ASSETS.fetch(new URL('/_app.html', url.origin).toString());
    }

    /* ===== SSR: same site.wasm, string backend ===== */
    try {
      /* siteWasm is a pre-compiled WebAssembly.Module (static import) */

      /* Virtual DOM tree (handle 0 = body) */
      var nid = 0;
      var nodes = { 0: { tag: 'body', ch: [], at: {}, st: {}, tx: '', ih: '' } };
      var metas = [];
      var mem = null;
      var title = 'antonlebed.com';

      /* Extract route from URL path (matches bootstrap.html logic) */
      var parts = url.pathname.split('/').filter(Boolean);
      var route = parts.length >= 2 ? parts[parts.length - 1] : (parts[0] || 'home');

      function rs(p) {
        var m = new Int32Array(mem.buffer), n = m[p / 4], s = '';
        for (var i = 0; i < n; i++) s += String.fromCharCode(m[p / 4 + 1 + i]);
        return s;
      }

      /* instantiate: Module → Instance, BufferSource → {module, instance} */
      var result = await WebAssembly.instantiate(siteWasm, { env: {
        show_int: function(v) { return v; },
        show_str: function(p) { return p; },
        dom_create: function(p) {
          var tag = rs(p);
          nodes[++nid] = { tag: tag, ch: [], at: {}, st: {}, tx: '', ih: '' };
          return nid;
        },
        dom_text: function(h, p) {
          if (nodes[h]) {
            var t = rs(p);
            nodes[h].tx = t;
            /* Extract page title from first h1 */
            if (nodes[h].tag === 'h1' && title === 'antonlebed.com') {
              title = t + ' \u2014 antonlebed.com';
            }
          }
          return 0;
        },
        dom_attr: function(h, np, vp) {
          if (nodes[h]) nodes[h].at[rs(np)] = rs(vp);
          return 0;
        },
        dom_style: function(h, pp, vp) {
          if (nodes[h]) nodes[h].st[rs(pp)] = rs(vp);
          return 0;
        },
        dom_append: function(ph, ch) {
          if (nodes[ph]) nodes[ph].ch.push(ch);
          return 0;
        },
        dom_body: function() { return 0; },
        dom_inner: function(h, p) {
          if (nodes[h]) nodes[h].ih = rs(p);
          return 0;
        },
        dom_on: function() { return 0; },
        dom_query: function() { return 0; },
        dom_head_meta: function(np, vp) {
          metas.push({ n: rs(np), c: rs(vp) });
          return 0;
        },
        get_hash: function() {
          var ptr = 900000, m = new Int32Array(mem.buffer);
          m[ptr / 4] = route.length;
          for (var i = 0; i < route.length; i++) m[ptr / 4 + 1 + i] = route.charCodeAt(i);
          return ptr;
        }
      }});

      var inst = result.exports ? result : (result.instance || result);
      mem = inst.exports.memory;
      inst.exports._main();

      /* ===== Serialize virtual DOM to HTML ===== */
      function esc(s) {
        return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
      }

      /* camelCase → kebab-case for CSS properties */
      function c2k(s) {
        var r = s.replace(/[A-Z]/g, function(m) { return '-' + m.toLowerCase(); });
        if (r.startsWith('webkit-') || r.startsWith('moz-')) r = '-' + r;
        return r;
      }

      var VOID = { br: 1, hr: 1, img: 1, input: 1, meta: 1, link: 1, area: 1, col: 1 };
      var RAW = { style: 1, script: 1 };

      function render(h) {
        var n = nodes[h];
        if (!n) return '';
        var o = '<' + n.tag;
        for (var k in n.at) o += ' ' + k + '="' + esc(n.at[k]) + '"';
        var ss = '';
        for (var k in n.st) ss += c2k(k) + ':' + n.st[k] + ';';
        if (ss) o += ' style="' + esc(ss) + '"';
        o += '>';
        if (VOID[n.tag]) return o;
        if (n.ih) {
          o += n.ih;
        } else {
          if (n.tx) o += RAW[n.tag] ? n.tx : esc(n.tx);
          for (var i = 0; i < n.ch.length; i++) o += render(n.ch[i]);
        }
        o += '</' + n.tag + '>';
        return o;
      }

      /* Build <head> with meta tags */
      var head = '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">';
      head += '<title>' + esc(title) + '</title>';
      head += '<link rel="icon" href="/favicon.png">';
      head += '<link rel="canonical" href="' + esc(url.href) + '">';
      head += '<meta property="og:title" content="' + esc(title) + '">';
      head += '<meta property="og:url" content="' + esc(url.href) + '">';
      head += '<meta property="og:image" content="https://antonlebed.com/og-image.jpg">';
      head += '<meta property="og:type" content="website">';
      head += '<meta property="og:site_name" content="antonlebed.com">';
      for (var i = 0; i < metas.length; i++) {
        head += '<meta name="' + esc(metas[i].n) + '" content="' + esc(metas[i].c) + '">';
        if (metas[i].n === 'description') {
          head += '<meta property="og:description" content="' + esc(metas[i].c) + '">';
        }
      }

      /* Full HTML: <head> + rendered body */
      var html = '<!DOCTYPE html><html lang="en"><head>' + head + '</head>' + render(0) + '</html>';

      return new Response(html, {
        headers: { 'Content-Type': 'text/html;charset=utf-8' }
      });

    } catch (e) {
      /* SSR failed — return error for debugging, fallback to bootstrap */
      return new Response('SSR error: ' + e.message + '\n' + e.stack, {
        status: 500,
        headers: { 'Content-Type': 'text/plain' }
      });
    }
  }
};
