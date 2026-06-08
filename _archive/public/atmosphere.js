// atmosphere.js — starfield + black sun + overlay scrollbar
// Visual reference: webax/pages/core.ax celestial theatre

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

  // Static CSS
  var staticCss =
    '#atmo-stars{position:fixed;top:0;left:0;width:100%;height:100%;overflow:hidden;pointer-events:none;z-index:-2}';

  // Sun: 80px, gradient core, 3-layer corona, 21s pulse
  staticCss += '#atmo-sun{position:absolute;top:20px;left:30px;width:80px;height:80px;border-radius:50%;' +
    'background:radial-gradient(circle at 50% 50%,#0a0a0f 0%,#0a0a0f 50%,#1a0800 68%,#4a1500 80%,#8B2500 90%,#CC5500 96%,#FF8C00 100%);' +
    'box-shadow:0 0 40px 14px rgba(255,60,0,0.3),0 0 90px 35px rgba(255,120,0,0.12),0 0 160px 65px rgba(255,80,0,0.05);' +
    'pointer-events:none;z-index:-1;animation:atmo-pulse 21s ease-in-out infinite}';
  staticCss += '@keyframes atmo-pulse{' +
    '0%,100%{box-shadow:0 0 30px 10px rgba(255,60,0,0.35),0 0 70px 30px rgba(255,120,0,0.15),0 0 140px 60px rgba(255,80,0,0.06)}' +
    '50%{box-shadow:0 0 45px 18px rgba(255,80,0,0.5),0 0 100px 45px rgba(255,140,0,0.22),0 0 180px 80px rgba(255,100,0,0.09)}}';

  // Scrollbar
  staticCss += 'html{position:relative;overflow-y:scroll;overflow-y:overlay;scrollbar-width:thin;scrollbar-color:#2a2a40 transparent}';
  staticCss += '::-webkit-scrollbar{width:8px;background:transparent}';
  staticCss += '::-webkit-scrollbar-thumb{background:#2a2a40;border-radius:4px}';
  staticCss += '::-webkit-scrollbar-thumb:hover{background:#3a3a55}';

  var style = document.createElement('style');
  style.textContent = staticCss;
  document.head.appendChild(style);

  document.body.appendChild(container);
  buildStars();

  // Sun (in page flow, scrolls away)
  var sun = document.createElement('div');
  sun.id = 'atmo-sun';
  document.body.insertBefore(sun, document.body.firstChild);

  // Regenerate on resize
  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(buildStars, 250);
  });
})();
