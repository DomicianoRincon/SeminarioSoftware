// Apertura (slides 1 a 3)
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS;

  function piece(name, soft, border, strong) {
    return '<div style="padding:16px 20px;border-radius:12px;background:' + soft + ';border:2px solid ' + border + ';' +
      'font-family:ui-monospace,Menlo,Consolas,monospace;font-size:22px;font-weight:700;color:' + strong + ';text-align:center;">' + name + '</div>';
  }

  // 1 · Portada
  window.SLIDES.push(icesi.titleSlideA(
    'Pantallas con componentes',
    'Scaffold, SafeArea y layout<br>' +
    '<span class="slide-footer-tag">Seminario de Ingeniería de Software &middot; Universidad Icesi</span>'
  ));

  // 2 · El recorrido de hoy
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'El recorrido de hoy',
    '<div style="margin-top:70px;">' + H.bigPipeline([
      { icon: I.screen, label: 'Scaffold y SafeArea', sub: 'el andamio<br>de una pantalla' },
      { icon: I.layout, label: 'Las dos barras', sub: 'AppBar y<br>BottomNavigationBar' },
      { icon: I.brick, label: 'Container y Padding', sub: 'aire y cajas' },
      { icon: I.map, label: 'Expanded y scroll', sub: 'cuando el contenido<br>no cabe' },
      { icon: I.tool, label: 'Taller', sub: 'la pantalla de perfil' }
    ]) + '</div>'
  ), 'Cuatro bloques cortos, una receta para armar cualquier pantalla y un taller. Todo se prueba sobre ProfileScreen, que se crea en el primer bloque y se termina en el taller.'));

  // 3 · Lo que ya tienes
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Lo que ya tienes',
    '<div style="margin-top:36px;display:grid;grid-template-columns:repeat(4,1fr);gap:22px;">' +
    piece('ProfileInfo', '#EEF1FF', '#A9B4F2', '#4453C9') +
    piece('StatsRow', '#F4EBFF', '#C9A6EE', '#7439B8') +
    piece('StatCard', '#FFF3DC', '#F0C572', '#A96C05') +
    piece('PrimaryButton', '#E3F6F3', '#86D3CA', '#0F8478') +
    piece('SecondaryButton', '#E8F6E3', '#9FD68D', '#3A8235') +
    piece('ContactCard', '#FFEBEF', '#F3A3B2', '#C2354F') +
    piece('ChatItem', '#EFF1F5', '#C4CBD8', '#556074') +
    '</div>' +
    '<p style="margin-top:56px;text-align:center;font-size:26px;">Siete componentes en <strong>lib/components/</strong> &middot; hoy se encajan en una pantalla</p>'
  ), 'En la sesión anterior hicieron siete componentes y los probaron dentro de un Center. Quien no los tenga terminados los completa primero con el Taller de componentes: son el insumo de hoy.'));
})();
