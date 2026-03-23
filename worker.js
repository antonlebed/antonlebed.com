/* ☠️ SCAFFOLDING — Cloudflare Worker: SPA routing + SSR.
   Browser → bootstrap.html (WASM + DOM imports).
   Crawler → SSR: same site.wasm, string-based imports → full HTML.
   Same .ax code, two surfaces. WYSIWYG by construction.
   Dies when WASI provides native server-side DOM. */

import siteWasm from './public/site.wasm';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    /* Static assets (.html, .js, .wasm, .png, .jpg, .css) */
    if (url.pathname.includes('.')) {
      return env.ASSETS.fetch(request);
    }

    /* ===== SSR for ALL requests. Browsers get WASM bootstrap appended. ===== */
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
        /* Game/ring import stubs — coupling() in widgets triggers ALL game imports */
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
        coupling: function(n){var N=970200;n=((n%N)+N)%N;function g(a,b){while(b){var t=b;b=a%b;a=t;}return a;}return N/g(n||N,N);},
        kingdom: function(n){var N=970200;n=((n%N)+N)%N;if(n===0)return 0;var ps=[2,3,5,7,11];for(var i=0;i<5;i++)if(n%ps[i]===0)return ps[i];return 1;},
        eigenvalue: function(n){var N=970200,qs=[8,9,25,49,11];n=((n%N)+N)%N;var t=0;for(var i=0;i<5;i++)t+=2*Math.cos(2*Math.PI*(n%qs[i])/qs[i]);return Math.round(t*1000);},
        mirror: function(n){return((970200-(n%970200))%970200);},
        crt_r: function(n,c){var qs=[8,9,25,49,11];return((n%970200)+970200)%970200%qs[c];},
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
          var ptr = 900000, m = new Int32Array(mem.buffer);
          m[ptr / 4] = route.length;
          for (var i = 0; i < route.length; i++) m[ptr / 4 + 1 + i] = route.charCodeAt(i);
          return ptr;
        },
        dom_value: function() { return 0; },
        repl_eval: function() { return 0; }
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

      /* Bootstrap script: browsers load WASM and take over (progressive enhancement).
         LLMs/crawlers see the HTML, ignore the script. */
      var boot = '<script>' +
        'var _domId=0,_dom={0:document.body};' +
        'function readStr(m,p){var a=new Int32Array(m.buffer),n=a[p/4],s="";for(var i=0;i<n;i++)s+=String.fromCharCode(a[p/4+1+i]);return s}' +
        '(async function(){var mem=null;function rs(p){return readStr(mem,p)}' +
        'var w=await WebAssembly.instantiate(await(await fetch("/site.wasm")).arrayBuffer(),{env:{' +
        'show_int:function(v){return v},show_str:function(p){return p},' +
        'canvas_clear:function(){return 0},canvas_rect:function(){return 0},canvas_circle:function(){return 0},canvas_line:function(){return 0},' +
        'canvas_pixel:function(){return 0},canvas_text:function(){return 0},canvas_width:function(){return 800},canvas_height:function(){return 600},' +
        'mouseX:function(){return 0},mouseY:function(){return 0},mouseClick:function(){return 0},keyPressed:function(){return 0},' +
        'now_ms:function(){return Date.now()},beep:function(){return 0},playNote:function(){return 0},stopSound:function(){return 0},' +
        'gvar:function(){return 0},svar:function(){return 0},gvar_f:function(){return 0},svar_f:function(){return 0},set_ring:function(){return 0},' +
        'coupling:function(n){var N=970200;n=((n%N)+N)%N;function g(a,b){while(b){var t=b;b=a%b;a=t}return a}return N/g(n||N,N)},' +
        'kingdom:function(n){var N=970200;n=((n%N)+N)%N;if(n===0)return 0;var ps=[2,3,5,7,11];for(var i=0;i<5;i++)if(n%ps[i]===0)return ps[i];return 1},' +
        'eigenvalue:function(n){var N=970200,qs=[8,9,25,49,11];n=((n%N)+N)%N;var t=0;for(var i=0;i<5;i++)t+=2*Math.cos(2*Math.PI*(n%qs[i])/qs[i]);return Math.round(t*1000)},' +
        'mirror:function(n){return((970200-(n%970200))%970200)},crt_r:function(n,c){var qs=[8,9,25,49,11];return((n%970200)+970200)%970200%qs[c]},' +
        'rand:function(n){return Math.floor(Math.random()*n)},grid:function(){return 0},gset:function(){return 0},' +
        'show_grid:function(){return 0},hflip:function(){return 0},vflip:function(){return 0},rot90:function(){return 0},transpose:function(){return 0},grid_eq:function(){return 0},' +
        'dom_create:function(p){var el=document.createElement(rs(p));_dom[++_domId]=el;return _domId},' +
        'dom_text:function(h,p){if(_dom[h])_dom[h].textContent=rs(p);return 0},' +
        'dom_attr:function(h,np,vp){if(_dom[h])_dom[h].setAttribute(rs(np),rs(vp));return 0},' +
        'dom_style:function(h,pp,vp){if(_dom[h])_dom[h].style[rs(pp)]=rs(vp);return 0},' +
        'dom_append:function(ph,ch){if(_dom[ph]&&_dom[ch])_dom[ph].appendChild(_dom[ch]);return 0},' +
        'dom_body:function(){return 0},' +
        'dom_inner:function(h,p){if(_dom[h])_dom[h].innerHTML=rs(p);return 0},' +
        'dom_on:function(h,ep,fnp){if(_dom[h]){var e=rs(ep),f=rs(fnp);_dom[h].addEventListener(e,function(){if(w.instance.exports[f])w.instance.exports[f]()});return 0}return 0},' +
        'dom_on1:function(h,ep,fnp){if(_dom[h]){var e=rs(ep),f=rs(fnp);_dom[h].addEventListener(e,function(ev){if(w.instance.exports[f])w.instance.exports[f](ev.keyCode||ev.which||ev.button||0)});return 0}return 0},' +
        'dom_on2:function(h,ep,fnp){if(_dom[h]){var e=rs(ep),f=rs(fnp);_dom[h].addEventListener(e,function(ev){if(w.instance.exports[f])w.instance.exports[f](ev.offsetX||0,ev.offsetY||0)});return 0}return 0},' +
        'dom_window:function(ep,fnp){var e=rs(ep),f=rs(fnp);window.addEventListener(e,function(){if(w.instance.exports[f])w.instance.exports[f]()});return 0},' +
        'dom_query:function(p){var s=rs(p);try{var el=document.querySelector(s)}catch(e){return -1}if(el){_dom[++_domId]=el;return _domId}return -1},' +
        'dom_head_meta:function(){return 0},' +
        'get_hash:function(){var parts=location.pathname.split("/").filter(Boolean);' +
        'var h=parts.length>=2?parts[parts.length-1]:(parts[0]||"home");' +
        'if(location.hash.length>1)h=location.hash.slice(1);' +
        'var ptr=900000,m=new Int32Array(mem.buffer);m[ptr/4]=h.length;' +
        'for(var i=0;i<h.length;i++)m[ptr/4+1+i]=h.charCodeAt(i);return ptr},' +
        'dom_value:function(h){var v=(_dom[h]&&(_dom[h].value||_dom[h].textContent))||"";var ptr=904000,m=new Int32Array(mem.buffer);m[ptr/4]=v.length;for(var i=0;i<v.length;i++)m[ptr/4+1+i]=v.charCodeAt(i);return ptr},' +
        'repl_eval:function(cp,rh){var code=rs(cp),el=_dom[rh];if(!el)return 0;el.innerHTML="<p style=\\"color:#999\\">Compiling...</p>";setTimeout(function(){_re(code,el)},0);return 0}' +
        '}});mem=w.instance.exports.memory;document.body.innerHTML="";_dom={0:document.body};_domId=0;w.instance.exports._main()})();' +
        'var _cMod=null,_N=970200;function _gcd(a,b){while(b){var t=b;b=a%b;a=t}return a}' +
        'async function _re(code,el){try{if(!_cMod){el.innerHTML="<p style=\\"color:#999\\">Loading compiler...</p>";var r=await fetch("/deep_ouroboros.wasm");_cMod=await WebAssembly.compile(await r.arrayBuffer())}' +
        'var pre="let o=0\\nlet s=1\\nlet D=2\\nlet K=3\\nlet E=5\\nlet b=7\\nlet L=11\\nlet GATE=13\\nlet OMEGA=606376\\nlet DATA=210\\nlet THIN=2310\\nlet HYDOR=105\\nlet LAMBDA=420\\nlet KEY=41\\nlet ANSWER=42\\n";' +
        'pre+="fn gcd(a,b)=if b==0 then a else gcd(b,a%b)\\nfn decompose(n)=[n%8,n%9,n%25,n%49,n%11]\\nfn reconstruct(arr)=arr[0]*363825+arr[1]*431200+arr[2]*853776+arr[3]*732600+arr[4]*529200\\nfn crt(n)=\\"(\\" + \\"${n%8}\\" + \\",\\" + \\"${n%9}\\" + \\",\\" + \\"${n%25}\\" + \\",\\" + \\"${n%49}\\" + \\",\\" + \\"${n%11}\\" + \\")\\"\\n";' +
        'code=pre+code;var cm=(await WebAssembly.instantiate(_cMod,{env:{show_int:function(v){return v},show_str:function(p){return p}}})).exports;' +
        'cm.memory.grow(Math.max(0,256-cm.memory.buffer.byteLength/65536));var m32=new Int32Array(cm.memory.buffer),addr=15*1024*1024;' +
        'm32[addr/4]=code.length;for(var i=0;i<code.length;i++)m32[addr/4+1+i]=code.charCodeAt(i);var bp=cm.wasm_from_src(addr);' +
        'm32=new Int32Array(cm.memory.buffer);var bl=m32[bp/4],wb=new Uint8Array(bl);for(var j=0;j<bl;j++)wb[j]=m32[bp/4+1+j];' +
        'if(!WebAssembly.validate(wb)){el.innerHTML="<pre style=\\"color:#ff6666\\">Compilation error</pre>";return}' +
        'var lines=[],childMem;var qs=[8,9,25,49,11];function rcs(p){var cm32=new Int32Array(childMem.buffer),n=cm32[p/4],s="";for(var k=0;k<n;k++)s+=String.fromCharCode(cm32[p/4+1+k]);return s}' +
        'var child=await WebAssembly.instantiate(wb.buffer,{env:{show_int:function(v){lines.push(""+v);return v},show_str:function(p){lines.push(rcs(p));return p},show_float:function(v){lines.push(""+v);return 0},' +
        'coupling:function(n){n=((n%_N)+_N)%_N;return _N/_gcd(n||_N,_N)},eigenvalue:function(n){n=((n%_N)+_N)%_N;var t=0;for(var i=0;i<5;i++)t+=2*Math.cos(2*Math.PI*(n%qs[i])/qs[i]);return Math.round(t*1000)},lambda_k:function(){return 420},' +
        'crt_r:function(n,c){return((n%_N)+_N)%_N%qs[c]},trace:function(n){n=((n%_N)+_N)%_N;var t=0;for(var i=0;i<5;i++)t+=n%qs[i];return t},' +
        'mul_order:function(n){n=((n%_N)+_N)%_N;if(_gcd(n,_N)!=1)return 0;var p=n,k=1;while(p!=1&&k<=420){p=(p*n)%_N;k++}return k},' +
        'sin_f:Math.sin,cos_f:Math.cos,sqrt_f:Math.sqrt,log_f:Math.log,exp_f:Math.exp,abs_f:Math.abs,floor_f:Math.floor,ceil_f:Math.ceil,' +
        'pow_f:Math.pow,toFloat:function(v){return v},PI_f:function(){return Math.PI},atan2_f:Math.atan2,rand:function(n){return Math.floor(Math.random()*n)},' +
        'canvas_clear:function(){return 0},canvas_rect:function(){return 0},canvas_circle:function(){return 0},canvas_line:function(){return 0},' +
        'canvas_text:function(){return 0},canvas_width:function(){return 800},canvas_height:function(){return 600},' +
        'play_sound:function(){return 0},stop_sound:function(){return 0},set_volume:function(){return 0},' +
        'key_down:function(){return 0},mouse_x:function(){return 0},mouse_y:function(){return 0},mouse_btn:function(){return 0},now_ms:function(){return Date.now()},' +
        'gvar:function(){return 0},svar:function(){return 0},raw_mode:function(){return 0},set_timer:function(){return 0},' +
        'grid:function(){return 0},grid_w:function(){return 0},grid_h:function(){return 0},grid_get:function(){return 0},' +
        'grid_set:function(){return 0},grid_show:function(){return 0},grid_clone:function(){return 0},grid_eq:function(){return 0}}});' +
        'childMem=child.instance.exports.memory;child.instance.exports._main();' +
        'var out=lines.join("\\n").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");' +
        'el.innerHTML=lines.length?"<pre style=\\"color:#88ddaa;white-space:pre-wrap;margin:0\\">"+out+"</pre>":"<p style=\\"color:#999;margin:0\\">No output (use show to display values)</p>"' +
        '}catch(e){var msg=(e.message||""+e).replace(/&/g,"&amp;").replace(/</g,"&lt;");el.innerHTML="<pre style=\\"color:#ff6666;margin:0\\">Error: "+msg+"</pre>"}}' +
        '<\/script>';

      /* Full HTML: <head> + rendered body + bootstrap script */
      var html = '<!DOCTYPE html><html lang="en" style="background:#050508"><head>' + head + '</head>' + render(0) + boot + '</html>';

      return new Response(html, {
        headers: { 'Content-Type': 'text/html;charset=utf-8' }
      });

    } catch (e) {
      /* SSR failed — fallback to bootstrap (client-side rendering) */
      return env.ASSETS.fetch(new URL('/_app.html', url.origin).toString());
    }
  }
};
