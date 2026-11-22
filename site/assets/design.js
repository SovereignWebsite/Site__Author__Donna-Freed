// Choose a design: five looks for the same pages. First-party, no network, no cookies.
// The choice is kept in this browser only (localStorage, if allowed) and in ?design=1..5 so it can be shared.
(function () {
  var html = document.documentElement, KEY = 'donna-freed-design', pick = null;
  try { var q = new URLSearchParams(location.search).get('design'); if (/^[1-5]$/.test(q)) pick = q; } catch (e) {}
  if (!pick) { try { var s = localStorage.getItem(KEY); if (/^[1-5]$/.test(s)) pick = s; } catch (e) {} }
  function apply(n, save) {
    html.setAttribute('data-design', n);
    if (save) { try { localStorage.setItem(KEY, n); } catch (e) {} }
    var links = document.querySelectorAll('.designs a[data-design]');
    for (var i = 0; i < links.length; i++) {
      if (links[i].getAttribute('data-design') === n) links[i].setAttribute('aria-current', 'true');
      else links[i].removeAttribute('aria-current');
    }
  }
  function ready() {
    apply(pick || '1', false);
    var links = document.querySelectorAll('.designs a[data-design]');
    for (var i = 0; i < links.length; i++) {
      links[i].addEventListener('click', function (ev) { ev.preventDefault(); apply(this.getAttribute('data-design'), true); });
    }
  }
  if (pick) html.setAttribute('data-design', pick);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready); else ready();
})();
