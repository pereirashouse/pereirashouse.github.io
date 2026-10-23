// Comportamentos progressivos: sem JavaScript, todas as seções aparecem em sequência.
document.documentElement.classList.remove('no-js');

// A altura do menu muda quando os links quebram em várias linhas no celular.
(function () {
  var nav = document.querySelector('.topnav');
  if (!nav) return;
  function updateHeight() {
    document.documentElement.style.setProperty('--nav-height', Math.ceil(nav.getBoundingClientRect().height) + 'px');
  }
  updateHeight();
  if (typeof ResizeObserver !== 'undefined') new ResizeObserver(updateHeight).observe(nav);
  else window.addEventListener('resize', updateHeight);
})();

// Abas de modo de leitura (Resumo executivo, Detalhes técnicos, Evidências, Versão didática)
(function () {
  var list = document.querySelector('[role="tablist"]');
  if (!list) return;
  var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
  var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute('aria-controls')); });

  function select(i, focus) {
    tabs.forEach(function (t, j) {
      var on = i === j;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      panels[j].hidden = !on;
    });
    if (focus) tabs[i].focus();
  }

  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () {
      select(i);
      history.replaceState(null, '', '#' + panels[i].id);
    });
    t.addEventListener('keydown', function (e) {
      var n = tabs.length, k = e.key;
      if (k === 'ArrowRight') select((i + 1) % n, true);
      else if (k === 'ArrowLeft') select((i - 1 + n) % n, true);
      else if (k === 'Home') select(0, true);
      else if (k === 'End') select(n - 1, true);
      else return;
      e.preventDefault();
    });
  });

  function fromHash() {
    var id = decodeURIComponent(location.hash.slice(1));
    var el = id && document.getElementById(id);
    var i = 0;
    if (el) panels.forEach(function (p, j) { if (p === el || p.contains(el)) i = j; });
    select(i);
    if (el && el !== panels[i]) el.scrollIntoView();
  }
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();

// Filtros do arquivo de projetos
(function () {
  var bar = document.querySelector('.filters');
  if (!bar) return;
  bar.hidden = false;
  var items = Array.prototype.slice.call(document.querySelectorAll('.arch > li'));
  var count = document.getElementById('arch-count');
  var buttons = Array.prototype.slice.call(bar.querySelectorAll('button'));

  function apply(tag) {
    var shown = 0;
    items.forEach(function (li) {
      var ok = tag === 'todos' || (' ' + li.dataset.tags + ' ').indexOf(' ' + tag + ' ') > -1;
      li.hidden = !ok;
      if (ok) shown++;
    });
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.f === tag ? 'true' : 'false'); });
    if (count) count.textContent = shown + (shown === 1 ? ' projeto exibido' : ' projetos exibidos');
  }
  buttons.forEach(function (b) { b.addEventListener('click', function () { apply(b.dataset.f); }); });
  apply('todos');

  // Link direto para um item do arquivo abre os detalhes dele
  function openFromHash() {
    var el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (!el || !el.closest('.arch')) return;
    if (el.hidden) apply('todos');
    var d = el.querySelector('details');
    if (d) d.open = true;
    el.scrollIntoView();
  }
  window.addEventListener('hashchange', openFromHash);
  openFromHash();
})();
