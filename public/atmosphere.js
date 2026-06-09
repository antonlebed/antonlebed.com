// atmosphere.js — starfield (sun + scrollbar styles now in style.css)

(function() {
  if (document.getElementById('atmo-stars')) return;

  var H = window.innerHeight;
  var W = window.innerWidth;

  // Green/aquamarine palette — single color family, depth-graded
  // Far: deep water. Mid: sea green. Near: aquamarine.
  var COLORS = ['#1A4D3E', '#2D8B6F', '#7FFFD4'];
  var GLOW_COLOR = 'rgba(74,255,160,';
  var GLOW_ALPHA = ['0.2)', '0.4)', '0.65)'];

  // [count, dotSpread(px), glowBlur(px), glowSpread(px), baseOpacity, driftSeconds, twinkleSeconds]
  // dotSpread: 0=1px dot, 0.5=2px, 1=3px (spread adds to each side of the 1px element)
  var layers = [
    [28, 0,   4,  1, 0.4, 80, 7],   // far: 1px dot, dim, slow
    [28, 0.5, 8,  2, 0.65, 50, 5],  // mid: 2px dot
    [28, 1,  12,  3, 0.9, 30, 3]    // near: 3px dot, bright, fast
  ];

  function makeStars(count, sz, blur, spread, colorIdx, W, H) {
    var shadows = [];
    var col = COLORS[colorIdx];
    var glow = GLOW_COLOR + GLOW_ALPHA[colorIdx];
    for (var i = 0; i < count; i++) {
      var x = (Math.random() * W) | 0;
      var y = (Math.random() * H) | 0;
      // Star dot
      shadows.push(x + 'px ' + y + 'px 0 ' + sz + 'px ' + col);
      shadows.push(x + 'px ' + (y - H) + 'px 0 ' + sz + 'px ' + col);
      // Glow halo
      shadows.push(x + 'px ' + y + 'px ' + blur + 'px ' + spread + 'px ' + glow);
      shadows.push(x + 'px ' + (y - H) + 'px ' + blur + 'px ' + spread + 'px ' + glow);
    }
    return shadows.join(',');
  }

  var container = document.createElement('div');
  container.id = 'atmo-stars';
  var driftStyle;

  function buildStars() {
    H = window.innerHeight;
    W = window.innerWidth;
    container.innerHTML = '';
    if (driftStyle) driftStyle.remove();

    var css = '';
    layers.forEach(function(L, i) {
      var el = document.createElement('div');
      el.className = 'atmo-layer';
      el.style.cssText = 'position:absolute;top:0;left:0;width:1px;height:1px;border-radius:50%;' +
        'box-shadow:' + makeStars(L[0], L[1], L[2], L[3], i, W, H) +
        ';animation:atmo-drift-' + i + ' ' + L[5] + 's linear infinite,' +
        'atmo-twinkle-' + i + ' ' + L[6] + 's ease-in-out infinite';
      container.appendChild(el);

      css += '@keyframes atmo-drift-' + i +
        '{from{transform:translateY(0)}to{transform:translateY(' + H + 'px)}}';

      var hi = L[4], lo = Math.max(hi * 0.35, 0.1);
      css += '@keyframes atmo-twinkle-' + i +
        '{0%,100%{opacity:' + hi + '}50%{opacity:' + lo + '}}';
    });

    driftStyle = document.createElement('style');
    driftStyle.textContent = css;
    document.head.appendChild(driftStyle);
  }

  // Sun + scrollbar + container CSS now in style.css (loads synchronously, no flash).
  // atmosphere.js only creates the starfield layers.

  document.body.appendChild(container);
  buildStars();

  // Sun: use existing HTML div if present, otherwise create
  if (!document.getElementById('atmo-sun')) {
    var sun = document.createElement('div');
    sun.id = 'atmo-sun';
    document.body.insertBefore(sun, document.body.firstChild);
  }

  // Regenerate on resize
  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(buildStars, 250);
  });
})();
