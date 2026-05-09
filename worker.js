/* [DEAD] SCAFFOLDING -- Cloudflare Worker: SPA routing + SSR.
   Browser -> _app.html (WASM + DOM imports).
   Crawler -> SSR: per-module WASM, string-based imports -> full HTML.
   Same .ax code, two surfaces. WYSIWYG by construction.
   Dies when WASI provides native server-side DOM. */

var _routeMap = {
  '':'home','home':'home',
  'basics':'home','structure':'structure','teach':'teach',
  'data':'data','deep':'deep','living':'living','demos':'demos',
  'eigenvalue_swim':'structure','repl':'living','egg':'living',
  '5016':'4924',
  '5352':'4924',
  '5668':'4924',
  '5976':'4924',
  '6284':'4924',
  '6592':'4924',
  '6812':'4924',
  '7132':'4924',
  '7488':'7360',
  '7900':'7360',
  '8136':'7360',
  '8360':'7360',
  '8584':'7360',
  '8804':'7360',
  '9012':'7360',
  '9284':'7360',
  '9500':'7360',
  '9724':'7360',
  '9948':'7360',
  '10200':'7360',
  '10472':'7360',
  '10688':'7360',
  '10956':'7360',
  '11380':'11272',
  '11668':'11272',
  '11912':'11272',
  '12148':'11272',
  '12340':'11272',
  '12596':'11272',
  '12872':'11272',
  '13136':'11272',
  '13356':'11272',
  '13564':'11272',
  '13800':'11272',
  '14084':'11272',
  '14344':'11272',
  '14556':'11272',
  '14800':'11272',
  '15084':'11272',
  '15400':'11272',
  '15644':'11272',
  '15940':'11272',
  '16272':'11272',
  '16500':'11272',
  '16792':'11272',
  '17116':'17056',
  '17344':'17056',
  '17536':'17056',
  '17724':'17056',
  '17968':'17056',
  '18128':'17056',
  '18312':'17056',
  '18664':'17056',
  '18880':'17056',
  '19052':'17056',
  '19240':'17056',
  '19412':'17056',
  '19620':'17056',
  '19884':'17056',
  '20172':'17056',
  '20416':'17056',
  '20616':'17056',
  '20840':'17056',
  '21024':'17056',
  '21236':'17056',
  '21420':'17056',
  '21628':'17056',
  '21832':'17056',
  '22044':'17056',
  '22240':'17056',
  '22456':'17056',
  '22592':'17056',
  '22800':'17056',
  '23040':'17056',
  '23292':'17056',
  '23668':'17056',
  '23880':'17056',
  '24068':'17056',
  '24224':'17056',
  '24388':'17056',
  '24612':'17056',
  '24856':'17056',
  '25036':'17056',
  '25220':'17056',
  '25448':'17056',
  '25676':'17056',
  '25856':'17056',
  '26072':'17056',
  '26380':'17056',
  '26612':'17056',
  '26844':'17056',
  '27096':'17056',
  '27452':'17056',
  '27812':'17056',
  '28144':'17056',
  '29856':'17056',
  '30056':'17056',
  '30228':'17056',
  '30388':'17056',
  '30556':'30512',
  '30784':'30512',
  '31020':'30512',
  '31232':'30512',
  '31472':'30512',
  '31676':'30512',
  '31916':'30512',
  '32188':'30512',
  '32384':'30512',
  '32576':'30512',
  '32764':'30512',
  '32956':'30512',
  '33156':'30512',
  '33336':'30512',
  '33520':'30512',
  '33704':'30512',
  '33912':'30512',
  '34128':'30512',
  '34332':'30512',
  '34648':'34540',
  '34864':'34540',
  '35108':'34540',
  '35340':'34540',
  '35564':'34540',
  '35796':'34540',
  '36072':'34540',
  '36268':'34540',
  '36552':'34540',
  '36828':'34540',
  '37020':'34540',
  '37284':'34540',
  '37504':'34540',
  '37680':'34540',
  '37948':'34540',
  '38152':'34540',
  '38336':'34540',
  '38500':'34540',
  '38716':'34540',
  '38980':'34540',
  '39220':'39168',
  '39396':'39168',
  '39632':'39168',
  '39832':'39168',
  '40060':'39168',
  '40232':'39168',
  '40428':'39168',
  '40668':'39168',
  '40860':'39168',
  '41048':'39168',
  '41268':'39168',
  '41456':'39168',
  '41656':'39168',
  '41868':'39168',
  '42068':'39168',
  '42288':'39168',
  '42476':'39168',
  '42684':'39168',
  '42904':'39168',
  '43132':'39168',
  '43360':'39168',
  '43564':'39168',
  '43784':'39168',
  '44008':'39168',
  '44228':'39168',
  '44448':'39168',
  '44652':'39168',
  '44868':'39168',
  '45104':'39168',
  '45316':'39168',
  '45520':'39168',
  '45736':'39168',
  '45940':'39168',
  '46172':'39168',
  '46400':'39168',
  '46592':'39168',
  '46768':'39168',
};
var _currentModule = '';
function _routeMod(r) { return _routeMap[r] || 'home'; }

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    /* ===== Sensor API: bridge writes, page reads ===== */
    if (url.pathname === '/api/sensor') {
      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET,POST', 'Access-Control-Allow-Headers': 'Authorization,Content-Type' } });
      }
      if (request.method === 'POST') {
        var auth = request.headers.get('Authorization') || '';
        if (auth !== 'Bearer crt7-sensor-214414200') {
          return new Response('Unauthorized', { status: 401 });
        }
        var body = await request.text();
        if (env.SENSOR_DATA) { await env.SENSOR_DATA.put('latest', body); }
        return new Response('OK', { status: 200, headers: { 'Access-Control-Allow-Origin': '*' } });
      }
      var data = '{}';
      /* cacheTtl: 600 -- Cloudflare edge-caches KV value 10 min (no KV read cost); */
      /* Cache-Control max-age=600 -- browser + CDN cache response 10 min (no Worker invocation). */
      /* Bridge POST naturally invalidates by overwriting the key. Cache TTL matches */
      /* sensor_bridge.py INTERVAL_SEC = 600. Free-tier safe at any viewer count. */
      if (env.SENSOR_DATA) { data = await env.SENSOR_DATA.get('latest', { cacheTtl: 600 }) || '{}'; }
      return new Response(data, { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Cache-Control': 'public, max-age=600' } });
    }

    /* Static assets (.html, .js, .wasm, .png, .jpg, .css) */
    if (url.pathname.includes('.')) {
      return env.ASSETS.fetch(request);
    }

    /* ===== SSR: render body via WASM, inject into _app.html template ===== */
    try {
      /* siteWasm is a pre-compiled WebAssembly.Module (static import) */

      /* Virtual DOM tree (handle 0 = body) */
      var nid = 0;
      var nodes = { 0: { tag: 'body', ch: [], at: {}, st: {}, tx: '', ih: '' } };
      var metas = [];
      var mem = null, _hashPtr = 0, _catPtr = 0;
      var title = 'antonlebed.com';

      /* Extract route from URL path (matches bootstrap.html logic) */
      var parts = url.pathname.split('/').filter(Boolean);
      var route = parts.length >= 2 ? parts[parts.length - 1] : (parts[0] || 'home');

      function rs(p) {
        var m = new Int32Array(mem.buffer), n = m[p / 4], s = '';
        for (var i = 0; i < n; i++) s += String.fromCharCode(m[p / 4 + 1 + i]);
        return s;
      }

      /* Fetch the right module WASM based on route */
      var _mod = _routeMod(route);
      var _wr = await env.ASSETS.fetch(new URL('/site_' + _mod + '.wasm', url.origin).toString());
      var result = await WebAssembly.instantiate(await _wr.arrayBuffer(), { env: {
        show_int: function(v) { return v; },
        show_str: function(p) { return p; },
        show_float: function(v) { return 0; },
        sin_f: Math.sin, cos_f: Math.cos, PI_f: function() { return Math.PI; }, exp_f: Math.exp,
        /* Game/ring import stubs -- coupling() in widgets triggers ALL game imports */
        canvas_clear: function(){return 0;}, canvas_rect: function(){return 0;},
        canvas_circle: function(){return 0;}, canvas_line: function(){return 0;},
        canvas_pixel: function(){return 0;}, canvas_text: function(){return 0;},
        canvas_width: function(){return 800;}, canvas_height: function(){return 600;},
        mouseX: function(){return 0;}, mouseY: function(){return 0;},
        mouseClick: function(){return 0;}, keyPressed: function(){return 0;},
        now_ms: function(){return 0;},
        beep: function(){return 0;}, playNote: function(){return 0;}, stopSound: function(){return 0;},
        gvar: function(){return 0;}, svar: function(){return 0;},
        gvar_f: function(){return 0;}, svar_f: function(){return 0;},
        set_ring: function(){return 0;},
        coupling: function(n){var N=214414200;n=((n%N)+N)%N;function g(a,b){while(b){var t=b;b=a%b;a=t;}return a;}return N/g(n||N,N);},
        kingdom: function(n){var N=214414200;n=((n%N)+N)%N;if(n===0)return 0;var ps=[2,3,5,7,11,13,17];for(var i=0;i<7;i++)if(n%ps[i]===0)return ps[i];return 1;},
        eigenvalue: function(n){var N=214414200,qs=[8,9,25,49,11,13,17];n=((n%N)+N)%N;var t=0;for(var i=0;i<7;i++)t+=2*Math.cos(2*Math.PI*(n%qs[i])/qs[i]);return Math.round(t*1000);},
        mirror: function(n){var N=214414200;return((N-(n%N))%N);},
        crt_r: function(n,c){var N=214414200,qs=[8,9,25,49,11,13,17];return((n%N)+N)%N%qs[c];},
        rand: function(n){return Math.floor(Math.random()*n);},
        grid: function(){return 0;}, gset: function(){return 0;},
        show_grid: function(){return 0;}, hflip: function(){return 0;},
        vflip: function(){return 0;}, rot90: function(){return 0;},
        transpose: function(){return 0;}, grid_eq: function(){return 0;},
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
        dom_on1: function() { return 0; },
        dom_on2: function() { return 0; },
        dom_window: function() { return 0; },
        dom_query: function() { return -1; },
        dom_head_meta: function(np, vp) {
          metas.push({ n: rs(np), c: rs(vp) });
          return 0;
        },
        get_hash: function() {
          var ptr = _hashPtr, m = new Int32Array(mem.buffer);
          m[ptr / 4] = route.length;
          for (var i = 0; i < route.length; i++) m[ptr / 4 + 1 + i] = route.charCodeAt(i);
          return ptr;
        },
        dom_value: function() { return 0; },
        /* Canvas 2D stubs -- no-op for SSR (canvas is browser-only) */
        cvs_getctx: function() { return -1; },
        cvs_fillrect: function() { return 0; },
        cvs_clearrect: function() { return 0; },
        cvs_strokerect: function() { return 0; },
        cvs_fillstyle: function() { return 0; },
        cvs_strokestyle: function() { return 0; },
        cvs_linewidth: function() { return 0; },
        cvs_beginpath: function() { return 0; },
        cvs_arc: function() { return 0; },
        cvs_fill: function() { return 0; },
        cvs_stroke: function() { return 0; },
        cvs_filltext: function() { return 0; },
        cvs_moveto: function() { return 0; },
        cvs_lineto: function() { return 0; },
        cvs_setsize: function() { return 0; },
        raf: function() { return 0; },
        key_state: function() { return 0; },
        cvs_font: function() { return 0; },
        readFile: function() { return 0; },
        writeBinary: function() { return 0; },
        cliArgs: function() { return 0; },
        dom_set_root: function() { return 0; },
        dom_spa_init: function() { return 0; },
        dom_scroll: function() { return 0; },
        shell_exec: function() { return 0; },
        readBinary: function() { return 0; },
        cvs_put_pixel: function() { return 0; },
        cvs_blit: function() { return 0; },
        cvs_get_pixel: function() { return 0; },
        aud_osc: function() { return 0; },
        aud_freq: function() { return 0; },
        aud_gain: function() { return 0; },
        gpu_init: function() { return 0; },
        gpu_bench: function() { return 0; },
        dom_fetch: function() { return 0; },
        dom_timeout: function() { return 0; },
        get_category: function() {
          var c = parts.length >= 2 ? parts[0] : (parts[0] || 'home');
          var ptr = _catPtr, m = new Int32Array(mem.buffer);
          m[ptr/4] = c.length;
          for (var i = 0; i < c.length; i++) m[ptr/4+1+i] = c.charCodeAt(i);
          return ptr;
        }
      }});

      var inst = result.exports ? result : (result.instance || result);
      mem = inst.exports.memory;
      _hashPtr = inst.exports.js_alloc(1024);
      _catPtr = inst.exports.js_alloc(256);
      inst.exports._main();

      /* ===== Serialize virtual DOM to HTML ===== */
      function esc(s) {
        return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
      }

      /* camelCase -> kebab-case for CSS properties */
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

      /* ===== SSOT: fetch bootstrap template, inject SSR content ===== */
      var tpl = await (await env.ASSETS.fetch(new URL('/_app.html', url.origin).toString())).text();

      /* Inject page-specific title */
      tpl = tpl.replace('<title>antonlebed.com</title>', '<title>' + esc(title) + '</title>');

      /* Inject canonical + og + custom metas before </head> */
      var headExtra = '<link rel="canonical" href="' + esc(url.href) + '">';
      headExtra += '<meta property="og:title" content="' + esc(title) + '">';
      headExtra += '<meta property="og:url" content="' + esc(url.href) + '">';
      for (var i = 0; i < metas.length; i++) {
        headExtra += '<meta name="' + esc(metas[i].n) + '" content="' + esc(metas[i].c) + '">';
        if (metas[i].n === 'description') {
          headExtra += '<meta property="og:description" content="' + esc(metas[i].c) + '">';
        }
      }
      tpl = tpl.replace('</head>', headExtra + '</head>');

      /* Inject SSR body: attributes + styles from node 0, then children */
      var bodyTag = '<body';
      var bn = nodes[0];
      for (var k in bn.at) bodyTag += ' ' + k + '="' + esc(bn.at[k]) + '"';
      var bss = '';
      for (var k in bn.st) bss += c2k(k) + ':' + bn.st[k] + ';';
      if (bss) bodyTag += ' style="' + esc(bss) + '"';
      bodyTag += '>';
      var ssrBody = '';
      for (var i = 0; i < bn.ch.length; i++) ssrBody += render(bn.ch[i]);
      tpl = tpl.replace('<body>', bodyTag + ssrBody);

      var html = tpl;

      return new Response(html, {
        headers: { 'Content-Type': 'text/html;charset=utf-8' }
      });

    } catch (e) {
      /* SSR failed -- fallback to bootstrap (client-side rendering) */
      return env.ASSETS.fetch(new URL('/_app.html', url.origin).toString());
    }
  }
};
