// atmosphere.js -- starfield as pure CSS box-shadows, ANCHORED TO THE PAGE
// (like the text). Stars live in document space and scroll with the
// content: browser-panel show/hide moves the VIEWPORT's edges, never the
// document -- the browser keeps the page visually stationary while its
// chrome animates, which is why text never teleports and any
// viewport-fixed layer always does. Anchoring to the document is the one
// frame that is immune (P26, Anton approved the trade: stars pass by like
// scenery while scrolling instead of holding screen position).
// Look: the pre-canvas ORIGINAL restored verbatim (git history,
// pages/atmosphere.js): 1/2/3px dots, glow blur 4/8/12 at alpha
// 0.2/0.4/0.65, base opacity 0.4/0.65/0.9, drift one viewport in
// 80/50/30s (the page feels like it is rising), twinkle 7/5/3s down to
// 35% of base. Deep water -> sea green -> aquamarine by depth.
// Engine: zero per-frame JS -- drift and twinkle are compositor-run CSS
// keyframe animations on three 1px divs in an absolute document-height
// container; each star is painted twice (y and y - docH) so the
// translateY(0 -> docH) drift loop wraps seamlessly. 28 stars per layer
// per viewport of page height, capped at 150/layer (very long pages get a
// sparser field, never a starless strip). Rebuilds only when width or
// document height actually change -- panel-driven resize events change
// neither, so the field is never re-randomized by scrolling.
// reduced-motion: style.css zeroes all animation durations = static field.
// Hidden tabs: browsers pause CSS animations natively. The black sun is
// pure CSS (style.css #atmo-sun). Stars are an enhancement: without JS
// the page is simply deep space.

(function() {
  if (document.getElementById('atmo-stars')) return;

  // Depth layers: deep water -> sea green -> aquamarine.
  var COLORS = ['#1A4D3E', '#2D8B6F', '#7FFFD4'];
  var GLOW = 'rgba(74,255,160,';
  var GLOW_ALPHA = ['0.2)', '0.4)', '0.65)'];
  // [perViewport, dotSpread(px), glowBlur(px), glowSpread(px), baseOpacity,
  //  driftSecsPerViewport, twinkleSecs]   (dot diameter = 1 + 2*dotSpread)
  var LAYERS = [
    [28, 0,   4,  1, 0.4,  80, 7],   // far: 1px dot, dim, slow
    [28, 0.5, 8,  2, 0.65, 50, 5],   // mid: 2px dot
    [28, 1,  12,  3, 0.9,  30, 3]    // near: 3px dot, bright, fast
  ];
  var CAP = 150;                     // stars per layer

  var container = document.createElement('div');
  container.id = 'atmo-stars';
  document.body.appendChild(container);

  var driftStyle, builtW = 0, builtH = 0;

  function makeStars(count, sz, blur, spread, ci, W, H) {
    var shadows = [];
    var col = COLORS[ci];
    var glow = GLOW + GLOW_ALPHA[ci];
    for (var i = 0; i < count; i++) {
      var x = (Math.random() * W) | 0;
      var y = (Math.random() * H) | 0;
      // star dot + a copy one wrap-band up, so the drift loop is seamless
      shadows.push(x + 'px ' + y + 'px 0 ' + sz + 'px ' + col);
      shadows.push(x + 'px ' + (y - H) + 'px 0 ' + sz + 'px ' + col);
      // glow halo
      shadows.push(x + 'px ' + y + 'px ' + blur + 'px ' + spread + 'px ' + glow);
      shadows.push(x + 'px ' + (y - H) + 'px ' + blur + 'px ' + spread + 'px ' + glow);
    }
    return shadows.join(',');
  }

  // Document height measured with the container collapsed: once built, the
  // container itself holds the page open, so measuring around it is the
  // only way to see the content's true height.
  function measureDocH() {
    container.style.height = '0px';
    return document.documentElement.scrollHeight;
  }

  function build() {
    builtW = document.documentElement.clientWidth;  // EXCLUDES scrollbar
    builtH = measureDocH();
    var viewH = window.innerHeight;
    container.style.width = builtW + 'px';
    container.style.height = builtH + 'px';
    container.innerHTML = '';
    if (driftStyle) driftStyle.remove();

    var css = '';
    LAYERS.forEach(function(L, i) {
      var count = Math.min(CAP, Math.round(L[0] * builtH / viewH));
      var el = document.createElement('div');
      el.style.cssText =
        'position:absolute;top:0;left:0;width:1px;height:1px;border-radius:50%;' +
        'opacity:' + L[4] + ';' +   // static base: twinkle overrides while it
                                    // runs; reduced-motion kills the animation
                                    // and must NOT leave the layer at opacity 1
        'box-shadow:' + makeStars(count, L[1], L[2], L[3], i, builtW, builtH) +
        ';animation:atmo-drift-' + i + ' ' +
        (L[5] * builtH / viewH).toFixed(1) + 's linear infinite,' +
        'atmo-twinkle-' + i + ' ' + L[6] + 's ease-in-out infinite';
      container.appendChild(el);

      css += '@keyframes atmo-drift-' + i +
        '{from{transform:translateY(0)}to{transform:translateY(' + builtH + 'px)}}';
      var hi = L[4], lo = Math.max(hi * 0.35, 0.1);
      css += '@keyframes atmo-twinkle-' + i +
        '{0%,100%{opacity:' + hi + '}50%{opacity:' + lo + '}}';
    });

    driftStyle = document.createElement('style');
    driftStyle.textContent = css;
    document.head.appendChild(driftStyle);
  }

  // Rebuild only on real geometry change: rotation/window resize (width)
  // or content reflow (document height). Mobile panel toggles change
  // neither. GROWTH always rebuilds -- the field must reach the bottom,
  // and pages grow right after the first build when their inline scripts
  // inject demos at DOMContentLoaded (deferred scripts run before that);
  // only shrinkage gets a tolerance, so minor reflows can't re-roll the
  // field.
  function check() {
    var docH = measureDocH();
    if (document.documentElement.clientWidth !== builtW ||
        docH > builtH + 8 ||
        docH < builtH - window.innerHeight / 2) {
      build();
    } else {
      container.style.height = builtH + 'px';  // undo the measure collapse
    }
  }

  build();
  document.addEventListener('DOMContentLoaded', check);
  window.addEventListener('load', check);

  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(check, 250);
  });
})();
