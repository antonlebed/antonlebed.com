// search.js -- client-side full-text search. PAGES is injected by build.py
// from manifest.py (SSOT: the page list lives in ONE place).
(function() {
  var PAGES = [
    {url:'index.html', title:'Home'},
    {url:'tower.html', title:'Tower'},
    {url:'crt.html', title:'CRT'},
    {url:'walls.html', title:'Walls'},
    {url:'measure.html', title:'Measure'},
    {url:'ecc.html', title:'ECC'},
    {url:'automata.html', title:'Automata'},
    {url:'dynamics.html', title:'Dynamics'},
    {url:'prediction.html', title:'Prediction'},
    {url:'build.html', title:'Build'}
  ];

  var index = null;
  var loading = false;

  function stripHTML(html) {
    html = html.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');
    html = html.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');
    html = html.replace(/<nav>[\s\S]*?<\/nav>/gi, '');
    html = html.replace(/<footer>[\s\S]*?<\/footer>/gi, '');
    html = html.replace(/<[^>]+>/g, ' ');
    html = html.replace(/&[a-z]+;/g, ' ');
    html = html.replace(/&#\d+;/g, ' ');
    return html.replace(/\s+/g, ' ').trim();
  }

  function buildIndex(cb) {
    if (index) { cb(); return; }
    if (loading) return;
    loading = true;
    var done = 0;
    index = [];
    PAGES.forEach(function(p) {
      fetch(p.url).then(function(r) { return r.text(); }).then(function(html) {
        index.push({url: p.url, title: p.title, text: stripHTML(html).toLowerCase()});
      }).catch(function() {
        index.push({url: p.url, title: p.title, text: ''});
      }).finally(function() {
        done++;
        if (done === PAGES.length) { loading = false; cb(); }
      });
    });
  }

  function search(q) {
    q = q.toLowerCase();
    var results = [];
    index.forEach(function(page) {
      var pos = page.text.indexOf(q);
      if (pos === -1) return;
      var start = Math.max(0, pos - 30);
      var end = Math.min(page.text.length, pos + q.length + 50);
      var snippet = (start > 0 ? '...' : '') +
        page.text.slice(start, pos) +
        '<mark>' + page.text.slice(pos, pos + q.length) + '</mark>' +
        page.text.slice(pos + q.length, end) +
        (end < page.text.length ? '...' : '');
      results.push({url: page.url, title: page.title, snippet: snippet});
    });
    return results;
  }

  var wrap = document.querySelector('nav .search-wrap');
  if (!wrap) return;

  var input = wrap.querySelector('input');
  var box = wrap.querySelector('.search-results');

  function doSearch() {
    var q = input.value.trim();
    if (!q) { box.style.display = 'none'; return; }
    if (!index) { buildIndex(doSearch); return; }
    var matches = search(q);
    if (!matches.length) {
      box.innerHTML = '<div style="padding:0.5rem 0.6rem;color:var(--fg-dim);font-size:0.8rem">No matches</div>';
    } else {
      box.innerHTML = matches.map(function(m) {
        return '<a href="' + m.url + '"><span class="match-title">' + m.title +
          '</span><br><span class="match-desc">' + m.snippet + '</span></a>';
      }).join('');
    }
    box.style.display = 'block';
  }

  input.addEventListener('input', doSearch);
  input.addEventListener('blur', function() {
    setTimeout(function() { box.style.display = 'none'; }, 200);
  });
  input.addEventListener('focus', function() {
    if (this.value.trim()) doSearch();
  });
})();
