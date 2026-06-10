// atmosphere.js -- starfield as pure CSS box-shadows, ANCHORED TO THE
// VIEWPORT. Resurrected from the pre-canvas original (git history:
// pages/atmosphere.js) after the canvas version proved unfixable on mobile:
// a canvas needs a JS loop that samples geometry (scrollY/innerHeight) and
// repaints, which means guessing how the browser animates its URL bar --
// and every guess (page anchor, 100vh band, bottom anchor, settle-glide)
// still moved stars on a real phone. This version samples NOTHING: stars
// are box-shadows on three 1px divs inside a fixed 100vh container, drift
// and twinkle are compositor-run CSS keyframe animations, and the only JS
// is the one-time build. During chrome animation the fixed layer behaves
// like every site's fixed header -- native platform behavior, no JS to
// fight it.
// Fixes over the original:
//   - band height = the container's own 100vh (the mobile URL bar cannot
//     change it), not innerHeight measured at load (bar-state-dependent);
//   - rebuild only when WIDTH or 100vh actually change (rotation, real
//     window resize) -- bar-driven resize events change neither, so the
//     field is never re-randomized by scrolling;
//   - clientWidth, not innerWidth (no scrollbar overlap).
// Look (P21-tuned, carried over from the canvas version): 28 stars/layer,
// deep water -> sea green -> aquamarine by depth, cores ~2/3/4px, tight
// glow; drift one band in 80/50/30s (the page feels like it is rising);
// twinkle 7/5/3s between base opacity (0.5/0.7/0.9) and 35% of it.
// Each star is painted twice (y and y-H) so the translateY(0 -> H) drift
// loop wraps seamlessly.
// reduced-motion: style.css zeroes all animation durations = static field.
// Hidden tabs: browsers pause CSS animations natively. The black sun is
// pure CSS (style.css #atmo-sun). Stars are an enhancement: without JS the
// page is simply deep space.

(function() {
  if (document.getElementById('atmo-stars')) return;

  // Depth layers: deep water -> sea green -> aquamarine.
  var COLORS = ['#1A4D3E', '#2D8B6F', '#7FFFD4'];
  var GLOW = 'rgba(74,255,160,';
  var GLOW_ALPHA = ['0.30)', '0.45)', '0.60)'];
  // [count, dotSpread(px), glowBlur(px), glowSpread(px), baseOpacity,
  //  driftSecsPerBand, twinkleSecs]   (dot diameter = 1 + 2*dotSpread)
  var LAYERS = [
    [28, 0.5, 4, 1, 0.5, 80, 7],   // far: ~2px dot, dim, slow
    [28, 1.0, 6, 2, 0.7, 50, 5],   // mid: ~3px dot
    [28, 1.7, 9, 3, 0.9, 30, 3]    // near: ~4px dot, bright, fast
  ];

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
      // star dot + a copy one band up, so the drift loop wraps seamlessly
      shadows.push(x + 'px ' + y + 'px 0 ' + sz + 'px ' + col);
      shadows.push(x + 'px ' + (y - H) + 'px 0 ' + sz + 'px ' + col);
      // glow halo
      shadows.push(x + 'px ' + y + 'px ' + blur + 'px ' + spread + 'px ' + glow);
      shadows.push(x + 'px ' + (y - H) + 'px ' + blur + 'px ' + spread + 'px ' + glow);
    }
    return shadows.join(',');
  }

  function build() {
    builtW = document.documentElement.clientWidth;  // EXCLUDES scrollbar
    builtH = container.clientHeight;                // 100vh: bar-stable
    container.innerHTML = '';
    if (driftStyle) driftStyle.remove();

    var css = '';
    LAYERS.forEach(function(L, i) {
      var el = document.createElement('div');
      el.style.cssText =
        'position:absolute;top:0;left:0;width:1px;height:1px;border-radius:50%;' +
        'box-shadow:' + makeStars(L[0], L[1], L[2], L[3], i, builtW, builtH) +
        ';animation:atmo-drift-' + i + ' ' + L[5] + 's linear infinite,' +
        'atmo-twinkle-' + i + ' ' + L[6] + 's ease-in-out infinite';
      container.appendChild(el);

      css += '@keyframes atmo-drift-' + i +
        '{from{transform:translateY(0)}to{transform:translateY(' + builtH + 'px)}}' +
        '@keyframes atmo-twinkle-' + i +
        '{0%,100%{opacity:' + L[4] + '}50%{opacity:' + (L[4] * 0.35).toFixed(3) + '}}';
    });

    driftStyle = document.createElement('style');
    driftStyle.textContent = css;
    document.head.appendChild(driftStyle);
  }

  build();

  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      // mobile URL-bar toggles change neither clientWidth nor 100vh --
      // only rotation or a real window resize gets past this guard
      if (document.documentElement.clientWidth !== builtW ||
          container.clientHeight !== builtH) build();
    }, 250);
  });
})();
